# Sample episode output

Two files produced from `inputs/sample-episode/ep-03.srt` + `ep-03.mp4` + `ep-03.meta.json`:

- **`corpus.json`** — one record per subtitle cue, with surface forms tokenized and lemmas resolved.
- **`lemma_index.json`** — inverted index mapping each lemma to the cues that contain it.

## How the dictionary site uses these

A search for the verb *راح* ("to go") hits `lemma_index.json["راح"]`, which returns `[["ep-03", 1]]`. The site then looks up cue 1 in `corpus.json` and renders:

> **Karim** (kitchen, 00:16.2): "أكيد، بس بدّي أروح عالسوق أول شي."

The cue's `start_ms` is fed to the video player's `currentTime`, so clicking the result plays the clip from that moment.

## Why we keep `surface` and `lemma` separate

A learner searching for *أروح* (1st-singular imperfect) should also find utterances of *راح* (3rd-singular perfect) and *رحت* (1st-singular perfect). The lemma is the join key; the surface form is what the student sees in the subtitle.
