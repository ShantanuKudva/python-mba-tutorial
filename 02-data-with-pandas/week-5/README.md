# Week 5 — Aggregations + Plotting

**Goal:** turn raw transactions into grouped summaries and a chart.

## What you'll learn

- `groupby` — Excel pivot tables, but scriptable.
- `pivot_table` — when you need rows × columns × values.
- `merge` / `join` — combine two DataFrames.
- `to_datetime` and `.resample(...)` for time series.
- `matplotlib` basics — bar, line, save to PNG.

## Map

| File | Topic |
|---|---|
| [`lessons/01-groupby.md`](lessons/01-groupby.md) | groupby + agg |
| [`lessons/02-pivot.md`](lessons/02-pivot.md) | Pivot tables |
| [`lessons/03-merge.md`](lessons/03-merge.md) | merge / join |
| [`lessons/04-dates.md`](lessons/04-dates.md) | Dates and resampling |
| [`lessons/05-plotting.md`](lessons/05-plotting.md) | matplotlib basics |
| [`exercises/`](exercises/) | 5 problems |
| [`project.md`](project.md) | Multi-sheet → consolidated dashboard |

## Checklist before week 6

- [ ] You can `groupby(col).agg(...)` without looking it up.
- [ ] You merged two DataFrames on a key.
- [ ] You parsed a date column with `pd.to_datetime`.
- [ ] You produced a chart and saved it to a `.png`.
