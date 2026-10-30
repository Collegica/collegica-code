"""Backtest the retail All-Weather mix, as an American and as a Canadian would hold it.

    python backtest.py            # downloads prices, writes results.md and monthly.csv

Monthly total returns from ETF prices adjusted for distributions (Yahoo Finance
via yfinance), January 2007 to September 2026. Rebalanced to target
weights each January. No fees beyond the funds' own, no taxes, no trading
costs. USD funds are converted to Canadian dollars at the month-end exchange
rate, unhedged.

Portfolios
  US All-Weather (USD)        VTI 30, TLT 40, IEF 15, GLD 7.5, DBC 7.5
  US All-Weather, in CAD      the same funds, measured in Canadian dollars
  Canadian All-Weather (CAD)  equities 30 (XIC/VTI/EFA in thirds), XLB 40,
                              XGB 15, GLD 7.5, DBC 7.5 (US funds in CAD)
  Global equities (CAD)       XIC/VTI/EFA in thirds
  60/40 (CAD)                 global equities 60, XBB 40
  50/50 stocks/bonds (CAD)    used only for the risk-share check
  Equal-risk (CAD)            the Canadian menu re-weighted each January so each
                              sleeve contributes equal risk over the prior 36
                              months (no hindsight); from 2010

Also sorts 2007-2025 into Dalio's four seasons from Canadian data: growth
"rising" when real GDP growth (Q4 over Q4, FRED NGDPRSAXDCCAQ) beat the year
before, inflation "rising" when CPI inflation (December over December, Bank of
Canada Valet V41690973) beat the year before. Acceleration is a crude stand-in
for the "surprise versus expectations" in Bridgewater's framing.

Needs pandas and yfinance.
"""
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import yfinance as yf

HERE = Path(__file__).resolve().parent
START, END = "2006-12-01", "2026-10-01"

TICKERS = ["VTI", "TLT", "IEF", "GLD", "DBC", "EFA",
           "XIC.TO", "XLB.TO", "XGB.TO", "XBB.TO", "CAD=X"]


def monthly_prices():
    px = yf.download(TICKERS, start=START, end=END, auto_adjust=True, progress=False)["Close"]
    return px.resample("ME").last().dropna()


def returns(px):
    usdcad = px["CAD=X"]                      # CAD per USD
    usd = ["VTI", "TLT", "IEF", "GLD", "DBC", "EFA"]
    cad = px.copy()
    for t in usd:
        cad[t] = px[t] * usdcad
    r_usd = px[usd].pct_change().dropna()
    r_cad = cad.drop(columns="CAD=X").pct_change().dropna()
    return r_usd, r_cad


def portfolio(r, weights):
    """Monthly returns of a portfolio rebalanced to `weights` every January."""
    w = pd.Series(weights, dtype=float)
    w = w / w.sum()
    holding = w.copy()
    out = []
    for date, row in r[w.index].iterrows():
        if date.month == 1:
            holding = w * holding.sum()
        holding = holding * (1 + row)
        out.append(holding.sum())
    value = pd.Series(out, index=r.index)
    return value.pct_change().fillna(value.iloc[0] - 1)


def equal_risk_weights(cov, iters=10_000, tol=1e-12):
    """Weights where every sleeve contributes the same share of variance.

    Cyclical coordinate descent on  min ½ wᵀΣw − (1/n) Σ log wᵢ, whose
    solution, rescaled to sum to one, is the equal-risk portfolio. It
    converges for any positive-definite Σ, including negative correlations.
    """
    c = cov.values
    n = len(c)
    b = 1 / n
    w = 1 / np.sqrt(np.diag(c))
    for _ in range(iters):
        prev = w.copy()
        for i in range(n):
            a = c[i] @ w - c[i, i] * w[i]
            w[i] = (-a + np.sqrt(a * a + 4 * c[i, i] * b)) / (2 * c[i, i])
        if np.abs(w - prev).max() < tol:
            break
    w = w / w.sum()
    return pd.Series(w, index=cov.index)


def equal_risk_portfolio(r, lookback=36):
    """Re-weighted each January from the previous `lookback` months only."""
    out, weights_log = [], {}
    holding = None
    for i, (date, row) in enumerate(r.iterrows()):
        if date.month == 1 and i >= lookback:
            w = equal_risk_weights(r.iloc[i - lookback:i].cov())
            weights_log[date.year] = w
            holding = w * (holding.sum() if holding is not None else 1.0)
        if holding is None:
            continue
        holding = holding * (1 + row)
        out.append((date, holding.sum()))
    value = pd.Series(dict(out))
    m = value.pct_change()
    m.iloc[0] = value.iloc[0] - 1
    return m, pd.DataFrame(weights_log).T


def seasons():
    gdp = pd.read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?id=NGDPRSAXDCCAQ",
                      index_col=0, parse_dates=True).iloc[:, 0]
    obs = pd.read_json("https://www.bankofcanada.ca/valet/observations/V41690973/json?start_date=2004-01-01",
                       typ="series")["observations"]
    cpi = pd.Series({pd.Timestamp(o["d"]): float(o["V41690973"]["v"]) for o in obs})
    g = gdp[gdp.index.month == 10]
    growth = (g / g.shift(1) - 1)
    growth.index = growth.index.year
    c = cpi[cpi.index.month == 12]
    infl = (c / c.shift(1) - 1)
    infl.index = infl.index.year
    df = pd.DataFrame({"growth": growth, "inflation": infl}).dropna()
    df["growth up"] = df["growth"] > df["growth"].shift(1)
    df["inflation up"] = df["inflation"] > df["inflation"].shift(1)
    df = df.loc[2007:2025]
    df["season"] = np.select(
        [df["growth up"] & ~df["inflation up"], df["growth up"] & df["inflation up"],
         ~df["growth up"] & df["inflation up"]],
        ["Growth up, inflation down", "Growth up, inflation up", "Growth down, inflation up"],
        "Growth down, inflation down")
    return df


def stats(m):
    years = len(m) / 12
    growth = (1 + m).cumprod()
    cagr = growth.iloc[-1] ** (1 / years) - 1
    vol = m.std() * np.sqrt(12)
    dd = (growth / growth.cummax() - 1).min()
    cal = (1 + m).groupby(m.index.year).prod() - 1
    return {
        "CAGR": cagr, "Volatility": vol, "Max drawdown": dd,
        "Worst year": cal.min(), "Worst year (when)": int(cal.idxmin()),
        "2008": cal.get(2008), "2022": cal.get(2022),
        "Growth of $10,000": 10_000 * growth.iloc[-1],
    }, cal


def risk_share(r, weights):
    """Each sleeve's share of portfolio variance (weight × covariance with the portfolio)."""
    w = pd.Series(weights, dtype=float)
    w = w / w.sum()
    cov = r[w.index].cov() * 12
    contrib = w * (cov @ w)
    return contrib / contrib.sum()


def main():
    px = monthly_prices()
    r_usd, r_cad = returns(px)
    eq = {"XIC.TO": 1 / 3, "VTI": 1 / 3, "EFA": 1 / 3}

    def scaled(d, k):
        return {t: v * k for t, v in d.items()}

    us_aw = {"VTI": 30, "TLT": 40, "IEF": 15, "GLD": 7.5, "DBC": 7.5}
    ca_aw = {**scaled(eq, 30), "XLB.TO": 40, "XGB.TO": 15, "GLD": 7.5, "DBC": 7.5}
    sixty = {**scaled(eq, 60), "XBB.TO": 40}
    fifty = {**scaled(eq, 50), "XBB.TO": 50}

    runs = {
        "US All-Weather (USD)": (r_usd, us_aw),
        "US All-Weather, in CAD": (r_cad, us_aw),
        "Canadian All-Weather (CAD)": (r_cad, ca_aw),
        "Global equities (CAD)": (r_cad, eq),
        "60/40 (CAD)": (r_cad, sixty),
    }
    rows, cals, monthly = {}, {}, {}
    for name, (r, w) in runs.items():
        m = portfolio(r, w)
        rows[name], cals[name] = stats(m)
        monthly[name] = m

    sleeves = r_cad[["XLB.TO", "XGB.TO", "GLD", "DBC"]].copy()
    sleeves.insert(0, "Equities", (r_cad[list(eq)] * pd.Series(eq)).sum(axis=1))
    erc, erc_w = equal_risk_portfolio(sleeves)
    ca_since = portfolio(r_cad, ca_aw).loc[erc.index[0]:]
    rows_erc = {"Equal-risk (CAD), from 2010": stats(erc)[0],
                "Canadian All-Weather (CAD), from 2010": stats(ca_since)[0],
                "60/40 (CAD), from 2010": stats(portfolio(r_cad, sixty).loc[erc.index[0]:])[0]}
    monthly["Equal-risk (CAD)"] = erc

    period = f"{r_cad.index[0]:%B %Y} to {r_cad.index[-1]:%B %Y}"
    lines = [f"# Backtest results\n\nMonthly, {period}, rebalanced each January. "
             "Total returns from distribution-adjusted prices; no taxes or trading costs.\n"]
    table = pd.DataFrame(rows).T
    pct = ["CAGR", "Volatility", "Max drawdown", "Worst year", "2008", "2022"]
    fmt = table.copy()
    for c in pct:
        fmt[c] = table[c].map(lambda x: f"{x:.1%}")
    fmt["Growth of $10,000"] = table["Growth of $10,000"].map(lambda x: f"${x:,.0f}")
    lines.append(fmt.to_markdown())

    lines.append("\n## Calendar-year returns\n")
    lines.append(pd.DataFrame(cals).map(lambda x: f"{x:.1%}").to_markdown())

    lines.append("\n## Share of risk (variance) by sleeve\n")
    for name, r, w in [("50/50 stocks/bonds (CAD)", r_cad, fifty),
                       ("Canadian All-Weather (CAD)", r_cad, ca_aw),
                       ("US All-Weather (USD)", r_usd, us_aw)]:
        s = risk_share(r, w)
        if name.startswith("50/50"):
            s = pd.Series({"Equities": s[list(eq)].sum(), "XBB.TO": s["XBB.TO"]})
        elif name.startswith("Canadian"):
            s = pd.concat([pd.Series({"Equities": s[list(eq)].sum()}), s.drop(list(eq))])
        lines.append(f"\n**{name}**\n")
        lines.append(s.map(lambda x: f"{x:.0%}").to_frame("share of risk").to_markdown())

    lines.append("\n## Equal-risk portfolio (weights from the prior 36 months)\n")
    t2 = pd.DataFrame(rows_erc).T
    f2 = t2.copy()
    for c in pct:
        f2[c] = t2[c].map(lambda x: f"{x:.1%}" if pd.notna(x) else "")
    f2["Growth of $10,000"] = t2["Growth of $10,000"].map(lambda x: f"${x:,.0f}")
    lines.append(f2.to_markdown())
    lines.append("\nWeights chosen each January:\n")
    lines.append(erc_w.map(lambda x: f"{x:.0%}").to_markdown())
    full = equal_risk_weights(sleeves.cov())
    lines.append("\nEqual-risk weights using the whole period (hindsight):\n")
    lines.append(full.map(lambda x: f"{x:.0%}").to_frame("weight").to_markdown())

    lines.append("\n## The four seasons, 2007-2025 (Canadian data)\n")
    sz = seasons()
    yearly = (1 + sleeves).groupby(sleeves.index.year).prod() - 1
    yearly["TLT (US long Treasuries, CAD)"] = ((1 + r_cad["TLT"]).groupby(r_cad.index.year).prod() - 1)
    yearly["CAD/USD"] = None
    lines.append(sz.assign(growth=sz["growth"].map("{:.1%}".format),
                           inflation=sz["inflation"].map("{:.1%}".format))
                 [["growth", "inflation", "season"]].to_markdown())
    joined = yearly.drop(columns="CAD/USD").join(sz["season"], how="inner")
    avg = joined.groupby("season").mean()
    avg["years"] = joined.groupby("season").size()
    lines.append("\nAverage calendar-year return in each season (CAD):\n")
    lines.append(avg.map(lambda x: f"{x:.1%}" if isinstance(x, float) else x).to_markdown())

    lines.append("\n## Correlations of monthly returns (CAD)\n")
    corr = r_cad[["XIC.TO", "VTI", "TLT", "XLB.TO", "GLD", "DBC"]].corr().round(2)
    lines.append(corr.to_markdown())

    (HERE / "results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    pd.DataFrame(monthly).to_csv(HERE / "monthly.csv", float_format="%.6f")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
