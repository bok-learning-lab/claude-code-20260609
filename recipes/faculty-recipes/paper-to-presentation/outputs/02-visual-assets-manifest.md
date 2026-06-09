# Visual Asset Manifest: "The Half-Full Landau Level"

**Talk:** 10-minute APS-style physics conference presentation  
**Audience:** Condensed matter physicists (familiar with quantum Hall effect, but may not know composite fermion details)  
**Visual Style:** Academic; clean line drawings; extracted figures from paper where possible; custom SVG diagrams for conceptual illustrations; minimal animation

---

## VISUAL LANDSCAPE

**Motivation slides (2–3):** Text-forward but need one key visual showing experimental anomaly.  
**Background slides (4–5):** Diagram-heavy; these are foundational concepts that must be visualized clearly.  
**Methods slides (6–7):** Conceptual schematics comparing two frameworks; benefit greatly from side-by-side visuals.  
**Results slides (8–10):** Mix of extracted data, custom comparison diagrams, and a decision tree.  
**Conclusions slides (11–13):** One connection diagram; mostly text summarizing the roadmap.

**Overall:** ~8 custom visuals, 1–2 extracted from paper, 0–1 animations (optional, depends on time budget).

---

## VISUAL ASSET MANIFEST

### Asset 1: Landau Level Quantization Diagram
**Slide:** 4 ("Landau Levels in a Magnetic Field")  
**Concept:** Show how a perpendicular magnetic field quantizes electron energy into discrete, degenerate Landau levels. Audience needs to visualize: (a) the applied field B, (b) the quantization axis, (c) discrete energy levels, (d) the number of states per level equals the number of flux quanta.

**Asset type:** Custom conceptual schematic

**Description:**
- Left panel: 2D electron gas shown from above; arrows indicate perpendicular magnetic field B pointing out of page (⊙ symbol).
- Center: Energy diagram showing three Landau levels (LL0, LL1, LL2) stacked vertically. Each level is drawn as a thick, degenerate band (represented as a shaded box with height indicating degeneracy).
- Right panel: Zoom-in on one Landau level; show it contains Nφ states (one per flux quantum). Label a few orbitals as circles/dots.
- Annotation: Label "ν = N_e / Nφ" (filling factor). Highlight "ν = 1/2 case: one electron per *two* flux quanta."
- Color: Black outline, light blue fill for field region, gray for energy levels, red label for the filling factor.

**Visual elements:**
- Axes: Energy (vertical), spatial (horizontal, showing sample edges)
- Labels: B (magnetic field), Nφ (flux quanta per level), ν (filling factor)
- Legend: One Landau level box = degenerate set of LL orbitals

**Animation:** None needed. Static diagram is sufficient.

**Alt-text / Caption:** "Landau level quantization in a perpendicular magnetic field. The degeneracy of each level equals the number of flux quanta Nφ."

**Creation notes:**
- **Tool:** Inkscape or Adobe Illustrator; simple geometry (boxes, circles, arrows)
- **Time estimate:** 30–45 minutes to make publication-quality
- **Dependencies:** None. Can be created independently.
- **Notes:** Keep it clean and simple. This is foundational; students should understand it cold.

---

### Asset 2: Particle-Hole Symmetry Schematic
**Slide:** 5 ("Particle-Hole Symmetry at ν = 1/2")  
**Concept:** Visualize the duality between electrons and holes. Show that a state with filling ν has a partner state at 1 − ν with the same energy. Highlight the special case: ν = 1/2 is self-dual.

**Asset type:** Custom conceptual schematic (comparison)

**Description:**
- Top row: Fermi surface illustration for ν = 1/3 (filled circle inside a larger circle; filled region = occupied states; empty circle = unoccupied).
- Arrow labeled "Particle-Hole Transform" (or "PH Symmetry") pointing downward and to the right.
- Bottom row: Fermi surface for ν = 2/3 (note: 1 − 1/3 = 2/3). The filled and empty regions are swapped.
- Bottom-center: Special case box showing ν = 1/2 Fermi surface (semicircle, half-filled). Arrow pointing to itself with label "Self-Dual: ν = 1 − ν."
- Color: Dark blue for filled states, light blue for empty states. Make the symmetry visually obvious.

**Visual elements:**
- Fermi surfaces shown as circles (schematic momentum-space picture)
- Arrow: large, clear, labeled
- Units: none (momentum space is schematic)

**Animation:** None. Static comparison diagram.

**Alt-text / Caption:** "Particle-hole symmetry maps ν → 1 − ν. At ν = 1/2, the state is self-dual (maps to itself)."

**Creation notes:**
- **Tool:** Inkscape; circles and arrows
- **Time estimate:** 20–30 minutes
- **Dependencies:** None.
- **Notes:** Make the visual symmetry obvious—swapped colors help. The self-dual case (ν = 1/2) should stand out.

---

### Asset 3: Composite Fermion Picture (HLR Framework)
**Slide:** 6 ("Composite Fermions: The Original Picture")  
**Concept:** Explain the composite fermion picture: electrons + flux attachment → composite fermions in zero effective field. Show the transformation conceptually and the resulting Fermi sea.

**Asset type:** Custom conceptual schematic (two-panel before/after)

**Description:**
- **Left panel (Before):** Electron in magnetic field B. Show: (a) electron (negative circle, labeled "e−"), (b) applied field B (⊙ pointing out), (c) magnetic field lines around the electron (classically spiraling).
- **Middle:** Transformation arrow labeled "Attach 2 flux quanta" or "Singular gauge transform."
- **Right panel (After):** Composite fermion (electron + 2 flux quanta bound together, drawn as a larger circle containing the electron and two flux symbols φ). Label: "Composite fermion (CF)." Show effective field B_eff = 0 (or ~0) with crossed-out magnetic field symbol.
- **Below:** Fermi sea schematic. Draw a circle (Fermi surface in momentum space) filled with states up to the Fermi level kF. Label "Fermi sea of composite fermions, zero effective field."

**Visual elements:**
- Electron: small blue circle with "−" label
- Flux quanta: small φ symbols or tiny circles
- Fermi surface: black circle, filled region shaded
- Field: B (large, clear), B_eff (crossed-out or ~0)

**Animation:** Optional: animate the flux attachment (2 flux symbols flying toward the electron from the field, then binding). Very simple 2–3 second animation. Not essential for understanding.

**Alt-text / Caption:** "HLR picture: electrons + flux attachment create composite fermions that see zero effective magnetic field, forming a Fermi sea."

**Creation notes:**
- **Tool:** Inkscape for diagram; Inkscape or CSS/SVG for animation (if desired)
- **Time estimate:** 
  - Static diagram only: 30–40 minutes
  - With simple animation: 1–1.5 hours (learning curve for animation tool)
- **Dependencies:** None for static; animation is optional.
- **Notes:** Keep it schematic, not realistic. The goal is conceptual clarity, not physical accuracy. The flux attachment is the key insight.

---

### Asset 4: Son-Dirac Comparison (Dirac Fermions)
**Slide:** 7 ("Son-Dirac: An Alternative Formulation")  
**Concept:** Show that Son-Dirac uses Dirac fermions (relativistic dispersion) instead of non-relativistic particles. Highlight the absence of the Chern-Simons term (ada), which manifests particle-hole symmetry.

**Asset type:** Custom comparison diagram (left: HLR, right: Son-Dirac)

**Description:**
- **Left column (HLR recap):**
  - Dispersion relation: parabola (E ∝ k²), labeled "Non-relativistic"
  - Chern-Simons term: formula "ada / 8π" shown; maybe a cartoon of a gauge field loop
  - Density: ρ(r) = electron density nel(r)
  
- **Right column (Son-Dirac):**
  - Dispersion relation: two straight lines crossing at origin (±E = v_D |p|), labeled "Dirac (linear)"
  - No Chern-Simons term: box labeled "NO ada term" with a checkmark ✓
  - Density: ρ_DF related to local B field, not nel(r)
  - Add note: "Berry phase = π" (as a label on the crossing point)

- **Below both:** Outcome: "Both theories predict the same Fermi sea at ν = 1/2" with an equality sign.

**Visual elements:**
- Graphs: Energy (vertical) vs. momentum (horizontal), both linear scale
- Parabola and crossing lines should be clearly distinct
- Color: HLR (blue), Son-Dirac (orange/red)
- Checkmark and "NO" should be visually prominent

**Animation:** None needed. Static side-by-side comparison.

**Alt-text / Caption:** "Son-Dirac uses relativistic Dirac fermions and has no Chern-Simons term, manifesting particle-hole symmetry explicitly."

**Creation notes:**
- **Tool:** Inkscape or matplotlib/Asymptote for the dispersion curves
- **Time estimate:** 40–50 minutes (drawing curves precisely takes time)
- **Dependencies:** Asset 3 (HLR picture) should already be created for comparison.
- **Notes:** The visual difference (parabola vs. lines) should be obvious. This is a powerful comparison—use color effectively.

---

### Asset 5: Jain Fractions & Energy Gaps (Where They Agree)
**Slide:** 8 ("HLR vs. Son-Dirac: Predictions That Agree")  
**Concept:** Show quantized Hall states at Jain fractions (ν = p/(2p+1)) as discrete points. Visualize that both theories predict gaps at these fractions.

**Asset type:** Custom schematic or chart (data-like representation)

**Description:**
- **Horizontal axis:** Filling factor ν (from 0 to 1), with ν = 1/2 marked prominently.
- **Vertical axis:** Energy gap Eg (in arbitrary units, increasing upward).
- **Data points:** Dots at ν = 1/3, 2/5, 3/7, 4/9, etc. (Jain fractions). Each dot at a height proportional to (roughly) |2p+1|−1 (smaller gaps for larger p).
- **Highlight:** Use one color for HLR predictions, another for Son-Dirac predictions. Overlay them—they should coincide perfectly at these points.
- **Annotation:** "Both HLR and Son-Dirac predict energy gaps at the same filling factors" in a box.
- **Note:** Add a hollow circle at ν = 1/2 with a label "No gap (gapless Fermi liquid)" and maybe a downward arrow.

**Visual elements:**
- Axes: ν (horizontal, 0–1), Eg (vertical, 0–some max)
- Dots/points: size consistent, colors distinct (HLR vs. Son-Dirac)
- Labels: ν values (0, 1/3, 2/5, 1/2, 3/5, 2/3, ..., 1)

**Animation:** None. Static plot.

**Alt-text / Caption:** "Jain fractions (ν = p/(2p+1)) show energy gaps predicted equally well by both HLR and Son-Dirac theories."

**Creation notes:**
- **Tool:** Matplotlib (Python) or Inkscape
- **Time estimate:** 25–35 minutes
- **Dependencies:** Understanding of Jain fractions (background section, slide 4).
- **Notes:** This slide is reassuring—it shows where the two theories *do* agree. Make the overlap visually obvious.

---

### Asset 6: PH Symmetry Violation in HLR (Where They Disagree)
**Slide:** 9 ("Subtle Differences at Next Order")  
**Concept:** Show that HLR predicts a static structure factor S(q) with a prefactor that violates PH symmetry, while Son-Dirac respects it. Make the disagreement concrete.

**Asset type:** Custom comparison diagram (response function or structure factor)

**Description:**
- **Horizontal axis:** Filling factor ν (centered at ν = 1/2).
- **Vertical axis:** Some observable (e.g., structure factor prefactor, or response function coefficient).
- **Left of ν = 1/2:** Show two curves (HLR and Son-Dirac) approaching ν = 1/2 from below.
- **Right of ν = 1/2:** Show the same curves approaching from above.
- **HLR curve:** Non-symmetric (say, larger on the left than the right, or a kink at ν = 1/2).
- **Son-Dirac curve:** Perfectly symmetric about ν = 1/2 (mirror image).
- **Annotation:** "HLR violates PH symmetry" (red box around asymmetry), "Son-Dirac respects it" (green checkmark on symmetric curve).

**Visual elements:**
- Curves: smooth, two distinct lines (one dashed, one solid, for clarity)
- Symmetry: evident visually (mirror vs. non-mirror)
- Labels: ν at key points (1/3, 2/5, 1/2, 3/5, 2/3), observable value on vertical axis

**Animation:** None.

**Alt-text / Caption:** "HLR (dashed) and Son-Dirac (solid) predictions diverge at next order in |Δν|. HLR violates particle-hole symmetry; Son-Dirac respects it."

**Creation notes:**
- **Tool:** Matplotlib or Inkscape
- **Time estimate:** 30–40 minutes (drawing smooth curves, getting the asymmetry right)
- **Dependencies:** Understanding of PH symmetry (slide 5, asset 2).
- **Notes:** This is the heart of the disagreement. Clarity here is crucial. Use symmetry/asymmetry as a visual cue.

---

### Asset 7: Three Possibilities Decision Tree (Open Question)
**Slide:** 10 ("Is HLR Fundamentally Compatible with Particle-Hole Symmetry?")  
**Concept:** Show the three possible resolutions to the HLR vs. Son-Dirac puzzle. Make it a clear, branching visualization.

**Asset type:** Custom decision tree or flowchart

**Description:**
- **Root node (top):** "HLR violates PH symmetry at next order. Why?"
- **Three branches, each leading to an outcome:**
  
  1. **Left branch:** "Vertex corrections restore it"
     - Outcome: "HLR ≡ Son-Dirac" (equivalence sign)
     - Color: Green (optimistic, problem solved)
  
  2. **Center branch:** "HLR is incomplete"
     - Outcome: "Son-Dirac is correct" (checkmark on Son-Dirac)
     - Color: Neutral/yellow
  
  3. **Right branch:** "PH violation is regime-specific"
     - Outcome: "Both theories have validity regions"
     - Color: Orange (caution, more complex)

- **Below:** Add icons or small labels for each outcome (e.g., ≡ for equivalence, ✓ for validity, ⚠ for caution).

**Visual elements:**
- Flowchart structure: clear branching, easy to follow
- Text: concise labels, no jargon
- Color: use color to convey attitude (green = solved, etc.)
- Arrows: clear directionality

**Animation:** None (optional: branches could appear sequentially, but not necessary).

**Alt-text / Caption:** "Three possible resolutions: (1) vertex corrections restore PH symmetry, (2) HLR is incomplete, (3) both theories are valid in different regimes."

**Creation notes:**
- **Tool:** Inkscape, OmniGraffle, or even PowerPoint/Keynote
- **Time estimate:** 20–30 minutes
- **Dependencies:** Slides 6–9 (both frameworks and their differences).
- **Notes:** Make this visually engaging—the three branches should feel like genuine alternatives, not a straw-man conclusion.

---

### Asset 8: Connection to ν = 5/2 (Implications)
**Slide:** 11 ("Why This Matters: The 5/2 State")  
**Concept:** Show how understanding ν = 1/2 (gapless) connects to ν = 5/2 (gapped with non-Abelian statistics). Visualize the hierarchy: ν = 1/2 is foundational for understanding the second Landau level.

**Asset type:** Custom schematic (nested/hierarchical diagram)

**Description:**
- **Top level:** "Lowest Landau level (LL0)"
  - ν = 1/2 (gapless, our focus)
  - PH symmetry question
- **Down arrow:** labeled "Lessons learned" or "Principles"
- **Bottom level:** "Second Landau level (LL1)"
  - ν = 5/2 (gapped, exotic)
  - Non-Abelian statistics (potential qubit)
  - PH symmetry breaking observed (?)

- **Annotation:** "Theory at ν = 1/2 constrains theory at ν = 5/2" (draw connecting lines).

**Visual elements:**
- Boxes or cards for each level
- Arrow showing upward learning/application
- Icons: (○) for gapless, (■) for gapped, ⚛ for quantum (just suggestions)

**Animation:** None.

**Alt-text / Caption:** "Understanding half-filling in the lowest Landau level provides the foundation for understanding the exotic ν = 5/2 gapped state in the second Landau level."

**Creation notes:**
- **Tool:** Inkscape or simple diagramming tool
- **Time estimate:** 20–25 minutes
- **Dependencies:** Background knowledge of Landau level structure (not visual—just conceptual).
- **Notes:** This is a "big picture" diagram. It should feel like an inverted pyramid: specific case (ν = 1/2) → general principle → broader application (ν = 5/2).

---

### Asset 9 (Optional): Weiss Oscillations Plot (Backup)
**Slide:** B3 ("Weiss Oscillations and Commensurability")  
**Concept:** Show experimental data on magnetoresistance oscillations and how both HLR and Son-Dirac predict them. This is supporting evidence for both theories.

**Asset type:** Extracted figure from paper + possibly annotated plot

**Description:**
- **Plot:** Longitudinal magnetoresistance (ρxx) vs. effective magnetic field (ΔB or ε, deviation from ν = 1/2).
- **Key feature:** Oscillations at periodic intervals in ΔB.
- **Overlay predictions:** Both HLR and Son-Dirac predict peak positions; overlay theoretical curves on experimental data.
- **Annotation:** Mark peak positions; add vertical lines showing theoretical predictions; label which theory predicts which peak.

**Visual elements:**
- Axes: ΔB (horizontal), ρxx (vertical), both linear scale
- Experimental data: points with error bars or a line
- Theoretical predictions: dashed lines (HLR), solid lines (Son-Dirac), overlapping at peaks

**Animation:** None.

**Alt-text / Caption:** "Weiss oscillations in magnetoresistance near ν = 1/2. Both HLR and Son-Dirac theories predict the oscillation frequencies (to next order), confirming composite fermion physics."

**Creation notes:**
- **Tool:** Extract from paper (if figure exists) or use matplotlib to create a idealized plot
- **Time estimate:** 15–20 minutes (if creating from scratch); 5 minutes (if extracting + light annotation)
- **Dependencies:** Paper figures; understanding of Weiss oscillations (backup slide topic).
- **Notes:** This is optional. Include only if you have time and want to show experimental validation. Great for backup slides or Q&A.

---

## SIMPLIFICATION WATCH

### Landau Level Diagram (Asset 1)
**Potential issue:** A diagram of Landau levels can look like classical orbits, misleading the audience into thinking electrons are classically circling. They're not—they're in stationary quantum states.

**Honest version:** Use symbolic orbitals (circles for levels), not classically-drawn loops. Emphasize "degenerate states" language, not "orbits."

---

### Composite Fermion Picture (Asset 3)
**Potential issue:** Drawing flux quanta as bound to an electron can suggest physical objects, when they're actually mathematical artifacts of a gauge transformation. The image might make students think "flux sticks to electrons" in a literal sense.

**Honest version:** Label the transformation as "singular gauge transform" (not just "attaching flux"). In speaker notes, clarify: "This is a mathematical trick—we're not literally gluing flux to electrons, but using a gauge transformation to make the problem solvable."

---

### Son-Dirac Dispersion (Asset 4)
**Potential issue:** Drawing Dirac dispersion as E = ±v_D |p| (linear) might suggest these are fundamental relativistic particles, like electrons in a high-energy setting. In reality, they're effective excitations in a 2D quantum Hall system.

**Honest version:** Label them "Effective Dirac fermions (composite fermion excitations)" and clarify in speaker notes that the linear dispersion is a *low-energy approximation*, not exact at high energies.

---

### Particle-Hole Symmetry (Asset 2)
**Potential issue:** The schematic Fermi circles might suggest spherical Fermi surfaces, which is not physically accurate for this system. The Fermi surface is actually in k-space and is shaped by the Landau level structure.

**Honest version:** Use a caption: "Schematic Fermi surface (not to scale or shape)." Focus on the *conceptual* symmetry (filled ↔ empty), not the geometric details.

---

## ASSET CREATION ROADMAP

**Phase 1 (Foundational, create first — no dependencies):**
1. Asset 1 (Landau levels) — ~40 min
2. Asset 2 (PH symmetry) — ~25 min

**Phase 2 (Framework diagrams, depends on Phase 1):**
3. Asset 3 (HLR composite fermions) — ~40 min (with optional animation: +1 hour)
4. Asset 4 (Son-Dirac comparison) — ~50 min

**Phase 3 (Results & analysis, depends on Phases 1–2):**
5. Asset 5 (Jain fractions chart) — ~30 min
6. Asset 6 (PH violation curve) — ~35 min

**Phase 4 (Synthesis & conclusions, depends on all prior):**
7. Asset 7 (Decision tree) — ~25 min
8. Asset 8 (ν = 5/2 connection) — ~25 min

**Phase 5 (Optional, independent):**
9. Asset 9 (Weiss oscillations) — ~20 min (if extracting from paper) or ~60 min (if creating from scratch)

**Total estimated time:**
- Minimal (no animations, no Asset 9): ~3.5–4 hours
- Standard (all 8 assets, no animations): ~4–4.5 hours
- Rich (all 8 assets + Asset 9): ~4.5–5 hours
- Animated (+ simple animation in Asset 3): ~5–5.5 hours

---

## VISUAL METAPHORS (OPTIONAL)

### "Composite Fermion as a Dressed Electron"
A composite fermion is like an electron dressed in a coat of flux quanta. The coat doesn't change the electron's identity, but it changes how the electron *feels* the external magnetic field. In the HLR picture, once dressed, the electron (now a CF) no longer feels the field (B_eff ≈ 0). This metaphor is **scientifically defensible** and helps intuition.

**Use it in speaker notes:** "Think of the composite fermion as an electron dressed in a coat of magnetic flux. The coat shields the electron from the external field, so the CF moves as if in zero field."

### "Particle-Hole Symmetry as a Mirror Flip"
Exchanging electrons and holes is like flipping a Fermi surface in a mirror. ν = 1/2 is the special point where the mirror is right in the middle—the state maps to itself. This is **clear and helps intuition**.

**Use it in speaker notes:** "PH symmetry is a mirror flip: electrons ↔ holes. At half-filling, the mirror passes through the Fermi surface, so the state is self-dual."

### "Landau Level as a Parking Lot"
A Landau level can be imagined as a parking lot with as many spaces as flux quanta. At ν = 1/2, half the spaces are filled. This metaphor is **okay but slightly imprecise** (it suggests classical positions, when we're in quantum states). Use cautiously.

**Avoid using this in the main talk.** It's too simplistic. Save it for informal Q&A if someone asks for an analogy.

---

## SUMMARY

This presentation uses **visuals strategically**: foundational concepts (Landau levels, PH symmetry) are visualized clearly; framework diagrams (HLR vs. Son-Dirac) use side-by-side comparison; results slides show where theories agree and disagree using data-like plots; and synthesis slides use decision trees and connection diagrams to show broader implications.

**Visual register:** Clean academic style; extracted figures where possible; custom SVG diagrams for clarity; no decorative elements; colors used sparingly but effectively (e.g., blue/orange for HLR/Son-Dirac, green/red for agreement/disagreement).

**Animation:** Optional in Asset 3 (flux attachment animation) — improves engagement but not essential. All other assets are static.

**Backup assets:** Asset 9 (Weiss oscillations) is good for questions or if time permits; focus on Slides 1–13 first.

---

## NEXT STEP

Once you approve this manifest (and create the visual assets themselves, or delegate to a designer), pass it to the deck builder (`03-build-deck.md`) along with the approved outline. The deck builder will embed visuals into the slides at exactly the right places.

