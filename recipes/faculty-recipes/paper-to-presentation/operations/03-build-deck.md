# Prompt template — Build the slide deck from an approved outline

**Purpose:** turn an **approved, edited** slide outline (from `01-outline-deck.md`)
into a real slide deck, **preserving speaker notes** so the argument survives.

**Prerequisite:** run `01-outline-deck.md` first and **edit the outline by hand**.
This step is mechanical; the judgment happened upstream. Garbage outline in,
garbage deck out.

**How to use:** fill in the `{{placeholders}}`, attach/paste the approved outline,
and send.

---

You are building a slide deck from an outline that a physicist has already
reviewed and approved. Your job is faithful execution, not re-editing the
argument. Follow the constraints in `../inputs/physics-conference-presentation-guidance.md`.

**Approved outline:** {{OUTLINE — attach or paste the edited outline; the
output from `01-outline-deck.md` is your input here}}

**Visual assets:** {{ASSETS — list or attach any visual files (SVGs, images,
diagrams, animations). Reference the manifest from `02-visual-assets.md` if you
ran that step. If not, note which figures to extract from the paper.}}

**Output format I want:** {{FORMAT — choose one:
- "a real .pptx file" (most common; ready to present),
- "an HTML/Markdown deck" (if .pptx is not available),
- "leave it as a polished outline I'll build in Keynote/PowerPoint myself"}}

**Visual register:** {{STYLE — e.g. "plain and academic; text-forward; no stock
photos; generous white space; dark background for projection" or "clean and
modern; minimal color; large sans-serif type"}}

**Talk length:** {{TALK_LENGTH — e.g. "10-minute contributed oral" / "20-minute
invited talk"}}

## Rules

1. **One move per slide**, exactly as the outline specifies. Do not merge, split,
   reorder, or "improve" the argument. If something in the outline looks wrong,
   *flag it and ask* — do not silently fix it.

2. **Put the key line on the slide; put the speaker notes in the notes field.**
   Speaker notes are not optional decoration — they carry the nuance, examples,
   and qualifications that make the argument defensible. Preserve them verbatim
   (lightly tightened only for spoken delivery, e.g. "um"s removed). Do not dump
   the notes onto the slide face.

3. **Keep bullets minimal and honest** — only those specified in the outline,
   each a *claim*, never a topic word or label. If the outline says "no bullets
   needed," don't add them.

4. **Quotations stay exact**, with attribution. This is especially important for:
   - The paper's thesis
   - Pivotal objections and replies
   - Key empirical findings or conclusions
   Use the author's own words; don't paraphrase.

5. **Visuals are placed exactly where the outline or manifest says.** If a slide
   calls for a figure, embed it. If the asset isn't ready yet, flag it and mark
   the slide as "[FIGURE TK]" so you can fill it in later.

6. **Restraint over flash.** No decorative filler, no clip-art, no padding
   slides. No animations unless the outline or asset manifest explicitly calls
   for them. A clean, readable deck beats a "designed" one.

7. **Respect the hard constraints:**
   - 16:9 aspect ratio (never 4:3)
   - Sans serif font, 20pt minimum for body text
   - One idea per slide
   - ~10–12 content slides for a 10-minute talk (+ title + backups)
   - All axis labels and annotations legible on a small screen

## If producing a real .pptx

Use the **pptx skill** to generate the file — it is the supported path to a real
PowerPoint, and it **can write speaker notes into the notes field** (essential
here: the notes are where the argument lives).

### Steps:

1. **Create the slide list** — convert the outline into structured data:
   ```
   Slide 1 (Title):
   - Slide title: [from outline]
   - Content on slide: [key line + visual reference if any]
   - Speaker notes: [from outline]
   
   Slide 2 (Motivation):
   - Slide title: [from outline]
   - Content on slide: [key line]
   - Speaker notes: [from outline, expanded for spoken delivery]
   - Visuals: [reference to asset or figure from paper]
   
   [... continue for all slides ...]
   ```

2. **Build the deck** using the pptx skill with:
   - Slide content (titles, key lines, visuals, minimal bullets)
   - Speaker notes (verbatim from outline, preserving nuance)
   - Consistent font and color across all slides
   - Proper spacing (lots of white space, not cramped)

3. **Embed visuals:**
   - Extract figures directly from the paper (with attribution)
   - Embed custom diagrams from the asset manifest (SVGs, PNGs, etc.)
   - Ensure all figures have captions
   - Crop or annotate if needed to highlight the relevant part

4. **After the .pptx is built, report back:**
   - Confirm that speaker notes were preserved (slide-by-slide list: "Slide 2
     (Motivation): ✓ notes preserved")
   - Flag any slide that felt too sparse (just a title and a visual) or too
     dense (too much text on screen)
   - List any "[TK]" placeholders where assets are still needed
   - Suggest font sizes or spacing tweaks if anything feels cramped at
     presentation size

## If producing HTML/Markdown

If .pptx is not practical:

1. **Create a Markdown deck** with explicit structure:
   ```markdown
   # Slide 1: [Title]
   
   ![visual](image.svg)
   
   **Key idea:** [one sentence from outline]
   
   **Notes:**
   [Speaker notes from outline, 2–5 sentences]
   
   ---
   
   # Slide 2: [Motivation]
   
   [... continue ...]
   ```

2. **Or build an HTML deck** that mimics slide presentation:
   - One `<section>` per slide
   - Speaker notes in a `<notes>` block (hidden by default, revealed in
     presenter view)
   - Simple CSS for readability and print-to-PDF support

3. **Deliver as:**
   - A `.md` file the author can import into Keynote/PowerPoint themselves
   - A single `.html` file that displays as slides (use a framework like
     Reveal.js or write vanilla HTML+CSS)
   - A README explaining how to build it in their preferred tool

## Checklist: Is this deck ready to present?

- [ ] **16:9 aspect ratio** across all slides
- [ ] **Sans serif, ≥20pt** for all body text (test on a projector or zoom in)
- [ ] **One idea per slide** — no slide says two things
- [ ] **~10–12 content slides** (not counting title + optional backups)
- [ ] **Clear narrative arc:** Each slide advances the argument from the outline
- [ ] **Speaker notes are in the notes field** (not on the slide face); are they
      preserved verbatim from the outline?
- [ ] **Visuals are embedded and legible** (test on a small screen)
- [ ] **Quotations are exact** (thesis, objection, reply especially)
- [ ] **No decorative filler or unnecessary animations**
- [ ] **Backup slides prepared** for likely questions (optional but encouraged)
- [ ] **Rehearsed timing:** Aloud, at natural speaking pace, the talk fits the
      allocated time

## Common pitfalls (and how to avoid them)

| Pitfall | What goes wrong | How to fix it |
|---------|-----------------|--------------|
| Notes dumped onto slides | Audience reads instead of listens; text is too small | Move all nuance to the notes field. Slide has only the key idea. |
| Bullet-point overload | Argument becomes a checklist; logic is lost | Each slide is one move. Bullets only if the outline specifies them. |
| Merged slides | Two ideas crammed into one slide to save space | Keep them separate. Respect the outline. |
| Paraphrased quotes | Misrepresents what the author said | Use exact quotations for thesis, objection, reply. |
| Pretty but empty | Deck looks polished but doesn't explain | Prioritize clarity and readability over design. White space is your friend. |
| Orphaned visuals | A figure appears with no caption or context | Every visual has a title or caption; speaker notes explain what to look for. |

## Next step

Once you approve this deck, it's ready to rehearse. Use the speaker notes to
practice your talk (out loud, to time it).

If you want to build a web version from this deck, export it to Step 4
(`04-web-version.md`) with your visual assets.
