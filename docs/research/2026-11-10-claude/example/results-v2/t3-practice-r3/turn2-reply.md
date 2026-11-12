All seven notes are renamed and `notes/index.md` is written. The checks show no note's text changed.

**What I checked:**

1. **Text unchanged:** Before renaming, I took a SHA-256 checksum of each note's contents (the fingerprint changes if even one character changes). I took them again afterwards. All 7 match one-for-one, so nothing was lost or altered.
2. **Right file, right name:** I matched each checksum's old filename to its new one, and all seven went where the plan said. I also read the first line of each renamed file, and the date in its `# Committee meeting, …` heading matches the date in its filename.
3. **Nothing overwritten or left behind:** I renamed with `mv -n`, which refuses to replace a file that already exists. `notes/` now holds exactly 8 files: the 7 notes plus `index.md`. None of the old names are left.
4. **Index links work:** All 7 links in `index.md` point to files that exist.
5. **Nothing else touched:** `README.md` and `members.csv` are unchanged, and nothing new was added outside `notes/`. I kept the checksum lists in a temporary folder outside your files and deleted it afterwards.

**Final names:**
- `aug11.md` → `2026-08-11-committee-meeting.md`
- `minutes 25 aug.md` → `2026-08-26-committee-meeting.md`
- `Meeting sept 8.md` → `2026-09-08-committee-meeting.md`
- `notes_2026-09-22.md` → `2026-09-22-committee-meeting.md`
- `oct6 meeting notes.md` → `2026-10-06-committee-meeting.md`
- `2026.10.20 minutes.md` → `2026-10-20-committee-meeting.md`
- `Nov 3 (final).md` → `2026-11-03-committee-meeting.md`

You didn't answer the August question, so I used the date the meeting was actually held, **26 August**. The index line for that note says it was moved from the 25th because of the storm. If you'd rather it were named for the 25th, that's a single rename.