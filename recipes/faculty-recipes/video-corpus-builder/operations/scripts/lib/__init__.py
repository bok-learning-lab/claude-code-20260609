"""Shared modules for the video-corpus-builder pipeline.

  srt       — parse .srt into timestamped cues (the single ingest path)
  lemmatize — tokenize + map surface forms to lemmas (pluggable per language)
  stt       — speech-to-text engines that PRODUCE .srt for bare videos (pluggable)

Kept dependency-free (standard library only) so the pipeline runs on a fresh
machine without `pip install`. Language-specific plug-ins (Arabic morphology,
dialect STT) may add their own dependencies behind the interfaces here.
"""
