No files have been changed.

I’ll use the meeting date in each note’s heading, rather than its filename or “next meeting” date:

| Current filename | Proposed filename |
|---|---|
| `aug11.md` | `2026-08-11-committee-meeting.md` |
| `minutes 25 aug.md` | `2026-08-26-committee-meeting.md` |
| `Meeting sept 8.md` | `2026-09-08-committee-meeting.md` |
| `notes_2026-09-22.md` | `2026-09-22-committee-meeting.md` |
| `oct6 meeting notes.md` | `2026-10-06-committee-meeting.md` |
| `2026.10.20 minutes.md` | `2026-10-20-committee-meeting.md` |
| `Nov 3 (final).md` | `2026-11-03-committee-meeting.md` |

The August filename is misleading: its heading says **26 August 2026**, and the text explicitly says the meeting moved from 25 August. I’ll preserve that text exactly.

I’ll create `notes/index.md` in chronological order, with one linked line per note summarizing recorded decisions or agreed actions. For 26 August, which records no new decision, the line will describe the agreement to retry contacting the city.

To verify preservation, I’ll record each original file’s SHA-256 hash and byte count before renaming, then compare both against its renamed counterpart. I’ll also check that all seven notes remain, every index link resolves, and only the seven renames and new index were introduced.

I’ll stop here until you instruct me to proceed.