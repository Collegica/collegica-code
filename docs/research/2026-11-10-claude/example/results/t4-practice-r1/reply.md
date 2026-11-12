**We have collected $855.00 net in autumn fees this year, from 20 paying members.** `members.csv` only holds the autumn season, so if there were fees for other seasons in 2026, they are not in this figure.

## What would make a simple sum wrong

A plain sum of the fee column gives $900.00, which is $45 too high.

| # | What I found | How I treated it |
|---|---|---|
| 1 | **Duplicate:** Bram Lindqvist appears twice (rows 8 and 14). The second has a trailing space in the name and the email in capitals, but the same plot 7, join date and $45.00. | Counted once, which removes $45.00. I assumed it is a double entry, not a second payment. |
| 2 | **Refund:** a second Sabela Pascoe row (name in lower case, no join date) shows -$45.00, "refund: moved away 1 Oct". | Kept in the sum so it cancels her $45.00 payment, leaving her net at $0. I did not count her as a member. |
| 3 | **Blank fee:** Leontyne Quist has no amount, with the note "reminder sent 28 Sept". | Treated as unpaid, $0. She is still a member, but not a paying one. |
| 4 | **Odd format:** Idris Rasku's fee is entered as `45`, not `45.00`. | Same value, counted as $45.00. |
| 5 | **Half fees:** Wren Castellan and Yeva Hartigan paid $22.50, noted "half season". | Counted as entered; the README confirms $22.50 is the half-season fee. |

## Member count

- **Paying members:** 20 (18 at $45.00 and 2 at $22.50).
- **Current members:** 21, which adds Leontyne Quist, who has not paid.
- **Distinct people in the file:** 22, which also includes Sabela Pascoe, who was refunded and has left.

## How I checked the total

- **Built up from the fee rates:** 18 × $45.00 = $810.00, plus 2 × $22.50 = $45.00, gives $855.00.
- **Worked down from the raw sum:** the 24 rows sum to $900.00; taking off the $45.00 duplicate Bram row gives $855.00. The refund is already in the raw sum as a negative.
- **Gross versus net:** $900.00 was actually received from 21 people, and $45.00 was refunded, leaving $855.00.

All three agree. The one assumption to confirm is that Bram paid once: if he really paid twice, the money received is $900.00 net and he is owed $45.00 back.