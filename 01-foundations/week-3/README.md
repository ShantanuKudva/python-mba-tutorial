# Week 3 — Files, Errors, Modules

**Goal of the week:** process structured data in memory, handle bad input gracefully, and write reusable helper functions.

By the end of the week you'll have an expense categorizer that parses CSV data, ignores junk rows, and prints a formatted summary — all in the browser playground.

## What you'll learn

- Reading and writing text/CSV files.
- `try / except` — catching errors instead of crashing.
- `import` your own files. `pip install` other people's.
- Reading documentation effectively.

## Why it matters (MBA tie-in)

In real life, data comes in messy formats: `.csv` exports from systems, partial `.xlsx` workbooks, missing fields, bad values. This week you learn how to parse that data systematically and handle surprises without crashing — a skill every analyst needs before they can automate anything.

## Map

| File | Topic |
|---|---|
| [`lessons/01-files.md`](lessons/01-files.md) | Reading and writing files |
| [`lessons/02-csv.md`](lessons/02-csv.md) | The `csv` module |
| [`lessons/03-errors.md`](lessons/03-errors.md) | `try/except`, common exceptions |
| [`lessons/04-modules.md`](lessons/04-modules.md) | `import`, `pip`, package structure |
| [`exercises/`](exercises/) | 5 problems |
| [`project.md`](project.md) | Expense categorizer |

## Checklist before week 4

- [ ] You can parse CSV data from an in-memory string, loop rows, and do something useful per row.
- [ ] You wrapped a risky operation in `try/except`.
- [ ] You called a helper function defined in the same script.
- [ ] You finished the categorizer project playground.
