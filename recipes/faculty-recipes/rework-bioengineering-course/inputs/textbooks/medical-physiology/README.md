# Medical Physiology — Boron & Boulpaep, 3rd ed. — Chapter Markdown

Source: `../Medical physiology (Boron Walter F., Boulpaep Emile L.) 3rd.pdf` (1316 pp., Internet Archive scan, OCR text layer).

Per-chapter markdown files for downstream use in an AI / RAG application. Files are named `chapter-NN-slug.md` and follow a uniform format.

## What each chapter file contains

Each chapter is structured for retrieval, not for re-reading the textbook end-to-end.

1. **YAML frontmatter** — chapter number, title, authors, section, source page range, PDF page range, counts of figures/equations/tables/clinical boxes.
2. **Chapter map** — top-level section list verbatim from the source.
3. **Per-section blocks** — each major source section gets:
   - Verbatim subsection headings.
   - **Core claims** in compact prose.
   - **Citation-anchor quotes** — short (1–3 sentence) verbatim quotes with `(p. X)` anchors. These are the retrieval-ready chunks for a RAG citation system.
   - **Figure descriptions** — see the figure-pass policy below.
   - **Equations** — LaTeX in `$…$` / `$$…$$`.
   - **Tables** — Markdown tables for compact data.
4. **Glossary** — flat term list for downstream chunking.
5. **Cross-links forward** — declared chapter references in the source.
6. **Format-verification notes** — at the bottom of each chapter, lists which figures were visually verified vs. described from caption + textual references.

## Figure-pass policy (current; can be deepened later)

The Internet Archive PDF is a **page scan**, not a vector PDF, so individual figures cannot be isolated programmatically — they have to be viewed page-by-page through a vision model.

**Current policy (fast pass):**
- ~5 representative figures per chapter are visually opened and described in detail from the rendered page image.
- The remaining figures are listed by source caption and described from the surrounding text references in the chapter.
- Each chapter's bottom `Format-verification notes` block enumerates which figures fall in each category, so a future pass knows exactly what is still pending.

**Deeper pass (deferred — do later):**
A second pass would open every figure page individually and produce a multi-paragraph vision description per figure: subpanel-by-subpanel labels, axis descriptions for plots, anatomical labels for diagrams, color coding, and any quantitative annotations. Estimated cost: ~5–10 minutes of model time per chapter, ~5–10 hours total across the book.

**How to run the deeper pass:**
1. Identify the chapter's PDF page range from the file's YAML frontmatter (`pdf_pages` field).
2. Render those pages to PNG:
   ```bash
   pdftoppm -png -r 120 -f <START> -l <END> \
     "../Medical physiology (Boron Walter F., Boulpaep Emile L.) 3rd.pdf" \
     /tmp/ch<NN>/p
   ```
3. For each `Figure 2-x` listed in the chapter, find the page it sits on (search the OCR text layer) and view the corresponding rendered PNG.
4. Replace the `*(listed)*` block with a `*(viewed)*` block containing a subpanel-by-subpanel description.
5. Move the figure from the "described from caption only" list to the "viewed" list in the chapter's footer `Format-verification notes`.

A small driver script could automate steps 1–3; a human (or a second LLM pass) does step 4.

## Quote density

Citation-anchor quotes are kept short — usually 1–3 sentences each. They are intended as **retrieval chunks**, not as a reading substitute for the textbook. If your downstream application needs longer quoted passages (e.g., to support a "quote in context" feature with paragraph-length excerpts), the chapter files should be regenerated with a higher quote-length budget; that is a separate pass.

## What is **not** in these files

- The running prose of the textbook is not reproduced. The files are an outlined + citation-anchored distillation suitable for RAG, not a markdown copy of the book.
- Online "Notes" (€) icons in the source pointing at companion-website content) are flagged inline by ID (e.g., `N1-1`) but their content is not pulled in.
- References sections are deferred to the companion site (the printed book itself does this).

## Source provenance

- Title: *Medical Physiology*, 3rd edition.
- Editors / lead authors: Walter F. Boron and Emile L. Boulpaep.
- Publisher: Elsevier.
- PDF source: Internet Archive (`https://archive.org/details/medicalphysiolog0000unse_u7z1_ed3`).
- PDF mechanical metadata: 1316 pp., 137 MB, scanned at ~564 × 750 pt with OCR layer.
- Use authorization: stated by the project owner as faculty-facing AI-application reformat with permission from the source publisher / authors.

## Page-number convention

- `source_pages` in the YAML refers to **book** page numbers (as printed in the source).
- `pdf_pages` in the YAML refers to **PDF** page numbers (1-indexed in the file).
- For this PDF: `pdf_page = book_page + 12` (the offset comes from the front matter).

## Index

| # | Title | Section | Status |
|---|---|---|---|
| 1 | Foundations of Physiology | I | done |
| 2 | Functional Organization of the Cell | II | done |
| 3 | Signal Transduction | II | done |
| 4 | Regulation of Gene Expression | II | done |
| 5 | Transport of Solutes and Water | II | done |
| 6 | Electrophysiology of the Cell Membrane | II | done |
| 7 | Electrical Excitability and Action Potentials | II | done |
| 8 | Synaptic Transmission and the Neuromuscular Junction | II | done |
| 9 | Cellular Physiology of Skeletal, Cardiac, and Smooth Muscle | II | done |
| 10 | Organization of the Nervous System | III | done |
| 11 | The Neuronal Microenvironment | III | done |
| 12 | Physiology of Neurons | III | done |
| 13 | Synaptic Transmission in the Nervous System | III | done |
| 14 | The Autonomic Nervous System | III | done |
| 15 | Sensory Transduction | III | done |
| 16 | Circuits of the Central Nervous System | III | done |
| 17 | Organization of the Cardiovascular System | IV | done |
| 18 | Blood | IV | done |
| 19 | Arteries and Veins | IV | done |
| 20 | The Microcirculation | IV | done |
| 21 | Cardiac Electrophysiology and the Electrocardiogram | IV | done |
| 22 | The Heart as a Pump | IV | done |
| 23 | Regulation of Arterial Pressure and Cardiac Output | IV | done |
| 24 | Special Circulations | IV | done |
| 25 | Integrated Control of the Cardiovascular System | IV | done |
| 26 | Organization of the Respiratory System | V | done |
| 27 | Mechanics of Ventilation | V | done |
| 28 | Acid-Base Physiology | V | done |
| 29 | Transport of Oxygen and Carbon Dioxide in the Blood | V | done |
| 30 | Gas Exchange in the Lungs | V | done |
| 31 | Ventilation and Perfusion of the Lungs | V | done |
| 32 | Control of Ventilation | V | done |
| 33 | Organization of the Urinary System | VI | done |
| 34 | Glomerular Filtration and Renal Blood Flow | VI | done |
| 35 | Transport of Sodium and Chloride | VI | done |
| 36 | Transport of Urea, Glucose, Phosphate, Calcium, Magnesium, Organic Solutes | VI | done |
| 37 | Transport of Potassium | VI | done |
| 38 | Urine Concentration and Dilution | VI | done |
| 39 | Transport of Acids and Bases | VI | done |
| 40 | Integration of Salt and Water Balance | VI | done |
| 41 | Organization of the Gastrointestinal System | VII | done |
| 42 | Gastric Function | VII | done |
| 43 | Pancreatic and Salivary Glands | VII | done |
| 44 | Intestinal Fluid and Electrolyte Movement | VII | done |
| 45 | Nutrient Digestion and Absorption | VII | done |
| 46 | Hepatobiliary Function | VII | done |
| 47 | Organization of Endocrine Control | VIII | done |
| 48 | Endocrine Regulation of Growth and Body Mass | VIII | done |
| 49 | The Thyroid Gland | VIII | done |
| 50 | The Adrenal Gland | VIII | done |
| 51 | The Endocrine Pancreas | VIII | done |
| 52 | The Parathyroid Glands and Vitamin D | VIII | done |
| 53 | Sexual Differentiation | IX | done |
| 54 | The Male Reproductive System | IX | done |
| 55 | The Female Reproductive System | IX | done |
| 56 | Fertilization, Pregnancy, and Lactation | IX | done |
| 57 | Fetal and Neonatal Physiology | IX | done |
| 58 | Metabolism | X | done |
| 59 | Regulation of Body Temperature | X | done |
| 60 | Exercise Physiology and Sports Science | X | done |
| 61 | Environmental Physiology | X | done |
| 62 | The Physiology of Aging | X | done |

Update the `Status` column as each chapter is generated.
