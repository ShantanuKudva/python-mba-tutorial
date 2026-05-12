# Phase 2 — Excel (Week 4)

**Goal:** master the spreadsheet as an analytical tool — then understand exactly when to move beyond it.

Excel is the universal language of business. Every financial model, ops dashboard, and sales report you'll touch in your MBA runs through it. This phase teaches you the formulas, lookup patterns, and structural thinking that turn a blank workbook into a real decision tool.

> 📊 **Runs in the browser.** Every spreadsheet block on these pages is a live, editable workbook powered by x-spreadsheet + SheetJS. No Excel license. No download. No upload. Just edit a cell and see the result.

## What you'll learn

- The core formula vocabulary: `SUM`, `AVG`, `IF`, `ROUND`, `IFERROR`.
- Relative vs. absolute cell references — the one concept most analysts get wrong.
- Lookup patterns: `VLOOKUP`, `INDEX`+`MATCH`.
- Pivot-table thinking: how to aggregate and slice data without a GUI wizard.
- When Excel is the right tool — and when it breaks.

## Map

| File | Topic |
|---|---|
| Lesson 01 | [Formulas: SUM, AVG, IF, ROUND](week-4/lessons/01-formulas.md) |
| Lesson 02 | [Cell References: relative, absolute, named ranges](week-4/lessons/02-cell-references.md) |
| Lesson 03 | [Lookups: VLOOKUP / INDEX-MATCH](week-4/lessons/03-lookups.md) |
| Lesson 04 | [Pivot Thinking: aggregation without a wizard](week-4/lessons/04-pivots-and-aggregation.md) |
| Lesson 05 | [Charts: bar, line, pie basics](week-4/lessons/05-charts.md) |
| Lesson 06 | [When Excel Breaks: bridge to SQL/pandas](week-4/lessons/06-when-excel-breaks.md) |
| Exercises | [🟢 Easy → 🟡 Medium → 🔴 Hard](week-4/exercises/README.md) |
| Project | [Sales Dashboard from raw transactions](week-4/project.md) |

## The datasets

All three workbooks are pre-loaded in the embedded sheets:

- **`sales.xlsx`** — Q1 and Q2 revenue by product and region (6 products × 3 months).
- **`pnl.xlsx`** — a simplified P&L with revenue, COGS, gross profit, and EBITDA.
- **`customers.xlsx`** — a customer master list + a pricing sheet that uses `VLOOKUP`.

See [datasets/README.md](datasets/README.md) for schema details.

## Done when

- You can write `SUM`, `AVERAGE`, `IF`, and `ROUND` from scratch without looking them up.
- You know the difference between `C3` and `$C$3` — and when each matters.
- You can replace a `VLOOKUP` with `INDEX`+`MATCH` and explain why that's better.
- You have finished all 6 lessons and at least 5 of the 7 exercises.
- You can articulate (in one sentence) why you would move data from Excel to SQL.
