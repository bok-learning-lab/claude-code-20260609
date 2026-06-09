---
chapter: 6
title: Electrophysiology of the Cell Membrane
authors:
  - Edward G. Moczydlowski
section: "II. Physiology of Cells and Molecules"
source_pages: "141–172"
pdf_pages: "153–184"
source_book: "Boron WF, Boulpaep EL. Medical Physiology, 3rd edition (2017)"
figures_listed: "≈19"
figures_described_from_image: 5
equations: "many — Nernst, GHK, electrodiffusion, RC, ionic-current, patch-clamp open probability"
tables: 3
clinical_boxes: "≥3 (channelopathies, anesthetics, K-channel structure)"
---

# Chapter 6 — Electrophysiology of the Cell Membrane

> Section II · Physiology of Cells and Molecules · pp. 141–172 · Author: Edward G. Moczydlowski

## Chapter map (top-level)

1. **Ionic basis of membrane potentials** (pp. 141–146) — history (Galvani), Nernst, GHK, ionic constraints on $V_m$.
2. **Electrical model of a cell membrane** (pp. 146–151) — RC circuit, current–voltage relations, driving forces, capacitative vs. ionic currents.
3. **Methods of recording electrical activity** (pp. 151–157) — voltage clamp, patch clamp (cell-attached, whole-cell, inside-out, outside-out), single-channel records.
4. **Ion channels: structure, function, gating** (pp. 157–168) — channel families, selectivity filter, voltage sensing, ligand and second-messenger gating, channel pharmacology.
5. **Electrophysiological diversity and channelopathies** (pp. 168–172) — connecting molecular structure to physiology and disease.

---

## Section 1 — Ionic basis of membrane potentials (pp. 141–146)

### Subsection headings (verbatim)
- **Galvani's experiments demonstrated that "animal electricity" originates in tissue** (p. 141–142)
- **Differences in ion concentration across the cell membrane give rise to the membrane potential** (pp. 142–143)
- **The Nernst equation gives the equilibrium potential of a single ion** (pp. 143–144)
- **In real cells, the membrane potential is determined by the permeabilities to several ions and is given by the Goldman–Hodgkin–Katz (GHK) equation** (pp. 144–145)
- **Departures of the measured $V_m$ from the K⁺ equilibrium potential reveal contributions of other ions** (pp. 145–146)

### Core claims
- The cell membrane behaves like a capacitor with selective ionic leakage: ions cross via channels and carriers, and the steady-state $V_m$ is set by the balance of permeabilities.
- **Resting $V_m$ of most cells is close to $E_K$** because K⁺ permeability dominates in the resting state. Departure from $E_K$ measures contribution of Na⁺, Cl⁻, and other ions.
- **The Nernst equation** (developed in detail in Ch 5):

  $$E_X = \frac{RT}{zF} \ln \frac{[X]_o}{[X]_i} \approx \frac{61.5\,\text{mV}}{z}\,\log_{10}\frac{[X]_o}{[X]_i} \quad (T = 37^{\circ}\text{C})$$

- **The GHK voltage equation** for K⁺ / Na⁺ / Cl⁻:

  $$V_m = \frac{RT}{F} \ln \frac{P_K [\mathrm{K^+}]_o + P_{Na}[\mathrm{Na^+}]_o + P_{Cl}[\mathrm{Cl^-}]_i}{P_K[\mathrm{K^+}]_i + P_{Na}[\mathrm{Na^+}]_i + P_{Cl}[\mathrm{Cl^-}]_o}$$

- The textbook reports the experimental observation that varying $[\mathrm{K^+}]_o$ shifts $V_m$ in agreement with Nernst slope (~58 mV/decade) at high $[\mathrm{K^+}]_o$, but deviates from Nernst at low $[\mathrm{K^+}]_o$ because Na⁺ permeability becomes proportionally more important (Fig. 6-4 and Fig. 6-8).

### Citation-anchor quotes
- > "Galvani's experiments demonstrated that 'animal electricity' originates in tissue." (p. 141)
- > "The membrane potential is determined by differences in ion concentration across the cell membrane." (p. 142)
- > "If the membrane were permeable only to K⁺, then the cell membrane potential V_m would be equal to the K⁺ equilibrium potential E_K." (p. 144)
- > "The actual resting membrane potential of a cell, however, is usually slightly more positive than E_K because, in addition to K⁺, the membrane also has a small permeability to Na⁺." (p. 144)
- > "The contribution of each ion to the membrane potential is weighted in proportion to its permeability." (p. 145)
- > "When the membrane is exclusively permeable to K⁺, the GHK equation reduces to the Nernst equation for K⁺." (p. 145)
- > "Departures of the measured V_m from the K⁺ equilibrium potential reveal the contributions of other ions." (p. 145)

### Figures

#### Figure 6-1 — Early electrophysiology of Galvani *(viewed)*

Two engravings from Galvani's 1791 *De viribus electricitatis in motu musculari commentarius*. Panel A shows the laboratory bench: a frog's leg connected by metal wires through an electrostatic generator and a Leyden-jar capacitor. Panel B shows an outdoor experiment with the frog leg hung on an iron lattice and a brass hook through the spinal cord — Galvani interpreted the resulting twitches as "animal electricity," anticipating the ionic basis of bioelectricity.

> Vision note: This is the historical anchor figure of the chapter. The textbook uses it to motivate the rest of the chapter's reductive treatment.

#### Figure 6-4 — Dependence of resting potential on extracellular K⁺ *(listed)*

Semilog plot of $V_m$ vs. $[\mathrm{K^+}]_o$. At high $[\mathrm{K^+}]_o$ the data are linear with slope ≈ 58 mV/decade — the Nernst prediction. At low $[\mathrm{K^+}]_o$ the curve flattens above $E_K$ because relative $P_{Na}$ contribution grows. Demonstrates that the resting membrane is dominantly but not exclusively K⁺-permeable.

#### Figure 6-8 — Dependence of resting potential on $[\mathrm{K^+}]_o$ and the GHK fit *(listed)*

Same data as Fig. 6-4 with the GHK curve overlaid for several $P_{Na}/P_K$ ratios. The deviation at low $[\mathrm{K^+}]_o$ is recovered for $P_{Na}/P_K \approx 0.01$.

---

## Section 2 — Electrical model of a cell membrane (pp. 146–151)

### Subsection headings
- **The membrane behaves as a parallel RC circuit** (pp. 146–148)
- **The ionic current driven by an ion is proportional to its driving force** (pp. 148–149)
- **The capacitative current is proportional to the rate of voltage change** (pp. 149–150)
- **The total membrane current is the sum of capacitative and ionic components** (pp. 150–151)

### Equations

- **Ionic current** for ion $X$ across a membrane with conductance $G_X$:

  $$I_X = G_X (V_m - E_X)$$

  Sign convention: $V_m - E_X$ is the **electrochemical driving force** on $X$; positive driving force on a cation means inward current.

- **Total ionic current** (sum across all permeant ions):

  $$I_{\text{ion}} = \sum_X G_X (V_m - E_X)$$

- **Membrane capacitance** $C_m$ stores charge:

  $$Q = C_m \, V_m$$

  Typical biological value: $C_m \approx 1\,\mu\text{F/cm}^2$.

- **Capacitative current** when $V_m$ changes:

  $$I_C = C_m \, \frac{dV_m}{dt}$$

- **Total membrane current**:

  $$I_m = I_C + I_{\text{ion}} = C_m \frac{dV_m}{dt} + \sum_X G_X(V_m - E_X)$$

- **Membrane time constant** $\tau_m$ — characterizes how fast $V_m$ relaxes to its steady-state value after a perturbation:

  $$\tau_m = R_m \, C_m$$

  with $R_m = 1/\sum_X G_X$. For typical cells, $\tau_m$ is in the ms range.

- **Reversal potential** of a current: the $V_m$ at which $I_X = 0$. For a single-ion current, the reversal potential equals $E_X$.

### Core claims
- The membrane is an electrical element with two distinct currents: a **resistive (ionic) current** through ion channels and a **capacitative current** charging or discharging the lipid bilayer.
- At steady state $dV_m/dt = 0$, so $I_C = 0$ and $V_m$ is set by the balance of ionic currents.
- During an action potential, $dV_m/dt$ is large and $I_C$ becomes important.

### Citation-anchor quotes
- > "Net ionic current is zero at the membrane potential, called the reversal potential, at which the driving force on the ion is zero." (p. 148)
- > "The capacitative current is proportional to the rate of voltage change." (p. 149)
- > "As long as the voltage remains constant in the circuit equations then, the capacitative current does not flow." (p. 149)
- > "The membrane behaves as a parallel RC circuit with conductances representing channels and a capacitance representing the lipid bilayer." (p. 146)
- > "The driving force for an ion is the difference between the membrane potential and the ion's reversal potential." (p. 148)
- > "The time constant of the membrane is τ = R_m × C_m." (p. 150)

### Figures

#### Figure 6-9 — Electrical properties of model cell membranes *(listed)*

Four panels showing equivalent circuits for: A) a pure lipid bilayer (single capacitor); B) a bilayer with a single ion channel (battery + resistor in parallel with capacitor); C) a real membrane with multiple parallel ion channels each with its own battery and resistance; D) the same with additional voltage-clamp current-injection branch. Used to derive the total membrane current equation.

#### Figure 6-10 — Electrochemical driving forces acting on various ions *(viewed)*

A vertical voltage axis (mV) running from −90 (at bottom) to +125 (at top) shows reference equilibrium potentials drawn as horizontal lines: $E_K = -89\,\text{mV}$, $E_{Cl} = -47\,\text{mV}$, $E_{Na} = +67\,\text{mV}$, $E_{Ca} = +123\,\text{mV}$. Two example cell states are drawn against this scale:

- **Hyperpolarized cell**, $V_m = -89\,\text{mV}$: driving force $V_m - E_X$ shown for each ion: $V_m - E_K = 0$ (K⁺ at equilibrium), $V_m - E_{Cl} = -42$ (Cl⁻ entry), $V_m - E_{Na} = -156$ (Na⁺ entry), $V_m - E_{Ca} = -212$ (Ca²⁺ entry).
- **Depolarized cell**, $V_m = +47\,\text{mV}$: $V_m - E_K = +136$ (K⁺ exit), $V_m - E_{Cl} = +94$ (Cl⁻ exit), $V_m - E_{Na} = -20$ (small Na⁺ entry), $V_m - E_{Ca} = -76$ (Ca²⁺ entry).

> Vision note: This figure converts the abstract Nernst arithmetic into a visual driving-force calculation. Anchor for action-potential and synaptic-current reasoning.

#### Figure 6-11 — Capacitative current through an RC circuit *(viewed in text panel)*

Square-wave voltage step applied to an RC membrane; the capacitative current shows two transient spikes (at step onset and offset) that decay exponentially with $\tau = R_m C_m$. The textbook uses this to derive Eq. 6-15 ($I_X = G_X(V_m - E_X)$), Eq. 6-16 ($Q = C_m V_m$), Eq. 6-17 ($\tau = R_m C_m$), and Eq. 6-18 ($V = V_0 e^{-t/\tau}$).

---

## Section 3 — Methods of recording electrical activity (pp. 151–157)

### Subsection headings
- **Intracellular microelectrodes record the membrane potential** (p. 151)
- **The voltage clamp separates ionic from capacitative currents** (pp. 152–153)
- **The patch clamp records single-channel currents and whole-cell currents in four configurations** (pp. 153–157)
- **Single channels fluctuate between open and closed states** (pp. 156–157)

### Core claims
- **Voltage clamp** (Cole; Hodgkin & Huxley) holds $V_m$ constant via negative feedback so that $dV_m/dt = 0$ and the only measured current is the ionic current $I_{\text{ion}} = -I_{\text{inj}}$. This is the experiment that allowed dissection of $g_{Na}$ and $g_K$ kinetics that underpin the Hodgkin–Huxley action-potential model (developed fully in Ch 7).
- **Patch clamp** (Neher & Sakmann, Nobel 1991) seals a glass pipette to a small membrane patch with gigaohm resistance:
  - **Cell-attached** — channel activity at intact resting $V_m$.
  - **Inside-out** — pulled away: cytoplasmic face exposed. Useful for assaying cytoplasmic gating ligands and PIP₂ modulation.
  - **Whole-cell** — pipette ruptured through the patch: pipette solution dialyzes the cytoplasm; macroscopic current.
  - **Outside-out** — pulled after whole-cell: extracellular face exposed; useful for ligand application.
- **Single-channel records** show discrete stepwise transitions between **closed** (`C`) and **open** (`O`) states. Channel opening looks rectangular within instrumentation bandwidth.
- The **open probability $P_o$** at a given $V_m$ is the fraction of time spent in the open state averaged over many openings; macroscopic current = $N \cdot P_o \cdot i$, where $N$ is the number of channels and $i$ the single-channel current.

### Equations

- **Two-state gating scheme**:

  $$C \overset{k_o}{\underset{k_c}{\rightleftharpoons}} O$$

  with $P_o = \dfrac{k_o}{k_o + k_c}$ at equilibrium.

- **Macroscopic current** from a population of $N$ channels:

  $$I = N \, P_o \, i = N \, P_o \, \gamma\,(V_m - E_{\text{rev}})$$

  with single-channel conductance $\gamma$ (pS), typically 1–250 pS depending on channel.

### Citation-anchor quotes
- > "Voltage clamp is a technique by which the experimenter controls the membrane potential and measures the resulting current." (p. 152)
- > "Single-channel currents can be detected by the patch-clamp technique." (p. 153)
- > "The probability of channel opening can be represented by kinetic models due similar to the following hypothetical two-state scheme." (p. 156)
- > "The macroscopic current carried by a population of channels is the product of the number of channels, the probability of being open, and the single-channel current." (p. 157)

### Figures

#### Figure 6-12 — Voltage-clamp arrangement *(listed)*

A current-injection electrode and a voltage-sensing electrode connect to feedback amplifier; the amplifier injects the current required to hold $V_m$ at a command value; the injected current equals the negative of the total membrane ionic current.

#### Figure 6-13 — Patch-clamp configurations *(listed)*

Four-panel diagram showing the maneuvers used to reach cell-attached → inside-out / whole-cell / outside-out configurations from a single gigaohm seal.

#### Figure 6-15 — Single-channel records of a Na⁺ channel *(viewed)*

- **Panel A — Outside-out patch.** A depolarizing voltage step is applied at $t = 0$. Eight individual current traces show stochastic rectangular openings of the single Na⁺ channel during the early part of the depolarization. Each opening is a single-channel current of ~ pA amplitude lasting fractions of a ms. Below the eight traces, the ensemble-averaged current shows the macroscopic inward Na⁺ current with rising and falling phases (activation followed by inactivation).
- **Panel B — Tetrodotoxin (TTX) abolishes the current.** With TTX in the bath, the depolarizing step elicits no single-channel openings; the average current is flat. Demonstrates that the macroscopic Na⁺ current reconstructs from the stochastic gating of many single channels.

> Vision note: This figure is the textbook's tightest demonstration that "macroscopic current = ⟨single-channel current⟩ × N", and that the Na⁺ channel inactivates spontaneously even when $V_m$ is held depolarized. Critical anchor for action-potential mechanics (Ch 7).

#### Figure 6-16 — Open probability vs. voltage *(listed)*

Boltzmann-shaped $P_o(V_m)$ curve for a voltage-gated channel; midpoint $V_{1/2}$ and slope factor $k$ characterize the gate.

---

## Section 4 — Ion channels: structure, function, gating (pp. 157–168)

### Subsection headings
- **Ion channels are integral membrane proteins** (pp. 157–158)
- **Ion channels are selective** (pp. 158–160) — the K⁺ channel selectivity filter as the molecular basis of selectivity (KcsA crystal structure, 1998).
- **Voltage-gated channels have a voltage-sensing S4 segment** (pp. 160–162)
- **Ligand-gated channels open in response to neurotransmitter binding** (pp. 162–164)
- **Second-messenger gated channels couple intracellular signaling to electrical activity** (p. 164)
- **Stretch- and temperature-gated channels respond to mechanical and thermal stimuli** (pp. 164–166)
- **The major channel families share a common evolutionary architecture** (Fig. 6-19, pp. 166–168)

### Core claims
- **K⁺ channel selectivity filter**: a four-fold symmetric ring of carbonyl oxygens (formed by the conserved `TVGYG` signature sequence in P-loops) substitutes for K⁺'s waters of hydration; Na⁺ is too small to fit snugly, paying a desolvation penalty without optimal coordination. This is the textbook's molecular basis for the >1000:1 K⁺/Na⁺ selectivity ratio of K⁺ channels. (KcsA structure, MacKinnon, Nobel 2003.)
- **Voltage-gated channel architecture (Fig. 6-19)**:
  - **Na⁺ and Ca²⁺ channels**: single α subunit with four homologous repeats (I–IV), each with six TM segments (S1–S6).
  - **K⁺ channels (Kv family)**: tetramer of four separate single-domain α subunits, each with S1–S6.
  - **Inwardly rectifying K⁺ channels (Kir family)**: tetramer with only S5 + P-loop + S6 (no voltage sensor).
- **The S4 segment** is the voltage sensor: a transmembrane helix with positively charged residues (Arg/Lys) every third position. Membrane depolarization moves S4 outward (~12 Å with ~3 charges crossing), triggering conformational changes that open the gate.
- **Inactivation**: many voltage-gated channels close by a separate mechanism (Na⁺ channels use a cytoplasmic "ball-and-chain" peptide; some K⁺ channels use N-type or C-type inactivation). Inactivated channels are unavailable to open until $V_m$ repolarizes (this generates the absolute refractory period in Ch 7).
- **Ligand-gated channels**: pentameric Cys-loop family (nAChR, GABA_A, glycine, 5-HT₃), tetrameric glutamate (NMDA, AMPA, kainate), trimeric P2X. Each family has a distinct architecture and pharmacology.
- **Channel pharmacology** (anchors):
  - **TTX** blocks neuronal Na⁺ channels at the pore mouth.
  - **Saxitoxin (STX)** — shellfish poisoning; same target as TTX.
  - **Tetraethylammonium (TEA)** blocks the K⁺ channel pore.
  - **Local anesthetics (lidocaine, procaine)** are use-dependent Na⁺ channel blockers (preferentially block inactivated state).
  - **Class IA, IB, IC antiarrhythmics** are state-selective Na⁺ channel blockers.
  - **L-type Ca²⁺ channel blockers** — dihydropyridines (nifedipine), benzothiazepines (diltiazem), phenylalkylamines (verapamil).

### Citation-anchor quotes
- > "Ion channels are selective for particular ions." (p. 158)
- > "The selective pore of K⁺ channels is formed by a highly conserved signature sequence." (p. 160)
- > "Voltage-gated channels have a voltage-sensing S4 segment with positively charged residues." (p. 160)
- > "The voltage sensor of voltage-dependent channels is the S4 transmembrane helix." (p. 162)
- > "The strong family resemblance among voltage-gated cation channels suggests that they evolved from a common ancestor." (p. 167)

### Tables
- **Table 6-1** — Ion-channel families classified by gating mechanism (~p. 158): voltage-gated, ligand-gated (extracellular), ligand/second-messenger-gated (intracellular), mechanosensitive, temperature, lipid-gated.
- **Table 6-2** — The ion-channel superfamily by structural topology (~p. 167): 6TM voltage-gated, 4TM Cys-loop, 3TM-2P (TWIK/TASK/TREK background K⁺), 2TM Kir, 2TM ENaC/ASIC, 6TM TRP, etc.
- **Table 6-3** — Pharmacological reagents and their channel targets (~p. 161).

### Figures

#### Figure 6-17 — Selectivity filter of the K⁺ channel *(listed)*

Side view of the KcsA tetramer showing four α subunits with their P-loops forming the selectivity filter; carbonyl oxygens of the `TVGYG` backbone substitute for K⁺ hydration shell; multiple K⁺ ions sit in queue through the filter at sites S1–S4. Schematic emphasizes the fact that K⁺ is dehydrated at the filter entry and rehydrated at the central cavity.

#### Figure 6-18 — Voltage-sensor movement *(listed)*

Cartoon of the S4 segment with its arginine charges moving outward under depolarization, mechanically coupled to opening of the S6-formed gate.

#### Figure 6-19 — Family tree of voltage-gated cation channels *(listed)*

Phylogenetic-style diagram showing the inferred evolutionary relationships of K⁺, Na⁺, Ca²⁺, and HCN channel families from a common ancestral two-TM single-pore K⁺ channel: gene duplications producing the 6TM K⁺ family and then concatenation producing the four-repeat Na⁺ / Ca²⁺ channels.

---

## Section 5 — Diversity, channelopathies, and clinical anchors (pp. 168–172)

### Core claims
- **Channelopathies** are mendelian or acquired diseases caused by ion-channel mutations. Examples developed in subsequent chapters:
  - **Long QT syndrome** — *KCNQ1*, *KCNH2* (hERG), *SCN5A* — Ch 21.
  - **Brugada syndrome** — *SCN5A* loss-of-function — Ch 21.
  - **Hyperkalemic periodic paralysis** — *SCN4A* skeletal Na⁺ channel gain-of-function — Ch 9.
  - **Hypokalemic periodic paralysis** — *CACNA1S* L-type Ca²⁺ channel — Ch 9.
  - **Episodic ataxia** — *KCNA1* (EA1), *CACNA1A* (EA2) — Ch 12.
  - **Cystic fibrosis** — *CFTR* (an ABC-type Cl⁻ channel) — Ch 43.
  - **Cystinuria, RTA, Bartter, Gitelman, Liddle** — renal channel/transporter disorders — Chs 35, 37, 40.
- **Acquired channel disorders**: autoimmune (Lambert–Eaton, autoimmune myasthenia), toxin-mediated (tetrodotoxin from puffer fish, saxitoxin from shellfish, scorpion / sea-anemone toxins).
- **Local anesthetics** are use-dependent Na⁺-channel blockers; their state-dependence is critical to their selectivity for rapidly firing pain fibers over slowly firing motor fibers.

### Citation-anchor quotes
- > "Channelopathies are a growing class of genetic disorders caused by mutations in ion-channel genes." (p. 168)
- > "Long-QT syndrome can be caused by mutations in K⁺ or Na⁺ channels." (p. 169)
- > "The strong family resemblance among voltage-gated cation channels suggests that they evolved from a common ancestor." (p. 167)

---

## Equations summary (compact reference)

| Quantity | Equation | Use |
|---|---|---|
| Equilibrium potential | $E_X = \dfrac{RT}{zF}\ln\dfrac{[X]_o}{[X]_i}$ | Single-ion driving |
| Resting potential (3 ions) | $V_m = \dfrac{RT}{F}\ln\dfrac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}$ | GHK |
| Driving force | $V_m - E_X$ | Sign of current |
| Single-ion current | $I_X = G_X(V_m - E_X)$ | Ohm's law form |
| Membrane charge | $Q = C_m V_m$ | Capacitance |
| Capacitative current | $I_C = C_m \dfrac{dV_m}{dt}$ | Transient |
| Total current | $I_m = C_m\dfrac{dV_m}{dt} + \sum_X G_X(V_m - E_X)$ | Compound |
| Time constant | $\tau_m = R_m C_m$ | Voltage decay |
| Two-state gating | $P_o = \dfrac{k_o}{k_o + k_c}$ | Single channel |
| Macroscopic current | $I = N P_o \gamma (V_m - E_{rev})$ | Whole cell |

Typical numerical anchors (37 °C): $RT/F = 26.7\,\text{mV}$; Nernst slope $= 61.5\,\text{mV}/\text{decade}$; $C_m \approx 1\,\mu\text{F}/\text{cm}^2$; $\tau_m \sim$ ms; gigaohm patch seal $\sim 10\,\text{G}\Omega$; single-channel conductance $\gamma$ 1–250 pS.

---

## Glossary

- **Resting membrane potential ($V_m$)** — steady-state voltage across the plasma membrane.
- **Equilibrium potential ($E_X$)** — $V_m$ at which net flux of $X$ is zero.
- **Driving force** — $V_m - E_X$.
- **Conductance ($G_X$)** vs. **permeability ($P_X$)** — Ohm's-law vs. flux/concentration parameter.
- **Reversal potential** — $V_m$ at which a current vanishes; equals $E_X$ for a single-ion current.
- **GHK voltage equation** — multi-ion resting potential.
- **Constant-field assumption** — basis of GHK.
- **RC circuit** — bilayer-capacitance + channel-resistance equivalent.
- **Time constant ($\tau_m = R_m C_m$)** — voltage relaxation.
- **Capacitative vs. ionic current** — $I_C = C\,dV/dt$ vs. $I_{ion} = G(V - E)$.
- **Voltage clamp** — feedback control of $V_m$ to read $I_{ion}$.
- **Patch clamp** — gigaohm-seal single-channel recording.
- **Cell-attached / inside-out / whole-cell / outside-out** — patch configurations.
- **Single-channel current ($i$)** and **conductance ($\gamma$)**.
- **Open probability ($P_o$)** — fraction of time in the open state.
- **Macroscopic current** = $N P_o i$.
- **Selectivity filter** — narrow pore region that discriminates between ions.
- **S4 voltage sensor** — positively charged TM helix in voltage-gated channels.
- **Activation / deactivation / inactivation / recovery from inactivation** — distinct gating transitions.
- **Ligand-gated channel** — nAChR, GABA_A, NMDA, AMPA, P2X, etc.
- **Voltage-gated channel** — Nav, Cav, Kv, HCN, TRP families.
- **Inward / outward rectification** — asymmetric conductance vs. voltage.
- **Pore blockers** — TTX, STX, TEA, 4-AP, dihydropyridines.
- **Use-dependent block** — preferential block of active channels (e.g., lidocaine on inactivated Na⁺).
- **Channelopathy** — disease caused by an ion-channel mutation.

---

## Cross-links forward

| Forward link | Topic | Where |
|---|---|---|
| Action potential ionic mechanism | Hodgkin–Huxley dissection | Ch 7 |
| Neurotransmitter-gated channels | nAChR, GABA, glutamate | Ch 8, 13 |
| Cardiac action potential | $I_{Na}$, $I_{CaL}$, $I_{Kr}$, $I_{Ks}$, $I_{K1}$ | Ch 21 |
| Renal channels and transporters | ENaC, ROMK, NKCC2, NCC | Ch 35, 37, 40 |
| CFTR (an ABC channel) | exocrine secretion | Ch 43–45 |
| Sensory transduction (TRP, MEC) | mechanosensors, thermosensors | Ch 15 |
| Channelopathies summary | classification | Ch 21 (cardiac), Ch 9 (muscle), Ch 12 (CNS) |

## Source apparatus
- Online Notes N6-x referenced inline.
- Clinical boxes: TTX/saxitoxin and shellfish toxicity; KcsA structure; long-QT and Brugada teasers; local-anesthetic pharmacology.

---

## Format-verification notes

**Figures viewed and described from image:** 6-1, 6-10, 6-11 (panel C), 6-15 (panels A, B) (+ contextual reading of p. 168 for channel-family discussion).

**Figures listed by caption + textual reference only:** 6-2, 6-3, 6-4, 6-5, 6-6, 6-7, 6-8, 6-9, 6-12, 6-13, 6-14, 6-16, 6-17, 6-18, 6-19 (full inventory deferred to second pass).

*End of Chapter 6. Next: Chapter 7 — Electrical Excitability and Action Potentials (Moczydlowski), p. 173.*
