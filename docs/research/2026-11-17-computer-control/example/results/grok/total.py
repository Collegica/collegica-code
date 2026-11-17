import csv
from decimal import Decimal

total = Decimal("0")
with open("sample.csv", newline="") as f:
    for row in csv.DictReader(f):
        total += Decimal(row["qty"]) * Decimal(row["price"])

print(f"Grand total: {total:.2f}")
