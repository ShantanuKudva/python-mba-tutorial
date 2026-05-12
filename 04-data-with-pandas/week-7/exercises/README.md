# Exercises — Week 7 · Group & Reshape

> Practice problems for the lessons in this module. Each exercise opens directly in the browser playground — fill in the steps and click ▶ Run.

## 📚 Read first

Skim these before attempting the harder exercises:
- [Lesson 01 — GroupBy](../lessons/01-groupby.md)
- [Lesson 02 — Pivot](../lessons/02-pivot.md)
- [Lesson 03 — Merge](../lessons/03-merge.md)
- [Lesson 04 — Dates](../lessons/04-dates.md)
- [Lesson 05 — Plotting](../lessons/05-plotting.md)
- [pandas official docs — GroupBy](https://pandas.pydata.org/docs/reference/groupby.html)
- [matplotlib official docs](https://matplotlib.org/stable/index.html)

## 🟢 Easy

- [ex01 — GroupBy with named aggregations](#play/04-data-with-pandas/week-7/exercises/ex01_groupby.py) — `groupby`, `.agg`, `reset_index`.
- [ex05 — Bar chart](#play/04-data-with-pandas/week-7/exercises/ex05_chart.py) — matplotlib bar chart, labels, title, `plt.show()`.
- [ex09 — Year-over-year growth](#play/04-data-with-pandas/week-7/exercises/ex09_yoy_growth.py) — `groupby`, `unstack`, derived column, percentage formatting.

## 🟡 Medium

- [ex02 — Pivot table](#play/04-data-with-pandas/week-7/exercises/ex02_pivot.py) — `pivot_table`, `fill_value`.
- [ex03 — Merge two tables](#play/04-data-with-pandas/week-7/exercises/ex03_merge.py) — `merge`, left join, order count per customer.
- [ex04 — Parse dates and monthly totals](#play/04-data-with-pandas/week-7/exercises/ex04_dates.py) — `pd.to_datetime`, `.dt.to_period`, `groupby`.
- [ex06 — Two-level groupby](#play/04-data-with-pandas/week-7/exercises/ex06_two_level_groupby.py) — `groupby` on multiple columns, named agg.

## 🔴 Hard

- [ex07 — Running total (cumsum)](#play/04-data-with-pandas/week-7/exercises/ex07_running_total.py) — `sort_values`, `cumsum`, derived column.
- [ex08 — Segment dashboard](#play/04-data-with-pandas/week-7/exercises/ex08_segment_dashboard.py) — merge, groupby, pivot, matplotlib subplots, cumulative line chart.
