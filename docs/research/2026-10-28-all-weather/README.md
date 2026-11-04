# All Weather, rebuilt for Canada — plan and research

Plan and notes for a Finance article on the All-Weather portfolio for a
Canadian investor in 2026, from first principles rather than the 2014 retail
recipe. Started 2026-10-28. Draft: `website/finance/all-weather/index.md`
(`draft: true` until reviewed).

## What was verified, and how

| Topic | Notes | Checked against |
|---|---|---|
| Origin, the retail recipe, track record, the five popular claims | [`notes/origins-and-evidence.md`](notes/origins-and-evidence.md) | Bridgewater papers and 4Q09 deck, Asness et al., Anderson et al., Man Group, AQR, Fortune |
| First principles; what is new in 2026 (ALLW, rates, RRBs, return stacking, trend, Dalio's view) | [`notes/first-principles-2026.md`](notes/first-principles-2026.md) | Bridgewater 2011 and 2015, Qian 2005, AQR 2026, SSGA ALLW snapshot, Fed H.15, Bank of Canada, StatCan, Finance Canada |
| Canadian funds per sleeve, tax placement, currency, published versions | [`notes/canadian-implementation.md`](notes/canadian-implementation.md) | Issuer factsheets (Sep 2026), BlackRock withholding guide, CRA, Bank of Canada FX |
| Backtests in CAD; equal-risk portfolio without hindsight; four seasons in Canadian data | [`backtest/`](backtest/) — `backtest.py`, `results.md`, `monthly.csv` | Yahoo Finance prices (downloaded 2026-10-28), Bank of Canada Valet CPI V41690973, FRED NGDPRSAXDCCAQ |

## Decisions

1. **Principles first, recipe second.** The user's outline is the Robbins
   2014 mix; the article states it, then tests it and rebuilds it.
2. **Everything in Canadian dollars.** The currency effect (US recipe +25.7%
   in 2008 for a Canadian) is a finding, not a footnote.
3. **The equal-risk portfolio uses only past data** (36-month lookback,
   re-solved each January), so it is not a hindsight optimisation. Its
   result is presented as one period's demonstration.
4. **XLB stands in for long federal bonds** in the 2007 backtest because ZFL
   starts in 2010; the article says XLB holds provincials and corporates.
5. **No 2008 figure for Bridgewater's fund** (only weak sources); 2022's −22%
   is from Bloomberg via Fortune.
6. **The "15 streams cut 80%" claim** is attributed to Dalio and corrected
   to ~74% at zero correlation.

## Open

- ZCOM's MER and assets are not yet published; the fund is a year old.
- Gold's 2024–25 annual returns and the 2026 commodity index gain are from
  secondary sources (snippets).
- Questrade's current ETF sell commission: sources conflict; not used.

## Hero

`hero-original.png` here; GPT Image 2 via HiggsField (`gpt_image_2`, 16:9,
2k, high; job `cbc459f4-2d91-48e2-bae5-86c4e9ca01c2`, 2026-10-28), the house
prompt with eyebrow `INVESTING`, title 'All Weather,' / 'Rebuilt for' /
'Canada' ('Canada' amber italic), subtitle 'First principles, tested on
twenty years.', and a paper-craft cabin under a navy-and-amber umbrella with
the four seasons around it. Mark fix: 36 × 36 paper patch from (168, 285)
pasted at (168, 204). Banner: rows 60–1404 → 1774 × 887, plus 900 wide.
