# Lesson 1 — Reading and Writing Files

## Reading a text file

```python
with open("notes.txt") as f:
    contents = f.read()

print(contents)
```

`with open(...) as f:` is the safe pattern. Python automatically closes the file when the block ends.

Read line by line (better for large files):

```python
with open("notes.txt") as f:
    for line in f:
        print(line.rstrip())   # rstrip removes the trailing newline
```

## Writing a text file

```python
with open("output.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("Line two.\n")
```

The `"w"` mode **overwrites**. Use `"a"` to append.

## File paths

```python
from pathlib import Path

data_dir = Path("datasets")
file_path = data_dir / "expenses.csv"

print(file_path.exists())   # True / False
```

🧠 Use `pathlib` rather than string concatenation. It works on Windows and macOS without you thinking about slashes.

## Common confusions

**`FileNotFoundError`** — the path is wrong, or you're running from the wrong directory. Check `Path.cwd()` to see where Python thinks you are.

**File contents look like `\n`** — that's a newline character. `print()` interprets it. `f.write()` requires you to add it explicitly.

---

Next: [`02-csv.md`](02-csv.md).
