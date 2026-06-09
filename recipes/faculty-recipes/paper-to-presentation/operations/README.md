# Paper-to-Presentation: A Four-Step Workflow

This folder contains a **chained set of prompts** for turning a research paper into compelling presentation materials. Each step produces output that feeds into the next, so judgment calls happen upstream.

---

## The Four Steps

### **Step 1: `01-outline-deck.md`** — Outline the structure
**What it does:**
- Reads your paper
- Reconstructs the argument (thesis, premises, objections, replies)
- Produces a slide *outline* that preserves the argument's logic
- Each slide carries one move; speaker notes hold the nuance

**Input:** Your research paper (PDF or text)
**Output:** A markdown outline with titles, key lines, and speaker notes
**Time to review/edit:** 15–30 minutes (you'll catch places where the outline needs tightening)

**Why this step matters:** A good outline is half the battle. Once the argument is clear on paper, the visual choices become obvious.

---

### **Step 2: `02-visual-assets.md`** — Design visual assets
**What it does:**
- Reads your approved outline
- Identifies where visualization would help (hard concepts, spatial ideas, processes)
- Specs out figures, diagrams, and animations
- Produces a visual asset manifest: what to build and where

**Input:** Your approved outline (from Step 1)
**Output:** A manifest describing each visual asset (type, concept, creation notes)
**Time to review:** 10–15 minutes (skim the specs, flag anything misleading or unclear)

**Why this step matters:** Visual specs go to the builder *before* they start designing, so they know what assets are coming and where they fit.

**Optional:** You can skip this step if your paper has good figures already and animation would take too long. Just note in Step 3 which figures to use directly.

---

### **Step 3: `03-build-deck.md`** — Build the slide deck
**What it does:**
- Takes your approved outline + visual asset manifest
- Builds a real .pptx (or HTML) slide deck
- Preserves speaker notes in the notes field
- Places visuals exactly where the manifest said they'd go
- Adds design polish (fonts, colors, layout)

**Input:** Your approved outline + visual manifest + visual asset files
**Output:** A .pptx file (ready to present) or a polished Markdown deck
**Time to review:** Skim for typos and visual placement; the argument structure is already locked in from Step 1

**Why this step matters:** The builder is *executing a plan*, not making judgment calls. Errors from Step 1 propagate here, which is why Step 1 is careful.

---

### **Step 4: `04-web-version.md`** — Build an interactive web version (optional)
**What it does:**
- Takes your finished slide deck + visual assets
- Builds a web-native, interactive experience
- Offers three viewing modes:
  - **Presentation mode** — minimal text, full-screen visuals (you present live)
  - **Study mode** — visuals + explanatory text (viewers read later)
  - **Speaker notes mode** — you see notes on your laptop while presenting
- Adds polish: dark mode, animations, responsive design, keyboard shortcuts

**Input:** Your finished .pptx + visual asset files
**Output:** An HTML file (or folder) you can host or share
**Time to build:** Depends on scope; a minimal version (single HTML file) takes ~2 hours; a polished version with custom animations takes longer

**Why this step is optional:** 
- If you're presenting once and never looking back, skip it.
- If you want a **reusable resource** (students study it, colleagues share it, you give it again next year), the web version is worth the effort. It's also more shareable than a .pptx.
- The web version is **not a replacement for slides**; it's a *complement*. Use whichever fits the moment (slides for a live talk, web for studying later).

---

## Quick-Start Checklist

- [ ] **Have your paper ready** (PDF or text)
- [ ] **Fill in Step 1's placeholders** (talk length, audience, constraints)
- [ ] **Run Step 1** → get the outline
- [ ] **Edit the outline by hand** (15–30 min; tighten arguments, flag hard moves)
- [ ] **Approve the outline** (sign off mentally: "this is the story I want to tell")
- [ ] **Run Step 2** (optional; helps if visuals are important)
- [ ] **Review the visual manifest** (10–15 min; catch anything misleading)
- [ ] **Run Step 3** → get the slide deck
- [ ] **Skim the deck for typos/polish** (the argument is already locked in)
- [ ] **Rehearse** (10 minutes, out loud)
- [ ] **Run Step 4** (optional; if you want a web version)

---

## How to use each prompt

Each prompt is a **template**. To use it:

1. **Open the prompt file** (e.g., `01-outline-deck.md`)
2. **Find the `{{placeholders}}`** (usually at the top)
3. **Fill them in with your specific info** (your paper, your audience, your constraints)
4. **Paste the filled-in prompt + your source material into Claude** (or another LLM)
5. **Review the output carefully** — the LLM is doing the mechanical work, but you're steering

---

## Important principles

### Preserve the argument, don't flatten it
The biggest risk in turning a paper into slides is **losing the logical structure**. This workflow combats that by:
- Making you reconstruct the argument *first* (Step 1)
- Locking in that structure with an outline
- Only then adding visuals and polish

### One idea per slide
A slide should do one job: convey one move in the argument. If you're tempted to say two things, split them. (The web version's "study mode" can hold richer notes, so detailed nuance goes *there*, not on the slide face.)

### Speaker notes are where the argument lives
Slides are *cues*, not scripts. Speaker notes hold the qualifications, examples, and nuance that make the argument defensible. The deck builder preserves them verbatim.

### Visuals should clarify, not decorate
A figure should make a concept visible that's hard to grasp in words. If it's just pretty, it doesn't belong.

---

## When to skip steps

- **Skip Step 2** if:
  - Your paper has clean figures already, and you don't need animations
  - You're short on time and a text-based outline is sufficient
- **Skip Step 4** if:
  - You're presenting once and moving on
  - Your audience is live, and they'll never see the deck again
  - You don't have the technical bandwidth to build a web version

**Never skip Step 1.** An outline is the cheapest insurance against a muddled talk.

---

## Customization notes

These prompts are written for a **physics research talk** (10–20 minutes, academic audience). But they generalize:

- **For philosophy:** The outline and deck-building steps work exactly; visuals are fewer, speaker notes are denser.
- **For computer science:** Same structure; examples might involve code snippets or demos instead of figures.
- **For a longer talk (30+ min):** Add more slides, but keep the narrative arc (motivation → methods → results → conclusion). Each arc can have sub-arcs.
- **For a general audience:** Emphasize Step 2 (visuals) and Step 4 (study mode notes); non-specialists need more scaffolding.

---

## Troubleshooting

**"The outline feels flat."**
→ Step 1 probably missed the objection/reply structure. Re-read the paper; flag any move where your theory predicts X but the data shows Y — that's likely the crux.

**"I have too many slides."**
→ Cut ruthlessly. A 10-minute talk is ~10–12 slides. If you have 20, you're trying to say too much. Pick 3 key results, not 6.

**"The visuals are too simple."**
→ That's fine. Simple, clear visuals beat flashy ones. If the concept is subtle, let speaker notes carry the nuance.

**"I don't have time for the web version."**
→ Build the .pptx first, present it, *then* (if it's worth it) hire someone to build the web version later or do it yourself as a future project.

---

## Reference materials

Input this folder also contains:
- `../inputs/nancy-duarte-presentation-transcript.md` — The "secret structure of great talks" (narrative arc)
- `../inputs/physics-conference-presentation-guidance.md` — APS & academic standards (hard constraints)
- `../inputs/` — Your paper(s) and any supporting materials

---

## Questions?

This workflow is designed to be **self-explanatory**, but if you hit a wall:
- Re-read the "Do this" section in whichever step you're on
- Look at the examples (especially in Step 1 and Step 2)
- Ask yourself: *What decision am I trying to make here, and what info do I need?*

The prompts are your guides. They're not rigid. If a step doesn't fit your paper, adapt it.

---

**Happy presenting.** 🎤
