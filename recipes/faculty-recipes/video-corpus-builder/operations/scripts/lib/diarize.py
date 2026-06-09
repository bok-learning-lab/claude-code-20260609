"""Diarized-JSON ingest — a second front door that preserves full precision.

The diarizing transcriber (operations/scripts/transcribe_parallel, OpenAI
gpt-4o-transcribe-diarize) emits JSON whose segments carry sub-second
`start`/`end` floats and a `speaker` label, e.g.:

    { "segments": [
        { "start": 1.2, "end": 2.7, "speaker": "A", "text": " Just do it!" },
        { "start": 6.95, "end": 9.65, "speaker": "A", "text": " Don't let..." }
    ] }

That precision is the whole point of diarized data, and a hand-typed SRT throws
it away. This module reads the JSON directly so nothing is lost:

  * parse_diarize_json(text) -> list[srt.Cue]   feed straight into build_corpus
  * diarize_json_to_srt(text) -> str            emit a clean ms-precision .srt

Both accept the two shapes we produce:
  - the combined file  {"startEpoch": ..., "segments": [...]}
  - the plain file     {"text": "...", "segments": [...]}
  - or a bare list     [ {segment}, ... ]

Speaker labels are preserved: the Cue carries `.speaker` directly, and the
emitted SRT uses the "A: text" prefix convention that lib/srt.py reads back.
Floating-point noise (17.599999999999998) is rounded to milliseconds — the
real resolution of the timestamps — so the SRT and the corpus agree exactly.
"""

from __future__ import annotations

import json

from .srt import Cue, seconds_to_timestamp


def _segments(data) -> list[dict]:
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return data.get("segments", [])
    raise ValueError("diarize JSON must be an object with 'segments' or a list")


def parse_diarize_json(text: str) -> list[Cue]:
    """Parse diarized-transcript JSON into timestamped Cues (precision intact)."""
    data = json.loads(text)
    cues: list[Cue] = []
    for i, seg in enumerate(_segments(data), start=1):
        body = (seg.get("text") or "").strip()
        if not body:
            continue
        cues.append(Cue(
            index=i,
            start=round(float(seg.get("start", 0.0)), 3),   # ms resolution
            end=round(float(seg.get("end", 0.0)), 3),
            text=body,
            speaker=(seg.get("speaker") or None),
            raw=body,
        ))
    return cues


def diarize_json_to_srt(text: str) -> str:
    """Render diarized JSON as a clean, millisecond-precise SRT string.

    Speaker labels become an "A: " prefix so a plain .srt still carries them.
    """
    cues = parse_diarize_json(text)
    blocks: list[str] = []
    for n, c in enumerate(cues, start=1):
        line = f"{c.speaker}: {c.text}" if c.speaker else c.text
        blocks.append(
            f"{n}\n"
            f"{seconds_to_timestamp(c.start)} --> {seconds_to_timestamp(c.end)}\n"
            f"{line}\n"
        )
    return "\n".join(blocks)
