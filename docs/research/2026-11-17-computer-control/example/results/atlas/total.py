import csv
from decimal import Decimal

with open("sample.csv", newline="") as f:
    total = sum(Decimal(row["qty"]) * Decimal(row["price"]) for row in csv.DictReader(f))

print(f"{total:.2f}")
