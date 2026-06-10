# SRT → Corpus pipeline: build a searchable utterance database from subtitled video

## Project context

The instructor researches **Levantine Arabic** and uses video clips (TV drama, news, interviews, classroom recordings) as the primary corpus for language learning and analysis. Each video has an `.srt` subtitle file aligned to its timeline; the corpus needs those timestamps preserved end-to-end so that any search result can be replayed as a video clip.

The end-state vision:

- A **"dictionary" website** where you type a word, see every utterance that contains it (across the whole corpus), and click an utterance to play the video clip at that timestamp.
- Surface forms (inflected words as they appear in the subtitle) must be **lemmatized** so a search for the root or headword retrieves all inflected uses.

This recipe is the **upstream pipeline**: from a folder of `.mp4 + .srt` pairs to a JSON corpus the dictionary site can index.

## What I want you to do

Build a Python script (`srt_to_corpus.py`) that:

1. Walks a folder of `episode-NN.srt` + `episode-NN.mp4` pairs (or `.json` sidecar with scene/speaker metadata).
2. Parses each `.srt` into a list of cue dicts: `{ start_ms, end_ms, text }`.
3. Tokenizes each cue's text (Arabic-aware — preserve diacritics and tatweel handling, strip punctuation, lower-case Latin-script borrowings).
4. **Lemmatizes** each surface form. Use `camel-tools` (CAMeL Lab) if available; otherwise leave a clearly marked `LEMMA_PLACEHOLDER` so the instructor can swap in their preferred tool.
5. Emits a single `corpus.json` array, one record per cue:

```json
{
  "episode": "ep-03",
  "cue_index": 47,
  "start_ms": 184500,
  "end_ms": 188100,
  "speaker": "Layla",
  "scene": "kitchen",
  "text": "بدّي أروح عالسوق بكرا",
  "tokens": [
    { "surface": "بدّي", "lemma": "أراد" },
    { "surface": "أروح", "lemma": "راح" },
    { "surface": "عالسوق", "lemma": "سوق" },
    { "surface": "بكرا", "lemma": "بكرة" }
  ]
}
```

6. Also emits an **inverted index** `lemma_index.json`: a dict mapping each lemma to a list of `(episode, cue_index)` references, for fast lookup by the dictionary site.

## Constraints

- Pure Python 3.11+, no compiled dependencies beyond `camel-tools` (optional).
- Idempotent: re-running on the same folder produces byte-identical output (sort tokens, sort index keys).
- Stream-safe: don't load all videos into memory; process one episode at a time.
- Speaker/scene data lives in an optional `episode-NN.meta.json` sidecar with the shape `{ "scenes": [{ "start_ms":..., "end_ms":..., "scene":"kitchen", "speakers":["Layla"] }] }`. If absent, leave `speaker` and `scene` as `null`.
- Log progress to stderr; reserve stdout for the optional `--print-summary` mode.
- No emoji. Comment sparingly; a one-liner above the lemma fallback is the only place a comment is warranted.

## What to hand back

- `srt_to_corpus.py`.
- A `README.md` in `operations/` describing how to install `camel-tools`, the expected folder layout, and the contract between this script and the dictionary site.
- A small worked example: one episode's worth of `corpus.json` and `lemma_index.json` in `outputs/sample-episode/`.
