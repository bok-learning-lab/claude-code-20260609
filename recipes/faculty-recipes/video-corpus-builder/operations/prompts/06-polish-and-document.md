# Step 6 — Polish and document

**Goal of this step:** make the folder presentable and self-explanatory, so
someone else (or future you) can pick it up.

---

## Prompt

> Let's tidy up and document.
>
> 1. **Human-friendly names.** Rename the videos and their transcript files to
>    meaningful names [e.g. by speaker or source], and set the real speaker labels
>    in the manifest. Keep any external ids that must stay exact (like a YouTube
>    video id used for embedding). Then rebuild and re-copy the data into the site.
> 2. **Remove cruft.** Delete intermediate audio, stray re-transcriptions, editor
>    caches, and browser-automation logs. Add a `.gitignore` that ignores the
>    regenerable junk but **keeps** the worked-example data so the demo runs out
>    of the box.
> 3. **One summary doc.** Write a single `summary.md` at the project root that
>    explains both **what's in the folder** (a short map of `inputs/`,
>    `operations/`, `outputs/`, `outputs/site/`) and **how we built it** (the
>    sequence: brief → ingest → clean transcripts → pipeline → site → polish).
>    Include a copy-pasteable "run it yourself" block. Fold any other scattered
>    docs into this one and delete them.
> 4. **Check the docs match the code.** After any moves or renames, verify the
>    paths in `CLAUDE.md`, `summary.md`, and the scripts all still resolve, and
>    that the tests and the build still run.

---

## Why this works

- **Naming tells the story.** `madeleine.mp4` / `labeouf.mp4` say more than
  `clip1.mp4` / `ZXsQAXx_ao0.mp4`, and a tidy `inputs/` is itself documentation.
- **One doc, not five.** A single summary that a newcomer can read top-to-bottom
  beats a scatter of overlapping READMEs. Fold and delete.
- **Docs drift after moves.** Renaming files and moving folders silently breaks
  relative paths and example commands; an explicit "do the docs still match the
  code?" pass catches it.

## What you should have after this step

- Cleanly named inputs, no cruft, a `.gitignore`, and a single `summary.md` that
  explains the project and how it was built — with every path verified to work.
