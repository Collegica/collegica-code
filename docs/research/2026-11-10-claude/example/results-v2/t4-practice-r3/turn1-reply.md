**Net fees collected this year: $855.00 CAD.** That is $900.00 received, minus one $45.00 refund. It covers the autumn season, which is the only fee period `members.csv` records.

**Things in `members.csv` that would throw off a simple sum**

1. **Duplicate: Bram Lindqvist.** He appears twice, both times on plot 7, joined 2021-07-15, paid $45.00. The second row has a trailing space in the name and the email in capitals. I treated it as one person and counted his $45 once.
2. **Refund: Sabela Pascoe.** Her extra row ("sabela pascoe", lowercase, no join date) shows **−$45.00** with the note "refund: moved away 1 Oct". It's not a second payment. I subtracted it, so her net is $0. Her original $45 payment is still counted in the $900 received.
3. **Blank: Leontyne Quist** (plot 10). The fee is empty, with the note "reminder sent 28 Sept". I counted it as $0, meaning unpaid.
4. **Different format: Idris Rasku** has `45` instead of `45.00`. It's the same amount and I counted it as $45.00.
5. **Half-season fees: Wren Castellan and Yeva Hartigan** paid $22.50 each, noted as "half season". The README says that's the correct half-season fee, so they're valid payments at full value.

**Number of members**
- **22 people are listed**: 24 rows, minus the Bram duplicate and Sabela's refund row. That's 22 unique emails across plots 1–22.
- **21 current members** if you leave out Sabela, who moved away and was refunded.
- **20 have paid**, excluding Leontyne and Sabela.

**How I checked the total**
- **Script:** I read the file, grouped rows by email (ignoring case and spaces), set aside blanks, refunds and duplicates, and added up the rest. Result: $900.00 received, −$45.00 refunds, $855.00 net.
- **Hand count:** the fee column holds 19 × "45.00", 1 × "45", 2 × "22.50", 1 × "−45.00" and 1 blank. Without Bram's duplicate that's 19 × $45 + 2 × $22.50 = $900.00, and $900 − $45 = $855.00.

**Warning:** a simple sum of the column also comes to $900.00. It looks right, but only because Bram's duplicate $45 and Sabela's −$45 refund cancel each other out. The real figure is $855.00 net, or $900.00 if you want the amount received before the refund.