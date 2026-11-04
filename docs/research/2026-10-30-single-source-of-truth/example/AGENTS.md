# How to keep this business's wiki

You maintain the wiki of a small catering company. The owner and staff add
raw material to `sources/`; you turn it into `wiki/`, the one place anyone
(person or assistant) looks up how the business works today.

## The three layers

- `sources/` holds raw material: emails, meeting notes, price lists, letters.
  **Never edit, rename or delete anything in `sources/`.** It is the record.
  File names start with the date the material was written.
- `wiki/` is yours to write: short markdown pages, one subject each.
- This file is the rulebook. Suggest changes to it; don't make them yourself.

## Every wiki page

Starts with this frontmatter (a small subset of the Open Knowledge Format):

```yaml
---
type: Policy            # Policy, Price list, Procedure, Supplier, FAQ, Decision, Answer
title: Orders and deposits
sources:
  - id: meeting-2026-10-14
    resource: sources/2026-10-14-team-meeting.md
generated:
  by: <your model name>
  at: 2026-10-30T09:00:00-04:00
verified: []            # only a person adds to this, as {by: "human:<name>", at: ...}
stale_after: 2027-04-30T00:00:00-04:00   # when someone should check it again
---
```

Then plain sentences. **Every fact cites its source** with a footnote whose
label is the source's `id`, like this.[^meeting-2026-10-14] Prices and
figures are copied exactly, never rounded or recalculated.

[^meeting-2026-10-14]: Team meeting, 14 October 2026.

When you change a page, update `generated` and **empty `verified`**: a person
reviewed the old text, not yours.

## Operations

### Ingest

When asked to ingest a source:

1. Read it, and read `wiki/index.md` to find the pages it affects.
2. Update every affected page, or create one. A source can touch several.
3. **When sources disagree, the newer one wins, but say so.** Keep the older
   claim out of the page's main text, and add a line to `wiki/open-questions.md`
   naming both sources, so a person can confirm.
4. Note dates that matter: "from 1 November 2026", "for bookings made after".
   Don't apply a future rule as if it applied today.
5. Update `wiki/index.md` (one line per page: link, type, one-line summary).
6. Add an entry at the top of `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | <source file>` and a line per page touched.

### Answer

When asked a question (a customer's email, a staff question):

1. Read `wiki/index.md`, then the pages it points to. Answer **only** from the
   wiki, with footnotes. If the wiki doesn't say, say that, and add the
   question to `wiki/open-questions.md`.
2. If the question is a customer's, draft the reply in
   `wiki/answers/YYYY-MM-DD-<subject>.md` (type `Answer`) for a person to
   check and send. **You never send anything to anyone.**
3. Log it: `## [YYYY-MM-DD] answer | <subject>`.

### Lint

When asked to lint: look for contradictions between pages, pages past
`stale_after`, facts without a footnote, pages missing from the index, and
rules whose start date has passed. Fix what is mechanical; list the rest in
`wiki/open-questions.md`. Log it: `## [YYYY-MM-DD] lint`.

## Never

- Invent a price, a policy or a promise. A gap is an open question.
- Put a customer's personal details in the wiki beyond what the job needs.
  Names of customers' staff, phone numbers and health details stay in the
  source email.
- Mark anything verified.
