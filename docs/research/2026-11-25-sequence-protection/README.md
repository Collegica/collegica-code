# Does a cash buffer protect you from a crash?

Notes behind `website/finance/sequence-protection/index.md` (finance series
item 5).

- `scripts/replay.py` prints every figure in the article;
  `scripts/output.txt` is its output. Run
  `python3 replay.py <data-folder> [chart.svg]`. First download the three
  Statistics Canada tables and unzip their CSVs into the folder:
  <https://www150.statcan.gc.ca/n1/tbl/csv/10100125-eng.zip>,
  <https://www150.statcan.gc.ca/n1/tbl/csv/10100139-eng.zip> and
  <https://www150.statcan.gc.ca/n1/tbl/csv/18100004-eng.zip>. The raw tables
  are not committed. The chart is
  `website/static/img/finance/sequence-2008.svg`.
- Data retrieved 2026-11-25. Table 10-10-0125: composite close to 2023-09,
  dividend yield to 2016-08 (the 2012-2016 readings are about 3%).

## Findings

- A buffer raised the early low and, in most cases tried, lowered the final
  value. Half a year of cash changed little.
- Spending cash only in downturns ended close to holding the same share fixed.
- Exceptions: with the invested part all in stocks, a two-year downturn buffer
  ended slightly ahead for the 2008 start; cash spent first and not refilled
  ended ahead for the 2000 and 2008 starts and in 50 of 165 ten-year windows.

## Checks and limits

- Yearly returns built by the script: TSX -32.9% (2008), 5.3% (2020), -5.9%
  (2022). A web search found a secondary, unofficial table
  (wealthnorth.ca) giving -33.0%, +5.6% and -5.8%; no 2009 figure was found,
  and no primary index source was read.
- The bond series is an approximation (yield carry less 8 x yield change).
- No tax, fees or public pensions; one country, 2000-2023.
- `website/aging-well/ai-planning/index.md` and its slides called three to
  six months of cash "sequence protection". This replay does not support that
  for six months (three was not run), so both now call it emergency cash.
