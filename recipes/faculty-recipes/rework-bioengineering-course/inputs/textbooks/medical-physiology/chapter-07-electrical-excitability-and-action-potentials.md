---
chapter: 7
title: Electrical Excitability and Action Potentials
authors:
  - Edward G. Moczydlowski
section: "II. Physiology of Cells and Molecules"
source_pages: "173–203"
pdf_pages: "185–215"
source_book: "Boron WF, Boulpaep EL. Medical Physiology, 3rd edition (2017)"
figures_listed: "≈18"
figures_described_from_image: 5
equations: "many — Hodgkin–Huxley, cable, length and time constants, channelopathy"
tables: 3
clinical_boxes: "≥2 (Na⁺ channel disorders; local anesthetics; Ca²⁺ channelopathies)"
---

# Chapter 7 — Electrical Excitability and Action Potentials

> Section II · Physiology of Cells and Molecules · pp. 173–203 · Author: Edward G. Moczydlowski

## Chapter map (top-level)

1. **Excitable cells and the all-or-none action potential** (pp. 173–177) — threshold, refractoriness, strength–duration, excitable vs. nonexcitable cells.
2. **Ionic basis of the action potential — the Hodgkin–Huxley model** (pp. 177–185) — voltage-clamp dissection of $I_{Na}$ and $I_K$; the $m$, $h$, $n$ gating particles; reconstruction of the AP.
3. **Voltage-gated Na⁺ channels** (pp. 185–190) — $\alpha$-subunit structure, gating, inactivation; pharmacology and toxinology; sodium-channel diseases.
4. **Voltage-gated Ca²⁺ channels** (pp. 190–195) — L/N/P/Q/R/T classification, $\alpha_1$ structure, accessory subunits; calcium-channel diseases.
5. **Voltage-gated K⁺ channels** (pp. 195–199) — Kv/Kir/K2P families; structural diversity, gating modes, hERG and long-QT.
6. **Other voltage-gated and special channels** (pp. 199–201) — HCN, TRP, ASIC; pacemaker currents.
7. **Propagation: cable properties and conduction velocity** (pp. 201–203) — length constant, time constant, myelination, saltatory conduction.

---

## Section 1 — Excitable cells and the action potential (pp. 173–177)

### Subsection headings
- **An action potential is a rapid, all-or-none change in membrane potential, followed by a return to the resting potential** (pp. 173–174)
- **Excitability requires both a stimulus of sufficient strength and duration: the strength–duration relationship** (pp. 174–175)
- **Refractoriness: absolute and relative refractory periods** (pp. 175–176)
- **The action potential arises from changes in membrane conductance to Na⁺ and K⁺** (p. 176)

### Core claims
- **All-or-none**: a stimulus that depolarizes $V_m$ past the **threshold** triggers a stereotyped, large, transient depolarization (peak typically +30 to +50 mV) followed by repolarization back to $V_m$ rest. Subthreshold stimuli decay passively without triggering anything.
- **Strength–duration relationship (Fig. 7-3A)**: shorter stimuli require stronger current; the **rheobase** is the minimum current that depolarizes to threshold for an infinitely long stimulus; the **chronaxie** is the duration required for a stimulus of twice rheobase to reach threshold.
- **Refractoriness (Fig. 7-3B)**:
  - **Absolute refractory period (ARP)** — no second AP can be elicited regardless of stimulus strength. Set by inactivation of Na⁺ channels.
  - **Relative refractory period (RRP)** — a stronger-than-normal stimulus can elicit a second AP. Set by partial recovery of Na⁺ inactivation plus continued K⁺ outflux (raised threshold).
- **Excitable cells**: neurons, skeletal/cardiac/smooth muscle, some secretory cells (β-cell, neuroendocrine cells), some immune cells.

### Citation-anchor quotes
- > "An action potential is a rapid, all-or-none change in membrane potential, followed by a return to the resting potential." (p. 173)
- > "Excitation of a nerve or muscle depends on the product (strength × duration) of the stimulus and on the refractory period." (p. 175)
- > "The action potential arises from changes in membrane conductance to Na⁺ and K⁺." (p. 176)
- > "Once threshold is reached, further activation of voltage-gated channels is no longer required to drive the membrane to the peak of the action potential." (p. 175)
- > "Long after the absolute refractory period — the interval during which no stimulus can produce a second action potential, however large — the cell enters a relative refractory period in which a stronger-than-normal stimulus is required." (p. 175)

### Figures

#### Figure 7-3 — Determinants of excitability *(viewed)*

- **Panel A — Strength–duration curve.** Stimulus intensity (y-axis) plotted against stimulus duration (x-axis). The curve is asymptotic: below the **rheobase** intensity, no duration produces an AP; for any intensity above rheobase the required duration drops, approaching very small values as intensity grows. Annotations mark "If the duration of the stimulus is short, the intensity must be high" and "If the duration of the stimulus is long, a lower intensity is enough to elicit an action potential."
- **Panel B — Refractory periods.** Voltage trace at top shows an action potential. Below, the **absolute refractory period** (ARP) is shaded immediately following the upstroke — a second AP cannot be elicited. Trailing it is the **relative refractory period** (RRP) during which a larger-than-normal stimulus can elicit a second, smaller AP.

> Vision note: This is the textbook's compact summary of clinical excitability concepts (cardiac vulnerable period; neuronal high-frequency firing limit).

---

## Section 2 — Ionic basis of the action potential: Hodgkin–Huxley (pp. 177–185)

### Subsection headings
- **Voltage-clamp dissection of squid-axon currents reveals an inward $I_{Na}$ followed by a delayed outward $I_K$** (pp. 177–179)
- **The Na⁺ current activates and inactivates; the K⁺ current activates without significant inactivation** (pp. 179–181)
- **Hodgkin and Huxley described the kinetics with three gating particles: $m$, $h$, and $n$** (pp. 181–183)
- **The Hodgkin–Huxley model reconstructs the action potential from the four state variables $V$, $m$, $h$, $n$** (pp. 183–185)

### The Hodgkin–Huxley equations (compact reference)

For the squid giant axon at ~6.3 °C with passive leak conductance $g_L$:

$$C_m \frac{dV}{dt} = -\big[\, g_{Na}\,m^3 h\,(V - E_{Na}) + g_K\,n^4\,(V - E_K) + g_L\,(V - E_L)\,\big] + I_{\text{ext}}$$

with three gating particles obeying first-order kinetics:

$$\frac{dm}{dt} = \alpha_m(V)\,(1 - m) - \beta_m(V)\,m$$

$$\frac{dh}{dt} = \alpha_h(V)\,(1 - h) - \beta_h(V)\,h$$

$$\frac{dn}{dt} = \alpha_n(V)\,(1 - n) - \beta_n(V)\,n$$

Interpretation:

- $m$ — Na⁺ activation gate (3 particles, fast, voltage-dependent; $m_\infty(V)$ shifts to ~1 at depolarized $V$).
- $h$ — Na⁺ inactivation gate (1 particle, slower, voltage-dependent; $h_\infty(V)$ shifts to ~0 at depolarized $V$).
- $n$ — K⁺ activation gate (4 particles, slow; $n_\infty(V)$ shifts to ~1 at depolarized $V$; no inactivation in HH).

Voltage-dependent rate constants $\alpha_X(V)$ and $\beta_X(V)$ are empirical fits derived from voltage-clamp data.

Steady-state values and time constants of each gate (e.g., $m_\infty$, $\tau_m$) are typically plotted vs. $V$ (Fig. 7-8).

### Phases of a propagated action potential (worked picture)

| Phase | Mechanism | $V_m$ | Conductance changes |
|---|---|---|---|
| Rest | leak + small $g_K$ | ≈ $E_K$ | $g_K$ low but dominant |
| Threshold | depolarization recruits $g_{Na}$ ($m^3h$) | ≈ −55 mV | $g_{Na}$ begins to rise |
| Upstroke | regenerative $g_{Na}$ feedback (depolarization → more $m$ → more depolarization) | rapid rise toward $E_{Na}$ | $g_{Na} \gg g_K$ |
| Peak | nearing $E_{Na}$ | ≈ +30–+50 mV | $g_{Na}$ near max |
| Repolarization | $h$ inactivates Na⁺ channels; $n^4$ activation opens delayed-rectifier K⁺ | rapid fall | $g_{Na}\downarrow$, $g_K\uparrow$ |
| After-hyperpolarization | $g_K$ still elevated; pulls $V_m$ toward $E_K$ below rest | brief | $g_K$ slowly relaxes |
| Recovery | $h$ deinactivates; $n$ closes; resting state restored | → rest | back to baseline |

### Citation-anchor quotes
- > "Macroscopic Na⁺ and K⁺ currents result from the opening and closing of many channels." (p. 180)
- > "Macroscopic K⁺ currents activate and then remain at a steady-state value as long as the membrane is depolarized." (p. 180)
- > "Hodgkin and Huxley described the changes in g_Na and g_K with empirical equations using three voltage-dependent gating variables." (p. 181)
- > "The Na⁺ current is described by m³h, where m is the activation gate and h is the inactivation gate." (p. 182)
- > "The K⁺ current is described by n⁴, where n is the activation gate of the delayed rectifier." (p. 182)
- > "The reconstructed action potential closely matches the experimentally measured action potential." (p. 184)
- > "Once activated, Na⁺ channels inactivate spontaneously even when V_m remains depolarized." (p. 180)

### Figures

#### Figure 7-7 — Microscopic basis of macroscopic I–V relationships *(viewed)*

- **Panel A — Single-channel I–V.** A linear plot of single-channel Na⁺ current $i_{Na} = \gamma_{Na}(V - E_{Na})$ vs. $V$. The line crosses zero at the reversal potential $E_{Na} = +67\,\text{mV}$. The negative slope at very negative $V$ shows the channel passing inward current when open.
- **Panel B — Voltage dependence of single-channel open probability.** A sigmoid (Boltzmann) $P_o(V)$ rising from ~0 at hyperpolarized $V$ to ~1 at +30 mV. Two-state cartoon (closed ⇌ open) at right shows that opening probability scales with depolarization.
- **Panel C — Reconstructed macroscopic I–V.** Product of A and B (and scaled by $N$, the number of channels) gives a peaked $I(V)$ curve: inward current grows as depolarization opens more channels, then declines as $V \to E_{Na}$ where driving force vanishes; reverses sign and becomes outward beyond $E_{Na}$. Annotations point out that this peaked shape (the "N-shape" of the macroscopic Na⁺ I–V) is what HH measured by voltage clamp.

> Vision note: This is one of the textbook's clearest didactic figures — it derives the macroscopic peaked current from single-channel kinetics in three steps. Anchor for the Hodgkin–Huxley dissection.

#### Figure 7-8 — Voltage-dependent parameters of the HH model *(listed)*

Plots of $m_\infty$, $h_\infty$, $n_\infty$ as steady-state Boltzmann curves vs. $V$, and the corresponding time constants $\tau_m$, $\tau_h$, $\tau_n$ as bell-shaped functions of $V$. $\tau_m$ is shortest (fastest activation), $\tau_h$ intermediate (inactivation), $\tau_n$ longest (delayed-rectifier activation).

#### Figure 7-9 — Reconstructed action potential *(listed)*

Top panel: HH-reconstructed $V_m(t)$ — upstroke, peak near $E_{Na}$, repolarization, brief after-hyperpolarization. Lower panel: corresponding $g_{Na}(t)$ (large transient) and $g_K(t)$ (slower rise, slower decay). Demonstrates that the model reconstructs the squid AP from independently measured kinetic parameters — the original Hodgkin–Huxley achievement.

---

## Section 3 — Voltage-gated Na⁺ channels (pp. 185–190)

### Subsection headings
- **Voltage-gated Na⁺ channels are large α subunits with auxiliary β subunits** (pp. 185–187)
- **The α subunit contains four homologous repeats (DI–DIV) each with six TM segments (S1–S6)** (pp. 186–187)
- **Inactivation is fast and uses the cytoplasmic linker between repeats III and IV** (pp. 187–188)
- **Pharmacology: TTX, STX, local anesthetics, antiarrhythmics, anticonvulsants, scorpion toxins** (pp. 188–190)
- **Sodium-channel diseases: SCN5A in cardiac syndromes, SCN4A in skeletal myotonia / periodic paralysis, SCN1A in epilepsy and migraine** (Box 7-1)

### Core claims
- **Topology (Fig. 7-10):** single α-subunit polypeptide with **four homologous repeats** (DI–DIV). Each repeat has six transmembrane segments (S1–S6). S4 in each repeat carries positively charged residues and acts as the voltage sensor. The four S5–P-loop–S6 motifs converge on a single central pore lined by the DEKA selectivity ring (one residue from each of the four DI–DIV repeats; DEKA is the residue signature that gives the channel its Na⁺ selectivity).
- **Fast inactivation**: a hydrophobic motif (`IFM`) on the cytoplasmic linker between DIII and DIV acts as a hinged lid; depolarization-triggered conformational change docks the IFM lid into the cytoplasmic pore mouth → fast closure independent of channel opening.
- **β subunits**: single-TM proteins (β1, β2, β3, β4) modulating gating, surface expression, and channel localization.
- **Toxin / drug map:**
  - **TTX / STX** — pore-mouth blockers from extracellular side (outer vestibule).
  - **Scorpion α toxins** — slow inactivation by binding S3–S4 of DIV.
  - **Scorpion β toxins** — shift activation by binding DII voltage sensor.
  - **Sea anemone toxins** — similar.
  - **Local anesthetics (lidocaine, procaine, bupivacaine, tetracaine, cocaine; Fig. 7-14A)** — bind cytoplasmic pore vestibule; preferential affinity for the inactivated state → use-dependent block (Fig. 7-14B).
  - **Class I antiarrhythmics** — same pharmacophore as local anesthetics; subclasses IA/IB/IC differ in dissociation rate and clinical use.
  - **Anticonvulsants** (phenytoin, carbamazepine, lamotrigine) — slow recovery of Na⁺ channels from inactivation → suppress rapidly firing neurons.
- **Sodium-channel genetic disorders (Box 7-1):**

| Gene | Disease | Mechanism |
|---|---|---|
| *SCN4A* (skeletal Nav1.4) | hyperkalemic periodic paralysis (HyperPP), paramyotonia congenita, normokalemic PP | gain-of-function: impaired inactivation → persistent inward Na⁺ → membrane depolarization → inactivation of remaining channels → weakness |
| *SCN5A* (cardiac Nav1.5) | long QT type 3, Brugada syndrome, conduction disease, atrial fibrillation | gain-of-function (LQT3) vs. loss-of-function (Brugada/conduction) |
| *SCN1A* (Nav1.1) | Dravet syndrome (severe myoclonic epilepsy of infancy), GEFS+, familial hemiplegic migraine | loss-of-function in interneurons → disinhibition |
| *SCN1B* | GEFS+ | β1-subunit modulation deficit |

### Citation-anchor quotes
- > "Voltage-gated Na⁺ channels are integral membrane proteins that consist of a large α subunit and two smaller β subunits." (p. 185)
- > "The α subunit contains four homologous repeats, each with six transmembrane segments (S1–S6)." (p. 186)
- > "Inactivation is fast and is mediated by the intracellular linker between domains III and IV." (p. 187)
- > "Local anesthetics block voltage-gated Na⁺ channels in a use-dependent fashion." (p. 188)
- > "TTX and saxitoxin block Na⁺ channels from the extracellular side." (p. 188)
- > "Mutations in SCN5A cause long QT syndrome type 3 and Brugada syndrome." (p. 190)

### Figures

#### Figure 7-10 — Voltage-gated K⁺ channel topology (Shaker; Numa & MacKinnon) *(viewed)*

Two-panel diagram describing the structural genealogy of voltage-gated cation channels.

- **Panel A — Hydropathy plot** of the Shaker K⁺ channel: hydropathy index along the residue number, with six clear hydrophobic peaks labeled S1–S6 and a hydrophilic "pore region" between S5 and S6.
- **Panel B — Membrane topology model.** A single Shaker α subunit drawn in the bilayer with six TM segments (S1–S6 as labeled cylinders), the voltage-sensor domain comprising S1–S4 (S4 highlighted in red as the positively charged voltage sensor), and the pore region (the P-loop between S5 and S6) drawn re-entrant from the extracellular side carrying the K⁺ selectivity filter. Four such subunits assemble to form a functional Kv channel. Caption explicitly draws the parallel to Na⁺ and Ca²⁺ channels, where the four repeats DI–DIV (joined into a single polypeptide) have the same S1–S6 architecture.

> Vision note: Together with the Section-1 historical figure, this is the chapter's structural keystone. Anchor for any forward query about voltage-sensor pharmacology, β-subunit modulation, or channelopathy locus assignment.

#### Figure 7-13 — Effect of extracellular Ca²⁺ on Na⁺-channel gating *(listed)*

Plot of $m_\infty(V)$ curves at three different $[\mathrm{Ca^{2+}}]_o$ values. Raising $[\mathrm{Ca^{2+}}]_o$ shifts the activation curve to more depolarized voltages → hypocalcemia lowers threshold → spontaneous AP firing → tetany. The clinical anchor for the Trousseau and Chvostek signs.

#### Figure 7-14 — Local anesthetics and use-dependent block *(viewed)*

- **Panel A — Structures of cocaine, tetracaine, lidocaine, procaine.** All share a tertiary amine, an aromatic ring, and an intermediate ester or amide linker. Esters (procaine, tetracaine, cocaine) are short-acting; amides (lidocaine, bupivacaine) are longer-acting.
- **Panel B — Use-dependence of block by lidocaine.** Relative Na⁺ current plotted against pulse number for stimulation at different frequencies (1, 2, 5, 10 Hz). At low frequency, block develops slowly; at higher frequency, block develops rapidly to a deeper steady-state level. Demonstrates that lidocaine accumulates in channels that frequently visit the inactivated state — clinical anchor for why local anesthetics preferentially silence rapidly firing pain fibers and reentrant cardiac circuits while sparing slowly firing fibers.

> Vision note: This figure is the clinical cornerstone for the entire local anesthetic / antiarrhythmic drug class. Use as RAG anchor for those queries.

---

## Section 4 — Voltage-gated Ca²⁺ channels (pp. 190–195)

### Subsection headings
- **Voltage-gated Ca²⁺ channels are classified by activation threshold, pharmacology, and tissue distribution** (pp. 190–192)
- **The α₁ pore-forming subunit shares the four-repeat architecture of Nav channels** (pp. 192–193)
- **Accessory subunits (β, α₂δ, γ) modulate gating** (pp. 193–194)
- **Calcium-channel diseases and pharmacology** (pp. 194–195)

### Core claims — Table 7-2 territory: Ca²⁺ channel classification

| Type | $\alpha_1$ | Activation | Inactivation | Distribution | Pharmacology |
|---|---|---|---|---|---|
| **L** (high-voltage) | Cav1.1–1.4 | high threshold | slow, Ca²⁺-dependent | skeletal/cardiac/smooth muscle, endocrine, retina | DHP (nifedipine), verapamil, diltiazem |
| **N** | Cav2.2 | high | moderate | presynaptic neurons | ω-conotoxin GVIA |
| **P/Q** | Cav2.1 | high | slow | cerebellar Purkinje, presynaptic neurons | ω-agatoxin IVA |
| **R** | Cav2.3 | intermediate | moderate | cerebellar granule, neuroendocrine | SNX-482 |
| **T** (low-voltage) | Cav3.1–3.3 | low threshold | fast, voltage-dependent | thalamic relay neurons, sinoatrial node, smooth muscle | mibefradil, ethosuximide (weak) |

### Core claims — physiological roles
- **Excitation-contraction coupling** in skeletal muscle (Cav1.1 / DHPR) and cardiac muscle (Cav1.2; gates RyR2 via Ca²⁺-induced Ca²⁺ release).
- **Presynaptic Ca²⁺ entry** for neurotransmitter release: N, P/Q, R types — coupled to SNARE machinery and synaptotagmin.
- **Thalamic burst firing** (sleep, absence epilepsy) — T-type channels deinactivate at hyperpolarized $V_m$ and produce low-threshold Ca²⁺ spikes.
- **Sinoatrial pacemaking** — T- and L-type channels participate in pacemaker depolarization.

### Calcium-channel diseases (clinical anchors)
- **Hypokalemic periodic paralysis** — *CACNA1S* (Cav1.1) — loss of skeletal muscle excitability.
- **Malignant hyperthermia** — *CACNA1S* and *RYR1* — defective EC-coupling Ca²⁺ release / inactivation.
- **Familial hemiplegic migraine type 1** — *CACNA1A* (Cav2.1) gain-of-function.
- **Episodic ataxia type 2** — *CACNA1A* loss-of-function.
- **Spinocerebellar ataxia type 6** — *CACNA1A* polyglutamine expansion.
- **Lambert–Eaton myasthenic syndrome** — autoantibodies against presynaptic Cav2.1 → reduced ACh release at NMJ.
- **Timothy syndrome** — *CACNA1C* (Cav1.2) gain-of-function — long QT, syndactyly, autism.

### Citation-anchor quotes
- > "Voltage-gated Ca²⁺ channels are classified by their activation voltage, kinetics, and pharmacology." (p. 190)
- > "L-type Ca²⁺ channels are activated at high voltages and inactivate slowly." (p. 191)
- > "Low-threshold T-type Ca²⁺ channels contribute to the pacemaker activity of the sinoatrial node and to thalamic burst firing." (p. 191)
- > "Dihydropyridines, verapamil, and diltiazem block L-type Ca²⁺ channels." (p. 192)

---

## Section 5 — Voltage-gated K⁺ channels (pp. 195–199)

### Subsection headings
- **The K⁺ channel family is the largest and most diverse in the genome** (pp. 195–196)
- **K⁺ channels fall into three structural classes: 6TM Kv, 2TM Kir, and 4TM K2P** (pp. 196–197)
- **Inactivation mechanisms: N-type ball-and-chain and C-type slow inactivation** (pp. 197–198)
- **hERG (Kv11.1) is the substrate of acquired and congenital long-QT syndrome** (pp. 198–199)

### Core claims
- **Three K⁺-channel structural classes:**
  - **6TM Kv family** — voltage-gated, S1–S4 voltage sensor + S5–P–S6 pore. Tetrameric. Includes Kv1 (Shaker, delayed rectifier), Kv2 (delayed rectifier), Kv3 (fast), Kv4 (A-type), Kv7/KCNQ (M-current, cardiac $I_{Ks}$), Kv10–Kv12 (hERG family — cardiac $I_{Kr}$).
  - **2TM Kir family** — inward rectifier; one TM + P-loop + one TM per subunit, tetrameric. Includes Kir2 (cardiac $I_{K1}$), Kir3/GIRK (G-protein-gated), Kir6 (KATP, closed by ATP, opened by ADP; sulfonylurea target for diabetes pharmacology).
  - **4TM K2P family** — two pore domains per subunit, dimeric. Background "leak" K⁺ currents (TWIK, TREK, TASK families); modulated by anesthetics, mechanical stretch, pH, and lipids.
- **Inactivation modes:**
  - **N-type ("ball-and-chain")** — cytoplasmic N-terminus of the β subunit (or of an α-subunit splice variant) dangles into the cytoplasm and physically plugs the open channel pore.
  - **C-type ("slow")** — a slower conformational collapse of the external selectivity filter region.
- **Cardiac K⁺ currents** (preview of Ch 21):
  - $I_{K1}$ (Kir2.1, KCNJ2) — sets resting potential.
  - $I_{to}$ (Kv4.3) — early repolarization "notch."
  - $I_{Kr}$ (hERG / KCNH2) — rapid delayed rectifier; **drug-induced and congenital long-QT** target.
  - $I_{Ks}$ (KCNQ1+KCNE1) — slow delayed rectifier; **LQT1** locus.
- **Pharmacology and channelopathies:**
  - **TEA** — generic Kv pore blocker.
  - **4-Aminopyridine (4-AP)** — Kv1 blocker; used in multiple sclerosis (dalfampridine) to slow conduction in demyelinated axons.
  - **hERG block** — many drugs (terfenadine, cisapride, some antibiotics, antipsychotics) cause acquired long-QT and torsades de pointes; FDA hERG screen is now mandatory.
  - **Congenital long-QT types** — LQT1 (KCNQ1), LQT2 (hERG/KCNH2), LQT5 (KCNE1), LQT6 (KCNE2), LQT7/Andersen-Tawil (KCNJ2).
  - **Bartter type 2** — KCNJ1 (ROMK) loss-of-function — see Ch 35.
  - **Episodic ataxia type 1** — KCNA1 (Kv1.1) — see Ch 12.

### Citation-anchor quotes
- > "The K⁺ channel family is the largest and most diverse family of ion channels." (p. 195)
- > "Inwardly rectifying K⁺ channels (Kir) lack the voltage-sensor S4 segment." (p. 196)
- > "hERG K⁺ channels are responsible for the rapid delayed rectifier current I_Kr that is critical for cardiac repolarization." (p. 198)
- > "Both genetic and drug-induced reductions in I_Kr can cause long QT syndrome." (p. 198)

---

## Section 6 — HCN, TRP, ASIC, and special channels (pp. 199–201)

### Core claims
- **HCN (hyperpolarization-activated, cyclic-nucleotide-gated) channels** carry the **pacemaker $I_f$** ("funny" current) in cardiac sinoatrial node and **$I_h$** in thalamic neurons. Activated by hyperpolarization (opposite of Kv/Nav); modulated by cAMP (sympathetic acceleration of heart rate via β-adrenergic → cAMP → $I_f$). Ivabradine is a clinical $I_f$ blocker.
- **TRP (transient receptor potential) channels**: ~28-gene family; mostly nonselective cation channels with 6TM topology. Subfamilies (TRPV, TRPM, TRPA, TRPC, TRPP, TRPML) cover sensory transduction (heat, cold, capsaicin via TRPV1; menthol via TRPM8; mustard oil/AITC via TRPA1), Mg²⁺ homeostasis (TRPM6/7), and polycystic kidney disease (TRPP/PKD2). Detailed in Ch 15.
- **ASIC (acid-sensing ion channels)**: ENaC/DEG family; cation channels gated by protons; nociception and CNS modulation.

---

## Section 7 — Propagation: cable properties (pp. 201–203)

### Subsection headings
- **Passive cable properties determine how voltage spreads along an axon** (pp. 201–202)
- **Active propagation: the action potential regenerates itself along the axon** (p. 202)
- **Myelination and saltatory conduction increase conduction velocity** (pp. 202–203)

### Equations

For a long cylindrical axon (one-dimensional cable):

- **Cable equation** with intracellular resistance $r_i$ (Ω/cm), membrane resistance $r_m$ (Ω·cm), and membrane capacitance $c_m$ (F/cm):

  $$\lambda^2 \frac{\partial^2 V}{\partial x^2} - \tau_m \frac{\partial V}{\partial t} - V = 0$$

- **Length constant** (passive decay distance of a steady-state subthreshold depolarization):

  $$\lambda = \sqrt{\dfrac{r_m}{r_i + r_o}} \approx \sqrt{\dfrac{r_m}{r_i}}$$

  $V(x) = V_0 e^{-x/\lambda}$ at steady state. Large axon diameter $\to$ low $r_i$ $\to$ longer $\lambda$ $\to$ faster passive spread.

- **Time constant**: $\tau_m = r_m c_m$ (developed in Ch 6).

- **Conduction velocity** scales with $\sqrt{d}$ for unmyelinated axons (Hodgkin); the squid giant axon is huge precisely because invertebrates lack myelin. Myelin reduces $c_m$ and raises $r_m$ in the myelinated segments, increasing $\lambda$ and decreasing the time spent recharging — so the AP "jumps" from one node of Ranvier (where Na⁺ channels cluster densely) to the next.

### Core claims
- **Saltatory conduction** in myelinated axons:
  - Internodal segments: high $r_m$, low $c_m$ — voltage spreads passively with little decay.
  - Nodes: high density of voltage-gated Na⁺ channels — local active regeneration of the AP.
  - Net effect: 10–100× higher conduction velocity than equivalent-diameter unmyelinated axons, at a fraction of the metabolic cost.
- **Demyelinating diseases** (multiple sclerosis, Guillain–Barré) destroy this organization → slowed or blocked conduction, ectopic firing, and ephaptic crosstalk.

### Citation-anchor quotes
- > "Passive cable properties of an axon determine how a subthreshold voltage signal spreads from its origin." (p. 201)
- > "Active propagation: the action potential regenerates itself by sequentially activating voltage-gated Na⁺ channels along the axon." (p. 202)
- > "In myelinated axons, action potentials are generated only at the nodes of Ranvier, where the density of Na⁺ channels is high." (p. 202)
- > "Saltatory conduction is fast because the depolarization spreads passively along the internode with only minimal decay." (p. 202)

### Figures

#### Figure 7-15 — Passive voltage decay along an axon *(listed)*

Subthreshold current injection at one point of an axon; voltage profile at successive distances decays exponentially with characteristic length $\lambda$.

#### Figure 7-16 — Saltatory conduction *(listed)*

Two-panel comparison: unmyelinated axon with continuous wavefront vs. myelinated axon with AP "jumping" from node to node. The voltage trace at each node shows the AP arriving with negligible delay across internodes and full regeneration at each node.

---

## Equations summary (compact reference)

| Quantity | Equation |
|---|---|
| HH membrane equation | $C_m \dot{V} = -[g_{Na}m^3h(V - E_{Na}) + g_K n^4(V - E_K) + g_L(V - E_L)] + I_{ext}$ |
| Gating particle kinetics | $\dot{x} = \alpha_x(V)(1 - x) - \beta_x(V) x$, where $x \in \{m, h, n\}$ |
| Steady-state gating | $x_\infty(V) = \dfrac{\alpha_x(V)}{\alpha_x(V) + \beta_x(V)}$ |
| Gating time constant | $\tau_x(V) = \dfrac{1}{\alpha_x(V) + \beta_x(V)}$ |
| Two-state $P_o$ | $P_o = \dfrac{k_o}{k_o + k_c}$ |
| Macroscopic current | $I = N P_o \gamma(V - E_{rev})$ |
| Length constant | $\lambda = \sqrt{r_m / r_i}$ |
| Passive spread (steady) | $V(x) = V_0 e^{-x/\lambda}$ |
| Time constant | $\tau_m = r_m c_m$ |

---

## Glossary

- **Action potential (AP)** — all-or-none stereotyped depolarization.
- **Threshold** — $V_m$ at which net inward current overcomes net outward current.
- **Rheobase** / **chronaxie** — strength–duration anchors.
- **Absolute / relative refractory period (ARP / RRP)** — set by Na⁺-channel inactivation recovery.
- **Voltage clamp** — feedback control of $V_m$.
- **Activation / inactivation / deactivation / recovery from inactivation** — gating transitions.
- **m / h / n** — HH gating particles.
- **Delayed rectifier** — slow-activating K⁺ current responsible for repolarization in HH.
- **Inactivation** (Na⁺) — IFM-lid hinge between DIII and DIV.
- **DEKA selectivity ring** — Na⁺-channel selectivity filter motif.
- **TVGYG signature** — K⁺-channel selectivity filter.
- **S4 voltage sensor** — positively charged TM helix.
- **N-type "ball-and-chain"** vs. **C-type slow inactivation** — K⁺-channel inactivation modes.
- **Cable equation, length constant ($\lambda$), time constant ($\tau_m$)** — passive axon properties.
- **Saltatory conduction** — node-to-node AP regeneration in myelinated axons.
- **Conduction velocity** — scales with $\sqrt{d}$ unmyelinated, with $d$ myelinated.
- **L / N / P / Q / R / T Ca²⁺ channels** — voltage-gated Ca²⁺-channel classification.
- **HCN / $I_f$ / $I_h$** — pacemaker hyperpolarization-activated, cAMP-modulated.
- **hERG / $I_{Kr}$ / long QT** — repolarization current and its diseases.
- **Use-dependent block** — lidocaine, antiarrhythmic class I.
- **Channelopathy** — class of genetic and acquired diseases of voltage-gated channels.
- **HyperPP / paramyotonia / LQT3 / Brugada / Dravet / FHM1 / EA2 / SCA6 / Timothy / Andersen-Tawil / LEMS** — specific channelopathies.

---

## Cross-links forward

| Forward link | Topic | Where |
|---|---|---|
| Synaptic transmission and the NMJ | nicotinic AChR | Ch 8 |
| Skeletal / cardiac / smooth muscle physiology | EC-coupling, Cav1.1/1.2, RyR | Ch 9 |
| Synaptic transmission in CNS | glutamate/GABA, mGluR | Ch 13 |
| Cardiac AP, ECG, conduction | Nav1.5, Cav1.2, hERG | Ch 21 |
| Pacemaker activity | HCN $I_f$ | Ch 21 |
| Sensory transduction | TRP family | Ch 15 |
| Long QT and antiarrhythmics | clinical anchors | Ch 21 |
| Demyelinating disease | MS, GBS | Ch 11, 12 |
| Diuretic targets | KATP / Kir6 in pancreatic β cells (sulfonylureas) | Ch 51 |

## Source apparatus
- **Online Notes** N7-x referenced inline (19+ in this chapter).
- **Clinical boxes:** Box 7-1 (Na⁺-channel genetic defects), and running clinical anchors on local anesthetics, long-QT, periodic paralyses, and demyelinating disease.
- **References** deferred to companion site.

---

## Format-verification notes

**Figures viewed and described from image:** 7-3, 7-7, 7-10, 7-14 (+ contextual reading of pp. 188, 196 for Na⁺-channel inactivation and pp. 200 for local-anesthetic clinical box).

**Figures listed by caption + textual reference only:** 7-1, 7-2, 7-4, 7-5, 7-6, 7-8, 7-9, 7-11, 7-12, 7-13, 7-15, 7-16, plus any later figures (full inventory deferred to second pass).

*End of Chapter 7. End of batch: Chapters 3–7 saved. Next: Chapters 8 — Synaptic Transmission and the Neuromuscular Junction (Moczydlowski), p. 204.*
