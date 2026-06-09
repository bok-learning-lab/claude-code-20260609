# Paper-to-Presentation Conversion Prompt

> Generate compelling conference presentation materials from a single research paper.
> This prompt combines storytelling narrative arc (Nancy Duarte) with technical physics
> conference standards (APS). Use it to guide Claude or another AI in creating slides,
> speaker notes, and supporting materials.

---

## YOUR TASK

You are converting a **single research paper into a 10-minute conference presentation** for a physics audience. Your goal is not to compress the paper; it's to **tell the paper's story** — why it matters, what new insight it provides, and why the audience should care.

---

## HARD CONSTRAINTS (non-negotiable)

- **Timing:** 10 minutes of spoken content (audience can absorb ~1 slide per minute)
- **Slide count:** ~10–12 content slides + title slide + optional backup slides
- **Aspect ratio:** 16:9 (never 4:3)
- **Font:** Sans serif, 20pt minimum for body text
- **One idea per slide** — if you're tempted to say two things, split them
- **Readability:** Assume viewers on a laptop, tablet, or phone. Charts and data must be legible at small size.

---

## THE NARRATIVE ARC (story structure from Nancy Duarte)

A great presentation has a **beginning, middle, and end**. It moves the audience from one understanding to another — not by overwhelming them with facts, but by making them feel the gap between *what is* and *what could be*.

### 1. **Beginning: Establish the Gap**

Your opening must answer: *"Why should I care about this?"*

- **What is:** Describe the current state of the field. What's the problem or unsolved question?
- **What could be:** Present the promise — what becomes possible with this work?
- **Make the gap vivid.** Use contrast. Show the limitation, then hint at the solution.

This is your "inciting incident." The audience must feel that something is at stake.

### 2. **Middle: Traverse the Gap**

Move back and forth between *what is* (the old understanding) and *what could be* (the new insight).

- Present the **background** needed to understand the problem (3–4 slides, not exhaustive).
- Sketch the **approach** (high level; omit the dead ends and false starts).
- Unfold the **results** in logical steps. Let evidence build.
- Each results slide must make **one clear point** — state it in the title or as a caption.
- Use contrast: show limitations of prior work, then show how your work solves them.

Don't just list findings. Show why each one matters.

### 3. **End: Call to Action & New Bliss**

- **Summarize the takeaway:** What does this mean for the field?
- **What's next?** Open questions, future directions, or implications.
- **Leave them with a vision:** Paint a picture of what becomes possible with this insight.

---

## SLIDE-BY-SLIDE STRUCTURE

### Slide 1: Title
- Paper title, your name, affiliation, date (or conference info if applicable)

### Slides 2–3: Motivation & Big Question  
- Why does this problem matter in the broader field?
- What's the scientific significance?
- What gap or question are you addressing?
- **Storytelling principle:** Make the audience *feel* why this matters. Use contrast (current limitations vs. new possibility).

### Slides 4–6: Background  
- Just enough context for the audience to understand the significance.
- Define key concepts without jargon (or define jargon clearly).
- Assume undergraduate-level physics knowledge; offer brief refreshers.
- **Avoid:** Exhaustive history, derivations, or lengthy equations. (Complex math belongs in backup slides.)

### Slides 7–8: Approach / Methods  
- High-level overview of what you did.
- What's the key insight or novelty in your approach?
- Summarize; omit the struggle.

### Slides 9–12: Results (Core of the Talk)  
- This is where most weight belongs.
- **One main plot or figure per slide** (two only if both are needed for a single interpretation).
- **Each results slide has one explicit takeaway** — state it in the slide title or bottom caption.
- **Label every axis with units.** Annotate key features.
- Use contrast: compare to prior results, competing theories, or predictions.
- Build logically — let evidence accumulate toward your conclusion.

### Slide 13: Conclusions & Takeaways  
- What does this mean? Why should physicists care?
- What's the broader impact?
- What questions remain?
- **Storytelling principle:** End with a vision — the new bliss. What becomes possible?

### Slides 14+: Backup Slides (optional)  
- Extra figures, derivations, robustness checks.
- Prepare for likely questions.

---

## CONTENT RULES

### On Equations
- **Minimize them.** Audiences absorb only the simplest in a live talk.
- A messy derivation belongs in a backup slide, not the main flow.
- If you include an equation, explain what it means in words.

### On Jargon
- **Avoid specialized jargon.** Define terms or use plainer language.
- "Fractional charge" is fine; "composite fermion condensate" needs a sentence of explanation first.
- If the term is unavoidable, define it. Then use it consistently.

### On Figures & Visuals
- Prefer pictures and clearly-labeled graphs over walls of text.
- Don't expect the audience to remember earlier slides — keep relevant context visible where needed (without overcrowding).
- Use color purposefully. Avoid rainbow color scales unless there's a reason.
- If using experimental data, error bars and uncertainties matter; show them.

### On Speaker Notes
- Write as **cues, not a script.** Notes should prompt you to speak, not be read aloud.
- Include the key takeaway for each slide (1–2 sentences).
- Note any tricky phrasing or anticipated questions.
- Time each section roughly (e.g., "Motivation: ~1 min, Results: ~5 min").

---

## THE FIVE QUESTIONS TO ASK YOURSELF

Before you finalize each slide, ask:

1. **Why is this slide here?** Does it advance the story?
2. **What is the one idea?** Can I state it in one sentence?
3. **Is it readable?** Would someone in the back row understand it?
4. **Does it fit the time budget?** (~1 minute per slide)
5. **Does it move the audience from *what is* to *what could be*?** Or is it just a fact dump?

If you can't answer these clearly, the slide needs revision.

---

## DELIVERY NOTES (for speaker preparation)

- **Rehearse out loud.** The talk must fit 10 minutes when spoken. Reading is faster than speaking.
- **Don't read slides verbatim.** Face the audience, not the screen. Use notes as memory cues.
- **Vary your tone.** Monotone loses attention. Show enthusiasm and confidence — you're telling a story.
- **Anticipate questions.** Backup slides are for this. Be ready to go deeper if asked.
- **Humor is risky.** Use sparingly, if at all. A physics talk lives or dies on clarity, not jokes.

---

## CHECKLIST: IS THIS PRESENTATION READY?

- [ ] **16:9 aspect ratio**
- [ ] **Sans serif, ≥20pt** for all body text
- [ ] **One idea per slide** — no slide says two things
- [ ] **~10–12 content slides** (not counting title + backups)
- [ ] **Clear narrative arc:** Why (motivation) → What we did (methods) → What we found (results) → So what (conclusions)
- [ ] **Results slides each have one explicit takeaway** in the title or footer
- [ ] **One main figure per results slide;** all axes labeled with units
- [ ] **Equations are minimal;** complex math is in backups
- [ ] **No unexplained jargon.** Every specialized term is defined.
- [ ] **Visuals are legible** on a phone-sized screen
- [ ] **Backup slides are prepared** for anticipated questions
- [ ] **Speaker notes are cues, not a script**
- [ ] **Timing:** Rehearsed aloud; fits 10 minutes

---

## EXAMPLE: NARRATIVE ARC FOR A QUANTUM HALL PAPER

**What is:** Scientists have studied the quantum Hall effect for decades, but understanding fractional filling factors (like ν = 1/3) remains mysterious.

**What could be:** This work reveals a hidden state at half-filling (ν = 1/2) that explains competing behaviors observed in experiments.

**Middle:** Build evidence — show the prediction, the experimental setup, the data, the comparison to prior theories.

**End:** This insight transforms how we think about even-denominator states. It opens the door to predicting new phases.

---

## SOURCES & REFERENCES

- Nancy Duarte, *Resonate: Present Visual Stories That Transform Audiences*
- American Physical Society Presenter Logistics: https://www.aps.org/events/logistics/oral-presentations
- APS Global Physics Summit Presenter Instructions: https://summit.aps.org/attend/presenter-instructions/
- Georgetown Physics Oral Presentation Guidelines
- Carleton Physics Honours Oral Presentation Guidelines
