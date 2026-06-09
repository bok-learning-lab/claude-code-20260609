---
chapter: 12
title: Physiology of Neurons
authors:
  - Barry W. Connors
section: "III. The Nervous System"
source_pages: "295–306"
pdf_pages: "307–318"
source_book: "Boron WF, Boulpaep EL. Medical Physiology, 3rd edition (2017)"
figures_listed: "≈10"
figures_described_from_image: 5
equations: "cable theory; length and time constants; AP-initiation threshold; firing-rate Hill"
tables: 1
clinical_boxes: "≥2 (episodic ataxia 1; demyelination/MS)"
---

# Chapter 12 — Physiology of Neurons

> Section III · The Nervous System · pp. 295–306 · Author: Barry W. Connors

## Chapter map (top-level)

1. **Diversity of neuronal firing patterns** (pp. 295–297) — regular-spiking, fast-spiking, bursting, intrinsically rhythmic.
2. **Passive properties: membrane time and length constants** (pp. 297–299) — cable theory in compact neurons.
3. **Dendritic integration of synaptic inputs** (pp. 299–302) — temporal and spatial summation; attenuation; active dendrites.
4. **Action-potential initiation at the axon initial segment (AIS)** (pp. 302–304) — biophysical reasons; AIS plasticity.
5. **Firing-rate codes and channel-mediated modulation** (pp. 304–306) — frequency–current curves; spike-frequency adaptation; afterhyperpolarization.

---

## Section 1 — Diversity of neuronal firing patterns (pp. 295–297)

### Subsection headings
- **Different classes of neurons display characteristic firing patterns in response to sustained current injection** (p. 295)
- **Firing patterns reflect the complement of ion channels expressed** (pp. 296–297)

### Core claims — firing pattern catalog (Table 12-1 territory)

| Firing pattern | Typical cell | Distinguishing features | Key channels |
|---|---|---|---|
| **Regular-spiking (RS)** | cortical pyramidal | adapting train at moderate rates | small-conductance Ca²⁺-activated K⁺ (SK), Kv7 (M-current) |
| **Fast-spiking (FS)** | cortical PV+ interneurons, RVLM, cerebellar Purkinje | very narrow APs (<0.5 ms), little adaptation | Kv3.1/3.2 (fast K⁺), Nav1.1 |
| **Intrinsically bursting (IB)** | layer-V pyramidal, thalamic relay (rebound), cerebellar dentate | clustered APs riding on slow Ca²⁺ or persistent Na⁺ depolarizations | Cav3 (T-type), Nav persistent, HCN |
| **Chattering** | layer-II/III cortex (cat visual cortex) | rhythmic high-frequency bursts | as IB; cortically described first |
| **Low-threshold spike (LTS)** | somatostatin+ cortical interneurons; thalamic relay neurons | rebound burst after hyperpolarization | Cav3 T-type, HCN |

### Citation-anchor quotes
- > "Different classes of neurons display characteristic firing patterns when given a sustained depolarizing current." (p. 295)
- > "The diverse firing patterns reflect the diverse complement of voltage-gated channels expressed." (p. 296)
- > "Thalamic relay neurons can fire in tonic or burst mode depending on their membrane potential." (p. 296)

### Figures

#### Figure 12-1 — Firing patterns of cortical neurons *(listed)*

Four traces of $V_m$ vs. time from a regular-spiking pyramidal neuron, a fast-spiking interneuron, an intrinsically bursting pyramidal neuron, and a low-threshold-spiking interneuron, each in response to the same current step. Each shows the canonical signature: adaptation in RS, narrow non-adapting APs in FS, clustered bursts in IB, rebound burst after hyperpolarization in LTS.

#### Figure 12-2 — Two firing modes of thalamic relay neurons *(listed)*

Top: tonic firing in response to depolarizing current from a normal resting potential. Bottom: same current applied from a hyperpolarized starting potential — single low-threshold T-type Ca²⁺ spike crowned by a burst of Na⁺ APs. Anchor for the EEG distinction between awake/tonic-relay and slow-wave-sleep/burst-relay modes.

---

## Section 2 — Passive properties and cable theory (pp. 297–299)

### Subsection headings
- **Subthreshold voltage signals in a neuron decay with characteristic time and length constants** (pp. 297–298)
- **Synaptic potentials attenuate as they propagate from dendrite to soma** (pp. 298–299)

### Equations (developed in Ch 7; applied here to compact neurons)

- **Cable equation** (one-dimensional dendrite of constant diameter):

  $$\lambda^2 \frac{\partial^2 V}{\partial x^2} - \tau_m \frac{\partial V}{\partial t} - V = 0$$

- **Length constant**:

  $$\lambda = \sqrt{\dfrac{R_m \, d}{4\,R_i}}$$

  where $R_m$ = specific membrane resistance (Ω·cm²), $R_i$ = axoplasmic resistivity (Ω·cm), $d$ = dendrite diameter (cm). Larger diameter $\to$ longer $\lambda$.

- **Time constant**:

  $$\tau_m = R_m \, C_m$$

  with $C_m$ = specific membrane capacitance (~1 μF/cm²).

- **Steady-state voltage decay** with distance:

  $$V(x) = V_0 \, e^{-x / \lambda}$$

- **Transient voltage decay** in time after current cutoff:

  $$V(t) = V_0 \, e^{-t / \tau_m}$$

### Core claims
- A localized depolarization (EPSP) injected at a dendritic spine generates a small *local* depolarization that **attenuates as it propagates** toward the soma.
- The faster the EPSP (small $\tau$), the more it attenuates over a given electrotonic distance — high-frequency synaptic inputs reach the soma poorly along a passive cable. This is why **dendritic active conductances** (voltage-gated Na⁺ and Ca²⁺ channels in dendrites) are critical: they allow EPSPs to regenerate, **boosting** their amplitude as they travel toward the soma, sometimes producing dendritic spikes.
- A neuron's **electrotonic length** $L = l/\lambda$ (where $l$ is real dendritic length) determines integration: $L \lesssim 1$ → "compact" neuron (all dendritic synapses equally weighted); $L \gg 1$ → "long" dendrite (distal synapses heavily filtered, needing active boosting).

### Citation-anchor quotes
- > "Subthreshold voltage signals decay over space and time according to the passive cable properties of the dendrite." (p. 297)
- > "Synaptic potentials decrease in amplitude as they spread from their site of origin to the soma." (p. 298)
- > "The length constant λ is large for large-diameter processes and high membrane resistance." (p. 298)

### Figures

#### Figure 12-3 — Attenuation of EPSPs in dendrites *(viewed)*

- **Panel A — Attenuation of EPSPs in dendrites.** A cartoon dendritic tree with an EPSP injected at three increasing electrotonic distances from the soma ($L = 0$, $L = 1$, $L = 2$). At the injection site, all three EPSPs have the same amplitude (rise time identical). The resulting somatic EPSPs (recorded at the cell body) are progressively smaller and broader as $L$ increases — confirming the cable-theory prediction that distal synapses contribute less to somatic potential than proximal ones, all else being equal.
- **Panel B — Attenuation of voltage along a passive cable.** Graph of $V/V_0$ as a function of normalized distance $x/\lambda$. Two curves: a steady-state ($t \to \infty$) curve following $e^{-x/\lambda}$ (red, "Steady"); a higher-frequency oscillation case that decays much more steeply with distance. Demonstrates that high-frequency (fast) EPSPs attenuate more than slow ones.

> Vision note: This is the textbook's most compact distillation of passive cable theory applied to real neurons. Anchor for any RAG query on dendritic integration, voltage attenuation, or rationale for active dendritic conductances.

#### Figure 12-4 — Frequency-dependent attenuation *(listed)*

Plot of attenuation factor vs. input frequency for sinusoidal injection at fixed distance: the cable acts as a low-pass filter — slowly varying inputs reach the soma nearly intact; rapidly varying inputs are heavily filtered.

---

## Section 3 — Dendritic integration (pp. 299–302)

### Subsection headings
- **EPSPs and IPSPs sum in space and time at the soma** (pp. 299–300)
- **Temporal summation depends on the time constant; spatial summation depends on the length constant** (p. 300)
- **Inhibition shunts excitation** (pp. 300–301)
- **Active dendritic conductances boost distal inputs and can produce dendritic spikes** (pp. 301–302)

### Core claims
- **Temporal summation**: two EPSPs arriving within $\sim \tau_m$ of each other add (linearly for small signals).
- **Spatial summation**: two EPSPs occurring simultaneously at different dendritic sites add at the soma (linearly for small signals; sublinearly when local saturation or shunting interferes).
- **Shunting inhibition**: opening Cl⁻ channels (GABA_A) near $E_{Cl} \approx V_m$ adds little voltage change but **lowers $R_m$ locally**, "shunting" current away from incoming excitation. Effect on EPSPs that pass through the shunted region is greater than the small Cl⁻-driven hyperpolarization alone.
- **Active dendritic conductances**:
  - **Voltage-gated Na⁺ channels** in dendrites support **backpropagating APs** from soma to dendrite — important for spike-timing-dependent plasticity (Ch 13).
  - **NMDA receptors** are themselves voltage-gated by their Mg²⁺ block; their coincidence-detection function is the canonical "AND" gate of dendritic computation.
  - **Voltage-gated Ca²⁺ channels** in tuft dendrites can produce regenerative Ca²⁺ spikes (Layer V pyramidal neurons) that bind distal apical inputs to proximal basal inputs — basis for two-compartment dendritic integration in cortex.
  - **HCN channels** ($I_h$) are graded along apical dendrites with higher density distally; they reduce $\tau_m$ and equalize the temporal integration of inputs across dendritic locations.

### Citation-anchor quotes
- > "EPSPs sum in time and in space at the soma." (p. 299)
- > "Inhibitory inputs can shunt excitatory currents even when they cause little hyperpolarization." (p. 300)
- > "Active conductances in dendrites can boost the influence of distal synaptic inputs." (p. 301)
- > "Backpropagating action potentials provide a global depolarizing signal that can interact with synaptic inputs throughout the dendritic tree." (p. 302)

---

## Section 4 — Action potential initiation at the axon initial segment (pp. 302–304)

### Subsection headings
- **The axon initial segment has the lowest threshold for AP initiation in the neuron** (pp. 302–303)
- **The AIS clusters voltage-gated Na⁺ channels at high density via ankyrin-G scaffolding** (p. 303)
- **AIS position and length are plastic and modulated by neuronal activity** (pp. 303–304)

### Core claims
- The **axon initial segment (AIS)** is the ~20–60 μm long axon segment immediately distal to the axon hillock. It has the **highest density of voltage-gated Na⁺ channels** (Nav1.6 — low-threshold; Nav1.2 — high-threshold) in the neuron — typically 50–100× higher than the soma.
- Consequence: even though a depolarizing wave from dendrites arrives at the soma first, the AIS reaches threshold first because of the high local channel density. The AP propagates orthodromically down the axon and antidromically (backpropagating) into the soma and dendrites.
- **Molecular organization**: ankyrin-G is the master scaffold; it tethers Nav channels, KCNQ2/3 K⁺ channels, βIV-spectrin, and other components into a stable AIS complex. Disruption of ankyrin-G (in some epilepsy mutations) destabilizes the AIS.
- **Activity-dependent AIS plasticity**: chronic depolarization causes the AIS to migrate distally and/or shorten — reducing excitability. Chronic silencing has the opposite effect. The AIS is now considered a major homeostatic excitability regulator.

### Citation-anchor quotes
- > "The axon initial segment has the lowest threshold for action potential initiation." (p. 302)
- > "Voltage-gated Na⁺ channels are clustered at very high density in the axon initial segment." (p. 303)
- > "Ankyrin-G is the master organizer of the AIS." (p. 303)

---

## Section 5 — Firing-rate codes and modulation (pp. 304–306)

### Subsection headings
- **The frequency–current (f–I) relationship encodes input intensity as firing rate** (pp. 304–305)
- **Spike-frequency adaptation is mediated by Ca²⁺-activated K⁺ channels and Kv7/M-current** (p. 305)
- **Afterhyperpolarization (AHP) has fast, medium, and slow components** (pp. 305–306)
- **Neuromodulators control firing-pattern transitions** (p. 306)

### Core claims
- **f–I curve**: firing rate (f) vs. injected current (I) for an integrate-and-fire neuron is roughly linear above rheobase; saturation occurs at high I when refractory period limits maximum rate.
- **Spike-frequency adaptation**: instantaneous firing rate is highest just after stimulus onset, then declines toward a steady-state lower rate. Mechanisms:
  - **SK channels** (small-conductance Ca²⁺-activated K⁺) carry the **medium AHP (mAHP)**.
  - **Kv7 (KCNQ2/3) M-current** is a slowly activating, non-inactivating K⁺ current that integrates over many APs.
  - **BK channels** (large-conductance Ca²⁺ + voltage-activated K⁺) carry the **fast AHP (fAHP)** immediately after each AP.
  - **Slow AHP (sAHP)**: large, prolonged hyperpolarization following a burst; carrier identity still debated (KCNN family with calmodulin sensors).
- **Neuromodulation**: noradrenaline (via β-adrenergic → cAMP → PKA), ACh (via M1 muscarinic → IP₃ → DAG → PKC), and 5-HT can suppress SK, Kv7, and sAHP currents, switching neurons from adapting to non-adapting firing — the cellular correlate of arousal, attention, and slow-wave sleep transitions.

### Box references
- **Episodic ataxia type 1** — KCNA1 (Kv1.1) loss-of-function in cerebellar Purkinje neurons → broadened APs and altered firing → episodic ataxia and myokymia.
- **Multiple sclerosis** — demyelination of CNS axons → conduction block, slowed conduction, ectopic firing, ephaptic interactions. **Dalfampridine (4-aminopyridine)** is a Kv1 blocker that broadens APs to compensate for the slower depolarizations of demyelinated nodes — improves walking speed in some MS patients.

### Citation-anchor quotes
- > "The firing rate of a neuron encodes the intensity of its input." (p. 304)
- > "Spike-frequency adaptation reduces firing rate during a sustained stimulus." (p. 305)
- > "The afterhyperpolarization following an action potential has fast, medium, and slow components." (p. 305)
- > "Neuromodulators can suppress the afterhyperpolarization and shift a neuron from adapting to tonic firing." (p. 306)

---

## Equations summary

| Quantity | Equation | Use |
|---|---|---|
| Cable length constant | $\lambda = \sqrt{R_m d / 4 R_i}$ | dendritic decay |
| Membrane time constant | $\tau_m = R_m C_m$ | temporal integration |
| Voltage decay (space) | $V(x) = V_0 e^{-x/\lambda}$ | passive dendrite |
| Voltage decay (time) | $V(t) = V_0 e^{-t/\tau_m}$ | EPSP relaxation |
| Electrotonic length | $L = l/\lambda$ | compact vs. extended neuron |
| f–I relationship | $f = G \cdot (I - I_{rheo})$ (above rheobase) | rate coding |
| Adapting firing | $f(t) = f_\infty + (f_0 - f_\infty)e^{-t/\tau_{adapt}}$ | SK / M-current adaptation |

Typical numbers: $C_m \approx 1\,\mu\text{F/cm}^2$; $R_m$ varies $10^3$–$10^5$ Ω·cm² (gating-dependent); $R_i \approx 100\,\Omega\,\text{cm}$; resulting $\tau_m \approx 10$–$100\,\text{ms}$ for many neurons; $\lambda \approx 0.1$–$1\,\text{mm}$ for typical apical dendrites.

---

## Glossary

- **Regular-spiking (RS) / fast-spiking (FS) / intrinsically bursting (IB) / low-threshold-spiking (LTS) / chattering** — firing-pattern classes.
- **Tonic vs. burst mode** (thalamic relay).
- **Cable equation** / $\lambda$ / $\tau_m$ / electrotonic length $L$.
- **Temporal vs. spatial summation**.
- **Shunting inhibition** — Cl⁻ conductance lowers local $R_m$.
- **Active dendritic conductances** — Nav, Cav, NMDAR, HCN in dendrites.
- **Backpropagating AP** — soma-to-dendrite signal supporting STDP.
- **NMDA receptor coincidence detection** — Mg²⁺-block voltage gating + ligand gating.
- **Dendritic Ca²⁺ spike** — local regenerative dendritic event.
- **Axon initial segment (AIS)** — site of AP initiation.
- **Nav1.6 / Nav1.2 / Kv7 / KCNQ / Ankyrin-G / βIV-spectrin** — AIS molecular components.
- **AIS plasticity** — homeostatic excitability regulation.
- **f–I curve / rheobase / gain (G)** — firing-rate code.
- **Adapting vs. non-adapting firing**.
- **fAHP / mAHP / sAHP** — afterhyperpolarization components.
- **SK / BK / Kv7 / M-current** — adaptation channels.
- **Neuromodulator-induced adaptation switch** — NE, ACh, 5-HT effects.
- **Episodic ataxia type 1 (KCNA1) / multiple sclerosis / dalfampridine** — clinical anchors.

---

## Cross-links forward

| Forward link | Topic | Where |
|---|---|---|
| Central synaptic transmission (NMDA/AMPA, GABA, glycine) | builds on dendritic integration | Ch 13 |
| Autonomic nervous system | f-I curves of cardiac autonomic outflow | Ch 14 |
| Sensory transduction | photoreceptors as graded-potential cells | Ch 15 |
| CNS circuits | thalamocortical integration, sleep | Ch 16 |
| Cardiac and skeletal channelopathies | similar logic applied to muscle/heart | Ch 7, 21 |
| Cerebellar Purkinje firing patterns | episodic ataxia 2 (CACNA1A) | Ch 16 |

## Source apparatus
- Online Notes N12-x referenced inline.
- Clinical boxes: episodic ataxia 1; multiple sclerosis and 4-AP / dalfampridine.

---

## Format-verification notes

**Figures viewed and described from image:** 12-3 (+ contextual reading of p. 298 for cable-theory narrative).

**Figures listed by caption + textual reference only:** 12-1, 12-2, 12-4 through 12-10 (full inventory deferred to second pass).

*End of Chapter 12. End of batch (Ch 8–12). Next: Chapter 13 — Synaptic Transmission in the Nervous System (Connors), p. 307.*
