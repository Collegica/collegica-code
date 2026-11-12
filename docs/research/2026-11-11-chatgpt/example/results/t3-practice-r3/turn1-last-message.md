No files have been changed.

I’ll use the meeting date in each note’s heading, including the year, to make these renames within `notes/`:

| Current name | New name |
|---|---|
| `aug11.md` | `2026-08-11-committee-meeting.md` |
| `minutes 25 aug.md` | `2026-08-26-committee-meeting.md` |
| `Meeting sept 8.md` | `2026-09-08-committee-meeting.md` |
| `notes_2026-09-22.md` | `2026-09-22-committee-meeting.md` |
| `oct6 meeting notes.md` | `2026-10-06-committee-meeting.md` |
| `2026.10.20 minutes.md` | `2026-10-20-committee-meeting.md` |
| `Nov 3 (final).md` | `2026-11-03-committee-meeting.md` |

The August filename conflicts with its contents: the heading says **26 August 2026**, and the note explicitly says the meeting moved from 25 August because of the storm. I’ll therefore use **26 August**, preserving that explanation exactly.

I’ll create `notes/index.md` with chronological links and one concise decision/action summary per note:

- **11 August:** Repaint the noticeboard, switch electricity rates, and ask the city about a second tap.
- **26 August:** Retry contacting the city about the second tap.
- **8 September:** Replace the shed roof, obtain three quotes, and send fee reminders.
- **22 September:** Choose the $1,480 roof quote, order compost, reschedule fee reminders, and hand the tap enquiry to Dov.
- **6 October:** Replace the gate latch and draft the winter closing checklist with water shut-off included.
- **20 October:** Query the roof invoice’s extra $80 before payment and arrange the November work day.
- **3 November:** Collect checklist comments, withhold roof payment pending clarification, and assign work-day notices and water shut-off.

Before renaming, I’ll record each original file’s SHA-256 hash and byte count. Afterwards, I’ll verify that every renamed file matches its original exactly, all seven notes remain, every index link resolves, and the only changes are the seven renames and the new index.