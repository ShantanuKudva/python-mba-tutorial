# Lesson 4 — Pivot Thinking: Aggregation Without a Wizard

## Why this matters

A pivot table is Excel's most powerful feature — and the one that transfers most directly to SQL `GROUP BY` and pandas `groupby`. But many analysts treat it as a GUI wizard they click through without understanding. This lesson teaches you the underlying mental model: **group rows by a dimension, then aggregate a metric**. Once you own that model, you can build it with formulas, with a pivot table, with SQL, or with Python — depending on which tool fits the job.

## The preloaded sheet (Q1 Sales)

The Q1 sales data has six products across three regions. In a real pivot table, you'd drag Region to rows and Product to columns. Here, we'll replicate that aggregation with formulas.

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

## The pivot mental model

Every aggregation answers the same question:

> For each unique value of [dimension], compute [aggregate] of [metric].

| Plain English | SQL | Excel formula |
|---|---|---|
| Total Q1 revenue by Region | `GROUP BY region, SUM(q1_total)` | `SUMIF(region_col, "North", total_col)` |
| Average Q1 by Product | `GROUP BY product, AVG(q1_total)` | `AVERAGEIF(product_col, "Widget", total_col)` |
| Count of products per Region | `GROUP BY region, COUNT(*)` | `COUNTIF(region_col, "North")` |

## SUMIF — conditional sum

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
```

```
=SUMIF(range, criteria, sum_range)
```

- `range` — the column you're grouping by (e.g. Region column B).
- `criteria` — the value you're matching (e.g. `"North"`).
- `sum_range` — the column to add up (e.g. Q1 Total column F).

Example, total Q1 revenue for North region:

```
=SUMIF(B2:B7, "North", F2:F7)
```

## AVERAGEIF and COUNTIF

Same syntax as `SUMIF`:

```
=AVERAGEIF(B2:B7, "North", F2:F7)    ← average Q1 total for North products
=COUNTIF(B2:B7, "North")             ← how many North products
```

## SUMIFS — multiple conditions

When you need to filter by more than one dimension (e.g. North region AND Hardware category):

```
=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)
```

Note: `SUMIFS` puts the `sum_range` first, unlike `SUMIF`. Easy to mix up.

---

## Build a summary table in the sheet above

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
```

In the empty area below the data (around row 12), build a Region summary:

| | North | East | West |
|---|---|---|---|
| Q1 Total Revenue | `=SUMIF(B2:B7,"North",F2:F7)` | `=SUMIF(B2:B7,"East",F2:F7)` | `=SUMIF(B2:B7,"West",F2:F7)` |
| # of Products | `=COUNTIF(B2:B7,"North")` | … | … |
| Avg Q1 per Product | `=AVERAGEIF(B2:B7,"North",F2:F7)` | … | … |

## Tasks

1. **Type labels** in cells A12:A14 — "Q1 Total Revenue", "# of Products", "Avg Q1 per Product".
2. **B12:** `=SUMIF(B2:B7,"North",F2:F7)`  
   **C12:** `=SUMIF(B2:B7,"East",F2:F7)`  
   **D12:** `=SUMIF(B2:B7,"West",F2:F7)`
3. Fill in B13:D13 with `COUNTIF` and B14:D14 with `AVERAGEIF`.
4. **Sense-check:** B12+C12+D12 should equal the grand total in F8. Write that check in E12 as `=B12+C12+D12-F8`. If E12 shows `0`, your totals are consistent.

---

## Pivot vs formula: when to use each

| Pivot table | SUMIF / SUMIFS formula |
|---|---|
| Exploring data interactively | Results must update automatically as data changes |
| Many dimensions to slice quickly | Specific known aggregations that live in a model |
| One-off analysis | Part of a structured dashboard |
| Source data refreshes from a query | Formula-based dashboards with named ranges |

The formula approach is also portable: the same logic becomes `GROUP BY` in SQL and `.groupby()` in pandas.

---

## Try it

In the sheet above, write a `SUMIF` that totals Q1 revenue for just the products in the **West** region. Then write a `SUMIFS` that totals Q1 revenue for West region products whose Q1 Total (column F) is greater than 20 000. Which products qualify?

---

Next: [Lesson 5 — Charts](05-charts.md)

---

## Resources

- [Microsoft — SUMIF](https://support.microsoft.com/en-us/office/sumif-function-169b8c99-c05c-4483-a712-1697a653039b)
- [Microsoft — PivotTable overview](https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576)
- [Chandoo.org — SUMIF vs pivot table](https://chandoo.org/wp/sumif-vs-pivot-tables/)
