No files have been changed.

I would use the meeting date in each note’s heading, including the year, to make these renames within `notes/`:

| Current filename | New filename |
|---|---|
| `aug11.md` | `2026-08-11-committee-meeting.md` |
| `minutes 25 aug.md` | `2026-08-26-committee-meeting.md` |
| `Meeting sept 8.md` | `2026-09-08-committee-meeting.md` |
| `notes_2026-09-22.md` | `2026-09-22-committee-meeting.md` |
| `oct6 meeting notes.md` | `2026-10-06-committee-meeting.md` |
| `2026.10.20 minutes.md` | `2026-10-20-committee-meeting.md` |
| `Nov 3 (final).md` | `2026-11-03-committee-meeting.md` |

The August filename is misleading: its heading says **26 August 2026**, and its text confirms the meeting moved from 25 August because of the storm. I would preserve that text exactly, including the weekday wording.

I would create `notes/index.md` with chronological links and these one-line summaries:

- **11 August:** Odile to repaint the noticeboard; Paolo to change electricity rates; Nell to ask about a second tap.
- **26 August:** Nell to retry contacting the city about the second tap.
- **8 September:** Replace the shed roof; Tessa to obtain three quotes and Ibrahim to send fee reminders.
- **22 September:** Choose the $1,480 roof quote, order four cubic metres of compost, and transfer the tap enquiry to Dov.
- **6 October:** Wren to replace the gate latch; Tessa to draft the winter closing checklist with water shut-off included.
- **20 October:** Query the roof invoice’s extra $80 before payment and set the work day for 14 November.
- **3 November:** Collect checklist comments, withhold roof payment pending clarification, and arrange work-day notice and winter water shut-off.

To verify preservation, I would record each original note’s SHA-256 hash and byte count before renaming, then compare them against its mapped destination afterwards. I would also check that all seven notes remain, every index link resolves, and the only additional file is `notes/index.md`. Matching hashes would confirm that every note’s contents—including whitespace and line endings—remained unchanged.