**Net fees collected this year: $855.00 CAD**, from 22 members. A plain sum of the column also gives $900.00, but that's a coincidence: two errors cancel out. $900 is the gross amount before the refund, not the right answer for the wrong reason.

## Problems in members.csv and how I treated them

| # | Issue | Row(s) | Treatment |
|---|---|---|---|
| 1 | **Duplicate**: Bram Lindqvist appears twice. The second row has a trailing space in the name and the email in all capitals, but the same plot (7), join date and $45. | Lines 8 and 14 | Counted once. I took this as a double entry, not a second payment. |
| 2 | **Refund**: a second Sabela Pascoe row (name in lowercase, no join date) shows **−$45.00**, "refund: moved away 1 Oct". | Line 25 | Kept as a negative. Her $45 was paid and then refunded, so she nets $0. |
| 3 | **Blank fee**: Leontyne Quist (plot 10) has no amount, with the note "reminder sent 28 Sept". | Line 11 | Counted as $0, meaning unpaid and still outstanding. I didn't treat it as missing data. |
| 4 | **Odd format**: Idris Rasku's fee is `45` rather than `45.00`. | Line 19 | Same value, so counted as $45.00. |
| 5 | **Half-season fees**: Wren Castellan and Yeva Hartigan paid $22.50. | Lines 6 and 16 | Kept as is. The README says $22.50 is the correct half-season fee. |

I also checked that "this year" doesn't mean filtering by the `joined` column. The README says the file lists *this year's* autumn fees, so members who joined in 2021 still paid in 2026.

## Numbers

- **Total collected, after the refund: $855.00.** If you want the gross amount before the refund, it's $900.00.
- **Members:** 22 people hold plots 1–22, one plot each.
  - 20 have paid and kept their membership: 18 paid in full and 2 paid half.
  - 1 hasn't paid: Leontyne Quist.
  - 1 left and was refunded: Sabela Pascoe. That leaves **21 current members**.

## How I checked

1. **Script:** I parsed the CSV and matched people by email after trimming spaces and ignoring case. Repeat positive payments were skipped and refunds were kept. Result: $855.00 across 22 unique people.
2. **Count by plot:** I grouped the rows by plot number, which avoids relying on the messy names. Every plot from 1 to 22 has one entry, except plot 7 (the duplicate) and plot 20 (payment plus refund). Adding it up by hand: 18 × $45 = $810, plus 2 × $22.50 = $45, gives **$855**. That matches the script.
3. **Against the minutes:** they're consistent. On 8 Sept about a third of members hadn't paid. Reminders went out on 28 Sept and 11 members paid after that. Leontyne's reminder note fits with her being the one still unpaid.

You may want to chase Leontyne's $45 and delete the duplicate Bram row so the file adds up correctly in future.