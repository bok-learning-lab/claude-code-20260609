# Prompt — Generate a module study guide

Use this prompt for any ES 53 module (Intro/EP, Muscle, Cardio, Vascular, Renal, Pulmonary). Produces a single exam-ready Markdown study guide students can review the night before an exam.

## Project context

ES 53 — Quantitative Physiology as a Basis for Bioengineering (Linsey Moyer, Harvard SEAS, Fall 2025). The course is dense: six organ-system modules, ~4 lectures each, with quantitative problem sets and three exams. Students need a way to consolidate each module without re-reading every slide.

The study guide is a **synthesis** of the module's lecture digests, the per-module learning-objectives handout (which the faculty has already written carefully), and the assigned textbook reading. Acting as a knowledgeable TA preparing exam-review material — the student's filter, not their replacement teacher.

## Inputs

- `inputs/course-pack/ES 53 Lectures 2025/<Module>/*.md` — text digests of the module's lecture slides
- `inputs/course-pack/ES 53 Lectures 2025/<Module>/*LearningObjective*.md` — the faculty's own objectives handout
- (Optional) `inputs/textbooks/medical-physiology/chapter-NN-*.md` and/or `inputs/textbooks/human-physiology/chapter-NN-*.md` for the assigned reading

## Hard rules

- **Every learning objective from the handout must be addressed somewhere** in the guide. Don't drop any.
- **Organize by sub-topic, not by lecture.** Students will be reading this with the exam in front of them, not the lecture schedule.
- **Critical equations get their own section.** For each equation: the formula, every variable defined with units, and one sentence on when it applies.
- **Quote verbatim from the objectives handout** when the faculty's phrasing is precise — those are the questions the exam will likely ask.
- **Honest about what's quantitative vs. conceptual.** Flag where students need to be able to *calculate*, not just describe.
- **No emojis.** Voice: terse, faculty-facing exam-prep tone. No hand-holding ("don't forget!" / "great job!").

## Output structure

Write to `outputs/<module>/study-guide.md`. Use this skeleton:

```markdown
# ES 53 Module N — <Module Name> Study Guide

_Synthesized from the lecture digests, the [<Module> learning objectives handout](../../inputs/course-pack/...), and assigned reading from Fox/Sherwood and Boron & Boulpaep._

## Roadmap

One short paragraph: what this module is about, the ~4 lectures it spans, and where it sits in the course arc.

## Vocabulary you should be able to define

Bullet list — straight from the objectives handout's "Be sure you can define/describe..." section, in the same order.

## Conceptual learning objectives

Group by sub-topic (e.g. for Cardio: I. Anatomy & ECG / II. Mechanics & cycle / III. PV dynamics). Under each sub-topic, the objectives as numbered prompts, with a 2–4 sentence answer that a student writing under exam pressure should be able to reproduce. Mark anything that requires drawing (Wigger's diagram, PV loop, ECG) explicitly.

## Equations to know cold

Numbered. For each: formula, variables (with units), one-sentence note on when it applies and any common gotchas.

## Quantitative skills

Things students must be able to *calculate* on the exam, with a one-line example. Pull from the objectives handout's calculation list verbatim.

## Common pitfalls

Bulleted, terse — the misreadings/conflations the faculty has flagged or that the lecture digests warn against.
```

## Voice

Imagine the faculty member sitting next to a strong student doing exam review: pointing at the diagram, naming the equation, saying *"this is what they'll ask."* No filler.
