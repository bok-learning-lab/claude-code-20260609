## Project context

A worked example of Claude as a **close reader at scale.** The corpus is 538 Bob Dylan songs; the task: name every writer mentioned in any lyric — poets, novelists, playwrights, philosophers — quoting the line each name appears in. The point isn't the Dylan corpus specifically; it's the move: **close reading, at corpus scale, by an LLM told to read like a close reader and refuse to grep.**

**Hard rules.** One pass per song, fully read — no grep, no regex. Verbatim quote on every entry (the receipt). List every writer when a line names two or more (the "Verlaine's and Rimbaud's" rule). Strict exclusions: actors, athletes, politicians (unless cited as authors), saints, fictional characters, place names, and common words that coincide with surnames (e.g. "frost," "pound," "swift"). No invented matches — the verbatim quote enforces this. Empty list `[]` when a song names no writer. Stable JSON shape across every batch: `{"song", "index", "writers": [{"name", "quote"}]}`.

**Pipeline.** Run in batches (e.g. 50 songs each) → `outputs/batch_NN.json`. Concatenate into `outputs/_aggregated.json`. Then a second pass: prose writeup at `outputs/writers-in-dylan.md`, ordered by release year, with the surrounding verse and a stab at *why* each writer is being named.

---

## Prompt

Carefully READ (do not grep or use regex) these Bob Dylan lyrics to find every
writer named in them.

Load the JSON file at <path/to/bob_dylan_lyrics_unique.json>. It's a list of
objects, each with the keys: name, first_album, first_album_year, text.
Process ONLY the songs at list indices {START} through {END} inclusive.

Read each song's full lyric like a close reader. Identify every writer named
anywhere in it — poets, novelists, playwrights, songwriters, lyricists,
essayists, philosophers who wrote books, journalists, and so on.

Rules:
- When a single line names TWO OR MORE people (e.g. "Nietzsche and Wilhelm Reich"
  or "Verlaine's and Rimbaud's"), list EACH writer separately — never drop the
  second name.
- Catch obscure or lesser-known writers too, not just the famous ones.
- Exclude anyone who isn't a writer: actors, athletes, politicians (unless cited
  as authors), saints, fictional or generic characters, place names, and common
  words that merely coincide with a surname (e.g. "frost," "pound," "swift").
- Do NOT invent matches. Only include names that actually appear in the text.

Write your findings as JSON to <outputs/batch_NN.json> in this shape:

[
  {
    "song": "<song name>",
    "index": <int>,
    "writers": [
      { "name": "<full writer name>", "quote": "<the exact line it appears in>" }
    ]
  }
]

Include only songs that name at least one writer; write an empty list [] if none.
Then reply with a one-line summary listing the writers you found.