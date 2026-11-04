# Expenses Extraction Notes

## Uncertainties

1. **Jean Coutu (IMG_4401.png, 2026-09-04)**: OCR output shows "subtotal 749" and "Tax 112" and "TOTAL CAD 861" — these appear to be missing decimal points (7.49, 1.12, 8.61). I've interpreted as $8.61 CAD total. Category "Other" (pharmacy/health items).

2. **Provigo (IMG_4402.png, 2026-09-10)**: OCR shows "subtotal 20.31" and "TOTAL CAD 20.31" with no tax line — treated as tax-inclusive total. Category "Groceries".

3. **BIXI (IMG_4403.png, 2026-09-16)**: OCR shows "Subtotal 7.25" and "TOTAL CAD 7.25" with no tax line — treated as tax-inclusive total. Category "Transport".

4. **Sushi Shop (IMG_4404.png, 2026-09-21)**: OCR shows "subtotal 15.95", "Tax 2.39", "TOTAL CAD 18.34" — math checks out (15.95 * 1.15 = 18.3425 ≈ 18.34). Category "Meals".

5. **Amazon.com duplicate (IMG_4405.png & scan_0016.pdf, both 2026-09-26)**: Both files show identical purchase (USB-C cable, $12.99 USD, same date). Listed once with both source files noted.

6. **Canadian Tire (IMG_4406.png, 2026-09-30)**: OCR shows "subtotal 24.99", "Tax 3.74", "TOTAL CAD 28.73" — math checks out (24.99 * 1.15 = 28.7385 ≈ 28.73). Category "Other" (hardware).

7. **Bureau Plus refund (refund.txt, 2026-09-22)**: Shows negative amounts (return of pens). Included as negative expense in Office category.

8. **Pharmaprix (receipt (3).txt, 2026-09-12)**: Toothpaste and Vitamin D — categorized as "Other" (pharmacy/personal care), not Groceries.

9. **Indigo (scan_0014.pdf, 2026-09-15)**: Notebook and Book — categorized as "Office" (could also be "Other").

10. **OCR limitations**: All PNG receipts were processed with Tesseract OCR (--psm 6). Some line items may be missing or misread. Amounts were cross-checked where subtotal/tax/total math was visible.