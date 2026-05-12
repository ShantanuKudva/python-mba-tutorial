# Exercise 04 — Pivot Thinking 🟡

**Scenario:** The CFO wants a one-page regional performance summary for the Q1 board pack. She needs: total Q1 revenue by region, the average Q1 revenue per product within each region, and a flag on any region where average product revenue is below $25,000. Build this with `SUMIF`, `AVERAGEIF`, and `IF` — no pivot table wizard required.

## The sheet (Q1 Sales)

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

## Tasks

Start in cell A12 and build a summary table.

**Task 1 — Labels (A12:D12):**  
Type these column headers: `Region`, `Q1 Total`, `Avg per Product`, `Flag`.

**Task 2 — Region rows (A13:A15):**  
Type the three regions in A13, A14, A15: `North`, `East`, `West`.

**Task 3 — Q1 Total by region (B13:B15):**  
In B13, write:

```
=SUMIF($B$2:$B$7, A13, $F$2:$F$7)
```

Copy this formula down to B14 and B15. The absolute references (`$`) keep the ranges fixed while A13 shifts to A14 and A15.

Sense-check: B13+B14+B15 should equal F8 (the grand total).

**Task 4 — Average per product (C13:C15):**  
In C13, write:

```
=AVERAGEIF($B$2:$B$7, A13, $F$2:$F$7)
```

Copy down to C14 and C15.

**Task 5 — Flag low-performing regions (D13:D15):**  
In D13, write:

```
=IF(C13 < 25000, "Review needed", "OK")
```

Copy down.

**Task 6 — Grand total check:**  
In B16, write `=SUM(B13:B15)`. Confirm it matches F8 exactly. If it doesn't, recheck your SUMIF ranges.

## Expected results

- North: 2 products (Widget + Gadget) → relatively low total
- East: 2 products (License + Service) → highest total by far
- West: 2 products (Cable + Plugin) → moderate total
- The "Flag" column should mark North as "Review needed" (average below $25k per product)

## Solution

<details>
<summary>Reveal solution</summary>

B13: `=SUMIF($B$2:$B$7,A13,$F$2:$F$7)`

Q1 totals by region:
- North: Widget ($37,300) + Gadget ($26,600) = $63,900 → Avg $31,950 → OK
- East: License ($143,000) + Service ($69,500) = $212,500 → Avg $106,250 → OK
- West: Cable ($10,500) + Plugin ($58,500) = $69,000 → Avg $34,500 → OK

*(Exact values depend on whether Q1 Total formulas in F2:F7 are correctly computing SUM of C:E.)*

If any region has avg < $25k, that's flagged. Adjust the threshold in the IF formula to see different results.

</details>
