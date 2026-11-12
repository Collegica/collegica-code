All seven notes have been renamed and `notes/index.md` has been written. The checks show no text was changed or lost.

**What I checked:**
1. **Each note is unchanged.** Before renaming, I saved a SHA-256 checksum of each file. Afterwards I checked every renamed file against the checksum of the specific old file it came from, and all seven match. The notes total 4,815 bytes before and after.
2. **The folder holds only what it should.** `notes/` now has exactly the seven `YYYY-MM-DD-committee-meeting.md` files plus `index.md`. No old filenames or extra files are left.
3. **Each name matches its meeting date.** The date in every new filename agrees with the date in that note's heading.
4. **The index links work.** All seven links in `index.md` point to files that exist, in date order.
5. **Nothing outside `notes/` changed.** `README.md` and `members.csv` are as they were. The only new things are `index.md` and a `check/` folder holding the checksum records, which sits one level above the garden folder. You can delete `check/` whenever you like.

You didn't answer about the 25/26 August note, so I used the meeting's actual date: `minutes 25 aug.md` is now `2026-08-26-committee-meeting.md`. The index line for it says the meeting was moved from 25 August because of the storm. The index wording is as I outlined in the plan.