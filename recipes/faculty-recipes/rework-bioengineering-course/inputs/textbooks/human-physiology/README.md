# Human Physiology — Fox & Rompolski, 16th ed. — Chapter Markdown

Source: `../Human Physiology, 16th Edition.pdf` (833 pp., born-digital, McGraw-Hill, 2022).

Per-chapter markdown files for downstream use in an AI / RAG application. Files are named `chapter-NN-slug.md` and follow a uniform format that matches the sibling `medical-physiology/` run.

## What each chapter file contains

Each chapter is structured for retrieval, not for re-reading the textbook end-to-end.

1. **YAML frontmatter** — chapter number, title, authors, source page range, PDF page range, counts of figures/equations/tables/clinical boxes.
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

This is a born-digital PDF (Adobe InDesign source), but figures are not isolable through `pdfimages` because the file is print-flattened. Figures are accessed by rendering each containing page with `pdftoppm` and viewing through a vision model.

**Current policy (fast pass):**
- ~5 representative figures per chapter are visually opened and described in detail from the rendered page image.
- The remaining figures are listed by source caption and described from the surrounding text references in the chapter.
- Each chapter's bottom `Format-verification notes` block enumerates which figures fall in each category, so a future pass knows exactly what is still pending.

**Deeper pass (deferred — do later):**
A second pass would open every figure page individually and produce a multi-paragraph vision description per figure: subpanel-by-subpanel labels, axis descriptions for plots, anatomical labels for diagrams, color coding, and any quantitative annotations.

**How to run the deeper pass:**
1. Identify the chapter's PDF page range from the file's YAML frontmatter (`pdf_pages` field).
2. Render those pages to PNG:
   ```bash
   pdftoppm -png -r 120 -f <START> -l <END> \
     "../Human Physiology, 16th Edition.pdf" \
     /tmp/hp_ch<NN>/p
   ```
3. For each `Figure NN.x` listed in the chapter, find the page it sits on and view the corresponding rendered PNG.
4. Replace the `*(listed)*` block with a `*(viewed)*` block containing a subpanel-by-subpanel description.
5. Move the figure from the "described from caption only" list to the "viewed" list in the chapter's footer.

## Quote density

Citation-anchor quotes are kept short — usually 1–3 sentences each. They are intended as **retrieval chunks**, not a reading substitute for the textbook.

## What is **not** in these files

- The running prose of the textbook is not reproduced. The files are an outlined + citation-anchored distillation suitable for RAG, not a markdown copy of the book.
- "Clinical Investigation" boxes are flagged inline by case name but their full prose is paraphrased, not reproduced.
- End-of-chapter "Test Your Knowledge" questions are not reproduced; "Test Your Quantitative Ability" computational examples are noted briefly.
- Glossary, appendices, and end-of-book index are deferred.

## Source provenance

- Title: *Human Physiology*, sixteenth edition.
- Authors: Stuart Ira Fox (Pierce College) and Krista Rompolski (Moravian College).
- Publisher: McGraw-Hill, 2022.
- ISBN: 978-1-260-59766-0.
- PDF mechanical metadata: 833 pp., 342 MB, born-digital (Adobe InDesign CS6 source; PDF 1.6).
- Use authorization: stated by the project owner as faculty-facing AI-application reformat with permission from the source publisher / authors.

## Page-number convention

- `source_pages` in the YAML refers to **book** page numbers (as printed in the source).
- `pdf_pages` in the YAML refers to **PDF** page numbers (1-indexed in the file).
- For this PDF: `pdf_page = book_page + 23` (the offset comes from the front matter).

## Index

| # | Title | Source pp. | PDF pp. | Status |
|---|---|---|---|---|
| 1 | The Study of Body Function | 1–23 | 24–46 | done |
| 2 | Chemical Composition of the Body | 24–48 | 47–71 | done |
| 3 | Cell Structure and Genetic Control | 49–85 | 72–108 | done |
| 4 | Enzymes and Energy | 86–103 | 109–126 | done |
| 5 | Cell Respiration and Metabolism | 104–127 | 127–150 | done |
| 6 | Interactions Between Cells and the Extracellular Environment | 128–159 | 151–182 | done |
| 7 | The Nervous System | 160–203 | 183–226 | pending |
| 8 | The Central Nervous System | 204–241 | 227–264 | pending |
| 9 | The Autonomic Nervous System | 242–264 | 265–287 | pending |
| 10 | Sensory Physiology | 265–314 | 288–337 | pending |
| 11 | Endocrine Glands | 315–357 | 338–380 | pending |
| 12 | Muscle | 358–402 | 381–425 | pending |
| 13 | Blood, Heart, and Circulation | 403–448 | 426–471 | pending |
| 14 | Cardiac Output, Blood Flow, and Blood Pressure | 449–491 | 472–514 | pending |
| 15 | The Immune System | 492–530 | 515–553 | pending |
| 16 | Respiratory Physiology | 531–579 | 554–602 | pending |
| 17 | Physiology of the Kidneys | 580–617 | 603–640 | pending |
| 18 | The Digestive System | 618–661 | 641–684 | done |
| 19 | Regulation of Metabolism | 662–701 | 685–724 | pending |
| 20 | Reproduction | 702–768 | 725–791 | pending |

Update the `Status` column as each chapter is generated.
