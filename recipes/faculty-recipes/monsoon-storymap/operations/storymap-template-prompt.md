# Build a story-map site template for HAA91 Art of Monsoon Asia

## Project context

HAA91 *Art of Monsoon Asia* is a Harvard art-history course about the art, architecture, and material culture of regions shaped by the South Asian and East Asian monsoon systems. Students compile primary-source materials in a shared Google Sheet across the semester, then collaborate in teams on a final **story-map project** that places sites and objects in space and time.

The faculty member is undecided between **Scalar** (Alliance for Networked Visual Culture's platform) and **ArcGIS StoryMaps** as the host. The deliverable here is **platform-neutral**: a static HTML/JS template that can be lifted into either platform later, or stand alone as a GitHub-Pages site.

### The shared Google Sheet

Students fill in rows organized into **five categories** (the Scalar site's five hub pages):

1. Monuments and sites
2. Movable objects (paintings, sculpture, textiles)
3. Routes and networks (trade, pilgrimage, monsoon winds)
4. People and patrons
5. Texts and inscriptions

Each row has at minimum: `title`, `category`, `lat`, `lon`, `date_start`, `date_end`, `short_description`, `image_url`, `student_team`.

## What I want you to do

Generate a **single self-contained HTML file** (Leaflet for the map, plain CSS, no build step) that:

1. Reads a `data.json` array sitting next to it (one object per Sheet row).
2. Renders a **left sidebar** with the five categories as filter chips.
3. Renders a **map** that drops a marker per row, colored by category.
4. Renders a **timeline ribbon** at the bottom — a horizontal scrubber that hides markers outside the selected date window.
5. On marker click, opens a **side panel** with the row's title, description, image, dates, and team credit.
6. Has a **header strip** with the course title and a "How to read this map" link.

## Constraints

- Single HTML file, no build step. Inline CSS and JS.
- Leaflet via CDN (`unpkg.com/leaflet`).
- Works offline once cached — no other external dependencies except OSM tiles.
- Mobile-responsive — sidebar collapses to a top drawer below 700 px.
- No emoji. Color palette: ink `#141414`, accent `#c8102e`, background `#fafaf7`. Category chips get distinct hues from a 5-color palette you choose (make them legible on the map).
- Comment the JS sparingly — only where the data contract or the timeline math is non-obvious.

Also produce a **sample `data.json`** with 5–8 made-up entries spanning the five categories, scattered across South and East Asia, dated between 800 CE and 1900 CE. Use these for illustration only — they will be replaced by the real student-compiled data.
