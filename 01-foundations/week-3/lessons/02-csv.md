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

Next: [`03-errors.md`](03-errors.md).
