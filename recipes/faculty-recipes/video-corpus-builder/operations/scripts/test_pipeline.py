#!/usr/bin/env python3
"""Tests for the corpus pipeline. Run: python3 operations/scripts/test_pipeline.py

Standard library only (unittest) — no pytest needed. The most important tests
guard the one invariant the whole tool rests on: SRT timestamps survive
parsing and round-trip exactly, because they are how the site seeks the video.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import srt as srtlib
from lib import diarize as diarizelib
from lib.lemmatize import EnglishLemmatizer, get_lemmatizer

INPUTS = Path(__file__).resolve().parent.parent.parent / "inputs"


class TimestampRoundTrip(unittest.TestCase):
    def test_to_seconds_basic(self):
        self.assertEqual(srtlib.timestamp_to_seconds("00", "00", "00", "000"), 0.0)
        self.assertAlmostEqual(
            srtlib.timestamp_to_seconds("01", "02", "03", "456"),
            3600 + 120 + 3 + 0.456)

    def test_to_seconds_matches_handoff_example(self):
        # handoff.md uses start = 134.92 -> 00:02:14,920
        self.assertAlmostEqual(
            srtlib.timestamp_to_seconds("00", "02", "14", "920"), 134.92)

    def test_round_trip_seconds_to_timestamp_to_seconds(self):
        for t in [0.0, 0.001, 1.5, 134.92, 3599.999, 3661.25, 7325.728]:
            ts = srtlib.seconds_to_timestamp(t)
            back = srtlib.timestamp_to_seconds(*_split_ts(ts))
            self.assertAlmostEqual(t, back, places=3, msg=f"{t} -> {ts} -> {back}")

    def test_comma_and_dot_separators(self):
        a = srtlib.parse_srt("1\n00:00:01,500 --> 00:00:02,000\nhi\n")
        b = srtlib.parse_srt("1\n00:00:01.500 --> 00:00:02.000\nhi\n")
        self.assertEqual(a[0].start, 1.5)
        self.assertEqual(b[0].start, 1.5)


class SrtParsing(unittest.TestCase):
    def test_basic_block(self):
        cues = srtlib.parse_srt(
            "1\n00:00:00,000 --> 00:00:01,000\nA: Just do it!\n")
        self.assertEqual(len(cues), 1)
        self.assertEqual(cues[0].speaker, "A")
        self.assertEqual(cues[0].text, "Just do it!")
        self.assertEqual(cues[0].start, 0.0)
        self.assertEqual(cues[0].end, 1.0)

    def test_crlf_and_bom(self):
        cues = srtlib.parse_srt(
            "﻿1\r\n00:00:00,000 --> 00:00:01,000\r\nhello\r\n")
        self.assertEqual(len(cues), 1)
        self.assertEqual(cues[0].text, "hello")

    def test_strips_inline_tags(self):
        cues = srtlib.parse_srt(
            "1\n00:00:00,000 --> 00:00:01,000\n<c>hello</c> <i>there</i>\n")
        self.assertEqual(cues[0].text, "hello there")

    def test_local_sample_file(self):
        srt = INPUTS / "madeleine.srt"
        if not srt.exists():
            self.skipTest("sample SRT not present")
        cues = srtlib.parse_srt(srt.read_text())
        self.assertEqual(len(cues), 9)
        self.assertTrue(all(c.speaker == "A" for c in cues))
        # millisecond precision preserved from the diarized source
        self.assertEqual(cues[0].start, 1.2)
        self.assertEqual(cues[0].end, 2.7)
        # timestamps strictly non-decreasing
        for a, b in zip(cues, cues[1:]):
            self.assertLessEqual(a.start, b.start)


class RollingDedupe(unittest.TestCase):
    def test_collapses_overlap_and_drops_transitions(self):
        raw = (
            "1\n00:00:03,000 --> 00:00:05,000\ndo\n\n"
            "2\n00:00:05,000 --> 00:00:05,010\ndo\n\n"          # transition cue
            "3\n00:00:05,010 --> 00:00:07,000\ndo it just do\n\n"
            "4\n00:00:07,000 --> 00:00:09,000\nit just do it\n"
        )
        cues = srtlib.dedupe_rolling(srtlib.parse_srt(raw))
        joined = " ".join(c.text for c in cues)
        # No immediate duplicate words from the rolling overlap.
        self.assertNotIn("do do", joined)
        # The 10ms transition cue is gone.
        self.assertTrue(all((c.end - c.start) >= 0.05 for c in cues))
        # Content is preserved in order.
        self.assertIn("just", joined)
        self.assertIn("it", joined)


class DiarizeJson(unittest.TestCase):
    SAMPLE = (
        '{"segments": ['
        '{"start": 1.2, "end": 2.7, "speaker": "A", "text": " Just do it!"},'
        '{"start": 17.599999999999998, "end": 19.75, "speaker": "A", "text": " Just, just,"}'
        ']}'
    )

    def test_parses_segments_with_precision(self):
        cues = diarizelib.parse_diarize_json(self.SAMPLE)
        self.assertEqual(len(cues), 2)
        self.assertEqual(cues[0].start, 1.2)
        self.assertEqual(cues[0].end, 2.7)
        self.assertEqual(cues[0].speaker, "A")
        self.assertEqual(cues[0].text, "Just do it!")
        # floating-point noise is rounded to milliseconds
        self.assertEqual(cues[1].start, 17.6)

    def test_to_srt_round_trips_through_srt_parser(self):
        srt_text = diarizelib.diarize_json_to_srt(self.SAMPLE)
        cues = srtlib.parse_srt(srt_text)            # speaker prefix recovered
        self.assertEqual(cues[0].speaker, "A")
        self.assertEqual(cues[0].text, "Just do it!")
        self.assertEqual(cues[0].start, 1.2)
        self.assertEqual(cues[1].start, 17.6)

    def test_srt_and_json_paths_agree_on_sample(self):
        srt_file = INPUTS / "madeleine.srt"
        json_file = INPUTS / "madeleine.json"
        if not (srt_file.exists() and json_file.exists()):
            self.skipTest("sample files not present")
        from_srt = srtlib.parse_srt(srt_file.read_text())
        from_json = diarizelib.parse_diarize_json(json_file.read_text())
        self.assertEqual(len(from_srt), len(from_json))
        for a, b in zip(from_srt, from_json):
            self.assertEqual((a.start, a.end, a.text, a.speaker),
                             (b.start, b.end, b.text, b.speaker))


class Lemmatization(unittest.TestCase):
    def setUp(self):
        self.lem = EnglishLemmatizer()

    def test_irregulars(self):
        self.assertEqual(self.lem._lemma("went"), "go")
        self.assertEqual(self.lem._lemma("said"), "say")
        self.assertEqual(self.lem._lemma("being"), "be")

    def test_regular_suffixes(self):
        self.assertEqual(self.lem._lemma("dreams"), "dream")
        self.assertEqual(self.lem._lemma("running"), "run")
        self.assertEqual(self.lem._lemma("making"), "make")

    def test_tokenize_keeps_contractions(self):
        self.assertEqual(self.lem.tokenize("don't stop"), ["don't", "stop"])

    def test_go_finds_going_and_went(self):
        # The core promise: surface forms collapse to one lemma.
        self.assertEqual(self.lem._lemma("going"), "go")
        self.assertEqual(self.lem._lemma("goes"), "go")
        self.assertEqual(self.lem._lemma("went"), "go")

    def test_arabic_engine_refuses_silently(self):
        ar = get_lemmatizer("ar")
        with self.assertRaises(NotImplementedError):
            ar.lemmatize("مرحبا")


def _split_ts(ts: str):
    hms, ms = ts.split(",")
    h, m, s = hms.split(":")
    return h, m, s, ms


if __name__ == "__main__":
    unittest.main(verbosity=2)
