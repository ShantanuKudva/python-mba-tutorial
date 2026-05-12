# Phase 4 — Data with pandas (Weeks 6–7)

Two weeks where Python finally meets Excel.

pandas is the tool every analyst uses to read, clean, slice, and reshape tabular data. By the end of these two weeks, anything you'd do in Excel by hand you'll do in five lines of Python — repeatable, auditable, and fast.

## Map

| Week | Topic | Open |
|---|---|---|
| 6 | DataFrames, reading/writing Excel, filtering, missing data | [Week 6 overview](week-6/README.md) |
| 7 | groupby, pivot, merge, dates, plotting | [Week 7 overview](week-7/README.md) |

## What you'll be able to do after Phase 4

- Load any `.xlsx` or CSV (in-browser via `io.BytesIO` / `io.StringIO`).
- Clean missing data, fix dtypes, rename columns.
- Group, aggregate, pivot, and merge tables.
- Produce a chart and write the cleaned data back out as an Excel file.

This is the bread-and-butter skill set. You'll keep using it every week from here on.

## Browser note

pandas, numpy, openpyxl, and matplotlib all run inside the playground via Pyodide. The first cell that imports pandas takes a few seconds to fetch the package; subsequent cells are instant. Exercises that "read a file" use an in-memory string (`io.StringIO`) so you don't need a real filesystem.

## How to study

1. Open the week's overview from the table above.
2. Work through the lessons in order — every code block is a runnable editor.
3. Exercises: 🟢 Easy → 🟡 Medium → 🔴 Hard.
4. Finish the week's project.
5. Click **Mark as complete** on every page.

## Done with Phase 4 when

- You can load a workbook, drop noisy rows, fill or remove missing values, and write a clean copy back out.
- You can answer "revenue by region by quarter" in a single groupby.
- You can merge a transactions table with a customer master table without losing rows by accident.
- You finished both weekly projects.
