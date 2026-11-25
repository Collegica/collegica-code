# Which account to draw from, in which year

Notes behind `website/finance/draw-order/index.md` (finance series item 3).

- `scripts/draw.py` prints every table in the article; `scripts/output.txt` is
  its output. The model's assumptions are in its docstring.
- Official figures read on Canada.ca on 2026-11-25: 2026 federal brackets;
  the RRIF prescribed factors ("all other RRIFs"); the OAS recovery threshold
  of $93,454 (2025) from the OASRI guide; CPP and OAS averages as in
  `2026-11-24-income-floor`.

## Findings

- Below the first federal bracket top ($58,523) every RRSP dollar is taxed at
  14% whenever it comes out, so the order does not change sustainable spending
  (within 0.3% in both households).
- Filling to $117,045 cost about 5% of sustainable spending and crossed the OAS
  threshold in 6 (A) and 14 (B) years.
- Leaving the RRSP for last left 3% to 14% less after tax at death than the best of the other orders.

## Not modelled / not verified

- Provincial tax, credits (including age amount phase-outs), spouse rollover.
- OAS threshold for 2026: the model uses the 2025 official figure, held real.
- The 20% tax drag on the non-registered account is an assumption.
- Constant real returns; no sequence risk.
