# Lesson 6 — When Excel Breaks: The Bridge to SQL and pandas

## Why this matters

Excel is the right tool for tens of thousands of rows and ad-hoc analysis. It is the wrong tool when data is in the hundreds of thousands of rows, when multiple people edit the same file, when calculations need to be audited, or when you need to run the same analysis every week automatically. Knowing *when to stop reaching for Excel* is as important as knowing how to use it. This lesson gives you the specific failure modes — and maps each one to the alternative that fixes it.

## The preloaded sheet (Q1 Sales)

Work through the exercise below in the Q1 data to feel the limitations firsthand.

```sheet
src: 02-excel/datasets/sales.xlsx.json
sheet: Q1
height: 280
```

---

## Failure mode 1: Scale

Excel's row limit is 1,048,576 rows. Sounds like a lot — until you're working with:

- 3 years of daily transaction logs: ~1M rows.
- Web server event logs: 10M+ rows.
- Retail POS data for a mid-size chain: 50M rows per quarter.

Even at 100k rows, Excel becomes painfully slow to open, recalculate, and filter.

**The fix:** SQL queries that run on the database before data reaches your machine. A `SELECT ... WHERE ... GROUP BY ...` on a 500M-row table returns a 20-row summary in seconds.

---

## Failure mode 2: Version control chaos

When five analysts each email around `v3_FINAL_JAN_updated_kp_reviewed.xlsx`, the organization loses track of the truth. Which version was used in the board presentation? Did that version include last week's correction?

**The fix:** Version control (git) for code that generates the analysis. The code is human-readable, line-diffable, and reviewable. The output (a report or chart) is generated fresh every time from the same source of truth.

---

## Failure mode 3: Reproducibility

An analyst built a model last quarter. She's now on a different team. The formulas look right but two cells have hardcoded numbers and nobody knows why. Re-running the analysis for the new quarter takes three hours of detective work.

**The fix:** Python scripts or SQL queries that read from named sources, apply documented transformations, and produce the same output every time. Steps are explicit, not hidden in cell logic.

---

## Failure mode 4: Collaboration

Excel's shared editing history is clunky. Two people opening the same file at once is a mess. Merging changes from two analysts is manual and error-prone.

**The fix:** A shared database (the single source of truth) plus code reviewed in pull requests. Everyone reads the same data. Changes are proposed, reviewed, and merged — same workflow as software engineering.

---

## Failure mode 5: Automation

You want the weekly revenue report to run every Monday at 8 am and email itself to the leadership team. In Excel, that requires VBA macros, Windows Task Scheduler, and some prayers. It breaks the moment anyone renames a sheet.

**The fix:** A Python script with a cron job (or a workflow scheduler). Ten lines of code replaces a fragile macro.

---

## The right mental model

Excel, SQL, and Python are not competing tools. They are layers of a stack:

| Layer | Tool | When |
|---|---|---|
| Explore + communicate | Excel | Quick analysis, investor model, ad-hoc one-off |
| Query structured data | SQL | Data > 10k rows, joins across tables, scheduled reports |
| Transform + automate | Python/pandas | Cleaning, reshaping, machine learning, reproducible pipelines |

Most analysts use all three. The skill is knowing which layer to reach for.

---

## Tasks — feel the limits in the sheet above

1. The Q1 sheet has 6 products. Imagine it had 100,000. Click on F8 (the TOTAL formula). How would recalculating `=SUM(F2:F7)` compare to `=SUM(F2:F100001)`? The formula is the same — but at 100k rows, Excel would take seconds to recompute on every edit.

2. Look at the formula in column F. There is no record of who wrote it, when, or what business rule it encodes. Write a note in cell H2: `"Q1 Total = Jan + Feb + Mar (see team wiki for definition)"`. In a Python script, this would be a comment in the code — visible in version control forever.

3. In any empty cell, write: `=IF(F2>50000, F2*0.05, 0)` — a "high-performer bonus" formula. Now ask: where does `50000` come from? Where does `0.05` come from? These magic numbers are Excel's version of undocumented assumptions. In Python/SQL, they'd be named constants at the top of the file.

---

## Try it

Write down (in your notes or in a cell) one analytical task you've done recently where Excel started to feel slow, fragile, or hard to share. What would SQL or pandas fix about that specific pain point?

---

## What's next

You now know what Excel is, what it does well, and where it breaks. The rest of this tutorial teaches you the tools that pick up where Excel stops:

- **Phase 3 (SQL):** Query structured data at scale.
- **Phase 4 (pandas):** Transform, clean, and reshape DataFrames in Python.
- **Phase 5 (MBA Analytics):** Apply both to finance, marketing, and ops models.

---

## Resources

- [Financial Times — data journalism tools (beyond Excel)](https://www.ft.com/content/a1c94ff1-8674-4a5b-a576-7c1a3ec97c4f)
- [Mode Analytics — Excel vs SQL for analysis](https://mode.com/blog/sql-vs-excel/)
- [Towards Data Science — when to use pandas instead of Excel](https://towardsdatascience.com/how-to-replace-excel-with-python-and-pandas-7e2c8bfa4db6)
