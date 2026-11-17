import csv

total = 0.0
with open("sample.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        qty = float(row["qty"])
        price = float(row["price"])
        total += qty * price

print(total)
