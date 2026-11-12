#!/bin/sh
# Builds the scratch repository used to try Herdr with two agents.
# Usage: sh make_scratch_repo.sh <empty-directory-outside-any-git-repo>
# The project is made up: a tiny tally of a garden club's seed swap.
set -eu
dir="$1"
mkdir -p "$dir"
cd "$dir"
git init -q -b main
git config user.name "Scratch Tester"
git config user.email "tester@example.com"

cat > seeds.py <<'EOF'
"""Seed swap tally for the Maple Lane garden club (made-up data)."""

SWAPS = [
    ("Ada Finch", "tomato", 12),
    ("Ben Wren", "bean", 30),
    ("Ada Finch", "bean", 8),
    ("Cora Teal", "squash", 5),
]


def total_by_member(swaps):
    totals = {}
    for member, _kind, count in swaps:
        totals[member] = totals.get(member, 0) + count
    return totals


if __name__ == "__main__":
    for member, count in total_by_member(SWAPS).items():
        print(f"{member}: {count}")
EOF

cat > TASKS.md <<'EOF'
# Two small, independent tasks

1. Add a function `total_by_kind(swaps)` to `seeds.py` that returns a dict of
   seed kind to total count, and print it under the member totals.
2. Add a `README.md` of no more than five lines saying what `seeds.py` does
   and how to run it.
EOF

git add seeds.py TASKS.md
git commit -q -m "Seed swap tally"
echo "scratch repo ready in $dir"
