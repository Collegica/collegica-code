#!/bin/sh
# inspect.sh NAME URL — download a clip, print its duration and size, and make a contact sheet (2 fps, 5x4 tiles for 10 s).
set -e
name=$1; url=$2
curl -sL -o "$name.mp4" "$url"
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of csv=p=0 "$name.mp4" | tr '\n' ' '; echo
ffmpeg -hide_banner -loglevel error -y -i "$name.mp4" -vf 'fps=2,scale=384:-1,tile=5x4' -frames:v 1 "$name-contact.jpg"
echo "$name-contact.jpg"
