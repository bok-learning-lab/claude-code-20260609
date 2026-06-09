# Step 4 — Build the search-and-playback site

**Goal of this step:** the static website. This is the half you can run **in
parallel** with Step 3, in a second Claude session, as long as both sides agree
on the shape of `corpus.json` first.

---

## Prompt

> Build the static website in `outputs/site/` — vanilla HTML/CSS/JS that runs by
> double-click from `file://` (no server, no build step, no `npm install`). It
> loads its data from `outputs/site/corpus-data.js` (which sets `window.CORPUS`);
> never `fetch()` a local file.
>
> Features (mirror the CORAAL Explorer):
> 1. **Search** with an EXACT / LEMMA toggle. Lemma mode (default) looks words up
>    in the lemma index so "go" finds "going"/"went"; exact mode uses the
>    surface-form index. Add filters by video and by speaker metadata.
> 2. **Results = a KWIC concordance**: one row per hit — Video | Line | Speaker |
>    Start | PreMatch | **Match** | PostMatch. **Highlight the word that actually
>    matched** (important for lemma search, so a hit on "are" under the lemma "be"
>    is obvious and doesn't look like a bug).
> 3. **Player view**, branching on `source_type`: local videos use HTML5
>    `<video>` and set `currentTime` to the utterance start; YouTube videos use
>    the IFrame API and `seekTo(start)` — handle the player-not-ready race. Show
>    the surrounding transcript with the active line highlighted; clicking a line
>    re-seeks.
> 4. **A shareable deep link** in the URL hash (video + line + time) that reopens
>    to that exact moment.
> 5. **A frequency / "easy utterances" view**: lemmas by frequency; click one to
>    see its utterances sorted easiest-first.

### If running in parallel with Step 3 — freeze the contract first

> Before either session starts coding, write down the exact shape of
> `corpus.json` (videos, speakers, utterances with `start`/`end`/`tokens`/
> `lemmas`/`difficulty`, plus the indexes) and give the site session a tiny
> **stub** `corpus-data.js` matching that shape to develop against. The pipeline
> session stays in `operations/` + `outputs/`; the site session stays in
> `outputs/site/`. When both finish, drop the real data in — no code changes.

---

## Why this works

- **Static + `file://`** means a faculty member can open the result by
  double-clicking, with nothing to install — the same reason the data ships as a
  `.js` wrapper instead of a fetched `.json`.
- **One frozen contract** is what lets two agents (or two people) work at once
  without colliding. The stub removes the blocking dependency on the pipeline.
- **Highlighting the matched word** preempts the single most common "is this
  broken?" question with lemma search.

## What you should have after this step

- `outputs/site/` with `index.html`, `app.js`, `styles.css`, reading
  `corpus-data.js`; search, concordance, player, deep links, and the frequency
  view all working against the (stub, then real) data.
