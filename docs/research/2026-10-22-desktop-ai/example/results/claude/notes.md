# Notes on expenses.xlsx (September 2026)

19 rows from 20 receipt files. CAD total: 585.40. USD total: 12.99. The two currencies are totalled separately and not converted.

## Duplicate
- **Amazon.com, 2026-09-26, USB-C cable, 12.99 USD**: `scan_0016.pdf` and `IMG_4405.png` show the same receipt (same date, item and amount). I listed it once. If you actually bought two cables, add a second row.

## Things I was unsure about
- **Refund (`refund.txt`)**: Bureau Plus, 2026-09-22, -9.76 CAD, for returning the pens bought on 2026-09-08 (`staples.txt`). It isn't a purchase, but I included it as a negative row so the CAD total shows what you really spent. Delete the row if you want gross purchases only.
- **Categories that were judgment calls:**
  - Jean Coutu (bandages) and Pharmaprix (toothpaste, vitamin D): pharmacy items, so **Other**.
  - Indigo (notebook 18.95 + book 29.99): **Office**. The book might be personal and belong in Other.
  - Canadian Tire (extension cord): **Other**. Could be Office if it's for your desk setup.
  - Amazon USB-C cable: **Office**.
  - VIA Rail Montreal–Ottawa: **Transport**. This could be business travel.
  - Restaurant Damas, "Dinner for two": **Meals**. I couldn't tell whether it was personal or business.
- **Taxi Diamond**: the 27.40 total includes a 4.00 tip. The receipt shows no tax line.
- **No tax on some receipts**: STM, BIXI, Taxi Diamond, Amazon and the grocery receipts (Marché Laurier, IGA, Provigo, Metro) show no tax. That's normal for basic groceries and transit passes, so I used the printed totals as-is. The Amazon receipt may leave out tax or import charges billed separately.
- **VIA Rail tax** is 13% (Ontario HST), not Quebec's 14.975%. It matches the receipt, so I didn't change it.
- **Filenames**: `staples.txt` is actually from **Bureau Plus**, not Staples. I used the vendor printed on each receipt, not the filename.
- **Images**: the PNG receipts were read visually. They were clear, but you may want to double-check the amounts.

All other totals were checked: line items add up to the subtotal, and subtotal plus tax equals the total. Nothing in `receipts/` was changed.
