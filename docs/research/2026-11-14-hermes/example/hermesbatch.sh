#!/bin/bash
# hermesbatch.sh <workdir> : the thirty runs, one at a time (free model, rate limits).
# Needs HERMES_HOME (with the provider sign-in) exported. Tasks from
# ../../2026-11-10-assistant-guides/tasks/. Re-running skips finished runs.
here="$(cd "$(dirname "$0")" && pwd)"
T="$here/../../2026-11-10-assistant-guides/tasks"
W="$1"; mkdir -p "$W"; W="$(cd "$W" && pwd -P)"
export HERMES_WRITE_SAFE_ROOT="$W"
run() { # tag promptfile [rules]
  local tag="$1" pf="$2" rules="$3" d="$W/$1"
  [ -e "$d.out/turn1.time" ] && return
  python3 "$T/make_folder.py" "$d" >/dev/null
  [ -n "$rules" ] && cp "$T/house-rules.md" "$d/AGENTS.md"
  "$here/hermesrun.sh" "$d" "$pf" turn1
}
for r in 1 2 3; do
  run t1-plain-r$r "$T/prompts/t1-plain.txt"
  run t1-practice-r$r "$T/prompts/t1-practice.txt"
  run t2-plain-r$r "$T/prompts/t2.txt"
  run t2-practice-r$r "$T/prompts/t2.txt" rules
  for k in plain practice; do
    run t4-$k-r$r "$T/prompts/t4-$k.txt"
    run t5-$k-r$r "$T/prompts/t5-$k.txt"
  done
  run t3-plain-r$r "$T/prompts/t3-plain.txt"
  d="$W/t3-practice-r$r"
  if [ ! -e "$d.out/turn2.time" ]; then
    python3 "$T/make_folder.py" "$d" >/dev/null
    "$here/hermesrun.sh" "$d" "$T/prompts/t3-practice-1.txt" turn1
    sid=$(grep -o '"session_id": "[^"]*"' "$d.out/turn1.jsonl" | tail -1 | cut -d'"' -f4)
    echo "$sid" > "$d.out/session-id.txt"
    "$here/hermesrun.sh" "$d" "$T/prompts/t3-practice-2.txt" turn2 --resume "$sid"
  fi
done
