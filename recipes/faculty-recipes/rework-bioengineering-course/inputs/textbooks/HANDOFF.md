# HANDOFF — Textbook → per-chapter RAG markdown

A portable recipe for turning a large physiology/biology textbook PDF into per-chapter
markdown files suitable for an AI / retrieval-augmented-generation (RAG) application.
Written so a fresh Claude instance can pick up the same process on a **different** textbook
with no other context. It was first run on Boron & Boulpaep *Medical Physiology*, 3rd ed.

---

## 0. The intellectual-property stance (read first)

The project owner is Harvard faculty reformatting texts **with stated permission from the
source publisher / authors** for a class / AI-application. Even so, we deliberately do **not**
reproduce the book's running prose. The format is a *distillation + citation anchors*, which
is both more useful for RAG and respectful of the source:

- **Short citation-anchor quotes only.** 1–3 sentences each, each tagged with a `(p. X)`
  page anchor. 4–8 such quotes per major section. These are the retrieval chunks.
- **Equations are reproduced** in LaTeX (`$…$` inline, `$$…$$` display). Equations are facts,
  not expression — reproduce them faithfully with their book equation numbers when given.
- **Tables are reproduced** as markdown when they hold reference data (ion concentrations,
  normal values, comparisons). These are data, not prose.
- **Figures are described**, not copied — vision descriptions of the rendered page image.
- **No wholesale prose dump.** Core claims are written in our own compact words; the book's
  sentences appear only inside the short quoted anchors.

If the owner later wants longer quoted passages, that is a separate higher-budget pass.

---

## 1. Folder layout

```
inputs/textbooks/
  <Book Title>.pdf                 # the source PDF (gitignored if commercial)
  <book-slug>/                     # one folder per book
    README.md                      # index of all chapters + status + provenance + policy
    chapter-NN-slug.md             # one file per chapter, zero-padded NN
  HANDOFF.md                       # this file
```

`inputs/` is read-only by convention in this repo; the generated markdown lives alongside
the PDF because it *is* an input to the downstream RAG app. No emojis anywhere (repo rule).
Use markdown link syntax for file references.

---

## 2. Inspect the PDF

```bash
PDF="<Book Title>.pdf"
pdfinfo "$PDF"                       # page count, size, page geometry
pdffonts "$PDF" | head               # is there a real text layer or is it a scan?
```

Two PDF kinds, handled differently:

- **Born-digital (vector) PDF** — has selectable text and isolable figures. `pdfimages -list`
  shows real figure images you can extract.
- **Scanned PDF with OCR layer** (e.g. Internet Archive) — text is OCR (expect garble in
  chemistry/subscripts), and `pdfimages` returns **full-page raster fragments, not figures**.
  For this kind you must render whole pages and view them. *Medical Physiology was this kind.*

### Page offset

The PDF page number ≠ the printed book page number. Find the offset once by locating any
known printed page in the rendered PDF, then record it. For Medical Physiology:
**`pdf_page = book_page + 12`.** Every book has its own offset — recompute per book.

---

## 3. Find chapter boundaries

Render the front-matter Contents pages to text and read off each chapter's **start** page:

```bash
pdftotext -f <toc_first> -l <toc_last> -layout "$PDF" - | grep -E "^\s*[0-9]+\s+[A-Z]"
```

Each chapter's end page = (next chapter's start page − 1). The last chapter ends where the
back-matter (Index / appendices) begins. Build a master table of `book pp.` and convert to
`pdf pp.` with the offset. Put this table in the book README so it is not recomputed.

---

## 4. Per-chapter extraction pipeline

For a chapter spanning PDF pages `START`–`END`:

```bash
# (a) Layout-preserving text — keeps two-column structure, good for reading flow & quotes
pdftotext -f START -l END -layout "$PDF" /tmp/<book>_chNN.txt

# (b) Flat text — no columns, better for grep-ing section headings & equations
pdftotext -f START -l END "$PDF" /tmp/<book>_chNN_flat.txt

# (c) Render pages to PNG for figure viewing (scanned books) at ~120–150 dpi
pdftoppm -png -r 120 -f START -l END "$PDF" /tmp/chNN/p
#   -> /tmp/chNN/p-NNN.png  (poppler zero-pads to the PDF's page-count width)
```

Then:
1. Read the layout text to map the chapter's section structure and pull citation anchors.
2. To describe a figure, find which PDF page it sits on (grep the flat text for `Figure NN-x`),
   then **view** the matching PNG with the Read tool and describe it subpanel-by-subpanel.
3. Watch for OCR corruption in equations/subscripts — correct against the rendered image, do
   not propagate OCR garble (`P_a,co,`, `Cel!`, `V̇o,`, etc.).

### Figure-pass policy (fast pass — current default)

The book is large; a full per-figure vision pass is deferred. Per chapter:
- **View ~5 representative / load-bearing figures** and write full subpanel descriptions
  (mark these `*(viewed)*`).
- **List the rest** by caption and describe from surrounding text (mark `*(listed)*`).
- The chapter footer enumerates which figures are viewed vs. listed so a later pass knows
  exactly what remains. The book README documents this policy and how to run the deeper pass.

---

## 5. Per-chapter markdown skeleton

Follow this exact shape (it is what the existing chapters use; match it for consistency):

```markdown
---
chapter: NN
title: <Chapter Title>
authors:
  - <Author One>
section: "<Roman>. <Section Name>"
source_pages: "<book start>–<book end>"
pdf_pages: "<pdf start>–<pdf end>"
source_book: "<Author>. <Title>, <edition> (<year>)"
figures_listed: "<count or ≈count>"
figures_described_from_image: <count>
equations: "<short summary of the key equations>"
tables: <count>
clinical_boxes: "<count + brief>"
---

# Chapter NN — <Title>

> Section <Roman> · <Section Name> · pp. <range> · Author: <Author>

## Chapter map (top-level)
1. **<Section title>** (pp. x–y) — one-line gloss.
...

---

## Section <k> — <title> (pp. x–y)

### Subsection headings
- **<verbatim subsection heading>** (pp. x–y)
...

### Core claims
- Compact prose in our own words. Numbers, mechanisms, normal values.

### Citation-anchor quotes
- > "<short 1–3 sentence verbatim quote>" (p. X)
  (4–8 per major section)

### Equations            # when present
- $$ <LaTeX> $$  with the book's equation number and variable glosses.

### Figures
#### Figure NN-x — <caption> *(viewed)* | *(listed)*
<description — subpanel-by-subpanel if viewed>

---

## Tables            # reference-data tables reproduced as markdown
## Glossary          # flat term list for downstream chunking
## Cross-links forward   # chapters the source explicitly points to
## Source apparatus  # online-notes IDs, clinical boxes, references deferred

---

## Format-verification notes
**Figures viewed and described from image:** <list>
**Figures listed by caption + textual reference only:** <list>

*End of Chapter NN. Next: Chapter NN+1 — <title>, p. <start>.*
```

---

## 6. Workflow order & pacing

1. Build the chapter-boundary table → README index (status column: pending/done).
2. Generate chapters in **batches of ~5**. Update the README status column as each lands.
3. Parallelize with subagents (`general-purpose`) when available: give each agent a
   self-contained brief naming its chapter, page ranges, this HANDOFF, and 1–2 finished
   chapters as format exemplars. One agent = one chapter.
4. **Long chapters can exceed a subagent's idle-stream timeout.** If an agent times out or
   errors, write that chapter directly in the main thread instead. Chapters 31 and 32 were
   done this way.

---

## 7. House-style decisions (locked)

- No emojis. Markdown links for file refs.
- En-dash page ranges (`722–738`). `(p. X)` anchors on every quote.
- LaTeX for every equation, even simple ones; keep book equation numbers.
- Subscripts/superscripts: use real Unicode (PCO₂, V̇_A/Q̇) or LaTeX in math mode; never OCR garble.
- Quotes are short. Core claims carry the bulk of the content in our own words.
- Each chapter ends with a Format-verification footer and a "Next:" pointer.

## 8. Common pitfalls

- **Wrong page offset** → you render the wrong pages. Verify the offset against a known page.
- **`pdftoppm` zero-pads filenames** to the PDF page-count width (`p-0734.png`). Glob, don't
  assume `p-734.png`.
- **Treating `pdfimages` output as figures** on a scanned book — it is page fragments. Render
  whole pages instead.
- **OCR garble in chemistry/equations** — always reconcile against the rendered image.
- **The built-in Read tool refuses PDFs > ~100 MB** — use the `pdftotext`/`pdftoppm` pipeline,
  never try to Read the raw PDF.

## 9. Tools used

`pdfinfo`, `pdffonts`, `pdftotext` (`-layout` and flat), `pdftoppm` (PNG render),
optionally `pdfimages` (vector PDFs only). Poppler suite; all CLI.

---

## End-of-batch report template

> Batch <a>–<b> done. Files written: chapter-<a> … chapter-<b>. README status updated.
> Figures viewed: <n total>. Notable: <anything that needed main-thread fallback / OCR fixes>.
> Next batch: <c>–<d>.
