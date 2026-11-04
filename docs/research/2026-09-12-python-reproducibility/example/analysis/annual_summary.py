#!/usr/bin/env python3
"""Regenerate outputs/annual-average.csv from data/overnight.csv.

Run with `pixi run summary`. Deterministic: same input, same output, every time.
"""

from pathlib import Path

from bocrates import annual_average, read_rates

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "overnight.csv"
OUT = ROOT / "outputs" / "annual-average.csv"


def main() -> None:
    averages = annual_average(read_rates(DATA))
    OUT.parent.mkdir(exist_ok=True)
    with open(OUT, "w", newline="") as handle:
        handle.write("year,mean_rate\n")
        for year, mean in averages.items():
            handle.write(f"{year},{mean:.4f}\n")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(averages)} rows)")


if __name__ == "__main__":
    main()
