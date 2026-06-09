# CLAUDE.md — Video Corpus Builder

Project-level instructions loaded when Claude Code starts in this folder.

## What this project is

A **searchable, video-linked language corpus** for teaching and research.
You feed it videos plus subtitle (`.srt`) files; it produces a static
website where a learner can **search a word, see every utterance that
contains it (in context, with who said it and when), and click to play
the video at that exact moment.**

It is modeled on the [CORAAL Explorer](https://lingtools.uoregon.edu/coraal/explorer/)
(search → KWIC concordance → click → media seeks to the timestamp), with
two additions CORAAL doesn't have:

1. **Lemma-aware search** — searching `go` also finds `going`, `went`,
   `goes`. (CORAAL only does literal/regex string matching.)
2. **Frequency / "easy utterance" view** — rank words by how common they
   are to surface high-frequency, low-difficulty utterances for learners.

See [summary.md](summary.md) for the fuller story and
[inputs/corall-explorer-reference.md](inputs/corall-explorer-reference.md)
for the reference UX, and [inputs/handoff.md](inputs/handoff.md) for the
original build brief.

This folder is **grabbable**: take just this directory, open Claude Code
inside it, and you have everything to build a corpus from your own videos.

## Two deployment modes, one codebase

Every video declares a `source_type`. The site behaves identically for
search and concordance; only the player branches.

- **Mode A — Local videos** (the workshop demo): a handful of video files
  you have on disk. Player uses HTML5 `<video>`. No network needed; the
  whole site runs from `file://` by double-click.
- **Mode B — Hosted / YouTube**: videos embedded from YouTube. Player uses
  the YouTube IFrame API and `seekTo()`. Use
  [operations/scripts/download_youtube.sh](operations/scripts/download_youtube.sh) to pull
  a video + its captions into `inputs/`.

## If you just opened this folder

Read in this order:

1. [summary.md](summary.md) — what this is, what's in the folder, and how we built it.
2. [inputs/handoff.md](inputs/handoff.md) — the detailed build brief
   (data model, pipeline phases, gotchas).

Then look at the worked example already in the folder: the local sample
video `inputs/madeleine.mp4` + its `.srt`, built into
`outputs/corpus.json` and browsable at `outputs/site/index.html`.

## The pipeline (inputs → corpus.json → site)

The flow is always: **transcript (+ video)  →  `build_corpus.py`  →
`corpus.json`  →  the static site reads it.** A transcript enters as either a
`.srt` or a diarized `.json` from the transcriber — both become the same
timestamped cues, so the diarized data's sub-second precision and speaker labels
survive. The website itself never reads the `.srt`/`.json`; it reads only
`corpus.json`. (Don't hand-author SRT timecodes when a diarized `.json` exists —
generate the `.srt` from it with `operations/scripts/diarize_to_srt.py` to keep full
precision.)

```
inputs/*.srt  ──►  operations/scripts/build_corpus.py  ──►  outputs/corpus.json
   (+ video)            (parse, lemmatize,            outputs/site/corpus-data.js
                         index, score)                (file://-friendly copy)
                                                            │
                                                            ▼
                                                    outputs/site/index.html
                                              (search · concordance · player)
```

Run the whole demo from this folder:

```bash
# 1. (Mode B only) pull a YouTube video + captions into inputs/
./operations/scripts/download_youtube.sh                 # defaults to the demo video

# 2. build the corpus JSON from one or more .srt files
python3 operations/scripts/build_corpus.py \
  --srt inputs/madeleine.srt \
  --video inputs/madeleine.mp4 \
  --title "Just Do It"

# 3. open the site (double-click also works)
open outputs/site/index.html
```

`build_corpus.py` runs on the **Python standard library only** — no
`pip install`, so faculty can run it on a fresh machine. The two
language-specific stages are pluggable (see below).

## Pluggable language components

Two stages are isolated behind clean interfaces so swapping languages
never touches the website:

- **STT (speech-to-text)** — for videos that arrive *without* an `.srt`.
  Default path is the OpenAI diarizing transcriber in
  [operations/scripts/transcribe_parallel](operations/scripts/transcribe_parallel).
  **Levantine Arabic** needs a dialect-capable model — treat this as a
  tooling dependency, do not assume English.
- **Lemmatizer** — groups surface forms to headwords. The default is a
  lightweight rule-based English lemmatizer in `operations/scripts/lib/`. For
  **Arabic**, a stemmer will NOT work; plug in a morphology-aware analyzer
  (CAMeL Tools / MADAMIRA-style). The slot is documented in the code.

## Hard rules (do not break these)

- **Never drop timestamps.** `start`/`end` come straight from the `.srt`
  and must survive every stage. They are how the site seeks the video.
- **The site needs no backend.** It consumes a static `corpus.json`
  (loaded as `outputs/site/corpus-data.js` so it works from `file://`). No server,
  no build step, no `fetch` of remote data at runtime.
- **Keep STT and the lemmatizer behind their interfaces** so a language
  swap is a one-file change, not a site rewrite.
- **`inputs/` is source material** — treat the videos, `.srt` files, and
  reference docs there as read-only unless the user asks to change them.
- **No emojis** in any generated file.

## Conventions

- **Generated artifacts go in `outputs/`** (`corpus.json` and any reports).
- **The website lives in `outputs/site/`** and is committed; its data file
  `outputs/site/corpus-data.js` is regenerated by the pipeline.
- **Scripts and pipeline code live in `operations/scripts/`** (with shared
  modules in `operations/scripts/lib/`); the demonstration prompts for building a
  project like this live in `operations/prompts/`. Both travel with this folder.

## Audience modes

- **Faculty building a corpus from their own videos.** May not be CLI- or
  git-fluent. Default to plain-English explanations; offer to run the
  commands for them. Natural first move: drop a video + `.srt` into
  `inputs/` and ask to "build the corpus."
- **Marlon (or a collaborator) iterating on the pipeline or site.** Terse,
  no hand-holding.

If unclear which mode applies, ask one question to disambiguate.

## Session-start checks

1. Confirm `operations/scripts/build_corpus.py` exists. If it does, silence is fine.
2. Make sure an `outputs/` directory exists.

If both are in place and the user hasn't asked anything, say nothing.
