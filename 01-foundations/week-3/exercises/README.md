# Exercises — Week 3 · Files & Errors

> Practice problems for the lessons in this module. Each exercise opens directly in the browser playground — fill in the steps and click ▶ Run.
> All file-reading exercises use in-memory strings (`io.StringIO`) instead of real files, so they run identically in the browser.

## 📚 Read first

Skim these before attempting the harder exercises:
- [Lesson 01 — Files](../lessons/01-files.md)
- [Lesson 02 — CSV](../lessons/02-csv.md)
- [Lesson 03 — Errors](../lessons/03-errors.md)
- [Lesson 04 — Modules](../lessons/04-modules.md)
- [Lesson 05 — pathlib & JSON](../lessons/05-pathlib-and-json.md)
- [Lesson 06 — Dates & Times](../lessons/06-datetime.md)
- [Python official docs — csv module](https://docs.python.org/3/library/csv.html)
- [Python official docs — datetime](https://docs.python.org/3/library/datetime.html)

## 🟢 Easy

- [ex01 — Read text (in-memory)](#play/01-foundations/week-3/exercises/ex01_read_text.py) — `.splitlines()`, slicing.
- [ex02 — Count non-empty lines](#play/01-foundations/week-3/exercises/ex02_count_lines.py) — loop + string methods.
- [ex05 — Use a helper function](#play/01-foundations/week-3/exercises/ex05_module_import.py) — calling a reusable function.

## 🟡 Medium

- [ex03 — Total a CSV column](#play/01-foundations/week-3/exercises/ex03_csv_total.py) — `csv.DictReader`, `io.StringIO`, float conversion.
- [ex04 — Safe parse with try/except](#play/01-foundations/week-3/exercises/ex04_safe_parse.py) — `ValueError`, `KeyError`, error counting.
- [ex06 — Walk a file listing](#play/01-foundations/week-3/exercises/ex06_path_walk.py) — list of dicts, string methods.
- [ex07 — Build and parse JSON](#play/01-foundations/week-3/exercises/ex07_json_report.py) — `json.dumps`, `json.loads`, formatted output.
- [ex08 — Invoice date filter](#play/01-foundations/week-3/exercises/ex08_invoice_dates.py) — `datetime.strptime`, `timedelta`.

## 🔴 Hard

- [ex09 — Expense report with anomaly flags](#play/01-foundations/week-3/exercises/ex09_expense_report.py) — full CSV pipeline: parse, accumulate, flag over-limit rows, print formatted report.
