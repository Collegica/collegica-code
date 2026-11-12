**Net fees collected: CAD $855.00**, for this year’s autumn fees recorded in [members.csv](members.csv). There are **22 unique members listed**, including one who moved away.

I found and treated these issues:

- **Duplicate Bram Lindqvist:** Two $45 entries match after trimming the name’s trailing space and ignoring email capitalization. Counted once.
- **Blank payment for Leontyne Quist:** Treated as no recorded collection ($0), rather than assuming the standard fee was paid.
- **Sabela Pascoe’s refund:** Kept both the $45 payment and −$45 refund. Her net contribution is $0; the refund row is not another member. Its blank joining date doesn’t affect the calculation.
- **Inconsistent capitalization:** Normalized names and emails when identifying repeated members.
- **Idris Rasku’s `45` format:** Read as $45.00.
- **Two half-season payments:** Wren Castellan and Yeva Hartigan each paid $22.50, consistent with the fee schedule in the README.

I checked using exact decimal arithmetic and two reconciliations:

- **19 × $45 + 2 × $22.50 − $45 refund = $855.00**
- Raw signed sum **$900.00 − $45 duplicate = $855.00**

Gross receipts before the refund were **$900.00**. The file covers autumn fees; it doesn’t establish whether other fees were collected earlier this year.