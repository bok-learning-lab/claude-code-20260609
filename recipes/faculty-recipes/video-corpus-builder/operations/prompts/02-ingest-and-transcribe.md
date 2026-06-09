# Step 2 — Get videos in and clean transcripts out

**Goal of this step:** real source material in `inputs/`, and a clean,
precise, speaker-labeled transcript for every video.

---

## Prompt A — pull videos in

> Write me a small shell script, `operations/scripts/download_youtube.sh`, that
> uses `yt-dlp` to download a YouTube video plus its subtitles into `inputs/`.
> Requirements:
> - Take a YouTube URL (or id) as an argument, with a sensible default I can set.
> - Cap the resolution (e.g. ≤540p) so the demo stays small.
> - Save the video and subtitles named by the video id so they stay paired, and
>   convert subtitles to `.srt`.
> - Print a "next step" hint showing how to build the corpus from what it pulled.
>
> Then run it on this video: [paste a YouTube URL].

*(For local videos a faculty member already has, just copy them into `inputs/`.)*

## Prompt B — get a clean transcript

> The captions we pulled are messy [or: this video has no usable subtitles].
> I have a diarizing transcription script at
> `operations/scripts/transcribe_parallel` (OpenAI speech-to-text with speaker
> labels). Run it on `inputs/[video].mp4` to produce a clean transcript with
> sub-second timestamps and speaker labels.
>
> Then **generate a precise `.srt` from that transcript's JSON** (don't hand-type
> timestamps — that loses precision). If we don't have a converter yet, write one
> at `operations/scripts/diarize_to_srt.py`.

---

## Why this works

- **YouTube auto-captions are not good enough.** They come down as overlapping,
  duplicated "rolling" lines with tiny junk cues. For a corpus you want clean
  segments with real speaker turns — so transcribe the audio yourself.
- **Precision is the whole game.** The timestamps are how the site seeks the
  video. Generating the `.srt` straight from the transcriber's JSON keeps
  millisecond precision; typing timestamps by hand silently rounds them and the
  clips land in the wrong place.
- **One ingest format.** Whatever the source (downloaded captions, a transcriber,
  or a hand-authored file), funnel everything to `.srt` (or the diarized `.json`)
  so the build step has a single, predictable input.

## What you should have after this step

- Each video in `inputs/` paired with a clean transcript (`.json`) and a
  precise `.srt`, plus a human-readable transcript for spot-checking.
