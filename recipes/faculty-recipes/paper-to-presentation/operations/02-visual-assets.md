# Prompt template — Design visual assets & animated explanations

**Purpose:** identify where visualization would strengthen audience understanding,
then spec out figures, diagrams, and animations that clarify difficult concepts
without oversimplifying the science. This produces a **visual asset manifest**
that bridges the outline and the deck — so the deck builder knows what visuals
to expect.

**Prerequisite:** you have an **approved slide outline** (from `01-outline-deck.md`).

**How to use:** fill in the `{{placeholders}}`, attach the approved outline, and send.

---

You are helping a physicist **design visual assets and animated explanations**
that clarify key concepts in a research paper presentation. The goal is to make
hard ideas *visible* without dumbing them down.

**Approved slide outline:** {{OUTLINE — attach or paste; the stand-in is
`../outputs/sample-deck-outline.md`}}

**Paper or source material:** {{SOURCE — attach the paper PDF or paste key
passages; needed to extract figures and understand notation}}

**Talk length:** {{TALK_LENGTH — e.g. "10 minutes" / "20-minute invited talk"}}

**Audience:** {{AUDIENCE — e.g. "condensed matter physicists" / "mixed physics
faculty, some non-specialists"}}

**Visual constraints/preferences:** {{e.g. "I want hand-drawn diagrams, not
stock graphics" / "I can code SVGs or simple animations" / "I want to keep it
minimal—maybe 2–3 key figures"}}

## Do this

1. **Read the outline and identify visualization points.** For each slide, ask:
   - Does this claim rest on a figure, a spatial arrangement, a process, or a
     pattern that *shows better than it tells*?
   - If the audience can't visualize this, will they understand?
   - What's the simplest diagram or animation that makes it click?

2. **For each visual opportunity, write a spec:** 
   - **Slide number & title** — which outline slide needs this
   - **The concept** — what does this visual need to make clear? (1–2 sentences)
   - **Asset type** — one or more of:
     - Extracted figure (from the paper; which figure number, what annotation)
     - Custom diagram (describe it: axes, labels, flow, structure)
     - Animated sequence (describe the motion and what it illustrates)
     - Conceptual schematic (e.g., a state-space diagram, energy landscape)
     - Comparison chart (side-by-side visual of "before / after")
   - **Visual elements** — axes, labels, color scheme, annotations, legends
   - **Animation (if applicable)** — what moves, how, and why? (e.g., "electron
     filling Landau levels one by one as magnetic field increases")
   - **Alt-text / caption** — what does the visual label say? How do you refer to
     it in speaker notes?

3. **Flag simplification tradeoffs honestly.** If the "obvious" visual would
   mislead (e.g., an energy diagram that suggests a false symmetry, or a cartoon
   that hides important features), say so. Propose the honest version instead.

4. **Suggest asset creation path:**
   - Which figures can be extracted directly from the paper (with permission)?
   - Which need redrawing or annotation?
   - Which are simple enough for SVG or hand-drawn?
   - Which require animation (and in what tool: CSS, SVG animation, or recorded
     video)?

5. **Optional: propose visual metaphors.** If the paper's concept is hard to
   grasp, can you find a useful analogy that a diagram could embody? (E.g.,
   "fractional charge as a shared electron in a Toffoli circuit" or "the Landau
   level filling as a parking lot with one big space.") Metaphors must be
   scientifically defensible or they're worse than useless; flag any that feel
   dangerous.

## Output format

- **"Visual landscape"** — a brief overview of how visuals fit into the talk
  (e.g., "Results section is visual-heavy; motivation is text-forward").
- **"Visual asset manifest"** — numbered entries (one per asset), each with:
  - Slide number & title
  - Concept (what it clarifies)
  - Asset type (extracted / custom diagram / animation / etc.)
  - Description & spec
  - Creation notes (tools, time estimate, dependencies)
- **"Simplification watch"** — places where the "obvious" visual would mislead,
  and how to stay honest.
- **"Asset creation roadmap"** — a rough order for making visuals (what to do
  first, what depends on what, which are quick wins).

## Examples of good visual specs

**Example 1: Animated diagram**
- Slide: "Results—why half-filling is special"
- Concept: Show how electrons fill the Landau level, and why ν = 1/2 forces a
  different phase.
- Asset type: Animated sequence
- Description: A grid of boxes (Landau level orbitals). Electrons appear one by
  one, colored by spin. At ν = 1/2, both spins are half-filled; animation shows
  why this configuration is unstable and triggers a phase transition.
- Animation: ~3 seconds; electrons appear in sequence; final frame holds; no
  sound.
- Caption: "Landau level filling at ν = 1/2: instability of the half-filled
  state."

**Example 2: Extracted + annotated figure**
- Slide: "Experimental setup"
- Concept: Show the geometry of the sample and measurement.
- Asset type: Extracted figure (Fig. 2 from paper) + annotation
- Description: Original Fig. 2 (sample schematic). Add arrows and labels for:
  magnetic field direction, current injection points, voltage probes. Highlight
  the region where the new physics happens.
- Creation: Export Fig. 2 from paper PDF; open in Illustrator or Inkscape; add
  color-coded overlays.
- Caption: "Two-dimensional electron system in a strong perpendicular magnetic
  field. Green region: where fractional charge emerges."

**Example 3: Comparison schematic**
- Slide: "How our result differs from prior theory"
- Concept: Side-by-side energy diagrams showing the old prediction vs. the new one.
- Asset type: Custom comparison diagram
- Description: Left: prior theory's energy landscape (shows one ground state at ν
  = 1/2). Right: our measurement (shows two competing states, one lower-energy).
  Axes labeled; energy in K (Kelvin); ν marked.
- Creation: SVG or TikZ; simple axis + curve shapes.
- Caption: "Prior theory predicted one ground state (left); our data shows two
  (right)."

## When NOT to visualize

- If the concept is abstract and a visual is a metaphor, label it as such. ("This
  schematic is analogous to...")
- If a figure from the paper is already clear, don't redraw it; just extract and
  annotate.
- If an animation would take hours to code and a static diagram does the job,
  choose static.
- If the visualization introduces false precision (e.g., a diagram of a quantum
  phase that looks solid and classical), warn the audience or skip it.

## Next step

Once you approve this manifest, send it to the deck builder (`03-build-deck.md`)
along with the outline. The deck builder will know exactly what visual assets to
expect and where to place them.
