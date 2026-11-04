# The run that produced `wiki/`

On 30 October 2026, Claude Code 2.1.314 (model `claude-opus-5-5`) was given a
copy of this folder with `wiki/` holding only an empty `index.md` and
`log.md`, and three requests, one at a time, in headless mode:

```bash
claude -p "Ingest every file in sources/, oldest first." \
  --permission-mode acceptEdits --allowedTools "Read,Write,Edit,Glob,Grep,Bash(ls:*)"
claude -p "Answer the customer email in sources/2026-10-21-customer-email.txt." …
claude -p "Lint the wiki." …
```

It could read and write files in the folder and list directories; nothing
else. The folder was a git repository so each step's changes could be read
as a diff. Nothing in `wiki/` was edited by hand afterwards.

| Step | Turns | Time | API cost (US$) |
|---|---|---|---|
| Ingest five sources | 20 | 112 s | 0.74 |
| Answer the customer | 19 | 63 s | 0.63 |
| Lint | 27 | 94 s | 0.72 |

The costs are pay-as-you-go API prices for this run; on a Claude or ChatGPT
subscription the same work is covered by the monthly fee.

## What it found

The sources were written for this example by a person, with two
contradictions on purpose (the old FAQ's 15-guest minimum and 25% deposit
against the newer price list and meeting). The assistant found those, and
three that were **not** planted:

- "20 guests for every menu" from 1 November would *lower* the hot buffet
  (25) and cocktail reception (30) minimums if read literally.
- The meeting notes say butter and cream go up; the supplier's letter also
  names cheese.
- "Existing bookings are honoured" doesn't say whether a booking exists from
  the enquiry, the confirmation or the deposit, which decides whether the
  customer's 16-guest November lunch can be taken at all.

It did not apply the 1 November rules early, did not mark anything verified,
quoted prices exactly, left the totals to the quote template, and drafted
the customer reply without sending it. Its one slip, caught by its own lint:
the draft's opening line ("glad to do … your team of 16") contradicts its
option B (a 20-guest minimum).

The draft reply mentions that one guest has coeliac disease, because the
reply has to answer that; no names or contact details appear anywhere in the
wiki (the example's source email carries none either).
