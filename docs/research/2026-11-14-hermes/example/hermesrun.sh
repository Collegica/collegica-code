#!/bin/bash
# hermesrun.sh <folder> <prompt-file> <tag> [--resume <session-id>]
# One Hermes Agent turn inside <folder>; outputs to <folder>.out/
# Needs HERMES_HOME (an empty data root, so none of the owner's memory, skills,
# SOUL.md or config load) holding only the sign-in for the provider. Default: ChatGPT
# Terra (openai-codex, gpt-5.6-terra). Free-model runs: OPENROUTER_API_KEY in the
# environment, HERMES_PROVIDER=openrouter, HERMES_MODEL=nvidia/nemotron-3-ultra-550b-a55b:free.
# Model pinned; tools limited to files, terminal and todo; file writes confined
# to the folder; `chat --oneshot` applies approvals.single_query_mode (default
# "deny": a dangerous command is refused, nothing asks).
dir="$1"; pf="$2"; tag="$3"; shift 3
cd "$dir" || exit 2
o="$dir.out"; mkdir -p "$o"
# the same for every run: a Hermes background process keeps the value it first saw
export HERMES_WRITE_SAFE_ROOT="${HERMES_WRITE_SAFE_ROOT:-$(dirname "$dir")}"
start=$(python3 -c 'import time;print(time.time())')
hermes chat --oneshot --query-file "$pf" \
  --provider "${HERMES_PROVIDER:-openai-codex}" -m "${HERMES_MODEL:-gpt-5.6-terra}" \
  -t file,terminal,todo --in "$dir" --format stream-json "$@" \
  > "$o/$tag.jsonl" 2> "$o/$tag.err"
rc=$?
end=$(python3 -c 'import time;print(time.time())')
python3 -c "print(f'exit {$rc} wall {$end-$start:.1f} s')" > "$o/$tag.time"
cat "$o/$tag.time"
