---
chapter: 28
title: Acid-Base Physiology
authors:
  - Walter F. Boron
section: "V. The Respiratory System"
source_pages: "628–646"
pdf_pages: "640–658"
source_book: "Boron WF, Boulpaep EL. Medical Physiology, 3rd edition (2017)"
figures_listed: "13 (28-1 through 28-13)"
figures_described_from_image: 5
equations: "many — pH = −log[H⁺]; HB^(n+1) ⇌ B^n + H⁺ with K = [H⁺][B^n]/[HB^(n+1)]; Henry's law [CO₂]_dis = s·P_CO₂; Henderson-Hasselbalch pH = pK + log([HCO₃⁻]/(s·P_CO₂)); buffering power β = Δ[strong base]/ΔpH; β_closed = 2.3·[H⁺]·K/([H⁺]+K)²·[TB]; β_open = 2.3·[HCO₃⁻]; whimsical pH = const + kidney/lungs; isohydric hypercapnia rule; anion gap = [Na⁺] − [Cl⁻] − [HCO₃⁻]; strong ion difference SID"
tables: 6
clinical_boxes: "1 explicit (Box 28-1 Strong Ion Difference) plus extensive clinical apparatus (Table 28-3 four major acid-base disorders + DKA, lactic acidosis, RTA, vomiting, COPD threaded through the narrative)"
---

# Chapter 28 — Acid-Base Physiology

> Section V · The Respiratory System · pp. 628–646 · Author: Walter F. Boron
> This chapter is the conceptual hinge between **Ch 27 (mechanics of ventilation)** and **Ch 39 (renal transport of acids and bases)**. It develops three nested narratives. (1) **Buffer chemistry**: pH, weak-acid/weak-base equilibrium, buffering power $\beta$, and the central distinction between a **closed** buffer (β bell-shaped, peaks at pK) and an **open** buffer (β rises exponentially with pH). (2) **The CO₂/HCO₃⁻ system as the dominant physiological open buffer**, summarized by the Henderson-Hasselbalch equation $\text{pH} = \text{p}K + \log\dfrac{[\text{HCO}_3^-]}{s\cdot P_{\text{CO}_2}}$ and operated graphically on the **Davenport diagram** (pH on x-axis, [HCO₃⁻] on y-axis, P_CO₂ isopleths as exponential curves). (3) **The four primary acid-base disorders** — respiratory acidosis, respiratory alkalosis, metabolic acidosis, metabolic alkalosis — each with its renal or respiratory **compensation**, mapped onto regions of the Davenport diagram, plus the **intracellular pH** machinery (NHE, NBC, AE, MCT) that defends cytosolic pH against the same insults.

## Chapter map (top-level)

1. **pH and buffers** (pp. 628–632) — Brønsted definitions; the pH scale (Sørensen 1909); body-compartment pH values (Table 28-2); definition of a buffer; **buffering power** $\beta$ as moles strong-base/pH-unit; the closed-system buffer with bell-shaped β peaking at pK (Eq. 28-18); multiple-buffer flattening of β (Fig. 28-2B); the CO₂/HCO₃⁻ pair as a uniquely **open** buffer because CO₂ exchanges with the atmosphere; Henderson-Hasselbalch derivation (Eq. 28-16); $\beta_{\text{open}} = 2.3\,[\text{HCO}_3^-]$ (Eq. 28-20).
2. **Acid-base chemistry when CO₂/HCO₃⁻ is the only buffer** (pp. 632–635) — doubling P_CO₂ at fixed open atmosphere drops pH by 0.3 with negligible Δ[HCO₃⁻] (respiratory acidosis); halving P_CO₂ raises pH by 0.3 (respiratory alkalosis); doubling [HCO₃⁻] at fixed P_CO₂ raises pH by 0.3 (metabolic alkalosis); the whimsical Henderson-Hasselbalch as "pH = const + kidney/lungs" (Eq. 28-27).
3. **Acid-base chemistry with non-HCO₃⁻ buffers — the Davenport diagram** (pp. 635–641) — CO₂ isopleths (isobars at P_CO₂ = 20, 40, 80 mm Hg); non-HCO₃⁻ titration line (slope = −β_non-HCO₃⁻, normally ~25 mM/pH); the four primary disturbances as moves between isopleth and titration line (Fig. 28-6C, 28-7); β_open's pH-dependence makes CO₂/HCO₃⁻ a better buffer of alkali than of acid (Table 28-6); β_non-HCO₃⁻ tracks hemoglobin (low in anemia, high in polycythemia); Stewart's strong-ion difference critiqued (Box 28-1).
4. **Compensation and the position of an acid-base state on the Davenport diagram** (pp. 641–644) — metabolic compensation to respiratory disturbances (Fig. 28-9); respiratory compensation to metabolic disturbances (Fig. 28-10); isohydric hypercapnia / isohydric hypocapnia; the five Davenport regions: normal, uncompensated, partially compensated, perfectly compensated, compound (Fig. 28-11).
5. **pH regulation of intracellular fluid** (pp. 644–646) — acid extruders (NBCn1 Na/HCO₃ cotransport, NHE1 Na/H exchange) vs. acid loaders (AE2 Cl/HCO₃ exchange) in push-pull balance (Fig. 28-12); pH_i recovery from acute acid and alkaline loads; pH_o sensitivity of extruders and loaders; apparent "K-H exchange" reanalyzed as depolarization-induced alkalinization; the three-phase intracellular response to an extracellular respiratory acidosis (rapid CO₂ entry → slow extruder/loader recovery → renal metabolic compensation pulling pH_e and pH_i back together; Fig. 28-13).

---

## Section 1 — pH and buffers (pp. 628–632)

### Subsection headings (verbatim)
- **pH values vary enormously among different intracellular and extracellular compartments** (pp. 628–629)
- **Buffers minimize the size of the pH changes produced by adding acid or alkali to a solution** (pp. 629–630)
- **According to the Henderson-Hasselbalch equation, pH depends on the ratio [CO₂]/[HCO₃⁻]** (pp. 630–631)
- **CO₂/HCO₃⁻ has a far higher buffering power in an open than in a closed system** (pp. 631–632)

### Core claims

#### pH, weak acids, and the body-fluid spectrum
- Brønsted definitions. An **acid** donates H⁺, a **base** accepts H⁺ ("alkali" is interchangeable with base). [H⁺] in biology spans >100 mM (gastric secretions) down to <10 nM (pancreatic secretions). Sørensen (1909) introduced $\text{pH} = -\log_{10}[\text{H}^+]$ (Eq. 28-1) to compress the scale.
- **Decadal arithmetic** (Table 28-1): a 10-fold change in [H⁺] is a 1.0 pH-unit shift; a 2-fold change is ~0.3 pH-unit.
- **Body-fluid pH spectrum** (Table 28-2): gastric secretion at maximal acidity ~0.7; lysosome 5.5; chromaffin granule ~5.7; neutral water at 37 °C 6.81; cytosol of a typical cell ~7.2; CSF ~7.35; arterial blood plasma 7.40; mitochondrial matrix ~7.7; pancreatic fluid ~8.1.
- Because neutral water is 6.81 at body temperature (not 7.00 — water is more dissociated at 37 °C than at 25 °C), **most body compartments are alkaline relative to neutrality** even when nominally "acidic."
- **Why even small pH changes matter.** The Na/K pump loses ~50% activity per 1 pH-unit shift; phosphofructokinase loses ~90% activity per 0.1 pH-unit fall; mitogen-driven cell proliferation can fall by up to 85% with a 0.4-unit drop in pH_i.

#### Buffers and buffering power
- **A buffer** is "any substance that reversibly consumes or releases H⁺" (p. 629). For a generic buffer $\text{HB}^{(n+1)} \rightleftharpoons \text{B}^n + \text{H}^+$ (Eq. 28-2), the conjugate-pair total concentration $[\text{TB}] = [\text{HB}^{(n+1)}] + [\text{B}^n]$ (Eq. 28-3) is conserved. Physiological examples (Eq. 28-4) include $\text{NH}_4^+ \rightleftharpoons \text{NH}_3 + \text{H}^+$, $\text{H}_2\text{CO}_3 \rightleftharpoons \text{HCO}_3^- + \text{H}^+$, and $\text{H}_2\text{PO}_4^- \rightleftharpoons \text{HPO}_4^{2-} + \text{H}^+$.
- The dissociation constant (Eq. 28-5): $K = \dfrac{[\text{H}^+][\text{B}^n]}{[\text{HB}^{(n+1)}]}$.
- **Buffering power** $\beta$ (Eq. 28-8) is operationally defined as the mmol of strong base (or strong acid, with sign flipped) per liter required to shift pH by 1 unit:

$$\beta = \frac{\Delta[\text{strong base}]}{\Delta \text{pH}} = -\frac{\Delta[\text{strong acid}]}{\Delta \text{pH}} \quad (\text{Eq. 28-8})$$

- **Whole blood vs plasma.** $\beta_{\text{non-HCO}_3^-}$ is ~25 mM/pH unit for whole blood (cells + plasma) but only ~5 mM/pH unit for plasma alone — the difference is mainly the **imidazole groups of hemoglobin** plus other intracellular protein groups carried inside erythrocytes.

#### The closed-system buffer (Eq. 28-18)
For a buffer whose [TB] is conserved (neither HB nor B leaves the system):

$$\beta_{\text{closed}} = 2.3 \cdot \frac{[\text{H}^+]\cdot K}{([\text{H}^+]+K)^2} \cdot [\text{TB}] \quad (\text{Eq. 28-18})$$

- At a given [TB], $\beta_{\text{closed}}$ has a **bell-shaped dependence on pH** with its maximum at $\text{pH} = \text{p}K$ (Fig. 28-2A). A buffer whose pK is one pH unit away from the working pH has only ~9% of its peak buffering power.
- A single closed buffer is therefore narrow-band. The lung-and-blood solution to this narrow-band problem is **two parallel strategies**: a mixture of many buffers with overlapping pK's (Fig. 28-2B, where nine buffers spaced 0.5 pH units apart in pK and each at 12.6 mM produce a $\beta_{\text{total}}$ that is nearly flat at ~25 mM/pH unit across pH 5–10), plus a single buffer (CO₂/HCO₃⁻) made effectively unlimited by **opening it to the atmosphere**.
- Whole blood matches Fig. 28-2B: a complex mixture of titratable groups on hemoglobin, plasma proteins, and inorganic phosphate produces a nearly pH-flat $\beta_{\text{non-HCO}_3^-} \approx 25$ mM/pH unit near physiological pH.

#### Why CO₂/HCO₃⁻ is uniquely powerful — the open-system buffer
- Henry's law (Eq. 28-9): $[\text{CO}_2]_{\text{dis}} = s \cdot P_{\text{CO}_2}$, with **$s \approx 0.03$ mM/mm Hg** at 37 °C in plasma. With arterial $P_{\text{CO}_2} = 40$ mm Hg, $[\text{CO}_2]_{\text{dis}} \approx 1.2$ mM (Eq. 28-10).
- The hydration/dissociation chain $\text{CO}_2 + \text{H}_2\text{O} \xrightarrow{\text{slow}} \text{H}_2\text{CO}_3 \xrightarrow{\text{fast}} \text{H}^+ + \text{HCO}_3^-$ (Eqs. 28-11, 28-12) is rate-limited by the uncatalyzed hydration. **Carbonic anhydrase** (in erythrocytes and many epithelia; see Ch 18 N18-3) catalyzes the slow step and effectively collapses the chain into one pseudo-equilibrium (Eq. 28-13): $\text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{H}^+ + \text{HCO}_3^-$.
- Combining with Henry's law gives the **Henderson-Hasselbalch equation** (Eq. 28-16):

$$\boxed{\text{pH} = \text{p}K + \log \frac{[\text{HCO}_3^-]}{s \cdot P_{\text{CO}_2}}}$$

with $\text{p}K \approx 6.1$ at 37 °C and arterial blood substitution (Eq. 28-17):

$$\text{pH} = 6.1 + \log \frac{24\,\text{mM}}{(0.03\,\text{mM/mm Hg})\cdot 40\,\text{mm Hg}} = 6.1 + \log 20 = 7.40$$

- **The central message of H-H.** pH depends **not on [HCO₃⁻] or P_CO₂ per se but on their ratio**. Plasma can be acid or alkaline at any absolute [HCO₃⁻] depending on the matched P_CO₂.
- **Open-system buffering power** (Eq. 28-20): when CO₂ exchanges freely with a large reservoir (the alveolar gas, and beyond it the atmosphere), [CO₂]_dis is clamped and only [HCO₃⁻] depletion limits acid-buffering. The result:

$$\boxed{\beta_{\text{open}} = 2.3 \cdot [\text{HCO}_3^-]}$$

For normal arterial blood ($[\text{HCO}_3^-] = 24$ mM), $\beta_{\text{open}} \approx 55$ mM/pH unit — **more than twice** $\beta_{\text{non-HCO}_3^-}$ of whole blood, and accounting for ≥2/3 of the total buffering in blood.
- $\beta_{\text{open}}$ has **no maximum**; it rises exponentially with pH (Fig. 28-4 blue curve), because $[\text{HCO}_3^-]$ itself rises exponentially with pH at fixed P_CO₂. The **same CO₂/HCO₃⁻ pair** in a closed system (e.g., a capped syringe, or ischemic tissue cut off from blood flow) collapses to $\beta_{\text{closed}} \approx 2.6$ mM/pH unit at pH 7.4 — less than 5% of the open value. **Ischemic tissues are therefore especially susceptible to large pH shifts.**

#### Worked open-buffer example (Fig. 28-3)
Add 10 mmol HCl to 1 L of CO₂/HCO₃⁻ solution (initial pH 7.40, $P_{\text{CO}_2}$ = 40 mm Hg, [HCO₃⁻] = 24 mM, no other buffers). Nearly 10 mmol of HCO₃⁻ is consumed, generating CO₂ that **evolves to the atmosphere** (open sink). New equilibrium: [HCO₃⁻] = 14 mM, $P_{\text{CO}_2}$ unchanged → pH = 7.17. The free [H⁺] increased by only ~28 nM despite adding 10 mmol H⁺ per liter — the open buffer absorbed 9.999,972 mmol of it.

### Equations

$$\text{pH} = -\log_{10}[\text{H}^+] \quad (\text{Eq. 28-1})$$

$$K = \frac{[\text{H}^+][\text{B}^n]}{[\text{HB}^{(n+1)}]} \quad (\text{Eq. 28-5})$$

$$\beta = \frac{\Delta[\text{strong base}]}{\Delta \text{pH}} \quad (\text{Eq. 28-8})$$

$$[\text{CO}_2]_{\text{dis}} = s \cdot P_{\text{CO}_2}, \quad s = 0.03 \text{ mM/mm Hg} \quad (\text{Eq. 28-9})$$

$$\text{pH} = \text{p}K + \log \frac{[\text{HCO}_3^-]}{s \cdot P_{\text{CO}_2}} \quad (\text{Eq. 28-16})$$

$$\beta_{\text{closed}} = 2.3 \cdot \frac{[\text{H}^+]\cdot K}{([\text{H}^+]+K)^2} \cdot [\text{TB}] \quad (\text{Eq. 28-18})$$

$$\beta_{\text{open}} = 2.3 \cdot [\text{HCO}_3^-] \quad (\text{Eq. 28-20})$$

### Citation-anchor quotes
- > "Acid-base physiology is really the study of the proton, or hydrogen ion (H⁺)." (p. 628)
- > "A buffer is any substance that reversibly consumes or releases H⁺. In this way, buffers help to stabilize pH. Buffers do not prevent pH changes, they only help to minimize them." (p. 629)
- > "The most important physiological buffer pair is CO₂ and HCO₃⁻. The impressive strength of this buffer pair is due to the volatility of CO₂, which allows the lungs to maintain stable CO₂ concentrations in the blood plasma." (p. 630)
- > "Its central message is that pH depends not on [HCO₃⁻] or P_CO₂ per se, but on their ratio." (p. 631)
- > "The buffering provided by CO₂/HCO₃⁻ in an open system (β_open) is so powerful because only depletion of HCO₃⁻ limits neutralization of H⁺." (p. 631)

### Tables (Section 1)

#### Table 28-1 — Relationship between [H⁺] and pH

| [H⁺] (M) | pH | Δ |
|---|---|---|
| 1 × 10⁻⁶ | 6.0 | 1 pH unit per 10× [H⁺] |
| 1 × 10⁻⁷ | 7.0 | |
| 1 × 10⁻⁸ | 8.0 | |
| 5 × 10⁻⁸ | 7.3 | 0.3 pH unit per 2× [H⁺] |
| 4 × 10⁻⁸ | 7.4 | |
| 2 × 10⁻⁸ | 7.7 | |

#### Table 28-2 — Approximate pH values of body fluids

| Compartment | pH |
|---|---|
| Gastric secretion (maximal acidity) | 0.7 |
| Lysosome | 5.5 |
| Chromaffin granule | ~5.7 |
| Neutral H₂O at 37 °C | 6.81 |
| Cytosol of a typical cell | ~7.2 |
| Cerebrospinal fluid | 7.35 |
| Arterial blood plasma | 7.40 |
| Mitochondrial inner matrix | ~7.7 |
| Secreted pancreatic fluid | 8.1 |

### Figures (Section 1)

#### Figure 28-1 — Interaction of CO₂ with water *(listed)*
Vertical-cascade reaction diagram. CO₂ in the atmosphere enters solution by Henry's law ($[\text{CO}_2]_{\text{dis}} = s \cdot P_{\text{CO}_2}$); CO₂ + H₂O slowly hydrates to H₂CO₃; H₂CO₃ rapidly dissociates to H⁺ + HCO₃⁻. The net reaction (collapsed to CO₂ + H₂O ⇌ H⁺ + HCO₃⁻) defines a pseudo-equilibrium constant K (Eq. 28-14) whose logarithmic form is the Henderson-Hasselbalch equation. Carbonic anhydrase, when present, accelerates the slow hydration step.

#### Figure 28-2 — Buffering power in a closed system *(listed)*
Two-panel plot, both with pH on x-axis (range ~4–10) and buffering power $\beta$ (mM/pH unit) on y-axis. **Panel A — Single buffer:** a bell-shaped (green) curve with peak at pH = pK; the worked example has pK = 7. **Panel B — Multiple buffers:** the red curve is the sum of nine bell curves (each [TB] = 12.6 mM with pK values spaced 0.5 pH units apart from ~5 to ~9). The sum is nearly flat at ~25 mM/pH unit over pH 5–10 — the textbook reconstruction of how a mixture of titratable protein groups in whole blood produces a pH-independent total $\beta_{\text{non-HCO}_3^-}$.

#### Figure 28-3 — Buffering of strong acids and bases by CO₂/HCO₃⁻ in an open system *(listed)*
Two parallel three-stage cartoons. **Top row — adding 10 mmol HCl:** Stage 1 (Start): 1 L solution open to a CO₂ reservoir at 40 mm Hg with [H⁺] = 40 nM, [HCO₃⁻] = 24 mM. Stage 2A (just after acid load): nearly 10 mmol HCO₃⁻ neutralizes the H⁺ → nearly 10 mmol CO₂ generated, which equilibrates with the atmosphere; HCO₃⁻ drops to ~14 mM. Stage 3A (equilibrated): [H⁺] = 68 nM, [HCO₃⁻] = 14 mM, pH = 7.17. **Bottom row — adding 10 mmol NaOH:** Stage 2B: nearly 10 mmol of OH⁻ combines with H⁺ derived from newly entering CO₂ → one HCO₃⁻ formed per OH⁻ buffered. Stage 3B: [H⁺] = 28 nM, [HCO₃⁻] = 34 mM, pH = 7.55. The takeaway is that the open-buffer absorbs >99.9997% of the added strong acid or base.

#### Figure 28-4 — Buffering power of the CO₂/HCO₃⁻ system *(listed)*
Plot of $\beta$ (mM/pH unit, y-axis, 0–250) vs pH (x-axis, 5.5–8.0) for a CO₂/HCO₃⁻ solution at fixed $P_{\text{CO}_2} = 40$ mm Hg. **Blue curve (open system):** $\beta_{\text{open}} = 2.3 \cdot [\text{HCO}_3^-]$ rises exponentially because [HCO₃⁻] does; at pH 7.4 it equals ~55 mM/pH unit. **Black curve (closed system):** bell-shaped with peak at pK = 6.1; at pH 7.4 it is only ~2.6 mM/pH unit. The vertical separation at physiological pH is the chapter's quantitative argument for why the lung-controlled CO₂/HCO₃⁻ system dominates whole-blood buffering.

#### Figure 28-5 — Doubling of CO₂ or HCO₃⁻ concentrations *(listed)*
Two parallel three-stage cartoons (same Henry's-law geometry as Fig. 28-3). **Top — doubling P_CO₂ from 40 → 80 mm Hg (respiratory acidosis in absence of non-HCO₃⁻ buffers):** [CO₂]_dis doubles to 2.4 mM (Stage 2A); only a vanishing flux (~40 nmol/L, "X") passes through the equilibration chain because every H⁺ formed remains free. New equilibrium (Stage 3A): [H⁺] ~80 nM (doubled), [HCO₃⁻] ~24.000,040 mM (unchanged to 6 figures), pH = 7.10 (Eqs. 28-22, 28-23). **Bottom — doubling [HCO₃⁻] from 24 → 48 mM by adding 24 mmol NaHCO₃ at fixed P_CO₂ = 40 mm Hg (metabolic alkalosis in absence of non-HCO₃⁻ buffers):** the extra HCO₃⁻ drives CO₂ formation, which simply vents to the atmosphere; new equilibrium [H⁺] ~20 nM, [HCO₃⁻] ~47.999,980 mM, pH = 7.70 (Eqs. 28-25, 28-26). **Bottom line:** in pure CO₂/HCO₃⁻ solution, doubling CO₂ drops pH by 0.3; doubling HCO₃⁻ raises pH by 0.3 — both with negligible change in the "spectator" species. Real blood, with its ~25 mM/pH-unit non-HCO₃⁻ buffering, instead allows substantial [HCO₃⁻] excursions (next section).

---

## Section 2 — Acid-base chemistry when CO₂/HCO₃⁻ is the only buffer (pp. 632–635)

### Subsection headings (verbatim)
- **In the absence of other buffers, doubling P_CO₂ causes pH to fall by 0.3 but causes almost no change in [HCO₃⁻]** (pp. 633–634)
- **In the absence of other buffers, doubling [HCO₃⁻] causes pH to rise by 0.3** (pp. 634–635)

### Core claims

#### The four primary disturbances introduced (Table 28-3)
The chapter's organizing dichotomy: **respiratory** disturbances begin with a change in $P_{\text{CO}_2}$ (lung), and **metabolic** disturbances begin with a change in [HCO₃⁻] at fixed $P_{\text{CO}_2}$ (kidney + tissues).

| Disorder | Proximate cause | Representative clinical causes | pH | [HCO₃⁻] | P_CO₂ |
|---|---|---|---|---|---|
| **Respiratory acidosis** | ↑ P_CO₂ | ↓ alveolar ventilation (drug OD, COPD, severe asthma, neuromuscular weakness); ↓ diffusing capacity (pulmonary edema); V̇/Q̇ mismatch | ↓ | ↑ (compensation) | ↑ |
| **Respiratory alkalosis** | ↓ P_CO₂ | ↑ alveolar ventilation: hypoxia (altitude), anxiety, salicylate (aspirin) intoxication, central stimulants, sepsis, hepatic failure | ↑ | ↓ (compensation) | ↓ |
| **Metabolic acidosis** | Addition of an acid other than CO₂/H₂CO₃, or removal of alkali at fixed P_CO₂ | ↓ urinary H⁺ secretion (renal failure, RTA); ketoacidosis (DKA); lactic acidosis (shock, ischemia, severe exercise); diarrhea with HCO₃⁻ loss; toxic alcohols | ↓ | ↓ | unchanged (initially) |
| **Metabolic alkalosis** | Addition of alkali, or removal of acid other than CO₂/H₂CO₃, at fixed P_CO₂ | NaHCO₃ load; loss of gastric H⁺ (vomiting, NG suction); diuretic-induced contraction alkalosis; mineralocorticoid excess | ↑ | ↑ | unchanged (initially) |

#### Respiratory acidosis without other buffers
Double $P_{\text{CO}_2}$ from 40 → 80 mm Hg. With no other buffers, only a vanishing flux $X$ of CO₂ passes through CO₂ + H₂O → H⁺ + HCO₃⁻ before the equilibrium constant is satisfied (Eq. 28-21):

$$10^{-6.1} \text{ M} = \frac{(0.000040 \text{ mM} + X)(24 \text{ mM} + X)}{2.4 \text{ mM}}$$

Solving gives $X \approx 0.000040$ mmol — a 40 nanomolar flux. [H⁺] doubles (40 → 80 nM); [HCO₃⁻] increases by only ~40 nM (negligible against 24 mM); $\text{pH} = -\log(80 \text{ nM}) = 7.10$. The same answer from H-H (Eq. 28-23): $\text{pH} = 6.1 + \log[24/(0.03 \times 80)] = 7.10$.

#### Respiratory alkalosis without other buffers
Halve $P_{\text{CO}_2}$ from 40 → 20 mm Hg → pH rises by 0.3 → final pH = 7.70. Symmetric to the above.

#### Metabolic alkalosis without other buffers
Double [HCO₃⁻] from 24 → 48 mM by adding 24 mmol NaHCO₃ (or removing 24 mmol HCl, e.g., **gastric H⁺ loss from severe vomiting** — see Table 28-3 and N28-7). The added HCO₃⁻ drives the equilibrium toward CO₂; the surplus CO₂ vents to the atmosphere because the system is open. Final pH = 7.70 (Eqs. 28-25, 28-26).

#### Metabolic acidosis without other buffers
Remove half the [HCO₃⁻] (or add 12 mM HCl) → pH falls by 0.3 → 7.10. Common clinical causes: **renal failure** (failure to excrete the ~1 mmol/kg/d daily acid load from protein metabolism), **DKA** (acetoacetate + β-hydroxybutyrate from accelerated lipolysis), **lactic acidosis** (anaerobic glycolysis in shock or ischemia), and **diarrhea** (loss of bicarbonate-rich intestinal fluid).

#### The whimsical Henderson-Hasselbalch (Eq. 28-27)
Because $P_{\text{CO}_2}$ is set by the lungs (Ch 31) and [HCO₃⁻] is set by the kidneys (Ch 39), Boron writes the H-H equation as

$$\text{pH} = \text{Constant} + \frac{\text{Kidneys}}{\text{Lungs}} \quad (\text{Eq. 28-27})$$

to underline that **arterial pH is under joint dual control of the two organ systems**, and that derangement of either, or compensation by either, moves pH along the H-H trajectory.

### Equations
$$10^{-\text{p}K} = \frac{[\text{H}^+][\text{HCO}_3^-]}{s\cdot P_{\text{CO}_2}} \quad (\text{Eq. 28-14})$$

$$\text{pH} = \text{Constant} + \frac{\text{Kidneys}}{\text{Lungs}} \quad (\text{Eq. 28-27})$$

### Citation-anchor quotes
- > "This disturbance is an example of a CO₂ titration, because we initiated it by altering P_CO₂. More specifically, it is a respiratory acidosis—'acidosis' because pH falls, and 'respiratory' because pulmonary problems … are the most common causes of an increase in the P_CO₂ of arterial blood." (p. 633)
- > "Thus, in the absence of non-HCO₃⁻ buffers, doubling [CO₂] causes pH to fall by 0.3, whereas halving [CO₂] causes pH to rise by 0.3." (p. 634)
- > "Because it is the kidney that controls [HCO₃⁻] in the blood plasma … and because it is the lung that controls P_CO₂ … the pH of blood plasma is under the dual control of both organ systems." (p. 635)

### Table — Table 28-3 (reproduced above as the "four primary disturbances" table)

---

## Section 3 — Acid-base chemistry with non-HCO₃⁻ buffers — the Davenport diagram (pp. 635–641)

### Subsection headings (verbatim)
- **The Davenport diagram is a graphical tool for interpreting acid-base disturbances in blood** (pp. 635–637)
- **The amount of HCO₃⁻ formed or consumed during "respiratory" acid-base disturbances increases with β_non-HCO₃⁻** (p. 637)
- **Adding or removing an acid or base—at a constant P_CO₂—produces a "metabolic" acid-base disturbance** (pp. 638–639)
- **During metabolic disturbances, CO₂/HCO₃⁻ makes a greater contribution to total buffering when pH and P_CO₂ are high and when β_non-HCO₃⁻ is low** (pp. 639–641)

### Core claims

#### Anatomy of the Davenport diagram
- **Axes.** x: arterial pH (commonly 6.8–8.0); y: [HCO₃⁻] (commonly 0–100 mM, often plotted 0–50 mM for clinical work).
- **CO₂ isopleths (isobars).** Curves of constant $P_{\text{CO}_2}$. By Henderson-Hasselbalch rearranged (Eq. 28-29): $[\text{HCO}_3^-] = s \cdot P_{\text{CO}_2} \cdot 10^{\text{pH} - \text{p}K}$. Each isopleth rises **exponentially** with pH. Standard isopleths: 20 mm Hg (alkalemia), 40 mm Hg (normal), 80 mm Hg (acidemia). The slope of an isopleth at a given pH equals $\beta_{\text{open}}$ (Eq. 28-20), so steeper isopleths sit at higher pH or higher [HCO₃⁻].
- **The non-HCO₃⁻ titration line.** Negative slope $-\beta_{\text{non-HCO}_3^-}$, normally ~25 mM/pH unit (the slope of the red curve in Fig. 28-2B over the physiological range). It is the locus of all acid-base states accessible by **respiratory** disturbance alone: starting from "Start" (pH 7.40, [HCO₃⁻] 24 mM, $P_{\text{CO}_2}$ 40 mm Hg), moving along this line carries you to the high-P_CO₂ isopleth (respiratory acidosis, lower pH, higher [HCO₃⁻] — because non-HCO₃⁻ buffers absorb H⁺ and shift CO₂ + H₂O → HCO₃⁻ + H⁺ forward) or to the low-P_CO₂ isopleth (respiratory alkalosis, higher pH, lower [HCO₃⁻]).
- **Movements parallel to the non-HCO₃⁻ titration line, displaced upward or downward by Δ[HCO₃⁻], represent metabolic disturbances** at fixed $P_{\text{CO}_2}$ — adding alkali raises the line; adding acid lowers it.

#### Solving the doubled-P_CO₂ problem with the Davenport (Fig. 28-6C)
Step 1: locate "Start" at the intersection of the 40-mm-Hg isopleth and the normal non-HCO₃⁻ titration line (pH 7.40, [HCO₃⁻] 24 mM).
Step 2: identify the new 80-mm-Hg isopleth.
Step 3: follow the non-HCO₃⁻ titration line to its intersection with the 80-mm-Hg isopleth → point **A** at pH 7.19, [HCO₃⁻] 29.25 mM.

Comparison: with no non-HCO₃⁻ buffers, doubling P_CO₂ gave pH 7.10 (Eq. 28-22). With $\beta_{\text{non-HCO}_3^-}$ = 25 mM/pH unit, pH only falls to 7.19 — the non-HCO₃⁻ buffers absorbed 5.25 mmol H⁺ per liter (Eq. 28-30 flux):

$$\text{CO}_2 + \text{H}_2\text{O} \xrightarrow{\sim 5.25 \text{ mM}} \text{HCO}_3^- + \text{H}^+$$

and **drove the conversion of CO₂ to HCO₃⁻**, raising [HCO₃⁻] from 24 to 29.25 mM (Table 28-5). Hemoglobin, in particular, is the major proton sink — its imidazole rings have pK's near 7, ideally placed for this buffering, which is why **anemic patients have a lower $\beta_{\text{non-HCO}_3^-}$ and lower [HCO₃⁻] rise during acute respiratory acidosis**, and polycythemic patients the reverse.

#### Solving the metabolic-acidosis problem (Fig. 28-7 left)
Add 10 mmol HCl to 1 L of blood-like solution. Four-step graphical solution:
- Step 1: locate "Start."
- Step 2: drop straight down by 10 mM (the amount of H⁺ added) → asterisk point.
- Step 3: through the asterisk draw a line parallel to the non-HCO₃⁻ titration line.
- Step 4: follow this new line to its intersection with the original 40-mm-Hg isopleth → point **C** at pH 7.26, [HCO₃⁻] 17.4 mM.

Bookkeeping: of the 10 mmol H⁺ added, 6.6 mmol is buffered by HCO₃⁻ → CO₂ (which vents); 3.4 mmol is buffered by non-HCO₃⁻ buffers; ~0.000015 mmol remains free and is responsible for the pH drop from 7.40 to 7.26. The **complementary alkalosis problem** (add 10 mmol NaOH) gives point **D** at pH 7.51, [HCO₃⁻] 31.1 mM (Fig. 28-7 right).

#### CO₂/HCO₃⁻ buffers alkali better than acid
Table 28-6 (reproduced): the mean $\beta_{\text{open}}$ over the metabolic-alkalosis trajectory (pH 7.40 → 7.51) is ~65 mM/pH unit; over the metabolic-acidosis trajectory (pH 7.40 → 7.26) it is only ~47 mM/pH unit. Because $\beta_{\text{open}} = 2.3 \cdot [\text{HCO}_3^-]$ rises exponentially with pH, **adding alkali always produces a smaller pH change than adding an equivalent amount of acid** (the same lung-physiologic asymmetry that drives the chemoreceptor curve's leftward steepening in Ch 32).

#### Patient-specific β_non-HCO₃⁻
- $\beta_{\text{non-HCO}_3^-}$ tracks **hemoglobin concentration**. Patients with anemia have low $\beta_{\text{non-HCO}_3^-}$ (so their pH excursions for the same acid-base insult are larger); polycythemia has the reverse.
- Patients with chronically elevated $P_{\text{CO}_2}$ (e.g., compensated COPD) have higher [HCO₃⁻] and therefore higher $\beta_{\text{open}}$ — a built-in protection against further pH drift.

#### The anion gap (not formally derived here; clinically essential)
Although the chapter does not derive it as a numbered equation, the **anion gap** is the clinical bridge from Davenport-diagram metabolic acidosis to mechanism:

$$\text{AG} = [\text{Na}^+] - ([\text{Cl}^-] + [\text{HCO}_3^-]) \approx 8\text{–}12 \text{ mEq/L (normal)}$$

| Anion-gap pattern | Mechanism | Clinical causes |
|---|---|---|
| **High AG metabolic acidosis** | Acid added contributes an unmeasured anion (titrating HCO₃⁻ down without replacing Cl⁻) | **MUDPILES**: Methanol, Uremia, DKA, Propylene glycol, Isoniazid/Iron, Lactic acidosis, Ethylene glycol, Salicylates |
| **Normal AG (hyperchloremic) metabolic acidosis** | HCO₃⁻ loss replaced by Cl⁻ (electroneutrality) | Diarrhea; renal tubular acidosis (proximal type 2, distal type 1, hyperkalemic type 4); carbonic anhydrase inhibitors (acetazolamide); recovery from DKA after Cl⁻-rich resuscitation |

The expected respiratory compensation to metabolic acidosis is captured by **Winter's formula**: $P_{\text{CO}_2} \approx 1.5 \cdot [\text{HCO}_3^-] + 8 \pm 2$ mm Hg.

### Stewart's strong-ion difference (Box 28-1)
- **SID** = ([Na⁺] + [K⁺] + [Ca²⁺] + [Mg²⁺]) − [Cl⁻] (with other strong anions added if measured). Stewart's framework treats SID, total weak-acid concentration A_TOT, and $P_{\text{CO}_2}$ as the three independent variables that determine pH.
- Boron's critique (Box 28-1): "proteins and physiological processes generally depend on pH, not SID"; "cells and the body closely regulate pH but have no known mechanism for directly sensing or regulating SID"; "SID neither is uniquely related to pH nor has a causal role in changing pH." He retains the classical pH/buffer approach throughout the chapter.

### Equations

$$[\text{HCO}_3^-] = s \cdot P_{\text{CO}_2} \cdot 10^{\text{pH} - \text{p}K} \quad (\text{Eq. 28-29; CO}_2 \text{ isopleth in Davenport space)}$$

$$\text{slope of CO}_2 \text{ isopleth at pH} = \beta_{\text{open}}(\text{pH}) = 2.3 \cdot [\text{HCO}_3^-](\text{pH})$$

$$\text{slope of non-HCO}_3^- \text{ titration line} = -\beta_{\text{non-HCO}_3^-} \approx -25 \text{ mM/pH unit (whole blood)}$$

$$\text{AG} = [\text{Na}^+] - ([\text{Cl}^-] + [\text{HCO}_3^-]) \approx 8\text{–}12 \text{ mEq/L (normal)}$$

$$\text{Winter's formula (metabolic acidosis): } P_{\text{CO}_2}^{\text{expected}} \approx 1.5 \cdot [\text{HCO}_3^-] + 8 \pm 2 \text{ mm Hg}$$

$$\text{SID} \approx ([\text{Na}^+] + [\text{K}^+] + [\text{Ca}^{2+}] + [\text{Mg}^{2+}]) - [\text{Cl}^-] \quad (\text{Box 28-1})$$

### Citation-anchor quotes
- > "Each of the isopleths in Figure 28-6A rises exponentially with pH. The slope of each isopleth also rises exponentially with pH and represents β_open for CO₂/HCO₃⁻." (p. 636)
- > "Thus, the non-HCO₃⁻ buffers drive the conversion of CO₂ to HCO₃⁻. These buffers minimize the increase in free [H⁺] that a given flux of CO₂ can produce." (p. 637)
- > "β_non-HCO₃⁻ varies with the hemoglobin content of blood. Thus, patients with anemia have a low β_non-HCO₃⁻, whereas patients with polycythemia have a high β_non-HCO₃⁻." (p. 637)
- > "Adding alkali will always cause a smaller pH change than adding an equivalent amount of acid." (p. 640)
- > "Because the SID approach provides no new mechanistic insight, we focus on the classical pH/buffer approach." (p. 638, Box 28-1)

### Tables (Section 3)

#### Table 28-4 — Relationship between [HCO₃⁻] and pH at three fixed P_CO₂ levels

| pH | [HCO₃⁻] at P_CO₂ = 20 mm Hg | [HCO₃⁻] at P_CO₂ = 40 mm Hg | [HCO₃⁻] at P_CO₂ = 80 mm Hg |
|---|---|---|---|
| 6.8 | 4.8 mM | 9.6 mM | 19.2 mM |
| 7.0 | 7.5 | 15.0 | 30.0 |
| 7.1 | 9.5 | 19.0 | 38.0 |
| 7.2 | 12 | 24 | 48 |
| 7.4 | 19 | 38 | 76 |
| 7.7 | 38 | 76 | 152 |

(Each row obeys Eq. 28-29; doubling $P_{\text{CO}_2}$ at fixed pH doubles [HCO₃⁻]. The columns become the colored isopleths of Fig. 28-6A.)

#### Table 28-5 — Relationship between β_non-HCO₃⁻ and HCO₃⁻ formed in response to doubling P_CO₂

| β_non-HCO₃⁻ | ΔpH | ΔHCO₃⁻ formed | Fractional Δ[H⁺] | Fractional Δ[HCO₃⁻] | Fractional Δ[HCO₃⁻] × Δ[H⁺] |
|---|---|---|---|---|---|
| 0 | −0.30 | 0.000040 mM | ~2.000 | ~1.000 | 2.00 |
| 25 mM/pH | −0.21 | 5.25 mM | 1.61 | 1.24 | 2.00 |
| ∞ | 0 | 24.0 mM | 1.00 | 2.00 | 2.00 |

Across all rows the product [HCO₃⁻]·[H⁺] doubles (because the equilibrium constant K is invariant and [CO₂]_dis doubles). What changes is the **partitioning** of that doubling between Δ[HCO₃⁻] (set by non-HCO₃⁻ buffering) and Δ[H⁺] (the pH excursion).

#### Table 28-6 — Buffering produced by CO₂/HCO₃⁻ and non-HCO₃⁻ buffers (1 L; start pH 7.40, P_CO₂ 40 mm Hg, [HCO₃⁻] 24 mM; β_non-HCO₃⁻ = 25 mM/pH unit)

| Addition | ΔpH | Δ[HCO₃⁻] | β_open | Δ[HB^(n+1)] | β_non-HCO₃⁻ | β_total |
|---|---|---|---|---|---|---|
| +10 mmol H⁺ | −0.14 | ~−6.6 mM | 47 mM/pH | ~3.4 mM | 25 mM/pH | 72 mM/pH |
| +10 mmol OH⁻ | +0.11 | ~+7.1 mM | 65 mM/pH | ~2.9 mM | 25 mM/pH | 89 mM/pH |

CO₂/HCO₃⁻ is a better buffer above 7.40 than below, because $\beta_{\text{open}} \propto [\text{HCO}_3^-]$ rises with pH.

### Figures (Section 3)

#### Figure 28-6 — Davenport diagram *(viewed)*
Four-panel composite that builds the diagram one ingredient at a time. **Panel A — CO₂ isopleths:** x-axis pH (6.8–8.0), y-axis [HCO₃⁻] (0–100 mM). Three exponentially-rising isopleths labeled $P_{\text{CO}_2}$ = 80 mm Hg (green, steepest), 40 mm Hg (blue, normal, intersecting (7.40, 24)), and 20 mm Hg (orange, shallowest). At any pH a vertical line cuts the three isopleths at [HCO₃⁻] values in 2:1:0.5 ratio. **Panel B — Non-HCO₃⁻ titration curves:** the textbook's nine-buffer construction from Fig. 28-2B replotted here as cumulative [HB^(n+1)] vs pH. The green curve is the single buffer with pK = 7; the eight black curves are the other eight buffers (pK's spaced by 0.5 unit); the red curve is the sum. Over the central pH range (~6.5–8.5) the red curve is nearly linear with slope ≈ −25 mM/pH unit (the negative of $\beta_{\text{non-HCO}_3^-}$). The dashed box marks the segment that becomes the red **non-HCO₃⁻ titration line** of panels C and D. **Panel C — Effect of respiratory acidosis and alkalosis:** the three isopleths from A superimposed with the red non-HCO₃⁻ titration line from B. "Start" sits at the intersection of the blue isopleth (40 mm Hg) and the red line (7.40, 24). The red arrow up-and-leftward along the red line ends at the green isopleth (80 mm Hg) at point **A** (pH 7.19, [HCO₃⁻] 29.25 mM) — uncompensated respiratory acidosis. The red arrow down-and-rightward along the red line ends at the orange isopleth (20 mm Hg) at point **B** (pH 7.60, [HCO₃⁻] 19 mM) — uncompensated respiratory alkalosis. **Panel D — Effect of changing β_non-HCO₃⁻:** three non-HCO₃⁻ titration lines through "Start" at slopes 0 (horizontal — no non-HCO₃⁻ buffers), −25 mM/pH (normal), and −∞ (vertical — infinitely strong non-HCO₃⁻ buffers). Doubling P_CO₂ moves the system along each line to its intersection with the 80 mm Hg isopleth: point A₀ (pH 7.10, [HCO₃⁻] unchanged), point A (pH 7.19, [HCO₃⁻] 29.25 mM), point A_∞ (pH 7.40, [HCO₃⁻] 48 mM). In every case the product [HCO₃⁻]·[H⁺] exactly doubles.

> Vision note: This is the canonical four-panel construction of the Davenport diagram. Anchor for every subsequent acid-base figure in the chapter (28-7 through 28-11) and for nephrology / pulmonology bedside reasoning.

#### Figure 28-7 — Metabolic acidosis and alkalosis in the presence of non-HCO₃⁻ buffers *(viewed)*
Two-panel Davenport diagram. **Left — adding 10 mmol HCl (metabolic acidosis):** the four-step graphical solution. Black arrow "2" drops vertically from "Start" by 10 mM to an asterisk at (7.40, 14 mM); a black line through the asterisk parallel to the red non-HCO₃⁻ titration line cuts the 40 mm Hg isopleth at point **C** (pH 7.26, [HCO₃⁻] 17.4 mM). Black arrow "4" curves from the asterisk to C along the new black line. The pathway maps the partitioning of H⁺: ~6.6 mmol absorbed by HCO₃⁻ → CO₂ (vented), ~3.4 mmol absorbed by non-HCO₃⁻ buffers, ~0.000015 mmol remaining free. **Right — adding 10 mmol NaOH (metabolic alkalosis):** mirror image. A new black line displaced upward by 10 mM from the red titration line cuts the 40 mm Hg isopleth at point **D** (pH 7.51, [HCO₃⁻] 31.1 mM). CO₂/HCO₃⁻ buffered ~7.1 mmol of the OH⁻ (slightly more than for acid because $\beta_{\text{open}}$ is larger at higher pH); non-HCO₃⁻ buffers handled ~2.9 mmol.

> Vision note: This is the figure that operationalizes the four-step Davenport algorithm for metabolic disturbances. Every bedside acid-base problem reduces to a version of this procedure. Anchor for vomiting (loss of HCl → metabolic alkalosis), diarrhea (loss of HCO₃⁻ → metabolic acidosis), DKA (gain of organic acids → high-AG metabolic acidosis).

#### Figure 28-8 — Effect of β_non-HCO₃⁻ on the pH increase caused by metabolic alkalosis *(listed)*
Three vertically-stacked Davenport-style panels, each showing the consequences of adding 10 mmol NaOH at $P_{\text{CO}_2}$ = 40 mm Hg. **A — β_non-HCO₃⁻ = 0:** non-HCO₃⁻ line is horizontal; black line displaced up by 10 mM intersects the 40 mm Hg isopleth at point D₀ (pH 7.55, [HCO₃⁻] 34 mM). CO₂/HCO₃⁻ buffered all 10 mmol of OH⁻; ΔpH = +0.15. **B — β_non-HCO₃⁻ = 25 mM/pH:** non-HCO₃⁻ line has the normal slope; same construction gives point D (pH 7.51, [HCO₃⁻] 31.1 mM); CO₂/HCO₃⁻ buffered 7.1 mmol, non-HCO₃⁻ buffered 2.9 mmol; ΔpH = +0.11. **C — β_non-HCO₃⁻ = ∞:** non-HCO₃⁻ line is vertical; the displaced line lies right on top of it, so no movement on the diagram; non-HCO₃⁻ buffers absorb all 10 mmol; [HB^(n+1)] rises by 10 mM, ΔpH = 0. Three-panel monotone: the more non-HCO₃⁻ buffering power, the smaller the pH excursion; the open CO₂/HCO₃⁻ contribution shrinks accordingly.

#### Figure 28-9 — Metabolic compensation to primary respiratory acid-base disturbances *(viewed)*
Two-panel Davenport. **A — Metabolic compensation to respiratory acidosis:** start at "Start" (pH 7.40, $P_{\text{CO}_2}$ 40); a primary respiratory acidosis (red arrow along the red non-HCO₃⁻ titration line) ends at point A (pH 7.19, [HCO₃⁻] 29.25 mM) on the 80 mm Hg isopleth. The kidney response: secrete more H⁺ (and reabsorb/generate more HCO₃⁻), displacing the cell from the original non-HCO₃⁻ line upward. Adding 10 mmol OH⁻ equivalent moves the cell to point A₁ (pH 7.29) — **partial compensation**. Adding an additional 14 mmol → total of 24 mmol OH⁻ equivalent (which numerically equals the starting [HCO₃⁻]) brings pH back to 7.40 at point A₂ — **perfect compensation = isohydric hypercapnia** (same pH at doubled P_CO₂; Eq. 28-31). **B — Metabolic compensation to respiratory alkalosis:** the mirror. Start → red arrow to point B (pH 7.60, [HCO₃⁻] 19 mM) at 20 mm Hg isopleth. Adding 10 mmol H⁺ moves to B₁ (pH 7.51) — partial. Adding 12 mmol H⁺ total returns pH to 7.40 (perfect compensation = isohydric hypocapnia). The renal compensation here is to secrete less H⁺ (lose more HCO₃⁻ in urine).

> Vision note: The graphical proof that **perfect compensation requires the metabolic correction to scale linearly with the starting [HCO₃⁻]** — doubling P_CO₂ requires an OH⁻ load equal to the original [HCO₃⁻] (24 mM); halving P_CO₂ requires an H⁺ load equal to half the original [HCO₃⁻] (12 mM). Real renal compensation is never perfect — it takes 3–5 days to fully develop and typically returns pH most of the way (but not all the way) to 7.40.

#### Figure 28-10 — Respiratory compensation to primary metabolic acid-base disturbances *(listed)*
Two-panel Davenport. **A — Respiratory compensation to metabolic acidosis:** start at "Start"; the primary metabolic acidosis (adding 10 mmol HCl) ends at point C (pH 7.26, [HCO₃⁻] 17.4 mM) on the 40 mm Hg isopleth. Hyperventilation (driven by peripheral and central chemoreceptors sensing low pH; Ch 32) lowers $P_{\text{CO}_2}$ from 40 → 30 mm Hg → moves along the new (post-HCl) non-HCO₃⁻ line to C₁ (pH 7.34) — partial. Further hyperventilation to $P_{\text{CO}_2}$ = 23.4 mm Hg returns pH to 7.40 at C₂ — perfect. The required fractional $P_{\text{CO}_2}$ decrease (40 − 23.4)/40 = 42% equals the fractional [HCO₃⁻] decrease (10/24 = 42%) — the lung perfectly mirrors the metabolic insult. **B — Respiratory compensation to metabolic alkalosis:** start → D (pH 7.51, [HCO₃⁻] 31.1 mM) from +10 mmol NaOH; hypoventilation raises $P_{\text{CO}_2}$ from 40 → 50 mm Hg → D₁ (pH 7.44, partial). To reach D₂ (pH 7.40, perfect) requires $P_{\text{CO}_2}$ = 56.7 mm Hg. **Boron's caveat:** respiratory compensation to metabolic alkalosis is the least perfect of the four because hypoventilation past a certain limit produces hypoxemia incompatible with life. Real-world respiratory compensation to metabolic alkalosis seldom raises $P_{\text{CO}_2}$ above ~55 mm Hg.

#### Figure 28-11 — Acid-base states represented by position on a Davenport diagram *(viewed)*
Four-panel Davenport with the same axes (pH on x, [HCO₃⁻] on y), the same 40-mm-Hg isopleth (blue) and 80- and 20-mm-Hg isopleths (green/orange), and the same red non-HCO₃⁻ titration line. **A — Uncompensated:** four labeled points: A (respiratory acidosis), B (respiratory alkalosis), C (metabolic acidosis), D (metabolic alkalosis). A and B lie on the red line off the 40 mm Hg isopleth (respiratory disturbances). C and D lie on the 40 mm Hg isopleth off the red line (metabolic disturbances). **B — Partially compensated:** four colored regions, each anchored by an arrow from the uncompensated point toward a partially compensated state. Compensated respiratory acidosis (point A₁) sits in the blue wedge bounded by the original red line, the vertical pH = 7.4 line, and the 80 mm Hg isopleth. Compensated respiratory alkalosis fills the corresponding orange wedge on the right side. Compensated metabolic acidosis and alkalosis fill green and yellow wedges. **C — Perfectly compensated:** all four primary disturbances, when perfectly compensated, lie on the vertical line through pH = 7.4. A₂ = D₂ defines isohydric hypercapnia; B₂ = C₂ defines isohydric hypocapnia. **D — Compound disturbances:** the two off-axis wedges that the four primary regions don't cover. Points A₃ and C₃ (lower-right quadrant) represent respiratory acidosis + metabolic acidosis (both pulling pH down — the classic "double-hit" of respiratory failure + renal failure in ICU patients). Mirror wedge represents respiratory alkalosis + metabolic alkalosis.

> Vision note: This is the chapter's bedside diagnostic atlas. Given a blood-gas {pH, P_CO₂, [HCO₃⁻]}, the clinician locates the point on the Davenport and reads off its region to classify the disturbance and the state of compensation. Anchor for clinical pulmonology and nephrology rounds.

---

## Section 4 — pH regulation of intracellular fluid (pp. 644–646)

### Subsection headings (verbatim)
- **Ion transporters at the plasma membrane closely regulate the pH inside of cells** (pp. 644–645)
- **Indirect interactions between K⁺ and H⁺ make it appear as if cells have a K-H exchanger** (p. 645)
- **Changes in intracellular pH are often a sign of changes in extracellular pH, and vice versa** (pp. 645–646)

### Core claims

#### The acid-extruder / acid-loader dichotomy (Fig. 28-12A)
Every cell maintains pH_i (~7.2 in a typical cell, Table 28-2) by a balance between **acid extruders** that tend to raise pH_i and **acid loaders** that tend to lower it. The textbook's prototypical set:

| Direction | Transporter | Slug | Driving force | Mechanism |
|---|---|---|---|---|
| **Acid extruder** | **NHE1** (SLC9A1) | Na/H exchanger | inward Na⁺ gradient | exports 1 H⁺ in exchange for 1 Na⁺ |
| **Acid extruder** | **NBCn1** (SLC4A7) | electroneutral Na/HCO₃ cotransporter | inward Na⁺ gradient | imports 1 Na⁺ + 1 HCO₃⁻ |
| **Acid extruder** (in some cells) | **NBCe1** (SLC4A4) | electrogenic Na/HCO₃ cotransporter (1 Na : 2–3 HCO₃) | inward Na⁺ + voltage | depending on stoichiometry/orientation, can be an extruder in epithelia or a loader in proximal tubule |
| **Acid loader** | **AE2** (SLC4A2) | Cl/HCO₃ exchanger | outward HCO₃⁻ gradient + inward Cl⁻ gradient | exports 1 HCO₃⁻ in exchange for 1 Cl⁻ |
| **Acid loader / extruder** | **MCT1–4** (SLC16A) | monocarboxylate / H⁺ cotransporters | gradients of lactate, pyruvate, ketone bodies + H⁺ | export or import a monocarboxylic anion with H⁺ — physiologically the export route for lactic acid from glycolytic and exercising tissue |
| **Specialized acid extruder** | **gastric H/K-ATPase** (parietal cells) | H/K pump | ATP | exports 1 H⁺ in exchange for 1 K⁺ — basis of gastric HCl secretion (Ch 42) |
| **Specialized acid extruder** | **V-type H⁺-ATPase** (α-intercalated cells, osteoclasts, vesicles) | proton pump | ATP | exports 1 H⁺ across plasma membrane (kidney; Ch 39) or into vesicle lumen |

A steady-state pH_i emerges when extruder flux = loader flux. **Push-pull regulation**: low pH_i stimulates extruders AND inhibits loaders; high pH_i does the reverse. The two limbs of the feedback are pH_i-dependent in opposite senses, producing a tight set-point near pH_i = 7.2.

#### Recovery from acute acid and alkaline loads (Fig. 28-12B–F)
- **Acid load (HCl micro-injection).** pH_i falls within seconds (intracellular metabolic acidosis), then spontaneously recovers to baseline over minutes via active NBCn1 + NHE1 (Fig. 28-12B, black curve). Carbonic anhydrase catalyzes HCO₃⁻ ↔ CO₂ + H₂O so that incoming HCO₃⁻ buffers H⁺ without changing intracellular CO₂.
- **Alkaline load (KOH micro-injection).** pH_i rises, then spontaneously recovers via AE2 (Fig. 28-12E, black curve).
- **pH_o sensitivity (Fig. 28-12B,E red and blue curves).** A simultaneous extracellular acidosis (low pH_o, red curve) slows pH_i recovery from an acid load and lowers the final steady-state pH_i — because extracellular protons shift the pH_i-dependence curve of acid extruders leftward (less extruder activity at any given pH_i; Fig. 28-12C, red curve) and stimulate acid loaders (Fig. 28-12F, red curve). Extracellular alkalosis does the opposite (blue curves).

#### Three-phase intracellular response to extracellular respiratory acidosis (Fig. 28-13)
1. **Phase A (seconds): CO₂ entry → rapid pH_i fall.** Elevated arterial $P_{\text{CO}_2}$ creates an inward CO₂ gradient. CO₂ diffuses freely across the plasma membrane; carbonic anhydrase hydrates it to H⁺ + HCO₃⁻ inside the cell within seconds. Intracellular pH falls in parallel with extracellular pH.
2. **Phase B (minutes): feeble intracellular extruder recovery.** NHE1 and NBCn1 would normally extrude the added H⁺, but extracellular acidosis simultaneously inhibits extrusion and stimulates loading, so pH_i barely recovers. The cell is effectively stuck.
3. **Phase C (hours–days): renal metabolic compensation rescues both pH_o and pH_i.** Renal acid secretion + new HCO₃⁻ generation raises arterial pH_o; the rising pH_o releases the inhibition on extruders and the stimulation of loaders; pH_i recovers in parallel with pH_o, typically reaching 20–60% of the ΔpH_o correction.

This is the chapter's mechanistic argument for why **"the primary reason that the body regulates the pH of the blood plasma and extracellular fluids is to allow the cells to properly regulate their pH_i"** (p. 646).

#### The apparent K-H exchanger
- Clinical: **extracellular acidosis ↔ hyperkalemia** (clinically observed in DKA, renal failure with metabolic acidosis, etc.) and **hyperkalemia ↔ intracellular alkalosis**.
- Boron's reanalysis: there is **no general K-H exchanger** in mammalian cells (the gastric H/K-ATPase is the only true exception). The phenomenology is instead **depolarization-induced alkalinization**: hyperkalemia depolarizes the membrane → electrogenic NBC (Na : ≥2 HCO₃) flips its driving force → net HCO₃⁻ uptake → pH_i rises. Conversely, low pH_o inhibits transporters responsible for K⁺ uptake → net K⁺ efflux → hyperkalemia.
- "Imagining that a K-H exchanger exists is sometimes a helpful tool for quickly predicting interactions of H⁺ and K⁺ in a clinical setting" (p. 645) — useful clinical heuristic, mechanistically incorrect.

#### Cellular sensors of pH
- **Intracellular sensors** (not fully catalogued in the source but implicit): NHE1's C-terminal tail acts as its own pH_i sensor with allosteric activation below the set-point. Many kinases (e.g., WNK, ERK pathway components) are pH-sensitive.
- **Extracellular sensors**: G-protein-coupled receptors GPR4, GPR65 (TDAG8), and GPR68 (OGR1) are activated by extracellular acidosis. ASICs (acid-sensing ion channels) on neurons detect rapid acid transients (Ch 13, Ch 15).
- **Carotid and aortic peripheral chemoreceptors** (Ch 32, p. 710) and **central chemoreceptors** in the brainstem (Ch 32, pp. 713–715) are the systemic sensors that link pH to the respiratory drive.

### Equations

$$\text{NHE1: } J_{\text{NHE}} = V_{\max}^{\text{NHE}}(pH_i, pH_o) \cdot f(\Delta\mu_{\text{Na}})$$

$$\text{NBCn1 (electroneutral): } 1\,\text{Na}^+_{\text{out}} + 1\,\text{HCO}_3^-_{\text{out}} \rightarrow 1\,\text{Na}^+_{\text{in}} + 1\,\text{HCO}_3^-_{\text{in}}$$

$$\text{AE2: } 1\,\text{HCO}_3^-_{\text{in}} + 1\,\text{Cl}^-_{\text{out}} \rightarrow 1\,\text{HCO}_3^-_{\text{out}} + 1\,\text{Cl}^-_{\text{in}}$$

$$\text{Steady-state pH}_i: \sum J_{\text{extruders}}(pH_i, pH_o, V_m, \ldots) = \sum J_{\text{loaders}}(pH_i, pH_o, V_m, \ldots)$$

$$\Delta \text{pH}_i \approx 0.2\text{–}0.6 \cdot \Delta \text{pH}_o \text{ (typical mammalian cell)} \quad (\text{p. 645–646})$$

### Citation-anchor quotes
- > "Ion transporters at the plasma membrane closely regulate the pH inside of cells." (p. 644)
- > "The response to low pH_i therefore involves two feedback loops operating in push-pull fashion, stimulating acid extrusion and inhibiting acid loading." (p. 645)
- > "Generally, a change in pH_o shifts pH_i in the same direction, but ΔpH_i is usually only 20% to 60% of ΔpH_o. In other words, an extracellular metabolic acidosis causes a net transfer of acid from the extracellular to the intracellular space, and an extracellular metabolic alkalosis has the opposite effect." (p. 646)
- > "The primary reason that the body regulates the pH of the blood plasma and extracellular fluids is to allow the cells to properly regulate their pH_i. The primary reason why the clinical assessment of blood acid-base parameters can be useful is that these parameters tend to parallel cellular acid-base status." (p. 646)

### Figures (Section 4)

#### Figure 28-12 — Recovery of a cell from intracellular acid and alkali loads *(viewed)*
Six-panel composite. **Panel A — Response to intracellular metabolic acidosis:** cell cartoon with three transporters drawn in the plasma membrane: NBCn1 (Na⁺ + HCO₃⁻ in, electroneutral), NHE1 (Na⁺ in, H⁺ out), AE2 (HCO₃⁻ out, Cl⁻ in). After HCl micro-injection, **low pH_i stimulates the two acid extruders (NBCn1, NHE1)** (green up-arrows) **and inhibits the acid loader (AE2)** (red down-arrow). Carbonic anhydrase II accelerates intracellular CO₂ ↔ HCO₃⁻ + H⁺ interconversion. **Panel B — Record of intracellular pH (acid load):** time-course of pH_i after one or two successive HCl injections; the black curve falls sharply, then recovers smoothly to baseline; the red curve (at low pH_o) recovers more slowly and to a lower steady state; the blue curve (at high pH_o) recovers faster and to a higher steady state. **Panel C — pH_i dependence of acid extruders:** Na/HCO₃ cotransporter rate (Y) vs pH_i (X). Three curves: at pH_o = 7.4 (black), at low pH_o (red — shifted left, lower rates everywhere), at high pH_o (blue — shifted right, higher rates everywhere). All curves cross zero at the set-point. **Panel D — Response to intracellular metabolic alkalosis:** KOH micro-injection. High pH_i **inhibits acid extruders and stimulates the acid loader (AE2)**. **Panel E — Record of intracellular pH (alkali load):** mirror of B. **Panel F — pH_i dependence of acid loaders:** Cl/HCO₃ exchange rate vs pH_i; rises with pH_i; shifted left by low pH_o (red, more loader activity at any given pH_i — drives faster acidification) and right by high pH_o (blue).

> Vision note: This is the textbook diagram of cellular pH homeostasis. Anchor for every downstream chapter that needs a cellular pH-regulating cartoon: gastric parietal cell (Ch 42), renal tubule cell (Ch 39), neuronal pH transients (Ch 13), muscle pH during exercise (Ch 60), and tumor pH (oncology).

#### Figure 28-13 — Response of cell to extracellular respiratory acidosis *(listed)*
Two-panel figure. **Panel A — Response of cell:** cell cartoon showing arterial blood with elevated $P_{\text{CO}_2}$. CO₂ enters the cell down its concentration gradient; intracellular carbonic anhydrase catalyzes CO₂ + H₂O → H⁺ + HCO₃⁻; pH_i falls. The fall in pH_i would stimulate NBCn1 and NHE1 except that low pH_o simultaneously inhibits these extruders and stimulates AE2 — net effect, intracellular acidosis persists. **Panel B — Time course of pH changes:** two stacked time-series. Upper panel shows pH_o falling in step from 7.40 with the onset of respiratory acidosis (phase A), then gradually rising over hours during renal compensation (phase C). Lower panel shows pH_i falling in parallel to pH_o (phase A, seconds), recovering only feebly during phase B (minutes — the cell can't beat the extracellular insult), then recovering in parallel with pH_o during phase C (hours-days). The bottom-line geometry: pH_i tracks pH_o, with ΔpH_i ≈ 0.2–0.6 × ΔpH_o.

---

## Acid-base disorder reference table (clinical synthesis)

The chapter develops the four primary disorders, their compensations, mixed patterns, and the anion gap as a single integrated bedside framework. Reproduced here for downstream clinical use:

| Disorder | Primary change | Compensatory change | Time to compensate | Davenport region | Worked compensation rule |
|---|---|---|---|---|---|
| **Acute respiratory acidosis** | ↑ P_CO₂ | ↑ [HCO₃⁻] by non-HCO₃⁻ buffering only | minutes | Point A (along non-HCO₃⁻ line) | Δ[HCO₃⁻] ≈ 1 mEq/L per 10 mm Hg ΔP_CO₂ |
| **Chronic respiratory acidosis** | ↑ P_CO₂ | ↑ [HCO₃⁻] by renal H⁺ secretion + new HCO₃⁻ generation | 3–5 days | Region between line and pH = 7.4 vertical | Δ[HCO₃⁻] ≈ 3.5–4 mEq/L per 10 mm Hg ΔP_CO₂ |
| **Acute respiratory alkalosis** | ↓ P_CO₂ | ↓ [HCO₃⁻] by non-HCO₃⁻ buffering only | minutes | Point B | Δ[HCO₃⁻] ≈ −2 mEq/L per 10 mm Hg ΔP_CO₂ |
| **Chronic respiratory alkalosis** | ↓ P_CO₂ | ↓ [HCO₃⁻] by ↓ renal H⁺ secretion | 3–5 days | Region | Δ[HCO₃⁻] ≈ −4–5 mEq/L per 10 mm Hg ΔP_CO₂ |
| **Metabolic acidosis** | ↓ [HCO₃⁻] | ↓ P_CO₂ by hyperventilation (peripheral + central chemoreceptors) | hours | Point C | **Winter's:** P_CO₂ ≈ 1.5·[HCO₃⁻] + 8 ± 2 |
| **Metabolic alkalosis** | ↑ [HCO₃⁻] | ↑ P_CO₂ by hypoventilation (limited by hypoxemia) | hours, partial only | Point D | ΔP_CO₂ ≈ 0.7 × Δ[HCO₃⁻]; rarely raises P_CO₂ > 55 |

### Clinical exemplars threaded through the chapter

- **Diabetic ketoacidosis (DKA).** Insulin deficiency → unrestrained lipolysis → hepatic ketogenesis → accumulation of β-hydroxybutyrate and acetoacetate. **High anion-gap metabolic acidosis** + dehydration + hyperglycemia. Compensatory **Kussmaul respiration** (deep, sighing hyperventilation) lowers $P_{\text{CO}_2}$. Treatment: insulin + IV fluid + K⁺ replacement (because intracellular K⁺ enters cells as acidosis corrects — see Fig. 28-12's apparent K-H story).
- **Lactic acidosis.** Shock, ischemia, severe exercise, mitochondrial poisoning (cyanide, metformin in renal failure). Anaerobic glycolysis generates lactate + H⁺ stoichiometrically. **High AG metabolic acidosis**. MCT1/4 exports lactic acid from tissue into blood.
- **Renal tubular acidosis (RTA).** Three types (Ch 39): type 1 (distal — α-intercalated cell H⁺-ATPase / band 3 defect, urine pH > 5.5, hypokalemia); type 2 (proximal — HCO₃⁻ reabsorption defect, often with Fanconi syndrome); type 4 (hyperkalemic — aldosterone deficiency or resistance). All produce a **normal AG (hyperchloremic) metabolic acidosis**.
- **Vomiting.** Loss of gastric HCl (H⁺ + Cl⁻ from parietal cells via the H/K-ATPase) → **metabolic alkalosis** with hypochloremia and (paradoxically) acidic urine ("paradoxical aciduria" because volume depletion drives Na⁺ + HCO₃⁻ reabsorption, dumping H⁺).
- **COPD / chronic respiratory failure.** Hypoventilation (mechanical limit from Ch 27 Fig. 27-18 — effort-independent expiratory flow at low V_L) → chronic ↑ $P_{\text{CO}_2}$ → chronic respiratory acidosis → renal compensation with chronically ↑ [HCO₃⁻] (often 30–35 mM). On the Davenport: a compensated state in the upper-left quadrant of Fig. 28-11B (blue region). Acute COPD exacerbation superimposes acute respiratory acidosis (further P_CO₂ rise) → moves the point further down-left along the non-HCO₃⁻ line and into the compound-disturbance region of Fig. 28-11D.
- **Aspirin (salicylate) intoxication.** Direct medullary stimulation → primary respiratory alkalosis + interference with mitochondrial oxidative phosphorylation → primary metabolic acidosis. The classic **mixed disturbance** with normal or only mildly abnormal pH but very abnormal P_CO₂ and [HCO₃⁻] — both pulled in opposite directions from the 40 mm Hg isopleth and 24 mM baseline.

---

## Glossary (downstream-chunkable)

- **pH** — $-\log_{10}[\text{H}^+]$. Sørensen (1909).
- **Brønsted acid / base** — proton donor / acceptor. "Alkali" = base.
- **Buffer** — substance that reversibly consumes or releases H⁺; conjugate weak-acid / weak-base pair.
- **Buffering power β** — moles of strong base per liter required to raise pH by 1 unit (Eq. 28-8). Mid-physiological-pH whole blood: ~25 mM/pH non-HCO₃⁻ + ~55 mM/pH open CO₂/HCO₃⁻.
- **Closed system** — buffer cannot leave/enter the solution; β bell-shaped, peaks at pH = pK (Eq. 28-18).
- **Open system** — one species (CO₂) exchanges freely with a large reservoir (atmosphere via lungs); β rises exponentially with pH (Eq. 28-20).
- **Henry's law** — $[\text{CO}_2]_{\text{dis}} = s \cdot P_{\text{CO}_2}$, s ≈ 0.03 mM/mm Hg at 37 °C.
- **Carbonic anhydrase (CA)** — accelerates CO₂ + H₂O ↔ H⁺ + HCO₃⁻; CA II in erythrocytes; CA IV apical in renal tubule; CA IX in tumors.
- **Henderson-Hasselbalch equation** — pH = pK + log([HCO₃⁻] / s·P_CO₂); pK = 6.1; ratio [HCO₃⁻]/(s·P_CO₂) = 20 at pH 7.40.
- **Whimsical H-H** — pH = constant + kidney/lungs (Eq. 28-27).
- **β_open** — 2.3·[HCO₃⁻]; ~55 mM/pH at arterial baseline.
- **β_closed** — 2.3·[H⁺]·K·[TB]/([H⁺]+K)²; peak at pK; ~2.6 mM/pH for CO₂/HCO₃⁻ at pH 7.4 closed.
- **β_non-HCO₃⁻** — ~25 mM/pH in whole blood; ~5 mM/pH in plasma; tracks Hb concentration.
- **Davenport diagram** — pH (x) vs [HCO₃⁻] (y) with exponential CO₂ isopleths.
- **CO₂ isopleth (isobar)** — locus of (pH, [HCO₃⁻]) at constant P_CO₂; rises exponentially with pH; slope at any pH = β_open.
- **Non-HCO₃⁻ titration line** — locus of (pH, [HCO₃⁻]) accessible by respiratory disturbance alone; negative slope of magnitude β_non-HCO₃⁻.
- **Respiratory acidosis** — ↑ P_CO₂ → ↓ pH; clinical: hypoventilation (COPD, drug OD, neuromuscular).
- **Respiratory alkalosis** — ↓ P_CO₂ → ↑ pH; clinical: hypoxia, anxiety, salicylates, sepsis.
- **Metabolic acidosis** — ↓ [HCO₃⁻] → ↓ pH; clinical: DKA, lactic acidosis, RTA, diarrhea, renal failure.
- **Metabolic alkalosis** — ↑ [HCO₃⁻] → ↑ pH; clinical: vomiting/NG suction, diuretics, NaHCO₃ load, hyperaldosteronism.
- **Acute vs chronic** — non-HCO₃⁻ buffering only (minutes) vs full renal/respiratory compensation (3–5 days).
- **Anion gap (AG)** — [Na⁺] − ([Cl⁻] + [HCO₃⁻]) ≈ 8–12 mEq/L.
- **High-AG metabolic acidosis** — MUDPILES.
- **Normal-AG (hyperchloremic) metabolic acidosis** — diarrhea, RTA, acetazolamide.
- **Winter's formula** — expected P_CO₂ in metabolic acidosis = 1.5·[HCO₃⁻] + 8 ± 2 mm Hg.
- **Isohydric hypercapnia / hypocapnia** — perfect compensation; normal pH at abnormal P_CO₂ (Eq. 28-31).
- **Compound disturbance** — both metabolic and respiratory derangement in same direction; off both the non-HCO₃⁻ line and the 40 mm Hg isopleth.
- **Strong-ion difference (SID; Stewart)** — [Na⁺] + [K⁺] + [Ca²⁺] + [Mg²⁺] − [Cl⁻]; alternative framework Boron critiques (Box 28-1).
- **NHE1 (SLC9A1)** — ubiquitous electroneutral Na⁺/H⁺ exchanger; prototypical acid extruder.
- **NBCn1 (SLC4A7)** — electroneutral Na⁺/HCO₃⁻ cotransporter; acid extruder.
- **NBCe1 (SLC4A4)** — electrogenic Na⁺/HCO₃⁻ cotransporter (1:2 or 1:3); basolateral acid extruder in PCT (Ch 39), acid extruder elsewhere.
- **AE2 (SLC4A2)** — electroneutral Cl⁻/HCO₃⁻ exchanger; prototypical chronic acid loader.
- **AE1 (SLC4A1; band 3)** — erythrocyte Cl⁻/HCO₃⁻ exchanger; the "chloride shift" of Ch 29.
- **MCT1–4 (SLC16A)** — H⁺-coupled monocarboxylate (lactate, pyruvate, ketones) transporters.
- **H/K-ATPase** — gastric parietal cell (Ch 42); only true K-H exchanger in mammals.
- **V-type H⁺-ATPase** — vesicular and α-intercalated cell apical (Ch 39); osteoclasts.
- **Cellular pH sensors** — NHE1 C-terminal tail (intracellular); GPR4/GPR65/GPR68 (extracellular); ASICs (rapid extracellular transients).
- **pH_i recovery** — push-pull regulation: low pH_i → ↑ extruder, ↓ loader; high pH_i → reverse.
- **Depolarization-induced alkalinization** — apparent K-H exchange in fact mediated by electrogenic NBC flipping with membrane voltage.
- **Three phases of intracellular response to respiratory acidosis (Fig. 28-13)** — A: rapid CO₂ entry (s); B: feeble extruder recovery (min); C: renal pH_o correction releases extruders (h–d).

---

## Cross-links forward

| Forward link | Topic | Where |
|---|---|---|
| Plasma CO₂ regulation by alveolar ventilation | sets the denominator of H-H | Ch 31 (alveolar ventilation, V̇/Q̇), Ch 32 (chemoreceptors) |
| Plasma HCO₃⁻ regulation by the kidneys | sets the numerator of H-H | Ch 39 (transport of acids and bases) |
| Carbonic anhydrase isoforms (CA I, II, IV, IX, XII, XIV) | accelerate the CO₂/HCO₃⁻ chain in different cells | Ch 18 (RBC), Ch 29 (chloride shift), Ch 39 (renal tubule) |
| Hemoglobin imidazole buffering + Haldane effect | the cellular substrate for whole-blood $\beta_{\text{non-HCO}_3^-}$ | Ch 29 |
| Peripheral and central chemoreceptors | sense pH and P_CO₂; drive respiratory compensation | Ch 32 (control of ventilation) |
| Renal tubular acidosis (RTA) types 1, 2, 4 | distal H⁺-ATPase, proximal HCO₃⁻ reabsorption, aldosterone deficiency | Ch 39 |
| K⁺ / H⁺ interaction; aldosterone | apparent K-H exchange in the distal nephron | Ch 35, 37, 50 |
| Diabetic ketoacidosis (DKA) | the canonical high-AG metabolic acidosis | Ch 51 (endocrine pancreas), Ch 58 (metabolism) |
| Lactic acidosis | anaerobic glycolysis, shock, hypoxia, MCT-mediated lactate efflux | Ch 24 (special circulations), Ch 58, Ch 60 (exercise) |
| Gastric acid secretion (H/K-ATPase, vomiting → metabolic alkalosis) | the parietal-cell mechanism | Ch 42 (gastric function) |
| Pulmonary edema and ARDS | hypoxemic respiratory failure → mixed respiratory acidosis | Ch 30, Ch 27 (Box 27-1) |
| COPD and chronic respiratory acidosis | the mechanical link from Ch 27 | Ch 27 (Box 27-2), Ch 31, Ch 32 |
| Aspirin (salicylate) intoxication | mixed respiratory alkalosis + metabolic acidosis | Ch 32 |
| Altitude acclimatization | respiratory alkalosis from hypoxic hyperventilation; renal HCO₃⁻ excretion | Ch 32, Ch 61 (environmental) |
| Bone as a long-term H⁺ buffer | carbonate dissolution under chronic acidosis | Ch 52 (parathyroid / Vitamin D) |
| CSF pH and the brain's protected acid-base environment | central chemoreceptor substrate | Ch 11, Ch 32 |

## Source apparatus

- **Online Notes** N28-1 through N28-10 referenced inline (Brønsted definitions, pH-scale history, alternative buffer reactions, slow CO₂ hydration, derivation of $\beta_{\text{closed}}$, derivation of $\beta_{\text{open}}$, vomiting / metabolic alkalosis, nine-buffer construction of Fig. 28-2B, addition of OH⁻ ≡ removal of H⁺ for metabolic compensation, push-pull pH_i feedback).
- **Box 28-1** — Strong Ion Difference (Stewart) and its critique.
- **References** deferred to the companion site.

---

## Format-verification notes

**Figures viewed and described from image:** 28-6 (four-panel construction of the Davenport diagram), 28-7 (metabolic acidosis/alkalosis with non-HCO₃⁻ buffers), 28-9 (metabolic compensation to primary respiratory disturbances), 28-11 (the four Davenport regions: uncompensated / partially compensated / perfectly compensated / compound), 28-12 (intracellular pH regulation by NBCn1 + NHE1 + AE2 with carbonic anhydrase II).

**Figures listed by caption + text reference only:** 28-1 (interaction of CO₂ with water), 28-2 (closed-system buffering power, single + nine-buffer), 28-3 (open-system buffering of strong acids and bases), 28-4 (β_open vs β_closed vs pH), 28-5 (doubling of CO₂ or HCO₃⁻ in pure CO₂/HCO₃⁻ solution), 28-8 (effect of β_non-HCO₃⁻ on metabolic-alkalosis ΔpH), 28-10 (respiratory compensation to primary metabolic disturbances), 28-13 (three-phase intracellular response to extracellular respiratory acidosis). Full inventory: 13 figures total.

**Equations verified:** 28-1 (pH = −log[H⁺]); 28-2 (HB^(n+1) ⇌ B^n + H⁺); 28-3 ([TB] = [HB^(n+1)] + [B^n]); 28-5 (K = [H⁺][B^n]/[HB^(n+1)]); 28-8 (β = Δ[strong base]/ΔpH); 28-9 (Henry's law); 28-10 ([CO₂]_dis = 1.2 mM at P_CO₂ 40 mm Hg); 28-11 / 28-12 / 28-13 (hydration / dissociation chain); 28-14 (K equilibrium constant for collapsed reaction); 28-15 / 28-16 (Henderson-Hasselbalch); 28-17 (worked H-H = 7.40); 28-18 (β_closed); 28-19 (worked Δ[H⁺] = 28 nM for 10 mM HCl into open system); 28-20 (β_open = 2.3·[HCO₃⁻]); 28-21 / 28-22 / 28-23 (worked respiratory acidosis pH 7.10); 28-24 / 28-25 / 28-26 (worked metabolic alkalosis pH 7.70); 28-27 (whimsical "kidney/lungs"); 28-28 (non-HCO₃⁻ + CO₂/HCO₃⁻ competing equilibria); 28-29 (CO₂ isopleth equation); 28-30 (worked CO₂ → HCO₃⁻ + H⁺ flux of 5.25 mM); 28-31 (isohydric hypercapnia at doubled P_CO₂ with doubled [HCO₃⁻]). Clinical equations not numbered in source: anion gap; Winter's formula; chronic-acidosis renal compensation rules; Stewart SID (Box 28-1).

*End of Chapter 28. Next: Chapter 29 — Transport of Oxygen and Carbon Dioxide in the Blood (Boron), p. 647.*
