# Step 3 — Build the pipeline (transcripts → one data file)

**Goal of this step:** a single build script that turns transcripts into one
`corpus.json` the website will read. This and Step 4 can run in parallel.

---

## Prompt

> Write the build step, `operations/scripts/build_corpus.py`. It reads one or
> more transcripts (a `.srt`, or a diarized `.json`) plus video info, and emits a
> single `outputs/corpus.json` (and a `corpus-data.js` wrapper — see below). Use
> the **Python standard library only**, no `pip install`, so it runs on a fresh
> machine.
>
> Pipeline:
> 1. **Parse** each transcript into timestamped utterances. Preserve `start`/`end`
>    exactly — convert `HH:MM:SS,mmm` to float seconds and never round by hand.
>    Keep speaker labels and let me attach speaker metadata (gender, region, etc.).
> 2. **Tokenize + lemmatize** each utterance — map surface forms to headwords so
>    searching "go" also finds "going" and "went". Make the lemmatizer
>    **pluggable per language**: a dependency-free English default now, plus a
>    documented slot for [your target language — e.g. Levantine Arabic, which
>    needs a morphology-aware analyzer, not a stemmer]. Same for the speech-to-text
>    engine: hide it behind an interface so a language swap never touches the site.
> 3. **Build indexes**: `lemma -> [utterance ids]`, `surface form -> [utterance
>    ids]`, and a lemma-frequency table.
> 4. **Score difficulty** per utterance (common words + short = easy) for a
>    "find easy utterances" view.
> 5. **Emit** `outputs/corpus.json`, and also `outputs/corpus-data.js` that just
>    does `window.CORPUS = {…}` — the site will load that as a `<script>` so it
>    works from `file://` (browsers block `fetch()` of a local `.json`).
>
> Let me drive multiple videos from one **manifest** file that lists each video
> (its transcript, whether it's a local file or a YouTube embed) and the speaker
> metadata. Run it on my videos and show me the resulting counts.

---

## Why this works

- **One canonical data file** decouples the pipeline from the site: the site
  never queries a server, it just reads `corpus.json`.
- **Pluggable language stages** are what make this reusable. The English default
  lets you demo immediately; the documented slots mean another language is a
  one-file change, not a rewrite.
- **Lemma + frequency + difficulty** are the genuinely new value over a plain
  string-search corpus — they're what make it a *learner's* dictionary.

## What you should have after this step

- `outputs/corpus.json` + `outputs/corpus-data.js` built from your manifest, with
  utterances carrying `start`/`end`, `tokens`, `lemmas`, and `difficulty`, plus
  the lemma/form indexes and frequency table.
