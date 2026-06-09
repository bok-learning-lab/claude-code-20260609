#!/usr/bin/env python3
"""diarize_to_srt.py — convert a diarized-transcript JSON into a precise .srt.

The diarizing transcriber emits JSON with sub-second timestamps and speaker
labels. This turns that JSON into a millisecond-precision .srt (speaker tags
kept as an "A: " prefix) so it flows through the normal .srt ingest path with
nothing lost.

Usage:
  python3 operations/scripts/diarize_to_srt.py inputs/madeleine.json
  python3 operations/scripts/diarize_to_srt.py inputs/foo.json -o inputs/foo.srt

With no -o, writes alongside the JSON with a .srt extension.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.diarize import diarize_json_to_srt


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("json", help="diarized-transcript JSON file")
    p.add_argument("-o", "--out", help="output .srt path (default: <json>.srt)")
    args = p.parse_args(argv)

    src = Path(args.json)
    out = Path(args.out) if args.out else src.with_suffix(".srt")
    srt_text = diarize_json_to_srt(src.read_text(encoding="utf-8"))
    out.write_text(srt_text, encoding="utf-8")
    n = srt_text.count(" --> ")
    print(f"Wrote {n} cues -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
