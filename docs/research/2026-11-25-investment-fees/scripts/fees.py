"""All-in investment fees and what they cost over time.

All portfolios are made up. Returns are real (after inflation) and constant,
before any fee; fees come off the return each year. No tax. Contributions are
made at the end of each year, retirement withdrawals at the start.

    python3 fees.py
"""
R = 0.04          # assumed real return before fees
YEARS = 25
START, ADD = 100_000, 6_000
LEVELS = [0.0025, 0.01, 0.022]

# (name, value, MER %, TER %) -- invented holdings
HOLDINGS = [("Balanced mutual fund", 60_000, 2.10, 0.08),
            ("Global equity ETF", 30_000, 0.20, 0.02),
            ("Canadian bond ETF", 10_000, 0.10, 0.01)]
ADVICE = 0.0      # separate advisory fee, % of the whole account
FLAT = 100        # fixed account fees, $ a year


def all_in(holdings=HOLDINGS, advice=ADVICE, flat=FLAT):
    total = sum(h[1] for h in holdings)
    rows = [(n, v, mer + ter, v * (mer + ter) / 100) for n, v, mer, ter in holdings]
    dollars = sum(r[3] for r in rows) + total * advice / 100 + flat
    return total, rows, dollars


def grow(fee, r=R, years=YEARS, start=START, add=ADD):
    """Ending balance and the fees actually charged along the way."""
    bal, paid = start, 0.0
    for _ in range(years):
        gross = bal * (1 + r)
        charge = bal * fee
        bal, paid = gross - charge + add, paid + charge
    return bal, paid


def spend(balance, fee, r=R, years=YEARS):
    """Level yearly spending, taken at the start of each year, that ends at zero."""
    net = r - fee
    return balance * net / (1 - (1 + net) ** -years) / (1 + net)


def main():
    total, rows, dollars = all_in()
    print("One account, read from a statement (made up)")
    print(f"{'holding':24}{'value':>9}{'MER+TER':>9}{'$ a year':>10}")
    for n, v, rate, d in rows:
        print(f"{n:24}{v:>9,}{rate:>8.2f}%{d:>10,.0f}")
    print(f"{'fixed account fees':24}{'':>18}{FLAT:>10,}")
    print(f"{'all-in':24}{total:>9,}{dollars / total:>9.2%}{dollars:>10,.0f}")

    print(f"\n${START:,} plus ${ADD:,} a year for {YEARS} years, {R:.0%} real before fees")
    free = grow(0)[0]
    print(f"no fee: {free:,.0f}")
    print(f"{'fee':>6}{'ending':>11}{'gap':>10}{'share':>8}{'fees charged':>14}{'lost growth':>13}")
    for f in LEVELS:
        end, paid = grow(f)
        gap = free - end
        print(f"{f:>6.2%}{end:>11,.0f}{gap:>10,.0f}{gap / free:>8.1%}"
              f"{paid:>14,.0f}{gap - paid:>13,.0f}")

    print(f"\nSpending from $500,000 for {YEARS} years, ending at zero")
    base = spend(500_000, 0.0025)
    for f in LEVELS:
        s = spend(500_000, f)
        print(f"{f:>6.2%}{s:>10,.0f} a year{s - base:>+10,.0f} vs 0.25%")

    print("\nSensitivity: ending-balance gap between 2.2% and 0.25%")
    for r in (0.02, 0.04, 0.06):
        for y in (10, 25, 35):
            gap = grow(0.0025, r, y)[0] - grow(0.022, r, y)[0]
            print(f"real {r:.0%}, {y:2} years: {gap:>9,.0f}"
                  f"  ({gap / grow(0.0025, r, y)[0]:.1%} of the cheaper result)")

    print("\nSwitching: years of saved fees needed to repay a one-time cost")
    old, new, value = 0.022, 0.0025, 100_000
    for label, cost in [("account transfer fee $150", 150),
                        ("redemption charge 3%", 0.03 * value),
                        ("tax on $30,000 gain, half taxable, 30% rate", 30_000 * 0.5 * 0.30)]:
        print(f"{label:46}{cost:>7,.0f}{cost / ((old - new) * value):>7.1f} years")


if __name__ == "__main__":
    main()
