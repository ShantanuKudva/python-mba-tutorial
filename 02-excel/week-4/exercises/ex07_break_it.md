# Exercise 07 — Break It 🔴

**Scenario:** This exercise is deliberately different. Instead of building something, you're going to *stress-test* Excel thinking — find the exact point where the tool stops being the right answer. By the end, you'll be able to explain to a hiring manager, a CFO, or a teammate exactly when to use Excel and when to reach for SQL or Python.

## Part 1 — Scale simulation (in the sheet)

The preloaded sheet has 6 rows of data. Imagine you need to repeat the same analysis on 100,000 rows of daily transaction data (one row per transaction: customer, product, region, amount, date).

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 280
```

In the sheet above, work through these thought experiments by writing your answers as text in cells in the empty area below row 10.

**Question 1 (A11):** The Q1 Total formula in F2 is `=SUM(C2:E2)`. If you had 100,000 product rows and needed a formula for each row, you'd have 100,000 formulas. What would happen to file size, open time, and recalculation speed?

Write your answer in B11: e.g. `"File size grows proportionally; recalculation on every edit; open time increases. Excel starts lagging around 100k+ formula cells."`.

**Question 2 (A12):** If five analysts all have their own copy of the Excel file, and each one makes edits, how do you reconcile their changes into one authoritative version?

Write your answer in B12.

**Question 3 (A13):** You're asked to run this exact Q1 analysis every month for the next 12 months. What manual steps would you repeat each time? What could go wrong?

Write your answer in B13.

---

## Part 2 — The SQL alternative

For each of the Excel operations below, write the SQL equivalent. You don't need to run it — just reason through it.

| Excel | SQL equivalent |
|---|---|
| `=SUM(F2:F7)` on a product column | `SELECT SUM(q1_total) FROM sales` |
| `=SUMIF(B2:B7,"North",F2:F7)` | `SELECT SUM(q1_total) FROM sales WHERE region = 'North'` |
| A pivot table with Region on rows, SUM(Q1) | `SELECT region, SUM(q1_total) FROM sales GROUP BY region` |
| A VLOOKUP joining two tables on CustomerID | `SELECT s.*, c.discount FROM sales s JOIN customers c ON s.customer_id = c.id` |

In an empty cell area, write out one more SQL equivalent for an Excel operation you've used in this week's lessons.

---

## Part 3 — The breaking point (reflection)

In any empty cell, or just in your notes, write your answer to this:

> "I would switch from Excel to SQL/Python when ___."

Fill in the blank with a specific, concrete threshold — not "when it gets big" but something like "when the data exceeds 50k rows" or "when more than one analyst needs to edit the same dataset" or "when I need to run the same analysis more than twice".

---

## Takeaway

You've now used Excel for formulas, references, lookups, aggregation, and dashboards. You also know its limits. The next three phases of this tutorial give you the tools that take over where Excel stops:

- **Phase 3 — SQL:** queries run on the database before data reaches your machine.
- **Phase 4 — pandas:** transform and reshape DataFrames with code that can be versioned, tested, and automated.
- **Phase 5 — MBA Analytics:** apply both to real business problems — finance models, marketing attribution, supply chain optimization.

Excel stays in your toolkit. It just moves from "the only tool" to "the right tool for the right job."
