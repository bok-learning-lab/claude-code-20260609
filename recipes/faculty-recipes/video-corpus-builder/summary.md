# Video Corpus Builder

A recipe for turning **videos + subtitles** into a **searchable, video-linked
language corpus**: a website where a learner searches a word, sees every
utterance that contains it (in context, with who said it and when), and clicks to
play the video at that exact moment.

This single document covers both **what is in this folder** and **how we built
it** with Claude Code. It is written for faculty who want to see the process, not
just the finished product.

---

## What this project is

It grew out of a faculty "Project as Recipe" card from the Summer of Claude
workshop ([inputs/video-corpus-builder.jpg](inputs/video-corpus-builder.jpg),
transcribed in [inputs/video-corpus-builder.md](inputs/video-corpus-builder.md)).
The ask, in the faculty member's words: *auto-generate subtitles, build a
database for NLP analysis that keeps speaker and scene data, group word forms to
headwords, do word-frequency analysis to find "easy" utterances, and ship a
dictionary website — search a word, see its utterances, click to a video clip.*

The reference design is the **CORAAL Explorer** (Corpus of Regional African
American Language): search → KWIC concordance → click a hit → the media player
seeks to that utterance's timestamp. We keep that pattern and add the two things
a *learner-facing* tool needs and CORAAL lacks:

1. **Lemma-aware search.** CORAAL matches literal strings, so "go" misses "going"
   and "went". We map every surface form to its headword, so searching a
   dictionary form finds all of its real utterances.
2. **A frequency / "easy utterance" view.** Rank words by how common they are and
   surface short, high-frequency utterances for beginners.

See [inputs/corall-explorer-reference.md](inputs/corall-explorer-reference.md)
for the reference write-up and [inputs/handoff.md](inputs/handoff.md) for the
build brief and full data model.

### Two deployment modes, one codebase

Each video declares a `source_type`; search and concordance are identical, only
the player branches.

- **Mode A — Local videos** (the workshop demo). Files on disk; runs offline.
  Seeded here with `inputs/madeleine.mp4`.
- **Mode B — Hosted / YouTube.** Videos embedded from YouTube. Seeded here with
  the YouTube original of the same speech (`inputs/labeouf.mp4`, embedded by its
  YouTube id) so both player paths are exercised from one corpus.

---

## What's in this folder

```
video-corpus-builder/
  CLAUDE.md          project instructions Claude loads on session start
  summary.md         this file
  inputs/            source material (read-only to the pipeline)
  operations/
    scripts/         the pipeline, scripts, and tests
    prompts/         demonstration prompts for building a project like this
  outputs/           generated data (rebuildable)
    site/            the static website
```

### inputs/ — source material

- [video-corpus-builder.jpg](inputs/video-corpus-builder.jpg) / [.md](inputs/video-corpus-builder.md) — the original handwritten recipe card + transcription
- [handoff.md](inputs/handoff.md) — the build brief: data model, pipeline phases, gotchas
- [corall-explorer-reference.md](inputs/corall-explorer-reference.md) — the CORAAL Explorer reference UX
- [corpus.manifest.json](inputs/corpus.manifest.json) — lists the videos + speakers for a build
- **Mode A clip (Madeleine Woods):** `madeleine.mp4`, `madeleine.srt` (ms-precision subtitles), `madeleine.json` (the diarizer's precise output), `madeleine_diarize.md` (readable transcript)
- **Mode B clip (Shia LaBoeuf, YouTube original):** `labeouf.mp4`, `labeouf.srt`, `labeouf.json`, `labeouf_diarize.md`

Each clip has the same four files — a clean template for adding more videos.

### operations/scripts/ — the pipeline and scripts

Python standard-library only (no `pip install`), plus shell scripts.
(The companion `operations/prompts/` folder holds the demonstration prompts for
building a project like this — see [operations/prompts/README.md](operations/prompts/README.md).)

- [build_corpus.py](operations/scripts/build_corpus.py) — the build step: subtitles (+video) → `outputs/corpus.json`
- [download_youtube.sh](operations/scripts/download_youtube.sh) — pull a video + captions from YouTube with `yt-dlp`
- [transcribe_parallel](operations/scripts/transcribe_parallel) — diarizing speech-to-text (OpenAI) → a transcript for a bare video
- [diarize_to_srt.py](operations/scripts/diarize_to_srt.py) — convert a diarized `.json` into a millisecond-precision `.srt`
- [test_pipeline.py](operations/scripts/test_pipeline.py) — unit tests (timestamp round-trip, SRT parsing, dedupe, lemmas, JSON ingest)
- lib/ — shared modules: [srt.py](operations/scripts/lib/srt.py), [diarize.py](operations/scripts/lib/diarize.py), [lemmatize.py](operations/scripts/lib/lemmatize.py) (English default + Levantine Arabic slot), [stt.py](operations/scripts/lib/stt.py) (engine interface + Arabic slot)
- *(bonus)* [respace_monologue.py](operations/scripts/respace_monologue.py) + `labeouf_respaced.txt`, `monologue.html` — a side experiment that reflows a transcript as a monologue, preserving the performer's pauses as text

### outputs/ — generated data

- `corpus.json` — the canonical data model the site is built against
- `corpus-data.js` — the same object as `window.CORPUS = {...}`, so the site can load it from `file://` (browsers block `fetch()` of a local `.json`)

### outputs/site/ — the website

Vanilla HTML/CSS/JS that runs by double-click from `file://` (no server, no build
step): search + lemma toggle + filters, KWIC concordance, the video player that
branches local vs YouTube and seeks to each utterance's timestamp, transcript
highlighting, a shareable deep-link hash, and the frequency / "easy utterances"
view. It reads `outputs/site/corpus-data.js` (copied from `outputs/corpus.json`'s
sibling `corpus-data.js` after a build).

---

## How we built it

The rhythm matters more than any single prompt: **agree on the artifact, gather
real material, get the data clean, build the machine that transforms it, and only
then build the thing people see.**

1. **From card to brief.** Before any code, we turned the handwritten card into
   the written brief in `inputs/` (`handoff.md` + the CORAAL reference), so Claude
   and the humans shared one picture of the target. This is the highest-leverage
   habit — spend the first prompts agreeing on the artifact, not generating it.

2. **Get the raw material.** A faculty member supplied a local clip; we asked
   Claude to write `download_youtube.sh` to pull the YouTube original.

3. **Get clean transcripts.** YouTube's auto-captions came down garbled (rolling
   duplicates, 10-millisecond junk cues), so we ran each video through the
   diarizing transcriber instead, getting clean segments with sub-second times
   and speaker labels. Precision matters: the timestamps are how the site seeks
   the video. We learned this directly — an early hand-typed subtitle file
   rounded to whole seconds and the clips landed slightly off, so we now generate
   subtitles straight from the transcriber's JSON with `diarize_to_srt.py`. A
   test asserts the `.srt` and `.json` ingest paths produce identical timestamps.

4. **Build the pipeline.** `build_corpus.py` parses subtitles into timestamped
   utterances, lemmatizes them (so "go" finds "going"/"went"), builds the
   inverted indexes and frequency table, scores utterance difficulty, and emits
   `corpus.json`. The language-specific stages (lemmatizer, speech-to-text) sit
   behind clean interfaces, so swapping in a **Levantine Arabic** analyzer is a
   one-file change that never touches the website. Those slots are stubbed and
   documented.

5. **Build the site, in parallel.** While one Claude session built the pipeline,
   a second built the website at the same time. We coordinated them with one
   trick: we froze the shape of `corpus.json` up front and handed the site
   session a small stub to develop against. Because both agreed on that one
   contract, they never collided — the pipeline session stayed in `operations/`
   and `outputs/`, the site session in `outputs/site/`. When both finished, the real data
   dropped in with no code changes.

6. **Tidy up.** We gave the videos human names (`madeleine.*`, `labeouf.*`), set
   the real speaker labels, deleted intermediate audio and stray files, and added
   a `.gitignore`.

Claude wrote the scripts, ran the transcriptions, and assembled the site; the
humans supplied the videos, made the naming and design calls, and kept asking "is
this precise enough?" That back-and-forth is what produced the folder.

---

## Run it yourself

```bash
# 1. Pull or place your videos in inputs/.
./operations/scripts/download_youtube.sh <a youtube url>          # or copy a file in

# 2. Transcribe anything without a good subtitle file.
./operations/scripts/transcribe_parallel inputs/your_video.mp4    # needs OPENAI_API_KEY

# 3. List your videos + speakers in inputs/corpus.manifest.json.

# 4. Build the corpus and load it into the site.
python3 operations/scripts/build_corpus.py --manifest inputs/corpus.manifest.json
cp outputs/corpus-data.js outputs/site/corpus-data.js
open outputs/site/index.html
```

## What you could translate it to

Any corpus of timed media + transcripts: an interview archive, lecture
recordings, oral histories, language-learning video, classroom discussion you
want students to search and cite to the second. Swap the lemmatizer for your
language; point the manifest at your videos; rebuild.
