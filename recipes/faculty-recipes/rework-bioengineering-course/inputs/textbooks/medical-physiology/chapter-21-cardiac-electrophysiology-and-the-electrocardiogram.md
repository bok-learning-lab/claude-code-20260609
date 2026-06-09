---
chapter: 21
title: Cardiac Electrophysiology and the Electrocardiogram
authors:
  - W. Jonathan Lederer
section: "IV. The Cardiovascular System"
source_pages: "483–506"
pdf_pages: "495–518"
source_book: "Boron WF, Boulpaep EL. Medical Physiology, 3rd edition (2017)"
figures_listed: "16 (21-1 through 21-16)"
figures_described_from_image: 5
equations: "few — Ohm's law for gap-junction current; chord-conductance V_m; Nernst (referenced)"
tables: 6
clinical_boxes: "3 (Vagal maneuvers; Basic interpretation of the ECG; Myocardial infarction)"
---

# Chapter 21 — Cardiac Electrophysiology and the Electrocardiogram

> Section IV · The Cardiovascular System · pp. 483–506 · Author: W. Jonathan Lederer

## Chapter map (top-level)

1. **Electrophysiology of cardiac cells** (pp. 483–493) — propagation through the heart via gap junctions; the four time- and voltage-gated currents ($I_{Na}$, $I_{Ca}$, $I_K$, $I_f$); the five phases; cell-type-specific action potentials (SA node, atrial, AV node, Purkinje, ventricular); autonomic modulation.
2. **The electrocardiogram** (pp. 493–500) — origin of the surface signal; the 12 leads (Einthoven's triangle, augmented limb, precordial); two-cell model of how vectors arise; basic ECG interpretation.
3. **Cardiac arrhythmias** (pp. 500–506) — conduction abnormalities (block, re-entry, accessory pathways); altered automaticity (EAD/DAD triggered activity, ectopic pacemakers); long-QT syndrome; Ca²⁺-overload and metabolic arrhythmogenesis.

This chapter applies the biophysics of Chapter 7 (voltage-gated channels, $m^3h$ kinetics, hERG/$I_{Kr}$, long QT) and the excitation–contraction coupling preview of Chapter 9 (Cav1.2-triggered SR Ca²⁺ release) to the heart in vivo, and ends with how the resulting transmembrane currents project onto the body-surface ECG.

---

## Section 1 — Electrophysiology of cardiac cells (pp. 483–493)

### Subsection headings
- **The cardiac action potential starts in specialized muscle cells of the sinoatrial node and then propagates in an orderly fashion throughout the heart** (pp. 483–484)
- **The cardiac action potential conducts from cell to cell via gap junctions** (pp. 484–485)
- **Cardiac action potentials have as many as five distinctive phases** (pp. 485–486)
- **The Na⁺ current is the largest current in the heart** (pp. 486–487)
- **The Ca²⁺ current in the heart passes primarily through L-type Ca²⁺ channels** (pp. 487–488)
- **The repolarizing K⁺ current turns on slowly** (pp. 488–489)
- **The $I_f$ current is mediated by a nonselective cation channel** (p. 489)
- **Different cardiac tissues uniquely combine ionic currents to produce distinctive action potentials** (pp. 489–491)
- **Atrial and ventricular myocytes fire action potentials but do not have pacemaker activity** (pp. 491–492)
- **Acetylcholine and catecholamines modulate pacemaker activity, conduction velocity, and contractility** (pp. 491–493)

### Core claims

#### Conduction pathway through the heart

The cardiac electrical signal originates at the **sinoatrial (SA) node** in the right atrium (intrinsic rate ≈60–100 bpm at rest) and propagates in a stereotyped sequence:

$$
\text{SA node} \rightarrow \text{atria (incl. Bachmann's bundle to LA)} \rightarrow \text{AV node} \rightarrow \text{bundle of His} \rightarrow \text{L \& R bundle branches} \rightarrow \text{Purkinje fibers} \rightarrow \text{ventricular muscle}
$$

The **fibrous AV ring** electrically isolates the atria from the ventricles, so the **AV node → His–Purkinje** system is the only normal conduction route between them. Action potentials are classified by upstroke speed: **slow** (SA, AV nodes — $I_{Ca}$-driven upstroke, no $I_{Na}$) vs. **fast** (atrial, Purkinje, ventricular — $I_{Na}$-driven upstroke).

#### Gap-junction propagation (Cx43)

Cardiac myocytes form an electrical **functional syncytium**. Cells are connected by **gap junctions** (Cx43-rich intercalated discs); current flows from one cell to the next by Ohm's law:

$$I_{AB} = \frac{V_A - V_B}{R_{AB}} = \frac{\Delta V_{AB}}{R_{AB}} \tag{21-1}$$

When $R_{AB}$ is small (tight coupling), depolarization spreads efficiently. Conduction velocity rises when (i) more depolarizing current is injected from the active region (larger $I_{Na}$ / $I_{Ca}$) or (ii) the threshold of the downstream cell is more negative. Each cell's intracellular current crossing a junction has an equal and opposite **extracellular** current loop; it is the **sum of these extracellular vectors across the whole heart** that constitutes the ECG signal.

#### The four time- and voltage-gated cardiac currents

| # | Current | Role |
|---|---|---|
| 1 | $I_{Na}$ | rapid depolarizing upstroke (phase 0) in **atrial, ventricular, Purkinje** (absent in SA / AV nodes) |
| 2 | $I_{Ca}$ (L-type) | upstroke in SA / AV nodes; plateau-sustaining in fast cells; **triggers EC-coupling** in all cardiomyocytes |
| 3 | $I_K$ | repolarization in all cardiomyocytes |
| 4 | $I_f$ ("funny") | pacemaker depolarization in SA, AV, Purkinje |

Two **electrogenic transporters** also carry current across the sarcolemma: the type-1 Na–Ca exchanger (**NCX1**) and the Na–K pump.

#### Five phases of the cardiac action potential

| Phase | Name | Mechanism (ventricular myocyte) |
|---|---|---|
| **0** | upstroke | rapid $I_{Na}$ activation (fast cells); $I_{Ca,L}$ in slow nodal cells |
| **1** | early rapid repolarization (notch) | inactivation of $I_{Na}$ + activation of $I_{to}$ (A-type K⁺ via Kv4.3 + KChIP2) |
| **2** | plateau | balance of inward $I_{Ca,L}$ (and small $I_{Na,late}$, NCX) against outward $I_{Ks}$ |
| **3** | repolarization | $I_{Kr}$ (hERG) + $I_{Ks}$ dominate; $I_{Ca,L}$ inactivates |
| **4** | electrical diastole | nodal/Purkinje: pacemaker depolarization driven by $I_f$, decaying $I_K$, ramping $I_{Ca}$; atrial/ventricular: stable resting $V_m$ set by $I_{K1}$ |

In SA and AV nodal cells, the most negative $V_m$ in phase 4 is the **maximum diastolic potential** (~–60 to –70 mV). Atrial and ventricular cells reach a stable **resting potential** (~–80 mV) set predominantly by $I_{K1}$ (Kir2.1, KCNJ2).

#### Channel and current inventory (Table 21-1)

| Current | Channel protein | Gene | $E_{rev}$ (mV) | Inhibitors |
|---|---|---|---|---|
| $I_{Na}$ | Nav1.5 | *SCN5A* | +60 | TTX, lidocaine, class I antiarrhythmics |
| $I_{Ca,L}$ | Cav1.2 | *CACNA1C* | +120 | nifedipine, verapamil, diltiazem |
| $I_{to}$ | Kv4.3 + KChIP2 | *KCND3 + KCNIP2* | −100 | tedisamil |
| $I_{Kr}$ | Kv11.1 (hERG) + miRP1 | *KCNH2 + KCNE2* | −100 | dofetilide, E-4031, Ba²⁺, Cs⁺, TEA |
| $I_{Ks}$ | Kv7.1 (KvLQT1) + minK | *KCNQ1 + KCNE1* | −100 | HMR1556, L-768,673, chromanols |
| $I_{K1}$ | Kir2.1 / Kir2.2 | *KCNJ2 / KCNJ12* | −100 | Ba²⁺, ML133 |
| $I_{K,ACh}$ (GIRK) | Kir3.4 (GIRK4) | *KCNJ5* | −100 | — |
| $I_{K,ATP}$ | Kir6.1/6.2 + SUR1/2 | *KCNJ8 / KCNJ11 + ABCC8/9* | −100 | glibenclamide |
| $I_f$ (Na⁺ + K⁺) | HCN4 | *HCN4* | −35 | Cs⁺, ivabradine (clinical) |

Typical equilibrium potentials (Table 21-2) at $[Na^+]_i = 10$, $[Na^+]_o = 145$ mM → $E_{Na} \approx +72$ mV; $[K^+]_i = 120$, $[K^+]_o = 4.5$ mM → $E_K \approx –88$ mV; $[Ca^{2+}]_i = 10^{-4}$, $[Ca^{2+}]_o = 1.16$ mM → $E_{Ca} \approx +137$ mV; $[Cl^-]_i \approx 30$, $[Cl^-]_o = 116$ → $E_{Cl} \approx –40$ mV.

#### Conduction velocities (Table 21-4)

| Tissue | Conduction velocity (m/s) |
|---|---|
| SA node | 0.05 |
| Atrial pathways | 1 |
| **AV node** | **0.05** (built-in delay → atria empty before ventricular systole) |
| Bundle of His | 1 |
| Purkinje system | **4** (fastest in the heart) |
| Ventricular muscle | 1 |

#### Cell-type specifics

**SA node — primary pacemaker.** Intrinsic rate ~60 bpm. Lacks $I_{Na}$. Phase 4 pacemaker depolarization driven by the interaction of three currents: declining $I_K$ + rising inward $I_f$ + rising $I_{Ca}$ (T- and L-type). Threshold ≈ –55 mV; phase 0 carried by $I_{Ca,L}$. Hierarchical override principle: the fastest pacemaker sets the heart rate.

**AV node — secondary pacemaker** (~40 bpm if SA fails). Same currents and ionic mechanism as SA node; slow conduction (0.05 m/s) imposes the **PR-interval delay** that lets the atria finish ejecting before ventricular activation.

**Atrial muscle.** $I_{Na}$, $I_{Ca}$, $I_K$. No normal pacemaker activity. Bachmann's bundle conducts SA → LA; three internodal tracts conduct SA → AV node.

**His–Purkinje system — tertiary pacemaker** (~20 bpm if SA + AV fail; unreliable). All four currents present; large $I_{Na}$ + favorable cable properties give the fastest conduction in the heart (4 m/s). Sequential ventricular activation:

1. Septum depolarizes **left to right**.
2. Anteroseptal myocardium depolarizes.
3. Free walls depolarize **endocardium → epicardium**; LV apex depolarizes first.
4. Wave spreads apex → base.
5. **Posterobasal LV is the last region to depolarize**.

Total ventricular activation ≈ 100 ms.

**Ventricular muscle.** $I_{Na}$, $I_{Ca,L}$, $I_K$. Resting $V_m \approx –80$ mV (no $I_f$). Prominent **plateau (phase 2)** because depolarized $V_m$ keeps $I_{Ca,L}$ open while $I_K$ activates slowly. The Ca²⁺ entering via Cav1.2 triggers **calcium-induced Ca²⁺ release (CICR)** from the SR via RyR2 (see Ch 9, pp. 242–243) — this is the EC-coupling link to mechanical contraction in Ch 22.

#### Refractoriness

Because $I_{Na}$ and $I_{Ca,L}$ are inactivated by sustained depolarization during the plateau, ventricular myocytes are **refractory** during most of phase 2 and early phase 3.

- **Absolute refractory period (ARP)** — no stimulus, however large, can produce another AP. Set by full inactivation of $I_{Na}$.
- **Effective refractory period (ERP)** — equivalent to ARP in cardiac muscle (Lederer's wording): no propagating AP can be re-initiated.
- **Relative refractory period (RRP)** — as $I_{Na}$ and $I_{Ca,L}$ recover from inactivation, a stronger-than-normal stimulus can elicit a smaller AP.
- **Supernormal period** — a brief window late in phase 3 when threshold is transiently more negative than at rest.

Refractoriness protects the ventricles from tetanus (cf. skeletal muscle, Ch 9) and from ectopic re-excitation.

#### Autonomic modulation (Table 21-3 + Fig. 21-6)

Three mechanisms can change SA-nodal firing rate:
1. **Steepness of phase 4 depolarization** (slope of pacemaker ramp).
2. **Maximum diastolic potential** (starting voltage).
3. **Threshold** for the regenerative upstroke.

**Vagal / parasympathetic — ACh on M₂ receptors → G_i:**
- ↓ $I_f$ (slower phase 4) — Fig. 21-6A.
- Opens **GIRK** ($I_{K,ACh}$) via Gβγ → more negative maximum diastolic potential — Fig. 21-6B.
- ↓ $I_{Ca,L}$ → less steep phase 4 + more positive threshold — Fig. 21-6C.
- Net: **negative chronotropy** in SA node; **negative dromotropy** (slowed conduction) at AV node — clinical basis of vagal maneuvers (Box 21-1: Valsalva, carotid sinus massage).

**Sympathetic — NE/Epi on β₁-AR → G_s → AC → cAMP → PKA:**
- ↑ $I_f$ (cAMP binds HCN4 cyclic-nucleotide-binding domain directly) → steeper phase 4.
- ↑ $I_{Ca,L}$ in all myocytes → more negative threshold; faster phase 0 in nodal cells.
- ↑ SR Ca²⁺ release sensitivity (RyR2 phosphorylation), ↑ SERCA via **phospholamban (PLN) phosphorylation** → larger Ca²⁺ stores.
- Net: **positive chronotropy, dromotropy, and inotropy**; shorter AP duration (faster relaxation, "lusitropy").

#### Catecholamine inotropy — four-step mechanism

1. ↑ $I_{Ca,L}$ → greater trigger Ca²⁺ entry.
2. Greater Ca²⁺-induced Ca²⁺ release (CICR) per heartbeat.
3. Phospholamban phosphorylation disinhibits **SERCA** → faster SR Ca²⁺ refilling.
4. Increased $I_{Ca,L}$ delivers more substrate to SERCA → SR stores grow over time.

### Citation-anchor quotes
- > "The cardiac action potential originates in a group of cells called the sinoatrial (SA) node, located in the right atrium. These cells depolarize spontaneously and fire action potentials at a regular, intrinsic rate." (p. 483)
- > "Because cardiac cells are electrically coupled through gap junctions, the action potential propagates from cell to cell in the same way that an action potential in nerve conducts along a single long axon." (p. 484)
- > "Each point on an electrocardiogram (ECG) is the sum of the many such electrical vectors, generated by the many cells of the heart." (p. 484)
- > "The Na⁺ current (I_Na) is the largest current in heart muscle... This current is not present in SA or AV nodal cells." (p. 486)
- > "The unique cardiac α subunit (Nav1.5) has several phosphorylation sites that make it sensitive to stimulation by cAMP-dependent protein kinase." (p. 486)
- > "The L-type Ca²⁺ channel (Cav1.2) is the dominant one in the heart." (p. 487)
- > "Cardiac action potentials last two orders of magnitude longer than action potentials in skeletal muscle because the repolarizing K⁺ current turns on very slowly." (p. 488)
- > "The HCN channels have the unusual property (hence the subscript f for 'funny' current) that they do not conduct at positive potentials but are activated by hyperpolarization at the end of phase 3." (pp. 488–489)
- > "The fastest pacemaker sets the heart rate and overrides all slower pacemakers." (p. 490)
- > "The effective refractory period is the same as the absolute refractory period in nerve and skeletal muscle." (p. 491)
- > "ACh decreases I_f in the SA node... opens GIRK channels, increasing relative K⁺ conductance and making the maximum diastolic potential of SA nodal cells more negative... reduces I_Ca in the SA node." (p. 492)
- > "Catecholamines... increase I_f in the nodal cells, thereby increasing the steepness of the phase 4 depolarization." (p. 492)

### Figures

#### Figure 21-1 — Conduction pathways through the heart *(viewed)*

A long-axis cross-section of the heart annotated with the full conduction tree, drawn in yellow over the muscular anatomy. Labeled, from top to bottom: **SA node** (high in the right atrial wall near the superior vena cava); **internodal pathways** running down the RA; **Bachmann's interatrial tract** branching from the SA node to the left atrium; **AV node** at the floor of the right atrium just above the AV ring; **bundle of His** crossing the fibrous ring; mainstem **left bundle branch** splitting almost immediately into an **anterosuperior** and a **posteroinferior** fascicle; **right bundle branch** descending along the septum; both bundle branches arborize into **Purkinje fibers** that ring the ventricular endocardium and feed the **ventricular muscle** from inside out. The atrial muscle and ventricular muscle are shown shaded.

> Vision note: This is the chapter's anatomical keystone. Use as a RAG anchor for any forward query about conduction-block localization (AV block at the node vs. infranodal; LAFB/LPFB hemiblocks; RBBB), accessory pathways (bundle of Kent bypasses the AV ring), and the SA-node neighborhood for surgical ablation targets.

#### Figure 21-2 — Cardiac action potentials by cell type *(viewed)*

Five stacked $V_m(t)$ traces over 800 ms, recorded as if simultaneously, showing how the same conduction wave acquires different shapes in different cells:

- **A — SA node.** Continuous pacemaker oscillation. Slow phase 4 ramp from ~–60 mV up to threshold ~–55 mV; slow upstroke (carried by $I_{Ca}$, no $I_{Na}$); no plateau; smooth repolarization back to maximum diastolic potential. No flat resting interval — phase 4 immediately starts ramping up again.
- **B — Atrial muscle.** Resting potential ~–80 mV. Fast upstroke ($I_{Na}$); brief, modest plateau; relatively rapid repolarization. Shorter AP duration than ventricular.
- **C — AV node.** Slow upstroke, low maximum diastolic potential, slow firing — qualitatively similar to SA node but slower intrinsic rate.
- **D — Purkinje fibers.** Largest fast upstroke; very prominent phase 1 notch; long plateau; clear phase 4 pacemaker drift (slowest of the three intrinsic pacemakers).
- **E — Ventricular muscle.** Resting –80 mV; rapid $I_{Na}$ upstroke; smaller phase 1 notch than Purkinje; the **longest plateau** in the heart (~200–300 ms); steep phase 3; flat phase 4 (no pacemaker activity).

> Vision note: The single most important figure in the chapter — it makes the "different cells, same conduction wave" point in one image. Anchor for any cell-type-specific arrhythmia or pharmacology query.

#### Figure 21-3 — Conduction in the heart and electrotonic spread *(viewed)*

Three-panel didactic explanation of how the action potential propagates.

- **Panel A — Currents through gap junctions.** A chain of three cells (A, B, C). Inside the cells, the **intracellular current** flows axially through the gap-junction channels (Cx43, drawn as paired hemichannel barrels). Outside, the **extracellular current** loops back through the bulk extracellular fluid. A **capacitative current** is shown charging/discharging the bilayer of cell B. The text formula box gives $I_{AB} = \Delta V_{AB}/R_{AB}$.
- **Panel B — Electrotonic spread of subthreshold current.** A chain of six cells (A–F). Current injected at cell A produces a depolarization that decays exponentially with distance along the chain. The dashed horizontal line marks the threshold; the subthreshold profile falls below it before reaching the last cell.
- **Panel C — Threshold vs. propagation speed.** Two superimposed exponential decay curves at the same starting depolarization but compared to two threshold lines. Red curve: cell A fires but the spread reaches cell B only after a long electrotonic delay. Blue curve (more current injected): cell B reaches threshold sooner → faster conduction. A second annotation shows that a **more negative threshold** also speeds conduction even with the same injected current.

> Vision note: This figure explains why conduction velocity depends on (i) source-current magnitude and (ii) downstream threshold — the framework needed to understand depolarization-induced conduction block in ischemia and the use-dependence of class I antiarrhythmics.

#### Figure 21-4 — Phases of cardiac action potentials *(listed)*

Two paired panels. **A — SA node** showing the slow $I_{Ca}$-driven upstroke, no $I_{Na}$ trace, and the three pacemaker currents ($I_f$ blue, $I_{Ca}$ red, $I_K$ green) ramping during phase 4. **B — Ventricular muscle** showing the five phases labeled 0–4 with current traces below: massive transient inward $I_{Na}$ for phase 0; small $I_{to}$ during phase 1; sustained inward $I_{Ca,L}$ balanced against slowly activating outward $I_K$ during phase 2; rising $I_K$ during phase 3; resting $I_{K1}$ during phase 4. The **effective refractory period (ERP)** and **relative refractory period (RRP)** are bracketed above the ventricular trace.

#### Figure 21-5 — Sequence of depolarization in cardiac tissue *(viewed)*

Six anatomical cartoons of the heart in long-axis section, drawn in cutaway, each highlighting (in yellow) the region of myocardium currently depolarizing. Step-by-step:

1. **Depolarize atria.** Yellow spreads from SA node down through both atria, axis roughly right-to-left and inferior — generating the **P wave**.
2. **Depolarize septum left to right.** A small yellow region appears in the interventricular septum near its left side; the LV side activates first because of left-bundle Purkinje arborization — generates the **septal Q wave** in lateral leads.
3. **Depolarize anteroseptal region toward apex.** Yellow expands into the anteroseptal myocardium running toward the apex.
4. **Depolarize bulk of ventricular myocardium, endocardium → epicardium.** Both ventricles' free walls light up; activation moves radially outward.
5. **Depolarize posterior portion of base of LV.** A last yellow patch at the posterobasal LV.
6. **Ventricles fully depolarized.** Entire ventricular shell highlighted; the surface ECG is now at the **isoelectric ST segment**.

Steps 2–6 unfold in ~100 ms and together write the **QRS complex**.

> Vision note: This is the bridge between intracellular electrophysiology and surface ECG morphology. Use it to anchor leads-correspondence reasoning (II/III/aVF "look at" the inferior wall; V1–V6 traverse the precordium from septum to lateral wall) and Q-wave localization in infarction (Box 21-3).

#### Figure 21-6 — Modulation of pacemaker activity *(listed)*

Three idealized panels of an SA-node $V_m(t)$ trace, each showing one mechanism of slowing the firing rate. **A — Decreased rate of phase-4 depolarization** (blue trace, shallower slope, lengthens time-to-threshold). **B — More negative maximum diastolic potential** (green trace, longer climb from a lower starting voltage). **C — More positive threshold** (purple horizontal threshold line; reaching it takes longer at unchanged slope). ACh uses all three; β-adrenergic stimulation reverses A and C.

#### Figure 21-7 — Components of the ECG recording *(viewed)*

A single idealized lead-II tracing over 2 s with all the standard labels. The waveforms in order: a small upright **P wave** (atrial depolarization); a brief flat segment (electrical signal traversing the AV node — invisible on the surface ECG); the **QRS complex** with a small initial downward **Q**, a tall upright **R**, and a downward **S** (ventricular depolarization); an isoelectric **ST segment** (ventricles uniformly depolarized — plateau); an upright **T wave** (ventricular repolarization); and a small late hump for the **U wave** (possibly papillary-muscle repolarization). Annotated intervals: **PR interval** (start of P to start of QRS — AV nodal conduction); **QRS duration** (ventricular activation time); **QT interval** (start of Q to end of T — total ventricular depolarization + repolarization); **R–R interval** (between successive R waves — defines heart rate). A note at the side states that the ECG cannot show the electrical activity of the **SA node, AV node, bundle of His, bundle branches, or Purkinje fibers** — the cell mass is too small.

> Vision note: The reference figure for ECG-interval interpretation. Use as the RAG anchor for all "what does the X interval mean" queries, and for long-QT correlation with phase-2/phase-3 lengthening.

### Tables

#### Table 21-3 — Electrical properties of cardiac tissues

| Tissue | Function | Principal currents | β-adrenergic effect | Cholinergic effect |
|---|---|---|---|---|
| SA node | primary pacemaker | $I_{Ca}$, $I_K$, $I_f$ | ↑ pacemaker rate; ↑ conduction velocity | ↓ pacemaker rate; ↓ conduction velocity |
| Atrial muscle | expel blood from atria | $I_{Na}$, $I_{Ca}$, $I_K$ | ↑ strength of contraction | little effect |
| AV node | secondary pacemaker | $I_{Ca}$, $I_K$, $I_f$ | ↑ pacemaker rate; ↑ conduction velocity | ↓ pacemaker rate; ↓ conduction velocity |
| Purkinje fibers | rapid conduction; tertiary pacemaker | $I_{Na}$, $I_{Ca}$, $I_K$, $I_f$ | ↑ pacemaker rate | ↓ pacemaker rate |
| Ventricular muscle | expel blood from ventricles | $I_{Na}$, $I_{Ca}$, $I_K$ | ↑ contractility | little effect |

---

## Section 2 — The electrocardiogram (pp. 493–500)

### Subsection headings
- **An ECG generally includes five waves** (pp. 493–494)
- **A pair of ECG electrodes defines a lead** (pp. 494–495)
- **A simple two-cell model can explain how a simple ECG can arise** (pp. 496–497)

### Core claims

#### The waves and intervals

A single PQRST cycle (Fig. 21-7) summarizes the electrical events of one heartbeat:

| Wave / interval | Electrical event | Normal duration |
|---|---|---|
| **P** | atrial depolarization | ≤ 0.12 s |
| **PR interval** | onset P → onset QRS (mostly AV-node delay) | 0.12–0.20 s |
| **QRS complex** | ventricular depolarization | < 0.12 s (narrow) |
| **ST segment** | ventricles fully depolarized (plateau) | isoelectric |
| **T wave** | ventricular repolarization | upright in most leads |
| **QT interval** | onset Q → end T (total ventricular AP duration) | rate-dependent ($QT_c \lesssim 440$ ms typically) |
| **U wave** | (possibly) papillary-muscle repolarization | small, often invisible |
| **R–R interval** | between successive R waves | defines heart rate |

The ECG does **not** display: SA node, AV node, bundle of His, bundle branches, or Purkinje fiber activity directly — these tissue masses are too small to generate detectable extracellular fields.

#### The 12 leads — geometry of the surface signal

The body is modeled as a volume conductor in which the heart projects a time-varying electrical vector onto a set of standardized axes (Einthoven's triangle and the precordial transverse plane).

**Six limb leads (frontal plane)**:
- **Standard bipolar (Einthoven):** I (LA⁺/RA⁻, axis 0°), II (LL⁺/RA⁻, +60°), III (LL⁺/LA⁻, +120°).
- **Augmented unipolar (Goldberger):** aVR (RA⁺ vs. mean LA + LL, axis –150°), aVL (LA⁺, –30°), aVF (LL⁺, +90°).
- Together these define axes every 30° around a polar circle in the frontal plane.

**Six precordial leads (transverse plane):**
- **V₁** — 4th intercostal space, right of sternum.
- **V₂** — 4th intercostal space, left of sternum.
- **V₃** — halfway between V₂ and V₄.
- **V₄** — 5th intercostal space, midclavicular line.
- **V₅** — between V₄ and V₆.
- **V₆** — 5th intercostal space, midaxillary line.

Each lead views the heart from a unique angle; recording 12 simultaneously lets a localized event (e.g., an inferior infarct seen in II/III/aVF) be detected and mapped.

**Einthoven's triangle (geometric ID):** the limb leads behave as an equilateral triangle with vertices at the two shoulders and the groin. The augmented leads bisect the triangle's sides, giving 30° resolution in the frontal plane.

#### Vector reasoning — the two-cell model (Fig. 21-10)

If two adjacent cells A and B fire APs displaced in time, the extracellular voltmeter records the difference $V_A - V_B$:
- Wave of depolarization **toward** positive electrode → upward (positive) deflection — the QRS equivalent.
- Wave **perpendicular** to the lead axis → isoelectric.
- Wave **away from** positive electrode → downward (negative) deflection.

Because in normal hearts the **ventricular myocytes that depolarize last repolarize first** (epicardial APs are shorter than endocardial), the T wave is **upright** in the same leads in which the QRS is upright. This explains the normal concordance of QRS and T axes despite repolarization being electrically the reverse of depolarization.

#### Heart-rate determination (Table 21-6)

ECG paper grid: small box = 1 mm = 0.04 s; large box = 5 mm = 0.20 s. With one R wave on a heavy line, the next R waves correspond to **300, 150, 100, 75, 60, 50 bpm** at 1–6 large boxes. General formula:

$$\text{Heart rate (bpm)} = \frac{300}{\text{R–R interval in large boxes}} = \frac{60}{\text{R–R interval in seconds}}$$

#### Eightfold approach to reading an ECG (Box 21-2, Table 21-5)

1. Search for **P waves**.
2. Determine relationship of P waves to QRS complexes.
3. Identify the **pacemaker** (sinus vs. ectopic vs. dissociated).
4. Measure heart rates from different waves (P–P interval, R–R interval — equal in sinus rhythm).
5. Characterize the **QRS shape** (narrow < 0.12 s vs. wide).
6. Examine **ST-segment** features.
7. Estimate the mean **QRS axis** (normal: –30° to +90°).
8. Examine the **rhythm** in a 20–30 s strip from lead II.

**Axis estimation** — quick qualitative method:
- Find a lead in which the QRS is **isoelectric**; the mean vector is perpendicular to that lead.
- Among the two perpendicular candidates, choose the one in which the QRS is **largely positive**.

#### ECG of ischemia and infarction (Box 21-3)

Acute MI evolves on the ECG through stereotyped stages, all interpretable via the two-cell model with cell B (the injured cell) having a less negative resting potential but the same plateau:

1. **Hyperacute T waves** (peaked).
2. **T-wave inversion**.
3. **ST-segment elevation** in leads overlying the injured wall — the most characteristic acute MI sign. Geometric origin: in the two-cell model, $V_A - V_B$ is depressed everywhere **except at the ST segment** (when both cells are at the plateau and equal), so the segment **appears** elevated relative to the depressed TP and PR baseline.
4. **Deep Q waves** in the leads overlying the infarct — net depolarization vector now points away from the electrically silent dead muscle.

Reperfused / transient ischemia → reversible T- and ST-changes; fixed occlusion without complete cell death → ST-depression and T-inversion (subendocardial ischemia).

### Citation-anchor quotes
- > "The P wave reflects depolarization of the right and left atrial muscle. The QRS complex represents depolarization of ventricular muscle. The T wave represents repolarization of both ventricles." (p. 494)
- > "Willem Einthoven was awarded the 1924 Nobel Prize in Physiology or Medicine." (p. 494)
- > "Because the body is an electrical 'volume conductor,' an electrical attachment to an arm is electrically equivalent to a connection at the shoulder joint." (p. 495)
- > "When a lead is perpendicular to the wave of depolarization, the measured deflection on that lead is isoelectric." (p. 497)
- > "Thus, on average, the ventricular myocytes that depolarize last are the first to repolarize." (p. 497)
- > "The next change, and one that is more characteristic of an acute myocardial infarction, is elevation of the ST segment." (Box 21-3, p. 499)
- > "The Q waves indicate an area of myocardium that has become electrically silent." (Box 21-3, p. 499)

### Figures

#### Figure 21-8 — The 12-lead placement *(listed)*

Two anatomical panels. **A — Frontal plane:** patient supine, electrodes at right arm, left arm, right leg (ground), left leg; the three resulting bipolar axes (I, II, III) drawn as an equilateral triangle around the torso. **B — Transverse plane:** chest cross-section with the six precordial-electrode sites V₁–V₆ marked along an arc from the right parasternal 4th intercostal space, across the midclavicular line, to the midaxillary line at the 5th intercostal space; the resultant axes radiate from the precordium toward the heart.

#### Figure 21-9 — Axes of the limb leads *(listed)*

Two panels. **A — Einthoven's triangle** with the three bipolar leads I, II, III separated by 60°. The augmented unipolar leads (aVR, aVL, aVF), referenced to the electronic average of the other two electrodes, bisect the three sides of the triangle. **B — Circle of axes:** translation of all six limb-lead axes to a common origin gives a polar coordinate system with axes at every 30° in the frontal plane (0°, +30°, +60°, +90°, +120°, +150°, +180°/–180°, –150°, –120°, –90°, –60°, –30°).

#### Figure 21-10 — Two-cell model of the ECG *(listed)*

Five panels using two coupled cells (A and B) connected by gap junctions ($R_{gj}$). **A — Intracellular APs** in A and B displaced in time. **B — Subtracted intracellular voltage** ($V_A - V_B$) producing a positive deflection (QRS-equivalent) and then a later negative deflection (T-equivalent — but inverted compared to a real T wave, because both cells in this model have equal APD). **C — Extracellular wave toward the positive electrode:** positive deflection on the ECG. **D — Wave perpendicular to the lead axis:** isoelectric trace. **E — Wave away from positive electrode:** negative deflection. The text explains how unequal APD between A and B (longer in endocardial-equivalent A than in epicardial-equivalent B) produces an **upright** T wave.

#### Figure 21-11 — Normal 12-lead ECG recording *(listed)*

A standard clinical recording showing the synchronized PQRST in all 12 leads simultaneously (three at a time across four panels), with a calibration pulse on the left.

#### Figure 21-12 — Estimation of the ECG axis in the frontal plane *(listed)*

Two worked examples: **A — Geometric method.** Measure R-wave height in two leads, mark on a circle of axes, drop perpendiculars, vector = head of the resultant arrow (~+95° example). **B — Inspection method.** Find the isoelectric lead (aVL), pick the perpendicular that has positive deflection in the dominant lead (lead II → +60° axis).

#### Figure 21-13 — Two-cell model of myocardial infarction *(listed)*

Same two-cell paradigm as Fig. 21-10, but cell B has a less negative resting potential (membrane leak from ischemic injury) and the same plateau height. The subtracted trace $V_A - V_B$ is depressed everywhere except at the plateau — so the baseline (TP and PR segments) is **depressed** while the ST segment is at zero. Clinically reads as **ST elevation** relative to a "normal" baseline.

---

## Section 3 — Cardiac arrhythmias (pp. 500–506)

### Subsection headings
- **Conduction abnormalities are a major cause of arrhythmias** (pp. 501–504)
- **Altered automaticity can originate from the sinus node or from an ectopic locus** (pp. 504–506)
- **Ca²⁺ overload and metabolic changes can also cause arrhythmias** (p. 506)

### Two basic mechanisms

| Class | Examples |
|---|---|
| **Altered conduction** | AV blocks (1°, 2° Mobitz I/II, 3°); bundle branch blocks; re-entry (atrial flutter, AVNRT, AVRT in WPW, atrial and ventricular fibrillation); accessory pathways |
| **Altered automaticity** | sinus bradycardia / tachycardia; ectopic atrial / junctional / ventricular pacemakers; triggered activity (EADs, DADs) |

Many tachyarrhythmias also involve **triggered activity** (EADs/DADs) as a sub-mechanism beneath the umbrella of "altered automaticity."

### Conduction disturbances

#### Normal variants
- **Sinus tachycardia** — sinus rhythm > 100 bpm (exercise, fear, hyperthyroidism).
- **Sinus arrhythmia** — phasic heart-rate variation with respiration (inspiration ↑ rate, expiration ↓ rate); reflects baroreflex/vagal tone. Loss of sinus arrhythmia → autonomic dysfunction (e.g., diabetic autonomic neuropathy).

#### Partial conduction block
- **First-degree AV block** — PR > 0.20 s, every P conducts (Fig. 21-14B).
- **Second-degree AV block:**
  - **Mobitz I (Wenckebach)** — progressive PR lengthening until one P fails to conduct (Fig. 21-14C); usually AV-nodal lesion; benign.
  - **Mobitz II** — constant PR, then a dropped QRS (Fig. 21-14D); infranodal (His or below); high risk of progression to 3° block.
- **Rate-dependent / bundle-branch block** — when heart rate exceeds a critical level, a diseased bundle fails to repolarize in time → wide-QRS conduction via slow myocyte-to-myocyte spread (Fig. 21-14E: RBBB pattern in V₁/V₂; LBBB pattern in V₅/V₆).

#### Complete (3°) AV block — AV dissociation

No supraventricular impulse reaches the ventricles. Atria continue at the SA-node rate; ventricles beat at the rate of whichever junctional or Purkinje pacemaker takes over (typically 20–40 bpm). On ECG: regular P waves, regular but slower QRS, **no fixed P–QRS relationship** (Fig. 21-14F). Often a medical emergency requiring a pacemaker.

#### Re-entry — three requirements

Re-entry is one of the major causes of clinical arrhythmias. It requires:
1. A **closed conduction loop**.
2. A **region of unidirectional block** (at least transiently).
3. **Sufficiently slow conduction** around the loop (so the head of the wave always finds tissue recovered from refractoriness).

**Unidirectional block (Fig. 21-15B)** arises when an asymmetric lesion leaves many healthy cells on one side and few on the other: many → few cells can drive an AP, but few → many cannot inject enough current to depolarize the larger mass.

**Re-entrant excitation (Fig. 21-15D, four steps):**
1. Antegrade wave hits the bifurcation; left branch has unidirectional block → only the right branch conducts.
2. Distal cells fire; loop tissue is refractory in the orthograde direction.
3. Impulse re-enters the loop retrogradely from the distal end.
4. Retrograde wave traverses the previously blocked region (which conducts retrograde) and arrives back at the bifurcation, where the original tissue has had time to recover → re-excites. The cycle repeats indefinitely at a rate set by loop length / conduction velocity, **overriding the SA node**.

Re-entry can occur in small (myocyte-scale "micro-reentry") or large (anatomical macro-reentry) loops. It drives **atrial flutter, AVNRT, AVRT (WPW), atrial fibrillation, monomorphic VT, and ventricular fibrillation**.

#### Wolff-Parkinson-White syndrome — accessory pathway

The **bundle of Kent** is a muscular accessory pathway that bypasses the AV ring, connecting atrium directly to ventricle. ECG features (Fig. 21-14G):
- **Short PR interval** — no AV-nodal delay.
- **Delta wave** — slurred upstroke of the QRS = pre-excited ventricular myocardium depolarizing before the AV-nodal wave arrives.
- **Wide QRS** because the early myocyte-to-myocyte spread is slow.
- Substrate for **AVRT** (orthodromic uses AV node down + accessory up — narrow QRS; antidromic uses accessory down + AV up — wide QRS) and a danger if **atrial fibrillation** uses the accessory pathway to drive 1:1 ventricular response → VF risk.

#### Atrial fibrillation (Fig. 21-14H)

Multiple wandering re-entry circuits in the atria firing at ~300–500 per minute. ECG: **no P waves**, irregular fibrillatory baseline, **irregularly irregular** QRS rhythm (only some impulses penetrate the AV node). Hemodynamic cost is the **loss of atrial booster pump function** (~15–25% of ventricular filling). Stroke risk from atrial stasis → LA appendage thrombus. Rate control: digitalis, β-blockers, non-DHP Ca²⁺-channel blockers (verapamil, diltiazem) — all slow AV-nodal conduction.

#### Ventricular tachycardia and fibrillation

- **VT** — ≥ 3 consecutive ventricular ectopic beats; usually 120–200 bpm; substrate is typically peri-infarct re-entry. Can degenerate to VF.
- **VF** — disorganized ventricular re-entry; no coordinated mechanical pumping → cardiac arrest. Defibrillation (high-voltage shock to depolarize the entire myocardium synchronously) is the only effective acute therapy; it resets the substrate so that the SA node can resume control.

### Altered automaticity

Pacemaker activity can be lost (sinus arrest, sick-sinus syndrome) or gained where it does not belong (ectopic foci in atrium, junction, or ventricle).

#### Triggered activity — EADs and DADs (Fig. 21-16)

- **Early afterdepolarization (EAD)** — secondary depolarization arising during phase 2 or phase 3 of a **prolonged AP**. Mechanism: $I_{Na}$ inactivated → recovered $I_{Ca,L}$ can reopen and produce a slow positive deflection before repolarization completes. Triggered by $I_{Kr}$ blockade (long QT) → bradycardia-dependent. Substrate for **torsades de pointes**.
- **Delayed afterdepolarization (DAD)** — secondary depolarization arising during phase 4, **after** the AP has fully repolarized. Mechanism: Ca²⁺-overloaded SR spontaneously releases Ca²⁺ → activates inward $I_{ti}$ via NCX1 (3 Na⁺ in / 1 Ca²⁺ out → net depolarizing) and a Ca²⁺-activated nonselective cation channel. Tachycardia-dependent. Substrate for digitalis-toxicity arrhythmias and catecholaminergic polymorphic VT (CPVT).

Quinidine, sotalol, and other $I_{Kr}$-blocking antiarrhythmics can paradoxically be **arrhythmogenic** by inducing EADs — the "proarrhythmia" problem.

### Long-QT syndrome (LQTS)

Prolonged ventricular AP duration → prolonged QT interval → EAD-mediated **torsades de pointes** (polymorphic VT in which the QRS axis appears to twist around the isoelectric baseline). Two etiologies:

| Form | Mechanism |
|---|---|
| **Congenital LQTS** | mutations in cardiac ion-channel genes |
| **Acquired LQTS** (much more common) | drugs that block hERG; electrolyte disturbance (hypokalemia, hypomagnesemia, hypocalcemia) |

#### Major congenital LQTS subtypes (cross-reference Ch 7)

| Type | Gene | Channel | Current | Defect |
|---|---|---|---|---|
| **LQT1** | *KCNQ1* | Kv7.1 (KvLQT1) | $I_{Ks}$ ↓ | loss-of-function → impaired phase 3 (exercise-triggered events) |
| **LQT2** | *KCNH2* (hERG) | Kv11.1 | $I_{Kr}$ ↓ | loss-of-function → drug-target locus for acquired LQTS (auditory triggers) |
| **LQT3** | *SCN5A* | Nav1.5 | $I_{Na,late}$ ↑ | gain-of-function → failed inactivation prolongs plateau (rest/sleep events) |
| **LQT5** | *KCNE1* | minK (with Kv7.1) | $I_{Ks}$ ↓ | accessory-subunit loss-of-function |
| **LQT6** | *KCNE2* | miRP1 (with hERG) | $I_{Kr}$ ↓ | accessory-subunit loss-of-function |
| **LQT7 / Andersen–Tawil** | *KCNJ2* | Kir2.1 | $I_{K1}$ ↓ | loss-of-function → resting depolarization, periodic paralysis |
| **LQT8 / Timothy syndrome** | *CACNA1C* | Cav1.2 | $I_{Ca,L}$ ↑ | gain-of-function → prolonged plateau; syndactyly, autism |

**Drug-induced LQT** is screened pre-clinically with a mandatory **hERG assay** at the FDA. Classic offenders: erythromycin, ciprofloxacin (and other fluoroquinolones), terfenadine and astemizole (withdrawn), cisapride (withdrawn), haloperidol, methadone, sotalol, dofetilide, ibutilide, quinidine, tricyclic antidepressants, ondansetron.

### Ca²⁺ overload arrhythmias

**Digitalis intoxication** is the classic cause. Mechanism: cardiac glycosides block the Na–K pump → intracellular [Na⁺] rises → NCX1 runs less efficiently in forward (Ca²⁺-extrusion) mode → cytosolic [Ca²⁺] rises → SR Ca²⁺ load rises → spontaneous SR Ca²⁺ release → NCX1 generates $I_{ti}$ → **DADs**. Result: ventricular ectopy, bidirectional VT.

### Metabolism-dependent arrhythmias

During ischemia, [ATP]_i falls → **K_ATP channels open** → tonic outward K⁺ current pulls $V_m$ toward $E_K$ → cells become less excitable, conduction slows. This contributes to peri-infarct re-entry circuits.

### Electromechanical dissociation (PEA)

ECG activity without mechanical output. Causes include cardiac tamponade (pericardial effusion compressing the heart), tension pneumothorax, massive PE, severe hypovolemia, profound acidosis, hyperkalemia.

### Vaughan–Williams classification of antiarrhythmics (not in Boron text directly; standard pharmacology cross-reference)

| Class | Target | Examples | Effect |
|---|---|---|---|
| **IA** | Na⁺ channel (moderate); also $I_{Kr}$ | quinidine, procainamide, disopyramide | ↓ phase 0, ↑ APD; can prolong QT |
| **IB** | Na⁺ channel (mild, ischemic tissue) | lidocaine, mexiletine, phenytoin | ↓ APD; ventricular-selective |
| **IC** | Na⁺ channel (strong) | flecainide, propafenone | ↓ phase 0 markedly; avoid in structural heart disease |
| **II** | β-adrenergic | metoprolol, propranolol, esmolol | ↓ SA / AV nodal activity |
| **III** | $I_{Kr}$ (± others) | amiodarone (mixed), sotalol, dofetilide, ibutilide | ↑ APD, ↑ ERP |
| **IV** | L-type Ca²⁺ channel | verapamil, diltiazem | ↓ SA / AV nodal conduction |
| **Other** | adenosine (A₁ → $I_{K,Ado}$, ↓ AV); digoxin (vagal + Na/K ATPase); ivabradine ($I_f$); ranolazine ($I_{Na,late}$) | — | rate / rhythm modulation |

### Citation-anchor quotes
- > "Any change in cardiac rhythm from the normal sinus rhythm is defined as an arrhythmia." (p. 497)
- > "Re-entry has three requirements: (1) a closed conduction loop, (2) a region of unidirectional block (at least briefly), and (3) a sufficiently slow conduction of action potentials around the loop." (p. 503)
- > "In Mobitz type I block (or Wenckebach block), the PR interval gradually lengthens from one cycle to the next until the AV node fails completely, skipping a ventricular depolarization." (p. 502)
- > "AV nodal block electrically severs the atria and ventricles, each of which beats under control of its own pacemakers. This situation is called AV dissociation." (p. 502)
- > "The aberrant conduction pathway in WPW syndrome also establishes a loop that may meet the requirements for re-entry." (p. 505)
- > "In atrial fibrillation... the re-entry loop within the atria moves wildly and rapidly, generating a rapid succession of action potentials — as many as 500 per minute." (p. 505)
- > "Ventricular fibrillation is a life-threatening medical emergency. The heart cannot generate cardiac output because the ventricles are not able to pump blood without a coordinated ventricular depolarization." (p. 505)
- > "Patients with long QT syndrome (LQTS) have a prolonged ventricular action potential and are prone to ventricular arrhythmias. In particular, these patients are susceptible to a form of ventricular tachycardia called torsades de pointes." (p. 506)
- > "Ca²⁺ overload occurs when [Ca²⁺]_i increases, causing the SR to sequester too much Ca²⁺. Thus overloaded, the SR begins to cyclically — and spontaneously — dump Ca²⁺ and then take it back up." (p. 506)

### Figures

#### Figure 21-14 — Pathological ECGs *(listed)*

Nine-panel gallery of representative tracings. **A** normal sinus rhythm. **B** 1° AV block (long PR). **C** Mobitz I (progressive PR until dropped QRS). **D** Mobitz II (constant PR, abrupt 2:1 dropped QRS). **E** bundle-branch block (wide QRS in V₁/V₂ for RBBB; V₅/V₆ for LBBB). **F** 3° AV block (P and QRS dissociated). **G** delta wave / WPW (short PR, slurred QRS upstroke). **H** atrial fibrillation (no P, irregularly irregular QRS). **I** ventricular fibrillation (chaotic, no organized QRS, no T).

#### Figure 21-15 — Abnormal conduction *(viewed)*

Four panels.

- **A — Normal conduction in both directions.** A linear array of myocytes; arrows show the AP propagating bidirectionally.
- **B — Unidirectional block.** A patch of dead cells partially severs the array. Right-to-left conduction succeeds (many healthy cells inject enough current to depolarize the few remaining); left-to-right conduction fails (few cells cannot drive the many).
- **C — Normal conduction through a bifurcation.** A Y-shaped Purkinje fiber feeding a ring of ventricular myocytes. Two opposing waves enter from the two branches and **collide in the middle**; they extinguish each other because the tissue ahead is refractory.
- **D — Re-entrant excitation.** Same anatomy as C, but a **unidirectional block** in the left branch prevents the antegrade wave from descending. The right-branch wave reaches the ventricular ring (step 1), depolarizes the distal myocardium (step 2), enters the bottom of the blocked left branch (step 3 — refractory cells in the right branch prevent retrograde re-excitation there), travels **retrograde** through the unidirectionally blocked segment (step 4 — block conducts retrograde), and re-emerges at the bifurcation (step 5) where the originally activated tissue has now recovered. The wave re-enters the ring, and the loop becomes self-sustaining at a frequency higher than the sinus rate. This loop is the substrate for AVNRT, AVRT, and many forms of VT.

> Vision note: The conceptual keystone for re-entry. Every form of macro-reentry tachyarrhythmia (AFlutter, AVNRT, AVRT, scar-related VT) is a topological variation of this picture.

#### Figure 21-16 — Abnormal automaticity in ventricular muscle *(listed)*

Two panels of idealized ventricular $V_m(t)$ with current traces below. **A — Prolonged AP → EAD.** A long plateau keeps $I_{Na}$ inactivated; $I_{Ca,L}$ recovers and reopens, producing a positive deflection during phase 3 (the EAD). **B — Prolonged AP → run of spontaneous activity.** Same prolonged AP, but the EAD reaches threshold and triggers a series of slow $I_{Ca,L}$-driven afterbeats — substrate for torsades de pointes.

---

## Equations summary (compact reference)

| Quantity | Equation |
|---|---|
| Gap-junction current (Ohm's law) | $I_{AB} = (V_A - V_B)/R_{AB}$ |
| Chord-conductance $V_m$ (from Ch 6, Eqn 6-12) | $V_m = G_{Na}/G_m \cdot E_{Na} + G_K/G_m \cdot E_K + G_{Ca}/G_m \cdot E_{Ca} + G_{Cl}/G_m \cdot E_{Cl}$ |
| Nernst (representative for cardiac ions, 37 °C) | $E_X = \dfrac{60\,\text{mV}}{z}\log_{10}\dfrac{[X]_o}{[X]_i}$ |
| Heart rate from R–R | $\text{HR} = 60 / \text{R–R}_{s} = 300/\text{R–R}_{\text{large boxes}}$ |
| Bazett's QT-correction (clinical, not in Boron) | $QT_c = QT / \sqrt{R\!-\!R}$ |

---

## Clinical mnemonics

- **SA → atria → AV → His → bundle branches → Purkinje → ventricles**: the conduction chain in order.
- **Phases 0–4** of the ventricular AP: 0 = Na⁺ in; 1 = $I_{to}$ K⁺ out; 2 = Ca²⁺ in vs. $I_{Ks}$ K⁺ out (plateau); 3 = $I_{Kr}$ + $I_{Ks}$ K⁺ out; 4 = $I_{K1}$ K⁺ out (rest).
- **"If a heart misses a hERG, it gets a torsades"** — $I_{Kr}$ (hERG) block prolongs QT → EAD → polymorphic VT.
- **Mobitz I = "Wenckebach lengthening"; Mobitz II = "sudden dropout"** — pneumonic for second-degree AV block patterns.
- **The 300/150/100/75/60/50 series** — heart-rate quick-look from R–R interval in large boxes.
- **R-on-T phenomenon** — premature ventricular complex during the vulnerable period (relative refractory) → VT/VF.
- **Re-entry triad: closed loop + unidirectional block + slow conduction.**

---

## Glossary

- **Action potential phases (0–4)** — cardiac AP segmentation.
- **Automaticity** — spontaneous diastolic depolarization in pacemaker cells.
- **Bachmann's bundle** — interatrial conduction tract SA → LA.
- **β₁-adrenergic** — sympathetic cardiac signaling via Gs → cAMP → PKA.
- **Bundle of His / right and left bundle branches / Purkinje fibers** — His–Purkinje conduction system.
- **Bundle of Kent** — WPW accessory pathway from atrium to ventricle.
- **Cardiac glycoside** — digoxin/digitalis; inhibits Na/K-ATPase.
- **Cav1.2** — cardiac L-type Ca²⁺-channel α₁; gene *CACNA1C*.
- **Cx43** — connexin 43, dominant gap-junction protein in working myocardium.
- **DAD / EAD** — delayed / early afterdepolarization (triggered activity).
- **Delta wave** — slurred QRS upstroke in WPW pre-excitation.
- **ECG (electrocardiogram)** — body-surface recording of cardiac extracellular potentials.
- **Einthoven's triangle / 12-lead ECG** — standard surface-recording geometry.
- **Effective refractory period (ERP)** — interval during which no propagating AP can be re-initiated; in cardiac muscle ≈ ARP.
- **Funny current ($I_f$)** — HCN4-mediated pacemaker current.
- **GIRK** — G-protein-coupled inwardly rectifying K⁺ channel (Kir3.x); mediates $I_{K,ACh}$.
- **hERG (Kv11.1, KCNH2)** — $I_{Kr}$ channel; LQT2 and drug-induced LQT locus.
- **HCN4** — pacemaker channel; ivabradine target.
- **$I_{Ca,L}$ / $I_{Ca,T}$** — L-type (Cav1.2) and T-type Ca²⁺ currents.
- **$I_{K1}$** — Kir2.1 inward-rectifier; sets resting potential in atrial/ventricular myocytes.
- **$I_{Kr}$ / $I_{Ks}$** — rapid (hERG) and slow (KCNQ1+KCNE1) delayed-rectifier K⁺ currents.
- **$I_{Na}$ / $I_{Na,late}$** — fast Nav1.5 current / persistent late component (LQT3 locus).
- **$I_{to}$** — Kv4.3 transient outward current (phase 1 notch).
- **Maximum diastolic potential** — most negative $V_m$ in pacemaker cells.
- **Mobitz type I (Wenckebach) / type II** — second-degree AV-block patterns.
- **NCX1 (SLC8A1)** — cardiac Na/Ca exchanger; electrogenic (3 Na : 1 Ca).
- **Pacemaker hierarchy** — SA (60 bpm) > AV (40 bpm) > Purkinje (20 bpm).
- **PR / QRS / QT / R–R intervals** — standard ECG intervals.
- **Phospholamban (PLN)** — SERCA inhibitor; relieved by PKA phosphorylation.
- **Re-entry** — closed-loop self-sustaining excitation.
- **RyR2** — cardiac SR Ca²⁺-release channel; CPVT locus.
- **SA / AV node** — sinoatrial (primary) and atrioventricular (secondary) pacemakers.
- **SERCA2a** — SR Ca²⁺-ATPase isoform of cardiac muscle.
- **Sinus arrhythmia** — respiration-coupled HR variation; normal.
- **Torsades de pointes** — polymorphic VT seen in LQTS.
- **Triggered activity** — EAD/DAD-driven ectopic firing.
- **Unidirectional block** — anatomical/functional substrate for re-entry.
- **Vagal maneuvers** — Valsalva, carotid sinus massage; ↑ parasympathetic tone, ↓ AV conduction.
- **Vaughan–Williams classes I–IV** — antiarrhythmic-drug taxonomy.
- **WPW (Wolff-Parkinson-White)** — pre-excitation syndrome with accessory pathway.

---

## Cross-links forward and back

| Link | Topic | Where |
|---|---|---|
| ← Excitable membrane biophysics | $m^3h$, voltage clamp, Hodgkin–Huxley | Ch 7 |
| ← Voltage-gated channel structure | Nav1.5, Cav1.2, hERG/KCNQ1 architecture | Ch 7 |
| ← Voltage-gated K⁺ channels & long QT | $I_{Kr}$, $I_{Ks}$, $I_{K1}$ | Ch 7 |
| ← Cardiomyocyte EC-coupling | Cav1.2 → RyR2 → SR Ca²⁺ → troponin C | Ch 9 |
| ← Autonomic nervous system | M₂ / β₁ signaling on the heart | Ch 14 |
| ← Cardiovascular organization | global anatomy / circulatory plan | Ch 17 |
| → The heart as a pump | EC-coupling → pressure–volume work | Ch 22 |
| → Regulation of arterial pressure and CO | baroreflex; chronotropy / inotropy | Ch 23 |
| → Integrated CV control | neurohumoral integration | Ch 25 |
| → K⁺ disturbances and the ECG | hyperkalemia / hypokalemia ECG changes | Ch 37 |
| → Adrenal medulla | catecholamine synthesis | Ch 50 |
| → Thyroid hormone & the heart | sinus tachycardia of hyperthyroidism | Ch 49 |
| ↔ Anesthetic / antiarrhythmic pharmacology | class I local anesthetic mechanism | Ch 7 (Fig. 7-14) |

---

## Source apparatus

- **Online Notes** referenced inline: N21-1 through N21-18 (channel architecture details, NCX1 stoichiometry, $I_{Na,late}$, $I_f$ structure, pacemaker math, atrial fibrillation epidemiology, AD/EAD mechanism, digitalis pharmacology).
- **Clinical boxes:** Box 21-1 (Vagal Maneuvers, p. 493), Box 21-2 (Basic Interpretation of the ECG, p. 498), Box 21-3 (Myocardial Infarction, p. 499).
- **Tables in source:** 21-1 (major cardiac currents), 21-2 (equilibrium potentials), 21-3 (electrical properties of cardiac tissues), 21-4 (conduction velocities), 21-5 (eightfold ECG-reading approach), 21-6 (heart-rate determination).
- **References** deferred to companion site (StudentConsult).

---

## Format-verification notes

**Figures viewed and described from image:** 21-1 (conduction pathways anatomy, p. 484), 21-2 (cardiac APs by cell type, p. 485), 21-3 (gap-junction current flow, p. 486), 21-5 (sequence of ventricular depolarization, p. 491), 21-7 (components of the ECG, p. 494), 21-15 (abnormal conduction and re-entry, p. 504). [Six figures viewed; one above the five-figure minimum to cover the chapter's three pillars — phases, ECG correspondence, and re-entry.]

**Figures listed by caption + textual reference only:** 21-4 (phases of cardiac APs), 21-6 (modulation of pacemaker activity), 21-8 (12-lead placement), 21-9 (axes of the limb leads), 21-10 (two-cell ECG model), 21-11 (normal 12-lead ECG), 21-12 (axis estimation), 21-13 (two-cell MI model), 21-14 (pathological ECG gallery), 21-16 (abnormal automaticity / EAD).

*End of Chapter 21. Next: Chapter 22 — The Heart as a Pump.*
