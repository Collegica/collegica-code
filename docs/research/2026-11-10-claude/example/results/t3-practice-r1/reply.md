The five notes are renamed and `notes/index.md` is written, with the text of every note byte-for-byte unchanged.

## What I checked

- **Note text unchanged:** I took a SHA-256 checksum of each note before renaming and again afterwards. All five match exactly.

  | New name | Was | Bytes | SHA-256 before = after |
  |---|---|---|---|
  | `2026-09-08-committee-meeting.md` | `Meeting sept 8.md` | 760 | `1e96b297…0f80c2ac` |
  | `2026-09-22-committee-meeting.md` | `notes_2026-09-22.md` | 652 | `b9b3719d…0b0d0c762b` |
  | `2026-10-06-committee-meeting.md` | `oct6 meeting notes.md` | 591 | `4b4ad762…0b9b021b` |
  | `2026-10-20-committee-meeting.md` | `2026.10.20 minutes.md` | 647 | `5819a741…1bf50f4d` |
  | `2026-11-03-committee-meeting.md` | `Nov 3 (final).md` | 711 | `f004b034…4486563b` |

- **Each name matches its meeting:** the heading inside each renamed file gives the same date as its new filename.
- **Nothing left over or lost:** `notes/` now holds exactly the five renamed notes plus `index.md`; no old names remain, and the total is still 3,361 bytes across the five notes.
- **Other files untouched:** `README.md` and `members.csv` have the same checksums as before.
- **No overwrites:** the renames used a move that refuses to replace an existing file, and all five completed.

## The index

`notes/index.md` lists the five meetings in date order, each linked to its note, with the one-line wording from the plan. I did not test the links in a markdown viewer; they are plain relative filenames matching the names above.