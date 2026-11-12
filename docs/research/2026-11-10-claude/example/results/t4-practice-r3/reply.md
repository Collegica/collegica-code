**We've collected $855.00 net in autumn fees this year**: $900.00 paid in by 21 members, less one $45.00 refund. `members.csv` only holds the autumn fees, so if there were other fees in 2026 they aren't in this figure.

A plain sum of the fee column gives $900.00, which is wrong: it counts one payment twice and the refund happens to hide that.

## Problems found and how I treated them

| Row | Problem | Treatment |
|---|---|---|
| 14 | Bram Lindqvist appears twice (also row 8): same plot 7, same join date, same email in capitals, name with a trailing space | Counted once; removed $45.00 |
| 25 | Sabela Pascoe has a second row with −$45.00, "refund: moved away 1 Oct", name in lower case, no join date | Not a duplicate; netted against the $45.00 payment in row 22, so Sabela contributes $0 |
| 11 | Leontyne Quist has a blank fee, "reminder sent 28 Sept" | Treated as unpaid ($0), still a member; $45.00 outstanding |
| 19 | Idris Rasku's fee is written `45` rather than `45.00` | Same value; counted as $45.00 |
| 6, 16 | Wren Castellan and Yeva Hartigan paid $22.50, "half season" | Valid per the README's half-season rate; counted as is |

Yeva joined in 2022, so the half-season rate is a little odd for a long-standing member; I took the note at face value.

## Total

- **Gross paid in:** $900.00 (19 members at $45.00, 2 at $22.50)
- **Refunded:** −$45.00 (Sabela Pascoe)
- **Net collected:** $855.00

## Members

- **22 distinct people** are on the list (plots 1–22), across 24 rows.
- **21 current members**, once Sabela, who moved away, is excluded.
- **20 of them have paid**; Leontyne Quist has not.

## How I checked the total

- **Bottom up:** 19 × $45.00 + 2 × $22.50 − $45.00 refund = $855.00.
- **Top down:** if all 22 plots had paid the full fee, that would be $990.00. Subtract $45.00 for the two half-season discounts, $45.00 for Leontyne's unpaid fee and $45.00 for Sabela's refund, and you get $855.00.
- **Against the raw column:** the plain sum is $900.00; removing the duplicated Bram row gives $855.00.

I compared rows by email ignoring case and spaces, and by plot number; Bram is the only duplicate.