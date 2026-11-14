#!/bin/bash
# hermessupplement.sh <workdir> : the extra runs made after the thirty.
#  - t2-practice-r4..r6: task 2 with house-rules.md as AGENTS.md again, because two of the
#    three first runs never read the notes.
#  - t2-skill-r1..r3: task 2 with the house rules as a Hermes skill (skills/house-rules/SKILL.md
#    in the test data root) preloaded with --skills, and no AGENTS.md.
# Needs HERMES_HOME (with the provider sign-in) exported.
here="$(cd "$(dirname "$0")" && pwd)"
T="$here/../../2026-11-10-assistant-guides/tasks"
W="$1"; mkdir -p "$W"; W="$(cd "$W" && pwd -P)"
export HERMES_WRITE_SAFE_ROOT="$W"
for r in 4 5 6; do
  d="$W/t2-practice-r$r"; python3 "$T/make_folder.py" "$d" >/dev/null
  cp "$T/house-rules.md" "$d/AGENTS.md"
  "$here/hermesrun.sh" "$d" "$T/prompts/t2.txt" turn1
done
for r in 1 2 3; do
  d="$W/t2-skill-r$r"; python3 "$T/make_folder.py" "$d" >/dev/null
  "$here/hermesrun.sh" "$d" "$T/prompts/t2.txt" turn1 --skills house-rules
done
