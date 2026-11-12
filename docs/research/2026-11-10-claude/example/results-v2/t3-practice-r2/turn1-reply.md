Nothing has been changed. Here is the plan.

## Renames

| Current name | New name | Date taken from |
|---|---|---|
| `aug11.md` | `2026-08-11-committee-meeting.md` | heading: 11 August 2026 |
| `minutes 25 aug.md` | `2026-08-26-committee-meeting.md` | heading: **26** August 2026 ⚠️ |
| `Meeting sept 8.md` | `2026-09-08-committee-meeting.md` | heading: 8 September 2026 |
| `notes_2026-09-22.md` | `2026-09-22-committee-meeting.md` | heading: 22 September 2026 |
| `oct6 meeting notes.md` | `2026-10-06-committee-meeting.md` | heading: 6 October 2026 |
| `2026.10.20 minutes.md` | `2026-10-20-committee-meeting.md` | heading: 20 October 2026 |
| `Nov 3 (final).md` | `2026-11-03-committee-meeting.md` | heading: 3 November 2026 |

## How I'll work out each date

I'll use the date in each note's `# Committee meeting, <date>` heading, not the filename. Several filenames have no year, and one of them is wrong:

- **`minutes 25 aug.md` is dated 25 August in its filename, but the meeting was on 26 August.** The note says: "Moved from Monday 25 August because of the storm." I'll name it 26 August. Tell me if you'd rather it be named for the planned date.
- I'll also check the dates against each other. Each note's "Next meeting …" line matches the date of the following note, so the order holds: 11 Aug → 25/26 Aug → 8 Sep → 22 Sep → 6 Oct → 20 Oct → 3 Nov. The 3 November note says there are no further meetings this year.
- The "(final)" in `Nov 3 (final).md` will be dropped from the name. The note's text doesn't say what it meant. My guess is "final version" or "last meeting of the year". Tell me if you want that recorded somewhere.

All seven dates are different, so no two new names clash. I'll use `mv -n`, which refuses to overwrite a file if one is already there.

## notes/index.md

This is the only new file. It will list the notes in date order, each with a link and one line on what was decided. Roughly:

- 2026-08-11: Odile to repaint the noticeboard; shed lights to move to the night rate; Nell to ask the city about a second tap.
- 2026-08-26 (moved from 25 Aug, storm): no new decisions; night rate done, second tap still pending.
- 2026-09-08: Replace the shed roof rather than patch it (Tessa to get 3 quotes); Ibrahim to send fee reminders.
- 2026-09-22: Chose the middle roof quote ($1,480, includes taking the old roofing away); Nell to order 4 m³ of compost; Dov takes over the second-tap request.
- 2026-10-06: Roofer booked for 17 Oct; Wren to replace the gate latch; garden closes end of November, Tessa to draft the winter checklist.
- 2026-10-20: Work day set for Sat 14 Nov; hold payment until the $80 roof overcharge is explained.
- 2026-11-03: Work-day arrangements confirmed (notice, tool sharpener, water shut-off); roof invoice still unpaid until the $80 is explained; no more meetings this year.

I'll show you the final wording before writing it, if you'd like.

## Checking that no text was lost

1. **Before:** record a SHA-256 checksum and byte count for each of the seven files, saved outside `notes/`.
2. **Rename only:** I'll use `mv` and nothing else, so the files' contents are never opened for writing.
3. **After:** take the checksums of the seven renamed files and confirm they match the "before" set exactly. That means seven files and seven identical checksums, each paired with its expected new name.
4. **Confirm:** `notes/` should contain exactly those seven files plus `index.md`, with no leftover old names and no extra files.
5. Leave `README.md` and `members.csv` alone.

I'll wait for your go-ahead, and your answer on the 25/26 August name, before changing anything.