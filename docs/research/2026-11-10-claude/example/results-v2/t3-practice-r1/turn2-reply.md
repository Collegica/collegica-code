The notes folder is tidied as planned: all seven notes are renamed by meeting date, `notes/index.md` exists, and the text of every note is unchanged.

**What I checked:**

1. **No text changed.** Before renaming, I recorded a checksum (a fingerprint of the exact contents) of all seven notes. Afterwards each renamed note matched the fingerprint of its original exactly, so not a single byte changed.
2. **Nothing was overwritten.** Each rename first checked that the new name wasn't already taken.
3. **The folder contains only what it should.** `notes/` now holds the seven dated notes plus `index.md` (8 files). No files are missing and there are no extras.
4. **Each new name matches the note's own date.** I compared every filename with the date in the note's first line, and all seven agree. That includes the meeting moved for the storm: it is saved as `2026-08-26-committee-meeting.md`, the day it was actually held, not the 25th from the old filename.
5. **The index links work.** All seven links in `index.md` point to notes that exist.

Nothing else in the folder was changed. `README.md` and `members.csv` are as they were. The fingerprint list I made for the comparison was saved outside the folder and deleted after the check.