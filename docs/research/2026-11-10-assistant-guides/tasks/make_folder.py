"""Build the made-up folder every assistant is tested on.

    python3 make_folder.py <target-dir>

Writes a small community garden club's files: seven committee meeting notes
with untidy names (one whose file name gives the wrong day), and a members
list with four planted problems. Everything
is invented; the output is the same on every run, so a fresh copy can be made
for each test and compared afterwards with check_t3.py.
"""

import sys
from pathlib import Path

NOTES = {
    "aug11.md": """# Committee meeting, 11 August 2026

Present: Tessa Varga, Ibrahim Solheim, Nell Okonjo, Paolo Drummond, Wren Castellan.

Noticeboard: the paint is peeling and the notices blow away. Odile
Fairweather has offered to repaint it. She will do it by 25 August.

Electricity: the bill for the shed lights for 2025 was $96.20 for the whole
year. Paolo will move us to the cheaper night rate.

Water: members keep asking for a second tap at the far end of the plots.
Nell will ask the city whether we may add one, by 8 September.

Next meeting 25 August.
""",
    "minutes 25 aug.md": """# Committee meeting, 26 August 2026

Moved from Monday 25 August because of the storm.

Present: Tessa Varga, Nell Okonjo, Paolo Drummond, Wren Castellan.
Apologies: Ibrahim Solheim.

Paolo has moved the shed lights to the night rate.

Nell has not yet reached the city about the second tap. She will try again
before the next meeting.

Seed swap: held on 23 August; about thirty members came.

Next meeting 8 September.
""",
    "Meeting sept 8.md": """# Committee meeting, 8 September 2026

Present: Tessa Varga, Ibrahim Solheim, Nell Okonjo, Paolo Drummond, Wren Castellan.

The shed roof leaked again in last week's rain. We agreed it needs replacing
before winter rather than another patch. Tessa will get three quotes for the
roof and bring them to the next meeting on 22 September.

Fees: about a third of members have not paid for the autumn season. Ibrahim
will email a reminder to everyone by 15 September.

The latch on the main gate is broken and the gate swings open in wind.
Somebody needs to fix it. Nobody had time this month.

Water: the bill for 2026 so far is $312.40, a little under last year's pace
according to Paolo, who did not have last year's figure with him.

Thanks to Odile for the freshly painted noticeboard, which members say is
much easier to read.

Second tap: Nell is still waiting to hear from the city.

Next meeting 22 September.
""",
    "notes_2026-09-22.md": """# Committee meeting, 22 September 2026

Present: Tessa Varga, Ibrahim Solheim, Nell Okonjo, Paolo Drummond.
Apologies: Wren Castellan.

Roof: Tessa brought three quotes, $1,250, $1,480 and $1,900. We chose the
middle one because it includes taking the old roofing away. Paolo will book
the roofer, and wants it done before the 6 October meeting.

Fee reminders have not gone out yet. Ibrahim was away and will send them by
29 September instead.

Compost: the bays are nearly empty. Nell will order four cubic metres by
2 October so it arrives before the beds are put to sleep.

Gate latch: still broken. Not discussed further.

Second tap: Nell has too much on with the compost. Dov Marchetti, who first
asked for the tap, will take over asking the city, by 20 October.

Next meeting 6 October.
""",
    "oct6 meeting notes.md": """# Committee meeting, 6 October 2026

Present: Tessa Varga, Ibrahim Solheim, Nell Okonjo, Paolo Drummond, Wren Castellan.

Roof: Paolo has booked the roofer for 17 October.

Fees: Ibrahim sent the reminders on 28 September and eleven members have
paid since.

Gate latch: still broken. Wren volunteered to replace it and will do it by
20 October.

Winter: we close the garden at the end of November. Tessa will draft a
winter closing checklist, the same as last year's with the water shut-off
added, by 3 November.

Compost is ordered, Nell says, and due mid-month.

Next meeting 20 October.
""",
    "2026.10.20 minutes.md": """# Committee meeting, 20 October 2026

Present: Tessa Varga, Nell Okonjo, Paolo Drummond, Wren Castellan.
Apologies: Ibrahim Solheim.

Gate latch: Wren replaced it on 18 October. It closes properly now.

Compost arrived on 15 October and is in the bays.

Roof: finished on 17 October and it looks good. The invoice came in at
$1,560, which is $80 over the quote. Paolo will ask the roofer what the $80
is for, by 27 October, before we pay.

Second tap: Dov has not heard back from the city. He will chase them by
3 November.

Work day: set for Saturday 14 November, 09:30 to 12:30. Members should bring
gloves; the club supplies soup. Nell will book the tool-sharpening person so
they are there on the day.

Next meeting 3 November.
""",
    "Nov 3 (final).md": """# Committee meeting, 3 November 2026

Present: Tessa Varga, Ibrahim Solheim, Nell Okonjo, Paolo Drummond, Wren Castellan.

Checklist: Tessa circulated the draft winter closing checklist last week.
All committee members are to send her their comments by 10 November.

Roof invoice: Paolo has not heard back from the roofer about the extra $80.
He will chase them by 10 November. We do not pay until we know.

Work day, 14 November: Nell has booked the tool sharpener, who will come at
10:00. Ibrahim will send the work-day notice to all members by 7 November.
Wren will shut off the water for the winter on the work day itself.

Second tap: Dov says the city has the request but has not decided. He will
call again by 17 November.

Water: the bill for 2026 came to $486.75 in total.

No further meetings this year.
""",
}

FIRST = [
    "Tessa", "Ibrahim", "Nell", "Paolo", "Wren", "Odile", "Bram", "Sunniva",
    "Kasimir", "Leontyne", "Dov", "Marisol", "Anselm", "Yeva", "Corwin",
    "Philippa", "Idris", "Greta", "Lucan", "Sabela", "Torin", "Mireille",
]
LAST = [
    "Varga", "Solheim", "Okonjo", "Drummond", "Castellan", "Fairweather",
    "Lindqvist", "Abara", "Thorne", "Quist", "Marchetti", "Ellery", "Novak",
    "Hartigan", "Bellamy", "Osei", "Rasku", "Whitlock", "Demir", "Pascoe",
    "Ainsley", "Kovalenko",
]

HALF_SEASON = {4, 13}     # joined late, pay 22.50
UNPAID = 9                # fee left blank
NO_DECIMALS = 16          # paid, written 45 rather than 45.00
DUPLICATED = 6            # entered twice, second time with the email in capitals
REFUNDED = 19             # paid, then refunded on a separate row


def members_csv() -> str:
    rows = ["name,email,plot,joined,fee_paid_cad,note"]
    for i, (first, last) in enumerate(zip(FIRST, LAST)):
        email = f"{first}.{last}@example.com".lower()
        joined = f"20{21 + i % 6}-{1 + (i * 5) % 12:02d}-{1 + (i * 7) % 28:02d}"
        fee, note = "45.00", ""
        if i in HALF_SEASON:
            fee, note = "22.50", "half season"
        if i == UNPAID:
            fee, note = "", "reminder sent 28 Sept"
        if i == NO_DECIMALS:
            fee = "45"
        rows.append(f"{first} {last},{email},{i + 1},{joined},{fee},{note}")
        if i == 11:
            first_d, last_d = FIRST[DUPLICATED], LAST[DUPLICATED]
            rows.append(
                f"{first_d} {last_d} ,{first_d.upper()}.{last_d.upper()}@EXAMPLE.COM,"
                f"{DUPLICATED + 1},2021-07-15,45.00,"
            )
    first_r, last_r = FIRST[REFUNDED], LAST[REFUNDED]
    rows.append(
        f"{first_r} {last_r},{first_r}.{last_r}@example.com".lower()
        + f",{REFUNDED + 1},,-45.00,refund: moved away 1 Oct"
    )
    return "\n".join(rows) + "\n"


README = """# Alder Lane Community Garden

Files of the garden's committee. `notes/` holds the minutes of committee
meetings; `members.csv` is the members list with this year's autumn fees.
The autumn fee is $45.00, or $22.50 for members who joined for half a season.
"""


def build(target: Path) -> None:
    (target / "notes").mkdir(parents=True, exist_ok=True)
    (target / "README.md").write_text(README)
    (target / "members.csv").write_text(members_csv())
    for name, text in NOTES.items():
        (target / "notes" / name).write_text(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    build(Path(sys.argv[1]))
    print(f"wrote {sys.argv[1]}")
