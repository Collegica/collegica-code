import csv

total = 0.0
with open("sample.csv", newline="") as f:
    for row in csv.DictReader(f):
        total += float(row["qty"]) * float(row["price"])

print(f"{total:.2f}")
