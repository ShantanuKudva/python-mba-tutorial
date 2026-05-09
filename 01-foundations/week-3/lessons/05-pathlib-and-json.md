# Lesson 5 — pathlib & JSON

Two practical tools that make file work cleaner.

---

## pathlib — modern file paths

In Lesson 1 you wrote paths as strings: `"data/sales.csv"`. That works but breaks across machines (Windows uses `\`, mac/linux use `/`), and you end up gluing strings together with `+`. **`pathlib` fixes this.**

```python
from pathlib import Path

data_dir = Path("data")
sales = data_dir / "sales.csv"        # data/sales.csv
print(sales)
```

The `/` operator joins paths the right way for your OS. No string gluing.

### Useful methods

```python
sales.exists()          # True / False
sales.is_file()
sales.suffix            # ".csv"
sales.stem              # "sales"
sales.name              # "sales.csv"
sales.parent            # Path("data")
sales.absolute()        # full path from root
```

### Listing a folder

```python
for f in Path("data").iterdir():
    print(f.name)

# Only CSV files, recursively:
for f in Path("data").rglob("*.csv"):
    print(f)
```

That last line replaces a whole nested-loop in `os.walk`. Use it.

### Reading and writing in one line

```python
text = Path("notes.md").read_text()
Path("output.txt").write_text("Q1 done\n")
```

For CSVs and Excel you'll still use `csv` (last lesson) or `pandas` (next week). But for plain text and config, `read_text` / `write_text` are the fastest path.

---

## JSON — the universal data format

JSON looks almost exactly like a Python `dict`. APIs return it. Config files use it. You'll see it everywhere.

```json
{
  "company": "Acme",
  "founded": 1947,
  "products": ["Widget", "Sprocket"],
  "active": true
}
```

### Reading JSON

```python
import json
from pathlib import Path

raw = Path("config.json").read_text()
data = json.loads(raw)        # str  → dict

print(data["company"])        # Acme
print(data["products"][0])    # Widget
```

### Writing JSON

```python
report = {
    "region": "North",
    "revenue": 1_245_000,
    "top_skus": ["WIDGET-RED", "SPROCKET-BLUE"],
}

Path("report.json").write_text(
    json.dumps(report, indent=2)
)
```

`indent=2` makes the file human-readable. Without it everything is on one line.

### dump vs dumps, load vs loads

| Function       | What it does                          |
|----------------|---------------------------------------|
| `json.dumps()` | Python object **→ string**            |
| `json.loads()` | String **→ Python object**            |
| `json.dump()`  | Python object → write to file handle  |
| `json.load()`  | Read file handle → Python object      |

The `s` is for "string". Easy to remember once you know.

---

## Putting it together

```python
import json
from pathlib import Path

# Find every report file and combine into one
reports = []
for f in Path("data/reports").rglob("*.json"):
    reports.append(json.loads(f.read_text()))

# Write the combined output next to the script
Path("combined.json").write_text(json.dumps(reports, indent=2))
print(f"Combined {len(reports)} reports.")
```

That's a real ETL micro-task in 7 lines.

---

## 🛠️ Your turn

Create `lessons/quarter_summary.json`:

```python
import json
from pathlib import Path

summary = {
    "quarter": "Q1",
    "regions": {
        "North": 1_245_000,
        "South":   980_000,
        "East":  1_410_000,
    },
    "currency": "USD",
}

# 1. Write it to disk with indent=2.
# 2. Read it back, parse with json.loads.
# 3. Print the total revenue across regions.
```

---

## Common confusions

**`json.load` vs `json.loads`** — `load` takes an already-open file, `loads` takes a string. Mixing them is the #1 JSON bug.

**JSON can't store every Python object.** `datetime`, `set`, custom classes don't serialize directly. Convert to strings/lists first.

**Quotes in JSON must be double quotes** — `'Acme'` is invalid JSON. Python's `json.dumps` handles this for you; just don't hand-edit JSON with single quotes.

**`Path("data")` does not create the folder.** If you need to make it: `Path("data").mkdir(exist_ok=True)`.

---

## 📚 Resources

**Official docs**
- [`pathlib` reference](https://docs.python.org/3/library/pathlib.html)
- [`json` reference](https://docs.python.org/3/library/json.html)

**Deep dives**
- [Real Python — `pathlib`](https://realpython.com/python-pathlib/)
- [Real Python — JSON](https://realpython.com/python-json/)

**Video tutorials**
- [YouTube — pathlib tutorial](https://www.youtube.com/results?search_query=python+pathlib+tutorial)
- [YouTube — Corey Schafer: JSON](https://www.youtube.com/results?search_query=corey+schafer+python+json)


---

Next: [`06-datetime.md`](06-datetime.md).
