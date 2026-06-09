#!/usr/bin/env python3
"""build_corpus.py — turn .srt files (+ videos) into the corpus the site reads.

This is the BUILD STEP. It runs offline, on the Python standard library only
(no pip install), and emits two files into outputs/:

    outputs/corpus.json     — the canonical data model (pretty-printed)
    outputs/corpus-data.js  — the same object as `window.CORPUS = {...};`
                              so the static site can load it from file://
                              (browsers block fetch() of local .json).

The front-end consumes outputs/site/corpus-data.js. We write to outputs/ to avoid
colliding with the site author; copy outputs/corpus-data.js -> outputs/site/ when ready:

    cp outputs/corpus-data.js outputs/site/corpus-data.js

PIPELINE (per the handoff brief):
  1. Parse each .srt -> utterance rows, timestamps preserved (lib/srt.py).
     (If a video has no .srt, generate one first with lib/stt.py — separate step.)
  2. Tokenize + lemmatize each utterance (lib/lemmatize.py; pluggable per lang).
  3. Build the inverted indexes (lemma -> utterances, surface form -> utterances)
     and lemma-frequency table.
  4. Score each utterance's difficulty (for the "easy utterances" view).
  5. Emit corpus.json (+ the corpus-data.js wrapper).

USAGE
  Single video (local):
    python3 operations/scripts/build_corpus.py \
        --srt inputs/madeleine.srt \
        --video inputs/madeleine.mp4 \
        --title "Just Do It"

  Single video (YouTube):
    python3 operations/scripts/build_corpus.py \
        --srt inputs/labeouf.en.srt --youtube-id ZXsQAXx_ao0 \
        --title "Just Do It (YouTube)" --dedupe-rolling

  Many videos at once:
    python3 operations/scripts/build_corpus.py --manifest inputs/corpus.manifest.json
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

# Make `lib` importable whether run as a script or a module.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import srt as srtlib          # noqa: E402
from lib import diarize as diarizelib  # noqa: E402
from lib.lemmatize import get_lemmatizer  # noqa: E402

# this file lives at <recipe>/operations/scripts/build_corpus.py
RECIPE_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUTS_DIR = RECIPE_ROOT / "outputs"
SITE_DIR = OUTPUTS_DIR / "site"          # the website lives at outputs/site/


# --------------------------------------------------------------------------- #
# Video sources
# --------------------------------------------------------------------------- #

class VideoSpec:
    """One video to ingest: where its transcript is, and how the site plays it.

    The transcript may be a `.srt` (the canonical ingest path) OR a diarized
    `.json` from the transcriber — both become the same timestamped cues, so the
    diarized data's sub-second precision and speaker labels are preserved.
    """

    def __init__(self, srt=None, diarize_json=None, title=None, video=None,
                 youtube_id=None, source_id=None, lang="en",
                 dedupe_rolling=False, scene_meta=None):
        if not srt and not diarize_json:
            raise ValueError("each video needs an 'srt' or a 'diarize_json' source")
        self.srt = Path(srt) if srt else None
        self.diarize_json = Path(diarize_json) if diarize_json else None
        self.video = Path(video) if video else None
        self.youtube_id = youtube_id
        self.lang = lang
        self.dedupe_rolling = dedupe_rolling
        self.scene_meta = scene_meta or {}
        # source_id: explicit, else from the video/transcript basename.
        transcript = self.video or self.srt or self.diarize_json
        stem = re.sub(r"\.(en|ar|[a-z]{2})$", "", transcript.stem)  # drop trailing .en
        self.source_id = source_id or stem
        self.title = title or self.source_id

    def load_cues(self):
        """Read this video's transcript into timestamped cues, whatever its form."""
        if self.diarize_json:
            if not self.diarize_json.exists():
                raise FileNotFoundError(f"diarize JSON not found: {self.diarize_json}")
            return diarizelib.parse_diarize_json(
                self.diarize_json.read_text(encoding="utf-8"))
        if not self.srt.exists():
            raise FileNotFoundError(f"SRT not found: {self.srt}")
        cues = srtlib.parse_srt(self.srt.read_text(encoding="utf-8"))
        if self.dedupe_rolling:
            cues = srtlib.dedupe_rolling(cues)
        return cues

    @property
    def transcript_name(self):
        return (self.srt or self.diarize_json).name

    @property
    def source_type(self) -> str:
        return "youtube" if self.youtube_id else "local"

    def file_for_site(self):
        """Local video path RELATIVE TO the site dir (outputs/site/).

        The site loads `<video src=...>` from outputs/site/, so we emit a path
        relative to that directory (e.g. ../../inputs/madeleine.mp4).
        """
        if self.source_type != "local" or not self.video:
            return None
        return os.path.relpath(self.video.resolve(), SITE_DIR).replace(os.sep, "/")

    def duration(self):
        if self.source_type == "local" and self.video and self.video.exists():
            return _ffprobe_duration(self.video)
        return None


def _ffprobe_duration(path: Path):
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(path)],
            capture_output=True, text=True, timeout=30,
        )
        return round(float(out.stdout.strip()), 3)
    except (subprocess.SubprocessError, ValueError, FileNotFoundError):
        return None


# --------------------------------------------------------------------------- #
# Build
# --------------------------------------------------------------------------- #

def build_corpus(specs, speaker_meta=None):
    speaker_meta = speaker_meta or {}

    videos, speakers_seen, utterances = [], {}, []

    for spec in specs:
        cues = spec.load_cues()
        lem = get_lemmatizer(spec.lang)

        spk_ids_for_video = []
        for line_no, cue in enumerate(cues, start=1):
            speaker_id = _speaker_id(spec.source_id, cue.speaker)
            if speaker_id not in speakers_seen:
                speakers_seen[speaker_id] = _speaker_record(
                    speaker_id, cue.speaker, speaker_meta.get(speaker_id, {}))
            if speaker_id not in spk_ids_for_video:
                spk_ids_for_video.append(speaker_id)

            tokens = lem.tokenize(cue.text)
            lemmas = lem.lemmatize(cue.text)
            utterances.append({
                "utterance_id": f"{spec.source_id}_{line_no:04d}",
                "source_id": spec.source_id,
                "line": line_no,
                "speaker_id": speaker_id,
                "start": round(cue.start, 3),   # straight from the SRT — never lost
                "end": round(cue.end, 3),
                "text": cue.text,
                "tokens": tokens,
                "lemmas": lemmas,
                # difficulty filled in after corpus-wide frequencies are known
            })

        videos.append({
            "source_id": spec.source_id,
            "title": spec.title,
            "source_type": spec.source_type,
            "file": spec.file_for_site(),
            "youtube_id": spec.youtube_id,
            "duration": spec.duration(),
            "speakers": spk_ids_for_video,
            "scene_meta": spec.scene_meta,
        })

    lemma_index, form_index, lemma_freq = _build_indexes(utterances)
    _score_difficulty(utterances, lemma_freq)

    speakers = list(speakers_seen.values())
    return {
        "meta": {
            "video_count": len(videos),
            "utterance_count": len(utterances),
            "lemma_count": len(lemma_freq),
            "generated_from": [s.transcript_name for s in specs],
        },
        "videos": videos,
        "speakers": speakers,
        "utterances": utterances,
        "lemma_index": lemma_index,
        "form_index": form_index,
        "lemma_freq": lemma_freq,
    }


def _speaker_id(source_id, label):
    """Namespace speaker ids by video so 'A' in two videos doesn't collide."""
    return f"{source_id}:{label}" if label else f"{source_id}:_"


def _speaker_record(speaker_id, label, meta):
    rec = {
        "speaker_id": speaker_id,
        "label": meta.get("label") or (f"Speaker {label}" if label else "Unlabeled"),
        "gender": meta.get("gender"),
        "age_group": meta.get("age_group"),
        "region": meta.get("region"),
        "role": meta.get("role"),
    }
    return rec


def _build_indexes(utterances):
    lemma_index, form_index, lemma_freq = {}, {}, {}
    for u in utterances:
        uid = u["utterance_id"]
        for lemma in dict.fromkeys(u["lemmas"]):       # dedupe within an utterance
            lemma_index.setdefault(lemma, []).append(uid)
        for form in dict.fromkeys(u["tokens"]):
            form_index.setdefault(form, []).append(uid)
        for lemma in u["lemmas"]:                       # frequency counts every token
            lemma_freq[lemma] = lemma_freq.get(lemma, 0) + 1
    # Sort frequency table high->low for a stable, useful ordering in the site.
    lemma_freq = dict(sorted(lemma_freq.items(), key=lambda kv: (-kv[1], kv[0])))
    return lemma_index, form_index, lemma_freq


# Closed-class words that shouldn't make an utterance look "hard" if rare.
_STOP = {
    "the", "a", "an", "and", "or", "but", "so", "if", "of", "to", "in", "on",
    "at", "for", "with", "as", "by", "be", "is", "are", "was", "were", "do",
    "you", "i", "it", "he", "she", "they", "we", "this", "that", "your", "my",
    "not", "no", "yes", "just", "now",
}


def _score_difficulty(utterances, lemma_freq):
    """Per-utterance difficulty in 0..1 (lower = easier). Drives the 'easy' view.

    Easy = short, made of common words. We combine mean lemma rarity (how
    uncommon its content words are, relative to the corpus max) with a mild
    length penalty.
    """
    max_freq = max(lemma_freq.values()) if lemma_freq else 1
    log_max = math.log(max_freq + 1)
    for u in utterances:
        content = [l for l in u["lemmas"] if l not in _STOP] or u["lemmas"]
        if content:
            rarities = []
            for lemma in content:
                f = lemma_freq.get(lemma, 1)
                # rarity in 0..1: common word -> ~0, hapax -> ~1
                rarities.append(1.0 - (math.log(f + 1) / log_max if log_max else 0))
            mean_rarity = sum(rarities) / len(rarities)
        else:
            mean_rarity = 0.0
        length_penalty = min(len(u["tokens"]) / 20.0, 1.0)
        difficulty = 0.7 * mean_rarity + 0.3 * length_penalty
        u["difficulty"] = round(min(max(difficulty, 0.0), 1.0), 3)


# --------------------------------------------------------------------------- #
# Emit
# --------------------------------------------------------------------------- #

def emit(corpus, outputs_dir=OUTPUTS_DIR):
    outputs_dir.mkdir(parents=True, exist_ok=True)
    json_path = outputs_dir / "corpus.json"
    js_path = outputs_dir / "corpus-data.js"

    json_text = json.dumps(corpus, ensure_ascii=False, indent=2)
    json_path.write_text(json_text + "\n", encoding="utf-8")

    banner = (
        "// Generated by operations/scripts/build_corpus.py — do not edit by hand.\n"
        "// Copy this file to outputs/site/corpus-data.js for the website to load it\n"
        "// (a JS wrapper, not raw JSON, so the site works from file://).\n"
    )
    js_path.write_text(banner + "window.CORPUS = " + json_text + ";\n",
                       encoding="utf-8")
    return json_path, js_path


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def specs_from_manifest(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    base = path.parent
    default_lang = data.get("lang", "en")
    def _resolve(rel):
        if not rel:
            return None
        return rel if Path(rel).is_absolute() else (base / rel)

    specs = []
    for v in data["videos"]:
        specs.append(VideoSpec(
            srt=_resolve(v.get("srt")),
            diarize_json=_resolve(v.get("diarize_json")),
            title=v.get("title"), video=_resolve(v.get("video")),
            youtube_id=v.get("youtube_id"), source_id=v.get("source_id"),
            lang=v.get("lang", default_lang),
            dedupe_rolling=v.get("dedupe_rolling", False),
            scene_meta=v.get("scene_meta"),
        ))
    return specs, data.get("speakers", {})


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--manifest", help="JSON manifest describing multiple videos")
    p.add_argument("--srt", help="path to one .srt file")
    p.add_argument("--diarize-json", help="path to one diarized-transcript .json "
                   "(precise timestamps + speaker labels; used instead of --srt)")
    p.add_argument("--video", help="local video file (Mode A)")
    p.add_argument("--youtube-id", help="YouTube id (Mode B)")
    p.add_argument("--title", help="human-readable video title")
    p.add_argument("--source-id", help="override the source id (default: basename)")
    p.add_argument("--lang", default="en", help="ISO 639 language code (default: en)")
    p.add_argument("--dedupe-rolling", action="store_true",
                   help="collapse YouTube-style rolling auto-captions")
    p.add_argument("--out", default=str(OUTPUTS_DIR),
                   help="output directory (default: outputs/)")
    args = p.parse_args(argv)

    if args.manifest:
        specs, speaker_meta = specs_from_manifest(Path(args.manifest))
    elif args.srt or args.diarize_json:
        specs = [VideoSpec(
            srt=args.srt, diarize_json=args.diarize_json,
            title=args.title, video=args.video,
            youtube_id=args.youtube_id, source_id=args.source_id,
            lang=args.lang, dedupe_rolling=args.dedupe_rolling,
        )]
        speaker_meta = {}
    else:
        p.error("provide --manifest, --srt, or --diarize-json")

    corpus = build_corpus(specs, speaker_meta)
    json_path, js_path = emit(corpus, Path(args.out))

    m = corpus["meta"]
    print("=== corpus built ===")
    print(f"  videos      : {m['video_count']}")
    print(f"  utterances  : {m['utterance_count']}")
    print(f"  lemmas      : {m['lemma_count']}")
    print(f"  -> {json_path}")
    print(f"  -> {js_path}")
    print(f"\nNext: cp {js_path.relative_to(RECIPE_ROOT)} outputs/site/corpus-data.js && open outputs/site/index.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
