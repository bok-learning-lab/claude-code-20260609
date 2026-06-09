#!/bin/bash
#
# download_youtube.sh — fetch a YouTube video + its subtitles into inputs/
#
# Part of the video-corpus-builder recipe. This is the "Mode B" ingest
# step: grab a hosted YouTube video so the pipeline has a real video and
# (when available) a real subtitle track to chew on.
#
# What it does:
#   1. Downloads the video as an .mp4 into inputs/ (capped at 540p so the
#      workshop demo stays small — match the local sample resolution).
#   2. Downloads human or auto-generated subtitles, converted to .srt.
#      The .srt is the single ingest format the build pipeline expects
#      (see operations/scripts/build_corpus.py). If real subs exist we keep those;
#      otherwise we fall back to YouTube's auto-captions.
#   3. Names every file by the YouTube video id so a video and its
#      subtitles stay paired (e.g. labeouf.mp4 / labeouf.en.srt).
#
# Usage:
#   ./download_youtube.sh                       # downloads the default demo video
#   ./download_youtube.sh <youtube-url-or-id>   # downloads any video
#   ./download_youtube.sh <url> <lang>          # pick a subtitle language (default: en)
#
# Requires: yt-dlp (brew install yt-dlp), ffmpeg (for the .srt conversion).
#
# NOTE on Levantine Arabic and other dialects: YouTube auto-captions are
# often poor or absent for the languages this project targets. When that
# happens, download the video here, then run the diarizing transcriber
# (operations/scripts/transcribe_parallel) or another STT engine to PRODUCE the
# .srt instead. Either path lands a .srt in inputs/ for build_corpus.py.

set -euo pipefail

# ---- defaults -------------------------------------------------------------

# The video Marlon asked to seed the corpus with.
DEFAULT_VIDEO="https://www.youtube.com/watch?v=ZXsQAXx_ao0"

INPUT_ARG="${1:-$DEFAULT_VIDEO}"
SUB_LANG="${2:-en}"

# Resolve where inputs/ lives relative to THIS script, so the command works
# no matter what directory you run it from.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # operations/scripts/
INPUTS_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)/inputs"          # <recipe>/inputs/

# ---- dependency checks ----------------------------------------------------

for cmd in yt-dlp ffmpeg; do
  if ! command -v "$cmd" &> /dev/null; then
    echo "Error: '$cmd' is required but not installed." >&2
    case "$cmd" in
      yt-dlp) echo "       Install it with: brew install yt-dlp" >&2 ;;
      ffmpeg) echo "       Install it with: brew install ffmpeg" >&2 ;;
    esac
    exit 1
  fi
done

mkdir -p "$INPUTS_DIR"

echo "=== video-corpus-builder :: YouTube download ==="
echo "Source : $INPUT_ARG"
echo "Subs   : $SUB_LANG (human first, auto-captions as fallback)"
echo "Into   : $INPUTS_DIR"
echo ""

# ---- download -------------------------------------------------------------

# Output template: name everything by the YouTube id so video + subs pair up.
# %(id)s.%(ext)s  ->  labeouf.mp4 , labeouf.en.srt
OUTPUT_TEMPLATE="$INPUTS_DIR/%(id)s.%(ext)s"

# Format: best video+audio at <=540p, muxed to mp4. Keeps the demo small and
# matches the local JUSTDOIT sample's resolution.
FORMAT='bestvideo[height<=540][ext=mp4]+bestaudio[ext=m4a]/best[height<=540]/best'

yt-dlp \
  --no-playlist \
  --format "$FORMAT" \
  --merge-output-format mp4 \
  --write-subs \
  --write-auto-subs \
  --sub-langs "$SUB_LANG" \
  --convert-subs srt \
  --restrict-filenames \
  --output "$OUTPUT_TEMPLATE" \
  "$INPUT_ARG"

echo ""
echo "=== Done ==="

# ---- report what landed ---------------------------------------------------

# Figure out the id so we can point at the files we just wrote.
VIDEO_ID="$(yt-dlp --no-playlist --get-id "$INPUT_ARG" 2>/dev/null | head -n1 || true)"

if [ -n "$VIDEO_ID" ]; then
  echo "Files for $VIDEO_ID in inputs/:"
  ls -1 "$INPUTS_DIR" | grep -F "$VIDEO_ID" | sed 's/^/  - /' || echo "  (none matched — check yt-dlp output above)"
  echo ""
  SRT_PATH="$INPUTS_DIR/${VIDEO_ID}.${SUB_LANG}.srt"
  if [ -f "$SRT_PATH" ]; then
    echo "Next step: build the corpus from the downloaded .srt, e.g."
    echo "  python3 operations/scripts/build_corpus.py \\"
    echo "    --srt inputs/${VIDEO_ID}.${SUB_LANG}.srt \\"
    echo "    --youtube-id ${VIDEO_ID} \\"
    echo "    --title \"<a human-readable title>\""
  else
    echo "No .srt was produced (this video may have no $SUB_LANG captions)."
    echo "Generate one with the transcriber, then build:"
    echo "  ./operations/scripts/transcribe_parallel inputs/${VIDEO_ID}.mp4"
  fi
fi
