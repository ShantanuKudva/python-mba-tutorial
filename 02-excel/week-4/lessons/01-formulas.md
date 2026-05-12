# Lesson 1 — Formulas: SUM, AVG, IF, ROUND

## Why this matters

Your VP of Sales hands you a raw export of Q1 numbers — six products, three regions, three months. She needs the totals by product, the average monthly revenue, and a flag on any product below $10 000 for the quarter. In Excel, that's four formulas and ten minutes. Knowing exactly which formula to reach for — and how to nest them — is what separates a business analyst from someone who just copies numbers into cells.

## The preloaded sheet

The sheet below contains Q1 sales data (Widget → Plugin, Jan–Mar). Work through the tasks directly in the cells.

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

## Core formulas

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
```

### SUM — add up a range

```
=SUM(C2:C7)        — sum Jan column for all products
=SUM(C2:E2)        — sum all three months for row 2 (Widget)
```

The Q1 Total column (F) already uses `=SUM(C2:E2)` for each product row.  
Row 8 (TOTAL) uses `=SUM(F2:F7)` — a column total.

### AVERAGE — arithmetic mean

```
=AVERAGE(C2:C7)    — average Jan revenue across all 6 products
=AVERAGE(C2:E2)    — average monthly revenue for Widget
```

### IF — branch on a condition

```
=IF(F2>=30000,"Above target","Below target")
```

`IF(condition, value_if_true, value_if_false)` — three arguments separated by commas.

You can nest them:

```
=IF(F2>=50000,"Excellent",IF(F2>=30000,"On track","Below target"))
```

### ROUND — control decimal places

```
=ROUND(F2/3, 0)    — monthly average, rounded to whole dollars
=ROUND(F2/177700, 4)   — share of total, 4 decimal places (for a percentage)
```

The second argument is the number of decimal places. Use `0` for whole numbers, `-3` for thousands.

---

## Tasks — do these in the sheet above

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
```

1. **Cell G2:** Write a formula that computes the **monthly average** for Widget (Jan+Feb+Mar divided by 3, or use `AVERAGE`). Format it as a whole number with `ROUND(..., 0)`.

2. **Cell H2:** Write an `IF` formula that shows `"Target met"` if Widget's Q1 Total (F2) is at or above 35 000, otherwise `"Below target"`.

3. **Cell C9:** (if the sheet has a gap row) Or pick any empty cell below the data — write `=AVERAGE(F2:F7)` to compute the average Q1 total across all six products.

4. **Cell F8 (TOTAL row):** Verify the formula already there. Click F8 and read the formula bar — it should say `=SUM(F2:F7)`. If the cell shows a number, not a formula, press `=` to start typing a replacement.

---

## Try it

In an empty cell below the data, write a formula that computes:

> (Widget Q1 Total + License Q1 Total) / 2

…using cell references, not raw numbers. Then wrap the whole thing in `ROUND(..., -3)` to round to the nearest thousand.

---

## Common mistakes

- **Forgetting the `=`:** typing `SUM(C2:C7)` shows the text, not the result. Every formula starts with `=`.
- **Wrong separator:** some locales use `;` instead of `,` between arguments. The in-browser sheet uses `,`.
- **Off-by-one range:** `=SUM(C2:C8)` would include the TOTAL row inside a total — double-check your ranges.

---

Next: [Lesson 2 — Cell References](02-cell-references.md)

---

## Resources

- [Excel SUM function (Microsoft)](https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89)
- [Excel IF function (Microsoft)](https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)
- [Investopedia — how to use Excel for finance](https://www.investopedia.com/articles/personal-finance/032415/advanced-excel-formulas-must-know.asp)
