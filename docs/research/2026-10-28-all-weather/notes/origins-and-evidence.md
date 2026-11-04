## Access and confidence

Research date: 2026-10-28. Tools: WebSearch and WebFetch, plus curl and pdftotext for PDFs the fetcher could not read, and one small backtest of my own (method in section 5).

**Read in full (primary or near-primary):**
- Bridgewater, "The All Weather Story" (Jan 2012): https://www.bridgewater.com/research-and-insights/the-all-weather-story
- Dalio, "Engineering Targeted Returns and Risks" (Aug 2011, a reprint of a 2004 article), extracted to text: https://bridgewater.brightspotcdn.com/fa/e3/d09e72bd401a8414c5c0bdaf88bb/bridgewater-associates-engineering-targeted-returns-and-risks-aug-2011.pdf
- Bridgewater, "The All Weather Strategy 4Q09", a manager presentation filed with SDCERA (the San Diego county pension board), extracted to text. It includes net performance from June 1996 to December 2009: https://sdcera.granicus.com/MetaViewer.php?view_id=4&clip_id=75&meta_id=9141
- The State Street Bridgewater All Weather ETF (ALLW) page: https://www.ssga.com/us/en/intermediary/etfs/state-street-bridgewater-all-weather-etf-allw
- Asness, Frazzini and Pedersen, "Leverage Aversion and Risk Parity" (FAJ 2012), working-paper text: https://pages.stern.nyu.edu/~lpederse/papers/LeverageAversionRP.pdf
- Anderson, Bianchi and Goldberg, "Will My Risk Parity Strategy Outperform?" (2011; FAJ 2012): https://eml.berkeley.edu/~anderson/risk%20parity111111.pdf
- Neville, Draaisma, Funnell, Harvey and Van Hemert, "The Best Strategies for Inflationary Times" (JPM 2021): https://people.duke.edu/~charvey/Research/Published_Papers/P154_The_best_strategies.pdf
- AQR, "A Changing Stock-Bond Correlation" (2023), the summary page: https://www.aqr.com/Insights/Research/Journal-Article/A-Changing-Stock-Bond-Correlation
- Fortune/Bloomberg (Apr 2024) on All Weather's 2022 loss and outflows: https://fortune.com/2024/04/23/lackluster-returns-ray-dalio-investing-strategy-investors-pull-billions/
- Canadian Couch Potato critique (2015): https://canadiancouchpotato.com/2015/07/06/raining-on-the-all-seasons-portfolio/
- Yahoo/Business Insider excerpt of the Robbins–Dalio exchange: https://finance.yahoo.com/news/tony-robbins--ray-dalio-s--all-weather--portfolio-161619133.html

**Not accessed:**
- The book itself, *Money: Master the Game* (2014). Every Robbins and Dalio quote below comes through the Business Insider excerpt or other secondary pages.
- Portfolio Visualizer and PortfoliosLab (403). Bogleheads (402). CNBC (403).
- The published AQR JPM paper. I read the summary page only.

**Confidence:**
- High on origin, design and the quadrant framework. These come from Bridgewater's own documents.
- High on the 2022 −22% figure (Bloomberg, via Fortune).
- **Low on the oft-quoted "All Weather fell ~20% in 2008".** I found it only on weak secondary sites and in search summaries; see section 2.
- Medium-high on the retail backtests. They come from third parties and my own ETF calculation, and they agree with each other to within a few points.

---

## 1. Origin and design

**Founding.** Bridgewater set up the All Weather principles in 1996. In 2011 Dalio wrote that they "have now been more broadly adopted under the banner 'Risk Parity'" (Engineering Targeted Returns, p.1, PDF above). The All Weather Story gives the motive as a family trust, an allocation Dalio believed "would prove reliable long after he was gone". The guiding question was: "What kind of investment portfolio would you hold that would perform well across all environments?" (All Weather Story URL).

**The name "risk parity".** It was not Bridgewater's term. The All Weather Story says "a clever consultant adopted the term 'Risk Parity'" after 2008 (same URL).

**Four environments, equal risk.** Bridgewater's 4Q09 presentation (SDCERA PDF, p.7–8) frames asset returns around growth and inflation, each rising or falling *relative to what markets price in*. The table assigns "25% of Risk" to each of the four boxes:
- Rising growth: equities, corporate spreads, commodities, EM debt spreads.
- Rising inflation: inflation-linked bonds, commodities, EM debt spreads.
- Falling growth: nominal bonds, inflation-linked bonds.
- Falling inflation: nominal bonds, equities.

Three more points from the same pages:
- The aim is that a weak asset in one environment is "naturally offset" by another asset suited to that environment.
- The portfolio invests in "more than 40 markets" worldwide. The list includes the S&P/TSE (Canada).
- The design is explicitly not predictive. Forecasting returns, correlations "or even precise volatilities" counts as "an attempt to predict the future" (All Weather Story).

**Stock–bond correlation was understood as regime-dependent from the start.** Bridgewater 4Q09, p.7: stocks and nominal bonds "are positively correlated when changes in inflation expectations are driving markets." They are negatively correlated when growth news dominates. This matters for claim (c) below.

**Leverage.** The institutional fund levers its low-volatility assets, mainly bonds, so that each asset carries a similar amount of risk.
- Dalio: "through the use of leverage, bonds can be made 'competitive' with equities" (Engineering Targeted Returns, p.3).
- He argues that "a moderately leveraged, highly diversified portfolio is considerably less risky than an unleveraged, non-diversified one" (p.5).
- The 4Q09 deck gives a worked example: a US 10-year note at 2:1 leverage.
- Bridgewater says the leverage can sit inside the fund structure, so investors carry no accounting leverage of their own.
- **Current live implementation.** ALLW, launched 5 March 2025 at a 0.85% gross expense ratio, holds futures and swaps. At 27 Oct 2026 its notional exposures were:
  - 69.9% global nominal bonds
  - 42.8% global equities
  - 41.6% inflation-linked bonds
  - 32.5% commodities
  - About 187% in total (SSGA URL).

**Inflation-linked bonds.** They are central to the design. The All Weather Story says they "help balance out both boxes ... in a way no other asset class could." Bridgewater's work on them dates to the mid-1990s, for a US foundation that wanted steady real returns (All Weather Story).

**How the retail version differs.** Robbins' "All Seasons" mix is 30% stocks, 40% long-term Treasuries, 15% intermediate Treasuries, 7.5% gold and 7.5% commodities (Yahoo/BI excerpt; Portfolio Charts https://portfoliocharts.com/portfolios/all-seasons-portfolio/). Compared with the fund, it:
- uses **no leverage**
- holds **no inflation-linked bonds**
- holds **no EM debt or corporate spreads**
- is **US-only and not currency-hedged**
- uses fixed weights, with none of the fund's active "depression gauge" overlay. That overlay is described below.

To keep bonds at an equal risk share without leverage, the retail mix holds 55% of the money in bonds and pushes duration out through the 40% sleeve of 20–25-year Treasuries.

**The fund was not purely static either.** After Lehman, Bridgewater moved All Weather clients into a "Safe portfolio" that served as a "hurricane shelter". In May 2009 it shifted to "60% AW/40% Safe" (4Q09 deck, p.14–15). The deck also discloses that target leverage, volatility and asset mix "varied from June 1996 to July 2005", and that the strategy has targeted 10% volatility since August 2005.

**Did Dalio endorse the retail mix?** Yes, with caveats. The mix was presented in Robbins' book as Dalio's simplified answer for individuals.
- In the excerpt, Dalio warns: "It's not really that simple."
- He justifies the 30% stock weight because "stocks are three times more risky than bonds."
- He says the gold and commodities guard against faster inflation (Yahoo/BI excerpt).
- Secondary sources quote the book as calling the weights "would not be exact or perfect" (Optimized Portfolio https://www.optimizedportfolio.com/all-weather-portfolio/). Another source gives "would not be exactly right or perfect" [snippet] (https://www.dividendes.ch/2026/02/all-weather-portfolio-by-ray-dalio-backtest-and-critical-analysis-1999-2025/). I could not check the exact wording against the book.
- I found no Bridgewater document that endorses the 30/40/15/7.5/7.5 figures.
- Bridgewater's own retail product, ALLW (2025), is levered, global, and holds inflation-linked bonds. In practice that is a different portfolio.

## 2. Track record

**The institutional fund.**
- **Inception to 2009** (4Q09 deck appendix, net of fees): annualized 7.9% from June 1996 to December 2009, standard deviation 11.3%, Sharpe 0.38. For periods ending December 2009: last 1 year +9.4%, last 3 years −0.8% a year, last 5 years +2.7% a year.
- **Gross figures in the same deck:** roughly 8.4% a year at about 11% volatility.
- **The deck's long backtests are simulated.** The "since 1970" charts showing 300–400 bp a year over 60/40 at equal risk (Engineering Targeted Returns, Chart 3: 13.8% vs 9.8% at 10.6% stdev) are hypothetical. Bridgewater itself labels them "HYPOTHETICAL OR SIMULATED".
- **2008: uncertain.** Several weak secondary pages and search summaries say "fell about 20%" in 2008 [snippet] (https://angelinvestorsnetwork.com/market-analysis/risk-parity-hedge-fund-strategy-bridgewater-all-weather). I could not confirm a calendar-2008 figure from Bridgewater or a major outlet. Bridgewater's own 3-year number (−0.8% a year for 2007–09, with 2009 at +9.4%) points to a 2007–08 loss of very roughly 10% in total. It does not support a −20% calendar year. **Recommend: do not print a 2008 figure, or say "a loss in 2008, much smaller than equities'".**
- **2013:** −4.61% for "All Weather @ 12%" (Insider Monkey via Yahoo, https://finance.yahoo.com/news/bridgewater-associates-returns-aum-holdings-174743874.html).
- **2015:** −8.36% (same source). The same source gives a worst drawdown of 32.26% for the 12%-volatility version.
- **2022:** −22% for the 10%-volatility version, "its worst" year (Fortune/Bloomberg, Apr 2024). The same source reports:
  - assets fell from about $160bn (2021) to about $90bn (end-2023), roughly $70bn out
  - realized volatility of about 10.7% since launch
  - risk parity has trailed global 60/40 every year since 2019
  - a consultant quote: "It's been disappointing for a long time."
- **ALLW (live, retail, levered):**
  - +12.08% since inception (5 Mar 2025 to 30 Sep 2026, NAV) against +21.24% for MSCI ACWI IMI
  - +3.91% YTD 2026 (SSGA)

**The retail "All Seasons" portfolio.**
- **Robbins' own backtest, 1984–2013:**
  - 9.72% a year at 7.63% standard deviation
  - positive in 86% of years
  - worst year −3.93% in 2008 (Yahoo/BI excerpt)
  - Canadian Couch Potato's objection: that window rode the fall in 30-year Treasury yields from about 11% to 3.5%. "any bond-heavy portfolio would have seen rare and modest drawdowns". In that window the S&P 500 did 11.1% and Canadian long bonds 10.3%.
- **Portfolio Charts (US, 1970–2025, real):** 5.3% a year average real return, worst real drawdown 22%, longest recovery "under 11 years".
- **Lazy Portfolio ETF** (data to 30 Sep 2026; https://www.lazyportfolioetf.com/allocation/ray-dalio-all-weather/):
  - 30 years: 7.25% a year at 7.52% stdev
  - 10 years: 5.43%
  - 5 years: 3.14% nominal, −1.01% real
  - deepest drawdown since 1871: −37.0%, in the Depression era, on simulated data
  - most recent drawdown: −20.6% (2022), 42 months to recover
- **My ETF backtest, Mar 2006 to Sep 2026** (method in section 5). Mix: VTI 30 / TLT 40 / IEF 15 / GLD 7.5 / DBC 7.5, rebalanced every January.
  - **Totals:** CAGR 6.58%, volatility 8.25%, max drawdown −21.5% (Dec 2021 to Oct 2023).
  - **Comparison:** 60/40 VTI/IEF made 8.32% at 9.35% volatility, with a −26.8% max drawdown in 2007–09. VTI alone made 10.96%, with a −50.8% max drawdown.
  - **Calendar years:**

    | Year | All Seasons | 60/40 | VTI |
    |---|---|---|---|
    | 2008 | **+3.2%** | −15.0% | −37.0% |
    | 2013 | +1.1% | | |
    | 2015 | −3.3% | | |
    | 2018 | −3.1% | | |
    | 2022 | **−19.2%** | −17.8% | −19.5% |
    | 2023 | +10.0% | | |
    | 2024 | +6.0% | | |
    | 2025 | +13.4% | | |
    | 2026 YTD (to Sep) | +2.9% | | |

  - **Sleeves in 2008:** VTI −37.0, TLT +34.0, IEF +17.9, GLD +4.9, DBC −31.8.
  - **Sleeves in 2022:** VTI −19.5, TLT −31.2, IEF −15.2, GLD −0.8, DBC +19.3.
- **2000–02** (before GLD and DBC existed; stock and Treasury sleeves only, from Vanguard funds VFINX/VUSTX/VFITX in a 30:40:15 ratio, rescaled):
  - this proxy: +8.6%, −0.8%, +2.5%
  - S&P 500 (VFINX): −9.1%, −12.0%, −22.2%
  - Gold rose in 2001–02, so the full mix would probably have done slightly better than the proxy. That is my inference, not a tested figure.
- **Swiss-franc investor:** one 2026 analysis says the strategy "fails" a 1999–2025 CHF backtest [snippet] (dividendes.ch URL above). It was not read in full. It is relevant by analogy for a non-USD (Canadian) investor.

**Academic and independent evidence on risk parity.**
- **Asness, Frazzini, Pedersen (2012).**
  - *Theory:* leverage-averse investors bid up risky assets, so safer assets earn higher risk-adjusted returns, and anyone who can use leverage can harvest that.
  - *US stocks and Treasuries, 1926–2010:* risk parity Sharpe 0.53, 60/40 0.40, value-weighted market 0.25.
  - *On the bull-market worry:* "You might worry that the superiority of Risk Parity is an artifact of the bond bull" market. Their answer is that 1926–2010 saw "a near perfect round trip in bond yields".
  - *Caveat:* the result needs leverage at roughly cash-like financing costs.
- **Anderson, Bianchi, Goldberg (2011/2012).** Over 85 years, three findings:
  - "the specific start and end dates of a backtest can have a material effect"
  - "transaction costs can negate apparent outperformance"
  - significance must be tested
  
  In **1946–1982**, which included high inflation, both 60/40 and the value-weighted portfolio beat risk parity.
- **AQR, "A Changing Stock-Bond Correlation" (2023).** The correlation was positive from the 1970s through the 1990s, and "for the first two decades of the 21st century ... consistently negative". The model "explains around 70%" of long-run variation. Equities and bonds have "same-sign sensitivities to inflation news", and rising inflation uncertainty can flip the correlation back to positive. AQR's suggested remedy is "alternative diversifiers", meaning liquid alternatives and commodities.

## 3. Checking the five claims

**(a) "An equal-dollar stock/bond portfolio leaves about 90% of the risk in stocks." Broadly true; the exact number depends on the bonds and the period.**
- Bridgewater 4Q09, p.4: in a conventional ~60/40 institutional mix, "equities contribute ~90% of the portfolio's exposure." Their pie shows 62% of dollars in equities becoming 88% of risk. On the same page: a 60% equity weight "actually has more like 80%" of risk. Dalio 2011 adds that such portfolios are "about 95% correlated" with equities.
- Note that Bridgewater's ~90% refers to roughly 60/40, not 50/50.
- My calculation (monthly data Mar 2006 to Sep 2026, VTI 15.6% vol, IEF 6.6%, correlation −0.07):
  - 50/50 VTI/IEF: stocks carry **87%** of variance.
  - 60/40: **94%**.
  - With long Treasuries (TLT, 13.8% vol), a 50/50 split would be much closer to balanced.
- Suggested wording: "with intermediate bonds, roughly 85–90% of the risk at 50/50, and over 90% at 60/40."
- The retail All Seasons mix comes out at roughly **stocks 33%, long Treasuries 48%, intermediate Treasuries 8%, gold 7%, commodities 4%** of variance (same data). It is not risk-balanced by these measures. It is a bet on long-duration Treasuries, which is exactly what hurt in 2022.

**(b) "Avoids catastrophic drawdowns regardless of regime." False as stated.**
- The fund lost 22% in 2022 (Bloomberg/Fortune).
- The 12%-volatility version had a 32% worst drawdown (Insider Monkey).
- The retail mix lost about 19–22% in 2022–23 and took roughly 3.5 years to recover. That figure appears in my ETF backtest, Lazy Portfolio ETF and Portfolio Charts alike.
- On long simulated data it shows a −37% drawdown in the Depression era (Lazy Portfolio ETF).
- Its 1946–82 relative performance was poor (Anderson et al.).
- Accurate framing: **shallower drawdowns than an all-stock portfolio in growth shocks (2000–02, 2008), but no protection when inflation and rising rates hit stocks and long bonds together.**

**(c) "Long-term government bonds typically surge when stocks plunge." True in the growth and deflation crashes since about 2000. False in inflationary regimes.**
- **Recent episodes:** in 2008 TLT returned +34% while VTI fell 37%. In 2000–02 long Treasuries rallied.
- **Correlations** (monthly, VFINX vs VUSTX, my calculation):
  - 1986–1999: **+0.27**
  - 2000–2020: **−0.30**
  - 2021–Sep 2026: **+0.54**
  - 2022 alone: +0.52
- **2022:** TLT −31% and VTI −19.5%.
- **The longer record:** across eight US inflation surges since about 1926, Man Group finds annualized real returns of **−8% for 30-year Treasuries**, −5% for the 10-year and −7% for equities (Neville et al. 2021, p.11–12).
- **Bridgewater's own view:** its 2009 deck explicitly calls the correlation unstable and inflation-driven (section 1).
- Suggested wording: "have often rallied when stocks crashed on growth fears, as in 2000–02, 2008 and early 2020, but fell alongside stocks in the 1970s and in 2022."

**(d) TIPS and commodities as inflation hedges. Commodities: yes historically, but volatile and a drag the rest of the time. TIPS: robust, but modest.**
- Man Group, eight US inflation regimes, with data from 1926 (TIPS from 1959, using synthetic history before the 1997 launch):
  - **Diversified commodity futures:** +14% annualized real in inflations, a 100% hit rate, and about +1% in normal times.
  - **Gold:** +13% real, but a 67% hit rate, and −1% in normal times.
  - **TIPS:** +2% real in inflations, "not better than" in non-inflationary times, a 60% hit rate. The authors also warned in 2021 that low starting yields made TIPS a "very expensive" hedge.
- **2022, the live test:** DBC +19.3% and GLD −0.8% (my data).
- **The retail mix holds no TIPS.** For a Canadian, the analogue is Real Return Bonds, though the Government of Canada stopped issuing new RRBs in 2022. That last point comes from my background knowledge and should be verified separately if used.

**(e) The benefit of annual rebalancing. Mainly risk control, not a reliable return boost.**
- Vanguard, "Best practices for portfolio rebalancing": risk-adjusted returns are "not meaningfully different" across monthly, quarterly and annual rebalancing, but costs rise with frequency. The firm suggests annual or semi-annual monitoring with about 5% thresholds [snippet] (https://www.aaii.com/journal/article/best-practices-for-portfolio-rebalancing; Vanguard research summary https://externalcrewnet.vanguard.com/content/corporatesite/us/en/corp/articles/tuning-frequency-for-rebalancing.html).
- The main purpose is to keep risk where you intended. Without rebalancing, the stock sleeve drifts upward.
- Any "rebalancing bonus" depends on the period. Do not claim it as a guaranteed return gain.

## 4. Risk of each sleeve (the arithmetic for risk balancing)

| Sleeve | Proxy | Annualized volatility | Correlation with US stocks | Source / period |
|---|---|---|---|---|
| US stocks | VTI | 15.6% | 1.00 | my calc, 2006-03–2026-09 |
| Long Treasuries (20+y) | TLT | 13.8% | −0.09 | same |
| Intermediate Treasuries (7–10y) | IEF | 6.6% | −0.07 | same |
| Gold | GLD | 17.5% | +0.08 | same |
| Broad commodities | DBC | 18.8% | +0.44 | same |
| US stocks (long run) | CRSP VW | 19.05% | n/a | Asness et al., 1926–2010 |
| US Treasuries (broad index) | CRSP gov bonds | 3.28% | n/a | Asness et al., 1926–2010 |
| S&P 500 vs 10y note, excess returns | | 15.6% vs 7.4% | n/a | Bridgewater 4Q09 illustrative chart |

The arithmetic:
- Intermediate Treasuries have well under half the volatility of stocks. Matching stocks' risk therefore needs roughly twice as much money in them (Bridgewater uses 2:1 leverage on the 10-year note), or a switch to long duration, which is what the retail mix does.
- Robbins' "three times more risky" ratio is about right for stocks versus a broad bond index (19% vs 3–7%). It is not right for stocks versus 20-year Treasuries, which are nearly as volatile as stocks (13.8% vs 15.6%).
- Gold and commodities are each as volatile as stocks, or more so. At 7.5% weight each, they add only a small share of portfolio variance (about 7% and 4%).

## 5. Method of my backtest (to reproduce or cite as "Collegica calculation")

- **Data:** monthly adjusted closes from the Yahoo Finance chart API (`query1.finance.yahoo.com/v8/finance/chart/<TICKER>?interval=1mo`) for VTI, TLT, IEF, GLD, DBC, VFINX, VUSTX and VFITX. Downloaded 2026-10-28.
- **Returns:** total return from adjusted closes. Rebalanced to target weights at the start of each January. No fees, taxes or FX.
- **Window:** March 2006 (the first full month of DBC) to September 2026.
- **Currency:** results are in USD. A Canadian holding unhedged US ETFs would see different CAD numbers. For example, the USD rose sharply against the CAD in 2008, which would have cushioned that year's loss in CAD terms (not computed).
- **Proxy note:** the 2000–02 proxy excludes gold and commodities.
- **Variance shares:** sample covariance of monthly returns over the same window.
- **Robbins' "−3.93% in 2008" versus my "+3.2%":** the difference is plausibly down to index and data choices. Robbins' index sources were not seen.
- **Script:** scratch only (not committed), at `/private/tmp/claude-501/.../scratchpad/aw/bt.py`. Re-create from this description if the article needs it.
