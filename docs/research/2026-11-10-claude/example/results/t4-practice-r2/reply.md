**Net autumn fees collected this year: $855.00 CAD, from 20 paying members out of 22 on the list.**

A plain sum of the fee column gives $900.00, which is wrong because it counts one member twice.

## What I found in `members.csv`

| Row | Issue | Treatment |
|---|---|---|
| Bram Lindqvist (plot 7), listed twice | The second row has a trailing space in the name and the email in capitals; plot, join date and amount are identical. | Treated as a duplicate entry and counted once (−$45.00). |
| Sabela Pascoe (plot 20), second row | A −$45.00 row in lowercase with no join date, noted "refund: moved away 1 Oct". | Treated as a refund of her payment, not a separate member; her net is $0.00. |
| Leontyne Quist (plot 10) | The fee is blank, noted "reminder sent 28 Sept". | Counted as unpaid ($0.00), still counted as a member. |
| Wren Castellan, Yeva Hartigan | Each paid $22.50, noted "half season". | Kept as is; the README confirms this is the half-season rate. |
| Idris Rasku | The fee is written `45` instead of `45.00`. | Same value, counted as $45.00. |

The Bram row is the one judgement call: I can't tell from the file whether he was entered twice or actually paid twice. If he paid twice, you collected $900.00 and owe him $45.00 back, so check it against the bank record.

## Members

- **22** unique members on the list (24 rows, minus the Bram duplicate and the Sabela refund row).
- **21** current members if you exclude Sabela, who moved away.
- **20** have a net payment: 18 at the full fee and 2 at the half-season fee.
- **1** is outstanding: Leontyne Quist, $45.00, assuming she owes the full fee.

## How I checked the total

- **By rate:** 18 × $45.00 + 2 × $22.50 = $810.00 + $45.00 = **$855.00**.
- **From the raw sum:** $900.00 − $45.00 for the Bram duplicate = **$855.00**; the Sabela refund is already netted in the raw sum.
- **By script:** grouping rows by lowercased email and dropping the exact duplicate gave 22 members, 20 paying, net $855.00.

The file only holds this year's autumn fees, so $855.00 covers those alone; any other fees taken this year aren't in it. If you want gross receipts instead of net, that is $900.00 received and $45.00 refunded.