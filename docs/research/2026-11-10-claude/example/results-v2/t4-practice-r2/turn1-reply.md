**Total net fees collected this year: $855.00 CAD**, from **22 members** on the list. 21 of them paid and 1 hasn't. One member was later refunded. That leaves 21 members if you don't count the person who moved away.

One limit on that figure: the README says `members.csv` holds this year's **autumn** fees only. If there was a spring fee, it isn't in this file, so $855.00 covers autumn only.

## Problems in members.csv and how I handled each

| # | Issue | Row | How I treated it |
|---|---|---|---|
| 1 | **Duplicate**: `Bram Lindqvist ` has a trailing space and an all-caps email, but the same plot (7) and join date as the earlier row | line 14 | Removed. Counted Bram's $45.00 once. |
| 2 | **Blank fee**: Leontyne Quist (plot 10), note says "reminder sent 28 Sept" | line 11 | Counted as unpaid ($0). She's a member, so she's in the count of 22, but not among those who paid. |
| 3 | **Refund**: `sabela pascoe` (lowercase, no join date) −45.00, "refund: moved away 1 Oct" | line 25 | This isn't a second member, it's a refund for plot 20. I subtracted it, so her net is $0. |
| 4 | **Odd format**: Idris Rasku `45` instead of `45.00` | line 19 | Same amount, counted as $45.00. |
| 5 | **Half-season fees**: Wren Castellan and Yeva Hartigan paid 22.50 | lines 6, 16 | Correct according to the README ($22.50 for half a season). Counted as is. |

A naive sum of the column also gives **$900.00**, but only by luck. The duplicate (+$45) and the refund (−$45) cancel each other out. The correct gross is also $900, but the net is $855.

## How I checked the total

1. **Script**: I parsed the CSV, matched people by email (trimmed and lowercased) to drop the duplicate, skipped the blank, and kept the refund separate. Result: 22 unique members, 21 paid, gross $900.00, refunds −$45.00, net $855.00.
2. **By hand from a count of each value**: there are 19 rows of `45.00` and 1 of `45`, so 20 × $45 = $900. Taking off Bram's duplicate leaves 19 × $45 = $855. Adding 2 × $22.50 = $45 gives a gross of $900.00. Subtracting the $45.00 refund gives a net of **$855.00**. Both methods agree.

The data has one oddity I didn't change. The Sept 8 minutes say "about a third" of members hadn't paid, and the Oct 6 minutes say eleven paid after the reminders. The CSV now shows only Leontyne as unpaid, which fits everyone else having paid since then.