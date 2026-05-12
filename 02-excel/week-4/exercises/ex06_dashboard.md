# Exercise 06 — Mini Dashboard 🔴

**Scenario:** The COO wants a single-page executive summary combining Q1 sales performance, P&L health, and customer segmentation insights. You need to pull from three different data sources and synthesize a dashboard that answers: Are we on track? Where is the risk? What's driving performance?

This is a longer exercise — budget 20–30 minutes.

## Starting sheet (Q1 Sales — your canvas)

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

## What to build

Use the sheet above as your working area. The goal is a **6-row summary block** starting around row 12 that a non-analyst could read in 30 seconds.

### Section 1 — Revenue Performance (rows 12–16)

| Row | Label | Formula / Value |
|---|---|---|
| 12 | (header) | "Q1 Revenue Summary" |
| 13 | Total Revenue | `=SUM(F2:F7)` |
| 14 | Top Product | use `=INDEX(A2:A7, MATCH(MAX(F2:F7), F2:F7, 0))` to return the name of the highest-revenue product |
| 15 | Top Product Revenue | `=MAX(F2:F7)` |
| 16 | Top Product % of Total | `=MAX(F2:F7)/SUM(F2:F7)` — format as a decimal showing 2 places |

### Section 2 — Regional Breakdown (rows 18–22)

| Row | Label | North | East | West |
|---|---|---|---|---|
| 18 | (header) | "North" | "East" | "West" |
| 19 | Q1 Total | SUMIF | SUMIF | SUMIF |
| 20 | % of Total | each SUMIF / grand total | … | … |
| 21 | # Products | COUNTIF | … | … |
| 22 | Avg per Product | AVERAGEIF | … | … |

### Section 3 — Health Check (rows 24–27)

In column A, write labels. In column B, write formulas or values.

| Row | Label | Value |
|---|---|---|
| 24 | "Products On Track (≥$30k)" | `=COUNTIF(F2:F7,">=30000")` |
| 25 | "Products Underperforming" | `=COUNTIF(F2:F7,"<15000")` |
| 26 | "Total Gap to $30k Target" | `=SUMIF(F2:F7,"<30000",F2:F7) - 30000 * COUNTIF(F2:F7,"<30000")` |
| 27 | "Best Month" | The month (Jan/Feb/Mar) with the highest total across all products. Use `=IF(SUM(C2:C7)>=SUM(D2:D7), IF(SUM(C2:C7)>=SUM(E2:E7),"Jan","Mar"), IF(SUM(D2:D7)>=SUM(E2:E7),"Feb","Mar"))` |

## Challenge: Add a data validation flag

In any empty cell, write a formula that shows `"DATA OK"` if the grand total in F8 equals `SUM(C2:C7)+SUM(D2:D7)+SUM(E2:E7)` (i.e., the column totals match the row totals). Otherwise show `"CHECK DATA"`.

```
=IF(F8=SUM(C2:E7),"DATA OK","CHECK DATA")
```

## Expected output

After completing all three sections, you should be able to answer these questions by reading your dashboard:

1. What is total Q1 revenue?
2. Which region drives the most revenue?
3. How many products are underperforming?
4. Was January, February, or March the strongest month overall?

## Solution

<details>
<summary>Reveal solution (partial — check your numbers match these)

</summary>

- Total Revenue (F8/row 13): ~$345,900 (sum of all 6 product Q1 totals)
- Top Product: License (~$143,000, ~41% of total)
- East region dominates due to License + Service both being large-ticket items
- Products on track (≥$30k): 4 (Widget, License, Service, Plugin)
- Underperforming (<$15k): 1 (Cable ~$10,500)
- Data validation: should show "DATA OK" if all formulas are correct

</details>
