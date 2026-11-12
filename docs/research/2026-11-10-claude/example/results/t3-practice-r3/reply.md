The five notes are renamed and `notes/index.md` is written, both exactly as in the plan. The text of every note is byte-for-byte unchanged.

## What I checked

**1. No text was lost.** The SHA-256 checksum of each note before the rename matches the checksum under its new name, and the byte counts match too.

| New name | Old name | Bytes | SHA-256 (before = after) |
|---|---|---|---|
| `2026-09-08-committee-meeting.md` | `Meeting sept 8.md` | 760 | `1e96b297…0f80c2ac` |
| `2026-09-22-committee-meeting.md` | `notes_2026-09-22.md` | 652 | `b9b3719d…5d0c762b` |
| `2026-10-06-committee-meeting.md` | `oct6 meeting notes.md` | 591 | `4b4ad762…0b9b021b` |
| `2026-10-20-committee-meeting.md` | `2026.10.20 minutes.md` | 647 | `5819a741…1bf50f4d` |
| `2026-11-03-committee-meeting.md` | `Nov 3 (final).md` | 711 | `f004b034…4486563b` |

**2. Each filename matches its meeting date.** After renaming, I read the first line of each file, and the heading date agrees with the date in the filename in all five.

**3. The folder holds what it should.** `notes/` contains exactly the five renamed notes plus `index.md`, with no old names left behind. `README.md` and `members.csv` are the same size and timestamp as before.

**4. The index links resolve.** The five link targets in `index.md` are the five new filenames, character for character.

One departure from the plan: I did not save the "before" checksums to a file outside the folder. They were only printed in this session, so the comparison above is the record.