---
chapter: 50
title: The Adrenal Gland
authors:
  - Eugene J. Barrett
section: "VIII. The Endocrine System"
source_pages: "1018–1034"
pdf_pages: "1030–1046"
source_book: "Boron WF, Boulpaep EL. Medical Physiology, 3rd edition (2017)"
figures_listed: "9"
figures_described_from_image: 5
equations: "few — steroidogenesis is enzymatic-pathway-driven, not equation-driven; LaTeX used for the cholesterol→cortisol/aldosterone reaction chains, the catecholamine pathway, and the cortisol free-fraction relation"
tables: 2
clinical_boxes: "5 (Cushing/Addison; 21α-hydroxylase deficiency / congenital adrenal hyperplasia; glucocorticoid therapy; attacking the RAA axis / Conn; pheochromocytoma)"
---

# Chapter 50 — The Adrenal Gland

> Section VIII · The Endocrine System · pp. 1018–1034 · Author: Eugene J. Barrett

## Chapter map (top-level)

1. **Anatomy and the two glands in one** (p. 1018) — cortex (mesoderm) vs. medulla (neural crest); the three cortical zones and their products.
2. **The adrenal cortex: cortisol** (pp. 1018–1026) — steroidogenesis from cholesterol; the CYP/P-450 enzymes; CBG transport; the glucocorticoid receptor; cortisol's metabolic and anti-inflammatory actions; the hypothalamic-pituitary-adrenal (HPA) axis (CRH → POMC/ACTH → cortisol), negative feedback, diurnal rhythm, and stress.
3. **The adrenal cortex: aldosterone** (pp. 1026–1030) — synthesis via aldosterone synthase in the glomerulosa; renal Na⁺/K⁺ actions; control by the renin-angiotensin-aldosterone system (RAAS) and K⁺ (not ACTH-dominant); 11β-HSD2 conferring mineralocorticoid-receptor specificity.
4. **The adrenal medulla** (pp. 1030–1034) — chromaffin cells as modified postganglionic sympathetic neurons; catecholamine synthesis (tyrosine → epinephrine via PNMT, induced by cortisol); secretion; degradation (COMT/MAO → metanephrines/VMA); adrenoceptors; CNS-driven integrated stress control.

---

## Section 1 — Anatomy and overview (p. 1018)

### Subsection headings
- **Two embryologically distinct glands in one organ** (p. 1018)
- **Three cortical zones, three product classes** (p. 1018)

### Core claims
- Each adrenal gland (~4 g) sits atop a kidney in the retroperitoneum. It is really **two glands**: an outer **cortex** (mesoderm) and an inner **medulla** (neural crest, migrating into the developing cortex).
- The **cortex** produces three classes of steroid: glucocorticoids (cortisol), mineralocorticoids (aldosterone), and adrenal androgens (DHEA/DHEAS). The **medulla** produces the catecholamines epinephrine and norepinephrine.
- **Cortical zonation** (surface → medulla):
  - **Zona glomerulosa** → aldosterone (the only layer with aldosterone synthase).
  - **Zona fasciculata** → cortisol (the principal site).
  - **Zona reticularis** → adrenal androgens (DHEA, androstenedione) and a small amount of cortisol.
- The enzymatic logic of zonation: every zone has SCC and the "vertical" enzymes, but **17α-hydroxylase is essentially absent in the glomerulosa** (so it cannot make cortisol/androgens) and **aldosterone synthase is present only in the glomerulosa** (so only it makes aldosterone).
- **Blood supply** runs cortex → medulla in series, so the medulla is bathed in the highest cortical-steroid concentrations of any tissue — the basis for cortisol's induction of medullary PNMT.

### Citation-anchor quotes
- > "The human adrenal glands, each weighing only ~4 g, are located above the upper pole of each kidney in the retroperitoneal space. They produce four principal hormones: cortisol, aldosterone, epinephrine (adrenaline), and norepinephrine." (p. 1018)
- > "Embryologically, the cortex is derived from mesoderm, whereas the medulla is derived from neural crest cells … that migrate into the developing cortex." (p. 1018)
- > "Cortisol, the principal glucocorticoid, is made in the fasciculata and to a small extent in the reticularis layer." (p. 1018)
- > "The adrenal androgens—dehydroepiandrosterone (DHEA) and its sulfated form DHEAS—are made in the reticularis layer." (p. 1018)

### Figures

#### Figure 50-1 — Anatomy of the adrenal gland *(viewed)*

A cutaway of one adrenal gland sitting on the upper pole of a kidney, with a magnified wedge showing the concentric histological layers and, to the right, the hormone each layer secretes.
- **Capsule** (outermost) → **Zona glomerulosa** → **Zona fasciculata** → **Zona reticularis** → **Medulla** (innermost), then the **medullary vein** draining the center.
- Right-hand "HORMONES" column maps each layer to its product: **Zona glomerulosa → Mineralocorticoid (aldosterone)**; **Zona fasciculata → Glucocorticoids (e.g., cortisol)**; **Zona reticularis → Androgens (DHEA and androstenedione)**; **Medulla → Epinephrine**.
- A **preganglionic sympathetic terminal** is drawn synapsing on the medullary chromaffin cells, making explicit that the medulla is innervated like a sympathetic ganglion.
- The caption stresses the **series blood flow**: "The blood supply enters the cortex in the subcapsular region and flows through anastomotic capillary beds while coursing through first the cortex and then the medulla." (p. 1019) — this portal-like arrangement exposes the medulla to high glucocorticoid concentrations.

---

## Section 2 — The adrenal cortex: cortisol (pp. 1018–1026)

### Subsection headings
- **Cortisol is the primary glucocorticoid hormone in humans** (pp. 1018–1020)
- **The adrenal zona fasciculata converts cholesterol to cortisol** (pp. 1019–1021)
- **Cortisol binds to a cytoplasmic receptor that translocates to the nucleus and modulates transcription in multiple tissues** (pp. 1022–1023)
- **CRH from the hypothalamus stimulates anterior pituitary corticotrophs to secrete ACTH, which stimulates the adrenal cortex to synthesize and secrete cortisol** (pp. 1023–1025)
- **Cortisol exerts negative feedback on CRH and ACTH secretion, whereas stress acts through higher CNS centers to stimulate the axis** (pp. 1025–1026)

### Core claims — steroidogenesis
- All steroids start from **cholesterol**, which the adrenal obtains chiefly by **LDL-receptor-mediated endocytosis** (quantitatively dominant) and secondarily by **de novo synthesis from acetate**.
- The **rate-limiting step** is delivery of cholesterol to, and cleavage by, the **side-chain-cleavage (SCC) enzyme** in the mitochondrion. **StAR protein** (steroidogenic acute regulatory protein) governs cholesterol delivery to the inner mitochondrial membrane; ACTH/cAMP acutely increases this flux.
- **Cortisol pathway (fasciculata)** — five steps:

  $$\text{cholesterol} \xrightarrow{\text{SCC (CYP11A1)}} \text{pregnenolone} \xrightarrow{\text{3β-HSD}} \text{progesterone} \xrightarrow{\text{17α-OHase (CYP17)}} \text{17α-OH-progesterone}$$
  $$\xrightarrow{\text{21α-OHase (CYP21)}} \text{11-deoxycortisol} \xrightarrow{\text{11β-OHase (CYP11B1)}} \textbf{cortisol}$$

  (The book also notes the parallel branch through 17α-OH-pregnenolone, with 3β-HSD acting after the 17-hydroxylation.)
- **Adrenal androgen pathway (reticularis)**: the **same CYP17 enzyme** also has **17,20-desmolase (lyase)** activity, cleaving 17α-OH-pregnenolone / 17α-OH-progesterone to **DHEA / androstenedione**. Peripheral 17β-HSD can then make testosterone. The rise in adrenal androgens before puberty is **adrenarche**.
- **Cholesterol is 27 carbons**; SCC removes carbons 22–27 to yield the 21-carbon pregnenolone — the corticosteroid backbone.
- Why each zone makes its product: SCC + the "vertical" enzymes (3β-HSD, 21α-OHase, 11β-OHase) are in **all three zones**; **17α-hydroxylase is absent from the glomerulosa** (→ no cortisol/androgen there) and **aldosterone synthase is present only in the glomerulosa**.

### Core claims — transport, receptor, actions
- **Transport**: ~90% of plasma cortisol is bound to **corticosteroid-binding globulin (CBG / transcortin**, a hepatic glycoprotein with ~30× higher affinity for cortisol than aldosterone), ~7% to albumin; only **3–4% is free** and bioactive.

  $$\text{cortisol}_{\text{total}} \approx \underbrace{0.90}_{\text{CBG}} + \underbrace{0.07}_{\text{albumin}} + \underbrace{0.03\text{–}0.04}_{\text{free, active}}$$

- **Clearance / interconversion**: **11β-HSD1** (liver, adipose) reversibly converts **cortisone ⇌ cortisol** (regenerating active hormone); **11β-HSD2** (kidney distal nephron, adrenal) **irreversibly** converts **cortisol → cortisone** (inactivation).
- **Receptor**: the **glucocorticoid receptor (GR)** sits in the cytoplasm bound to chaperones (hsp90). Cortisol crosses the membrane freely, binds GR, the chaperone dissociates, and the cortisol-GR **homodimer** translocates to the nucleus to bind **glucocorticoid response elements (GREs)**, up- or down-regulating transcription. There is also a fast **nongenomic** feedback on ACTH release.
- **Metabolic actions** (catabolic, glucose-mobilizing):
  - **Liver**: induces gluconeogenic and amino-acid-metabolizing enzymes → ↑ hepatic glucose/glycogen.
  - **Muscle**: ↑ protein breakdown → amino acids exported to liver.
  - **Adipose**: ↑ lipolysis → fatty acids (fuel) + glycerol (gluconeogenic substrate); paradoxically deposits central fat (moon facies, buffalo hump).
- **Other actions**: potent **anti-inflammatory / immunosuppressive** (basis of clinical use and of Cushing-type infection risk); **permissive** on catecholamines (vascular tone); **bone**: ↓ osteoblast activity + ↓ gut Ca²⁺ absorption → osteoporosis with chronic use; **CNS**: mood/cognition effects.

### Core claims — HPA axis, feedback, rhythm, stress
- **Axis**: hypothalamic paraventricular neurons release **CRH** (41-aa) into the hypophyseal portal blood → corticotrophs bind CRH on **CRH-R1** (Gαs → cAMP → PKA → L-type Ca²⁺ channels → exocytosis of ACTH) → **ACTH** acts on **MC2R** (melanocortin-2 receptor; Gαs → cAMP → PKA) on all three cortical layers, but only fasciculata/reticularis (which have 17α-OHase) make cortisol.
- **POMC**: ACTH is cleaved from **pro-opiomelanocortin (POMC)**. Anterior-lobe processing → N-terminal peptide, J-peptide, **ACTH**, β-LPH. The melanocortins (ACTH, α/β/γ-MSH) act on **MC1R** in melanocytes → hyperpigmentation when ACTH is grossly elevated (Addison, ectopic ACTH).
- **AVP** is a secondary ACTH secretagogue, important in stress (dehydration, trauma).
- **ACTH's adrenal actions**: acute (stimulate SCC / cholesterol→pregnenolone) and chronic (induce all the P-450 enzymes, the LDL receptor, and HMG-CoA reductase; cause adrenal **growth**). Without ACTH the fasciculata/reticularis **atrophy** (iatrogenic insufficiency on stopping steroids), but the **glomerulosa does not atrophy** because ANG II and K⁺ are its trophic factors.
- **Negative feedback**: cortisol inhibits both **corticotrophs** (POMC transcription + release of stored ACTH) and **CRH neurons** (less important). ACTH itself short-loops back onto the hypothalamus.
- **Diurnal rhythm**: ACTH/cortisol peak in **early morning**, trough in late evening; the suprachiasmatic nucleus (retinal input) drives the rhythm — blind people can lose it. Superimposed **pulsatile** CRH bursts make ACTH pulsatile; cortisol's longer half-life damps and broadens its pulses.
- **Stress** (physical, psychological, biochemical e.g. **hypoglycemia**) ↑ CRH → ↑ ACTH → ↑ cortisol via increased **amplitude** of CRH bursts.

### Citation-anchor quotes
- > "The ability of cortisol to increase plasma [glucose] largely results from its ability to enhance mobilization of amino acids from proteins in many tissues and to enhance the ability of the liver to convert these amino acids into glucose and glycogen by activating gluconeogenesis." (p. 1018)
- > "This enzyme, or the supply of substrate to it, appears to be the rate-limiting step for the overall process of steroid hormone synthesis." (p. 1020)
- > "Thus, only 3% to 4% of the circulating cortisol is free." (p. 1021)
- > "11β-HSD2 … catalyzes an essentially irreversible conversion of cortisol to cortisone. This breakdown of cortisol allows aldosterone to regulate the relatively nonspecific mineralocorticoid receptor (MR) without interference from cortisol." (p. 1021)
- > "Binding of cortisol causes the chaperone to dissociate from the GR and this allows the cortisol-GR complex to translocate to the nucleus." (p. 1022)
- > "CRH stimulates the release of ACTH, also called corticotropin, from the anterior pituitary. ACTH directly stimulates the adrenal fasciculata layers to synthesize and secrete cortisol. Circulating cortisol exerts negative-feedback control on the release of both ACTH and CRH." (p. 1023)
- > "In the absence of pituitary ACTH, the fasciculata and reticularis layers of the adrenal cortex atrophy. The glomerulosa layer does not atrophy under these conditions because in addition to ACTH, angiotensin II (ANG II) and high levels of K⁺ are trophic factors that act on the glomerulosa layer." (p. 1023)
- > "ACTH secretory activity is greatest in the early morning and diminishes late in the afternoon and early evening." (p. 1026)

### Figures

#### Figure 50-2 — Biosynthesis of adrenal steroids *(viewed)*

A grid of steroid structures (chemical skeletons shown for each product) laying out the entire steroidogenic tree from cholesterol. Reading the layout:
- **Top:** acetate → **cholesterol (27 C)** → (SCC / 20,22-desmolase) → **pregnenolone**.
- **Vertical "down" enzymes** (boxed, run in all three zones): **3β-HSD** (pregnenolone→progesterone), then **21α-hydroxylase**, then **11β-hydroxylase**.
- **Horizontal "rightward" enzyme**: **17α-hydroxylase** (and its **17,20-desmolase/lyase** activity), converting the pregnenolone/progesterone column into the 17α-hydroxy column and then the androgen column (**DHEA, androstenedione, → testosterone**).
- **Three product blocks at right**, color-coded:
  - **Glucocorticosteroids** (cortisol; cortisone shown as the inactive 11-keto partner).
  - **Mineralocorticosteroids** (11-deoxycorticosterone → corticosterone → **aldosterone**), explicitly tagged **"Glomerulosa cells only"** for the corticosterone→aldosterone step (aldosterone synthase).
  - The androgen/sex-steroid block (DHEA/androstenedione/testosterone), with a forward pointer to the gonadal-steroid figures (Figs 54-6, 55-8).
- Caption note carried into the text: a **block in 21α-hydroxylase diminishes both cortisol and aldosterone and shunts precursors into androgen excess** — the mechanism of congenital adrenal hyperplasia (Box 50-2). "The chemical groups modified by each enzyme are highlighted in the reaction product." (p. 1020)

> Vision note: this is the keystone figure for any RAG query about which enzyme makes which product, why glomerulosa makes only aldosterone (no 17α-OHase) and only it makes aldosterone (aldosterone synthase), and how 21-hydroxylase deficiency produces salt-losing virilizing CAH.

#### Figure 50-3 — Hypothalamic-pituitary-adrenocortical axis *(viewed)*

A whole-axis schematic from cerebral cortex down to the adrenal, with two inset signaling-cascade panels.
- **Top:** cerebral cortex and inputs labeled **diurnal rhythms** and **physical / biochemical stress** feeding the **paraventricular nucleus**, whose small-bodied neurons make **CRH**.
- **Portal vessels** carry CRH down the pituitary stalk to the **anterior lobe corticotroph**.
- **Inset 1 (corticotroph):** CRH → **CRH receptor (GPCR)** → AC → cAMP → PKA → L-type Ca²⁺ channel → ↑[Ca²⁺]ᵢ → exocytosis of **ACTH**; CRH also drives **POMC** transcription.
- ACTH travels in the blood to the **adrenal cortex cell**.
- **Inset 2 (adrenal cortex cell):** ACTH → **melanocortin-2 receptor (MC2R)** → AC → cAMP → PKA → rapid cholesterol→pregnenolone conversion + slower induction of steroidogenic proteins → **cortisol**.
- **Feedback arrows:** cortisol negative-feeds-back on both the **pituitary** and the **hypothalamus**; ACTH short-loops back on the hypothalamus.
- The adrenal **medulla** is drawn at the bottom of the gland, anatomically downstream of the cortical blood flow.

#### Figure 50-4 — Processing of POMC *(listed)*

Linear maps of the POMC precursor showing differential cleavage in two pituitary lobes. **Anterior lobe:** N-terminal peptide · J-peptide · **ACTH** · β-LPH. **Intermediate lobe** (important only in fetal life/pregnancy): N-terminal peptide · γ-MSH · J-peptide · α-MSH · CLIP · γ-LPH · β-endorphin. Numbers mark residue boundaries. Explains why ACTH oversecretion co-produces melanotropic peptides (hyperpigmentation).

#### Figure 50-5 — Rhythm of ACTH and cortisol release *(listed)*

Two stacked time-courses over 24 h (midnight → noon → midnight): episodic **ACTH** bursts (brief, reflecting ACTH's short plasma half-life) and the **cortisol** curve they drive (broader, damped, lagging). Both peak in the early morning and fall through the day — the circadian + pulsatile pattern.

---

## Section 3 — The adrenal cortex: aldosterone (pp. 1026–1030)

### Subsection headings
- **The mineralocorticoid aldosterone is the primary regulator of salt balance and extracellular volume** (pp. 1026)
- **The glomerulosa cells synthesize aldosterone from cholesterol via progesterone** (pp. 1026–1027)
- **Aldosterone stimulates Na⁺ reabsorption and K⁺ excretion by the renal tubule** (pp. 1027–1028)
- **Angiotensin II, K⁺, and ACTH all stimulate aldosterone secretion** (pp. 1027–1029)
- **Aldosterone exerts indirect negative feedback on the renin-angiotensin axis** (pp. 1029–1030)

### Core claims
- **Aldosterone = primary regulator of extracellular volume** (and thus arterial pressure) via renal Na⁺ handling. Contrast with **AVP**, the primary regulator of plasma osmolality (free-water balance).
- **Synthesis (glomerulosa)** — diverges from cortisol because the glomerulosa lacks 17α-OHase and uniquely has **aldosterone synthase (CYP11B2)**:

  $$\text{cholesterol} \xrightarrow{\text{SCC}} \text{pregnenolone} \xrightarrow{\text{3β-HSD}} \text{progesterone} \xrightarrow{\text{21α-OHase}} \text{11-deoxycorticosterone (DOC)}$$
  $$\xrightarrow{\text{11β-OHase}} \text{corticosterone} \xrightarrow{\text{aldosterone synthase (CYP11B2)}} \textbf{aldosterone}$$

  Aldosterone synthase (18-methyloxidase, an isoform of 11β-hydroxylase) does the final **11β-hydroxylation + 18-methyl hydroxylation + 18-methyl oxidation** to install the C-18 aldehyde.
- **No storage pool** — secretion is limited by synthesis rate.
- **Plasma binding**: ~37% free, ~21% CBG, ~42% albumin (much less protein-bound than cortisol).
- **Renal actions** (principal cells, distal tubule + collecting duct): ↑ transcription of the **Na-K pump**, ↑ apical **ENaC Na⁺ channels**, ↑ an Na/K/Cl cotransporter → **net ↑ Na⁺ reabsorption and ↑ K⁺ secretion** (K⁺ loss is secondary to Na⁺ reabsorption). Also a rapid **nongenomic** effect via **GPR30**.
- **Three secretagogues** (Fig. 50-6), in order of importance:
  1. **Angiotensin II** (RAAS): AT₁ receptor → Gαq → PLC → DAG/IP₃ → ↑[Ca²⁺]ᵢ → ↑ pregnenolone production + ↑ aldosterone synthase.
  2. **↑ plasma [K⁺]**: directly depolarizes the glomerulosa cell → voltage-gated Ca²⁺ entry → ↑[Ca²⁺]ᵢ (no PLC needed); synergizes with ANG II.
  3. **ACTH**: MC2R → cAMP/PKA — present but **weak**; ACTH is **not** the dominant aldosterone regulator (unlike for cortisol).
- **The 11β-HSD2 problem solved**: MR in the kidney binds cortisol and aldosterone with **similar affinity**, and cortisol circulates ~100–1000× higher than aldosterone. **11β-HSD2 in MR target cells irreversibly converts cortisol → cortisone (low MR affinity)**, "confer[ring] aldosterone specificity on the MR." (Defects / licorice → apparent mineralocorticoid excess.)
- **Indirect feedback**: aldosterone raises effective circulating volume (Na⁺ retention) and lowers plasma [K⁺]; both reduce the stimuli (renin, K⁺) that drove aldosterone. ANG II also short-loops to inhibit renin and raises arterial pressure.

### Citation-anchor quotes
- > "Aldosterone determines extracellular volume by controlling the extent to which the kidney excretes or reabsorbs the Na⁺ filtered at the renal glomerulus." (p. 1026)
- > "Because glomerulosa cells are the only ones that contain aldosterone synthase, these cells are the exclusive site of aldosterone synthesis." (p. 1026)
- > "Although ACTH also stimulates the production of aldosterone in the glomerulosa cell, increases in extracellular [K⁺] and the peptide hormone ANG II are physiologically more important secretagogues." (p. 1027)
- > "Surprisingly, MR in the kidney has a similar affinity for aldosterone and cortisol." (p. 1027)
- > "Thus, the presence of 11β-HSD2 effectively confers aldosterone specificity on the MR." (p. 1027)
- > "The net effect of these actions is to increase Na⁺ reabsorption and K⁺ secretion." (p. 1028)
- > "Three secretagogues control aldosterone synthesis by the glomerulosa cells of the adrenal cortex. The most important is ANG II … An increase in plasma [K⁺] is also a powerful stimulus … Third, just as ACTH promotes cortisol secretion, it also promotes the secretion of aldosterone, although this effect is weak." (p. 1027)

### Figures

#### Figure 50-6 — Control of aldosterone secretion *(viewed)*

A three-color flow diagram converging on the glomerulosa cell, then showing the downstream renal consequences and feedback.
- **Green (renin-angiotensin cascade):** ↓ effective circulating volume → JGA granular cells release **renin** → angiotensinogen (liver) → **ANG I** → (**ACE**, mostly lung) → **ANG II** → glomerulosa AT₁ receptor.
- **Blue (ACTH):** brain → CRH/AVP → anterior pituitary → **ACTH** → glomerulosa MC2R (weak input).
- **Red (K⁺):** **↑ plasma [K⁺]** → direct depolarization of the glomerulosa cell.
- All three converge on **↑ aldosterone synthesis**.
- **Downstream (renal effects):** aldosterone → ↑ renal **Na⁺ reabsorption** / ↓ Na⁺ excretion, ↑ H₂O retention, **↑ K⁺ excretion** → ↓ plasma [K⁺]; ↑ effective circulating volume → ↑ extracellular fluid volume → ↑ **blood pressure**.
- **Feedback loops** close back onto renin (volume/pressure up → renin down) and onto K⁺ (K⁺ excreted → plasma K⁺ falls → glomerulosa stimulation falls).

#### Figure 50-7 — Structure of the JGA *(listed)*

Anatomy of the juxtaglomerular apparatus at the glomerular pole: afferent and efferent arterioles, **granular (juxtaglomerular) cells** in the afferent arteriole wall (renin source), **macula densa** cells of the early distal tubule, extra/intraglomerular mesangial cells, podocytes, Bowman's space, and glomerular capillaries. Establishes where the volume/pressure/NaCl signals that govern renin are sensed.

---

## Section 4 — The adrenal medulla (pp. 1030–1034)

### Subsection headings
- **The adrenal medulla bridges the endocrine and sympathetic nervous systems** (pp. 1030)
- **Only chromaffin cells of the adrenal medulla have the enzyme for epinephrine synthesis** (pp. 1030–1032)
- **Catecholamines bind to α and β adrenoceptors on the cell surface and act through heterotrimeric G proteins** (pp. 1033–1034)
- **The CNS-epinephrine axis provides integrated control of multiple functions** (pp. 1033–1034)

### Core claims
- **Chromaffin cells** are the **structural and functional equivalents of postganglionic sympathetic neurons** — neural-crest-derived, innervated by **preganglionic splanchnic fibers** that release **ACh** onto **nicotinic** receptors. They secrete mainly **epinephrine** (and less norepinephrine); virtually all **circulating epinephrine comes from the medulla**.
- **Catecholamine synthesis** (from tyrosine), with cellular compartmentalization:

  $$\text{tyrosine} \xrightarrow[\text{(rate-limiting)}]{\text{tyrosine hydroxylase}} \text{L-DOPA} \xrightarrow{\text{aromatic AA decarboxylase}} \text{dopamine} \xrightarrow{\text{dopamine β-hydroxylase}} \text{norepinephrine} \xrightarrow{\text{PNMT}} \textbf{epinephrine}$$

  - **Tyrosine hydroxylase** is rate-limiting; induced by sympathetic stimulation and ACTH.
  - Dopamine is pumped into chromaffin granules by **VMAT1** (a catecholamine–H⁺ exchanger); **dopamine β-hydroxylase** acts inside the granule.
  - In ordinary sympathetic neurons the pathway **stops at norepinephrine**.
  - **PNMT** (phenylethanolamine-N-methyltransferase) — present in substantial amounts **only in adrenal chromaffin cells** — methylates NE → Epi. **PNMT is induced by cortisol** delivered via the cortical-medullary portal circulation, linking the CRH-ACTH-cortisol axis to the epinephrine response.
- **Storage / secretion**: catecholamines (up to ~0.5 M) bind **chromogranins** + ATP + Ca²⁺ in dense-core granules (osmotically inactivated). Splanchnic ACh → nicotinic depolarization → voltage-gated Ca²⁺ entry → exocytosis. **Chromogranin A** release is a clinical marker of medullary activity.
- **Degradation** (Fig. 50-8B): **COMT** (endothelium, heart, liver, kidney) converts epinephrine → **metanephrine** and NE → **normetanephrine**; **MAO** then yields **vanillylmandelic acid (VMA)**. Liver/gut conjugate to sulfate/glucuronide for urinary excretion. Urinary **catecholamines, metanephrines, and VMA** index total catecholamine production (basis of pheochromocytoma workup).
- **Receptors**: epinephrine and NE bind **α- and β-adrenoceptors**, all **GPCRs**, each binding both ligands with different affinities (Ahlquist's α = mostly excitatory, β = mostly inhibitory; refined into ≥3 β and ≥2 α subtypes, Table 14-2). **β** couple to **Gαs** (↑cAMP); **α₂** to **Gαi** (↓cAMP); **α₁** to **Gαq** (↑IP₃/Ca²⁺). Lefkowitz and Kobilka shared the 2012 Nobel for GPCR work.
- **No endocrine feedback loop** governs medullary secretion — control is purely **CNS/neural**. Example: mild **hypoglycemia** (<~3.5 mM) triggers central sympathetic outflow → epinephrine release → hepatic glycogenolysis + α-adrenergic suppression of insulin → restores glucose. The integrated **fight-or-flight** response (↑ HR/contractility, fuel mobilization, bronchodilation, piloerection, pupil dilation) is activated within seconds.

### Citation-anchor quotes
- > "Chromaffin cells are the structural and functional equivalents of the postganglionic neurons in the sympathetic nervous system." (p. 1030)
- > "Virtually all the circulating epinephrine, the principal product of the adrenal medulla, comes from the adrenal medulla." (pp. 1030–1031)
- > "The activity of the first enzyme in the pathway, tyrosine hydroxylase, which converts tyrosine to L-dopa, is rate limiting for overall synthesis." (p. 1031)
- > "Substantial amounts of this enzyme are present only in the cytosol of adrenal chromaffin cells." (p. 1031) — on PNMT.
- > "Second, cortisol transported from the adrenal cortex by the portal circulation to the medulla upregulates PNMT in chromaffin cells." (pp. 1031–1032)
- > "Circulating catecholamines are degraded first by the enzyme catechol-O-methyltransferase (COMT) … A second enzyme, monoamine oxidase, converts these metabolites to vanillylmandelic acid (VMA)." (p. 1032)
- > "Unlike in other glandular tissue, no endocrine feedback loop governs the secretion of adrenal medullary hormones. Control of catecholamine secretion resides within the CNS." (p. 1034)

### Figures

#### Figure 50-8 — Synthesis and degradation of catecholamines *(viewed)*

Two-panel figure.
- **Panel A (synthesis):** vertical chain of chemical structures **tyrosine → L-DOPA → dopamine → norepinephrine → epinephrine**, with each enzyme named at its arrow: **tyrosine hydroxylase** (with a horizontal arrow flagged "Sympathetic stimulation; ACTH" indicating induction), **amino-acid decarboxylase**, **dopamine β-hydroxylase** (also induced by sympathetic stimulation/ACTH), and the final **PNMT** step labeled "**Cortisol from adrenal cortex via portal circulation**" — visually encoding cortisol's induction of the epinephrine-forming step.
- **Panel B (degradation):** a 2×2 grid: **epinephrine** and **norepinephrine** (left column) are converted by **COMT** to **metanephrine** and **normetanephrine** (right column); **MAO** acts on both rows to yield **dihydroxymandelic acid** and ultimately **vanillylmandelic acid (VMA, in urine)**. Lays out the metabolite panel used to diagnose pheochromocytoma.

#### Figure 50-9 — Cellular view of catecholamine synthesis *(listed)*

A single chromaffin cell showing the **four enzymatic + three transport steps**: cytosolic TH (tyrosine→L-DOPA) and AADC (L-DOPA→dopamine); **VMAT1** transports dopamine into the **chromaffin granule**, where DBH makes NE; NE exits to cytosol, **PNMT** makes epinephrine, and VMAT1 re-imports epinephrine into the granule for storage (granule H⁺-ATPase maintains the proton gradient). Both Epi and NE are stored before secretion.

---

## Tables

### Table 50-1 — Relative potency of glucocorticoid and mineralocorticoid analogs

Potency reflects combined half-life and receptor affinity; cortisol = 1 reference.

| Compound | Glucocorticoid effect | Mineralocorticoid effect |
|---|---|---|
| Cortisol | 1 | ~1 (reference) |
| Prednisone | 3–4 | 0.5 |
| Methylprednisone | 10 | 0.5 |
| Dexamethasone | 20 | 1 |
| Fludrocortisone | 12 | 125 |

*Dexamethasone: high glucocorticoid, minimal mineralocorticoid (used in suppression testing). Fludrocortisone: the clinical mineralocorticoid (Addison replacement).*

### Table 50-2 — Cytochrome P-450 enzymes in steroidogenesis

| Enzyme | Synonym | Gene |
|---|---|---|
| Cholesterol side-chain cleavage | P-450scc | CYP11A1 |
| 11β-hydroxylase | P-450c11 | CYP11B1 |
| 17α-hydroxylase | P-450c17 | CYP17 |
| 17,20-desmolase (lyase) | P-450c17 | CYP17 (same enzyme) |
| 21α-hydroxylase | P-450c21 | CYP21A2 |
| Aldosterone synthase (18-methyloxidase) | P-450aldo | CYP11B2 |
| Aromatase | P-450arom | CYP19 (estrogen synthesis) |

*3β-HSD is **not** a P-450 enzyme (it is an SER dehydrogenase) and so is not in this table, though it is a required step.*

---

## Glossary

- **Zona glomerulosa / fasciculata / reticularis** — aldosterone / cortisol / adrenal androgens.
- **StAR protein** — delivers cholesterol to inner mitochondrial membrane; gates the rate-limiting SCC step.
- **SCC / CYP11A1 (P-450scc, 20,22-desmolase)** — cholesterol → pregnenolone; rate-limiting.
- **3β-HSD** — pregnenolone → progesterone (non-P-450).
- **17α-hydroxylase / 17,20-desmolase (CYP17)** — one enzyme; hydroxylation + androgen lyase; absent in glomerulosa.
- **21α-hydroxylase (CYP21)** — deficiency → salt-losing virilizing congenital adrenal hyperplasia.
- **11β-hydroxylase (CYP11B1)** — final step to cortisol.
- **Aldosterone synthase (CYP11B2)** — glomerulosa-only; makes the C-18 aldehyde.
- **CBG / transcortin** — carries ~90% of plasma cortisol; only 3–4% free.
- **11β-HSD1 / 11β-HSD2** — cortisone⇌cortisol (regenerating) / cortisol→cortisone (inactivating, confers MR aldosterone-specificity).
- **GR / MR** — glucocorticoid / mineralocorticoid receptors; nuclear-receptor superfamily; GREs.
- **CRH → POMC/ACTH → cortisol** — the HPA axis; MC2R on adrenal cortex.
- **POMC** — precursor of ACTH, MSH, LPH, β-endorphin; source of hyperpigmentation.
- **Diurnal rhythm** — ACTH/cortisol peak early morning; suprachiasmatic-nucleus driven.
- **RAAS** — renin → ANG I → (ACE) → ANG II → AT₁ → aldosterone; dominant aldosterone control.
- **Chromaffin cell** — modified postganglionic sympathetic neuron; ACh/nicotinic driven.
- **Tyrosine hydroxylase** — rate-limiting catecholamine enzyme.
- **PNMT** — NE → Epi; adrenal-medulla-specific; cortisol-induced.
- **VMAT1** — vesicular catecholamine–H⁺ exchanger.
- **COMT / MAO** — catecholamine degradation → metanephrines / VMA (urinary diagnosis).
- **α / β adrenoceptors** — all GPCRs; β-Gαs, α₂-Gαi, α₁-Gαq.
- **Cushing / Addison / CAH / Conn / pheochromocytoma** — the five clinical syndromes.

---

## Clinical boxes (source apparatus)

- **Box 50-1 — Cushing syndrome and Addison disease.** Cushing = glucocorticoid excess (truncal adiposity, moon facies, hypertension, easy bruising, osteopenia, muscle wasting, hyperglycemia); "Cushing disease" = pituitary-ACTH cause. Addison = primary adrenal insufficiency (now mostly autoimmune): ↑ ACTH/POMC → hyperpigmentation; hypoglycemia, hypotension, hyponatremia, **hyperkalemia** (aldosterone loss); once uniformly fatal.
- **Box 50-2 — 21α-hydroxylase deficiency (congenital adrenal hyperplasia).** Most common steroidogenic defect; ↓ cortisol + aldosterone, precursor shunt → **androgen excess**; salt-losing, virilizing; ACTH-driven adrenal hyperplasia; ambiguous genitalia in female infants.
- **Box 50-3 — Therapy with glucocorticoids.** Iatrogenic Cushing: fat redistribution (buffalo hump, moon facies), skin thinning, osteopenia, infection risk, proximal myopathy, insulin resistance/diabetes.
- **Box 50-4 — Treating hypertension by attacking the RAA axis.** Aldosterone antagonists (spironolactone, eplerenone), ACE inhibitors, ARBs, direct renin inhibitors.
- **Box 50-5 — Pheochromocytoma.** Catecholamine-secreting tumor of medulla/extra-adrenal chromaffin tissue: paroxysmal hypertension, tachycardia, headache, sweating, anxiety, tremor, glucose intolerance; diagnosed by serum/urinary catecholamines + metabolites; resected.

---

## Cross-links forward

| Forward link | Topic | Where |
|---|---|---|
| The endocrine pancreas | insulin, glucose counter-regulation, metabolic syndrome | Ch 51 |
| Adrenal androgens → gonadal steroids | DHEA → testosterone/estrogen pathways | Ch 54, 55 |
| Renin-angiotensin-aldosterone / renal Na⁺ handling | RAAS, distal Na⁺/K⁺ transport, JGA | Ch 33, 35, 40 |
| Sympathetic nervous system / fight-or-flight | autonomic control, adrenoceptor subtypes | Ch 14 |
| Hypothalamic-pituitary control | portal system, POMC neurons | Ch 47 |
| Nuclear-receptor signaling / GREs | steroid-receptor transcriptional mechanism | Ch 3, 4 |
| Bone / Ca²⁺ effects of glucocorticoids | osteoblast suppression, gut Ca²⁺ | Ch 52 |

## Source apparatus
- Online Notes N50-1 … N50-6 referenced inline (Addison signs; ANG metabolism; glomerulosa K⁺ channels; Conn/hyperaldosteronism; PNMT; adrenoceptor Nobel).
- Clinical boxes: 50-1 through 50-5 (summarized above).
- References deferred (StudentConsult).

---

## Format-verification notes

**Figures viewed and described from image:** 50-1 (adrenal anatomy/zonation), 50-2 (steroidogenesis tree), 50-3 (HPA axis), 50-6 (control of aldosterone secretion), 50-8 (catecholamine synthesis + degradation).

**Figures listed by caption + textual reference only:** 50-4 (POMC processing), 50-5 (ACTH/cortisol rhythm), 50-7 (JGA structure), 50-9 (cellular catecholamine synthesis).

*End of Chapter 50. Next: Chapter 51 — The Endocrine Pancreas, p. 1035.*
