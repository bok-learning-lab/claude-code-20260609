# Step 5 — Lock in precision and guard it with tests

**Goal of this step:** make sure the timestamps are exactly right, and add tests
so they stay right.

---

## Prompt

> Let's make sure our timestamps are precise enough — they're how the site seeks
> the video, so small errors are visible as clips starting in the wrong place.
>
> 1. Audit the path from transcript to `corpus.json`: confirm nothing rounds the
>    `start`/`end` times. If any subtitle file was hand-authored with coarse
>    (whole-second) timestamps, **regenerate it from the diarized `.json`** so it
>    carries the real millisecond values.
> 2. Confirm the build can ingest the diarized `.json` **directly** (not only via
>    a `.srt`), and that both paths produce identical timestamps.
> 3. Write `operations/scripts/test_pipeline.py` (standard-library `unittest`, no
>    pytest) covering:
>    - `HH:MM:SS,mmm` → seconds and the round-trip back, exactly;
>    - SRT parsing edge cases (CRLF, a BOM, `,` vs `.` separators, speaker tags);
>    - the rolling-caption de-duplication, if we handle YouTube auto-captions;
>    - lemmatization (e.g. "went"/"going" → "go", "dreams" → "dream");
>    - that the `.srt` and `.json` ingest paths agree on the sample.
>
> Run the tests and show me they pass.

---

## Why this works

- **Precision is silent when wrong.** A clip that starts a second late looks like
  a vague UI bug, not a data error. Pinning it down — and asserting it in a test —
  is the difference between "seems fine" and "correct."
- **Testing the conversion, not the framework.** The one invariant worth guarding
  is the timestamp math and the parsers; a few standard-library tests cover it
  with zero dependencies.
- **Two ingest paths, one result.** Asserting the `.srt` and `.json` routes agree
  means you can author from either format and trust the output.

## What you should have after this step

- Precise, regenerated subtitles; a build that accepts `.srt` or `.json`; and a
  green `test_pipeline.py` that will catch any future regression in the timestamps.
