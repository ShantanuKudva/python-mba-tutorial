# Lesson 6 — Dates & Times

Every business dataset has dates: order date, hire date, invoice date, fiscal quarter. Doing date math correctly is one of those skills that immediately separates "scripting" from "real analysis".

---

## The two types you'll use

```python
from datetime import date, datetime, timedelta
```

| Type        | Holds                   | Example                            |
|-------------|-------------------------|------------------------------------|
| `date`      | year/month/day          | `date(2026, 5, 8)`                 |
| `datetime`  | date **+ time**         | `datetime(2026, 5, 8, 14, 30)`     |
| `timedelta` | a duration              | `timedelta(days=30)`               |

---

## Today, now

```python
from datetime import date, datetime

today = date.today()           # 2026-05-08
now   = datetime.now()         # 2026-05-08 14:32:11.045
```

---

## Parsing strings into dates

You almost never type dates manually — they arrive as strings from CSVs.

```python
from datetime import datetime

raw = "2026-03-15"
d = datetime.strptime(raw, "%Y-%m-%d").date()
print(d)         # 2026-03-15
```

The `%Y-%m-%d` is a **format code** describing the input. Common ones:

| Code | Means          | Example  |
|------|----------------|----------|
| `%Y` | 4-digit year   | 2026     |
| `%m` | month (01-12)  | 03       |
| `%d` | day (01-31)    | 15       |
| `%H` | hour (00-23)   | 14       |
| `%M` | minute         | 30       |
| `%B` | month name     | March    |
| `%b` | short month    | Mar      |
| `%A` | weekday name   | Sunday   |

Mismatched format → `ValueError`. The error message tells you which part failed.

---

## Formatting dates back to strings

The reverse: `strftime` ("string format time").

```python
d = date(2026, 3, 15)
d.strftime("%Y-%m-%d")        # "2026-03-15"
d.strftime("%B %d, %Y")       # "March 15, 2026"
d.strftime("%a")              # "Sun"
```

In an f-string this is even cleaner:

```python
print(f"Report date: {d:%B %Y}")    # Report date: March 2026
```

---

## Date math with `timedelta`

```python
from datetime import date, timedelta

today    = date.today()
in_30    = today + timedelta(days=30)
last_wk  = today - timedelta(weeks=1)

# How many days between two dates?
deadline = date(2026, 12, 31)
days_left = (deadline - today).days
print(f"{days_left} days until year-end.")
```

Subtracting two dates gives a `timedelta`. Adding a `timedelta` to a date gives a new date. That's the whole pattern.

---

## Pulling parts out

```python
d = date(2026, 3, 15)
d.year              # 2026
d.month             # 3
d.day               # 15
d.weekday()         # 6  (Mon=0, Sun=6)

# Quarter from a month:
quarter = (d.month - 1) // 3 + 1     # 1
print(f"Q{quarter} {d.year}")        # Q1 2026
```

---

## A real example

```python
from datetime import date, datetime, timedelta

orders = [
    {"id": 1, "date": "2026-01-12", "amount": 250},
    {"id": 2, "date": "2026-02-28", "amount": 980},
    {"id": 3, "date": "2026-03-15", "amount": 410},
    {"id": 4, "date": "2026-04-02", "amount": 175},
]

cutoff = date(2026, 3, 1)
recent = []

for o in orders:
    d = datetime.strptime(o["date"], "%Y-%m-%d").date()
    if d >= cutoff:
        recent.append(o)

print(f"{len(recent)} orders since {cutoff}.")
```

Next week with `pandas` you'll do this in **one line** — but the underlying dates work the same way.

---

## 🛠️ Your turn

```python
from datetime import date, timedelta

# 1. Print today's date in "March 15, 2026" format.
# 2. Print the date 90 days from now.
# 3. Given hire_date = date(2024, 2, 1),
#    print how many full days the employee has been with the company.
# 4. Bonus: print the quarter (Q1/Q2/Q3/Q4) of today's date.
```

---

## Common confusions

**`date` vs `datetime`** — if you don't care about hours/minutes, use `date`. Mixing them in subtraction breaks. Convert with `.date()` if needed.

**Timezones** — `datetime.now()` is **naive** (no timezone). Fine for local reports, dangerous for anything global. For timezone-aware work use `datetime.now(timezone.utc)`.

**`%Y` vs `%y`** — capital is 4-digit (2026), lowercase is 2-digit (26). Get this wrong and 1926 looks identical to 2026.

**Excel date weirdness** — Excel stores dates as numbers (days since 1900-01-01) and famously thinks 1900 was a leap year. When pandas reads Excel, it converts cleanly — but if you ever see dates off by ~2 days, that's why.

---

Done with week 3 lessons. Move to [`exercises/`](../exercises/) and the [project](../project.md).
