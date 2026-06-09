# Prompt — Build the interactive grade-trajectory explorer

Paste the block below to Claude (e.g. in Claude Code, with this repo open). It
points at the files already in `inputs/` and asks for the interactive artifact
described in the recipe. Everything Claude needs — the assessment order, the
weights, the letter scale, the framing — is either in this prompt or in the
input files it names.

This prompt is kept in sync with the artifact the generator actually produces
([`build_explorer.py`](build_explorer.py) → `outputs/grade_explorer.html`).

---

## The prompt

> **Role.** You are helping me, the instructor of MATH 21a (Multivariable
> Calculus), build an **interactive web artifact** for my students. I will share
> it at the start of term so they can see how grade outcomes actually unfold over
> a semester — clearly and **without alarming students** — and so each student
> can plot *their own* grades so far and see how their path compares to past
> students. The goal is for a student to think "a rough first exam is not a
> verdict, and here's where getting help tends to change the trajectory," not
> "I'm doomed."
>
> **Inputs** (all in `recipes/faculty-recipes/gradebook-visualization/inputs/`):
> - `gradebook_AY25.csv` and `gradebook_AY26.csv` — two past offerings,
>   ~50 anonymized students each. One row per student. Columns in chronological
>   order: `Mini-Exam`, `PS1`…`PS10`, `Midterm1`, `Midterm2`, `Participation`,
>   `Final`, then the computed `Course_Pct` and final letter `Final_Grade`.
>   All scores are out of 100. The data is synthetic.
> - `assessment_schedule.csv` — the name, week, date, and weight of every
>   assessment (the timeline the chart should step through).
> - `syllabus.md` — the grade formula and the letter-grade scale.
>
> **Grade weights** (sum to 1.0; also in the syllabus / schedule):
> Mini-Exam 5% · Problem Sets 30% (10 × 3%) · Midterm 1 15% · Midterm 2 15% ·
> Participation 5% · Final 30%.
>
> **The core chart.** A "running grade" trajectory plot. The x-axis is the
> assessments in chronological order (Mini-Exam → PS1…PS10 → Midterm 1 →
> Midterm 2 → Participation → Final); the y-axis is the **running weighted grade
> so far** — after each assessment, recompute the grade using only the
> assessments completed up to that point, renormalizing the weights of what has
> happened so far. Each past student is a faint line that ends at their final
> `Course_Pct` / letter grade. Soft shaded letter-grade bands (A / B / C / D / F)
> sit behind the lines as a calm backdrop with labels on the right axis. Hovering
> any historical line surfaces a tooltip of where that student started and
> finished.
>
> **The interactive student feature (this is the centerpiece):**
> - A panel where a student enters the grades they've received **so far** — one
>   input per assessment, in order, which they can fill in progressively (leave
>   later ones blank). As they type, draw **their** trajectory as a bold,
>   distinct line on top of the historical cloud, updating live.
> - **Find similar past students:** match the student's entered scores against
>   the historical rows over the assessments they've completed (nearest
>   neighbors by those columns), highlight that matched subset, and show **where
>   those similar students ended up** — the range and the median final grade.
>   Phrase it supportively, e.g. "Students who looked like you after Midterm 1
>   finished between B- and A-, most often around a B+."
> - **Projection, not prophecy:** from the matched neighbors, shade a gentle
>   projected cone from the student's current point to the end of term, and state
>   plainly that it is a range of past outcomes, not a prediction or a ceiling.
>   The projection should **widen when fewer assessments are entered** (less
>   information → more uncertainty) and narrow as the term fills in.
> - **Goal check (target-grade solver):** let the student pick a target letter
>   grade and show what average they'd need across the **remaining** weight to
>   reach it — and reassure them when a grade is already secured, or be honest
>   (gently) when it's out of reach.
> - **"Where you can still gain":** when grades remain, surface a short,
>   encouraging list of the assignment *types* still ahead (problem sets,
>   midterms, final, participation, mini-exam), ranked by how much weight is left
>   in each, with one supportive line apiece — this is where the intervention
>   guidance lives (e.g. office hours and the Math Question Center change
>   midterm trajectories most).
> - Let the student toggle which past cohort(s) to compare against (AY25, AY26,
>   or both).
>
> **Design requirements (non-alarmist + clear):**
> - Calm, encouraging visual language. No harsh red "failing" zone; use soft
>   letter-band shading and supportive copy throughout.
> - Include one **"Try an example"** button that loads a real *turnaround* path
>   from the data — a weak Mini-Exam that climbs to a strong finish — filled in
>   only through Midterm 1, with a one-line caption making the point that early
>   scores don't lock in the outcome. A "Clear" button resets to the student's
>   own entry.
> - Use the real assessment names/weeks from `assessment_schedule.csv` on the
>   axis. Never present anonymized IDs as real people — they're illustrative paths.
> - Privacy: a student's own entered grades must stay **in the browser** — no
>   network calls, no storage that leaves the page session.
>
> **Output & tech.**
> - Produce a **single, self-contained `.html` file** written to
>   `recipes/faculty-recipes/gradebook-visualization/outputs/`
>   (e.g. `grade_explorer.html`) that opens by double-clicking — no server, no
>   build step, works offline.
> - **Embed the historical data inline** in the HTML as JSON (read the CSVs and
>   bake the rows in) so the file is fully portable. Write a small Python helper
>   in `operations/` (e.g. `build_explorer.py`) that reads the CSVs + weights and
>   generates the HTML, so I can regenerate after editing the data — don't
>   hand-place the numbers.
> - Plain HTML/CSS/JS. **Preferred:** inline a lightweight SVG or Canvas chart so
>   the file is truly offline with zero dependencies. If you instead use one
>   well-known charting library via CDN (e.g. Plotly or Chart.js), say so clearly
>   and note that it then needs internet. State which you chose and why.
> - Responsive and readable on a laptop and a projector. Accessible color
>   contrast and keyboard-usable inputs.
>
> **Before you code**, briefly confirm your plan: the running-grade math
> (renormalizing completed weights), the similar-student matching method and how
> you'll phrase/define the outcome range and projection, how the goal-check
> solver and the "where you can still gain" tips work, the single turnaround
> example you'll feature, your charting choice (inline vs CDN), and the exact
> output file(s). Then build it, run the generator, and tell me how to open and
> use it.
