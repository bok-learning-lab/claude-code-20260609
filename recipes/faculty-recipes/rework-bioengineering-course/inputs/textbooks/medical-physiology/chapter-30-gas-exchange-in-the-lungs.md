---
chapter: 30
title: Gas Exchange in the Lungs
authors:
  - Walter F. Boron
section: "V. The Respiratory System"
source_pages: "660–674"
pdf_pages: "672–686"
source_book: "Boron WF, Boulpaep EL. Medical Physiology, 3rd edition (2017)"
figures_listed: "11 (30-1 through 30-11)"
figures_described_from_image: 5
equations: "many — Fick's law $\\dot V_X = D_L (P_1 - P_2)$; lung-extended Fick (Eq. 30-5) with area/thickness/solubility/MW; Fick principle for $\\dot V_{O_2}$ (Eq. 30-10/11); $D_M$ + $\\theta V_c$ partition (Eq. 30-15); $D_{L_{CO}}$ from steady-state and single-breath methods (Eq. 30-25/26); alveolar gas equation $P_{A_{O_2}} = P_{I_{O_2}} - P_{A_{CO_2}}/R$; A-a gradient"
tables: 3
clinical_boxes: "implicit — diffuse interstitial pulmonary fibrosis, COPD, surgical loss of lung tissue, anemia (all on p. 673–674); also IRDS/ARDS forward-linked"
---

# Chapter 30 — Gas Exchange in the Lungs

> Section V · The Respiratory System · pp. 660–674 · Author: Walter F. Boron
>
> This chapter is the **diffusion-physics bridge** between **Ch 29 (O₂ and CO₂ carriage in the blood)** and **Ch 31 (V̇/Q̇ matching, regional gas exchange, A-a gradient pathophysiology)**. It develops Fick's law in the geometry of the alveolar-capillary membrane, separates the lung's diffusing capacity $D_L$ into a **membrane component $D_M$** and a **blood/hemoglobin component $\theta V_c$**, distinguishes **diffusion-limited** from **perfusion-limited** gases via three test molecules (**CO** — purely diffusion-limited; **N₂O** — purely perfusion-limited; **O₂** — normally perfusion-limited, becomes diffusion-limited only under stress), introduces the **DLCO measurement** (steady-state and single-breath) as the clinical readout of $D_L$, and sets up the **alveolar gas equation** $P_{A_{O_2}} = P_{I_{O_2}} - P_{A_{CO_2}}/R$ and the **A-a gradient** as the bedside discriminator among the **five causes of hypoxemia** (low $P_{I_{O_2}}$, hypoventilation, V̇/Q̇ mismatch, shunt, diffusion impairment).

## Chapter map (top-level)

1. **Diffusion of gases** (pp. 660–664) — Fick's law for a dry homogeneous barrier (Eq. 30-3/4); extension to the wet alveolar-capillary barrier with area, thickness, gas MW (Graham), gas solubility (Henry), and an interaction constant (Eq. 30-5); analogy with Ohm's law (Eq. 30-6); the practical impossibility of integrating Fick over all alveoli and all times → use the **Fick principle** (Eq. 30-10/11) and the bookkeeping identity that the two views must give the same total uptake (Eq. 30-12); the 12-mini-barrier dissection of the diffusion pathway (Fig. 30-4) → **membrane diffusing capacity $D_M$** and **blood/hemoglobin component $\theta V_c$** (Eq. 30-13/15).
2. **Diffusion vs. perfusion limitations** (pp. 664–668) — CO as the textbook **diffusion-limited** gas: it never reaches alveolar $P$ within the ~0.75 s RBC transit time, so $\dot V_{CO} \propto D_{L_{CO}}$ and is independent of $\dot Q$ over the physiological range (Fig. 30-5, Table 30-1). N₂O as the textbook **perfusion-limited** gas: equilibrium achieved within the first ~10% of the capillary, so $\dot V_{N_2O} \propto \dot Q$ and independent of $D_L$ (Fig. 30-6, Table 30-2). The **railway-car analogy** (Fig. 30-7) makes the dichotomy mechanical: workers = diffusive capacity; car capacity = Hb binding; train speed = perfusion.
3. **Measuring $D_L$ — the DLCO test** (pp. 668–671) — steady-state method (Fig. 30-8) and single-breath method (Fig. 30-9, the clinical standard); the breakdown $1/D_{L_{CO}} = 1/D_M + 1/(\theta V_c)$ (Eq. 30-26) where both terms contribute roughly equally; **Table 30-3 — factors that affect $D_{L_{CO}}$** (body size, age, sex, lung volume, exercise, body position, $P_{A_{O_2}}$, $P_{A_{CO_2}}$).
4. **O₂ and CO₂ transport are normally perfusion-limited** (pp. 671–674) — at rest, capillary $P_{O_2}$ reaches alveolar $P_{O_2}$ in the first ~one-third of the capillary (Fig. 30-10B). The **$D_L$ reserve for O₂** is so large that halving $D_{L_{O_2}}$ still permits equilibration; only the combination of **exercise + altitude** (Fig. 30-10D) or **exercise + pathology** (Fig. 30-10C, brown curve) pushes O₂ into diffusion-limited territory. CO₂ is normally perfusion-limited despite a small driving gradient (~6 mm Hg) because of its higher solubility and the steepness of the CO₂-dissociation curve (Fig. 30-11). **Reductions in $D_L$ from disease** (fibrosis, COPD, lobectomy, anemia) cause hypoxemia primarily through associated V̇/Q̇ mismatch rather than through diffusion impairment per se — bridging directly into Ch 31.

---

## Section 1 — Diffusion of gases (pp. 660–664)

### Subsection headings (verbatim)
- **Gas flow across a barrier is proportional to diffusing capacity and concentration gradient (Fick's law)** (pp. 660–661)
- **The total flux of a gas between alveolar air and blood is the summation of multiple diffusion events along each pulmonary capillary during the respiratory cycle** (pp. 661–663)
- **The flow of O₂, CO, and CO₂ between alveolar air and blood depends on the interaction of these gases with red blood cells** (pp. 663–664)

### Core claims

#### Fick's law for the alveolar-capillary barrier
- For a barrier separating two gas compartments at partial pressures $P_1$ and $P_2$, unidirectional collision flow on each side is proportional to that side's partial pressure → **net flow is proportional to the partial-pressure difference, not the ratio**. Worked numerical point in the text: $P_1=100,\;P_2=95$ (ratio 1.05) gives **5×** the net flow of $P_1=2,\;P_2=1$ (ratio 2). The driving variable is $\Delta P$, not $P_1/P_2$.
- Convention for the lung: **flow** = molecules/s across the barrier (or volume of gas at STPD per unit time, written $\dot V$); **flux** = flow/area. Respiratory physiologists report $\dot V$ as an STPD volumetric rate (Box 26-3 in source).
- The diffusion proportionality constant is the **lung diffusing capacity $D_L$** (units: mL gas · min⁻¹ · mm Hg⁻¹), giving the simplified Fick form used throughout pulmonary physiology:

$$\boxed{\dot V_{net} = D_L \cdot (P_1 - P_2)} \quad (\text{Eq. 30-4})$$

- **Two gas properties** enter $D_L$ — molecular weight (MW) via **Graham's law** ($D \propto 1/\sqrt{MW}$, since heavier molecules diffuse more slowly) and **water solubility $s$** via **Henry's law** ([gas dissolved] $= s \cdot P_{gas}$). Poorly soluble gases (N₂, He) cross the wet barrier poorly even at the same $\Delta P$ as more soluble gases.
- **Two barrier properties** also enter $D_L$ — **area $A$** (more wall = more collisions = more flow) and **thickness $a$** (more wall = shallower $\Delta P/\Delta x$ → less flow). The skier analogy in the text: a steep "expert" trail and a shallow "beginner's" trail descend the same vertical drop, but the steep one is much faster — same $\Delta P$, but the **gradient $\Delta P/a$** is what drives flow.
- A composite interaction constant $k$ (gas + barrier) closes the form. Substituting these into Eq. 30-4 yields the **extended Fick form for a wet barrier**:

$$\boxed{\dot V_{net} = \frac{k \cdot A \cdot s}{a \cdot \sqrt{MW}} \cdot (P_1 - P_2)} \quad (\text{Eq. 30-5})$$

- **Ohm's-law analogy** (Eq. 30-6): $I = (1/R) \Delta V$. Current ↔ net gas flow; conductance ($1/R$) ↔ $D_L$; voltage difference ↔ $\Delta P$. Used throughout the chapter to reason about resistors in series for the multi-step diffusion pathway.

#### The microscopic-to-macroscopic bookkeeping problem
- Eq. 30-5 describes diffusion across **one uniform barrier patch at one instant** but the lung is **spatially and temporally inhomogeneous**:
  - **$D_L$ varies temporally and spatially** — at end-inspiration the alveolar surface area $A$ is maximal and the barrier thickness $a$ is minimal, so $D_L$ is maximal at end-inspiration (Fig. 30-3A). Across the lung, both $A$ and $a$ differ from alveolar patch to alveolar patch.
  - **$P_{A_{O_2}}$ varies temporally and spatially** — it is highest just after a fresh inspiration and lowest just before the next breath (temporal); it is highest near the apex of an upright lung and lowest near the base (spatial — but recall from Ch 31 that *ventilation* is greater at the base, so the apex-base $P_{A_{O_2}}$ gradient is in the opposite direction one might naïvely expect; this couples to the regional V̇/Q̇ argument).
  - **$P_{c_{O_2}}$ varies along the capillary path** — capillary $P_{O_2}$ rises from mixed-venous (~40 mm Hg) to alveolar (~100 mm Hg) as the RBC transits the capillary, so the driving force $(P_{A_{O_2}} - P_{c_{O_2}})$ falls along the path (Fig. 30-3C).
- The exact integrated form is

$$\dot V_{O_2}^{\text{overall}} = \sum_{\text{patches}} \sum_{\text{time}} D_{L_{O_2}} \cdot (P_{A_{O_2}} - P_{c_{O_2}}) \quad (\text{Eq. 30-9})$$

which is **not practical** for predicting uptake — but is **equal** to the macroscopic **Fick principle** value:

$$\boxed{\dot V_{O_2}^{\text{overall}} = \dot Q \cdot (C_{a_{O_2}} - C_{\bar v_{O_2}})} \quad (\text{Eq. 30-10})$$

with $\dot Q$ = cardiac output and $C$ = total O₂ content of arterial vs. mixed-venous blood. The textbook worked example uses $\dot Q = 5$ L/min, $C_{a_{O_2}} = 20$ mL O₂/dL, $C_{\bar v_{O_2}} = 15$ mL O₂/dL → **$\dot V_{O_2} = 250$ mL O₂/min** at rest (Eq. 30-11), the standard resting metabolic rate target value.

- **The two views must equate** (Eq. 30-12), which is the bookkeeping identity that lets pulmonary physiologists move between **macroscopic Fick-principle** (whole-body O₂ uptake) and **microscopic Fick's-law** (alveolar-level diffusion) reasoning.

#### The 12-mini-barrier dissection (Fig. 30-4) and $D_M$ vs. $\theta V_c$
- The alveolar-capillary barrier is **three-ply at the cellular level** (type I alveolar pneumocyte / interstitium with extracellular matrix / capillary endothelial cell) and **thirteen-step at the molecular level** when one resolves each membrane, each cytoplasm, and the plasma layer:
  1. air–water interface; 2. surface water layer; 3–5. apical membrane / cytoplasm / basolateral membrane of the type I cell; 6. interstitial space (lamina densa of basement membrane, often <50 nm, type IV collagen); 7–9. basal membrane / cytoplasm / apical membrane of the capillary endothelial cell; 10. plasma layer (~0.2 μm in mammals); 11–12. RBC membrane and cytoplasm.
- Each mini-step has a mini-diffusing capacity $D_i$. Because resistors in series add:

$$\frac{1}{D_M} = \frac{1}{D_1} + \frac{1}{D_2} + \cdots + \frac{1}{D_{12}} \quad (\text{Eq. 30-13})$$

  $D_M$ is the **membrane diffusing capacity** — the diffusion-only part of the pathway. Total barrier area is 50–100 m², total thickness ~0.6 μm.
- The final step — **binding to Hb** — is **not** diffusion. It has a finite rate constant $\theta$ (mL gas · min⁻¹ · mm Hg⁻¹ per mL blood). Multiplied by the **pulmonary-capillary blood volume $V_c$**, $\theta V_c$ has the same units as $D_M$ and adds in series:

$$\boxed{\frac{1}{D_L} = \frac{1}{D_M} + \frac{1}{\theta V_c}} \quad (\text{Eq. 30-15})$$

- **The relative magnitude of the two terms depends on the gas**:
  - **O₂**: binds Hb rapidly, $1/(\theta V_c) \approx 5\%$ of $1/D_M$ → $D_{L_{O_2}} \approx D_{M_{O_2}}$ (the kinetic Hb step is negligible).
  - **CO**: binds Hb tightly **but slowly**, so $1/(\theta V_c) \approx 1/D_M$ → both terms contribute about equally to $D_{L_{CO}}$. This is why DLCO falls in **anemia** even though the diffusion pathway itself is unchanged.
  - **CO₂**: 23× more soluble in water than O₂, so naïvely $D_{L_{CO_2}}$ should be ~23× $D_{L_{O_2}}$ — measured ratio is only **3–5×** because CO₂ transport in the RBC involves carbonic anhydrase and the AE1 (Cl⁻/HCO₃⁻) exchanger (Ch 29) and so has a non-trivial $1/(\theta V_c)$ term as well.

### Equations (Section 1)

- **Fick proportionality** (driving force is $\Delta P$, not ratio):

$$\dot V_{net} \propto (P_1 - P_2) \quad (\text{Eqs. 30-1, 30-2, 30-3})$$

- **Lung diffusing-capacity Fick law**:

$$\dot V_{net} = D_L \cdot (P_1 - P_2) \quad (\text{Eq. 30-4})$$

- **Extended Fick** for the wet alveolar-capillary barrier:

$$\dot V_{net} = \frac{k \cdot A \cdot s}{a \cdot \sqrt{MW}} \cdot (P_1 - P_2) \quad (\text{Eq. 30-5})$$

- **Ohm's-law analogue**: $I = (1/R) \Delta V$ (Eq. 30-6).

- **Fick principle** for whole-lung uptake:

$$\dot V_{O_2}^{\text{overall}} = \dot Q (C_{a_{O_2}} - C_{\bar v_{O_2}}) \quad (\text{Eq. 30-10})$$

  Worked example: $\dot V_{O_2} = 5\,\text{L/min} \times (20-15)/100\;\text{mL/mL} = 250$ mL/min (Eq. 30-11).

- **Membrane / blood partition** of $D_L$:

$$\frac{1}{D_L} = \frac{1}{D_M} + \frac{1}{\theta V_c} \quad (\text{Eq. 30-15})$$

### Citation-anchor quotes
- > "Random motion alone causes a net movement of molecules from areas of high concentration to areas of low concentration. Although diffusion per se involves no expenditure of energy, the body must do work — in the form of ventilation and circulation — to create the concentration gradients down which O₂ and CO₂ diffuse." (p. 660)
- > "Note that net flow is proportional to the difference in partial pressures, not the ratio." (p. 660)
- > "The proportionality constant in Equation 30-3 is the diffusing capacity for the lung, $D_L$." (p. 660)
- > "Graham's law states that diffusion is inversely proportional to the square root of molecular weight." (p. 660)
- > "Henry's law … these concentrations are proportional to the respective partial pressures, and the proportionality constant is the solubility of the gas (s). Therefore, poorly soluble gases (e.g., N₂, He) diffuse poorly across the alveolar wall." (p. 660)
- > "The barrier is remarkable not only for its impressive surface area (50 to 100 m²) and thinness (~0.6 μm) but also for its strength, which derives mainly from type IV collagen in the lamina densa of the basement membrane." (p. 663)
- > "Because O₂ binds to Hb so rapidly, its 'Hb' term 1/(θ · V_c) is probably only ~5% as large as its 'membrane' term 1/D_M." (p. 664)
- > "For carbon monoxide (CO), which binds to Hb even more tightly than does O₂ — but far more slowly — θ · V_c is quantitatively far more important." (p. 664)

### Figures (Section 1)

#### Figure 30-1 — Diffusion of a gas across a barrier *(viewed)*

**Panel A — Dry, homogeneous barrier.** A two-compartment box with a vertical barrier of area $A$ and thickness $a$. Side 1 (left, blue) at partial pressure $P_1$, side 2 (right, also blue) at $P_2$, with $P_1 > P_2$. Arrows show three flows: a leftward arrow labeled "Flow$_{1\to 2}$ ∝ $P_1$", a rightward arrow labeled "Flow$_{2\to 1}$ ∝ $P_2$", and a net rightward arrow "Flow$_{net}$ = Flow$_{1\to 2}$ − Flow$_{2\to 1}$ ∝ $(P_1 - P_2)$". The diagram makes the point that diffusion across a dry barrier obeys Fick's law in its simplest form (Eq. 30-3).

**Panel B — Alveolar wall.** Same two-compartment geometry but now Side 1 is **alveolar air** (left, white) at $P_{A_{O_2}}$ and Side 2 is **blood plasma** (right, red) at $P_{c_{O_2}}$. Between them sits a **water film** layer adherent to the alveolar epithelium. The barrier is now an extended physical structure with surface area $A \sim 50–100$ m² and thickness $a$. O₂ molecules are shown dissolving from gas into the water layer according to Henry's law: $[O_2]_w = s \cdot P_{O_2}$ (annotation in the figure). The wet-barrier Fick form $\dot V_{net} = (k A s / a\sqrt{MW})(P_1 - P_2)$ — Eq. 30-5 — is the analytical statement of this geometry.

> Vision note: This is the canonical lung-diffusion diagram of the chapter; everything from "increased thickness in fibrosis lowers $D_L$" to "decreased surface area in emphysema lowers $D_L$" is read off of this figure. Anchor for the pathophysiology list on pp. 673–674.

#### Figure 30-2 — Effect of barrier thickness *(listed)*

Two stacked $P_{O_2}$-vs.-distance plots through the barrier. **Top panel — Thick barrier ($a$ large).** $P_{O_2}$ falls gradually from $P_1=100$ to $P_2=40$ mm Hg over a long horizontal distance; the slope (gradient $\Delta P_{O_2}/\Delta x$) is shallow → low flow. **Bottom panel — Thin barrier ($a$ small).** Same $\Delta P=60$ mm Hg between the same end-points, but compressed into a short horizontal distance; the slope is steep → high flow. The ski-trail analogy in the text (same vertical drop, much steeper trail) is the verbal version of this figure.

#### Figure 30-3 — Complications of using Fick's law *(listed)*

Three-panel composite. **A — Variation of area and thickness during the respiratory cycle.** Two stacked cartoons of the same alveolar-capillary unit at end-expiration and end-inspiration; at end-inspiration the alveolus is stretched (↑$A$, ↓$a$) so $D_L$ is maximal. **B — Variation of alveolar $P_{O_2}$ and $P_{CO_2}$ during the respiratory cycle.** Two stacked $P$-vs.-time traces over one breath; $P_{A_{O_2}}$ peaks just after inspiration (fresh O₂-rich air enters) and dips just before the next breath (perfusion has drained alveolar O₂); $P_{A_{CO_2}}$ is the mirror image. **C — Variation of capillary $P_{O_2}$ along the capillary path.** $P_{c_{O_2}}$ rises from ~40 mm Hg at the mixed-venous end to ~100 mm Hg as it equilibrates with alveolar air, with the equilibration point (~one-third of the way along) labeled "Reaches equilibrium". The driving force for O₂ diffusion is maximal at the start and falls to zero before the end of the capillary.

#### Figure 30-4 — Transport of O₂ from alveolar air to Hb *(viewed)*

A horizontal cutaway through the alveolar wall, from alveolar air (left) to RBC cytoplasm (right). The barrier is drawn as five physical sub-zones — **alveolar air** | **type I alveolar epithelial cell** (with apical membrane + cytoplasm + basolateral membrane) | **interstitial space with extracellular matrix** | **pulmonary capillary endothelial cell** (with three sub-layers) | **blood plasma** | **RBC** (with membrane + cytoplasm + Hb). Twelve numbered diffusion steps are labeled $D_1$ through $D_{12}$ along the path: (1) air-water interface, (2) water layer, (3–5) the two membranes plus cytoplasm of the alveolar type I cell, (6) interstitial space, (7–9) the two membranes plus cytoplasm of the capillary endothelial cell, (10) the thin plasma layer (<0.2 μm in mammals), (11–12) RBC membrane and cytoplasm. A thirteenth label, $\theta \cdot V_c$, identifies the final non-diffusive step: **binding of O₂ to Hb** inside the RBC. The figure caption emphasizes that $D_1$–$D_{12}$ collectively give the **membrane diffusing capacity $D_M$** while $\theta V_c$ is the **blood/Hb component**. The total $1/D_L = 1/D_M + 1/(\theta V_c)$ (Eq. 30-15) — the central partition equation of the chapter.

> Vision note: This is the figure that licenses the DLCO interpretation logic. When DLCO falls in anemia, $\theta V_c$ falls (less Hb to bind CO). When DLCO falls in pulmonary fibrosis, $D_M$ falls (thickened interstitium = larger denominator in step 6). Anchor for the Table 30-3 column "Explanation" and for the pathology list on p. 674.

---

## Section 2 — Diffusion vs. perfusion limitations (pp. 664–668)

### Subsection headings (verbatim)
- **The diffusing capacity normally limits the uptake of CO from alveolar air to blood** (pp. 664–666)
- **Perfusion normally limits the uptake of N₂O from alveolar air to blood** (pp. 666–667)
- **In principle, CO transport could become perfusion limited and N₂O transport could become diffusion limited under special conditions** (pp. 667–668)

### Core claims

#### CO — the prototypical diffusion-limited gas (Fig. 30-5)
- Set-up: subject breathes 0.1% CO briefly. Inspired wet-air CO partial pressure:

  $$P_{I_{CO}} = F_{I_{CO}} \cdot (P_B - P_{H_2O}) = 0.001 \cdot (760 - 47) \approx 0.7 \text{ mm Hg} \quad (\text{Eq. 30-16})$$

  So **alveolar driving pressure $P_{A_{CO}}$ is only ~0.7 mm Hg** — already low.
- Why $P_{c_{CO}}$ rises so slowly along the capillary:
  1. **Low CO flux** (Fick's law with small driving pressure plus moderate $D_{L_{CO}}$).
  2. **Hb continuously traps incoming CO** — Hb's affinity for CO is 200–300× that for O₂, so $P_{c_{CO}}$ (which is proportional to *free* CO, not total CO) stays near zero even as the RBC accumulates CO bound to Hb.
- Result: by the end of the **~0.75-second** capillary transit, $P_{c_{CO}} \ll P_{A_{CO}}$. **CO never reaches diffusion equilibrium.** Therefore the alveolar-to-blood driving gradient stays large throughout transit, and uptake is set by $D_L$, not by perfusion.
- **Quantitative dependence** (Table 30-1, summarized below): if you fix $\dot Q$ and **double $D_{L_{CO}}$**, the $P_{c_{CO}}$ trajectory becomes twice as steep, end-capillary CO content $C_{c'_{CO}}$ doubles, and **$\dot V_{CO}$ doubles**. Conversely, **halving $\dot Q$** lets the blood spend twice as long in the capillary, so $P_{c_{CO}}$ rises twice as steeply *per unit cumulative time*, $C_{c'_{CO}}$ doubles — but the product $\dot Q \cdot C_{c'_{CO}} = \dot V_{CO}$ **is unchanged**. Thus over the physiological range, **$\dot V_{CO} \propto D_L$ and is insensitive to $\dot Q$** — the textbook definition of diffusion limitation.

| Condition | $D_L$ | $\dot Q$ | $C_{c'_{CO}}$ | $\dot V_{CO}$ |
|---|---|---|---|---|
| Control | 1 | 1 | 1 | 1 |
| Double $D_L$ | 2 | 1 | 2 | **2** |
| Halve $D_L$ | ½ | 1 | ½ | **½** |
| Double $\dot Q$ | 1 | 2 | ½ | **1** |
| Halve $\dot Q$ | 1 | ½ | 2 | **1** |

(*Adapted from Table 30-1.*)

- **Diagnostic principle.** Compare end-capillary $P$ with alveolar $P$ for a gas. If the gas **fails to equilibrate** (end-capillary $P$ < alveolar $P$), transport is **diffusion-limited**. If it **does equilibrate**, transport is **perfusion-limited**.

#### N₂O — the prototypical perfusion-limited gas (Fig. 30-6)
- N₂O **does not bind Hb**, so the only sink for incoming N₂O is the small volume of plasma plus RBC cytoplasm in the capillary. As soon as those volumes saturate (i.e., $P_{c_{N_2O}}$ rises to $P_{A_{N_2O}}$), net diffusion ceases.
- $P_{c_{N_2O}}$ reaches $P_{A_{N_2O}}$ at **~10% of the way along the capillary** — diffusion equilibrium is achieved very early.
- For the **distal 90% of the capillary**, the driving pressure is zero and no further diffusion occurs. Total $\dot V_{N_2O}$ is therefore determined by *how much blood passes through the capillary per unit time* — i.e., by $\dot Q$.
- **Quantitative dependence** (Table 30-2): doubling $D_{L_{N_2O}}$ moves the equilibration point even closer to the start of the capillary but **does not change $C_{c'_{N_2O}}$** (which has already reached its maximum) and so **does not change $\dot V_{N_2O}$**. Halving $\dot Q$ doubles the contact time and keeps $C_{c'_{N_2O}}$ at maximum but halves $\dot Q$ and so **halves $\dot V_{N_2O}$**. **$\dot V_{N_2O} \propto \dot Q$, independent of $D_L$** — the textbook definition of perfusion limitation.

| Condition | $D_L$ | $\dot Q$ | $C_{c'_{N_2O}}$ | $\dot V_{N_2O}$ |
|---|---|---|---|---|
| Control | 1 | 1 | 1 | 1 |
| Double $D_L$ | 2 | 1 | 1 | **1** |
| Halve $D_L$ | ½ | 1 | 1 | **1** |
| Double $\dot Q$ | 1 | 2 | 1 | **2** |
| Halve $\dot Q$ | 1 | ½ | 1 | **½** |

(*Adapted from Table 30-2.*)

#### The railway-car analogy (Fig. 30-7)
The textbook's mechanical analogy is one of the chapter's signature pedagogical devices. **Workers** at a railroad siding = diffusion events ($D_L$). **Railway cars** = RBCs with finite capacity = Hb binding capacity. **Train speed** = blood flow $\dot Q$.

- **(A) Perfect match**: every worker is busy; every car leaves the siding fully loaded. Total shipping rate is at maximum.
- **(B) Decreased worker count** (lower $D_L$), normal train speed: cars leave partially empty; shipping rate falls proportionally → **diffusion-limited regime**.
- **(C) Increased worker count** (higher $D_L$), normal train speed: cars still leave fully loaded; shipping rate unchanged → **perfusion-limited regime** (extra workers are wasted because cars cap the throughput).
- **(D) Increased train speed** (higher $\dot Q$), normal worker count: cars leave partially empty (workers can't load fast enough), but shipping rate stays the same because more cars compensate for emptier cars → **diffusion-limited regime**.
- **(E) Decreased train speed** (lower $\dot Q$), normal worker count: cars leave fully loaded, but fewer cars per unit time → shipping rate falls proportionally → **perfusion-limited regime**.

**Reading rule.** Cars **partially empty** → diffusion-limited. Cars **fully loaded** → perfusion-limited. This is the mechanical translation of "fails to reach equilibrium" vs. "reaches equilibrium" (the diagnostic principle above).

### Equations (Section 2)

- **Inspired wet-gas partial pressure**:

$$P_{I_{gas}} = F_{I_{gas}} \cdot (P_B - P_{H_2O}) \quad (\text{Eq. 30-16})$$

  Worked CO example: $0.001 \times (760-47) \approx 0.7$ mm Hg.

- **Fick principle for CO uptake**:

$$\dot V_{CO}^{\text{overall}} = \dot Q \cdot (C_{c'_{CO}} - C_{\bar v_{CO}}) \quad (\text{Eq. 30-17})$$

  In a non-smoker, $C_{\bar v_{CO}} \approx 0$, so

$$\dot V_{CO}^{\text{overall}} \approx \dot Q \cdot C_{c'_{CO}} \quad (\text{Eq. 30-18})$$

### Citation-anchor quotes
- > "By the time the blood reaches the end of the capillary (~0.75 second later), $P_{c_{CO}}$ is still far below alveolar $P_{CO}$. In other words, CO fails to reach diffusion equilibrium between the alveolus and the blood." (p. 665)
- > "The uptake of CO is diffusion limited because it is the diffusing capacity that predominantly limits CO transport. We can judge whether the transport of a gas is predominantly diffusion limited by comparing the partial pressure of the gas at the end of the pulmonary capillary with the alveolar partial pressure." (p. 666)
- > "Unlike CO, nitrous oxide ('laughing gas,' N₂O) does not bind to Hb. … By the time the blood is ~10% of the way along the capillary, $P_{c_{N_2O}}$ has reached alveolar $P_{N_2O}$, and N₂O is thus in diffusion equilibrium between alveolus and blood." (p. 666)
- > "The transport of a gas is predominantly perfusion limited if the gas in the capillary comes into equilibrium with the gas in the alveolar air by the end of the capillary." (p. 667)
- > "Whenever you see cars leaving the siding only partially filled, you can conclude that shipping rate is worker (diffusion) limited … whenever you see cars leaving the siding fully filled, you can conclude that shipping rate is speed (perfusion) limited." (p. 668)

### Figures (Section 2)

#### Figure 30-5 — Diffusion of CO *(viewed)*

**Panel A — CO diffusion** (anatomical cartoon). A single alveolus (yellow) with a capillary loop curling beneath it. The capillary holds a single-file train of RBCs, each annotated as "O₂ occupies three of the four Hb sites" — i.e., the residual fourth Hb site is the one that grabs incoming CO. CO molecules are drawn diffusing from alveolar air into the plasma, with the annotation that the CO flux is small and Hb traps CO so avidly that free $[CO]$ in the plasma stays near zero. **Panel B — $P_{c_{CO}}$ profile.** A graph with x-axis "distance along capillary (%)" 0–100 and y-axis "$P_{c_{CO}}$ (% of alveolar $P_{CO}$)" 0–100. The curve rises slowly and **never reaches the alveolar level (dashed horizontal line at 100%)** — captioned "Because capillary $P_{CO}$ fails to reach alveolar $P_{CO}$ … the uptake of CO is **diffusion limited**." **Panel C — Vary diffusing capacity ($D_L$).** Family of three $P_{c_{CO}}$ trajectories at $D_L$ = ½, 1, 2 (and a fourth "$D_L$ very high" curve that reaches plateau early). All start at zero; the high-$D_L$ curves rise steeply, the low ones gently; none of the physiological-range curves reach 100% by the end of the capillary. **Panel D — Vary blood flow ($\dot Q$).** Family of three $P_{c_{CO}}$ trajectories at $\dot Q$ = ½, 1, 2. Halving $\dot Q$ (slow transit) raises the curve; doubling $\dot Q$ (fast transit) lowers it. **None reach 100% in the physiological range** — i.e., transport of CO remains diffusion-limited across the entire physiological $\dot Q$ range.

> Vision note: This is the textbook's diagnostic chart for "diffusion-limited." The reader is being trained to recognize that **failure to reach the dashed alveolar line is the signature of diffusion limitation**. The same chart pattern, with the curves now hitting the line early, becomes the signature of perfusion limitation (Fig. 30-6) — and the O₂ chart (Fig. 30-10) is the diagnostic puzzle that uses these two to interpret pathology.

#### Figure 30-6 — Diffusion of N₂O *(listed)*

Same four-panel layout as Fig. 30-5. **A — N₂O diffusion** anatomical cartoon, but the RBC annotation is now "N₂O does not bind Hb." **B — $P_{c_{N_2O}}$ profile** — the curve **shoots up to 100% of alveolar $P$ within the first ~10% of the capillary** and then runs flat → diffusion equilibrium achieved early; captioned "perfusion limited." **C — Vary $D_L$** — even doubling or halving $D_L$ does not change the end-capillary value (only changes how early equilibrium is reached). **D — Vary $\dot Q$** — annotations include the contact time: $\dot Q = 0.5 \to \Delta t = 1.5$ s; $\dot Q = 1 \to \Delta t = 0.75$ s; $\dot Q = 2 \to \Delta t = 0.375$ s. Doubling $\dot Q$ halves contact time but does not change end-capillary $P_{c_{N_2O}}$ (because equilibrium is still reached within the shortened time); halving $\dot Q$ doubles contact time, also without changing end-capillary value. Only at very-high $\dot Q$ does the curve fail to reach equilibrium.

#### Figure 30-7 — Railway car analogy *(listed)*

Five-panel cartoon. **A — Perfect match.** A train with railway cars passes a siding where the right number of workers are loading boxes; cars depart full. **B — Decreased number of workers.** Same train speed; not all boxes get loaded; cars depart partially empty → diffusion-limited. **C — Increased number of workers.** Train still moves at normal speed; cars still full (capped by car capacity); extra workers idle → perfusion-limited. **D — Increased train speed.** Cars whip past; even normal workers can't fill them → cars depart partially empty → still diffusion-limited (more workers would help). **E — Decreased train speed.** Cars move slowly; workers fill them completely; but fewer cars pass per hour → perfusion-limited (more train speed would help). The summary rule: *partially-filled cars ⇒ add workers; fully-filled cars ⇒ add speed*.

---

## Section 3 — Measuring $D_L$: the DLCO test (pp. 668–671)

### Subsection headings (verbatim)
- **The uptake of CO provides an estimate of $D_L$** (pp. 668–671)

### Core claims

#### Why CO is the gas of choice for measuring $D_L$
- N₂O is useless for measuring $D_L$: its uptake is essentially independent of $D_L$ (perfusion-limited), and the driving pressure $(P_A - P_c)$ collapses to zero after 10% of the capillary, so there is no reasonable average to plug into Fick's law.
- **CO is ideal** because uptake is diffusion-limited → $\dot V_{CO}$ is nearly proportional to $D_L$. Also, $(P_{A_{CO}} - P_{c_{CO}})$ falls **roughly linearly** along the capillary (Fig. 30-5B), so an average driving pressure $(\bar P_{A_{CO}} - \bar P_{c_{CO}})$ has a stable interpretation.
- The working equation:

$$\boxed{D_{L_{CO}} = \frac{\dot V_{CO}}{\bar P_{A_{CO}} - \bar P_{c_{CO}}}} \quad (\text{Eq. 30-25})$$

  In a non-smoker living in clean air, $\bar P_{c_{CO}} \approx 0$, so $D_{L_{CO}} \approx \dot V_{CO} / \bar P_{A_{CO}}$. **This is the key clinical simplification — the entire DLCO test rests on it.**

#### Two measurement methods

**(1) Steady-state method (Fig. 30-8).**
1. Subject breathes a low-CO mixture (e.g., 0.1–0.2% CO) for ~12 breaths to bring $P_{A_{CO}}$ to a stable plateau.
2. Two measurements: **$P_{A_{CO}}$** from an end-tidal alveolar-air sample; **$\dot V_{CO}$** from the (inspired CO/min − expired CO/min) difference.
3. **$D_{L_{CO}} = \dot V_{CO} / P_{A_{CO}}$** (or with the $P_{\bar v_{CO}}$ correction if needed for smokers).

**(2) Single-breath method (Fig. 30-9) — the clinical standard.**
1. Subject exhales to **residual volume (RV)**.
2. Subject makes a maximal inspiration of a mixture of **0.3% CO + 10% He** + balance air.
3. Subject **holds breath for 10 seconds** at TLC.
4. Subject exhales; the lab samples **pure alveolar air** (after discarding the dead-space portion).
5. **Helium** (an insoluble gas that does not cross the alveolar wall) serves as a **dilution marker**: comparing inspired He concentration to the post-equilibration alveolar He concentration gives the dilution factor and the alveolar volume $V_A$.
6. The initial $P_{A_{CO}}$ (computed from inspired CO concentration × He-dilution factor) and the final $P_{A_{CO}}$ (measured) bracket the 10-second average $\bar P_{A_{CO}}$. The fall in alveolar CO amount over those 10 seconds gives $\dot V_{CO}$.
7. **$D_{L_{CO}} = \dot V_{CO} / \bar P_{A_{CO}}$** as above.

#### Normal values and the $D_M / \theta V_c$ split
- **Normal $D_{L_{CO}} \approx 25$ mL CO · min⁻¹ · mm Hg⁻¹** (at normal Hb content).
- For CO, $D_M$ and $\theta V_c$ each contribute about equally:

$$\frac{1}{D_{L_{CO}}} = \frac{1}{D_M} + \frac{1}{\theta V_c} \;\;\;\sim\;\;\; \frac{1}{25} = \frac{1}{50} + \frac{1}{50} \quad (\text{Eq. 30-26})$$

  with both $D_M$ and $\theta V_c \approx 50$ mL · min⁻¹ · mL blood⁻¹. **This is the partition that explains why anemia (↓Hb → ↓$V_c$) reduces DLCO even though the alveolar wall is structurally normal.**

#### Table 30-3 — Factors that affect $D_{L_{CO}}$

| Factor | Effect | Explanation |
|---|---|---|
| **Body size** | ↑ size → ↑ DLCO | ↑ lung size → ↑ diffusion area $A$ and ↑ pulmonary-capillary volume $V_c$ |
| **Age** | ↑ age → ↓ DLCO | DLCO falls ~2% per year after age 20 |
| **Sex** | Male > female DLCO | Corrected for age and body size, men have ~10% greater DLCO than women |
| **Lung volume** | ↑ $V_L$ → ↑ DLCO | ↑ $V_L$ → ↑ $V_c$, ↑ $A$, and ↓ diffusion distance $a$ |
| **Exercise** | ↑ DLCO | ↑ $\dot Q$ dilates and recruits pulmonary capillaries → ↑ $A$ and ↑ $V_c$ |
| **Body position** | supine > sitting > standing | Posture shifts presumably ↑ pulmonary capillary blood volume $V_c$ |
| **$P_{A_{O_2}}$** | ↑ $P_{A_{O_2}}$ → ↓ DLCO | O₂ competes with CO for Hb binding → lowers the rate at which CO combines with Hb (↓$\theta$) |
| **$P_{A_{CO_2}}$** | ↑ $P_{A_{CO_2}}$ → ↑ DLCO | CO₂ increases pulmonary-capillary blood volume $V_c$ |

### Equations (Section 3)

- **DLCO from Fick's law (clinical equation)**:

$$D_{L_{CO}} = \frac{\dot V_{CO}}{P_{A_{CO}} - P_{c_{CO}}} \quad (\text{Eq. 30-25})$$

  In practice, $P_{c_{CO}} \approx 0$ → $D_{L_{CO}} \approx \dot V_{CO} / P_{A_{CO}}$.

- **Membrane + blood partition for CO**:

$$\frac{1}{D_{L_{CO}}} = \frac{1}{D_M} + \frac{1}{\theta V_c} \quad (\text{Eq. 30-26})$$

  with $D_M \approx \theta V_c \approx 50$ mL CO · min⁻¹ · mL blood⁻¹.

### Citation-anchor quotes
- > "CO is an excellent choice because its uptake is diffusion limited, so that changes in the parameter of interest (i.e., $D_L$) have nearly a proportionate effect on $\dot V_{CO}$." (p. 670)
- > "A normal value for DLCO is ~25 mL CO taken up per minute for each millimeter of mercury of partial pressure driving CO diffusion and for each milliliter of blood having a normal Hb content." (p. 670)
- > "$1/(\theta \cdot V_c)$ makes a major contribution to the final DLCO. Because $V_c$ is proportional to the Hb content of the blood, and because Hb content is decreased in anemia, a subject can have a reduced DLCO even though the diffusion pathways in the lung (i.e., $D_M$) are perfectly normal." (p. 671)

### Figures (Section 3)

#### Figure 30-8 — Steady-state method for estimating DLCO *(listed)*

Schematic of a spirometric setup. Subject (upper right) breathes a low-CO mixture from a reservoir; the figure shows two measurement loops: one labeled "Calculate $\dot V_{CO}$ from difference of inspired versus expired CO/min, over several respiratory cycles" (the difference of two flow-meter readings), and one labeled "Measure $P_{A_{CO}}$ in sample of pure alveolar air" (an end-tidal sample collected after a maximum expiration to discard dead-space air). Lower-left inset shows the partitioning of an exhaled breath into anatomic dead-space air and alveolar air. The two measurements are combined as $D_{L_{CO}} = \dot V_{CO} / P_{A_{CO}}$.

#### Figure 30-9 — Single-breath method for estimating DLCO *(listed)*

Three-panel sequence. **(Maximum inspiration)**: Subject starts at **residual volume (RV)**; the lungs are drawn small; the inspired-gas reservoir contains **0.3% CO + 10% He**. **(Hold breath for 10 s)**: Subject inhales fully to TLC; the lungs are drawn large; the inspired CO/He mixture is diluted by the pre-existing alveolar air, allowing computation of (i) the initial $P_{A_{CO}}$ and (ii) the initial alveolar CO amount via the He dilution factor. During the hold, CO diffuses into pulmonary capillary blood while He (with negligible solubility / DL) does not. **(Expiration)**: Subject exhales; the lab discards the first (dead-space) portion and analyzes the last portion (pure alveolar air) to measure the final $P_{A_{CO}}$. The initial and final $P_{A_{CO}}$ values yield $\bar P_{A_{CO}}$; the change in alveolar CO amount over 10 s yields $\dot V_{CO}$; $D_{L_{CO}} = \dot V_{CO} / \bar P_{A_{CO}}$.

---

## Section 4 — O₂ and CO₂ transport are normally perfusion-limited (pp. 671–674)

### Subsection headings (verbatim)
- **For both O₂ and CO₂, transport is normally perfusion limited** (pp. 671–673)
- **Pathological changes that reduce $D_L$ do not necessarily produce hypoxia** (pp. 673–674)

### Core claims

#### O₂ uptake — perfusion-limited at rest, with a large $D_L$ reserve (Fig. 30-10)
- **Mixed-venous $P_{\bar v_{O_2}} \approx 40$ mm Hg** enters the pulmonary capillary; **alveolar $P_{A_{O_2}} \approx 100$ mm Hg**; initial driving gradient = ~60 mm Hg. This is **enormous** compared to the ~0.7 mm Hg CO gradient.
- Three reasons O₂ equilibrates fast (unlike CO):
  1. **Hb is already ~75% preloaded** with O₂ entering the capillary (Ch 29) — only the top ~25% of Hb's capacity is left to fill. CO sees a near-empty Hb (~0% pre-loaded).
  2. **Driving gradient is huge** (~60 mm Hg for O₂ vs. <1 mm Hg for CO).
  3. **$D_L$ for O₂ is higher than $D_L$ for CO** (chiefly because $\theta V_c$ is larger for O₂ — Hb-O₂ binding is fast).
- **Result**: capillary $P_{c_{O_2}}$ reaches alveolar $P_{A_{O_2}}$ at about **one-third of the way along the capillary** (Fig. 30-10B, black curve). O₂ is therefore **perfusion-limited at rest**.
- **Two-thirds $D_L$ reserve.** Even if $D_{L_{O_2}}$ is **halved**, equilibration is still reached by ~two-thirds of the way along the capillary (Fig. 30-10B, blue curve). Equilibration would have to be threatened by **DL falling to ~one-third of normal** before O₂ uptake at rest becomes diffusion-limited.

#### Stress conditions: when O₂ becomes diffusion-limited
- **Exercise** (Fig. 30-10C). Cardiac output rises up to ~5× (Ch 22, 23). Capillary transit time (~0.75 s at rest) falls — but **not** by the full factor of 5 because rising perfusion pressure **recruits** previously closed capillaries and **distends** open ones (Ch 31). Net: contact time falls to **~0.25 s** at peak exercise. In **healthy subjects**, O₂ still equilibrates (green curve hits the dashed alveolar line near 100% of capillary length). In **patients with $D_L$ reduction from pulmonary disease**, equilibration fails (brown curve never reaches the alveolar line) → **exercise-induced diffusion limitation in fibrosis or COPD**.
- **High altitude** (Fig. 30-10D). Low ambient $P_B$ → low $P_{I_{O_2}}$ → low $P_{A_{O_2}}$. Two compounding effects: (1) **smaller alveolar-to-venous driving gradient** (since alveolar $P_{A_{O_2}}$ is reduced and mixed-venous $P_{\bar v_{O_2}}$ is also reduced — but the gradient $P_{A_{O_2}} - P_{\bar v_{O_2}}$ is smaller); (2) operation on a **steeper part of the Hb-O₂ dissociation curve** (Ch 29), so a given $\Delta$content corresponds to a larger $\Delta P_{O_2}$ — equilibration takes longer.
- **Exercise + altitude** → diffusion limitation even in **healthy** people (Fig. 30-10D, green curve). This is the textbook explanation for the elite-athlete observation that arterial $P_{O_2}$ falls during heavy exercise at altitude even in fit individuals.
- **Exercise + altitude + pathology** is the worst case: all three insults compound.

#### CO₂ — normally perfusion-limited, rarely a clinical problem (Fig. 30-11)
- Mixed-venous $P_{\bar v_{CO_2}} \approx 46$ mm Hg; alveolar $P_{A_{CO_2}} \approx 40$ mm Hg; initial driving gradient = **~6 mm Hg**, only 10% as large as the O₂ gradient. CO₂ flows **from blood to alveolus** (opposite direction to O₂).
- Two factors **slow** CO₂ equilibration:
  1. Small initial gradient (6 mm Hg).
  2. The **CO₂-content / $P_{CO_2}$ curve is much steeper than Hb-O₂** (Ch 29) — so a given drop in CO₂ content yields only a small drop in $P_{CO_2}$, prolonging the partial-pressure equilibration.
- One factor **speeds** equilibration: $D_{L_{CO_2}}$ is **3–5× higher** than $D_{L_{O_2}}$.
- Net result: capillary $P_{CO_2}$ reaches alveolar $P_{CO_2}$ at **~one-third of the way along the capillary** (similar to O₂; Fig. 30-11B, black curve). Some authorities argue it equilibrates a bit later, but in either case **CO₂ excretion is perfusion-limited** at rest.
- CO₂ rarely becomes diffusion-limited because the perfusion-limitation buffer is large and CO₂'s high water solubility keeps $D_M$ for CO₂ high. CO₂ retention in lung disease is almost always a **ventilation problem**, not a diffusion problem.

#### The clinical paradox: low $D_L$ ≠ hypoxia
- Diseases that **reduce DLCO**: **diffuse interstitial pulmonary fibrosis** (thickened interstitium → ↓$D_M$; can be idiopathic, or due to sarcoidosis, scleroderma, asbestos), **COPD** (capillary destruction → ↓area and ↓$V_c$), **surgical loss of lung tissue** (lobectomy/pneumonectomy → ↓area and ↓$V_c$), **anemia** (↓Hb → ↓$\theta V_c$).
- **These diseases also cause hypoxemia**, but the hypoxemia is **mostly not** due to the $D_L$ reduction per se. Recall the **two-thirds rule**: $D_L$ would have to fall to ~one-third of normal before O₂ transport becomes diffusion-limited at rest.
- The hypoxemia in these diseases is mostly due to the **disturbed distribution of ventilation and perfusion** (V̇/Q̇ mismatch, Ch 31) that accompanies the structural damage. **DLCO is therefore a marker of structural disease, not a direct measure of the cause of hypoxemia.**

### Equations (Section 4 — implied / forward to Ch 31)

The chapter does not derive the **alveolar gas equation** explicitly (it is developed in detail in Ch 31, ventilation-perfusion), but Chapter 30 is the natural place to anchor it for the AI-application reformat because everything that follows in Ch 31 depends on it. The alveolar gas equation states the steady-state value of $P_{A_{O_2}}$:

$$\boxed{P_{A_{O_2}} = P_{I_{O_2}} - \frac{P_{A_{CO_2}}}{R}} \quad (\text{alveolar gas equation, simplified form})$$

with:
- $P_{I_{O_2}} = F_{I_{O_2}} \cdot (P_B - P_{H_2O})$ = inspired wet-air $P_{O_2}$ (= $0.21 \times (760-47) \approx 150$ mm Hg at sea level on room air);
- $P_{A_{CO_2}} \approx P_{a_{CO_2}} \approx 40$ mm Hg in health, set by alveolar ventilation;
- $R$ = **respiratory exchange ratio** = $\dot V_{CO_2} / \dot V_{O_2} \approx 0.8$ at rest on a mixed diet (Ch 32).

The full form includes a small correction term $[F_{I_{O_2}} (1-R)/R]$:

$$P_{A_{O_2}} = P_{I_{O_2}} - \frac{P_{A_{CO_2}}}{R} + \left[F_{I_{O_2}} \cdot P_{A_{CO_2}} \cdot \frac{1-R}{R}\right]$$

The **alveolar-arterial (A-a) gradient** is:

$$\boxed{\text{A-a gradient} = P_{A_{O_2}} - P_{a_{O_2}}}$$

with normal value **<10–15 mm Hg in young adults**, widening with age approximately as:

$$\text{Normal A-a} \approx \frac{\text{age}}{4} + 4 \quad \text{(mm Hg, rule of thumb)}$$

The A-a gradient is the bedside discriminator among the **five causes of hypoxemia**:

| Cause | A-a gradient | Responds to 100% O₂? | Mechanism |
|---|---|---|---|
| **Low $P_{I_{O_2}}$** (altitude) | **Normal** | Yes | Less O₂ in inspired air → less in alveolus and blood; gradient preserved |
| **Hypoventilation** (opioids, neuromuscular disease) | **Normal** | Yes | ↑$P_{A_{CO_2}}$ → ↓$P_{A_{O_2}}$ via alveolar gas equation; gradient preserved |
| **V̇/Q̇ mismatch** (most lung disease) | **Widened** | Yes (mostly) | Some alveoli over-ventilated, some under-ventilated; weighted-mean $P_{a_{O_2}}$ < $P_{A_{O_2}}$ |
| **Right-to-left shunt** (atelectasis, congenital cardiac, AVM) | **Widened** | **No** (or poorly) | Deoxygenated blood bypasses alveoli entirely; cannot be oxygenated by raising $F_{I_{O_2}}$ |
| **Diffusion impairment** (fibrosis at exercise + altitude) | **Widened** | Yes | $D_L$ insufficient for equilibration; raising $P_{I_{O_2}}$ raises driving gradient and restores equilibration |

(This table is the standard bedside framework; it is anchored in Ch 30's diffusion physics and developed in detail in Ch 31's V̇/Q̇ pathophysiology.)

### Citation-anchor quotes
- > "Capillary $P_{O_2}$ reaches the alveolar $P_{O_2}$ of ~100 mm Hg about one third of the way along the capillary." (p. 671)
- > "Because capillary $P_{O_2}$ reaches alveolar $P_{O_2}$, O₂ transport is perfusion limited, as is the case for N₂O. Because O₂ normally reaches diffusion equilibrium so soon along the capillary, the lung has a tremendous $D_L$ reserve for O₂ uptake." (p. 672)
- > "Even if we reduce $D_{L_{O_2}}$ by half, O₂ still reaches diffusion equilibrium about two thirds of the way along the capillary." (p. 672)
- > "The combination of exercise and high altitude can cause O₂ transport to become diffusion limited even in healthy individuals." (p. 673)
- > "Capillary $P_{CO_2}$ reaches alveolar $P_{CO_2}$ about one third of the way along the pulmonary capillary (as is the case for O₂). … CO₂ excretion is perfusion limited." (p. 673)
- > "Although pulmonary diseases can cause both a decrease in $D_L$ and hypoxemia (i.e., a decrease in arterial $P_{O_2}$), it is not necessarily true that the decrease in $D_L$ is the sole or even the major cause of the hypoxemia." (p. 674)
- > "The lung has a sizeable $D_L$ reserve for O₂ (and perhaps for CO₂ as well), $D_L$ would have to decrease to about one third of its normal value for O₂ transport to become diffusion limited." (p. 674)

### Figures (Section 4)

#### Figure 30-10 — Diffusion of O₂ *(viewed)*

Four-panel figure. **A — O₂ diffusion** (anatomical cartoon, same style as Fig. 30-5A and 30-6A). Single alveolus over a capillary with single-file RBCs; each RBC annotated "O₂ occupies three of the four sites on Hb" — i.e., entering Hb is already ~75% loaded with O₂, leaving only the top quartile of binding capacity to fill. **B — At rest.** Graph: x = "distance along capillary (%)" 0–100; y = "Capillary $P_{O_2}$ (mm Hg)" 0–100. Initial $P_{c_{O_2}} = 40$ (mixed venous). Three colored trajectories: **black ($D_L = 1$)** reaches the dashed alveolar line $P_{A_{O_2}} = 100$ by ~1/3 of capillary length; **red ($D_L = 2$)** reaches the line even faster; **blue ($D_L = 0.5$)** reaches the line by ~2/3. Captioned: "Initial $P_{O_2}$ gradient" (the vertical arrow from venous baseline to alveolar plateau). **C — Exercise.** Same axes; capillary transit time is shortened by ↑$\dot Q$. Trajectories: **green ($D_L = 1$)** still reaches the alveolar line (by ~end of capillary in normal exercisers); **brown ($D_L = 0.5$)** **fails to reach** the line by the end of the capillary — the textbook example of **exercise-unmasked diffusion limitation in fibrosis or COPD**. **D — High altitude.** Initial $P_{c_{O_2}}$ is lower; the dashed alveolar line is at a lower $P_{A_{O_2}}$ (~50–60 mm Hg) because $P_{I_{O_2}}$ is reduced. **Red (rest)** still equilibrates. **Green (exercise + altitude)** fails to equilibrate even in healthy people — diffusion-limited.

> Vision note: This is the chapter's most important diagnostic figure. The bedside framework for interpreting exercise oximetry, six-minute walk testing, and exercise-desaturation in interstitial lung disease all read off of this figure. Anchor for the clinical pulmonologist's "DLCO low + exercise desaturation" pattern recognition.

#### Figure 30-11 — Diffusion of CO₂ *(listed)*

Two-panel figure. **A — CO₂ diffusion** anatomical cartoon, but with CO₂ now flowing **from blood to alveolus** (arrows reversed from Fig. 30-5A). RBC shown delivering CO₂ to the plasma (note: most CO₂ travels in blood as HCO₃⁻, see Ch 29). **B — $P_{c_{CO_2}}$ profile.** x = distance along capillary; y = "Capillary $P_{CO_2}$ (mm Hg)" 40–50. Initial $P_{c_{CO_2}} = 46$ (mixed venous). Three trajectories: **black (rest)** falls smoothly to the dashed alveolar line $P_{A_{CO_2}} = 40$ by about one-third of the way along (some draw it falling more slowly, reaching 40 nearly at the end); **red (exercise)** falls more slowly, reaching equilibrium only near the end; **blue (lung disease)** **fails to reach** the alveolar line by the end of the capillary — the rare situation where CO₂ excretion becomes diffusion-limited (heavy exercise + lung pathology).

### Tables (Section 4)

#### Mini-table — Diffusion-limited vs. perfusion-limited gases

| Gas | Rest | Exercise | Exercise + altitude | Exercise + pathology |
|---|---|---|---|---|
| **CO** | diffusion | diffusion | diffusion | diffusion |
| **N₂O** | perfusion | perfusion | perfusion | perfusion |
| **O₂** | **perfusion** | perfusion (healthy); **diffusion** (severe disease) | **diffusion** (even in healthy) | **diffusion** |
| **CO₂** | perfusion | perfusion | perfusion | perfusion (sometimes diffusion in severe disease + heavy exercise) |

#### Mini-table — Pathological causes of low $D_L$

| Disease | $D_M$ effect | $\theta V_c$ effect | Net DLCO | Hypoxemia mechanism (mostly) |
|---|---|---|---|---|
| **Diffuse interstitial pulmonary fibrosis** | ↓↓ (thickened interstitium) | mild ↓ | ↓↓ | V̇/Q̇ mismatch; exercise-unmasked diffusion limitation |
| **COPD / emphysema** | ↓ (alveolar destruction → ↓$A$) | ↓ (↓capillary bed → ↓$V_c$) | ↓ | V̇/Q̇ mismatch (chiefly); some shunt; loss of $D_L$ reserve |
| **Surgical loss of lung tissue** | ↓ (↓$A$) | ↓ (↓$V_c$) | ↓ | Compensated by remaining lung if reserve is adequate |
| **Anemia** | normal | ↓ (↓Hb → ↓effective $V_c$) | ↓ | Reduced O₂-carrying capacity, not failure of equilibration |

---

## Tables in Chapter 30

- **Table 30-1** — Alveolar transport of CO: how $\dot V_{CO}$ depends on $D_L$ and $\dot Q$ (reproduced in Section 2 above). Conclusion: $\dot V_{CO} \propto D_L$, insensitive to $\dot Q$ → diffusion-limited.
- **Table 30-2** — Alveolar transport of N₂O: how $\dot V_{N_2O}$ depends on $D_L$ and $\dot Q$ (reproduced in Section 2 above). Conclusion: $\dot V_{N_2O} \propto \dot Q$, insensitive to $D_L$ → perfusion-limited.
- **Table 30-3** — Factors that affect $D_{L_{CO}}$ (reproduced in Section 3 above). Eight rows: body size, age, sex, lung volume, exercise, body position, $P_{A_{O_2}}$, $P_{A_{CO_2}}$.

---

## Glossary (downstream-chunkable)

- **Fick's law of diffusion** — $\dot V_X = D_L \cdot \Delta P$. Net diffusion flux is proportional to the partial-pressure **difference**, not the ratio.
- **Diffusing capacity $D_L$** — proportionality constant relating gas flow to partial-pressure gradient across the alveolar-capillary barrier (mL · min⁻¹ · mm Hg⁻¹).
- **Membrane diffusing capacity $D_M$** — the diffusion-only part of $D_L$ (12 mini-barriers in series; Eq. 30-13).
- **Hb-binding component $\theta V_c$** — the rate of Hb binding × pulmonary-capillary blood volume; the non-diffusive contribution to $D_L$.
- **Graham's law** — diffusion ∝ $1/\sqrt{MW}$.
- **Henry's law** — $[gas]_{aq} = s \cdot P_{gas}$.
- **Fick principle** — $\dot V_{O_2} = \dot Q (C_{a_{O_2}} - C_{\bar v_{O_2}})$; the macroscopic identity for whole-lung uptake.
- **Diffusion-limited gas** — end-capillary $P$ does not reach alveolar $P$; $\dot V \propto D_L$. Prototype: **CO**.
- **Perfusion-limited gas** — end-capillary $P$ reaches alveolar $P$; $\dot V \propto \dot Q$. Prototype: **N₂O**. Also: O₂ and CO₂ at rest.
- **DLCO** — diffusing capacity of the lung for CO. Normal ~25 mL CO · min⁻¹ · mm Hg⁻¹. Clinical readout of $D_L$.
- **Steady-state DLCO method** — repeated low-CO breaths; measure $\dot V_{CO}$ and $P_{A_{CO}}$; $D_{L_{CO}} = \dot V_{CO} / P_{A_{CO}}$.
- **Single-breath DLCO method** — clinical standard. Inhale 0.3% CO + 10% He from RV to TLC, hold 10 s, exhale; He gives dilution factor → $\bar P_{A_{CO}}$ and $\dot V_{CO}$.
- **RBC transit time** — ~0.75 s at rest; falls to ~0.25 s at peak exercise.
- **Alveolar gas equation** — $P_{A_{O_2}} = P_{I_{O_2}} - P_{A_{CO_2}}/R$. Forward to Ch 31, 32.
- **Respiratory exchange ratio $R$** — $\dot V_{CO_2}/\dot V_{O_2}$, ≈ 0.8 at rest on mixed diet.
- **A-a gradient** — $P_{A_{O_2}} - P_{a_{O_2}}$. Normal <10–15 mm Hg in young adults; widens with age (~age/4 + 4 mm Hg).
- **Five causes of hypoxemia** — (1) low $P_{I_{O_2}}$ (altitude), (2) hypoventilation, (3) V̇/Q̇ mismatch, (4) right-to-left shunt, (5) diffusion impairment. Distinguished by A-a gradient and response to 100% O₂.
- **Shunt** — perfused but unventilated alveoli (or anatomical right-to-left bypass); hypoxemia does not correct with 100% O₂.
- **V̇/Q̇ mismatch** — uneven matching of ventilation to perfusion; the dominant cause of hypoxemia in most lung disease. Anchored to Ch 31.
- **DLCO interpretation rules of thumb** —
  - Low DLCO + low lung volumes + restrictive spirometry → **interstitial lung disease (fibrosis)**.
  - Low DLCO + high lung volumes + obstructive spirometry → **emphysema**.
  - Low DLCO + normal lung volumes + normal spirometry → **pulmonary vascular disease** (chronic thromboembolic disease, pulmonary hypertension) or **anemia**.
  - Normal DLCO + obstructive spirometry → **asthma / chronic bronchitis** (resistance problem, not a diffusion or capillary-bed problem).

---

## Cross-links forward

| Forward link | Topic | Where |
|---|---|---|
| Alveolar gas equation, A-a gradient, five causes of hypoxemia | this chapter sets up the physics; Ch 31 develops the bedside framework | Ch 31 |
| V̇/Q̇ mismatch as the chief cause of hypoxemia in most lung disease | this chapter's "low $D_L$ ≠ hypoxia" claim is grounded here | Ch 31 |
| Control of $P_{A_{CO_2}}$ via alveolar ventilation | sets $P_{A_{O_2}}$ through alveolar gas equation | Ch 32 |
| Exercise pulmonary physiology (recruitment + distention of capillaries; transit-time shortening) | Q̇ rises ~5×, transit time falls to ~0.25 s | Ch 60 |
| High-altitude physiology (low $P_B$ → low $P_{I_{O_2}}$ → low $P_{A_{O_2}}$ → diffusion limitation at exercise) | Ch 30's Fig. 30-10D phenomenon | Ch 61 |
| Hb-O₂ dissociation curve (its steep portion at low $P_{O_2}$ amplifies altitude's effect on equilibration time) | invoked but not derived here | Ch 29 (back) |
| CO₂-content curve (steeper than O₂ → slows partial-pressure equilibration) | invoked but not derived here | Ch 29 (back) |
| CO poisoning pathophysiology (200–300× Hb affinity vs O₂) | mentioned as the toxic basis | pp. 1224–1225 forward |
| ARDS/IRDS as surfactant-deficient states that reduce $D_L$ chiefly via V̇/Q̇ mismatch and shunt | the "low $D_L$ ≠ hypoxia" framework | Ch 27 (back), Ch 56–57 forward |
| CFTR / cystic fibrosis as a cause of obstructive disease + V̇/Q̇ heterogeneity | DLCO usually preserved; hypoxemia from V̇/Q̇ + shunt | Ch 43 forward |

## Source apparatus

- **Online Notes** N30-1 through N30-10 referenced inline (deferred to companion site).
- No formal Clinical Boxes in this chapter; the pathology list on pp. 673–674 (fibrosis, COPD, lobectomy, anemia) functions as the equivalent clinical anchor.
- **References** deferred to www.StudentConsult.com.

---

## Format-verification notes

**Figures viewed and described from image:** 30-1 (diffusion across a barrier; A dry homogeneous + B alveolar wall), 30-4 (12-mini-barrier dissection of the alveolar-capillary pathway with $D_M$/$\theta V_c$ partition), 30-5 (diffusion of CO; the diffusion-limited diagnostic chart), 30-10 (diffusion of O₂; the rest/exercise/altitude diagnostic chart), 30-11 (diffusion of CO₂, viewed in passing during page-684 visual pass).

**Figures listed by caption + text reference only:** 30-2 (effect of barrier thickness), 30-3 (complications of using Fick's law — temporal/spatial nonuniformity), 30-6 (diffusion of N₂O — the perfusion-limited prototype), 30-7 (railway-car analogy), 30-8 (steady-state DLCO method), 30-9 (single-breath DLCO method).

**Equations included as LaTeX:** Fick proportionality (Eqs. 30-1/2/3); lung-Fick (Eq. 30-4); wet-barrier extended Fick (Eq. 30-5); Ohm analogy (Eq. 30-6); microscopic Fick integrated form (Eq. 30-9); Fick principle (Eq. 30-10) with worked 250 mL O₂/min example (Eq. 30-11); micro/macro bookkeeping identity (Eq. 30-12); membrane-resistor sum (Eq. 30-13); $D_M + \theta V_c$ partition (Eq. 30-15); inspired wet-gas partial pressure (Eq. 30-16); CO Fick principle (Eq. 30-17/18); DLCO clinical equation (Eq. 30-25); CO partition (Eq. 30-26); alveolar gas equation; A-a gradient (forward to Ch 31).

*End of Chapter 30. Next: Chapter 31 — Ventilation and Perfusion of the Lungs (Boron), p. 675.*
