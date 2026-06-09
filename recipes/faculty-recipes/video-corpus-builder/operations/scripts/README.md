# operations/scripts/ — the pipeline and scripts

Everything that turns raw videos + subtitles into the data the website reads.
Pure Python standard library (no `pip install`) plus two shell scripts.
(The companion `operations/prompts/` folder holds the demonstration prompts for
building a project like this with Claude Code.)

```
operations/scripts/
  download_youtube.sh    # Mode B ingest: yt-dlp a video + captions into inputs/
  transcribe_parallel    # STT: make a transcript from a bare video (OpenAI diarize)
  diarize_to_srt.py      # convert a diarized .json into a precise .srt
  build_corpus.py        # the build step: .srt or .json (+video) -> outputs/corpus.json
  test_pipeline.py       # unit tests (timestamps, SRT, dedupe, lemmas, JSON ingest)
  respace_monologue.py   # (bonus) reflow a transcript as a pause-aware monologue
  lib/
    srt.py               # parse .srt -> timestamped cues; rolling-caption dedupe
    diarize.py           # parse diarized .json -> cues; emit a precise .srt
    lemmatize.py         # tokenize + lemmatize; English default, Arabic slot
    stt.py               # STT engine interface; diarize adapter, Arabic slot
```

## The one-paragraph mental model

There is exactly **one ingest path: a `.srt` file.** A human-authored `.srt`,
captions from `download_youtube.sh`, or output from `transcribe_parallel` all
become `.srt`, and `build_corpus.py` reads only that. This is deliberate: it is
the single place timestamps enter the system, and timestamps are how the website
seeks the video. Never lose them.

## Common commands (run from the recipe root)

```bash
# Build the demo corpus (two videos: local + YouTube) — no API key needed.
python3 operations/scripts/build_corpus.py --manifest inputs/corpus.manifest.json

# Build from a single local video.
python3 operations/scripts/build_corpus.py \
    --srt inputs/madeleine.srt \
    --video inputs/madeleine.mp4 \
    --title "Just Do It"

# Build from a single YouTube video (collapse its rolling auto-captions).
python3 operations/scripts/build_corpus.py \
    --srt inputs/labeouf.en.srt --youtube-id ZXsQAXx_ao0 \
    --title "Just Do It (YouTube)" --dedupe-rolling

# Pull a new YouTube video + captions into inputs/.
./operations/scripts/download_youtube.sh https://www.youtube.com/watch?v=VIDEO_ID

# Make an .srt for a video that has none (needs OPENAI_API_KEY).
./operations/scripts/transcribe_parallel inputs/some_video.mp4

# Convert a diarized-transcript .json into a precise .srt.
python3 operations/scripts/diarize_to_srt.py inputs/madeleine.json

# Build straight from a diarized .json (skip the .srt entirely).
python3 operations/scripts/build_corpus.py \
    --diarize-json inputs/madeleine.json \
    --video inputs/madeleine.mp4 --title "Just Do It"

# Run the tests.
python3 operations/scripts/test_pipeline.py
```

## Two transcript formats, one result

A video's transcript can enter as either a `.srt` or a diarized `.json` from the
transcriber; both become the same timestamped cues, so the diarized data's
**sub-second precision and speaker labels survive intact**.

- `.srt` — the canonical, portable format. Millisecond timecodes
  (`HH:MM:SS,mmm`), optional `A:` speaker prefixes.
- diarized `.json` — `{"segments": [{"start", "end", "speaker", "text"}, ...]}`
  straight from `transcribe_parallel`. Use `diarize_json` in the manifest (or
  `--diarize-json`) to ingest it directly, or run `diarize_to_srt.py` to bake it
  into a precise `.srt` first.

Do NOT hand-author SRT timecodes when a diarized JSON exists — you will lose
precision. The demo's `inputs/madeleine.srt` is generated from
`inputs/madeleine.json`, and `test_pipeline.py` asserts the two paths
yield identical timestamps.

The build writes **`outputs/corpus.json`** (canonical) and
**`outputs/corpus-data.js`** (a `window.CORPUS = {...}` wrapper). The website
loads the `.js` wrapper because browsers block `fetch()` of a local `.json` from
`file://`. Copy it into place when ready:

```bash
cp outputs/corpus-data.js outputs/site/corpus-data.js
```

## The manifest

`inputs/corpus.manifest.json` lists the videos in one build. Per-video fields:

| field            | meaning                                                      |
|------------------|-------------------------------------------------------------|
| `source_id`      | stable id (default: file basename)                          |
| `title`          | human-readable title shown in the UI                        |
| `srt`            | path to the subtitle file (relative to the manifest)        |
| `video`          | local video file -> `source_type: "local"`                  |
| `youtube_id`     | YouTube id -> `source_type: "youtube"` (omit `video`)       |
| `dedupe_rolling` | `true` to collapse YouTube rolling auto-captions            |
| `lang`           | ISO 639 code; picks the lemmatizer (default from top level) |
| `scene_meta`     | free-form `{setting, topic, ...}` kept with the video       |

A top-level `speakers` map attaches metadata (`label`, `gender`, `age_group`,
`region`, `role`) to a `speaker_id` (which is `"<source_id>:<srt-speaker-tag>"`).

## Swapping languages (the pluggable parts)

Two stages are isolated so a language change never touches the website:

- **Lemmatizer** (`lib/lemmatize.py`). English is rule-based and dependency-free.
  For **Levantine Arabic**, a stemmer will not work — implement
  `ArabicLemmatizer` against a morphology-aware analyzer (CAMeL Tools) and it is
  picked automatically for `lang: "ar"`. Until then it raises rather than
  silently mangling Arabic with English rules.
- **STT** (`lib/stt.py`). For a bare video, an engine PRODUCES an `.srt`. The
  diarizing OpenAI engine is wired up; the Levantine Arabic engine is a
  documented stub. Both return `.srt`, so the single ingest path holds.

## What the build produces (the contract)

The website depends only on the shape of `corpus.json`. See the schema and the
field-by-field contract in [../inputs/handoff.md](../inputs/handoff.md). The
short version: `videos[]`, `speakers[]`, `utterances[]` (each with `start`/`end`
seconds, `tokens`, `lemmas`, `difficulty`), plus `lemma_index`, `form_index`,
and `lemma_freq`.
