# Build Handoff: Video Corpus Builder + Learner Dictionary

## TL;DR for the agent
Build a static-friendly HTML project that lets a user search a word and
see every utterance (subtitle segment) containing it, then click an
utterance to play the corresponding video clip seeked to that timestamp.
Two deployment modes share ONE codebase and ONE data format:
  MODE A — Local videos (workshop demo): a handful of video files the
           faculty download locally; small, simple, no network.
  MODE B — Hosted corpus: a larger set of YouTube-embedded videos.

The reference UX is the CORAAL Explorer (see reference-coraal.md):
search -> KWIC concordance -> click -> media playback at exact timestamp.
Difference: we use VIDEO and we add LEMMA-aware search + word-frequency
("easy utterance") views.

## Project goals (from the faculty "recipe")
- Inputs: videos + SRT subtitle files. MUST preserve timestamps through
  all processing.
- Auto-generate subtitles when missing (speech-to-text). Levantine Arabic
  is a target language and needs a dialect-capable STT + morphological
  analyzer — treat as a pluggable component, do not hardcode English.
- Build a database for NLP analysis that retains speaker data and scene
  data alongside each utterance.
- Group surface forms to lemmas / headwords.
- Word-frequency analysis to surface "easy" utterances/interactions.
- A dictionary website: search a word -> list of utterances -> click ->
  video clip at that timestamp.

## Architecture decisions (please follow)
- Keep it a SIMPLE HTML/JS project. Prefer a static build: a prebuilt
  JSON index + vanilla JS (or a tiny framework) so it runs from
  file:// or any static host with no backend.
- ONE canonical data file the front end consumes: `corpus.json`
  (or sharded per-video JSON for the larger corpus). The Python/NLP
  pipeline is a BUILD STEP that produces this JSON; the site never needs
  a live server to query.
- Source-type abstraction: each video record declares
  `source_type: "local" | "youtube"` plus the locator
  (`file` path or `youtube_id`). The player component branches on this:
  HTML5 `<video>` + WebVTT for local; YouTube IFrame API `seekTo()` for
  embeds. Everything else (search, concordance, data) is identical.

## Canonical data model
```json
{
  "videos": [
    {
      "source_id": "vid001",
      "title": "...",
      "source_type": "local",          // or "youtube"
      "file": "videos/vid001.mp4",      // when local
      "youtube_id": null,               // set when youtube
      "speakers": ["spk001", "spk002"],
      "scene_meta": { "setting": "...", "topic": "..." }
    }
  ],
  "speakers": [
    { "speaker_id": "spk001", "gender": "f", "age_group": "2",
      "region": "...", "role": "..." }
  ],
  "utterances": [
    {
      "utterance_id": "vid001_0007",
      "source_id": "vid001",
      "line": 7,
      "speaker_id": "spk001",
      "start": 134.92,                  // seconds, FROM THE SRT
      "end": 137.24,
      "text": "Okay, so now I'm finna get into some more",
      "tokens": ["okay","so","now","i'm","finna","get","into","some","more"],
      "lemmas": ["okay","so","now","be","finna","get","into","some","more"]
    }
  ]
}
```
Notes:
- `start`/`end` come straight from the SRT — never lose them. SRT
  `HH:MM:SS,mmm` -> float seconds.
- `lemmas` is the search key for the "dictionary." Maintain an inverted
  index: lemma -> [utterance_id...].
- For frequency/difficulty: precompute lemma frequency across the corpus
  and an utterance "difficulty" score (e.g. mean lemma rarity, length).

## Build pipeline (Python, produces corpus.json)
1. Parse SRT -> utterance rows (preserve timestamps + any speaker tags).
2. If a video has no SRT: run STT to generate one (pluggable engine;
   Levantine Arabic uses a dialect-capable model). Output still SRT so
   step 1 stays the single ingest path.
3. Tokenize + lemmatize each utterance (pluggable per language; for
   Arabic use a morphology-aware analyzer, not a stemmer). Attach lemmas.
4. Build inverted index (lemma -> utterances) and frequency tables.
5. Emit corpus.json (+ per-video shards for the large/YouTube corpus).

## Front end (the site)
- Search box + filters (speaker gender / age group / region; video).
  Support exact-form AND lemma search (toggle). Optional regex later.
- Results = KWIC concordance table: PreMatch | **Match** | PostMatch,
  with speaker + start/end timestamps + source. Like CORAAL's hit list.
- Clicking a hit opens the player view, seeked to `start`:
    local  -> `<video>`; set currentTime = start.
    youtube-> IFrame API player.seekTo(start, true).
  Show the surrounding transcript with the active line highlighted
  (mirror CORAAL's browse view + its line/settime deep-link, but encode
  it as a front-end route/hash like `#/v/vid001?line=7&t=134.92`).
- A "Frequency / Easy utterances" view: list lemmas by frequency; let the
  user jump to low-difficulty utterances for that lemma.

## Suggested prompt sequence for me (Claude Code), phased
P1. Scaffold the repo: /pipeline (Python), /site (static HTML/JS),
    /context, /outputs. Add corpus.json schema + 1 tiny fixture video
    (Mode A) and 1 YouTube record (Mode B) so both paths are exercised.
P2. SRT parser -> utterances (timestamps preserved); unit tests on the
    HH:MM:SS,mmm -> seconds conversion and round-trip.
P3. Pluggable STT step for videos lacking SRT (interface + one engine);
    document the Levantine-Arabic engine slot.
P4. Pluggable tokenize+lemmatize; English default + Arabic
    morphological-analyzer slot. Attach tokens/lemmas; build inverted
    index + frequency tables; emit corpus.json.
P5. Static front end: search + filters + KWIC concordance.
P6. Player view with source_type branching (HTML5 + YouTube IFrame),
    seek-to-timestamp, transcript highlight, deep-link routing.
P7. Frequency / "easy utterance" view + difficulty scoring.
P8. Polish: empty states, no-results, sample dataset for the workshop,
    README explaining Mode A vs Mode B.

## Constraints / gotchas
- Never drop timestamps anywhere in the pipeline.
- Keep STT and lemmatizer behind clean interfaces so language swaps don't
  touch the site.
- The site must run with no backend (static JSON) for the local workshop.
- For YouTube, seeking requires the IFrame API (enablejsapi) and the
  player to be ready before seekTo — handle the onReady race.
- We are referencing CORAAL's design only; not redistributing its data.