"""Make the made-up receipts folder used for the three-app test.

    python make_receipts.py OUTDIR

Writes 20 files into OUTDIR/receipts/ (8 plain text, 6 text PDFs, 6 PNG
"photos") and the answer key to OUTDIR/answer-key.csv, outside the folder the
agents see. Every vendor, amount and date is invented. Three traps: one
purchase appears twice (a PDF and a photo of the same receipt), one file is a
refund, and one purchase is in US dollars. Needs Pillow and fpdf2.
"""
import csv
import sys
from pathlib import Path

from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont

QC = 0.14975  # GST + QST

# (file, date, vendor, [(item, price)], tax rate, category, currency)
RECEIPTS = [
    ("2026-09-02_groceries.txt", "2026-09-02", "Marché Laurier", [("Bread", 4.25), ("Apples 2kg", 6.98), ("Coffee beans", 17.49)], 0.0, "Groceries", "CAD"),
    ("bus-pass-sept.txt", "2026-09-01", "STM", [("Monthly pass", 97.00)], 0.0, "Transport", "CAD"),
    ("lunch.txt", "2026-09-05", "Café Olimpico", [("Sandwich", 11.50), ("Latte", 5.25)], QC, "Meals", "CAD"),
    ("staples.txt", "2026-09-08", "Bureau Plus", [("Printer paper", 12.99), ("Pens x10", 8.49)], QC, "Office", "CAD"),
    ("receipt (3).txt", "2026-09-12", "Pharmaprix", [("Toothpaste", 4.99), ("Vitamin D", 12.99)], QC, "Other", "CAD"),
    ("taxi.txt", "2026-09-14", "Taxi Diamond", [("Fare", 23.40), ("Tip", 4.00)], 0.0, "Transport", "CAD"),
    ("dinner-friday.txt", "2026-09-19", "Restaurant Damas", [("Dinner for two", 86.00)], QC, "Meals", "CAD"),
    ("refund.txt", "2026-09-22", "Bureau Plus", [("Return: Pens x10", -8.49)], QC, "Office", "CAD"),
    ("scan_0012.pdf", "2026-09-03", "IGA", [("Milk", 5.49), ("Eggs", 6.29), ("Cheese", 9.99)], 0.0, "Groceries", "CAD"),
    ("scan_0013.pdf", "2026-09-09", "Via Rail", [("Montreal-Ottawa", 64.00)], 0.13, "Transport", "CAD"),
    ("scan_0014.pdf", "2026-09-15", "Indigo", [("Notebook", 18.95), ("Book", 29.99)], 0.05, "Office", "CAD"),
    ("scan_0015.pdf", "2026-09-20", "Metro", [("Vegetables", 14.37), ("Rice 5kg", 13.99), ("Olive oil", 15.49)], 0.0, "Groceries", "CAD"),
    ("scan_0016.pdf", "2026-09-26", "Amazon.com", [("USB-C cable", 12.99)], 0.0, "Office", "USD"),
    ("scan_0017.pdf", "2026-09-28", "Tim Hortons", [("Coffee", 2.39), ("Bagel", 2.79)], QC, "Meals", "CAD"),
    ("IMG_4401.png", "2026-09-04", "Jean Coutu", [("Bandages", 7.49)], QC, "Other", "CAD"),
    ("IMG_4402.png", "2026-09-10", "Provigo", [("Chicken", 16.82), ("Pasta", 3.49)], 0.0, "Groceries", "CAD"),
    ("IMG_4403.png", "2026-09-16", "Bixi", [("Day pass", 7.25)], 0.0, "Transport", "CAD"),
    ("IMG_4404.png", "2026-09-21", "Sushi Shop", [("Combo", 15.95)], QC, "Meals", "CAD"),
    ("IMG_4405.png", "2026-09-26", "Amazon.com", [("USB-C cable", 12.99)], 0.0, "Office", "USD"),  # same purchase as scan_0016
    ("IMG_4406.png", "2026-09-30", "Canadian Tire", [("Extension cord", 24.99)], QC, "Other", "CAD"),
]


def receipt_text(date, vendor, items, tax, currency):
    sub = round(sum(p for _, p in items), 2)
    t = round(sub * tax, 2)
    out = [vendor.upper(), f"Date: {date}", "-" * 28]
    out += [f"{n:<20}{p:>8.2f}" for n, p in items]
    out += ["-" * 28, f"{'Subtotal':<20}{sub:>8.2f}"]
    if tax:
        out.append(f"{'Tax':<20}{t:>8.2f}")
    out.append(f"{'TOTAL ' + currency:<20}{sub + t:>8.2f}")
    return out, round(sub + t, 2)


def main(outdir):
    folder = Path(outdir) / "receipts"
    folder.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default(size=22)
    key = []
    for name, date, vendor, items, tax, category, currency in RECEIPTS:
        text, total = receipt_text(date, vendor, items, tax, currency)
        path = folder / name
        if name.endswith(".txt"):
            path.write_text("\n".join(text) + "\n", encoding="utf-8")
        elif name.endswith(".pdf"):
            pdf = FPDF(format=(80, 40 + 6 * len(text)))
            pdf.add_page()
            pdf.set_font("Courier", size=9)
            for line in text:
                pdf.cell(0, 5, line.encode("latin-1", "replace").decode("latin-1"), new_x="LMARGIN", new_y="NEXT")
            pdf.output(str(path))
        else:
            im = Image.new("RGB", (420, 60 + 30 * len(text)), (246, 243, 236))
            draw = ImageDraw.Draw(im)
            for i, line in enumerate(text):
                draw.text((24, 24 + 30 * i), line, fill=(40, 40, 40), font=font)
            im.rotate(2, expand=True, fillcolor=(120, 110, 100)).save(path)
        key.append([name, date, vendor, f"{total:.2f}", currency, category])
    with open(Path(outdir) / "answer-key.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["file", "date", "vendor", "total", "currency", "category"])
        w.writerows(key)
    cad = sum(float(k[3]) for k in key if k[4] == "CAD")
    print(f"{len(key)} files; CAD total {cad:.2f}; plus USD 12.99 once (IMG_4405 repeats scan_0016)")


if __name__ == "__main__":
    main(sys.argv[1])
