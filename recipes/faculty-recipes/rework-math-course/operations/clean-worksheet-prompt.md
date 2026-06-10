# Clean and re-flow a Math 21b worksheet (.tex)

## Project context

Math 21b is Harvard's *Linear Algebra, Differential Equations, and Fourier Series* course. The instructor maintains a library of `.tex` worksheets, problem sets, exams, lesson plans, and learning goals from past semesters. The materials work but have accumulated friction:

- Tight spacing — students can't write between problems.
- No visual hierarchy for **Definitions**, **Theorems**, **Examples**.
- Broken or stale cross-file links (e.g., "see Worksheet 2" when the numbering shifted).
- Minor typos, occasional sign errors in solutions.
- Inconsistent macro usage (`\Nul` vs `\text{Nul}` vs `\mathrm{Nul}`).

This recipe is about **upgrading one file at a time**, not a wholesale rewrite. The math is correct; the layout and the polish need help.

## What I want you to do

Given a Math 21b `.tex` worksheet file, produce a **cleaned version** that:

1. **Adds vertical breathing room** between exercises (use `\vspace{3em}` or a `tcolorbox` solution shell, your call — but be consistent within the file).
2. **Boxes definitions and key theorems** in a visually distinct shell. Use `tcolorbox` (`\usepackage[most]{tcolorbox}`) with one named environment per category — `defn`, `thm`, `ex` — and a sober color scheme (charcoal rule, no fluorescent fills).
3. **Standardizes notation macros** at the top of the file: define `\Nul`, `\Col`, `\Row`, `\rank`, `\nullity`, and use them throughout. Replace inline `\text{...}` with the macros.
4. **Adds writing space** for each exercise: an empty `tcolorbox` or `\fbox{\parbox}{...}` sized to the expected answer length. Mark each space with a faint "work here" hint so the layout reads correctly when printed.
5. **Flags possible issues** in a comment block at the top of the file (`% REVIEW: ...`) — typos, sign errors, ambiguous instructions. Do NOT silently fix mathematical errors — surface them for the instructor to confirm.
6. **Preserves all original content and ordering.** No new problems, no removed problems, no reordering.

## Constraints

- The file must compile with a standard TeX Live install plus `tcolorbox`.
- No exotic packages (no `tikz` unless the original used it).
- Keep the `amsart` (or original) document class.
- No emoji. American mathematical notation.
- Output: the full cleaned `.tex` file body, plus a short `## Changes` section in a code-block comment listing what you changed.

## When you are unsure

If a problem statement is ambiguous, flag it in a `% REVIEW:` comment rather than guessing the intended meaning. If a theorem name varies in the course (e.g., "Rank-Nullity" vs "Dimension Theorem"), preserve the original term and add a `% REVIEW: terminology choice` note.
