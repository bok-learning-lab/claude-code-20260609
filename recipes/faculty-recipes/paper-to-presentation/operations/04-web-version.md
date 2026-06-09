# Prompt template — Build an interactive web version of the presentation

**Purpose:** transform the slide deck into a **web-native experience** that lives
beyond the presentation moment. The web version offers multiple viewing modes
(presentation, study, speaker notes), smooth animations, responsive design, and
the option to embed interactive elements. It's a alternative to slides, not a
replacement for them — use whichever fits the moment.

**Prerequisites:** 
- An **approved, built slide deck** (from `03-build-deck.md`)
- An **approved visual asset manifest** (from `02-visual-assets.md`)
- The **speaker notes** from your deck (essential for the "study" mode)

**How to use:** fill in the `{{placeholders}}` and send.

---

You are building a **web version of a physics presentation** that preserves the
scientific argument while leveraging the web's strengths: smooth animation,
interactivity, responsive typography, and mode-switching.

The web version should serve three audiences:
- **Live presenter:** sees notes, speaker cues, and can advance at their own pace
- **Audience member during the talk:** sees visuals and minimal text; slides
  advance with the speaker
- **Later viewer (study mode):** sees visuals + explanatory text; can linger on
  difficult concepts; can pause and explore

**Approved deck:** {{DECK — attach the .pptx or slide outline; the stand-in is
`../outputs/sample-deck.pptx`}}

**Visual assets:** {{ASSETS — list or attach the visual asset files (SVGs,
images, descriptions); reference the manifest from `02-visual-assets.md`}}

**Talk length:** {{TALK_LENGTH — e.g. "10 minutes"}}

**Technical preferences:** {{e.g. "vanilla HTML/CSS/JS" / "React" / "just give
me a single-page HTML file" / "I can host this on my web server"}}

**Visual register:** {{STYLE — e.g. "minimal, academic; lots of white space;
dark mode option" / "modern, polished; animated transitions" / "clean and
simple, no fuss"}}

---

## What the web version includes

### 1. **Presentation mode**
- Full-screen slide view, one slide at a time
- Minimal text on screen (key idea only; speaker notes hidden from audience)
- Visuals full-width; readable on a projector at 20 feet or on a laptop screen
- Navigation: arrow keys, click/tap to advance, or keyboard shortcuts
- **Optional:** timer showing elapsed time (speaker can toggle it on/off)
- Smooth fade or slide transitions between slides

### 2. **Study mode**
- Slides + speaker notes visible side-by-side (on desktop) or stacked
  (mobile)
- Reader can pause on any slide; expand speaker notes; linger on visuals
- Explanatory text is **rich and complete** (not a summary)
- Links to references, related papers, or background resources (optional)
- Each visual has a detailed caption and context
- Outline visible as a sidebar (optional navigation by section)

### 3. **Speaker notes view** (presenter-only, if needed)
- Notes prominently displayed
- Current slide + preview of next slide
- Simple speaker timer (elapsed time since start)
- Accessible via a keyboard shortcut or a toggle
- Can be viewed on a separate device (notes on laptop, presentation on screen)

### 4. **Responsive design**
- Works on desktop (full experience), tablet (study mode works well), and
  mobile (content legible; may switch to single-column layout)
- Typography scales gracefully; no text so small it's unreadable on a phone
- Touch-friendly navigation (large tap targets)

### 5. **Visual styling**
- **Dark mode + light mode toggle** (physics talks often happen in dark rooms;
  study mode readers may prefer light)
- Consistent typography (sans serif, generous line-height)
- Color palette that supports both modes
- No moving elements except intentional animations (avoid seizure-inducing
  effects)
- Plenty of white/dark space; avoid clutter

### 6. **Animations & interactivity (optional)**
- Fade-in for visuals as you advance (feels polished, not jarring)
- Animated visuals from the asset manifest can play on slide load (or on
  click if complex)
- Optional: clickable elements to expand more detail on a diagram
  (e.g., hover over a label to highlight a feature)
- Smooth scrolling in study mode

---

## Build steps

1. **Structure the content:**
   - Export slides to a JSON or YAML file (one entry per slide with: title, key
     idea, speaker notes, visual asset reference)
   - Organize sections / acts (motivation, methods, results, conclusion)

2. **Build the HTML skeleton:**
   - Single-page app (SPA) structure: container for slides, mode toggles, navigation
   - Semantic HTML: `<article>` per slide, `<figure>` for visuals, `<aside>` for
     notes

3. **Style with CSS:**
   - Base styles for both dark and light modes (CSS variables make this easy:
     `--bg-color`, `--text-color`, etc.)
   - Slide layout: visual full-width, key idea below, notes in a secondary area
   - Responsive breakpoints: desktop (side-by-side), tablet (stacked), mobile
     (single column)
   - Smooth transitions (e.g., `transition: opacity 0.3s ease`)

4. **Add interactivity with JavaScript:**
   - Mode switching (presentation ↔ study ↔ speaker notes)
   - Slide navigation (arrows, keyboard shortcuts, next/prev buttons)
   - Timer (starts on first slide, user can toggle pause/reset)
   - Dark mode toggle (store preference in localStorage)
   - Full-screen toggle for presentation mode

5. **Embed visuals:**
   - SVG files inline (allows CSS manipulation and interaction)
   - Raster images as `<img>` with alt-text (accessibility)
   - Animated SVGs or videos play on slide load or on user click
   - Captions and figure labels visible in study mode

6. **Polish:**
   - Test navigation on keyboard and touch
   - Check readability on a projector (borrow one, or simulate with a 1920×1080
     screenshot)
   - Proofread speaker notes and captions
   - Ensure alt-text is present for all visuals (accessibility)

---

## Output format

- A **single `.html` file** (self-contained, no server needed) *or* a **folder
  structure** (if assets are large: `index.html`, `/css`, `/js`, `/assets`)
- **Keyboard shortcuts cheat sheet** (printed or shown on load)
- **Browser compatibility notes** (modern browsers: Chrome, Firefox, Safari, Edge)
- **Optional:** a README with setup instructions and a quick demo walkthrough

---

## Example: minimal structure for a 10-minute talk

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Half-Full Landau Level</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div id="app">
    <!-- Mode toggles -->
    <nav class="controls">
      <button id="mode-presentation">Presentation</button>
      <button id="mode-study">Study</button>
      <button id="mode-speaker">Speaker Notes</button>
      <button id="dark-mode-toggle">🌙</button>
    </nav>

    <!-- Slide container -->
    <main id="slide-container" class="presentation-mode">
      <article class="slide" data-slide="1">
        <h1>The Half-Full Landau Level</h1>
        <p class="subtitle">Bertrand I. Halperin, Harvard University</p>
        <aside class="speaker-notes" hidden>
          [Speaker notes for slide 1...]
        </aside>
      </article>
      
      <article class="slide" data-slide="2">
        <h2>Why fractional quantum Hall states?</h2>
        <figure>
          <img src="landau-filling.svg" alt="Landau level filling at ν = 1/2">
          <figcaption>Why this state is special.</figcaption>
        </figure>
        <aside class="speaker-notes" hidden>
          [Speaker notes for slide 2...]
        </aside>
      </article>
      
      <!-- More slides... -->
    </main>

    <!-- Navigation -->
    <footer class="nav">
      <button id="prev">← Previous</button>
      <span id="slide-counter">1 / 13</span>
      <button id="next">Next →</button>
    </footer>
  </div>

  <script src="app.js"></script>
</body>
</html>
```

---

## Keyboard shortcuts (default)

| Key          | Action                  |
|--------------|-------------------------|
| `→` / `Space` | Next slide              |
| `←`          | Previous slide          |
| `m`          | Toggle mode             |
| `d`          | Toggle dark mode        |
| `f`          | Full-screen (presentation mode) |
| `n`          | Toggle speaker notes    |
| `t`          | Toggle timer            |
| `Esc`        | Exit full-screen        |

---

## Accessibility checklist

- [ ] All visuals have alt-text
- [ ] Text contrast ratio ≥ 4.5:1 (WCAG AA standard)
- [ ] Keyboard navigation fully functional (no mouse required)
- [ ] Color not the only visual cue (use shapes, text, or patterns too)
- [ ] No automatic animations lasting >5 seconds (user can pause)
- [ ] Respects `prefers-reduced-motion` system setting

---

## Deployment (optional)

If you want to share the web version:
- **GitHub Pages:** Upload the folder as a repo, enable Pages, share the link
- **Self-hosted:** drop the files on your server (no build step required if it's
  a single HTML file)
- **QR code:** generate a QR code pointing to the URL; students/colleagues can
  access it on their phones during/after the talk

---

## Next steps

Once the web version is built and tested:
- Use it **during the talk** (presentation mode on the projector, speaker notes
  on your laptop)
- Share the link **after the talk** (study mode for students who want to
  understand deeper)
- Iterate: if viewers struggle with a concept, edit the speaker notes or add
  more visuals
