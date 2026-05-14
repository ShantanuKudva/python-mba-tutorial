# Lesson 8 — IFERROR, IFS, and Conditional Aggregation

## Why this matters

Two things trip up almost every new analyst: formulas that crash with errors instead of failing gracefully, and counting or summing "only the rows that match a condition." This lesson covers both — error-handling wrappers and the conditional aggregation family (COUNTIF, SUMIF, AVERAGEIF, and their multi-criteria siblings).

## The preloaded sheet

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 340
```

---

## IFERROR — handle errors gracefully

`=IFERROR(value, value_if_error)` evaluates `value`; if it produces any error (`#N/A`, `#DIV/0!`, `#VALUE!`, etc.) it returns `value_if_error` instead.

```
=IFERROR(VLOOKUP(D2, Customers!A:F, 6, 0), "Not found")
=IFERROR(A2/B2, 0)           -- divide-by-zero safe
=IFERROR(VALUE(C2), "bad data")
```

Think of it as a try/except block in Python: you attempt an operation, and you define what to show if it blows up.

### IFNA — narrower than IFERROR

`=IFNA(value, value_if_na)` only catches `#N/A` errors — the error you get from a failed VLOOKUP or MATCH. Use it instead of IFERROR when you want other errors (like `#DIV/0!`) to surface visibly.

```
=IFNA(VLOOKUP(A2, LookupRange, 2, 0), "—")
```

---

## IF — the foundation

```
=IF(logical_test, value_if_true, value_if_false)
```

Examples with the Q1 sheet:
```
=IF(F2>50000, "Flagship", "Standard")      -- flag high-revenue products
=IF(C2>D2, "Jan beat Feb", "Feb ahead")
```

### Nested IF vs IFS

**Nested IF** stacks multiple conditions by putting another IF in the false branch — but it gets unreadable fast:
```
=IF(F2>100000,"A",IF(F2>50000,"B",IF(F2>20000,"C","D")))
```

**IFS** (Excel 2019+) is cleaner — it checks conditions in order and returns the first match:
```
=IFS(F2>100000,"A", F2>50000,"B", F2>20000,"C", TRUE,"D")
```
The trailing `TRUE,"D"` acts as the else/default.

### SWITCH — match a value to a list

`SWITCH(expression, val1, result1, val2, result2, …, [default])` is cleaner than IFS when you're matching an exact value:
```
=SWITCH(A2, "North","North Region", "East","East Region", "West","West Region", "Unknown")
```

---

## COUNTIF — count rows that match one condition

```
=COUNTIF(range, criteria)
```

```
=COUNTIF(C2:C7, ">10000")        -- how many products beat $10k in Jan
=COUNTIF(B2:B7, "License")       -- exact match
=COUNTIF(B2:B7, "L*")            -- wildcard: starts with L
```

## SUMIF — sum rows that match one condition

```
=SUMIF(range, criteria, [sum_range])
```

If `sum_range` is omitted, Excel sums the `range` itself.

```
=SUMIF(B2:B7, "License", F2:F7)     -- Q1 total for License only
=SUMIF(F2:F7, ">50000", F2:F7)      -- sum of Q1 totals above $50k
```

## AVERAGEIF — average rows that match one condition

```
=AVERAGEIF(range, criteria, [average_range])
```

```
=AVERAGEIF(B2:B7, "Hardware*", F2:F7)   -- avg Q1 revenue for "Hardware" products
```

---

## COUNTIFS / SUMIFS — multiple conditions

Add an "S" and you can pass multiple range/criteria pairs. Excel evaluates them as AND (all conditions must be true for the row to count).

```
=COUNTIFS(range1, criteria1, range2, criteria2, ...)
=SUMIFS(sum_range, range1, criteria1, range2, criteria2, ...)
```

### SUMIFS example

Suppose you have a deals sheet with Region (col A), Product (col B), and Amount (col C):

```
=SUMIFS(C2:C100, A2:A100, "North", B2:B100, "License")
-- sum amounts where region=North AND product=License
```

### COUNTIFS example

```
=COUNTIFS(A2:A100, "East", C2:C100, ">5000")
-- count East-region orders larger than $5,000
```

---

## Putting it all together: a conditional summary table

A common MBA deliverable is a table that breaks revenue down by product type and flags which rows exceed a threshold. You can build the entire thing with SUMIFS + IFERROR + IFS — no pivot table needed.

| Formula | What it does |
|---|---|
| `=SUMIFS(Amount, Region, "North", Product, "License")` | North region License revenue |
| `=IFERROR(SUMIFS(...), 0)` | Returns 0 instead of crashing on empty ranges |
| `=IFS(total>100000,"Tier 1", total>50000,"Tier 2", TRUE,"Tier 3")` | Categorise each row |

---

## Practice tasks

1. In any blank cell, count how many products had Q1 revenue above $30,000. Use `COUNTIF`.
2. Sum January revenue (column C) only for products whose name starts with the letter "L". Use `SUMIF` with a wildcard.
3. Write an `IFS` formula that categorises Q1 total (column F) as "Flagship" (>100k), "Growth" (>30k), or "Niche".
4. Wrap a `VLOOKUP` on a value that doesn't exist (e.g. `=VLOOKUP("Fridge", B2:F7, 5, 0)`) in an `IFERROR` so it shows "No data" instead of `#N/A`.
