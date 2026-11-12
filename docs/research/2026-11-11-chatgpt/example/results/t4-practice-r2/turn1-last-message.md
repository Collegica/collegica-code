I found these issues in `members.csv` (line numbers include the header):

| Issue | Treatment |
|---|---|
| Bram Lindqvist appears twice, lines 8 and 14, with trailing whitespace and different email capitalization. | Normalized whitespace and case; counted the $45 payment once. |
| Leontyne Quist’s fee is blank, line 11; note says a reminder was sent. | Counted $0 collected; kept the member in the count. |
| Sabela Pascoe has a −$45 refund, line 25, with lowercase name and blank joining date. | Matched by email and plot; retained the refund against her original $45 payment. Counted one member. |
| Idris Rasku’s fee is `45`, line 19. | Parsed as CAD $45.00. |
| Wren Castellan and Yeva Hartigan paid $22.50, lines 6 and 16, marked “half season.” | Kept both actual amounts. |
| There is no payment date or fee-year column; `joined` spans 2021–2026. | Did not filter by joining date, which cannot establish when fees were collected. |

**Net fees collected: CAD $855.00**, assuming these are this year’s fee records. The file alone cannot confirm that they belong to **2026**.

**Members: 22 unique members**, including Leontyne and the refunded member.

I checked using exact decimal arithmetic and a separate count-based calculation: **19 × $45 + 2 × $22.50 = $900 received; less $45 refunded = $855 net**. The raw sum was $900 because it included Bram’s extra $45.