# Exercise 01 — SUM Basics 🟢

**Scenario:** Your manager asks for a quick summary of Q1 performance before the Monday meeting. She needs: total revenue for January across all products, total Q1 revenue for all products combined, and the highest single-product Q1 total.

## The sheet

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

## Tasks

Complete each task by editing the sheet above — type your formula in the indicated cell and press Enter.

**Task 1 — January total (cell C9):**  
In the empty cell C9, write a formula that sums all January revenue (C2:C7).

Expected result: the sum of 12000 + 8500 + 45000 + 22000 + 3200 + 18000.

**Task 2 — Q1 grand total (cell F9 or any empty cell):**  
Write `=SUM(F2:F7)` to compute the grand total across all products. Compare it to F8 — they should match.

**Task 3 — Maximum Q1 product (any empty cell):**  
Write `=MAX(F2:F7)`. Which product does this correspond to? Look at the row with that value in column F.

**Task 4 — Minimum Q1 product (any empty cell):**  
Write `=MIN(F2:F7)`. Which product had the lowest quarter?

## Expected results

Once you've written your formulas, the numbers should tell a clear story: one product category dominates (Licenses at ~$143k), while hardware accessories trail far behind.

## Solution

<details>
<summary>Reveal solution</summary>

- C9: `=SUM(C2:C7)` → 108,200
- F9: `=SUM(F2:F7)` → same as F8 (345,900 if Q1 Total formulas in F2:F7 are correct)
- MAX: `=MAX(F2:F7)` → 143,000 (License, row 4)
- MIN: `=MIN(F2:F7)` → 10,500 (Cable, row 6)

</details>
