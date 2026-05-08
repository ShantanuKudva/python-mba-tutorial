# Lesson 4 — Modules and `import`

## Importing standard library

Already met:

```python
import csv
from pathlib import Path
import math
```

Anything in the [Python standard library](https://docs.python.org/3/library/) is available without installing.

## Installing third-party packages

```bash
pip install pandas
```

Then in code:

```python
import pandas as pd
```

`as pd` is a common alias. Conventional aliases (memorize):

| Package | Alias |
|---|---|
| `pandas` | `pd` |
| `numpy` | `np` |
| `matplotlib.pyplot` | `plt` |

## `requirements.txt`

A text file listing what your project needs. Anyone can recreate your environment with:

```bash
pip install -r requirements.txt
```

Generate one for your current environment:

```bash
pip freeze > requirements.txt
```

🧠 In real projects, **always** keep a `requirements.txt`. Otherwise no one (including future you) can run your code.

## Importing your own files

If you have:

```
my_project/
├── helpers.py
└── main.py
```

In `helpers.py`:

```python
def gross_margin(rev, cost):
    return (rev - cost) / rev * 100
```

In `main.py`:

```python
from helpers import gross_margin

print(gross_margin(1000, 750))
```

## The `if __name__ == "__main__":` pattern

```python
def main():
    print("running directly")

if __name__ == "__main__":
    main()
```

Means: "only run this if the file is executed directly, not when it's imported by another file." You'll see this in well-organized Python code. Adopt the habit.

---

Next: [`05-pathlib-and-json.md`](05-pathlib-and-json.md).
