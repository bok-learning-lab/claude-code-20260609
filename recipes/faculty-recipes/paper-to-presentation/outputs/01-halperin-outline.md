# Slide Outline: "The Half-Full Landau Level"

**Paper:** Bertrand I. Halperin, "The Half-Full Landau Level" (2020)  
**Talk Format:** 10-minute APS-style contributed oral  
**Slide Count:** 12 content slides + title + backups

---

## NARRATIVE ARC

**What is:** At ν = 1/2 filling, the Landau level exhibits non-trivial low-energy phenomena without an energy gap. The HLR (Halperin-Lee-Read) theory explained much of this behavior through composite fermions, but questions remain about whether it respects particle-hole symmetry.

**What could be:** A unified understanding that respects particle-hole symmetry at half-filling—one where two competing theories (HLR and Son-Dirac) are shown to be fundamentally equivalent, revealing deeper principles about gapless quantum Hall states.

---

## SLIDE-BY-SLIDE OUTLINE

### Slide 1: Title Slide
**Title:** The Half-Full Landau Level: Composite Fermions and Particle-Hole Symmetry

**Visual:** (minimal—just title, author, affiliation, date)

**Speaker Notes:**  
Good morning. I'm going to talk about a puzzle that has fascinated condensed-matter physicists for nearly three decades: what exactly is happening at half-filling of the lowest Landau level. We have two competing theories that work beautifully, but it's still unclear whether they're describing the same physics.

---

### Slide 2: The Problem—What We Observe (Motivation)
**Title:** ν = 1/2: Gapless But Non-Trivial

**Key idea:** No energy gap, no quantized Hall plateau—yet non-trivial physics persists.

**Content on slide:**
- Half-full Landau level: one electron per flux quantum
- Hall conductance: smooth, not quantized
- But: surface acoustic wave anomalies (Willett et al., 1990)

**Speaker Notes:**  
Here's the puzzle. In the GaAs quantum wells that experimental groups study, when the Landau level is exactly half-full (filling factor ν = 1/2), you don't see a Hall conductance plateau like you do at filling factors 1/3 or 2/5. The Hall conductance varies smoothly with electron density. You might think the system is boring, disordered, or metallic. But in 1990, Willett's group discovered something strange: surface acoustic waves propagate anomalously near ν = 1/2. That was the signal that something interesting—and ordered—was happening at half-filling.

---

### Slide 3: The Big Question (Motivation, continued)
**Title:** Two Competing Descriptions (2015 onwards)

**Key idea:** HLR theory works, but is it the complete story?

**Content on slide:**
- HLR (1993): Composite fermion Fermi sea + Chern-Simons gauge field
- Son-Dirac (2015): Relativistic Dirac fermions + manifest particle-hole symmetry
- Do they describe the same physics or different theories?

**Speaker Notes:**  
In 1993, Halperin, Lee, and Read proposed a clever picture: treat the electron interactions using a singular gauge transformation that introduces an effective "composite fermion"—an electron bound to two flux quanta. These composite fermions see a zero effective magnetic field on average, forming a Fermi sea, much like ordinary metals. This theory successfully predicted the acoustic wave anomaly and many other phenomena. But it has a flaw: it's not obviously symmetric under particle-hole exchange, even though the underlying electron Hamiltonian is. Twenty-two years later, Son proposed a relativistic description—Dirac fermions coupled to a gauge field—that *manifests* particle-hole symmetry. Both theories make nearly identical predictions for many observable quantities. So the question is: are these just two different ways of writing the same theory, or do they fundamentally disagree?

---

### Slide 4: Background—Landau Levels in a Magnetic Field
**Title:** The Landau Level Picture

**Key idea:** Quantization of electron motion in a perpendicular magnetic field creates discrete, degenerate states.

**Content on slide:**
- Strong perpendicular magnetic field B
- Electrons confined to Landau levels
- Degeneracy: Nφ = flux quanta = number of states
- At ν = 1/2: N_electrons = 0.5 × Nφ

**Speaker Notes:**  
Let me set up the basics. A strong perpendicular magnetic field quantizes the kinetic energy of a 2D electron gas into discrete Landau levels. Each Landau level is highly degenerate—there are as many states as flux quanta threading the sample. If you have exactly one electron per flux quantum, you're at filling factor ν = 1. Half that number (one electron per *two* flux quanta) is ν = 1/2. The challenge is understanding the ground state and low-energy excitations at this special filling factor.

---

### Slide 5: Background—Particle-Hole Symmetry
**Title:** A Hidden Symmetry at ν = 1/2

**Key idea:** When Landau level mixing is negligible, the Hamiltonian is symmetric under swapping electrons and holes.

**Content on slide:**
- Assume: m → 0 (infinite magnetic field)
- No mixing between Landau levels
- Electron at filling ν ↔ Hole at filling 1 − ν
- At ν = 1/2: symmetry maps ground state to itself (or a degenerate partner)

**Speaker Notes:**  
Here's a crucial point. In the limit where the bare electron mass vanishes and we don't mix between different Landau levels, there's an exact particle-hole symmetry. Every eigenstate at filling ν has a partner state at filling 1 − ν with the same energy. At half-filling, ν = 1/2, this symmetry is special: it maps the system to itself. Any complete theory of ν = 1/2 *should* respect this symmetry. But does the Hamiltonian-based HLR theory actually preserve it? That's an open question the paper addresses.

---

### Slide 6: The HLR Framework (Methods)
**Title:** Composite Fermions: The Original Picture

**Key idea:** A singular gauge transformation decouples electrons from the full magnetic field by binding flux to them.

**Content on slide:**
- Attach 2 flux quanta to each electron → composite fermion
- Effective field seen by composite fermions: zero (on average)
- Mean-field ground state: filled Fermi sea
- Spectrum: low-energy excitations of this Fermi sea

**Speaker Notes:**  
The HLR approach begins with an exact unitary transformation—attach two flux quanta to each electron via a singular gauge transformation. In the transformed picture, the electrons now couple to a *Chern-Simons* gauge field. The magic: at ν = 1/2, the effective magnetic field felt by the composite fermions is zero on average. So the mean-field problem becomes a familiar one: a Fermi sea of non-interacting fermions in zero field, which we know how to solve. Corrections come from Coulomb interactions and gauge-field fluctuations, treated perturbatively. The theory has been remarkably successful—it predicts a Fermi surface, quasiparticles, and transport properties that have been observed.

---

### Slide 7: Son-Dirac: An Alternative Formulation (Methods, cont.)
**Title:** Dirac Fermions: The New Picture

**Key idea:** Massless relativistic fermions coupled to gauge fields manifest particle-hole symmetry.

**Content on slide:**
- Composite fermions are Dirac particles (not non-relativistic)
- Berry phase of π as particle goes around Fermi surface
- No Chern-Simons ada term (manifests PH symmetry)
- Fermion density tied to local magnetic field, not electron density

**Speaker Notes:**  
Son's approach takes a different route. He proposes that the low-energy excitations are *massless* Dirac fermions—particles with linear dispersion near zero energy, like those in graphene or topological insulators. These Dirac fermions couple to a gauge field, but crucially, the Chern-Simons term (ada) is absent. This absence is not a loss—it's a feature: it guarantees manifest particle-hole symmetry. The density of Dirac fermions is determined by the local magnetic field, not the electron density. At ν = 1/2, this reproduces the same Fermi sea as HLR. But away from ν = 1/2, the two pictures can differ.

---

### Slide 8: HLR vs. Son-Dirac: Predictions That Agree (Results)
**Title:** Most Observable Quantities: Both Theories Agree

**Key idea:** For many transport and thermodynamic properties, HLR and Son-Dirac make identical RPA predictions near ν = 1/2.

**Content on slide:**
- Nearby quantized Hall states (Jain fractions ν = p/(2p+1))
- Energy gaps at those fractional fillings
- Weiss oscillations in magnetoresistance
- Hall conductance at ν = 1/2 (to leading order)

**Speaker Notes:**  
Here's the reassuring part: if we calculate properties to lowest order in the gap or deviations from ν = 1/2, both HLR and Son-Dirac give the same answer. They predict quantized Hall states at filling fractions like 1/3, 2/5, 3/7—the Jain fractions—with energy gaps that scale in a specific way. They both predict Weiss oscillations, a signature of the composite fermion cyclotron radius. They even agree on the Hall conductance at ν = 1/2, to order (mean-free-path)^{−2}. So if you're doing most experiments, both theories work, and you might not notice the difference.

---

### Slide 9: Where HLR and Son-Dirac Disagree (Results, cont.)
**Title:** Subtle Differences at Next Order

**Key idea:** Discrepancies appear in certain correlation functions and static structure factors, especially when particle-hole symmetry is crucial.

**Content on slide:**
- Static structure factor S(q) as q → 0
- Hall conductivity at order q²
- Certain response functions without particle-hole protection
- HLR violates PH symmetry; Son-Dirac respects it

**Speaker Notes:**  
But there are cracks in the consensus. When you calculate the static structure factor—a measure of density correlations—both theories predict it should vanish as q⁴ for small wave vector q. However, the prefactor differs between HLR and Son-Dirac, with HLR's version violating particle-hole symmetry at next order. Similarly, the Hall conductivity should have a q² correction that is antisymmetric about ν = 1/2 due to PH symmetry. HLR predicts this at leading order, but it's not obvious—you have to be careful. Son-Dirac predicts it automatically because PH symmetry is manifest. These are subtle points, and resolving them is important for understanding whether the two theories are equivalent or genuinely different.

---

### Slide 10: The Open Question: Equivalence or Difference? (Results, cont.)
**Title:** Is HLR Fundamentally Compatible with Particle-Hole Symmetry?

**Key idea:** The central mystery: can vertex corrections in HLR repair the PH-symmetry violations, or does the theory have a fatal flaw?

**Content on slide:**
- HLR at RPA level violates PH symmetry in certain quantities
- Possibility 1: Vertex corrections restore PH symmetry
- Possibility 2: HLR is incomplete and Son-Dirac is the correct description
- Possibility 3: Both are correct but describe different regimes

**Speaker Notes:**  
This is where the paper's main open question lies. The HLR theory, in its simplest form, seems to violate particle-hole symmetry when you look closely at higher-order terms. Now, one possibility is that when you include vertex corrections—the interactions between composite fermions that we've been neglecting—those corrections are just the right amount to restore PH symmetry. In that case, HLR and Son-Dirac would be two equivalent descriptions of the same physics, and we'd understand the deep reason for their agreement. But it's not obvious whether such corrections exist or have the right form. The alternative is that HLR fundamentally cannot be reconciled with PH symmetry, meaning the full microscopic theory must be the Son-Dirac description (or something like it). And there's a third possibility: maybe both theories are correct in their respective domains, and the PH violation is an artifact of how we're approximating HLR.

---

### Slide 11: Why This Matters (Implications)
**Title:** Why Resolve This Question?

**Key idea:** Understanding the equivalence of HLR and Son-Dirac is crucial for gapped states, non-Abelian statistics, and topological quantum computing.

**Content on slide:**
- At ν = 5/2: gapped state with non-Abelian excitations (possible qubit)
- PH symmetry breaking at higher Landau levels?
- Theory must describe the 5/2 state correctly
- Same principles apply to new materials (graphene, etc.)

**Speaker Notes:**  
You might ask: does it matter? After all, for practical calculations, both theories work. But it matters deeply. When you move to the second Landau level and ν = 5/2, you *do* get a gapped state, and the excitations have non-Abelian statistics—potentially useful for quantum computing. Which theory describes 5/2 correctly? The answer hinges on understanding PH symmetry. If HLR is incomplete, we need Son-Dirac or a successor. Moreover, with new materials like graphene and higher Landau levels, the same questions arise. A clean understanding of the half-filled level is the foundation for everything that follows.

---

### Slide 12: Open Questions and Future Directions (Conclusions)
**Title:** What Remains Unsolved

**Key idea:** Multiple fronts of research remain open: vertex corrections in HLR, microscopic derivations of Son-Dirac, effects of disorder and temperature.

**Content on slide:**
- Can HLR be derived from microscopic Hamiltonian?
- Do vertex corrections preserve PH symmetry?
- How do disorder, anisotropy, and temperature affect the physics?
- What about the gapped state at ν = 5/2?

**Speaker Notes:**  
The paper concludes with a roadmap of open questions. First: can the Son-Dirac theory be derived rigorously from a microscopic model, without ad hoc assumptions? Second: if we include all the vertex corrections in the HLR formalism, do they conspire to restore PH symmetry? If yes, HLR and Son-Dirac are equivalent, and we've solved a deep puzzle. If no, then HLR is incomplete. Third: beyond the idealized limit of zero temperature and no disorder, how robust is this picture? Real samples have impurities, anisotropic disorder, and finite temperature effects. Do they preserve the essential physics? And finally: what about the ν = 5/2 state in the second Landau level, where an energy gap *does* appear? Does the same framework apply? The Halperin paper sets the stage for answering these questions.

---

### Slide 13: Key Takeaway (Conclusions, continued)
**Title:** The Half-Filled Landau Level: A Goldmine of Open Questions

**Key idea:** This system is a laboratory for testing fundamental principles of quantum mechanics and condensed matter physics.

**Visual/Content:**
- Nearly three decades of theoretical and experimental work
- Two competing frameworks, almost always in agreement
- The differences matter—for principles and for future applications
- A model problem for understanding quantum Hall physics at even-denominator filling

**Speaker Notes:**  
To summarize: the half-filled Landau level at ν = 1/2 is a remarkable system. No energy gap, yet highly ordered. Two theoretical frameworks describe it almost identically, yet with subtle differences rooted in particle-hole symmetry. Resolving whether these differences are real or artifacts is not just academic—it shapes how we think about the more exotic gapped states at higher fillings, and it tests fundamental principles of symmetry and duality in quantum mechanics. Over the next few years, I expect we'll see progress on all fronts: better experiments, more rigorous theoretical analyses, and new insights from condensed-matter physics and mathematical physics. This is a goldmine of open questions that touches the deepest aspects of quantum Hall physics.

---

## BACKUP SLIDES (Optional)

### B1: Particle-Hole Symmetry in Detail
**Title:** How Particle-Hole Symmetry Works

**Content:**  
- Electron at filling ν creates a state with N = ν × Nφ electrons
- Hole at filling 1 − ν: create a state with (1−ν) × Nφ electrons (or ν × Nφ holes)
- Transformation: (electrons) ↔ (holes); equivalent to flipping the Fermi surface

**Speaker Notes:**  
For those unfamiliar: particle-hole symmetry in a single Landau level is a duality. If you have an electron at position r with momentum k, you can reinterpret it as a hole (absence of an electron) in the background. The ground state at ν must have the same energy and structure as the ground state at 1 − ν, by this symmetry. At ν = 1/2, the symmetry is special because the state is self-dual: 1 − 1/2 = 1/2. So the symmetry maps the ground state to itself.

### B2: The Jain Fractions and Composite Fermion Hierarchy
**Title:** Nearby Quantized States

**Content:**  
- Jain fractions: ν = p / (2p+1) for integer p
- At ν = 1/3, 2/5, 3/7, 4/9: fractional quantum Hall states
- Energy gaps observed; explain via composite fermion picture
- Both HLR and Son-Dirac reproduce these successfully

**Speaker Notes:**  
Near ν = 1/2, there are other quantized Hall states at Jain fractions. For example, ν = 2/5 (p=1), 3/7 (p=2), and 4/9 (p=3). Both HLR and Son-Dirac correctly predict that these states are gapped and explain their properties. This success gives confidence to both theories, at least at leading order.

### B3: Weiss Oscillations and Commensurability
**Title:** A Smoking Gun for Composite Fermions

**Content:**  
- Oscillations in longitudinal magnetoresistance near ν = 1/2
- Periodicity determined by composite fermion cyclotron radius
- Both HLR and Son-Dirac predict the same positions (to order |ΔB|²)
- Experiments confirm predictions; validates both frameworks

**Speaker Notes:**  
One of the most striking confirmations of the composite fermion picture is the observation of Weiss oscillations—periodic bumps in the magnetoresistance as you vary the magnetic field slightly away from ν = 1/2. These oscillations reflect the cyclotron orbits of composite fermions in the small effective magnetic field ΔB they see. Both HLR and Son-Dirac predict the positions of these oscillations, and experiments by Willett's group have verified them to high precision. This is strong evidence that both theories capture something real about the physics.

### B4: Infrared Divergences in the HLR Theory
**Title:** A Technical Issue: Divergences at Low Energy

**Content:**  
- Coulomb interactions in 2D diverge logarithmically at large distances (r → ∞)
- This leads to divergences in the composite fermion effective mass
- Simple solution: work with short-range interactions instead
- Alternatively: these divergences are artifacts of the approximation

**Speaker Notes:**  
A technical note for those interested in the details: the HLR theory predicts that the effective mass of composite fermions diverges logarithmically as you approach ν = 1/2 from away from it. This is because Coulomb interactions, in 2D, fall off as 1/r and lead to logarithmic corrections. It's similar to issues in other low-dimensional systems. One solution is to work with short-range interactions; another is to argue that these divergences are canceled by other effects we're neglecting. This is still an open theoretical question.

---

## TIMING BREAKDOWN

- **Slides 1–3 (Motivation):** ~2 minutes
- **Slides 4–7 (Background & Methods):** ~3 minutes  
- **Slides 8–10 (Results & Open Questions):** ~3 minutes
- **Slides 11–13 (Implications & Conclusions):** ~2 minutes

**Total:** ~10 minutes

---

## NOTES FOR THE PRESENTER

1. **Emphasize the puzzle:** Start with what makes ν = 1/2 special (no gap, yet ordered). This hooks the audience.
2. **Build two frameworks in parallel:** HLR (Slide 6) and Son-Dirac (Slide 7) are both elegant. Show how each works before revealing their differences.
3. **The agreement is the headline:** Slides 8–9 are the heart. Spend time here. Both theories agree on *most* things, which is why the field has moved forward. But the subtle differences (PH symmetry violations in HLR) are the frontier.
4. **Stay conceptual:** Avoid detailed calculations. Use intuition and analogy (e.g., composite fermions as "dressed" electrons, Dirac fermions as relativistic particles).
5. **Backup slides are for depth:** Don't include them in your main 10 minutes. Have them ready for questions.
6. **End with a vision:** The final slide (Slide 13) should leave the audience excited about unresolved questions and future directions.

