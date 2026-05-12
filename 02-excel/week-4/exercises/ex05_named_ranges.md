# Exercise 05 — Named Ranges 🟡

**Scenario:** You're building a pricing model for the CFO. The model has two key assumptions: the target gross margin (35%) and the operating expense ratio (20%). These live in cells that will be referenced by dozens of formulas throughout the workbook. Using named ranges instead of raw cell addresses makes the model readable, auditable, and change-safe.

## The sheet (P&L)

```sheet
src: 02-excel/datasets/pnl.xlsx.json
sheet: P&L
height: 400
```

## Tasks

**Task 1 — Create a named range for Total Revenue (Q1):**  
Click on cell C4 (which contains the Q1 Total Revenue formula or value). In the **Name Box** at the top-left of the spreadsheet, click and type `Q1Revenue`, then press Enter. You've now named that cell.

**Task 2 — Use the named range in a formula:**  
In any empty cell (e.g. cell J2), type:

```
=Q1Revenue * 0.35
```

This should return 35% of Q1 total revenue — your target gross profit. Compare it to C10 (the actual gross profit).

**Task 3 — Assumptions block:**  
In cells I5:J6, build a small assumptions table:

| | I | J |
|---|---|---|
| Row 5 | Target Margin | 0.35 |
| Row 6 | OpEx Ratio | 0.20 |

Name J5 as `TargetMargin` and J6 as `OpExRatio`.

**Task 4 — Use named assumptions in formulas:**  
In cell J8, write a formula:

```
=Q1Revenue * TargetMargin
```

In cell J9, write:

```
=Q1Revenue * OpExRatio
```

These should return the target gross profit and the expected OpEx for Q1.

**Task 5 — Change an assumption, watch everything update:**  
Change J5 (TargetMargin) from `0.35` to `0.40`. What happens to J8? The formula automatically updates — that's the value of named ranges over hardcoded numbers.

## Why this matters

In a real financial model, the target margin might appear in 30 formulas across 10 sheets. If you hardcode `0.35` everywhere, changing it requires finding and replacing every instance — and one missed cell will silently break the model. Named ranges make a single source of truth.

## Solution

<details>
<summary>Reveal solution</summary>

After naming C4 as `Q1Revenue`:

- J2: `=Q1Revenue * 0.35` → 35% of Q1 Total Revenue
- J8: `=Q1Revenue * TargetMargin` → same value (when TargetMargin = 0.35)
- J9: `=Q1Revenue * OpExRatio` → 20% of Q1 Total Revenue

When you change TargetMargin to 0.40, J8 immediately updates to 40% of Q1Revenue.

</details>
