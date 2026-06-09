"""SRT parsing — the single ingest path for the corpus pipeline.

Everything upstream (a human-authored .srt, captions from yt-dlp, or output
from an STT engine) is normalized to a .srt so this module is the ONE place
timestamps enter the system. Those timestamps are sacred: they are how the
website seeks the video to the exact moment of an utterance. We parse them
once, here, into float seconds, and never lose them.

Two extras beyond vanilla SRT, both optional and both safe on normal files:

  * Speaker prefixes. A cue whose text begins with "NAME:" (e.g. "A: Just
    do it!") is split into a speaker label + the remaining text. This lets a
    plain .srt carry the speaker data CORAAL keeps in a separate metadata
    file. Turn it off with parse_speakers=False.

  * Rolling-caption de-duplication. YouTube auto-captions arrive as
    overlapping, duplicated lines with tiny 10ms "transition" cues (run
    yt-dlp on almost anything to see it). dedupe_rolling() collapses that
    mess back into clean, non-overlapping utterances.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class Cue:
    """One timestamped subtitle segment — a future 'utterance'."""

    index: int
    start: float           # seconds (from the SRT — never round-trip-lose this)
    end: float             # seconds
    text: str              # surface text, speaker prefix already stripped
    speaker: str | None = None
    raw: str = field(default="", repr=False)  # original text, for debugging


_TIME_RE = re.compile(
    r"(\d+):(\d{2}):(\d{2})[,.](\d{1,3})\s*-->\s*(\d+):(\d{2}):(\d{2})[,.](\d{1,3})"
)
# "A: text"  /  ">> NARRATOR: text"  — a short leading label, then a colon.
_SPEAKER_RE = re.compile(r"^\s*(?:>>\s*)?([A-Za-z][\w .'\-]{0,30}?):\s+(.*)$", re.DOTALL)


def timestamp_to_seconds(h: str, m: str, s: str, ms: str) -> float:
    """HH:MM:SS,mmm -> float seconds. The conversion the whole tool rests on."""
    ms = (ms + "000")[:3]  # normalize 1-3 digit fractions to milliseconds
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def seconds_to_timestamp(t: float) -> str:
    """float seconds -> HH:MM:SS,mmm. Inverse of the above; used for round-trip tests."""
    if t < 0:
        t = 0.0
    total_ms = round(t * 1000)
    h, rem = divmod(total_ms, 3600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def parse_srt(text: str, parse_speakers: bool = True) -> list[Cue]:
    """Parse SRT text into a list of Cues, in file order.

    Tolerant of: CRLF, a BOM, both ',' and '.' millisecond separators,
    blank-line padding, and missing trailing newlines.
    """
    text = text.lstrip("﻿").replace("\r\n", "\n").replace("\r", "\n")
    # Blocks are separated by one or more blank lines.
    blocks = re.split(r"\n\s*\n", text.strip())
    cues: list[Cue] = []

    for block in blocks:
        lines = [ln for ln in block.split("\n")]
        # Find the timecode line (it may or may not be preceded by an index line).
        tc_idx = next((i for i, ln in enumerate(lines) if _TIME_RE.search(ln)), None)
        if tc_idx is None:
            continue
        m = _TIME_RE.search(lines[tc_idx])
        start = timestamp_to_seconds(m.group(1), m.group(2), m.group(3), m.group(4))
        end = timestamp_to_seconds(m.group(5), m.group(6), m.group(7), m.group(8))

        # Optional leading index line.
        index = len(cues) + 1
        if tc_idx > 0 and lines[tc_idx - 1].strip().isdigit():
            index = int(lines[tc_idx - 1].strip())

        raw_text = " ".join(ln.strip() for ln in lines[tc_idx + 1:] if ln.strip())
        raw_text = _strip_tags(raw_text)
        if not raw_text:
            continue

        speaker = None
        clean_text = raw_text
        if parse_speakers:
            sm = _SPEAKER_RE.match(raw_text)
            if sm:
                speaker, clean_text = sm.group(1).strip(), sm.group(2).strip()

        cues.append(Cue(index=index, start=start, end=end,
                        text=clean_text, speaker=speaker, raw=raw_text))

    return cues


def dedupe_rolling(cues: list[Cue], min_duration: float = 0.05) -> list[Cue]:
    """Collapse YouTube-style rolling auto-captions into clean utterances.

    Auto-captions repeat the previous line as on-screen context and emit tiny
    transition cues. Strategy: drop near-zero-duration cues, then for each
    remaining cue keep only the suffix that is genuinely NEW relative to the
    words we have already emitted. Re-numbers the survivors.

    On a normal (non-rolling) .srt this is close to a no-op, so it is safe to
    pass --dedupe-rolling defensively. We still gate it behind a flag so clean
    files are never altered by surprise.
    """
    out: list[Cue] = []
    prev_words: list[str] = []

    for c in cues:
        if (c.end - c.start) < min_duration:
            continue  # transition cue
        words = c.text.split()
        # Find the longest overlap where the tail of prev_words == head of words.
        new_words = words
        max_overlap = min(len(prev_words), len(words))
        for k in range(max_overlap, 0, -1):
            if [w.lower() for w in prev_words[-k:]] == [w.lower() for w in words[:k]]:
                new_words = words[k:]
                break
        if not new_words:
            # No new content; extend the previous cue's end time so we don't
            # lose the fact that it stayed on screen.
            if out:
                out[-1].end = max(out[-1].end, c.end)
            prev_words = words
            continue
        text = " ".join(new_words).strip()
        out.append(Cue(index=len(out) + 1, start=c.start, end=c.end,
                       text=text, speaker=c.speaker, raw=c.raw))
        prev_words = words

    return out


def _strip_tags(text: str) -> str:
    """Remove WebVTT/SRT inline markup (<c>, <i>, <00:00:00.000> karaoke tags)."""
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()
