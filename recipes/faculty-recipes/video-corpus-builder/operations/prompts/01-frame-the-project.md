# Step 1 — Frame the project before writing code

**Goal of this step:** turn a rough idea into a shared, written target — a brief
and a folder skeleton — so everything that follows has something to aim at.

---

## Prompt

> I want to build a **searchable, video-linked language corpus**. The idea: I
> have videos with subtitles, and I want a website where a learner can search a
> word, see every utterance (subtitle segment) that contains it — in context,
> with who said it and when — and click a result to play the video at that exact
> moment.
>
> Before writing any code, help me **write this down clearly**. I'm attaching my
> rough notes / a photo of my handwritten "recipe card": [drop in your notes,
> or describe the project in 4–5 sentences].
>
> Please do three things:
> 1. Write a short **build brief** I can keep in the repo: the data model (videos,
>    speakers, and timestamped utterances), the processing steps, and the hard
>    constraints. The most important constraint: **never lose the subtitle
>    timestamps** — they're how the site will seek the video.
> 2. Note any **reference** we should borrow the UX from. (For a searchable
>    spoken-language corpus, look at the CORAAL Explorer: search → concordance →
>    click → media seeks to the timestamp. Summarize what we'd keep and what we'd
>    add — specifically lemma-aware search and a word-frequency view.)
> 3. Propose a **folder structure** for the project and create the skeleton:
>    `inputs/` (source videos + transcripts + the brief), `operations/` (scripts),
>    `outputs/` (generated data + the site). Put a `CLAUDE.md` at the root that
>    explains the project so I can open Claude Code here later and it has context.
>
> Don't build the pipeline or the site yet — just get us aligned on the artifact.

---

## Why this works

- **The brief is the contract.** Spending the first prompts agreeing on the data
  model and constraints (not generating code) is the highest-leverage habit in
  the whole build. Every later step refers back to it.
- **Naming the reference** gives Claude a concrete UX to match instead of guessing.
- **A `CLAUDE.md` up front** means every future session starts with context, so
  you don't re-explain the project each time.

## What you should have after this step

- A written brief in `inputs/` (data model + steps + "never lose timestamps").
- A one-page note on the reference UX and what you're adding to it.
- An empty but sensible folder skeleton, and a root `CLAUDE.md`.
