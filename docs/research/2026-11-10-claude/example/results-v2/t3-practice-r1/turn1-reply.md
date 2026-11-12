Nothing has been changed. I read all seven notes, the README and `members.csv`. Here's the plan.

## Renames

| Current name | New name | Date taken from |
|---|---|---|
| `aug11.md` | `2026-08-11-committee-meeting.md` | Heading: "11 August 2026" |
| `minutes 25 aug.md` | `2026-08-26-committee-meeting.md` | Heading: "26 August 2026" |
| `Meeting sept 8.md` | `2026-09-08-committee-meeting.md` | Heading: "8 September 2026" |
| `notes_2026-09-22.md` | `2026-09-22-committee-meeting.md` | Heading: "22 September 2026" |
| `oct6 meeting notes.md` | `2026-10-06-committee-meeting.md` | Heading: "6 October 2026" |
| `2026.10.20 minutes.md` | `2026-10-20-committee-meeting.md` | Heading: "20 October 2026" |
| `Nov 3 (final).md` | `2026-11-03-committee-meeting.md` | Heading: "3 November 2026" |

## How I'll work out each date

I'll use the date in each note's first line (`# Committee meeting, <date>`), not the filename. The filenames are inconsistent, and in one case wrong:

- **`minutes 25 aug.md` is the 26 August meeting.** The note says it was "Moved from Monday 25 August because of the storm." So it becomes `2026-08-26`, not `2026-08-25`.
- **The year is missing from three filenames** (`aug11`, `sept 8`, `oct6`). Every heading says 2026, so I'll use that.
- **Each note agrees with the ones around it.** Every note ends with "Next meeting <date>", and that date matches the next file. The one exception is 25 August, which became 26 August as explained above.
- "(final)" in `Nov 3 (final).md` means the last meeting of the year ("No further meetings this year"). It isn't a version marker, and no other Nov 3 draft exists.

All seven dates are different, so no two files will end up with the same name. No file with a new name exists yet.

## The index (`notes/index.md`)

The index will list the notes in date order. Each line links to its note and summarises what was decided. Draft lines:

- **2026-08-11**: Odile to repaint the noticeboard; shed lights to move to the night rate; Nell to ask the city about a second tap.
- **2026-08-26** (moved from 25 Aug, storm): progress only. Lights now on the night rate; Nell still to reach the city about the tap.
- **2026-09-08**: Shed roof to be replaced, not patched (Tessa to get 3 quotes); Ibrahim to send fee reminders; broken gate latch noted but nobody assigned.
- **2026-09-22**: Middle roof quote ($1,480) chosen; Nell to order 4 m³ of compost; Dov takes over the second-tap request.
- **2026-10-06**: Roofer booked for 17 Oct; Wren to replace the gate latch; garden closes end of November, and Tessa will draft a winter checklist.
- **2026-10-20**: Roof invoice ($80 over) held until Paolo gets an explanation; work day set for Sat 14 Nov.
- **2026-11-03**: Roof invoice stays unpaid until the $80 is explained; work-day jobs assigned, including the water shut-off on the day; last meeting of the year.

I'll keep these lines to what the notes actually say.

## How I'll check no text was lost

1. **Before:** record a SHA-256 checksum of every file in `notes/`, plus the file count (7).
2. **Rename only:** use `mv` and never open or rewrite the notes. Before running it, I'll check that the target name doesn't already exist, so nothing gets overwritten.
3. **After:**
   - Checksum the renamed files and compare them against the "before" list, matched by the old→new mapping. All 7 must be identical.
   - Confirm `notes/` contains exactly those 7 dated files plus `index.md`, and nothing else has changed.
   - Confirm each index link points to a file that exists.

I won't touch `README.md` or `members.csv`. The folder isn't a git repo, so the checksums are the safety net. I can also copy `notes/` somewhere first as a backup if you want.

Say the word and I'll go ahead.