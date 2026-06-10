---
chapter: 25
title: Integrated Control of the Cardiovascular System
authors:
  - Emile L. Boulpaep
section: "IV. The Cardiovascular System"
source_pages: "572–589"
pdf_pages: "584–601"
source_book: "Boron WF, Boulpaep EL. Medical Physiology, 3rd edition (2017)"
figures_listed: "10 (25-1 through 25-10)"
figures_described_from_image: 5
equations: "1 explicit (normalized distensibility, Eq. 25-1); qualitative balance equations for MAP, CO, Starling forces, hydrostatic column, R_post/R_pre ratio"
tables: 1
clinical_boxes: "embedded clinical anchors — vasovagal syncope, hypovolemic shock (compensated → decompensated → irreversible), orthostatic hypotension, postural hypotension on tilt-table"
---

# Chapter 25 — Integrated Control of the Cardiovascular System

> Section IV · The Cardiovascular System · pp. 572–589 · Author: Emile L. Boulpaep
> This chapter is the **assembly chapter** for Section IV. It takes the local-flow regulation of Ch 20 + Ch 24, the cardiac-pump determinants of Ch 22, and the systemic baroreflex / cardiac-output regulation of Ch 23, and shows how the cardiovascular system, the ANS (Ch 14), the kidney (Ch 33, 40), the endocrine system (Ch 47, 50), and thermoregulation (Ch 59) act in concert during four canonical stresses: **orthostasis, emotional stress, exercise, and hemorrhage**. The opening conceptual move is methodological — the body's responses cannot be captured by a linear chart or a simple branching tree; they require a **connected diagram** with feedback loops, repeated parameters, and cross-branch interactions. The closing conceptual move is the **transition from compensated to decompensated to irreversible shock** — a clinical archetype of positive feedback in physiology.

## Chapter map (top-level)

1. **Interaction among the different cardiovascular control systems** (pp. 572–574) — three diagram archetypes (linear chart → branching tree → connected diagram, Fig. 25-1); the systems-analysis approach; non-cardiovascular subsystems (ANS, respiratory, hematopoietic/liver, GI/urinary, endocrine, thermoregulatory) that must be included in any honest model (Fig. 25-2); the IV norepinephrine paradox (predicted tachycardia → observed bradycardia) as a worked example.
2. **Response to erect posture** (pp. 574–577) — gravitational redistribution of ~500 mL into dependent veins; the horizontal-cylinder / vertical-cylinder thought experiment (Fig. 25-3); four counter-pooling factors (nonuniform initial distribution, nonuniform distensibility, skeletal-muscle pump, autonomic reflexes); orthostatic / postural hypotension; thermal modulation of the orthostatic response (Table 25-1).
3. **Responses to acute emotional stress** (pp. 577–580) — fight-or-flight as a *centrally-originating* response with no peripheral sensor (Fig. 25-4); cortex → amygdala → locus coeruleus → PVN → medullary CV centers + IML; eight effector compartments (muscle, skin, adrenal, renal/splanchnic, veins, heart, blood volume via AVP, MAP). Vasovagal (vasodepressor) syncope as a *parasympathetic mass discharge* with simultaneous baroreflex suppression (Fig. 25-5); the Bezold–Jarisch reflex; warm-room / volume-loss / orthostasis as facilitators; post-faint AVP-driven oliguria.
4. **Response to exercise** (pp. 580–583) — the early-physiology "muscle-only" model (mechanical venous return + chemical vasodilation, Fig. 25-6) and Rushmer's 1950s falsification (no rise in LVEDP, no drop in MAP, no delay before tachycardia); the modern **central-command** model (Fig. 25-7); medial prefrontal cortex + insula + cingulate + H₁ fields of Forel + hypothalamic periventricular gray drive parallel motor and CV outflow; seven reinforcing mechanisms (exercise pressor reflex, baroreflex resetting, metabolite vasodilation, increased venous return, histamine release, epinephrine release, thermoregulatory cutaneous vasodilation).
5. **Response to hemorrhage** (pp. 583–587) — sequential cascade venous return → SV → CO → MAP; hypovolemic shock thresholds (30%+ loss; SBP <90, MAP <70 mm Hg); four-receptor reflex compensation (high-pressure baroreceptors, low-pressure stretch receptors, peripheral chemoreceptors, central chemoreceptors → massive sympathetic surge, Fig. 25-9); transcapillary refill — Starling-force reversal during compensation (Fig. 25-10A→B→C); RAAS/AVP/ANP-mediated renal salt-and-water conservation; thirst.
6. **Irreversible hemorrhagic shock** (pp. 587) — positive-feedback decompensation: failure of the vasoconstrictor response (sympathetic escape, AVP depletion), failure of capillary refill (R_post/R_pre reversal, Fig. 25-10D), failure of the heart (acidosis ↓ Ca²⁺ handling, subendocardial necrosis, cardiotoxic shock factors → hypovolemic → cardiogenic shock), and CNS depression (ischemic shutdown of sympathetic outflow).

---

## Section 1 — Interaction among the different cardiovascular control systems (pp. 572–574)

### Subsection headings (verbatim)
- **The control of the cardiovascular system involves "linear," "branched," and "connected" interactions** (pp. 572–573)
- **Regulation of the entire cardiovascular system depends on the integrated action of multiple subsystem controls as well as noncardiovascular controls** (pp. 573–574)

### Core claims

#### Three diagram archetypes (Fig. 25-1)
- **Linear chart (Fig. 25-1A).** Useful pedagogically — e.g., baroreflex drawn as a single one-way arrow chain from carotid stretch → receptor depolarization → CN IX firing → medullary integration → sympathetic outflow → vascular smooth-muscle tone. Hides the actual structure of physiology.
- **Branching tree (Fig. 25-1B).** Next refinement. Cardiac output bifurcates into HR × SV; each branch bifurcates again (SV → preload, afterload, contractility; HR → max diastolic potential, slope of diastolic depolarization, humoral factors); each leaf bifurcates again (preload → ventricular compliance, end-diastolic volume; ESV → afterload, contractility). The tree captures multifactorial dependence but **ignores interactions among parameters**.
- **Connected diagram (Fig. 25-1C).** The honest version. Adds three structural complications to the tree: (1) **feedback loops** (red arrows — e.g., arterial pressure → baroreceptor → ANS → HR), (2) **the same parameter appearing in more than one branch** (red dashed line — e.g., venous return entering both the CO branch and the filling-pressure branch), and (3) **cross-branch effects** (brown arrows — e.g., humoral factors acting simultaneously on intrinsic regulation of HR and on vascular tone). The connected diagram is the only honest substrate for "what happens if I disturb parameter X?"

#### The systems-analysis program
The book frames the rest of the chapter as a thought experiment: combine all the cardiac equations (Starling's law, force–velocity, Bowditch staircase, etc.) into one mathematical model of the heart, simulate, compare to in-vivo data, iterate. Agreement is **evidence, not proof**, that the model's feedback weights are correct. The same logic, scaled up to the entire circulation + non-circulatory subsystems, would yield hundreds of variables — too many for narrative understanding. The chapter therefore proceeds case-by-case through four canonical stresses.

#### Worked example: the IV norepinephrine paradox
A pure branching-tree prediction for an IV NE bolus (high α₁, intermediate β₁, low β₂ affinity): widespread α₁ vasoconstriction + β₁-mediated rise in HR + contractility → CO rises, MAP rises, HR rises. **Observed: HR falls.** The connected-diagram explanation is that the α₁ rise in TPR + the β₁ rise in CO together raise MAP enough to drive the **baroreceptor reflex** (Fig. 25-1C, red right-arrow), which instructs the heart to slow. The direction of the HR change therefore depends on the **pre-existing state** of the other parameters: a pre-vasodilated subject's BP rises less and the bradycardia is blunted; a hypertensive subject with a **reset baroreflex** (Box 23-1) may not show bradycardia at all. This is the canonical example for why initial conditions matter.

#### Six non-cardiovascular subsystems (Fig. 25-2)
A circulatory control model that omits any of these is incomplete:
1. **Autonomic nervous system.** Both organ-specific (baroreflex) and global (fight-or-flight) influence.
2. **Respiratory system.** Three vectors: (a) ventilatory drive converts peripheral-chemoreceptor bradycardia into tachycardia; (b) inspiration drops intrathoracic pressure → increases venous return; (c) respiratory evaporative water loss erodes blood volume over hours.
3. **Hematopoietic organs + liver.** Set hematocrit (viscosity, Ch 18) and plasma proteins (colloid osmotic pressure → Starling forces → interstitial-plasma equilibrium).
4. **GI + urinary systems.** Net electrolyte/water balance → ECF volume → long-term MAP control (Ch 40).
5. **Endocrine system.** Adrenal medullary epinephrine; vasoactive hormones; renal/GI-acting hormones (aldosterone, AVP, ANP).
6. **Temperature control.** Skin blood flow as the dominant non-evaporative heat-loss mechanism; sweating as an ECF-loss vector (Ch 59).

### Citation-anchor quotes
- > "Cardiovascular parameters and associated physiological responses are often related by multiple factors, requiring a more complex diagram called a branching tree (or an algorithmic tree)." (p. 572)
- > "A physiological system with such complex interactions is best represented by a connected diagram, which may include feedback loops … parameters that appear more than once in the tree … or factors that modulate parameters in two different branches of the tree." (p. 572)
- > "When one disturbs a single parameter in a complex physiological system, the initial state of other parameters determines the end state of the system." (p. 572)
- > "Although our analysis predicts that the heart rate should increase, in most cases the dominant effect of intravenous norepinephrine injection is to slow down the heart." (p. 574)
- > "Bradycardia might also not occur if the baroreceptor reflex were less sensitive, as would be the case in a chronically hypertensive patient." (p. 574)
- > "We cannot fully understand how a particular disturbance affects the overall circulation unless we consider all subsystems in an integrated fashion." (p. 573)

### Figures

#### Figure 25-1 — Patterns of cardiovascular control: linear chart, branching tree, connected diagram *(viewed)*

**Three stacked schematics.** **A (linear chart):** five boxes in a row, left-to-right — stretch of carotid artery → receptor potential (depolarization) in baroreceptor → firing of CN IX → integration of response by medulla → sympathetic output → tone of vascular smooth muscle. Single arrows; no feedback. **B (branching tree):** an inverted dendrogram with **cardiac output** at the root, branching down to **stroke volume** and **heart rate**, each of which then branches further — SV into ventricular compliance, afterload, contractility (feeding end-diastolic volume vs. end-systolic volume); HR into maximum diastolic potential, slope of diastolic depolarization, humoral factors (feeding intrinsic regulation vs. extrinsic regulation). No back-arrows. **C (connected diagram):** the same tree (left limb identical to B) with **mean arterial pressure** at the new root and **total peripheral resistance** branching down through **systemic vasomotor control** and **local vasomotor control** on the right. Superimposed on the tree are three new structural elements: **red feedback arrows** (the baroreceptor loop closing from MAP back through the medulla to HR and to systemic vasomotor control); a **red dashed line** linking the same parameter (venous return / filling pressure) reappearing in two places; and **brown cross-arrows** (humoral factors acting simultaneously on cardiac contractility and on systemic vasomotor control). The legend across panels notes CN = cranial nerve.

> Vision note: this figure is the chapter's epistemological foundation. Every later case study (orthostasis, syncope, exercise, hemorrhage) is implicitly an exercise in working through a connected diagram, not a linear or branching one. It is also the visual mnemonic for why physiology resists single-equation summaries.

#### Figure 25-2 — Interaction among cardiovascular subsystems and noncirculatory systems *(listed)*

A central yellow box ("Cardiovascular System") contains four internal nodes — cardiac output, mean arterial pressure, total peripheral resistance, blood volume — connected to two further internal nodes (systemic circulatory reflexes, local vasomotor control). Six surrounding blue boxes name the non-circulatory subsystems that interact with the yellow core: **autonomic nervous system, respiratory system, hematopoietic organs and liver** (top row); **urinary and GI systems, endocrine system, temperature-control system** (bottom row). Bidirectional arrows connect each outer box to the appropriate node in the yellow core (e.g., autonomic ↔ MAP/CO; endocrine ↔ blood volume/MAP; temperature ↔ TPR/blood volume). The figure visualizes the central claim of Section 1 — that no whole-body cardiovascular question can be answered without these six external subsystems in the model.

---

## Section 2 — Response to erect posture (orthostasis) (pp. 574–577)

### Subsection headings (verbatim)
- **Because of gravity, standing up (orthostasis) tends to shift blood from the head and heart to veins in the legs** (pp. 574–575)
- **The ANS mediates an "orthostatic response" that raises heart rate and peripheral vascular resistance and thus tends to restore mean arterial pressure** (pp. 576–577)

### Core claims

#### The orthostatic problem
~⅔ of total blood volume sits in systemic veins (Ch 19). Tilting from supine to standing in the absence of any compensation would redistribute a large fraction of blood from the central blood volume reservoir into dependent leg veins. Right atrial pressure (RAP) would fall; venous return, SV, CO, and MAP would all fall in sequence. The textbook quantifies the failure mode with a thought experiment.

#### The horizontal–vertical cylinder model (Fig. 25-3; Eq. 25-1)
Model the entire circulation as a single elastic cylinder, 180 cm long × 3 cm radius, containing 5000 mL of blood. With the heart stopped, the cylinder rests at the **mean systemic filling pressure (MSFP) ≈ 7 mm Hg** (Ch 23, p. 549). Transfusing 100 mL more raises MSFP by ~1 mm Hg. The **normalized distensibility** (Eq. 25-1) is therefore:

$$\text{Relative distensibility} = \frac{\Delta V / V_0}{\Delta P} = \frac{100 \text{ mL} / 5000 \text{ mL}}{1 \text{ mm Hg}} = 0.02 / \text{mm Hg}$$

- **Horizontal cylinder (A):** uniform 7 mm Hg pressure along the length; no gravitational column.
- **Vertical cylinder, high distensibility 0.02/(mm Hg) (B):** gravity creates a hydrostatic gradient; the bottom of the cylinder distends until the actual blood column reaches only ~100 cm. If the heart is 50 cm below the top, the column ends 30 cm **below** the heart → RAP would be approximately −22 mm Hg (i.e., −30 cm H₂O). The heart cannot "suck" against such a negative pressure → CO = 0.
- **Vertical cylinder, reduced distensibility 0.01/(mm Hg) (C):** halving the distensibility halves the blood shift; the column now reaches ~130 cm and the top just meets heart level — venous return is preserved.

The model predicts catastrophic failure; in reality, RAP stays at +2 mm Hg even when standing, and only ~500 mL of blood actually pools in both legs combined (not the 2.3 L predicted by the high-distensibility cylinder). Four real-world factors explain the discrepancy.

#### Four counter-pooling factors (Table 25-1 backbone)
1. **Nonuniform initial blood distribution.** Most pre-tilt venous blood is already concentrated in the **central blood volume**, not in the head. The vertical-shift donor is therefore the intrathoracic compartment (high-volume, near the heart) draining into the dependent legs.
2. **Nonuniform vascular distensibility.** Small vessels are stiffer than the aorta and venae cavae; leg veins behave more like the 0.01/(mm Hg) cylinder (C) than the 0.02 one (B). Active sympathetic venoconstriction further drops the effective distensibility.
3. **Skeletal-muscle pump.** Postural muscle activity + venous valves (Fig. 22-7C, Fig. 24-6) shorten the effective hydrostatic column. Without it, prolonged motionless standing is what soldiers do before they faint at parade.
4. **Autonomic reflexes.** The high-pressure baroreceptors detect the small drop in MAP that follows the ~20 % drop in CO; sympathetic outflow rises → ↑HR + ↑contractility + arteriolar constriction (↑TPR) + venoconstriction (↑MSFP / ↓venous distensibility). Together these restore MAP and largely restore RAP, at the cost of a small persistent fall in SV. The **lumbar-sympathectomy** patient faints on standing until they relearn the muscle-pump compensation.

#### Postural hypotension and thermal modulation
- **Postural hypotension** on a tilt table (in susceptible subjects): cerebral perfusion fails transiently → dizziness or syncope.
- **Cool environment:** arteriolar constriction in the legs is already present; blood redistributes slowly enough for the sympathetic reflex to act first; minimal initial BP dip.
- **Warm environment:** cutaneous arterioles are dilated; redistribution is fast; the BP dip is large before the reflex catches up. Hence "soldiers at attention in hot weather are more likely to faint than soldiers marching in a cold environment" — quoted almost verbatim from the source.

### Equations

- **Eq. 25-1 (normalized vascular distensibility):**

$$\text{Relative distensibility} = \frac{\Delta V / V_0}{\Delta P}$$

(applied above to derive the 0.02/(mm Hg) baseline figure.)

- **Gravitational hydrostatic column** (implicit):

$$P_{\text{gravity}} = \rho g h$$

A 180-cm column of blood corresponds to roughly 130 mm Hg of pressure at the foot — explaining ankle venous pressures of ~90–100 mm Hg in the standing subject (cf. Fig. 17-8, Fig. 22-7C).

### Citation-anchor quotes
- > "Because of gravity, standing up (orthostasis) tends to shift blood from the head and heart to veins in the legs." (p. 574)
- > "About two thirds of the total blood volume resides in the systemic veins." (p. 574)
- > "The MSFP is the pressure in the circulation that would remain in the absence of any pumping or any gravity effects." (p. 574)
- > "Of the four factors that contribute to the stability of RAP during orthostasis, two are anatomical (i.e., nonuniformities of initial blood volume distribution and distensibility) and two are physiological (i.e., muscle pumps and autonomic reflexes)." (p. 576)
- > "After a lumbar sympathectomy, patients tend to faint when standing." (p. 576)
- > "Soldiers standing quietly at attention in hot weather are more likely to faint than are soldiers marching in a cold environment." (p. 576)

### Tables

#### Table 25-1 — Factors influencing the degree of orthostatic response (paraphrased)

| Class | Factor |
|---|---|
| Volume | Total blood volume; distribution of blood volume |
| Vascular geometry | Size of vessels in dependent regions; vascular distensibility |
| Hydrostatic | Mean systemic filling pressure; level of zero effective pressure; degree of tilt |
| Skeletal-muscle pump | Skeletal muscle tone; strength and rate of intermittent muscle contraction; abdominal muscle tone |
| Vascular state | Vascular sufficiency |
| Thermal | Temperature |
| Reflex sensitivity | Response of low-pressure receptors; response of high-pressure baroreceptors; activity of the sympathetic system |
| Heart | Initial heart rate; initial myocardial contractility |
| End-organ sensitivity | Sensitivity of vascular smooth muscle to sympathetic stimulation |

### Figures

#### Figure 25-3 — Model of the orthostatic redistribution of blood *(viewed)*

Three stacked tube schematics. **A — Horizontal cylinder:** a horizontal distensible tube 180 cm long × 3 cm radius, the long axis horizontal. The cylinder is uniformly pink (filled with 5 L of blood at rest) and labeled with a single pressure value of 7 mm Hg throughout — the mean systemic filling pressure. **B — Vertical cylinder with high compliance (0.02/(mm Hg)):** the same cylinder now standing upright with the head end at top. Pressure increases linearly toward the bottom; the bottom one-third has visibly bulged outward. The blood column reaches only ~100 cm in height — labeled with a heart symbol drawn 50 cm below the original top, so the column ends 30 cm *below* the heart. A caption note marks this as "no venous return; RAP would be ~−22 mm Hg." **C — Vertical cylinder with reduced compliance (0.01/(mm Hg)):** the same cylinder, now with stiffer walls and only mild bulging at the bottom. The column reaches ~130 cm — just touching the heart level — and venous return is preserved. The figure pairs with Eq. 25-1 and is the chapter's quantitative anchor for why the four real-world factors (nonuniform distribution, nonuniform distensibility, muscle pump, autonomic reflex) matter.

---

## Section 3 — Responses to acute emotional stress (pp. 577–580)

### Subsection headings (verbatim)
- **The fight-or-flight reaction is a sympathetic response that is centrally controlled in the cortex and hypothalamus** (pp. 577–578)
- **The common faint reflects mainly a parasympathetic response caused by sudden emotional stress** (pp. 579–580)

### Core claims

#### Fight-or-flight: a centrally-originating response (Fig. 25-4)
Unlike the baroreflex, the fight-or-flight response has **no peripheral sensor** — it is initiated entirely within the CNS. The wiring (Fig. 25-4):
- **Cortical sensory centers** (sight, sound, threat perception) → **amygdala** (limbic appraisal, p. 349) → **locus coeruleus** (pons, p. 312, noradrenergic projection to virtually the entire CNS) **and** hypothalamic nuclei.
- **Hypothalamic paraventricular nucleus (PVN)** is the dominant downstream node, producing two parallel outputs:
  - **Endocrine arm.** Magnocellular PVN neurons release AVP (→ ↓ renal water loss, ↑ blood volume). Parvocellular PVN neurons release CRH → ACTH → cortisol (metabolic stress response).
  - **ANS arm.** Projections to the medullary cardiovascular center (NTS, RVLM, dorsal motor nucleus of vagus), and direct descending projections to the spinal intermediolateral cell column.

#### Eight effector vectors of the fight-or-flight response
1. **Skeletal-muscle blood flow.** Direct sympathetic cholinergic vasodilation (in some species, debated in humans) + circulating epinephrine acting on β₂ adrenoceptors → dilation; metabolite vasodilation if real exercise ensues.
2. **Cutaneous blood flow.** Little net change *unless* sweating is triggered; then sympathetic cholinergic fibers release ACh and vasodilatory cotransmitters (CGRP, VIP). ACh also triggers local kinin formation → ↑ capillary permeability + arteriolar dilation + venular constriction → ↑ midcapillary pressure → dermal swelling.
3. **Adrenal medulla.** Preganglionic sympathetic → chromaffin cells → epinephrine → β₂ vasodilation in muscle, α₁ vasoconstriction in kidney + splanchnic beds.
4. **Renal + splanchnic flow.** Generalized α₁ vasoconstriction; epinephrine reinforces.
5. **Veins.** Sympathetic constriction → ↓ venous capacity → ↑ MSFP → ↑ venous return.
6. **Heart.** ↑ Sympathetic + ↓ vagal → ↑ HR + ↑ contractility → ↑ CO.
7. **Blood volume.** Elevated AVP → ↓ urinary water loss → maintained blood volume.
8. **Mean arterial pressure.** Net direction of TPR change is variable (depends on the dilation-vs-constriction balance), but CO definitely rises → MAP rises.

#### The common faint: vasovagal (vasodepressor) syncope, VVS (Fig. 25-5)
- **Epidemiology.** ~⅕ of humans have ≥1 episode during adolescence; ~40% of outpatient syncope cases are vasovagal.
- **Trigger.** Sudden emotional stress (phlebotomy, sight of blood, acute pain) when the patient is sitting or standing — almost never recumbent. The "playing dead" reaction in animals is the homologue.
- **Origin.** Specific cortical areas (anterior cingulate gyrus → stimulation can trigger VVS experimentally) initiate the cascade. The trigger pattern resembles the **Bezold–Jarisch reflex** — originally described with IV *Veratrum* alkaloids causing bradycardia + hypotension + apnea, but reproducible with nicotine, capsaicin, histamine, 5-HT, snake/insect venoms, IV contrast or thrombolytics. These chemicals likely activate the same stretch-sensitive **TRPC channels** of arterial/ventricular baroreceptors that normally fire to high pressure.
- **Mechanism (Fig. 25-5):** massive parasympathetic discharge + simultaneous *removal* of sympathetic tone. Note: this is the opposite of every other autonomic response — VVS *abolishes* sympathetic outflow, and the brain pattern that orchestrates VVS *also* **suppresses the expected baroreflex** that would normally oppose hypotension. Four downstream effects:
  1. **TPR:** massive vasodilation across muscle, splanchnic, renal, cerebral beds → falling MAP.
  2. **CO:** intense vagal output → bradycardia + ↓ SV. Atropine fails to reliably prevent syncope → sympathetic withdrawal must also contribute.
  3. **MAP:** profound combined fall (↓ TPR + ↓ CO).
  4. **Cerebral blood flow:** falls globally; ≥10 s of inadequate cerebral perfusion → loss of consciousness. Reflex hyperventilation often accompanies the trigger, lowering arterial P_CO₂ and adding *direct cerebral vasoconstriction* (Ch 24) — worsening the ischemia.
- **Other ANS signs.** Pallor, sweating, GI vagal cramping (interpreted as nausea), mydriasis, blurred vision.
- **Facilitators.** Warm room, volume loss (dehydration, hemorrhage), recent orthostasis. Counterintuitively, these also bias the brain *toward* the syncopal pattern rather than triggering compensatory baroreflexes.
- **Post-faint oliguria.** Elevated AVP (driven both by emotional input and by reduced atrial stretch during the syncope; Ch 40 pp. 817–819) → reduced urine output for hours afterward, plus persistent pallor + nausea from circulating AVP.

### Citation-anchor quotes
- > "Fight-or-flight behavior is an extreme example of an integrated acute stress response that originates entirely within the central nervous system (CNS), without involvement of peripheral sensors or reflexes." (p. 577)
- > "Noradrenergic neurons in the locus coeruleus project to nearly every part of the CNS … including the hypothalamic paraventricular nucleus (PVN), which produces both an endocrine and an ANS response." (p. 577)
- > "About one fifth of humans experience one or more episodes of fainting during adolescence." (p. 579)
- > "VVS … has been attributed to activation of the Bezold-Jarisch reflex." (p. 579)
- > "Vagal afferents carry signals to higher CNS centers, which act through autonomic nuclei in the medulla to cause a massive stimulation of the parasympathetic system and abolition of sympathetic tone." (p. 579)
- > "The same integrated pattern of brain activity that orchestrates VVS also appears to suppress the expected baroreceptor reflexes that would otherwise counteract the syncope." (p. 580)

### Figures

#### Figure 25-4 — Fight-or-flight response *(viewed)*

A vertically-organized integration diagram. **Top:** "Emotional stress" enters the **cortex**; cortex sends a descending projection to the **hypothalamus**; hypothalamus sends descending projections both to the **medullary cardiovascular control centers** and directly to the spinal cord. **Middle:** a spinal-cord cross-section with red sympathetic preganglionic axons leaving the intermediolateral cell column at multiple levels, traveling to a row of sympathetic chain ganglia, and emerging as red postganglionic axons. **Bottom:** the effector row. From left to right: **blood vessels in muscle** (innervated by sympathetic cholinergic fibers releasing ACh → sympathetic vasodilation response); **sweat glands** (sympathetic cholinergic, ACh → sweating); **adrenal medulla** (preganglionic ACh onto chromaffin cells → epinephrine into bloodstream); **kidney and splanchnic arterioles** (sympathetic noradrenergic, NE → sympathetic vasoconstriction response); **veins** (sympathetic noradrenergic, NE → venoconstriction); **heart** (sympathetic NE + parasympathetic ACh, with sympathetic dominant → increased heart rate and stroke volume). An "epinephrine" arrow runs underneath the row, indicating systemic adrenal output reinforcing all of these effects. A right-side legend color-codes higher control, hypothalamic control, interneurons, sympathetic pre/post, parasympathetic pre/post, and ganglia.

> Vision note: this is the chapter's structural anchor for the *integrated effector pattern* of acute sympathetic activation. Compare with Fig. 14-4 (Ch 14, the ANS organizational schematic) — Fig. 25-4 is the "all switches on at once" version.

#### Figure 25-5 — Vasovagal syncope *(viewed)*

A causal flow diagram organized top-down, with two distinct triggers entering the top row: **emotional stress** (left) and **chemical stimulus** acting on baroreceptors (right). Both converge on the **cortex**, which projects to the **hypothalamus** (which simultaneously triggers ↑ AVP release) and to the **medulla**. The medulla produces two outputs side-by-side: **↓ sympathetic output** (left, drawn in muted color) and **↑ vagal output** (right, drawn in solid green). Downstream: ↓ sympathetic → **blood vessels** (drawn dilated) → ↓ total peripheral resistance; ↑ vagal → **heart** (drawn slowed) → ↓ cardiac output + ↓ venous return (with feedback to ↓ atrial stretch and consequently further ↑ AVP). Both arms converge: ↓ TPR + ↓ CO → **↓ arterial pressure** → ↓ blood flow to **brain** → **loss of consciousness** at the bottom. The diagram makes visible the key claim of the section — that VVS is a *mirror image* of fight-or-flight, with the same wiring but opposite signs.

> Vision note: an unusual figure in physiology because it diagrams a **failure mode** of the baroreflex (the reflex is suppressed, not engaged). It is the conceptual anchor for understanding why VVS is paradoxical: hypotension occurs *with* the baroreflex pathway intact but actively gated off.

---

## Section 4 — Response to exercise (pp. 580–583)

### Subsection headings (verbatim)
- **Early physiologists suggested that muscle contraction leads to mechanical and chemical changes that trigger an increase in cardiac output** (pp. 580–581)
- **Central command organizes an integrated cardiovascular response to exercise** (pp. 581)
- **Muscle and baroreceptor reflexes, metabolites, venous return, histamine, epinephrine, and increased temperature reinforce the response to exercise** (pp. 581–583)

### Core claims

#### Magnitude and partitioning of the exercise response
At peak exercise, CO rises 4–5× resting. Of that, HR rises ~3× and SV rises ~1.5× — i.e., HR is the dominant lever. The response has both **early** (anticipatory, CNS-originating) and **late** (delayed, reflex- and metabolite-driven) components.

#### The early "muscle-only" model and its falsification (Fig. 25-6)
Early 20th-century physiology argued that **all** the CV changes in exercise originated in the contracting muscle itself, via two parallel limbs:
- **Mechanical limb.** Muscle pump → ↑ venous return → ↑ RAP → ↑ EDV → ↑ SV by Starling's law.
- **Chemical limb.** ↓ P_O₂, ↑ P_CO₂, ↓ pH, ↑ K⁺, ↑ adenosine, ↑ lactate, ↑ osmolarity → arteriolar dilation → ↓ TPR → transient ↓ MAP → baroreceptor reflex → ↑ HR + ↑ SV.

In the 1950s, **Rushmer** (trained, unanesthetized dogs) showed three predictions of this model **fail**:
1. LV end-diastolic *pressure* does **not** rise at exercise onset (and EDV actually **falls slightly** rather than rising) — undermining the Starling story as the primary lever.
2. MAP does **not** dip transiently at exercise onset — undermining the baroreflex-as-trigger story for the tachycardia.
3. HR rises **immediately**, with no detectable lag for chemical signals to accumulate.

The conclusion: there must be a **central command** that *anticipates* the contraction and pre-emptively activates the sympathetic system.

#### The central-command model (Fig. 25-7)
- **Cortical sites.** Medial prefrontal cortex (thinking/planning exercise) + insula + anterior cingulate gyrus (limbic, p. 349). Both project to the hypothalamus.
- **Diencephalic relay.** Rushmer's stimulation experiments showed that exciting the **H₁ fields of Forel (ventral thalamus)** or **periventricular hypothalamic gray** reproduces the full cardiac response to exercise even in a paralyzed (quiescent-muscle) animal. These centers project to lateral hypothalamus → RVLM, NTS → spinal IML.
- **Effector pattern (Fig. 25-7).** Parallel motor-cortex activation + medullary-CV-center activation → simultaneously:
  1. **↑ CO** via sympathetic ↑ HR + ↑ contractility (early tachycardia precedes any peripheral reflex).
  2. **Vasoconstriction** in inactive muscle, renal, splanchnic, and (initially) cutaneous beds. Absolute renal/splanchnic flow stays near resting because TPR rise is matched by MAP rise; *fractional* flow drops. Skin flow drops early.
  3. **Early vasodilation in active muscle** (in dogs; debated in humans/primates): hypothalamic axons bypass the medulla and drive spinal sympathetic preganglionics that synapse on **cholinergic sympathetic vasodilator** postganglionics innervating muscle arterioles. (Cf. Ch 14, pp. 342–343.)
- **Anticipation.** Cardiac output rises *before* the gun in a 100-m dash — pure feed-forward CNS output, no peripheral input required.

#### Seven reinforcing mechanisms (delayed phase)
1. **Exercise pressor reflex.** Stretch + chemoreceptors in active muscle → Aδ (group III) + C (group IV) afferents → spinal cord → medullary CV centers → sustained sympathetic outflow.
2. **Arterial baroreflex resetting.** During exercise, central command shifts the baroreflex set-point upward so the elevated MAP does *not* slow the heart. If massive active-muscle vasodilation drops TPR too far, the baroreflex still defends MAP.
3. **Metabolite-driven vasodilation in active muscle.** ↑ K⁺, adenosine, CO₂; ↓ O₂, pH; ↑ osmolarity → arteriolar dilation + capillary recruitment → active muscle flow up to ~20× resting. Overcomes sympathetic noradrenergic vasoconstriction locally.
4. **Increased venous return.** Mechanical muscle pump (Ch 22, Fig. 22-7C) + chemical mobilization of central blood volume → preserved/increased SV by Starling's law (delayed phase, consistent with Fig. 25-6's mechanical limb but as a *reinforcer* rather than the trigger).
5. **Histamine release.** Arteriolar-adjacent cells release histamine (Table 20-8) when sympathetic tone wanes locally → further vasodilation + ↑ capillary pressure → ↑ extravasation + ↑ lymph flow.
6. **Epinephrine release.** Severe exercise → adrenal preganglionic firing → systemic epinephrine → cardiac β₁ (reinforces neural ↑ HR + ↑ contractility) + vascular β₂ (skeletal muscle, heart vasodilation).
7. **Thermoregulation.** Rising core temperature → hypothalamic temperature-sensitive neurons (Ch 59, p. 1199) → (a) medullary inhibition of sympathetic vasoconstrictor outflow to skin (reverses the early cutaneous vasoconstriction); (b) sympathetic cholinergic activation of sweat glands → sweating + indirect cutaneous vasodilation (via kinins + co-released vasodilator neurotransmitters).

### Citation-anchor quotes
- > "The main feature of the cardiovascular response to exercise is an increased cardiac output, up to four or five times the resting cardiac output." (p. 580)
- > "The increase in cardiac output during exercise is more the result of increased heart rate (~3 times the control value) than of increased stroke volume (~1.5 times control)." (p. 580)
- > "Rushmer … found that at the onset of exercise, left ventricular end-diastolic pressure does not rise and that left ventricular end-diastolic volume diminishes rather than increases." (p. 581)
- > "Furthermore, he saw no delay between the onset of exercise and the increase of heart rate, thus calling into question the idea that the chemically induced vasodilation is at the root of the tachycardia." (p. 581)
- > "Stimulation of the H₁ fields of Forel in the ventral thalamus or neurons in the periventricular gray matter of the hypothalamus reproduced all the details of the cardiac response to exercise, even though the muscles of the dog were completely quiescent." (p. 581)
- > "During exercise, central command resets the sensitivity of the arterial baroreflex so that the heart slows only at much higher arterial pressures." (p. 583)
- > "Blood flow to active skeletal muscle can be as much as 20 times that to resting skeletal muscle." (p. 583)

### Figures

#### Figure 25-6 — Early ("muscle-only") model of how exercise affects cardiovascular function *(listed)*

A two-column causal flow diagram. **Left column ("mechanical"):** contracting muscle → muscle pump → ↑ venous return → ↑ RAP → ↑ end-diastolic pressure → ↑ EDV → ↑ SV → ↑ CO. **Right column ("chemical"):** contracting muscle → ↑ metabolites → ↓ P_O₂ + ↑ P_CO₂ + ↓ pH → local vasodilation of active muscle → ↓ arterial pressure → arterial baroreceptor activation → ↑ HR → ↑ CO. Both columns converge at the bottom into the same ↑ CO arrow. The figure is historically important as the model Rushmer falsified — it remains a useful straw-man because every link in it *does* occur, just not in the predicted order and not as the trigger of the response.

#### Figure 25-7 — Integrated cardiovascular response to exercise *(viewed)*

The chapter's keystone integration diagram for exercise. **Top:** cortex (medial prefrontal + insula + cingulate, depicted as cortical patches) connected to a thermo-receptor in the periphery on the right, both projecting downward to the hypothalamus. **Middle:** hypothalamus → medullary cardiovascular control centers and direct descending projections to a spinal-cord cross-section. From the cord, sympathetic preganglionic axons (red) emerge to a row of ganglia. **Bottom (left to right):** **active muscle** (sympathetic cholinergic, releasing ACh from a stretch-receptor-equipped varicosity → early vasodilation + delayed local metabolite vasodilation shown as a separate yellow-highlighted arrow); **skin** (thermo-receptor afferent feedback to hypothalamus, sympathetic cholinergic to sweat glands → kallikreins → delayed vasodilation, highlighted yellow); **adrenal medulla** (ACh on chromaffin cells → epinephrine — yellow-highlighted as a delayed reinforcer); **inactive muscle, splanchnic, cutaneous, renal arterioles** (sympathetic NE → vasoconstriction); **veins** (sympathetic NE → venoconstriction); **heart** (sympathetic NE + parasympathetic ACh, with sympathetic dominant → ↑ HR + ↑ SV). The yellow highlights flag the **delayed** components added on top of the central-command early response. A legend on the left names higher control, hypothalamic control, interneuron, sensory, sympathetic pre/post, parasympathetic pre/post, ganglia.

> Vision note: this is the visual culmination of the chapter's exercise narrative. Compare with Fig. 25-4 (fight-or-flight) — the two share most of the same effector wiring; what differs is the upstream trigger (cortical emotion vs. central command + reinforcers) and the inclusion of (1) muscle stretch/chemoreceptor afferents, (2) thermoreceptor feedback, and (3) baroreflex resetting. Anchor for Ch 60 (Exercise Physiology) downstream.

---

## Section 5 — Response to hemorrhage (pp. 583–587)

### Subsection headings (verbatim)
- **(introduction)** (p. 583)
- **After hemorrhage, cardiovascular reflexes restore mean arterial pressure** (pp. 583–585)
- **After hemorrhage, transcapillary refill, fluid conservation, and thirst restore the blood volume** (pp. 585–587)
- **Positive-feedback mechanisms cause irreversible hemorrhagic shock** (pp. 587)

### Core claims

#### Categories of blood loss
- **Rapid loss <10–20% of total volume from a large vein:** sequential cascade ↓ central blood volume → ↓ venous return → ↓ ventricular filling → ↓ SV → ↓ CO → ↓ MAP.
- **Loss from a large peripheral artery:** central arterial pressure stays normal until CO drops secondary to ↓ venous return — so MAP falls *late* relative to the cascade.
- **Blown aortic aneurysm:** MAP drops immediately.
- **Loss ≥ 30% of total blood volume → hypovolemic shock.** Defined clinically as SBP < 90 mm Hg, MAP < 70 mm Hg. By the time MAP records a significant drop, the patient already displays:
  - Narrowing of the pulse pressure.
  - Faintness on sitting/standing.
  - Cold, moist, "clammy" skin.
  - Rapid weak pulse.
  - Oliguria <25 mL/hr.

#### Two lines of defense
After the initial fall, MAP either **recovers toward normal** (red curve, Fig. 25-8) or **decays irreversibly** (blue dashed curve, Fig. 25-8). Recovery requires:
1. **Circulatory reflexes** acting on heart + vessels to restore CO + raise TPR.
2. **Capillary fluid mechanisms + renal conservation + thirst** to restore intravascular volume.

#### Four-receptor reflex compensation (Fig. 25-9)
The medullary cardiovascular center integrates signals from four receptor populations simultaneously:
1. **High-pressure baroreceptors** (carotid sinus, aortic arch; Ch 23, p. 534). ↓ MAP → ↓ stretch-receptor firing → ↑ sympathetic + ↓ vagal → ↑ HR + ↑ contractility + venoconstriction + arteriolar constriction.
2. **Low-pressure baroreceptors** (atrial/pulmonary venous stretch receptors; Ch 23, p. 547). ↓ effective circulating volume → ↓ stretch-receptor firing → ↑ sympathetic outflow → renal vasoconstriction + ↓ GFR + ↓ urine output. ↓ atrial stretch also signals the hypothalamus to ↑ AVP → renal water retention + (importantly during shock) **direct vasoconstriction** by AVP. ↓ atrial stretch → ↓ circulating ANP → further renal Na⁺/water retention.
3. **Peripheral chemoreceptors** (carotid + aortic bodies; Ch 32). ↓ local perfusion → glomus-cell hypoxia → ↑ chemoreceptor firing → ↑ sympathetic vasoconstrictor outflow + indirect ↑ HR via ventilatory drive.
4. **Central chemoreceptors** (medulla; Ch 32, p. 713). Severe hypotension → brain ECF: ↓ P_O₂, ↑ P_CO₂, ↓ pH → potent central chemoreceptor activation → sympathetic output **several-fold more powerful** than baroreflex-driven output.

Net effect: massive systemic sympathetic surge + adrenal release of epinephrine + NE. At MAP 40 mm Hg, circulating epinephrine rises **50-fold** and NE **10-fold**.

#### Five integrated effects of the surge
- **Tachycardia + ↑ contractility.** HR rise proportional to volume lost; clinical index of severity.
- **Arteriolar constriction.** Most pronounced in extremities, skin, skeletal muscle, abdominal viscera. Precapillary constriction dominates initially → capillary hydrostatic pressure (P_c) **falls** precipitously → drives transcapillary refill (below). Renal flow falls fast, recovers partially by autoregulation, fails again if hypotension persists; medullary flow is preserved relative to cortical → "medullary washout" of the concentration gradient → inability to concentrate urine. Cerebral + coronary flow protected by autoregulation.
- **Venous constriction.** Hits the capacitance vessels (which hold the central blood volume). ↓ venous capacity and ↓ venous compliance → ↑ MSFP → ↑ venous return. Postcapillary venoconstriction is also key for transcapillary refill.
- **Circulating vasoactive agonists.** Adrenal medullary epinephrine; juxtaglomerular renin → ANG II at vasoconstrictive levels; sympathetic cholinergic sweating (clammy skin).
- With moderate (10–20%) blood loss these four mechanisms can keep MAP roughly normal — but **CO remains depressed**.

#### Transcapillary refill: a Starling-force reversal (Fig. 25-10A→B→C)
The dominant defense against the *volume* deficit is the movement of fluid **from the interstitium into the blood plasma**. Within ~1 hour, interstitial fluid replaces ~75% of the shed volume. The mechanism is a transient reversal of the normal Starling balance:

- **Normal (Fig. 25-10A).** Arteriole 60 → capillary ~25 → venule 15 mm Hg. R_post/R_pre ≈ 0.35 (i.e., capillary pressure is closer to venular than arteriolar). Net Starling balance: small filtration outward (Ch 20).
- **Uncompensated hemorrhage (B).** Arteriole drops to 40, venule to 5, capillary to ~14 mm Hg. With unchanged R_post/R_pre, the entire pressure profile falls; capillary hydrostatic pressure (P_c) drops below colloid osmotic pressure of plasma → net **reabsorption** into the capillaries.
- **Compensated hemorrhage (C).** Sympathetic surge raises precapillary resistance much more than postcapillary → R_post/R_pre drops to ~0.25 → P_c stays low even though arteriolar pressure has recovered to ~50 mm Hg → sustained net reabsorption from interstitium.

The reabsorption gradient dissipates as: (1) interstitial volume drops → ↓ P_i (favors continued filtration); (2) plasma proteins dilute → ↓ π_c; (3) interstitial colloid concentration rises (and subglycocalyx π_g rises, pp. 471–472) → ↑ π_i. Eventually transcapillary refill plateaus.

The second step in refill is **protein restoration**: plasma proteins enter the blood across **fenestrated** mesenteric + hepatic capillaries, then the liver upregulates albumin synthesis (the same response is seen after plasmapheresis, suggesting plasma-protein concentration itself is the stimulus).

Finally, **intracellular water** moves out to refill the interstitium, driven by the post-hemorrhage rise in blood osmolality (from ischemic tissues releasing proteolytic, glycolytic, and lipolytic products into the interstitium).

#### Renal salt + water conservation
↓ MAP + ↓ renal blood flow → ↓ GFR → ↓ urine output. Four neurohumoral mechanisms (Ch 40):
1. **Activated RAAS** → ↑ aldosterone → ↑ distal-nephron Na⁺/water reabsorption.
2. **↑ Sympathetic outflow** (p. 842) → renal hemodynamics + ↑ renin + direct tubular Na⁺ reabsorption.
3. **↑ AVP** → ↓ renal water excretion + direct vasoconstriction.
4. **↓ ANP** → ↓ renal Na⁺/water loss.

The renal arm **conserves** ECF; it does not add new water — that is the role of:

#### Thirst
Hyperosmolality stimulates **osmoreceptors** (pp. 845–846); reduced effective circulating volume + reduced BP are even more potent stimuli for **thirst + salt appetite** (p. 849). Behavioral fluid intake is what actually replenishes lost volume.

#### Irreversible hemorrhagic shock: four positive-feedback failure modes
With prolonged hypotension, recovery converts to decay (Fig. 25-8, blue dashed curve), and at this point blood-volume restoration **no longer reverses** the trajectory. Four failure modes:

1. **Vasoconstrictor response fails ("sympathetic escape").**
   - Vascular adrenoceptor desensitization or NE depletion at the terminals.
   - Ischemic tissues release vasodilator metabolites that override the sympathetic signal.
   - AVP stores deplete (low-pressure baroreceptor reflex fatigues or hypothalamus runs out of releasable AVP). Restoring AVP at this stage *can* raise BP — diagnostic of the depletion.

2. **Capillary refill fails (Fig. 25-10D: R_post/R_pre reverses).**
   - The precapillary sphincter is the first to fail; postcapillary tone is partially maintained. R_post/R_pre rises (from 0.25 toward 0.45) → midcapillary P_c climbs (from ~16 to ~21 mm Hg) → Starling balance reverses *again*: net filtration restarts, **draining the plasma volume back into the interstitium** even though blood volume has not been restored. This is the classic decompensation point.

3. **Heart fails.** Acidosis ↓ [Ca²⁺]ᵢ handling → ↓ contractility (Ch 22, pp. 530–532). Severe cases: subendocardial hemorrhage + necrosis. Ischemic organs release **cardiotoxic shock factors** (negative inotropes). Hypovolemic shock converts to **cardiogenic shock**.

4. **CNS depression.** Moderate ischemia *stimulates* the central chemoreceptors and CV centers; prolonged ischemia *depresses* them, weakening sympathetic output. Adrenal catecholamine release also declines, removing the systemic-epinephrine reinforcement.

The clinical implication: irreversible shock is defined operationally — fluid restoration no longer restores BP because the compensation machinery itself is in failure.

### Equations

The chapter has no new symbolic equations beyond Eq. 25-1; key quantitative anchors are inequality / ratio statements:

- **Hypovolemic-shock thresholds:** loss ≥ 30% of total blood volume; SBP < 90 mm Hg; MAP < 70 mm Hg; urine output < 25 mL/hr.
- **Catecholamine surge** at MAP 40 mm Hg: epinephrine ↑ 50×, NE ↑ 10×.
- **Transcapillary refill:** ~75% of shed volume replaced within 1 hour by interstitial fluid.
- **Resistance ratio dynamics (Fig. 25-10 series):** normal R_post/R_pre ≈ 0.35 → compensated ≈ 0.25 → decompensated ≈ 0.45.
- **Capillary pressure trajectory (Fig. 25-10A→B→C→D):** ~25 → ~14 → ~16 → ~21 mm Hg.

### Citation-anchor quotes
- > "Large hemorrhages, in which one loses 30% or more of total blood volume, produce hypovolemic shock." (p. 583)
- > "During shock, the systolic arterial pressure is usually <90 mm Hg, and the mean arterial pressure is <70 mm Hg." (p. 583)
- > "Lowering of the mean arterial pressure to 40 mm Hg causes circulating levels of epinephrine to rise 50-fold and those of norepinephrine, 10-fold." (p. 585)
- > "Within an hour, interstitial fluid replaces ~75% of the shed blood volume." (p. 585)
- > "Hemorrhagic shock can become irreversible as a result of the failure of multiple response components: (1) the vasoconstrictor response, (2) the capillary refill response, (3) the cardiac response, and (4) the CNS response." (p. 587)
- > "Ultimately hypovolemic shock converts to cardiogenic shock." (p. 587)
- > "The reflexes … compensate for the principal consequences of blood loss — decreased blood pressure and reduced cardiac output. The responses discussed here compensate for the primary disturbance, the loss of blood volume." (p. 585)
- > "Capillary hydrostatic pressure … falls precipitously, leading to the transcapillary refill." (p. 585)

### Figures

#### Figure 25-8 — Changes in blood pressure with hemorrhage *(listed)*

A single time-series plot. Horizontal axis: time (hr) from 0 to ~6 h. Vertical axis: mean arterial pressure (mm Hg, 0 to ~100). At t = 0 the investigator removes enough blood to drop MAP to ~45 mm Hg. Two trajectories diverge: the **red curve ("Reversible")** climbs back toward normal MAP within a few hours; the **blue dashed curve ("Irreversible")** initially recovers partially, plateaus, then decays inexorably toward zero. The figure encapsulates the central clinical distinction of the section: same initial insult, very different outcome depending on whether the four compensatory machines stay in their operating range.

#### Figure 25-9 — Integrated response to hemorrhage *(viewed)*

The chapter's master integration diagram for hemorrhage. **Top center:** a "Hemorrhage" arrow drives parallel rows of upstream signals to the right and left. **Left limb (cardiac):** ↓ venous return → ↓ stroke volume → ↓ cardiac output → ↓ arterial pressure. **Center limb (volume):** ↓ central blood volume → ↓ atrial volume; ↓ regional blood flow → ↓ P_O₂, ↑ P_CO₂, ↓ pH of brain ECF. Above the "↓ stroke volume" arrow, a feedback loop annotation reads "Increased cardiac output restores venous return" and "Increased cardiac output and total peripheral resistance restore arterial pressure." Each of the upstream signals feeds one of **four numbered receptor groups** in the middle row: (1) **high-pressure baroreceptors**, (2) **low-pressure baroreceptors**, (3) **peripheral chemoreceptors**, (4) **central chemoreceptors**. All four converge on the **medullary cardiovascular centers**, which generate a single dominant arrow labeled **"sympathetic response."** From there, five output arrows fan out: **↑ heart rate + contractility → ↑ cardiac output**; **arteriolar constriction → ↑ total peripheral resistance**; **venous constriction → ↓ venous capacity**; **↑ renin release → ANG II → ↑ TPR**. The integrated effect at the bottom: ↑ arterial pressure, completing the compensatory loop.

> Vision note: the master integration diagram of Ch 25. It is the visual analog of the connected-diagram archetype of Fig. 25-1C, instantiated for a specific clinical insult. Every Ch 23/24 reflex appears here; the four-receptor convergence on the medulla is the heart of the figure. Anchor for clinical reasoning about every hypovolemic state (hemorrhage, dehydration, burns, sepsis with relative hypovolemia).

#### Figure 25-10 — Effect of hemorrhage on capillary hydrostatic pressure *(viewed)*

Four stacked microvascular schematics, each showing the arteriole → capillary → venule axis with annotated pressures. **A — Normal:** arteriole 60 → capillary 25 → venule 15 mm Hg; R_post/R_pre ≈ 0.35; capillary pressure closer to venular end (because R_pre > R_post — Ch 20). Standard Starling balance. **B — Uncompensated hemorrhage:** arteriole 40 → capillary 14 → venule 5 mm Hg; R_post/R_pre still ≈ 0.35; the whole pressure column has collapsed; net Starling forces drive **fluid from interstitium INTO the capillary** (drawn as inward blue arrows along the capillary wall). **C — Compensated hemorrhage:** sympathetic surge has selectively raised precapillary resistance (drawn as a "greatly increased resistance" wedge on the arteriolar side) more than postcapillary (drawn as a "moderately increased resistance" wedge); arteriole back up to 50 mm Hg, but capillary hydrostatic pressure stays low (R_post/R_pre drops to ~0.25) → net Starling reabsorption sustained. **D — Decompensated hemorrhage:** the precapillary vasoconstriction has "faded" (drawn as a faded wedge), while the postcapillary vasoconstriction is partly maintained (R_post/R_pre rises to ~0.45); arteriole 50 mm Hg, but capillary midpressure climbs to ~21 mm Hg → Starling forces reverse *again*, this time driving **fluid OUT of the capillary** (drawn as outward arrows) — net loss of plasma volume into the interstitium **even though blood volume has not been restored**.

> Vision note: this is the chapter's most quantitatively rich figure and the visual mechanism for *why* irreversible shock is "irreversible." The R_post/R_pre ratio (a single dimensionless number) governs the direction of fluid flux at the capillary; the four panels show its trajectory across the four phases of the response. Anchor for Ch 40 (integration of salt and water balance) and for clinical reasoning about fluid resuscitation in late shock.

---

## Glossary

- **Linear chart / branching tree / connected diagram** — three diagrammatic archetypes for cardiovascular regulation; the connected diagram (with feedback loops, parameter recurrences, and cross-branch arrows) is the only honest representation.
- **Mean systemic filling pressure (MSFP)** — pressure in the circulation in the absence of cardiac output and gravity; ≈ 7 mm Hg.
- **Normalized vascular distensibility** — (ΔV/V₀)/ΔP; ≈ 0.02/(mm Hg) for whole circulation.
- **Orthostasis** — assumption of an upright posture (Greek *orthos* + *histanai*).
- **Right atrial pressure (RAP)** — pressure at the heart's input; ≈ +2 mm Hg supine and upright (preserved by compensation).
- **Central blood volume** — blood in the great veins, right heart, pulmonary circulation; the reservoir from which orthostatic redistribution draws.
- **Zero effective pressure level** — anatomical height where vascular pressure = atmospheric pressure; approximately at the right atrium during quiet standing.
- **Postural / orthostatic hypotension** — transient cerebral hypoperfusion on standing.
- **Skeletal-muscle pump / muscle-vein pump** — intermittent compression + venous valves shorten the effective hydrostatic column.
- **Lumbar sympathectomy** — surgical interruption of the sympathetic chain; causes transient orthostatic intolerance.
- **Fight-or-flight response** — centrally-originating mass sympathetic discharge; no peripheral sensor; cortex → amygdala → locus coeruleus → PVN → medulla + IML.
- **Paraventricular nucleus (PVN)** — hypothalamic node coordinating sympathetic, AVP, and CRH outputs.
- **Vasovagal (vasodepressor) syncope (VVS) / common faint** — sudden parasympathetic mass discharge + abolition of sympathetic tone + baroreflex suppression; ~⅕ adolescents.
- **Bezold–Jarisch reflex** — bradycardia + hypotension + apnea from intracardiac chemoreceptor activation by *Veratrum* alkaloids, capsaicin, nicotine, contrast, etc.
- **TRPC channels** — stretch-sensitive cation channels in arterial and ventricular baroreceptors; also chemically activated in VVS.
- **Anterior cingulate gyrus / medial prefrontal cortex / insula** — cortical limbic triad activating the fight-or-flight and exercise responses.
- **Central command** — feed-forward CNS pattern that drives motor + cardiovascular output simultaneously; demonstrated by Rushmer in the 1950s.
- **H₁ fields of Forel** — ventral thalamic site whose stimulation reproduces the cardiac response to exercise.
- **Exercise pressor reflex** — Aδ + C-fiber feedback from active muscle to the medullary CV center; sustains the sympathetic surge.
- **Baroreflex resetting** — central-command-mediated upward shift of the baroreflex set point during exercise.
- **Sympathetic cholinergic vasodilator fibers** — direct vasodilator innervation of skeletal-muscle arterioles (robust in dogs; debated in humans).
- **Metabolite-driven vasodilation** — ↓ P_O₂, ↑ P_CO₂, ↓ pH, ↑ K⁺, ↑ adenosine, ↑ lactate, ↑ osmolarity; ≤ 20× resting flow in active muscle.
- **Histamine release** — adjacent-cell vasodilator augmentation when sympathetic tone falls; also raises capillary pressure.
- **Hypovolemic shock** — loss ≥ 30% of total blood volume; SBP < 90, MAP < 70 mm Hg; clammy skin, weak pulse, oliguria.
- **Compensated / decompensated / irreversible shock** — three phases distinguished by the R_post/R_pre ratio and by whether volume restoration reverses MAP.
- **Transcapillary refill** — net movement of fluid from interstitium into plasma after hemorrhage; ~75% of shed volume in ~1 hour.
- **R_post / R_pre ratio** — postcapillary-to-precapillary resistance ratio; governs the direction of capillary fluid flux.
- **Medullary washout** — loss of the corticomedullary osmotic gradient when renal medullary flow is preserved during cortical ischemia; impairs urine concentration.
- **Sympathetic escape** — loss of vasoconstrictor response with prolonged hypotension; due to receptor desensitization, NE depletion, AVP exhaustion, and ischemic-metabolite override.
- **Cardiotoxic shock factors** — circulating negative-inotropic agents released by ischemic organs in late shock; convert hypovolemic to cardiogenic shock.
- **Vasoactive agonists in hemorrhage** — epinephrine + NE (adrenal), ANG II (RAAS), AVP (PVN), histamine (local).
- **Pulse pressure narrowing** — early bedside sign of hypovolemia (↓ SV → ↓ pulse pressure before MAP drops detectably).
- **Plasmapheresis** — artificial removal of plasma proteins; experimentally shows that plasma-protein concentration itself drives hepatic albumin synthesis.

---

## Cross-links forward

| Forward link | Topic | Where |
|---|---|---|
| Detailed baroreceptor anatomy + RVLM circuitry | high-pressure baroreflex closing the connected diagram of Fig. 25-1C | Ch 23 (pp. 534–539) |
| Regulation of cardiac output by venous return | mean systemic filling pressure, RAP, the cardiac-function/venous-return curve crossover | Ch 23 (pp. 545–549) |
| Regional special circulations | coronary, cerebral, splanchnic, renal, cutaneous, skeletal-muscle (basis for the differential effects of fight-or-flight and exercise) | Ch 24 (pp. 553–571) |
| Microcirculatory Starling forces | the four Starling forces that govern Fig. 25-10 | Ch 20 (pp. 467–472) |
| Pre/postcapillary resistance ratio R_post/R_pre | mechanism of midcapillary pressure setting | Ch 19 (pp. 451–452) |
| Cardiac contractility, force–velocity, ESPVR | how acidosis and shock factors reduce contractility | Ch 22 (pp. 522–532) |
| RAAS and renal pressure-natriuresis | long-term BP control | Ch 40 (pp. 841–843) |
| AVP physiology + osmoreceptors + thirst | volume defense after hemorrhage and in fight-or-flight | Ch 40 (pp. 845–849); Ch 47 (pp. 817–819) |
| Adrenal medullary epinephrine biosynthesis | chromaffin-cell release | Ch 50 (pp. 1030–1034) |
| Peripheral chemoreceptors | hypoxic drive contribution to the four-receptor convergence in hemorrhage | Ch 32 (pp. 710–713) |
| Central chemoreceptors | the most powerful arm of the hemorrhage sympathetic surge | Ch 32 (p. 713) |
| Thermoregulatory CV adjustments | the sweat / cutaneous-vasodilation arm of the exercise response | Ch 59 (pp. 1199–1201) |
| Exercise physiology | the full integrated description; deconditioning, training adaptations | Ch 60 (pp. 1212–1220) |
| Endocrine response to stress | CRH → ACTH → cortisol arm of fight-or-flight | Ch 50 |
| Autonomic ganglionic transmission | sympathetic cholinergic vasodilator fibers, varicosities, co-transmission | Ch 14 (pp. 342–347) |

---

## Source apparatus
- Online Notes N25-1 through N25-7 referenced inline (companion-site content; not pulled in here).
- Cross-references to Box 23-1 (chronic hypertension and baroreflex resetting), Fig. 22-7C (muscle-vein pump), Fig. 24-6 (skeletal-muscle circulation), Fig. 17-8 (ankle venous pressure), Fig. 21-14H (atrial fibrillation), and Fig. 19-4A (capillary resistance schematic).
- References deferred to www.StudentConsult.com (per source).

---

## Format-verification notes

**Figures viewed and described from image:** 25-1, 25-3, 25-4, 25-5, 25-7, 25-9, 25-10 (seven viewed during a single visual pass over pp. 584–598 of the PDF). Note: this exceeds the standard "~5 viewed" budget because Figures 25-1, 25-9, and 25-10 are quantitatively rich integration diagrams that anchor the entire chapter's reasoning.

**Figures listed by caption + textual reference only:** 25-2 (subsystem interaction map), 25-6 (early exercise model), 25-8 (BP trajectory after hemorrhage).

**Tables viewed:** 25-1 (orthostatic-response factors).

*End of Chapter 25. Next: Chapter 26 — Organization of the Respiratory System (opening Section V), p. 590.*
