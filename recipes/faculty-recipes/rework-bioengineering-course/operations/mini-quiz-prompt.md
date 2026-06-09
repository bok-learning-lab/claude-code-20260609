# Prompt — Generate a 5-MCQ mini quiz

Produces a five-question multiple-choice quiz students can finish in five minutes. Used either as a **lecture-review** mini quiz (based on the prior lecture's content) or as a **reading-check** mini quiz (based on an assigned textbook chapter).

## Project context

ES 53 — Quantitative Physiology as a Basis for Bioengineering (Linsey Moyer, Harvard SEAS, Fall 2025). The faculty member wants short, ungraded-or-low-stakes mini quizzes that surface whether students actually did the reading or paid attention in class — without playing gotcha. The goal is a calibration tool, not an evaluation tool.

## The quality bar (the faculty's exact words)

> The correct answer should be **non-obvious**, but should not look like trick questions. They should be **easy to answer for someone who paid attention and read the textbook**, but **not obvious to those who haven't done the reading or paid attention in class.**

Translate that into question construction:

- The stem must be answerable from the source material (lecture digest or chapter), not from general intuition.
- The correct answer should not be the most superficially appealing one — surface recall isn't enough.
- Distractors should be **plausible** to a student who half-read the material: common misconceptions, partially correct answers that miss a qualifier, values close to but not equal to the right number, related concepts from adjacent material.
- Avoid: "all of the above," "none of the above," double-negative stems, two answers that are obviously identical except for one trivial detail.

## Inputs

The user supplies the source. Either:

- **Lecture mini-quiz:** a path to a lecture digest in `inputs/course-pack/ES 53 Lectures 2025/<Module>/<Lecture>.md`, optionally with the module's objectives handout.
- **Reading mini-quiz:** a path to a textbook chapter outline in `inputs/textbooks/<book>/chapter-NN-*.md`.

## Hard rules

- **Exactly five questions.** Not four, not six.
- **Four choices per question (A–D), one correct.**
- **Coverage breadth.** Each question targets a different learning objective / sub-topic in the source — don't ask five versions of the same concept.
- **Include at least one quantitative question** when the source contains equations or numerical values. (For purely qualitative chapters, skip this.)
- **Answer key at the bottom**, separated by `---`, with a **one-sentence rationale** for each correct answer that names the specific section / paragraph / equation in the source. The rationale is for the instructor, not the student.
- **No emojis. No "Good luck!" or other student-portal filler.** Faculty-facing markdown.

## Output structure

Write to `outputs/<module>/mini-quiz-<n>.md` (for lecture mini-quizzes) or `outputs/reading-quizzes/<book>/ch<NN>.md` (for reading checks). Use this skeleton:

```markdown
# Mini Quiz — <Source short title>

_Five questions, ~five minutes. Source: [<source path>](<relative link>)._

## 1. <Question stem>

A. ...
B. ...
C. ...
D. ...

## 2. ...

[etc.]

---

## Answer key (instructor)

1. **C.** <one-sentence rationale tying it to a section / equation in the source>
2. **A.** ...
[etc.]
```

## Calibration: what "non-obvious but fair" looks like

- ✗ "What is the SA node?" (pure recall, obvious)
- ✗ "What is *not* a function of the ventricles?" (negation + obscure)
- ✓ "A patient's ECG shows a normal P wave followed by a wide QRS that occurs at a regular rhythm independent of the P–P interval. Which conduction abnormality best explains this?" (requires having understood the ECG–anatomy mapping; rewards reading; distractors are real arrhythmias)
- ✓ "If end-diastolic volume increases from 120 mL to 140 mL while end-systolic volume stays at 50 mL, what is the new ejection fraction (rounded)?" (calculation + definition; rewards knowing EF = SV / EDV, not just naming it)
