# Your Network Is Already in Your Inbox

Article of 2026-10-31 (`website/ai/contacts-network/`). Owner's brief:
export your Gmail, Yahoo, Apple, Facebook and LinkedIn data, build a
contacts database, enrich and maintain it, and use it for business
outreach. The research added the legal frame (CASL consent; PIPEDA once
contacts are used for business; platform terms and regulators' scraping
statements), which shapes the article's second half.

- `notes/exports-and-rules.md`: each platform's export (official help
  pages, 2026-10-31; several details behind sign-in or unstated, marked
  unverified), platform terms, CASL and PIPEDA as they apply, scraping
  statements. CRTC pages returned 403; the social-media analysis rests on
  the statute and regulations.
- `test/`: everything to rerun the test. **All people, companies, addresses
  and phone numbers are fictional** (example.com/.org/.net, 555-01xx).
  - `make_exports.py` writes `exports/` in each service's format (modelled
    on the documented formats; exact column names unverified for some).
  - `PROMPT.txt` (build) and `PROMPT2.txt` (update), given to Claude Code
    headless with an allow list (file tools, python3, sqlite3, ls/head/wc).
  - `ANSWER-KEY.md`, written before the runs and not shown to the assistant.
  - `build_contacts.py`, `selftest.py`, `assistant-README.md`: what the
    assistant wrote (as after the update run).
  - `exports/2026-10-31-update/`: the newer LinkedIn and Gmail files for the
    update run.

## Results

Build: 9.4 min, US$2.56, 36 turns. 71 source records → 27 people, 25
after two flagged merges (Ella/"Ella Mac"; LinkedIn Grace Li with a new
employer). CASL statuses all match the answer key; it also flagged an
invoice numbered 2024 but dated 2025 (an inconsistency in our data).

Update (fresh session): 3.1 min, US$1.43, 34 turns. Backup first; kept the
owner's note and consent record (applying the latter); merged Grace on the
new email evidence; new connection; job change; Victor's consent renewed by
a new quote request; noticed the partial LinkedIn export; fixed its own
source-ordering bug.

## Hero

`hero-original.png`; GPT Image 2 via HiggsField (`gpt_image_2`, 16:9, 2k,
high; job `cf4a766b-b385-4247-b039-92eb7b3ad9be`), house prompt with eyebrow
`AI`, title 'Your Network' / 'Is Already in' / 'Your Inbox', subtitle
'Export, merge, keep it current, reach out the right way.' Mark fix: 40 × 40
paper patch from (229, 233) pasted at (182, 233). Banner: rows 60–1404 →
1774 × 887, plus 900 wide.
