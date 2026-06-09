# operations/prompts/ — how this project was prompted into being

These are **idealized demonstration prompts**: a clean, efficient sequence you
could give Claude Code to build a project like this one from scratch. They are
not verbatim transcripts of our session — they are the prompts we *wish* we had
given, in the order that gets you there with the least backtracking.

Each file is one step. Read them in order; adapt the bracketed `[...]` parts to
your own corpus. The throughline is the lesson the real build taught us:

> **Agree on the artifact, gather real material, get the data clean, build the
> machine that transforms it, and only then build the thing people see.**

## The sequence

1. [01-frame-the-project.md](01-frame-the-project.md) — turn a rough idea (or a
   handwritten recipe card) into a written brief and a folder skeleton before any
   code.
2. [02-ingest-and-transcribe.md](02-ingest-and-transcribe.md) — get real videos
   in, and get clean, precise, speaker-labeled transcripts out.
3. [03-build-the-pipeline.md](03-build-the-pipeline.md) — the Python build step:
   transcripts → one `corpus.json` (parse, lemmatize, index, score).
4. [04-build-the-site.md](04-build-the-site.md) — the static search-and-playback
   website, built in parallel against a frozen data contract.
5. [05-precision-and-tests.md](05-precision-and-tests.md) — lock in timestamp
   precision and guard it with tests.
6. [06-polish-and-document.md](06-polish-and-document.md) — naming, cleanup, and
   a single summary doc.

## How to use them

- **One at a time.** Let each step finish and eyeball the result before the next.
- **Two at once where it pays.** Steps 3 and 4 are designed to run in parallel in
  two Claude sessions — see the note in step 4 about freezing the `corpus.json`
  contract so they never collide.
- **Keep asking "is this precise enough?"** The single most valuable human move in
  the real build was pushing on data quality (timestamps, transcripts, lemmas).
