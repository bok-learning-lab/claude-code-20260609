# Turn a research paper into a 10-slide research talk

## Project context

Faculty often need to present a paper — sometimes their own, sometimes someone else's — to a non-specialist audience: a course they teach, a faculty seminar at the Bok Center, a public talk. The starting material is usually a PDF and a vague sense of "what the audience needs to take away." The output is a slide deck that can be delivered in 15–20 minutes.

This recipe takes a paper (or a structured digest of it, as in `inputs/freeman-2014-active-learning.md`) and produces a **slide outline** in markdown — one slide per `##` heading, with speaker notes underneath in a `> notes:` block. The outline can then be poured into Google Slides, Keynote, Beamer, or `marp` for the final deck.

## What I want you to do

Given a paper input, produce a **10-slide outline** with this exact structure:

1. **Title slide.** Paper title, authors, citation, one-line stake.
2. **Why this matters now.** A hook tied to the audience — for the Bok faculty audience, this might be a current course-design tension or a recent campus conversation.
3. **The question.** State the research question as a single sentence. Resist hedging.
4. **Prior work in one beat.** What the field believed before this paper, and where the gap was.
5. **Methods, in plain language.** Two to four bullets. Skip jargon — name the thing the audience cares about (e.g., "they pooled 225 studies and compared exam scores" rather than "random-effects meta-analysis with Hedges' g").
6. **Key result 1.** The headline number with the unit and the comparison group made explicit.
7. **Key result 2.** A second result that triangulates or qualifies result 1.
8. **The figure to remember.** Reproduce or describe one figure. State what claim the figure supports.
9. **What this changes.** Implications for the audience's practice. Be concrete — "next semester, you could..." beats "this suggests pedagogical implications."
10. **What it does NOT settle.** Limitations and open questions, framed honestly. This is the slide that earns trust.

For each slide:

- The slide body should be **3–5 short bullets**, no more.
- The speaker notes should be **2–4 sentences** in conversational prose — what the presenter would actually say.
- No emoji. No filler ("In this slide, we will see..."). The bullets are notes for the audience; the speaker notes are for the speaker.

## Constraints

- Stay faithful to the paper. Do not invent numbers, claims, or quotes.
- If the input is a digest rather than the full paper, flag any place where the original paper is needed to settle a detail (e.g., "verify exact CI bounds from §Results before publishing slide 6").
- The talk is 15–20 minutes. One slide per ~90 seconds. Resist adding an 11th slide.
- The "what it does NOT settle" slide is mandatory and non-trivial — it is what separates a research talk from an advertisement.
