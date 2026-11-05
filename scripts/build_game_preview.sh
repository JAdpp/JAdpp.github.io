#!/usr/bin/env bash
# Usage: build_game_preview.sh <title-cover.png> <verified-preview.mp4> <output-stem>
# Encodes a 1.25s title cover, unchanged project footage, then a 1.25s title cover.
# Inputs must be verified source footage and labeled accurately on the page.
# PV scenes must not be labeled gameplay. No frame synthesis or audio is used.
set -euo pipefail
poster="$1"; gameplay="$2"; stem="$3"
mkdir -p "$(dirname "$stem")"
ffmpeg -hide_banner -loglevel error -y -loop 1 -t 1.25 -i "$poster" -i "$gameplay" -loop 1 -t 1.25 -i "$poster" \
  -filter_complex '[0:v]scale=960:540:force_original_aspect_ratio=decrease,pad=960:540:(ow-iw)/2:(oh-ih)/2:color=0x142026,setsar=1,fps=24,format=yuv420p,setpts=PTS-STARTPTS[a];[1:v]scale=960:540:force_original_aspect_ratio=decrease,pad=960:540:(ow-iw)/2:(oh-ih)/2:color=0x142026,setsar=1,fps=24,format=yuv420p,setpts=PTS-STARTPTS[b];[2:v]scale=960:540:force_original_aspect_ratio=decrease,pad=960:540:(ow-iw)/2:(oh-ih)/2:color=0x142026,setsar=1,fps=24,format=yuv420p,setpts=PTS-STARTPTS[c];[a][b][c]concat=n=3:v=1:a=0[v]' \
  -map '[v]' -an -c:v libx264 -preset slow -crf 25 -pix_fmt yuv420p -color_range tv -movflags +faststart -map_metadata -1 "${stem}-960.mp4"
ffmpeg -hide_banner -loglevel error -y -i "${stem}-960.mp4" -vf 'scale=640:360,fps=20' -an -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p -color_range tv -movflags +faststart -map_metadata -1 "${stem}-640.mp4"
