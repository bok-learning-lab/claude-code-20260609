#!/usr/bin/env python3
"""
respace_monologue.py — rebuild a monologue from a diarize.md, inserting
gaps where the performer pauses.

Input format (one utterance per line):

    **[HH:MM:SS --> HH:MM:SS]** **A:**  Some spoken text.

For each utterance we know when it ends and when the next one starts. The
silence in between is the performer's pause. This script reflows the text
as a continuous monologue and marks every pause whose length meets a
threshold, so the *rhythm* of the delivery survives in plain text.

Standard library only — no pip install.

Usage:
    python3 operations/scripts/respace_monologue.py \
        --md inputs/labeouf_diarize.md

Options:
    --min-gap   SECONDS  smallest pause worth marking      (default 0.75)
    --style     STYLE    how to render a pause: one of
                         "ellipsis"  -> "..." (longer pause = more dots)
                         "seconds"   -> "(1.5s)"
                         "newlines"  -> blank lines (1 per ~second)
                         (default "seconds")
    --out       FILE     write here instead of stdout
"""

import argparse
import re
import sys

LINE_RE = re.compile(
    r"\*\*\[(\d{2}):(\d{2}):(\d{2})\s*-->\s*(\d{2}):(\d{2}):(\d{2})\]\*\*"
    r"\s*\*\*([^*]+?):\*\*\s*(.*\S)\s*$"
)


def to_seconds(h, m, s):
    return int(h) * 3600 + int(m) * 60 + int(s)


def parse(path):
    """Return a list of (start, end, speaker, text) tuples."""
    utterances = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            m = LINE_RE.match(line)
            if not m:
                continue
            sh, sm, ss, eh, em, es, speaker, text = m.groups()
            utterances.append(
                (to_seconds(sh, sm, ss), to_seconds(eh, em, es),
                 speaker.strip(), text.strip())
            )
    return utterances


def render_gap(seconds, style):
    if style == "seconds":
        return f"({seconds:g}s)"
    if style == "newlines":
        return "\n" * (1 + int(round(seconds)))
    # ellipsis: ~one dot-group per second, min one group of three
    groups = max(1, int(round(seconds)))
    return " " + ("..." * groups)


def build(utterances, min_gap, style):
    parts = []
    for i, (start, end, _speaker, text) in enumerate(utterances):
        parts.append(text)
        if i + 1 < len(utterances):
            next_start = utterances[i + 1][0]
            gap = next_start - end
            if gap >= min_gap:
                marker = render_gap(gap, style)
                if style == "newlines":
                    parts.append(marker)
                else:
                    parts.append(" " + marker)
            parts.append("\n" if style != "newlines" else "")
        # close out the utterance
    if style == "newlines":
        return " ".join(p for p in parts if p)
    return "".join(parts).strip() + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--md", required=True, help="path to the diarize.md file")
    ap.add_argument("--min-gap", type=float, default=0.75,
                    help="smallest pause (seconds) worth marking")
    ap.add_argument("--style", default="seconds",
                    choices=["ellipsis", "seconds", "newlines"])
    ap.add_argument("--out", default=None, help="output file (default stdout)")
    args = ap.parse_args(argv)

    utterances = parse(args.md)
    if not utterances:
        sys.exit(f"No utterances parsed from {args.md} — check the format.")

    text = build(utterances, args.min_gap, args.style)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Wrote {args.out} ({len(utterances)} utterances).", file=sys.stderr)
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
