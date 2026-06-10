# Build a one-week schedule for the Rising Scholars summer course

## Project context

This is a **seven-week, four-day-per-week, three-hour-per-day** summer course for rising scholars. It interleaves two Harvard math courses:

- **Math 1a/1b** — standard single-variable calculus (limits, derivatives, integrals, series).
- **AM50 (Intro to Applied Math)** — applications drawn from imaging, sports analytics, epidemiology, signal processing.

The pedagogical move is to let AM50 applications **motivate and drive** the calculus topics, not the other way around.

Each three-hour block is structured:

| Block | Time | Purpose |
|---|---|---|
| Lecture | ~45 min | New concept, anchored in an application |
| Active practice | ~75 min | Worked problems and pair work |
| HW support | ~60 min | Structured help on the day's homework |

## What I want you to do

Given:

- A week number (1 through 7).
- The calculus topic for that week (e.g., "Week 1: limits and continuity").
- The AM50 application thread for that week (e.g., "Week 1: discrete-time models of disease spread").

Produce a **week schedule** in markdown with this shape:

```
# Week N: <calc topic> via <AM50 application>

## Monday — Day 1
**Lecture (45 min):** ...
**Active practice (75 min):** ...
**HW support (60 min):** ...

## Tuesday — Day 2
...
```

For each day:

- The **lecture** segment should open with a concrete AM50 problem that needs the day's calc tool. State what calc concept emerges from the problem.
- The **active practice** segment should be 3–5 problems progressing from scaffolded to open. Mark each problem with whether it is a pure-calc problem, a pure-application problem, or a bridge.
- The **HW support** segment should list 1–2 likely sticking points for that day's HW and how the instructor will pre-empt them.

## Constraints

- Calculus topics must follow the Math 1a/1b sequence in order — don't jump ahead.
- The "application thread" should run *continuously* across the week so students see one AM50 problem deepen day by day.
- Include a Friday-style weekly quiz at the end of the week (5 questions, 30 min, mixing pure-calc and application).
- No emoji. Plain markdown. Cite the calc concept and the application clearly in each block.
