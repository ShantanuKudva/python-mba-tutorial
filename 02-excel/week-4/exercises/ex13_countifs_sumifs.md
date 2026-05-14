# Exercise 13 — COUNTIFS & SUMIFS: Multi-Condition Reporting 🔴

**Scenario:** Your regional sales director needs a performance report: total Q1 revenue by product for products that beat the average, and a count of products with at least two months exceeding $10k. You'll need SUMIFS and COUNTIFS with multiple criteria to build the report without a pivot table.

## The sheet

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

Columns: B = Product, C = Jan, D = Feb, E = Mar, F = Q1 Total.

## Tasks

**Task 1 — Sum of products above average (single criterion on F):**  
First calculate the average Q1 total in a blank cell: `=AVERAGE(F2:F7)`.

Then use SUMIF to sum only products whose Q1 total (F) exceeds that average:
```
=SUMIF(F2:F7, ">"&AVERAGE(F2:F7), F2:F7)
```
(The `">"&` trick concatenates the operator with a calculated value.)

**Task 2 — Count months where revenue exceeded $10,000 across columns C, D, E:**  
In a blank cell: `=COUNTIF(C2:E7, ">10000")` — this counts all cells in the 6×3 range that exceed $10k. How many of the 18 month-product cells cleared the bar?

**Task 3 — Multi-criterion SUMIFS: Jan AND Feb both >10k:**  
Use COUNTIFS to count products where BOTH January (C) AND February (D) exceeded $10,000:
```
=COUNTIFS(C2:C7, ">10000", D2:D7, ">10000")
```

**Task 4 — Multi-criterion SUMIFS: sum Q1 totals for "strong" products:**  
Define a "strong" product as one where Jan > $10k AND Q1 Total > $50k. Use SUMIFS to total their Q1 revenue:
```
=SUMIFS(F2:F7, C2:C7, ">10000", F2:F7, ">50000")
```

**Task 5 — AVERAGEIF: average Q1 for products above $30k:**  
```
=AVERAGEIF(F2:F7, ">30000", F2:F7)
```
How does this compare to the overall average?

## Expected results

- AVERAGE(F2:F7): roughly $57–58k
- SUMIF above average: sum of products beating the average (should include License and Service)
- COUNTIF C2:E7 > 10000: should be 10–12 cells
- COUNTIFS (Jan AND Feb both >10k): around 4–5 products
- SUMIFS (Jan>10k AND Q1>50k): the revenue from only the top-performing products

## Solution

<details>
<summary>Reveal solution</summary>

Task 1: `=SUMIF(F2:F7,">"&AVERAGE(F2:F7),F2:F7)`

Task 2: `=COUNTIF(C2:E7,">10000")`

Task 3: `=COUNTIFS(C2:C7,">10000",D2:D7,">10000")`

Task 4: `=SUMIFS(F2:F7,C2:C7,">10000",F2:F7,">50000")`

Task 5: `=AVERAGEIF(F2:F7,">30000",F2:F7)`

The AVERAGEIF result should be notably higher than the plain AVERAGE because it excludes the low-revenue Niche products.

</details>
