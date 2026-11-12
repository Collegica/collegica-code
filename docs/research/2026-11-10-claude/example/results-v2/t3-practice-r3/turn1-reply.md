I've read all seven notes and changed nothing. Here is the plan.

## Renames (all inside `notes/`)

| Current name | New name | Date taken from |
|---|---|---|
| `aug11.md` | `2026-08-11-committee-meeting.md` | heading: "11 August 2026" |
| `minutes 25 aug.md` | `2026-08-26-committee-meeting.md` | heading: "26 August 2026" (see below) |
| `Meeting sept 8.md` | `2026-09-08-committee-meeting.md` | heading: "8 September 2026" |
| `notes_2026-09-22.md` | `2026-09-22-committee-meeting.md` | heading: "22 September 2026" |
| `oct6 meeting notes.md` | `2026-10-06-committee-meeting.md` | heading: "6 October 2026" |
| `2026.10.20 minutes.md` | `2026-10-20-committee-meeting.md` | heading: "20 October 2026" |
| `Nov 3 (final).md` | `2026-11-03-committee-meeting.md` | heading: "3 November 2026" |

## How I worked out each date

I took each date from the note's own `# Committee meeting, <date>` heading, not from the filename. Filenames are what's untidy here, and two of them leave out the year. I also checked each date against the "Next meeting …" line in the note before it. They form an unbroken chain: 11 Aug → 25 Aug → 8 Sep → 22 Sep → 6 Oct → 20 Oct → 3 Nov.

**One mismatch needs your OK:** `minutes 25 aug.md` is the note for a meeting held on **26 August**. The text says "Moved from Monday 25 August because of the storm." It was planned for the 25th and held on the 26th, so I'd name it `2026-08-26-…`. If you'd rather keep the planned date (25th), tell me.

The seven dates are all different, so no two files can end up with the same name. "(final)" in the November filename gets dropped; there's no draft version to tell it apart from.

## The index (`notes/index.md`, a new file)

It lists the notes oldest first, each as a link to its renamed file with one line on what was decided. My draft lines:

- **2026-08-11**: Odile to repaint the noticeboard by 25 Aug; shed lights to move to the night rate; Nell to ask the city about a second tap by 8 Sep.
- **2026-08-26**: Nothing new decided; the move to the night rate was confirmed done and Nell will chase the city again about the tap.
- **2026-09-08**: Replace the shed roof before winter (Tessa to get 3 quotes); Ibrahim to send fee reminders by 15 Sep.
- **2026-09-22**: Chose the $1,480 roof quote; compost order by 2 Oct; Dov takes over the second-tap request.
- **2026-10-06**: Roofer booked for 17 Oct; Wren to replace the gate latch by 20 Oct; garden closes end of November, and Tessa will draft a closing checklist.
- **2026-10-20**: Query the $80 roof overcharge before paying; work day set for Sat 14 Nov, 09:30–12:30.
- **2026-11-03**: Roof invoice stays unpaid until the $80 is explained; work-day arrangements fixed; water shut off on the work day; no more meetings this year.

## How I'll check that no text was lost

1. **Before:** record a SHA-256 checksum of every note's contents (the fingerprint changes if even one character changes), plus the file count (7).
2. **Rename:** use `mv` only, never copy-and-rewrite. If a target name already exists, it stops instead of overwriting.
3. **After:** take checksums of the renamed files and compare them with the "before" list. All 7 must match one-for-one and none may be missing. There should be 8 files in `notes/` (7 notes plus `index.md`), and no old filenames left.
4. Check that every link in `index.md` points to a file that exists.

Nothing outside `notes/` will change. `README.md` and `members.csv` stay as they are.

Let me know about the 26 August date, and I'll go ahead.