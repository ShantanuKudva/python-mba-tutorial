# Lesson 2 — CSV Files

CSV = comma-separated values. The lingua franca of spreadsheet exports. Python has it built-in.

## Reading rows as lists

```python
import csv

with open("expenses.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)         # consume header row
    for row in reader:
        print(row)                 # ['2025-01-04', 'Stationery', '142.50']
```

## Reading rows as dicts (preferred)

```python
import csv

with open("expenses.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["category"], row["amount"])
```

`DictReader` uses the first row as keys. Each row comes back as a dict — exactly the shape you practiced in week 2.

⚠️ All values come back as **strings**. Convert numbers explicitly:

```python
amount = float(row["amount"])
```

## Writing a CSV

```python
import csv

rows = [
    {"category": "Travel", "total": 1240.00},
    {"category": "Software", "total": 320.50},
]

with open("summary.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["category", "total"])
    writer.writeheader()
    writer.writerows(rows)
```

---

## 📚 Resources

**Official docs**
- [`csv` module](https://docs.python.org/3/library/csv.html)
- [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader)

**Deep dives**
- [Real Python — Reading & writing CSV](https://realpython.com/python-csv/)

**Video tutorials**
- [YouTube — Corey Schafer: CSV module](https://www.youtube.com/results?search_query=corey+schafer+python+csv+module)


---

Next: [`03-errors.md`](03-errors.md).

---

## 🏋️ Practice

### Easy

Open `exercises/sample_expenses.csv` with `csv.DictReader`. Print each row's `date`, `category`, and `amount` on one line. Count the total number of rows.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex03_csv_total.py)

### Medium

Read `sample_expenses.csv` and compute the total amount per category using a dict accumulator (same technique as ex08 from week 2). Print the category totals sorted by amount descending.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex03_csv_total.py)

### Hard

Read `sample_expenses.csv`, compute per-category totals, then write a summary CSV called `expense_summary.csv` with columns `category` and `total`. Make the script robust: skip rows where `amount` cannot be converted to float (catch `ValueError`) and report how many rows were skipped.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex04_safe_parse.py)
