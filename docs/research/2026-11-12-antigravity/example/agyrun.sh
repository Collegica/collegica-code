#!/bin/bash
# agyrun.sh <folder> <prompt-file> <tag> [extra agy args...]
# One headless Antigravity CLI turn inside <folder>; outputs to <folder>.out/
# Permissions: accept-edits mode, terminal sandbox, and session-only settings
# (agy-session-settings.json, passed with --settings, never saved): commands
# run in the sandbox only if on a short allow list; anything else, and any
# command outside the sandbox, is denied because headless runs cannot ask.
here="$(cd "$(dirname "$0")" && pwd)"
dir="$1"; pf="$2"; tag="$3"; shift 3
cd "$dir" || exit 2
o="$dir.out"; mkdir -p "$o"
start=$(python3 -c 'import time;print(time.time())')
agy -p "$(cat "$pf")" --model "${AGY_MODEL:-gemini-4-argon-medium}" \
  --mode "${AGY_MODE:-accept-edits}" --sandbox \
  --settings "$here/agy-session-settings.json" \
  --output-format json "$@" > "$o/$tag.json" 2> "$o/$tag.err"
rc=$?
end=$(python3 -c 'import time;print(time.time())')
python3 -c "print(f'exit {$rc} wall {$end-$start:.1f} s')" > "$o/$tag.time"
cat "$o/$tag.time"
