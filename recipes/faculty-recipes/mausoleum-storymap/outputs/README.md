# The Lotus Group: Interactive Monsoon Asia Digital Humanities Project

A self-contained interactive prototype demonstrating what a high-quality HAA 81 student final project could look like. Built with vanilla HTML/CSS/JavaScript, no build steps required.

## Quick Start

1. **Open the file**: Simply open `index.html` in any modern web browser. It works locally (no server needed).

2. **Explore the prototype**:
   - **Map** (left): Interactive map of Monsoon Asia with objects and sites pinned by location
   - **Timeline** (left): Chronological view of research phases with student narratives
   - **Objects Grid** (right): Browse the Lotus Group's collected artifacts and monuments
   - **Dark Mode** (top-right): Toggle dark/light themes

3. **Click objects** to read:
   - Museum metadata
   - Scholarly descriptions
   - **Student annotations**: close-looking notes, significance statements, and connections to related objects

## What's Inside

- **8 objects** (artifacts: bronze lamps, coins, reliefs, tiles)
- **6 sites** (architectural monuments: Borobudur, Nalanda, Angkor)
- **1 route** (Bay of Bengal maritime trade path)
- **Student group profile** with thesis statement and 3 research phases
- **Curated thematic groupings** showing how students organized their findings
- **Embedded student annotations** at multiple levels (group, individual objects)

## Features

✅ **Interactive Map** — Click markers to open object details; see geographic distribution  
✅ **Timeline** — Research phases with student narrative explaining argument  
✅ **Search & Filter** — Find objects by keyword, type, time period  
✅ **Student Annotations** — Close-looking analysis and connection explanations (the intellectual work)  
✅ **Dark Mode** — WCAG AA accessible light/dark parity  
✅ **Mobile Responsive** — Works on phones, tablets, desktop  
✅ **No Dependencies** — Single HTML file + CDN-hosted libraries (Leaflet.js, OpenStreetMap)  
✅ **GitHub Pages Ready** — Deploy instantly to GitHub Pages, no build step

## For Faculty: How to Share & Use This

### Share with Students
1. **Upload to your course site** or GitHub
2. **Tell students**: *"This is what excellence looks like. Notice how the student group's intellectual work is visible — their thesis, their curatorial themes, their close-looking notes on each object."*
3. **Point out specific examples**:
   - **Thesis statement** (top-left sidebar): A clear, evidence-based argument about cultural transmission
   - **Research phases** (left sidebar): Narrative showing how the group's thinking evolved across time
   - **Student annotations** (in object modals): Sample close-looking notes and connection explanations
   - **Curated themes** (implied in groupings): Shows editorial judgment and thematic thinking

### Use as a Reference
- This prototype models:
  - How to organize research spatially (map) and temporally (timeline)
  - How to make student intellectual work visible (annotations, not hidden)
  - How to design for clarity and accessibility (minimalist, progressive disclosure)
  - A realistic scope for undergrad groups (8 objects, 3 research phases)

### Customize for Your Own Group Data
See "For Developers" below.

---

## For Students: How to Build Your Own

### Process
1. **Research phase**: Find 6-12 objects/sites using digital museum collections (Met, V&A, Freer, British Museum, etc.)
2. **Gather metadata**: For each object, collect:
   - Image (public URL from museum collection)
   - Accession number, date, material, size, location
   - Museum/scholarly description (from museum website or academic sources)
3. **Write student annotations**:
   - **Close-looking notes**: Describe materials, technique, iconography in 2-3 sentences
   - **Significance**: What does this object reveal about your research theme? (2-3 sentences)
   - **Connections**: Which other objects does this link to, and why? (1 sentence per connection)
4. **Create your group profile**:
   - **Thesis statement**: 1-2 sentences stating your big claim (e.g., "X functioned as Y in Z networks")
   - **Research phases**: 3 chronological phases showing how your argument develops over time
   - **Curated themes**: 2-3 thematic groupings showing your editorial choices (e.g., "Objects as Status Markers," "Trade Network Evidence")
5. **Use this prototype as a template**: Modify the data, keep the design, and deploy to GitHub Pages

### Sample Data Structure
The `index.html` file includes a `DATA` object at the top of the `<script>` tag:
```javascript
const DATA = {
  objects: [
    {
      id: "object-001",
      name: "Lotus-capital bronze lamp",
      museum: "National Museum, New Delhi",
      date: "8th–9th century CE",
      location: { name: "Nalanda, Bihar, India", coords: [25.1368, 85.4430] },
      media: "https://...",
      description: "...",
      tags: ["lotus", "bronze", "Nalanda"],
      annotations: {
        closeLooking: "...",
        significance: "...",
        connections: [{ linkedId: "site-001", explanation: "..." }]
      }
    }
    // ... more objects
  ],
  sites: [ ... ],
  groupProfile: { ... }
};
```

**To customize**:
1. Edit the `DATA` object to add your own objects, sites, and annotations
2. Add image URLs (must be publicly accessible)
3. Modify the thesis statement and research phases in `groupProfile`
4. Save and refresh the page — your changes appear instantly (no rebuild needed!)

---

## For Developers: Customization Guide

### Colors
Edit the CSS variables at the top of the `<style>` section:
```css
:root {
    --color-accent: #b8860b;  /* Gold — change to your theme color */
    --color-object: #3b82f6;  /* Blue for objects */
    --color-site: #f97316;    /* Orange for sites */
    --color-route: #22c55e;   /* Green for routes */
}
```

### Adding/Editing Objects
Locate the `const DATA = { objects: [ ... ] }` section and add new objects:
```javascript
{
    id: "object-009",
    name: "Your Object Name",
    museum: "Museum Name, City",
    accession: "Museum-123",
    date: "12th century CE",
    year: 1100,
    endYear: 1200,
    location: { name: "City, Country", coords: [latitude, longitude] },
    material: "Material type",
    size: "H. X cm, W. Y cm",
    description: "Scholarly description (150-250 words)",
    media: "https://public-url-to-image.jpg",
    mediaCredit: "Museum / Attribution",
    tags: ["tag1", "tag2", "tag3"],
    group: "Your Group Name",
    type: "object",
    annotations: {
        closeLooking: "Your close-looking analysis...",
        significance: "What does this reveal...",
        connections: [
            { linkedId: "object-002", linkedName: "Related Object", explanation: "Why they connect..." }
        ]
    }
}
```

### Adding Sites
Follow the same structure but use `type: "site"` and include location + description.

### Modifying Research Phases
Edit `DATA.groupProfile.researchPhases`:
```javascript
researchPhases: [
    {
        period: "5th–7th century CE",
        name: "Your Phase Name",
        narrative: "Your narrative explaining what happened in this phase..."
    }
    // ... more phases
]
```

### Modifying Curated Themes
Edit `DATA.groupProfile.curatedThemes`:
```javascript
curatedThemes: [
    {
        name: "Your Theme Name",
        description: "What this theme groups together...",
        objectIds: ["object-001", "object-003"],
        siteIds: ["site-002"]
    }
    // ... more themes
]
```

### Adding Image URLs
Images **must be from public sources**:
- **Museum collections**: Metropolitan Museum, V&A, British Museum, Freer, Smithsonian, etc. (often have "open access" sections)
- **Wikimedia Commons**: https://commons.wikimedia.org (public domain and licensed images)
- **Institutional repositories**: University museums, research centers
- **Your own website**: If you upload and host images

Avoid copyrighted images without permission.

### Mobile Testing
Open DevTools (F12) → Toggle device toolbar → Test on 320px, 768px, 1024px widths.

### Accessibility Checklist
- ✅ WCAG AA contrast (7:1 text, 4.5:1 UI) — already built in
- ✅ Keyboard navigation (Tab, Enter, Escape) — all buttons and interactive elements
- ✅ Dark mode parity — toggle dark mode and verify all text is readable
- ✅ Alt text on images — add via `alt` attribute if modifying
- ✅ Semantic HTML — use `<main>`, `<nav>`, `<article>`, `<section>`

---

## Deploying to GitHub Pages

1. **Create a GitHub repository** (or use existing)
2. **Add files**: Place `index.html` in the root (or `/docs` folder)
3. **Push to GitHub**:
   ```bash
   git add index.html
   git commit -m "Add Monsoon Asia project prototype"
   git push origin main
   ```
4. **Enable GitHub Pages**: Go to repo Settings → Pages → Select `main` branch (or `/docs` folder) as source
5. **Your project is live** at: `https://yourusername.github.io/repo-name/`

---

## Technical Stack

- **Leaflet.js** (39 KB) — lightweight mapping library
- **OpenStreetMap** — free, open tile layer
- **Vanilla JavaScript** — no frameworks, no build step
- **CSS Grid & Flexbox** — responsive layout
- **CSS Custom Properties** — easy color customization
- **localStorage** — persists dark mode preference

**All in a single 60 KB HTML file** that opens directly from disk (`file://`) with no server.

---

## Accessibility & Browser Support

✅ **WCAG 2.1 AA** compliant  
✅ **Keyboard accessible** (Tab, Enter, Escape)  
✅ **Dark mode** for reduced eye strain  
✅ **Mobile responsive** (tested 320px–1920px)  
✅ **Works in**:
- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

---

## Common Questions

**Q: Can I add more objects after deployment?**  
A: Yes! Edit the `DATA` object in the HTML file and save. Changes appear immediately (no rebuild needed).

**Q: Can I change the map center or zoom?**  
A: Yes! Find `map = L.map('map').setView([10, 85], 4)` and change the coordinates and zoom level.

**Q: Can I use this for a different research theme?**  
A: Absolutely! Modify the thesis, research phases, and curated themes. The map, timeline, and search all adapt to your data automatically.

**Q: What if I want to add a Comparison view?**  
A: The HTML includes CSS for `.comparative-view` — you can extend the modal to add a "Compare with another object" button and side-by-side viewer.

**Q: Can I embed this in a course site?**  
A: Yes! Use an `<iframe>` pointing to your GitHub Pages URL, or embed directly if your course platform allows HTML uploads.

---

## Attribution & License

This prototype was created as part of the **Summer of Claude faculty workshop** (Harvard University, June 2026) for **HAA 81: Art of Monsoon Asia**.

**Sample data**: Objects and sites are real; descriptions adapted from museum collection records and academic publications (fully cited in the prototype).

**Design inspiration**: Contemporary digital humanities practices (Wikidata, V&A Collections, Are.na, Programming Historian).

**Built with**: Leaflet.js, OpenStreetMap, vanilla JavaScript.

---

## Questions or Issues?

- Test locally first: just open `index.html` in a browser
- Check browser console (F12 → Console) for any errors
- Verify image URLs are publicly accessible
- For dark mode issues, clear localStorage: `localStorage.clear()` in console

---

*Happy exploring! Share with students and let them see what rigorous, AI-assisted digital scholarship looks like.* 🎓
