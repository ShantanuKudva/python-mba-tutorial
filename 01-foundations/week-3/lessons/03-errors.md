# Lesson 3 — Errors and `try/except`

## The big idea

When something can fail, wrap it. If it fails, react instead of crashing.

```python
amount_str = "twelve"
try:
    amount = float(amount_str)
except ValueError:
    print(f"Skipping bad value: {amount_str}")
    amount = 0
```

## The shape

```python
try:
    # risky thing
except SomeError:
    # what to do if that error happens
except AnotherError as exc:
    # exc has details about the error
finally:
    # always runs, error or not (rare)
```

## Common errors you'll meet

| Exception | Meaning |
|---|---|
| `ValueError` | A value is the right type but wrong content (e.g., `int("abc")`). |
| `TypeError` | Wrong type — e.g., adding a string to a number. |
| `KeyError` | Asked a dict for a key that's not there. |
| `IndexError` | Asked a list for an index out of range. |
| `FileNotFoundError` | Path doesn't exist. |
| `ZeroDivisionError` | Divided by zero. |

## When NOT to catch errors

Don't catch them just to silence them. If you don't know how to react, **let it crash** — the traceback is information.

```python
# BAD
try:
    do_something()
except Exception:
    pass   # swallowed silently → impossible to debug
```

## Real-world pattern

```python
import csv

bad_rows = 0
total = 0.0

with open("expenses.csv", newline="") as f:
    for row in csv.DictReader(f):
        try:
            total += float(row["amount"])
        except (ValueError, KeyError):
            bad_rows += 1

print(f"Total: ${total:,.2f}   (skipped {bad_rows} bad rows)")
```

This is exactly how production scripts handle dirty data.

---

## 📚 Resources

**Official docs**
- [Tutorial — errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in exceptions](https://docs.python.org/3/library/exceptions.html)

**Deep dives**
- [Real Python — Exceptions](https://realpython.com/python-exceptions/)

**Video tutorials**
- [YouTube — Corey Schafer: exceptions](https://www.youtube.com/results?search_query=corey+schafer+python+exceptions)


---

Next: [`04-modules.md`](04-modules.md).

---

## 🏋️ Practice

### Easy

Write a small script that tries to convert each item in `["100", "abc", "250", "", "75"]` to a float. Wrap the conversion in `try/except ValueError`. Accumulate valid values in one list and invalid ones in another, then print both.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex04_safe_parse.py)

### Medium

Open `sample_expenses.csv` and accumulate amounts with `try/except (ValueError, KeyError)`. Track skipped rows with a counter. After reading all rows, print the total, the count of valid rows, and the count of skipped rows.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex04_safe_parse.py)

### Hard

Write a function `safe_load(path)` that opens a CSV file and returns a list of dicts. It must: (a) raise `FileNotFoundError` with a helpful message if the file is missing, (b) skip rows where any numeric column is invalid (catching `ValueError`), (c) return a tuple `(rows, skipped_count)`. Write a second function that calls `safe_load` and prints a formatted summary.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex03_csv_total.py)
