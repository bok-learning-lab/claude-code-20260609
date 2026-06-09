# CLAUDE.md — Summer of Claude, week of 2026-06-08

Workshop materials for the *Summer of Claude* faculty workshop at Harvard's Bok Center Learning Lab, week of 2026-06-08. Day 1 (Mon 8 June) introduces the desktop app — Chat and Cowork. Days 2–4 build out from there into Claude Code, skills, and beyond.

## The frame for today

Every project in this repo follows the same three-folder recipe — the pedagogical move of Day 1:

```
inputs/        ingredients (your context — readings, syllabi, data, transcripts)
operations/    instructions (prompts, scripts; sometimes assets the prompts point at)
outputs/       what gets served (the artifacts Claude produces from the recipe)
```

That's it. No `CLAUDE.md` files inside the sub-projects, no `skills/` folders, no MCP configuration yet. Those come on later days. Today the lesson is that **even basic structures get to surprisingly complex outputs** when you put thought into the ingredients and the instructions.

## What's here

- **[recipes/learning-lab-examples/](recipes/learning-lab-examples/)** — validated worked examples from the Lab. Open any one as a Cowork project: read the prompts in `operations/`, look at the artifacts in `outputs/`, and trace how the inputs got cooked into them.
- **[recipes/faculty-recipes/](recipes/faculty-recipes/)** — in-progress projects from this week's faculty cohort. One folder per project, each one a recipe the faculty member is working on with us through the week.
- **[resources/](resources/)** — handouts and checklists for each day, a glossary, and the Day 1 recap activities (population pyramids, the *Coriolanus* close-reading prompt, etc).
- **[my-recipe/](my-recipe/)** — a scratch folder for your own project. Drop your inputs in, write your prompt in `operations-tools-commands/`, watch the output land in `outputs/`.

## Conventions

- **`inputs/` is read-only by convention.** Don't modify source materials in place — generated artifacts go in `outputs/`.
- **No emojis** in any file (workshop-wide convention).
- **Markdown link syntax** for file references.
- **Faculty's commercial textbooks are gitignored** — see `.gitignore`. Outline versions live alongside.

## If you've just opened this folder

1. Pick an example in `recipes/learning-lab-examples/` that looks like work you do.
2. Read its `operations/<n>-prompt.md` first — that's where the alignment constraints and the "project context" live.
3. Skim its `inputs/` to see what got fed in, and its `outputs/` to see what came out.
4. Then try the same shape on your own materials in `my-recipe/`.
