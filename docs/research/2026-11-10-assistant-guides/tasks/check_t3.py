"""Check a folder after task 3 (tidy the notes).

    python3 check_t3.py <folder-after-the-task>           # careful prompt
    python3 check_t3.py --plain <folder-after-the-task>   # plain prompt

Passes when all seven notes are still there with their text unchanged, each
is named for the date of its own meeting (from its heading, which for
"minutes 25 aug.md" is the 26th, not the 25th), and one index lists them all.

The careful prompt names the pattern YYYY-MM-DD-committee-meeting.md and the
index notes/index.md, so it is held to both. The plain prompt names neither,
so with --plain any name starting with the right date passes
(2026-08-26.md, 2026-08-26-minutes.md) and any new Markdown file in notes/
or the folder that lists every note counts as the index; its name is
reported. Version 2.1, 2026-11-12: the --plain rule was added after ChatGPT
and Grok failed version 2 only on these two points. Prints one line per check
and exits 1 if any fails.
"""

import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from make_folder import NOTES  # noqa: E402

DATES = {
    "aug11.md": "2026-08-11",
    "minutes 25 aug.md": "2026-08-26",
    "Meeting sept 8.md": "2026-09-08",
    "notes_2026-09-22.md": "2026-09-22",
    "oct6 meeting notes.md": "2026-10-06",
    "2026.10.20 minutes.md": "2026-10-20",
    "Nov 3 (final).md": "2026-11-03",
}


def digest(text: str) -> str:
    return hashlib.sha256(text.strip().encode()).hexdigest()


def main(folder: Path, plain: bool) -> int:
    notes = folder / "notes"
    originals = {digest(t) for t in NOTES.values()}
    found = {p.name: p.read_text() for p in notes.glob("*.md")}
    by_digest = {digest(t): n for n, t in found.items() if digest(t) in originals}
    candidates = [p for p in list(notes.glob("*.md")) + list(folder.glob("*.md"))
                  if digest(p.read_text()) not in originals]
    failed = 0

    def report(ok: bool, what: str) -> None:
        nonlocal failed
        failed += not ok
        print(("ok    " if ok else "FAIL  ") + what)

    report(len(by_digest) == len(NOTES), f"{len(NOTES)} notes with their text unchanged (found {len(by_digest)})")
    names = []
    for old, text in NOTES.items():
        new = by_digest.get(digest(text))
        report(new is not None, f"text unchanged: {old}")
        if new is None:
            continue
        names.append(new)
        want = DATES[old]
        pattern = rf"{want}(-[A-Za-z0-9-]+)?\.md" if plain else rf"{want}-[a-z0-9-]+\.md"
        report(re.fullmatch(pattern, new) is not None,
               f"named {want}{'[-<words>]' if plain else '-<words>'}.md: {new}")

    if plain:
        index = next((p for p in candidates if names and all(n in p.read_text() for n in names)), None)
        report(index is not None, f"an index lists every note: {index.relative_to(folder) if index else 'none found'}")
    else:
        idx = notes / "index.md"
        text = idx.read_text() if idx.exists() else ""
        report(idx.exists(), "notes/index.md exists")
        for n in names:
            report(n in text, f"listed in index.md: {n}")
    return 1 if failed else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    plain = "--plain" in args
    args = [a for a in args if a != "--plain"]
    if len(args) != 1:
        sys.exit(__doc__)
    sys.exit(main(Path(args[0]), plain))
