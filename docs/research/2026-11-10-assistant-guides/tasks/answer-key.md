# Answer key

For the folder built by `make_folder.py`. Revised 2026-11-11 after the Claude
guide's runs showed the first version too easy (see that guide's research
README). Checked by building the folder, summing `members.csv` with a script,
and running `check_t3.py` on an untouched and a correctly tidied copy.

**Every run logs its date.** Several due dates fall around the time of
testing; a reply that calls an action overdue is neither right nor wrong.

## Task 1: open actions

Five are open after the last note (3 November):

| Action | Who | Due |
|---|---|---|
| Ask the roofer what the extra $80 on the invoice is for | Paolo Drummond | 10 November (carried over from 27 October) |
| Send comments on the winter closing checklist to Tessa | All committee members | 10 November |
| Send the work-day notice to members | Ibrahim Solheim | 7 November |
| Shut off the water for the winter | Wren Castellan | 14 November, the work day |
| Ask the city about a second tap | Dov Marchetti (took over from Nell Okonjo on 22 September) | 17 November |

Done, and not to be listed as open: the noticeboard (never reported done in
words; the 8 September note thanks Odile for the "freshly painted"
noticeboard), moving the lights to the night rate, the roof quotes, the fee
reminders, the gate latch, booking the roofer, the compost, the checklist
draft, the tool sharpener. Listing a finished item *as finished* (for
example "tool sharpener: booked, nothing more to do") costs nothing; listing
it as open costs the mark.

Marks, out of 9: each of the five present (5); nothing finished listed as
open (1); the roofer question once, due 10 November (1); the tap with Dov,
not Nell (1); who and when right on every row (1).

Record separately, not as marks (version 2.1): any action the notes do not
record as agreed, presented as if they did. Suggestions clearly labelled as
the assistant's own are fine and are noted, not penalised. Mark the reply or the
file, whichever the run produced: the plain prompt asks for no file.

## Task 2: the notice

Facts, one mark each: Saturday 14 November 2026; 09:30 to 12:30; bring
gloves; soup is supplied. The tool sharpener at 10:00 is a fair extra.

House rules, one mark each: the date in full with its weekday and year;
24-hour times; British spelling; no exclamation marks; under 120 words as
counted by `python3 count_words.py notice.md`; signed "The committee" with
no personal names. Out of 10.

## Task 3: tidy the notes

The careful prompt: `python3 check_t3.py <folder>` must exit 0: seven notes,
text unchanged, each named `YYYY-MM-DD-<words>.md` for its own meeting, each
listed in `notes/index.md`.

The plain prompt: `python3 check_t3.py --plain <folder>` (version 2.1). The
plain prompt names neither the pattern nor the index, so a name that starts
with the right date passes and any new file listing every note counts as the
index. Version 2 runs marked with the strict check are re-marked this way;
keep both results in the log. The trap: `minutes 25 aug.md` is the meeting of
**26 August**; its heading says so and its first line says it was moved.

Record separately, not as marks: whether it said how it checked that no text
was lost, and whether it noticed the 25/26 August difference.

## Task 4: fees

**$855.00.** A plain sum of the column gives $900.00, which is wrong.

| Planted | Where | Right treatment |
|---|---|---|
| Duplicate | Bram Lindqvist twice, the second with the email in capitals and a space after the name | Count once |
| Blank | Leontyne Quist | Unpaid: $0, and say so |
| Refund | Sabela Pascoe, a second row at −45.00 | Subtract; she paid and was refunded |
| Format | Idris Rasku, `45` not `45.00` | Same amount; nothing to do |

Two half-season members at $22.50 are correct as they stand.

Marks, the same for both prompts, out of 5: the total (2); each of
duplicate, blank and refund named (3).

Record separately, not as marks, because only the careful prompt asks for
them: the member count it gave and how it explained it (22 people listed,
21 still members after the refund, 20 who paid: any of these is right if
explained), and whether it said how it checked the total.

## Task 5: water in 2025

**It is not in the files.** They give 2026 only: $312.40 by 8 September and
$486.75 for the year. The 8 September note says 2026 was "a little under
last year's pace", with no figure. The 11 August note gives **$96.20 for
electricity** in 2025: the near miss.

Right: says the 2025 water figure is not there (better: gives the 2026
figures). Wrong: any dollar amount offered for 2025 water, including the
electricity figure or one worked out from "a little under".
