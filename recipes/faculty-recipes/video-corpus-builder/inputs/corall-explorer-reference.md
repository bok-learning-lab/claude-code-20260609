# Reference Site Concept: CORAAL Explorer

## Purpose of this document
This explains the conceptual model behind our reference site, the
**CORAAL Explorer** (Corpus of Regional African American Language),
hosted at https://lingtools.uoregon.edu/coraal/explorer/.

We are NOT cloning CORAAL. We are borrowing its proven UX pattern for a
searchable, timestamp-linked spoken-language corpus and adapting it for
video (local files + YouTube embeds) and for a learner-facing
"dictionary" workflow.

## What CORAAL is
CORAAL is a downloadable linguistic corpus of recorded sociolinguistic
interviews — 220+ speakers across regional components (Atlanta, DC,
Detroit, Rochester, Princeville, Lower East Side, Valdosta).

The raw data ships as PARALLEL files per component:
- audio: .wav (split into parts for download)
- transcripts: plain text files, one per interview
- time-aligned annotations: Praat .TextGrid and ELAN .eaf files
- one metadata.txt per component (speaker + recording info)

The single most important structural fact:
**Every transcript is segmented into timestamped utterances** — each row
has a line number, a speaker label, a start time, the text, and an end
time. This is conceptually identical to an SRT subtitle file. That
parallel structure (media + time-aligned transcript + speaker metadata)
is the entire foundation of the tool.

## The two tools that matter
The Explorer is made of exactly two pieces. Together they ARE the
"dictionary website + media playback" experience the faculty want.

### 1. The File Searcher = the "dictionary"
URL: explorer/search.php
- You type a word or phrase. It also supports R-style regular
  expressions (e.g. `they \w*ing\b`), and `|` matches pauses.
- You can scope the search to a component, and filter by speaker
  demographics: Gender, Age group, Socioeconomic (SES) group.
- It returns a **KWIC concordance** (Key Word In Context): a results
  table where each row is one hit, showing:
      File (clickable) | Line | Speaker (clickable) | Turn Start |
      PreMatch | **Match** | PostMatch | Turn End | Match No.
- Example: searching "finna" returned 37 hits laid out this way.

This is the core faculty ask: search a word -> see every utterance that
contains it, in context, with who said it and when.

IMPORTANT LIMITATION: CORAAL's searcher is a literal/regex string match.
It does NOT group word forms. Searching "go" will NOT find "going" or
"went". Our project adds that linguistic layer (see "Lemmas" below) —
that's the genuinely new contribution beyond this reference.

### 2. The File Browser = the "playback tool"
URL: explorer/browse.php
- Clicking a concordance hit deep-links into the transcript via a URL
  like:
      browse.php?what=ATL_se0_ag1_f_01_1.txt&line=117&settime=134.92
  Note the `line` and `settime` parameters — they jump the transcript to
  a specific line AND seek the media player to that exact second.
- The page shows: a synced audio player (with "Get Time", "Move to
  Time", and "Jump to line" controls), a speaker-metadata header
  (e.g. "Female, born 1995, Occupation: Cashier, interviewed 2017"),
  and the full transcript table: Line | Speaker | Start | Text | End.

This deep-link-to-timestamp pattern is precisely what our video tool
needs. We swap the audio player for a video player (HTML5 `<video>` for
local files; YouTube IFrame API for embeds) and seek to the utterance's
start time.

## The data model implied by the reference
Two joined tables.

UTTERANCE (one row per timestamped subtitle segment):
- utterance_id
- source_id (which video/interview)
- line number
- speaker_id
- start_time (seconds)
- end_time (seconds)
- text (raw surface text)
- [our addition] lemmas: list of headwords in this utterance

SPEAKER / SOURCE METADATA (joined on speaker_id / source_id).
CORAAL's actual metadata.txt columns (a useful menu to pick from) include:
  CORAAL.Spkr, CORAAL.File, Primary.Spkr, Gender, Age, Age.Group,
  Year.of.Birth, Year.of.Interview, CORAAL.SEC.Group (socioeconomic),
  Education, Edu.Group, Occupation, Other.Places.Lived, Interviewer.Code,
  Interviewer.Gender, plus recording specs (Sampling.Rate, etc.),
  CORAAL.Length.of.Transcript, CORAAL.Word.Count, Notes.
We will use a much smaller subset, but the principle holds: keep speaker
and scene metadata in a separate table, joined to utterances.

## Linguistics concepts (plain-language)
- **Surface form**: a word exactly as it appears ("running", "ran",
  "runs").
- **Lemma / headword**: the dictionary base form they all map to
  ("run"). Lemmatization = grouping surface forms under their lemma.
- Why it matters: a learner should search a headword and find ALL its
  real utterances. Searching "go" should surface "going", "went",
  "finna go", etc. This needs an NLP lemmatizer.
- **Levantine Arabic note**: Arabic morphology is rich (clitics,
  prefixes/suffixes, root-and-pattern). A naive English-style stemmer
  will NOT work. We need a morphology-aware analyzer (e.g. CAMeL Tools /
  MADAMIRA-style dialectal analysis) and an STT model that handles
  Levantine Arabic. Flag this as a research/tooling dependency.
- **Word-frequency analysis**: rank lemmas by occurrence count. This is
  how we identify "easy" high-frequency utterances/scenes for learners.

## What we keep, what we change
KEEP: search -> KWIC concordance -> click hit -> media seeks to the exact
utterance timestamp; speaker/scene metadata filters; transcript view with
per-line timestamps.
CHANGE/ADD: video instead of audio (local + YouTube); lemma-aware search
(not just literal); frequency-based "difficulty" view for learners.

## Source / licensing note
CORAAL is CC BY-NC-SA 4.0 and free for research use. We are using it as a
design reference only, not redistributing its data.
Citation: Kendall, Tyler and Charlie Farrington. 2023. The Corpus of
Regional African American Language. Version 2023.06. ORAAL Project.