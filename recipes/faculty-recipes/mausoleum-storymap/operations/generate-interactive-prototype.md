# Prompt Template — Build the Monsoon Asia Interactive Prototype (Faculty Exemplar)

**For faculty:** A prompt to generate a polished interactive prototype demonstrating what a high-quality HAA 81 student final project could look like. Use the Lotus Group sample dataset to create a reference exemplar students can study and aspire to. Fill in the `{{placeholders}}` and paste it to Claude (Chat, Cowork, or Code). It is safe to run again whenever the data changes.

---

Build a **polished, interactive HTML5 prototype** that demonstrates what a high-quality HAA 81 student final project could look like. Using the "Lotus Group" sample dataset, create a reference exemplar that students can view and learn from. The prototype combines **geospatial mapping, temporal visualization, and curatorial annotation** to demonstrate networked (non-diffusionist) historical thinking and rigorous digital scholarship.

## Data

**Input:** Four CSV files in `{{CSV_FOLDER}}`:
- `{{OBJECTS_CSV}}` — individual artifacts (lamps, coins, reliefs, tiles, bronzes)
- `{{SITES_CSV}}` — architectural monuments (temples, monastic complexes)
- `{{ROUTES_CSV}}` — maritime/overland journeys with waypoints
- `{{ITINERANT_CSV}}` — portable objects moving between locations

**Key columns in each CSV:**
- `Name/Title`, `Location Geo coordinates` (lat, lon), `Date` / `Year` / `Month` / `Day`
- `Media` (public URL), `Media Credit`, `Media Caption`
- `Analytical Description` (museum context)
- `Associated Object(s)` / `Associated story/iconography` (cross-references)
- `Tags`, `Group` (student group name)

**Course context:** `{{CONTEXT_DOC}}` — summarizes course pedagogy, learning objectives, and why networked thinking matters.

## Title & Group

**Project Title:** `{{PROJECT_TITLE}}`  
**Student Group Name:** `{{GROUP_NAME}}`  
**Group Thesis (1–2 sentences):** `{{GROUP_THESIS}}`  
Example: *"The lotus motif functioned as a portable visual currency in Buddhist maritime trade networks, enabling monks and merchants to recognize and transmit shared religious concepts across South and Southeast Asia."*

**Research Phases (3–5 chronological sections):**
```
Phase 1: {{PERIOD}} — {{PHASE_NAME}}
Narrative: {{STUDENT_NARRATIVE}}

Phase 2: {{PERIOD}} — {{PHASE_NAME}}
...
```

## Requirements

**Architecture:**
1. **Single self-contained HTML file** — no build step, no backend, no external dependencies beyond CDN-hosted libraries. Must open and render correctly from disk (`file://`).
2. **Inline all CSV data as JavaScript objects** — do NOT fetch CSVs over the network. Parse and embed as a `const DATA = { objects: [...], sites: [...], routes: [...], itinerantObjects: [...], groupProfile: {...} }` at the top of `<script>`.
3. **Lightweight libraries only** (CDN-hosted):
   - **Leaflet.js** for mapping (~39 KB)
   - **Vanilla CSS** (Tailwind via CDN optional) for responsive layout and dark mode
   - NO React, NO Webpack, NO TypeScript compilation

**Visual Design (2024–2026 Academic Digital Humanities Aesthetic):**
1. **Minimalist, utility-first layout** — clean typography, generous whitespace, neutral palette (white/gray/black) with one accent color (e.g., muted gold/blue evocative of Monsoon Asia). WCAG AA contrast (7:1 text, 4.5:1 UI).
2. **Progressive disclosure** — secondary controls (filters, annotations, connections) hidden until toggled. Reduces cognitive load.
3. **Card + grid system** — modular layout with consistent spacing; responsive to viewport (CSS Grid, mobile-first).
4. **No carousels, no decorative animations** — all interaction clarifies state or guides navigation.

**Interactive Features:**
1. **Interactive Map** (Leaflet):
   - Center on Monsoon Asia; one pin per object/site, color-coded by type (object=blue, site=orange).
   - Click marker → open object/site card panel. Hover → tooltip (name + date).
   - "Show Connections" button (off by default) → draws lines between related items with student explanation labels.
   - Filter by tag/theme → show/hide markers, dim non-matching to 20% opacity.

2. **Object/Site Card Panel**:
   - Image (left, ~300px) + metadata (right): title, museum, accession, date, location, material.
   - "Analytical Description" (expandable).
   - **Student Annotations Toggle** (show/hide): close-looking notes, significance, connections to other objects with brief explanation.
   - "Compare" button → opens side-by-side comparative viewer.

3. **Timeline Visualization**:
   - Vertical or horizontal spanning 5th–16th century.
   - Student-created research phases as sections (Phase 1: 5th–7th c. "Buddhist Learning Centers" with narrative + objects in that phase).
   - Click a phase → filters map/cards to that period. Hover object on timeline → highlights on map and in card panel.
   - "Show Student Narrative" toggle → reveals phase narratives and thematic explanations.

4. **Connection Visualization**:
   - On map: lines/bezier curves between related objects/sites; label shows student explanation ("Both attest to Pala-period luxury production and monastic patronage").
   - In card: "Connections" section lists related objects with explanation snippets.
   - Hover/click connection → highlights both objects, shows full explanation, optionally opens comparative viewer.

5. **Comparative Viewer**:
   - Two object cards side-by-side (desktop) or stacked (mobile).
   - Shows full metadata + images for both. Student analytical statement between them (e.g., *"Both 9th–10th century; both from ports; both Buddhist. What connects them geographically?"*).
   - "Swap" button to replace one object. "Add note" placeholder for student comparative analysis.

6. **Search + Faceted Filter**:
   - Search bar (full-text across names, descriptions, tags).
   - Filter facets (collapsible):
     - Date range (5th–7th c., 7th–9th c., etc.)
     - Type (Objects, Sites, Routes)
     - Thematic tags (student-curated: "Lotus as Purity," "Coastal Ports & Exchange," "Monastic Transmission")
     - Material (bronze, stone, terracotta, etc.)
   - Results grid: cards of matching items + count.

7. **Student Group Profile Section**:
   - Accessible from main nav (sidebar or top section).
   - Displays group thesis, research phases narrative, curatorial themes with associated objects.
   - Click theme → filters map/cards to that theme.

8. **Dark Mode Toggle**:
   - Moon/sun icon in top-right. Toggle saves to localStorage. Both modes WCAG AA compliant.

**Pedagogical Exemplar (This is what excellence looks like for students):**
1. **Student intellectual work must be prominently visible:**
   - Annotations reveal close-looking analysis (material, iconography, technique, provenance).
   - Connection explanations show causal reasoning (WHY linked, not just THAT linked) — evidence of networked, non-diffusionist thinking.
   - Curatorial themes demonstrate editorial judgment and thematic synthesis.
   - Research phase narratives show argument evolution over time.
   - This prototype serves as a reference standard: *"This is the level of analytical depth and visual communication we expect."*

2. **Exemplary student annotations (embed these to model scholarship):**
   - Object: *"This lamp's lotus-form stem echoes Amaravati prototypes but is cast more finely, suggesting high-status patron. The lotus-capital appears at sites 3,000 km apart (Nalanda, Borobudur, Paharpur), suggesting either itinerant craftspeople or shared workshop traditions."*
   - Connection: *"Both attest to Pala-period luxury object production and monastic patronage (5th–12th c.). The similarity in execution suggests knowledge transfer through itinerant monks trained at Nalanda."*
   - Phase narrative: *"Pala-period monks and craftspeople carry lotus-decorated objects (coins, tiles, bronzes) along Bay of Bengal trade routes. Objects appear simultaneously at geographically distant sites, suggesting systematic transmission via merchant and monastic networks—not random diffusion."*

**Accessibility & Performance:**
- Semantic HTML5 (`<main>`, `<nav>`, `<article>`, `<section>`).
- WCAG AA contrast + keyboard navigation (Tab, Enter, Escape; all interactive elements keyboard-accessible).
- Alt text on all images.
- Mobile-responsive (test 320px, 768px, 1024px viewports).
- Fast page load: no external image fetches (only URLs in data); CSS + JS optimized.

---

## Deliverables

1. **`index.html`** — single file with embedded data, all CSS + JS. Open directly from disk; render in any modern browser (Chrome, Firefox, Safari, Edge).
2. **`README.md`** — instructions for deploying to GitHub Pages, editing data/annotations, customizing colors/text, extending with new objects.

**Success Criteria:**
- ✅ Map shows all objects/sites at correct coordinates with correct color coding.
- ✅ Timeline spans 5th–16th century; student research phases and objects appear in correct chronological order.
- ✅ Clicking a map marker opens a card with all metadata + image visible.
- ✅ Toggling "Student Annotations" reveals close-looking notes, significance, and connection explanations (not empty placeholders).
- ✅ "Show Connections" draws visible lines between related objects; hovering/clicking a line shows the student explanation.
- ✅ Search + filters work; results update live and count is accurate.
- ✅ Comparative viewer loads two objects side-by-side with student analytical statement visible.
- ✅ Student Group Profile section prominently displays thesis statement and research phase narratives.
- ✅ Dark mode toggle works; both modes meet WCAG AA contrast.
- ✅ Page is fully keyboard navigable and renders on mobile (320px viewport).

When done, confirm:
1. File path(s) of deliverables (ready to share with students and deploy to course site).
2. That student intellectual work (annotations, connections, thesis) is clearly visible — this is the exemplar students will learn from.
3. That the design feels contemporary and polished (minimalist, progressive disclosure, no carousels or skeuomorphism) — something students aspire to create.
4. That a student or faculty member with no technical background could open the HTML, see the data, understand the Lotus Group's argument about Monsoon Asia cultural transmission, and think *"I could do something like this with my own research."*

---

**Faculty Notes:**
- This prototype demonstrates that students can do rigorous, scholarly work *using* AI for technical scaffolding without AI replacing the intellectual labor.
- Share this with students early in the project timeline as a reference exemplar and assignment standard.
- The annotations embedded in this prototype model the depth of analysis you expect; students should write similarly substantive close-looking notes and connection explanations for their own objects.
- The code is intentionally readable and modular so students could adapt this structure for their own data if interested in the technical side.

---

*Template created for HAA 81: Art of Monsoon Asia (Harvard University, Summer of Claude workshop, June 2026).*
