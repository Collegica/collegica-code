The five notes are renamed and `notes/index.md` is written; the text of every note is byte-for-byte what it was before.

## What I checked

- **Text unchanged:** the SHA-256 checksum of each note after the rename is identical to the one I recorded before it, and the byte counts match.

  | New name | Old name | Bytes | SHA-256 (start) |
  |---|---|---|---|
  | `2026-09-08-committee-meeting.md` | `Meeting sept 8.md` | 760 | `1e96b297…` |
  | `2026-09-22-committee-meeting.md` | `notes_2026-09-22.md` | 652 | `b9b3719d…` |
  | `2026-10-06-committee-meeting.md` | `oct6 meeting notes.md` | 591 | `4b4ad762…` |
  | `2026-10-20-committee-meeting.md` | `2026.10.20 minutes.md` | 647 | `5819a741…` |
  | `2026-11-03-committee-meeting.md` | `Nov 3 (final).md` | 711 | `f004b034…` |

- **Right date on each file:** the heading inside each renamed note gives the same date as its new filename.
- **Nothing extra or missing:** `notes/` holds exactly those five notes plus `index.md`; no old names remain.
- **Other files untouched:** `README.md` and `members.csv` have the same checksums as before.
- **Index links:** the five link targets in `index.md` are the five filenames above. I compared them by eye against the listing rather than with a script.

The index lines are the ones from the plan, unchanged.