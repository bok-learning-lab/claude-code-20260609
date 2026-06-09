# The Half-Full Landau Level: Composite Fermions and Particle-Hole Symmetry

**10-minute APS-style physics conference presentation**  
Based on Bertrand I. Halperin, "The Half-Full Landau Level" (2020)

---

## Slide 1: Title Slide

**Title:** The Half-Full Landau Level: Composite Fermions and Particle-Hole Symmetry

**Visual:** (minimal—just title, author, affiliation, date)

**Speaker Notes:**
Good morning. I'm going to talk about a puzzle that has fascinated condensed-matter physicists for nearly three decades: what exactly is happening at half-filling of the lowest Landau level. We have two competing theories that work beautifully, but it's still unclear whether they're describing the same physics.

---

## Slide 2: ν = 1/2: Gapless But Non-Trivial

**Key idea:** No energy gap, no quantized Hall plateau—yet non-trivial physics persists.

**Content on slide:**
- Half-full Landau level: one electron per flux quantum
- Hall conductance: smooth, not quantized
- But: surface acoustic wave anomalies (Willett et al., 1990)

**Speaker Notes:**
Here's the puzzle. In the GaAs quantum wells that experimental groups study, when the Landau level is exactly half-full (filling factor ν = 1/2), you don't see a Hall conductance plateau like you do at filling factors 1/3 or 2/5. The Hall conductance varies smoothly with electron density. You might think the system is boring, disordered, or metallic. But in 1990, Willett's group discovered something strange: surface acoustic waves propagate anomalously near ν = 1/2. That was the signal that something interesting—and ordered—was happening at half-filling.

---

## Slide 3: Two Competing Descriptions (2015 onwards)

**Key idea:** HLR theory works, but is it the complete story?

**Content on slide:**
- HLR (1993): Composite fermion Fermi sea + Chern-Simons gauge field
- Son-Dirac (2015): Relativistic Dirac fermions + manifest particle-hole symmetry
- Do they describe the same physics or different theories?

**Speaker Notes:**
In 1993, Halperin, Lee, and Read proposed a clever picture: treat the electron interactions using a singular gauge transformation that introduces an effective "composite fermion"—an electron bound to two flux quanta. These composite fermions see a zero effective magnetic field on average, forming a Fermi sea, much like ordinary metals. This theory successfully predicted the acoustic wave anomaly and many other phenomena. But it has a flaw: it's not obviously symmetric under particle-hole exchange, even though the underlying electron Hamiltonian is. Twenty-two years later, Son proposed a relativistic description—Dirac fermions coupled to a gauge field—that *manifests* particle-hole symmetry. Both theories make nearly identical predictions for many observable quantities. So the question is: are these just two different ways of writing the same theory, or do they fundamentally disagree?

---

## Slide 4: The Landau Level Picture

**Key idea:** Quantization of electron motion in a perpendicular magnetic field creates discrete, degenerate states.

**Visual:** Asset 1 (asset-01-landau-levels.svg)
- Left panel: 2D electron gas with perpendicular magnetic field B (⊙ symbol)
- Center: Energy diagram with three Landau levels (LL0, LL1, LL2) stacked vertically
- Right panel: Zoom-in showing Nφ states (circles/dots) in one level
- Annotation: ν = N_e / Nφ, highlighting ν = 1/2 case

**Content on slide:**
- Strong perpendicular magnetic field B
- Electrons confined to Landau levels
- Degeneracy: Nφ = flux quanta = number of states
- At ν = 1/2: N_electrons = 0.5 × Nφ

**Speaker Notes:**
Let me set up the basics. A strong perpendicular magnetic field quantizes the kinetic energy of a 2D electron gas into discrete Landau levels. Each Landau level is highly degenerate—there are as many states as flux quanta threading the sample. If you have exactly one electron per flux quantum, you're at filling factor ν = 1. Half that number (one electron per *two* flux quanta) is ν = 1/2. The challenge is understanding the ground state and low-energy excitations at this special filling factor.

---

## Slide 5: A Hidden Symmetry at ν = 1/2

**Key idea:** When Landau level mixing is negligible, the Hamiltonian is symmetric under swapping electrons and holes.

**Visual:** Asset 2 (asset-02-particle-hole-symmetry.svg)
- Top row: Fermi surface for ν = 1/3 (filled dark blue, empty light blue)
- Transformation arrow: "Particle-Hole Transform"
- Bottom row: Fermi surface for ν = 2/3 (filled/empty regions swapped)
- Bottom-center: Special case ν = 1/2 Fermi surface (semicircle, self-dual, with self-pointing arrow)

**Content on slide:**
- Assume: m → 0 (infinite magnetic field)
- No mixing between Landau levels
- Electron at filling ν ↔ Hole at filling 1 − ν
- At ν = 1/2: symmetry maps ground state to itself (or a degenerate partner)

**Speaker Notes:**
Here's a crucial point. In the limit where the bare electron mass vanishes and we don't mix between different Landau levels, there's an exact particle-hole symmetry. Every eigenstate at filling ν has a partner state at filling 1 − ν with the same energy. At half-filling, ν = 1/2, this symmetry is special: it maps the system to itself. Any complete theory of ν = 1/2 *should* respect this symmetry. But does the Hamiltonian-based HLR theory actually preserve it? That's an open question the paper addresses.

---

## Slide 6: Composite Fermions: The Original Picture

**Key idea:** A singular gauge transformation decouples electrons from the full magnetic field by binding flux to them.

**Content on slide:**
- Attach 2 flux quanta to each electron → composite fermion
- Effective field seen by composite fermions: zero (on average)
- Mean-field ground state: filled Fermi sea
- Spectrum: low-energy excitations of this Fermi sea

**Speaker Notes:**
The HLR approach begins with an exact unitary transformation—attach two flux quanta to each electron via a singular gauge transformation. In the transformed picture, the electrons now couple to a *Chern-Simons* gauge field. The magic: at ν = 1/2, the effective magnetic field felt by the composite fermions is zero on average. So the mean-field problem becomes a familiar one: a Fermi sea of non-interacting fermions in zero field, which we know how to solve. Corrections come from Coulomb interactions and gauge-field fluctuations, treated perturbatively. The theory has been remarkably successful—it predicts a Fermi surface, quasiparticles, and transport properties that have been observed.

---

## Slide 7: Dirac Fermions: The New Picture

**Key idea:** Massless relativistic fermions coupled to gauge fields manifest particle-hole symmetry.

**Content on slide:**
- Composite fermions are Dirac particles (not non-relativistic)
- Berry phase of π as particle goes around Fermi surface
- No Chern-Simons ada term (manifests PH symmetry)
- Fermion density tied to local magnetic field, not electron density

**Speaker Notes:**
Son's approach takes a different route. He proposes that the low-energy excitations are *massless* Dirac fermions—particles with linear dispersion near zero energy, like those in graphene or topological insulators. These Dirac fermions couple to a gauge field, but crucially, the Chern-Simons term (ada) is absent. This absence is not a loss—it's a feature: it guarantees manifest particle-hole symmetry. The density of Dirac fermions is determined by the local magnetic field, not the electron density. At ν = 1/2, this reproduces the same Fermi sea as HLR. But away from ν = 1/2, the two pictures can differ.

---

## Slide 8: Most Observable Quantities: Both Theories Agree

**Key idea:** For many transport and thermodynamic properties, HLR and Son-Dirac make identical RPA predictions near ν = 1/2.

**Content on slide:**
- Nearby quantized Hall states (Jain fractions ν = p/(2p+1))
- Energy gaps at those fractional fillings
- Weiss oscillations in magnetoresistance
- Hall conductance at ν = 1/2 (to leading order)

**Speaker Notes:**
Here's the reassuring part: if we calculate properties to lowest order in the gap or deviations from ν = 1/2, both HLR and Son-Dirac give the same answer. They predict quantized Hall states at filling fractions like 1/3, 2/5, 3/7—the Jain fractions—with energy gaps that scale in a specific way. They both predict Weiss oscillations, a signature of the composite fermion cyclotron radius. They even agree on the Hall conductance at ν = 1/2, to order (mean-free-path)^{−2}. So if you're doing most experiments, both theories work, and you might not notice the difference.

---

## Slide 9: Subtle Differences at Next Order

**Key idea:** Discrepancies appear in certain correlation functions and static structure factors, especially when particle-hole symmetry is crucial.

**Content on slide:**
- Static structure factor S(q) as q → 0
- Hall conductivity at order q²
- Certain response functions without particle-hole protection
- HLR violates PH symmetry; Son-Dirac respects it

**Speaker Notes:**
But there are cracks in the consensus. When you calculate the static structure factor—a measure of density correlations—both theories predict it should vanish as q⁴ for small wave vector q. However, the prefactor differs between HLR and Son-Dirac, with HLR's version violating particle-hole symmetry at next order. Similarly, the Hall conductivity should have a q² correction that is antisymmetric about ν = 1/2 due to PH symmetry. HLR predicts this at leading order, but it's not obvious—you have to be careful. Son-Dirac predicts it automatically because PH symmetry is manifest. These are subtle points, and resolving them is important for understanding whether the two theories are equivalent or genuinely different.

---

## Slide 10: Is HLR Fundamentally Compatible with Particle-Hole Symmetry?

**Key idea:** The central mystery: can vertex corrections in HLR repair the PH-symmetry violations, or does the theory have a fatal flaw?

**Content on slide:**
- HLR at RPA level violates PH symmetry in certain quantities
- Possibility 1: Vertex corrections restore PH symmetry
- Possibility 2: HLR is incomplete and Son-Dirac is the correct description
- Possibility 3: Both are correct but describe different regimes

**Speaker Notes:**
This is where the paper's main open question lies. The HLR theory, in its simplest form, seems to violate particle-hole symmetry when you look closely at higher-order terms. Now, one possibility is that when you include vertex corrections—the interactions between composite fermions that we've been neglecting—those corrections are just the right amount to restore PH symmetry. In that case, HLR and Son-Dirac would be two equivalent descriptions of the same physics, and we'd understand the deep reason for their agreement. But it's not obvious whether such corrections exist or have the right form. The alternative is that HLR fundamentally cannot be reconciled with PH symmetry, meaning the full microscopic theory must be the Son-Dirac description (or something like it). And there's a third possibility: maybe both theories are correct in their respective domains, and the PH violation is an artifact of how we're approximating HLR.

---

## Slide 11: Why Resolve This Question?

**Key idea:** Understanding the equivalence of HLR and Son-Dirac is crucial for gapped states, non-Abelian statistics, and topological quantum computing.

**Content on slide:**
- At ν = 5/2: gapped state with non-Abelian excitations (possible qubit)
- PH symmetry breaking at higher Landau levels?
- Theory must describe the 5/2 state correctly
- Same principles apply to new materials (graphene, etc.)

**Speaker Notes:**
You might ask: does it matter? After all, for practical calculations, both theories work. But it matters deeply. When you move to the second Landau level and ν = 5/2, you *do* get a gapped state, and the excitations have non-Abelian statistics—potentially useful for quantum computing. Which theory describes 5/2 correctly? The answer hinges on understanding PH symmetry. If HLR is incomplete, we need Son-Dirac or a successor. Moreover, with new materials like graphene and higher Landau levels, the same questions arise. A clean understanding of the half-filled level is the foundation for everything that follows.

---

## Slide 12: What Remains Unsolved

**Key idea:** Multiple fronts of research remain open: vertex corrections in HLR, microscopic derivations of Son-Dirac, effects of disorder and temperature.

**Content on slide:**
- Can HLR be derived from microscopic Hamiltonian?
- Do vertex corrections preserve PH symmetry?
- How do disorder, anisotropy, and temperature affect the physics?
- What about the gapped state at ν = 5/2?

**Speaker Notes:**
The paper concludes with a roadmap of open questions. First: can the Son-Dirac theory be derived rigorously from a microscopic model, without ad hoc assumptions? Second: if we include all the vertex corrections in the HLR formalism, do they conspire to restore PH symmetry? If yes, HLR and Son-Dirac are equivalent, and we've solved a deep puzzle. If no, then HLR is incomplete. Third: beyond the idealized limit of zero temperature and no disorder, how robust is this picture? Real samples have impurities, anisotropic disorder, and finite temperature effects. Do they preserve the essential physics? And finally: what about the ν = 5/2 state in the second Landau level, where an energy gap *does* appear? Does the same framework apply? The Halperin paper sets the stage for answering these questions.

---

## SLIDE DECK SPECIFICATIONS

**Format:** 10-minute APS-style contributed oral  
**Slide Count:** 12 content slides + 1 title slide = 13 total  
**Aspect Ratio:** 16:9  
**Font:** Sans-serif (Arial or Helvetica), ≥20pt for body text, 36pt+ for titles  
**Color Scheme:**
- Title background: Dark blue (#1E40AF)
- Accent text: Orange (#FF6600)
- Body text: Dark gray (#333333)
- Background: White

**Visual Assets Embedded:**
- Slide 4: `asset-01-landau-levels.svg` (Landau Level Quantization)
- Slide 5: `asset-02-particle-hole-symmetry.svg` (Particle-Hole Symmetry)

**Timing (estimated):**
- Slides 1–3 (Introduction/Motivation): 2 minutes
- Slides 4–5 (Background): 1.5 minutes
- Slides 6–7 (Methods): 2 minutes
- Slides 8–10 (Results/Analysis): 3 minutes
- Slides 11–12 (Implications/Conclusions): 1.5 minutes
- **Total: ~10 minutes**

**Speaker Notes:**
All speaker notes are provided above for each slide. These notes contain the full argument, nuance, and qualifications that the key bullet points on the slide cue. Rehearse with these notes to ensure smooth delivery and proper timing.

---

## INSTRUCTIONS FOR IMPORTING INTO POWERPOINT OR KEYNOTE

1. **Open your preferred slide software** (PowerPoint, Keynote, or Google Slides)
2. **Create a new blank presentation** (16:9 aspect ratio)
3. **Copy the title and key points** from each section above into a new slide
4. **Set the title bar background color** to dark blue (#1E40AF)
5. **Set the accent text color** to orange (#FF6600) for key ideas
6. **Insert the visual assets** at the specified locations:
   - Slide 4: Embed `asset-01-landau-levels.svg`
   - Slide 5: Embed `asset-02-particle-hole-symmetry.svg`
7. **Add speaker notes** by pasting the "Speaker Notes" text into the Notes field for each slide
8. **Check fonts:** Arial or Helvetica, body text ≥20pt, titles ≥36pt
9. **Rehearse** with the speaker notes and time the talk (aim for ~10 minutes)

---

## DECK VERIFICATION CHECKLIST

- [ ] 13 slides total (1 title + 12 content)
- [ ] 16:9 aspect ratio
- [ ] Sans-serif font, ≥20pt for body text
- [ ] One idea per slide
- [ ] Key idea highlighted in orange on each content slide
- [ ] Visual assets embedded in Slides 4 and 5
- [ ] Speaker notes in Notes field for all slides
- [ ] No decorative filler or unnecessary animations
- [ ] Narrative arc preserved: motivation → background → methods → results → conclusions
- [ ] Rehearsed timing: ~10 minutes at natural speaking pace

---

## NEXT STEPS

✓ **Step 1 (Outline):** Complete  
✓ **Step 2 (Visual Assets Manifest):** Complete  
✓ **Step 3 (Slide Deck):** Complete (this document)  
→ **Step 4 (Optional: Web Version):** See `04-web-version.md` to build an interactive web version

**Ready to rehearse and present!**
