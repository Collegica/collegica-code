import csv
from collections import defaultdict

with open('members.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("=== ALL ROWS ===")
for i, r in enumerate(rows, 1):
    print(f"Row {i}: {r}")

print("\n=== ISSUES FOUND ===")

# 1. Check for duplicates by email (case-insensitive)
email_map = defaultdict(list)
for i, r in enumerate(rows):
    email = r['email'].strip().lower()
    email_map[email].append((i+1, r))

for email, entries in email_map.items():
    if len(entries) > 1:
        print(f"DUPLICATE EMAIL: {email}")
        for row_num, r in entries:
            print(f"  Row {row_num}: name='{r['name']}', plot={r['plot']}, joined={r['joined']}, fee={r['fee_paid_cad']}, note={r['note']}")

# 2. Blank fees
print("\nBLANK FEES:")
for i, r in enumerate(rows):
    fee = r['fee_paid_cad'].strip()
    if fee == '':
        print(f"  Row {i+1}: {r['name']} - fee is blank")

# 3. Refunds (negative fees)
print("\nREFUNDS/NEGATIVE FEES:")
for i, r in enumerate(rows):
    fee = r['fee_paid_cad'].strip()
    if fee.startswith('-'):
        print(f"  Row {i+1}: {r['name']} - fee={fee}, note={r['note']}")

# 4. Odd formats (non-standard decimals)
print("\nODD FEE FORMATS:")
for i, r in enumerate(rows):
    fee = r['fee_paid_cad'].strip()
    if fee and not fee.startswith('-'):
        try:
            val = float(fee)
            if fee != f"{val:.2f}":
                print(f"  Row {i+1}: {r['name']} - fee='{fee}' (parsed as {val})")
        except:
            print(f"  Row {i+1}: {r['name']} - fee='{fee}' (UNPARSEABLE)")

# 5. Half-season / partial payments
print("\nPARTIAL PAYMENTS (half season):")
for i, r in enumerate(rows):
    if 'half season' in r['note'].lower():
        print(f"  Row {i+1}: {r['name']} - fee={r['fee_paid_cad']}")

# Calculate totals
print("\n=== TOTAL CALCULATION ===")
# Unique members by email (case-insensitive), keeping first occurrence
seen_emails = set()
unique_members = []
for r in rows:
    email = r['email'].strip().lower()
    if email not in seen_emails:
        seen_emails.add(email)
        unique_members.append(r)

print(f"Unique members (by email): {len(unique_members)}")

total = 0
paying_members = 0
for r in unique_members:
    fee_str = r['fee_paid_cad'].strip()
    if fee_str == '':
        fee = 0
    else:
        fee = float(fee_str)
    total += fee
    if fee > 0:
        paying_members += 1
    print(f"  {r['name']}: {fee}")

print(f"\nTotal collected (all unique members): {total:.2f} CAD")
print(f"Paying members: {paying_members}")
print(f"Members with $0 or negative: {len(unique_members) - paying_members}")

# Also calculate 2026 joiners only
print("\n=== 2026 JOINERS ONLY ===")
total_2026 = 0
count_2026 = 0
for r in unique_members:
    joined = r['joined'].strip()
    if joined.startswith('2026-'):
        fee_str = r['fee_paid_cad'].strip()
        fee = float(fee_str) if fee_str else 0
        total_2026 += fee
        count_2026 += 1
        print(f"  {r['name']}: joined {joined}, fee={fee}")
print(f"2026 joiners: {count_2026}, total: {total_2026:.2f} CAD")

EOF