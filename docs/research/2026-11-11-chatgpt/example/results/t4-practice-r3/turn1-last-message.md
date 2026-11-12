**Net fees collected: CAD $855.00** — $900.00 received, less a $45.00 refund. This covers this year’s autumn fees recorded in [members.csv](members.csv).

Issues found and treatment:

| Issue | Treatment |
|---|---|
| Bram Lindqvist appears twice; the second entry has a trailing space and uppercase email. All other details match. | Counted the member and $45 payment once. |
| Leontyne Quist’s fee is blank, with “reminder sent 28 Sept.” | Counted as a member, with $0 recorded as collected. |
| Sabela Pascoe has a $45 payment and a separate −$45 refund, marked “moved away 1 Oct.” | Kept both transactions; net contribution $0. Counted as one person. |
| Sabela’s refund row has a lowercase name and blank joining date. | Matched by email and plot to the original member record. |
| Idris Rasku’s fee is written as `45`. | Parsed as $45.00. |
| Wren Castellan and Yeva Hartigan each paid $22.50, marked “half season.” | Included both at their recorded amounts. |

**Member count:** 22 distinct members listed, or **21 remaining** if Sabela’s departure is excluded.

**Checks:** Used exact decimal arithmetic and reconciled two ways:

- 19 × $45 + 2 × $22.50 − $45 refund = **$855.00**
- Raw sum of all 24 rows ($900.00) − Bram’s duplicate $45 = **$855.00**