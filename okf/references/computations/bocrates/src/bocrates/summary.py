"""Summarise a series of dated interest-rate observations.

The functions here are deliberately free of file paths, printing and plotting:
everything they need arrives as an argument and everything they produce is
returned. That is what makes them testable, and it is the whole reason the
analysis script is a separate file.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


def read_rates(path: str | Path) -> list[tuple[str, float]]:
    """Read a two-column `date,rate` CSV into (date, rate) pairs."""
    with open(path, newline="") as handle:
        rows = list(csv.DictReader(handle))
    return [(row["date"], float(row["rate"])) for row in rows]


def annual_average(observations: list[tuple[str, float]]) -> dict[int, float]:
    """Mean rate per calendar year, keyed by year.

    Observations are (ISO-8601 date, rate) pairs. Years are taken from the
    first four characters of the date, so the input must be ISO-8601.
    """
    buckets: dict[int, list[float]] = defaultdict(list)
    for date, rate in observations:
        buckets[int(date[:4])].append(rate)
    return {year: sum(rates) / len(rates) for year, rates in sorted(buckets.items())}
