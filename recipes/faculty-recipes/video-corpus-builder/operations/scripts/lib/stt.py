"""Speech-to-text — the pluggable slot for videos that arrive WITHOUT a .srt.

The pipeline has exactly one ingest path: a .srt file (see lib/srt.py). When a
video has no subtitles, an STT engine must PRODUCE one first. Keeping STT behind
this interface means the rest of the pipeline never knows or cares which engine
ran — and a language swap is a one-class change.

An Engine is anything with:

    transcribe(media_path) -> str   # returns SRT text (HH:MM:SS,mmm cues)

We deliberately return SRT (not raw JSON) so the engine's output re-enters the
single .srt ingest path and timestamps are preserved end to end.

ENGINES:
  * DiarizingShellEngine — wraps the existing operations/scripts/transcribe_parallel
    script (OpenAI gpt-4o-transcribe-diarize). Good general-purpose English +
    many languages, with speaker labels.
  * LevantineArabicEngine — STUB. Levantine Arabic needs a dialect-capable
    model; a generic English ASR will mis-transcribe it. Wire your model in here.

This module is intentionally NOT imported by build_corpus.py's happy path: the
demo ships with .srt files already, so no API keys are needed to build the
corpus. STT is invoked only when you explicitly ask to transcribe a bare video.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


class STTEngine:
    """Interface. Subclass and implement transcribe()."""

    lang = "und"

    def transcribe(self, media_path: str) -> str:  # pragma: no cover - interface
        """Return SRT text for the given audio/video file."""
        raise NotImplementedError


class DiarizingShellEngine(STTEngine):
    """Adapter over operations/scripts/transcribe_parallel (OpenAI diarizing transcribe).

    That script writes a *_diarize.md (wall-clock times) and *_diarize.json next
    to the media. This adapter runs it, then converts the JSON's relative
    segment times into clean SRT cues with "SPEAKER: text" so lib/srt.py can
    recover the speaker. Requires OPENAI_API_KEY and ffmpeg/curl/jq.
    """

    lang = "en"

    def __init__(self, script_path: str | None = None):
        here = Path(__file__).resolve().parent.parent
        self.script_path = script_path or str(here / "transcribe_parallel")

    def transcribe(self, media_path: str) -> str:
        media = Path(media_path)
        subprocess.run([self.script_path, str(media)], check=True)
        # The script emits <dir>/<basename>/<basename>_diarize.json
        out_dir = media.with_suffix("")
        diarize_json = out_dir / f"{media.stem}_diarize.json"
        if not diarize_json.exists():
            raise FileNotFoundError(
                f"transcribe_parallel did not produce {diarize_json}; "
                "check its output above."
            )
        return self._json_to_srt(diarize_json.read_text())

    @staticmethod
    def _json_to_srt(json_text: str) -> str:
        import json

        from .srt import seconds_to_timestamp

        data = json.loads(json_text)
        segments = data.get("segments", data if isinstance(data, list) else [])
        lines: list[str] = []
        for i, seg in enumerate(segments, start=1):
            start = seconds_to_timestamp(float(seg.get("start", 0.0)))
            end = seconds_to_timestamp(float(seg.get("end", 0.0)))
            spk = seg.get("speaker")
            text = (seg.get("text") or "").strip()
            if spk:
                text = f"{spk}: {text}"
            lines += [str(i), f"{start} --> {end}", text, ""]
        return "\n".join(lines)


class LevantineArabicEngine(STTEngine):
    """STUB — wire a dialect-capable Levantine Arabic ASR in here.

    Generic ASR mis-handles Levantine Arabic. Options to evaluate: a fine-tuned
    Whisper-large variant for Levantine/Gulf, or a vendor API with explicit
    dialect support. Implement transcribe() to return SRT text and register the
    engine where you select engines (build_corpus.py / your own driver).
    """

    lang = "ar"

    def transcribe(self, media_path: str) -> str:  # pragma: no cover - stub
        raise NotImplementedError(
            "Levantine Arabic STT is not wired up. Plug in a dialect-capable "
            "model and return SRT text. Do NOT use a generic English ASR."
        )


_ENGINES: dict[str, type[STTEngine]] = {
    "diarize": DiarizingShellEngine,
    "ar-levantine": LevantineArabicEngine,
}


def get_engine(name: str = "diarize") -> STTEngine:
    if name not in _ENGINES:
        raise KeyError(f"Unknown STT engine '{name}'. Known: {sorted(_ENGINES)}")
    return _ENGINES[name]()
