"""Replay Canadian retirements with and without a cash buffer.

Data: Statistics Canada tables, which you download and unzip into DATA
(argument 1); they are not committed. All figures printed are in today's-money terms of the start
month (deflated by Canada all-items CPI).

  10-10-0125  S&P/TSX composite close (to 2023-09), dividend yield (to 2016-08)
  10-10-0139  3-month Treasury bill and 10-year benchmark bond yields (daily)
  18-10-0004  Consumer Price Index, monthly

Assumptions, all adjustable below: the dividend yield after August 2016; the
bond return, built from the 10-year yield; no fees and no tax.
"""
import csv, sys
from pathlib import Path

DATA = Path(sys.argv[1])
START_VALUE, SPEND = 1_000_000.0, 40_000.0   # made-up round numbers
EQUITY = 0.60                                # of the invested part
DURATION = 8.0                               # of a 10-year bond, approx.
LATE_YIELD = 3.0                             # dividend yield, % a year, after 2016-08
TRIGGER = 0.10                               # spend cash when this far below peak
END = "2023-09"


def table(pid):
    path = DATA / f"{pid}.csv"
    if not path.exists():
        sys.exit(f"missing {path}\nDownload "
                 f"https://www150.statcan.gc.ca/n1/tbl/csv/{pid}-eng.zip "
                 f"and unzip {pid}.csv into {DATA}")
    return csv.DictReader(open(path, encoding="utf-8-sig"))


def load():
    price, dy, cpi, daily = {}, {}, {}, {}
    for r in table("10100125"):
        name, v = r["Toronto Stock Exchange Statistics"], r["VALUE"]
        if v and name.endswith("Composite Index, close"):
            price[r["REF_DATE"]] = float(v)
        if v and "dividend yields" in name:
            dy[r["REF_DATE"]] = float(v)
    for r in table("18100004"):
        if r["GEO"] == "Canada" and r["Products and product groups"] == "All-items" and r["VALUE"]:
            cpi[r["REF_DATE"]] = float(r["VALUE"])
    wanted = {"Treasury Bills, 3-month": "bill",
              "Government of Canada benchmark bond yields, 10 year": "bond"}
    for r in table("10100139"):
        key = wanted.get(r["Financial market statistics"])
        if key and r["VALUE"]:
            # rows are in date order, so the last value of each month wins
            daily.setdefault(key, {})[r["REF_DATE"][:7]] = float(r["VALUE"])
    return price, dy, cpi, daily["bill"], daily["bond"]


def returns(late_yield=LATE_YIELD):
    """Monthly (month, equity, bond, cash, inflation) returns."""
    price, dy, cpi, bill, bond = load()
    months = sorted(m for m in price if "1999-12" <= m <= END)
    out = []
    for prev, m in zip(months, months[1:]):
        y = dy.get(m, late_yield) / 100
        eq = price[m] / price[prev] - 1 + y / 12
        bd = bond[prev] / 1200 - DURATION * (bond[m] - bond[prev]) / 100
        cs = bill[prev] / 1200
        out.append((m, eq, bd, cs, cpi[m] / cpi[prev] - 1))
    return out


def run(R, start, years_cash, rule, equity=EQUITY, spend=SPEND, until=END,
        trigger=TRIGGER, cash_extra=0.0, path=None):
    """rule: 'none'   everything invested, no cash
             'hold'   cash is a fixed share of the whole, rebalanced monthly
             'wedge'  cash is spent while the invested part is below its peak
                      by TRIGGER, and refilled when it regains the peak
             'once'   cash is spent first and never refilled"""
    buf = years_cash * spend
    inv, cash = START_VALUE - buf, buf
    share = buf / START_VALUE
    index = peak = 1.0
    price_level, low, n = 1.0, START_VALUE, 0
    for m, eq, bd, cs, inf in R:
        if m < start or m > until:
            continue
        need = spend / 12 * price_level          # spent at the start of the month
        if rule == "wedge":
            down = index < peak * (1 - trigger)
            if not down and index >= peak:       # at a high: top the buffer up
                move = min(max(buf * price_level - cash, 0), inv)
                inv, cash = inv - move, cash + move
            from_cash = min(need, cash) if down else 0.0
        elif rule == "once":
            from_cash = min(need, cash)
        elif rule == "hold":
            from_cash = need * share
        else:
            from_cash = 0.0
        from_inv = min(need - from_cash, inv)
        from_cash += min(need - from_cash - from_inv, cash - from_cash)
        inv, cash = inv - from_inv, cash - from_cash
        if rule == "hold" and share:
            total = inv + cash
            inv, cash = total * (1 - share), total * share
        growth = equity * eq + (1 - equity) * bd
        inv *= 1 + growth
        cash *= 1 + cs + cash_extra / 12
        index *= 1 + growth
        peak = max(peak, index)
        price_level *= 1 + inf
        n += 1
        if path is not None:
            path.append((m, (inv + cash) / price_level))
        if n <= 24:                              # lowest point, first two years
            low = min(low, (inv + cash) / price_level)
    return (inv + cash) / price_level, low


RULES = [("no cash", 0, "none"),
         ("0.5 yr, spent in downturns", 0.5, "wedge"),
         ("2 yr, spent in downturns", 2, "wedge"),
         ("2 yr, spent first", 2, "once"),
         ("2 yr, held as a fixed 8%", 2, "hold"),
         ("5 yr, spent in downturns", 5, "wedge"),
         ("5 yr, held as a fixed 20%", 5, "hold")]


def report(R, title, start, until=END):
    print(f"\n{title}: retire {start}, measured to {until}")
    print(f"{'strategy':30}{'left at end':>13}{'low, 2 years':>15}")
    for label, n, rule in RULES:
        end, low = run(R, start, n, rule, until=until)
        print(f"{label:30}{end:>13,.0f}{low:>15,.0f}")


def main():
    R = returns()
    print(f"data {R[0][0]} to {R[-1][0]}; ${START_VALUE:,.0f}, spending ${SPEND:,.0f} "
          f"a year indexed to CPI; invested part {EQUITY:.0%} TSX, rest 10-year bonds")
    checks(R)
    report(R, "Retiring into 2008", "2008-06")
    report(R, "Retiring into 2020", "2020-02")
    report(R, "A calmer start", "2009-04")
    report(R, "Retiring into the 2000 peak", "2000-09")

    print("\nEvery start month 2000-01 to 2013-09, each measured over 10 years")
    starts = [r[0] for r in R if r[0] <= "2013-09"]
    base = []
    print(f"{'strategy':30}{'median left':>13}{'worst left':>13}{'beats no cash':>15}")
    for label, n, rule in RULES:
        ends = []
        for s in starts:
            y, mo = int(s[:4]), s[5:]
            ends.append(run(R, s, n, rule, until=f"{y + 10}-{mo}")[0])
        base = base or ends
        wins = sum(e > b + 1 for e, b in zip(ends, base))
        print(f"{label:30}{sorted(ends)[len(ends)//2]:>13,.0f}{min(ends):>13,.0f}"
              f"{wins:>9} of {len(ends)}")

    print("\nSensitivity, retire 2008-06, left at end / low in first two years")
    for name, kw, y in [("base", {}, LATE_YIELD), ("late yield 2%", {}, 2.0),
                        ("late yield 4%", {}, 4.0), ("all equity", {"equity": 1.0}, LATE_YIELD),
                        ("40% equity", {"equity": 0.4}, LATE_YIELD),
                        ("spend 50,000", {"spend": 50_000}, LATE_YIELD),
                        ("trigger 0%", {"trigger": 0.0}, LATE_YIELD),
                        ("trigger 20%", {"trigger": 0.2}, LATE_YIELD),
                        ("cash pays +1%", {"cash_extra": 0.01}, LATE_YIELD),
                        ("cash pays +2%", {"cash_extra": 0.02}, LATE_YIELD)]:
        Rs = returns(y)
        cells = []
        for label, n, rule in [RULES[0], RULES[2], RULES[4]]:
            end, low = run(Rs, "2008-06", n, rule, **kw)
            cells.append(f"{end:>10,.0f} /{low:>9,.0f}")
        print(f"{name:16}" + " |".join(cells))


def checks(R):
    print("\nCalendar-year returns used, for checking against published figures")
    print(f"{'year':6}{'TSX':>8}{'bonds':>8}{'bills':>8}{'CPI':>8}")
    for year in ("2008", "2009", "2020", "2022"):
        g = [1.0] * 4
        for m, *r in R:
            if m.startswith(year):
                g = [a * (1 + b) for a, b in zip(g, r)]
        print(f"{year:6}" + "".join(f"{x - 1:>8.1%}" for x in g))


def chart(R, out):
    """The 2008 retirement under three strategies, as a static SVG."""
    series = [("No cash", 0, "none", "#2a78d6"),
              ("5 years of cash, spent in downturns", 5, "wedge", "#eb6834"),
              ("2 years of cash, spent first", 2, "once", "#1baf7a")]
    W, H, L, Rt, T, B = 900, 460, 70, 110, 84, 40
    lo, hi = 450_000, 1_050_000
    paths = []
    for label, n, rule, colour in series:
        pts = [("2008-05", START_VALUE)]
        run(R, "2008-06", n, rule, path=pts)
        paths.append((label, colour, pts))
    count = len(paths[0][2])
    x = lambda i: L + i * (W - L - Rt) / (count - 1)
    y = lambda v: T + (hi - v) * (H - T - B) / (hi - lo)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
         f'height="{H}" font-family="system-ui, sans-serif" font-size="13">',
         f'<rect width="{W}" height="{H}" fill="#fcfcfb"/>',
         '<text x="16" y="26" font-size="16" font-weight="600" fill="#0b0b0b">'
         'Retiring into 2008: savings left, in June 2008 dollars</text>']
    lx = 16
    for label, colour, _ in paths:
        o.append(f'<line x1="{lx}" x2="{lx + 18}" y1="52" y2="52" stroke="{colour}" stroke-width="3"/>'
                 f'<text x="{lx + 25}" y="57" fill="#52514e">{label}</text>')
        lx += 45 + len(label) * 7
    for v in range(500_000, 1_000_001, 100_000):
        o.append(f'<line x1="{L}" x2="{W - Rt}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="#e4e3df"/>'
                 f'<text x="{L - 8}" y="{y(v) + 4:.1f}" text-anchor="end" fill="#52514e">'
                 f'${v // 1000:,}k</text>')
    for i, (m, _) in enumerate(paths[0][2]):
        if m.endswith("-01") and int(m[:4]) % 3 == 0:
            o.append(f'<text x="{x(i):.1f}" y="{H - 14}" text-anchor="middle" '
                     f'fill="#52514e">{m[:4]}</text>')
    for label, colour, pts in paths:
        line = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, (_, v) in enumerate(pts))
        o.append(f'<polyline points="{line}" fill="none" stroke="{colour}" '
                 f'stroke-width="2" stroke-linejoin="round"/>')
    # end labels, pushed apart where the lines finish close together
    last = None
    for label, colour, pts in sorted(paths, key=lambda p: -p[2][-1][1]):
        v = pts[-1][1]
        ly = y(v) if last is None else max(y(v), last + 17)
        last = ly
        o.append(f'<circle cx="{x(count - 1):.1f}" cy="{y(v):.1f}" r="4" fill="{colour}"/>'
                 f'<circle cx="{W - Rt + 14}" cy="{ly:.1f}" r="4" fill="{colour}"/>'
                 f'<text x="{W - Rt + 24}" y="{ly + 4:.1f}" fill="#0b0b0b">${v / 1000:,.0f}k</text>')
    o.append("</svg>")
    Path(out).write_text("\n".join(o) + "\n")


if __name__ == "__main__":
    main()
    if len(sys.argv) > 2:                        # optional: where to write the chart
        chart(returns(), sys.argv[2])
