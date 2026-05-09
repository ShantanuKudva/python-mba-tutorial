# Lesson 4 — Strings & f-strings

## 🧠 The big idea

Half of business data is text: customer names, SKUs, region codes, email addresses. You need to **clean it, slice it, combine it, and format it for reports**. That's what strings are for.

---

## A string is a sequence of characters

```python
name = "Acme Corporation"
sku  = "WIDGET-2026-RED"
```

You can ask Python questions about it:

```python
len(name)              # 16  — how many characters
name.upper()           # "ACME CORPORATION"
name.lower()           # "acme corporation"
name.startswith("Ac")  # True
sku.endswith("RED")    # True
"Corp" in name         # True
```

---

## Slicing — grab part of a string

Python counts from **0**.

```python
sku = "WIDGET-2026-RED"
sku[0]      # "W"
sku[0:6]    # "WIDGET"
sku[7:11]   # "2026"
sku[-3:]    # "RED"   (last 3 chars)
```

Excel parallel: `LEFT`, `RIGHT`, `MID`. Python's slice does all three with `[start:stop]`.

---

## Cleaning messy text

Real data has trailing spaces, mixed case, extra symbols.

```python
raw = "  ACME corp.  "
clean = raw.strip()              # "ACME corp."
clean = clean.replace(".", "")   # "ACME corp"
clean = clean.title()            # "Acme Corp"
```

Each method **returns a new string** — the original stays the same. Reassign if you want to keep the change.

---

## Splitting and joining

```python
row = "north,Q1,12450"
parts = row.split(",")           # ["north", "Q1", "12450"]
parts[0]                         # "north"

regions = ["north", "south", "east"]
",".join(regions)                # "north,south,east"
```

You'll use `split` constantly when reading text files (Week 3).

---

## f-strings — the modern way to build text

This is the single most useful pattern in Python:

```python
revenue = 1_245_000
region  = "North"
margin  = 0.184

print(f"{region} region: ${revenue:,.0f} at {margin:.1%} margin")
# North region: $1,245,000 at 18.4% margin
```

Inside `f"..."`, anything in `{ }` is **evaluated as Python**. The `:,.0f` and `:.1%` are **format specifiers**:

| Spec       | Effect                | Example         |
|------------|-----------------------|-----------------|
| `:,`       | thousands separator   | `1,245,000`     |
| `:.2f`     | 2 decimal places      | `1245000.00`    |
| `:,.0f`    | combined              | `1,245,000`     |
| `:.1%`     | percent, 1 decimal    | `18.4%`         |
| `:>10`     | right-align in 10 cols| `␣␣␣␣␣␣Acme`    |
| `:<10`     | left-align            | `Acme␣␣␣␣␣␣`    |

This replaces Excel's `TEXT()` function — and it's faster to type once you have it.

---

## 🛠️ Try it

Run this and confirm the output. Try feeding in different `raw` strings with extra spaces or mixed case.

```python
raw = "  ACME corp.  "
clean = raw.strip()
clean = clean.replace(".", "")
clean = clean.title()
print(clean)   # Acme Corp
```

---

## Common confusions

**`name.upper` vs `name.upper()`** — without parens you got the *method itself*, not the result. Always call with `()`.

**Methods don't change the original** — `name.upper()` returns a new string. If you want to keep it, do `name = name.upper()`.

**Mixing quotes** — `"It's fine"` works. `'It's fine'` breaks (the apostrophe ends the string). Use double quotes when text contains apostrophes.

**`f"{x}"` vs `"{x}"`** — without the leading `f`, Python prints the literal `{x}`, not the value.

---

## 📚 Resources

**Official docs**
- [`str` methods reference](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Format spec mini-language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
- [PEP 498 — formatted string literals](https://peps.python.org/pep-0498/)

**Deep dives**
- [Real Python — f-strings](https://realpython.com/python-f-strings/)
- [Real Python — string methods](https://realpython.com/python-strings/)

**Video tutorials**
- [YouTube — Corey Schafer: strings](https://www.youtube.com/results?search_query=corey+schafer+python+strings)
- [YouTube — f-strings deep dive](https://www.youtube.com/results?search_query=python+f-strings+tutorial)


---

Next: that's all of week 1's lessons. Head to the [exercises](../exercises/) and [project](../project.md).

---

## 🏋️ Practice

### Easy

Clean the string `"  ACME Industries, LLC.  "` by stripping whitespace, removing the trailing period, and applying `.title()`. Print the result.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex06_clean_customer.py)

### Medium

Given the SKU string `"WIDGET-2026-RED"`, use slicing and `.split()` to extract the product category (`"WIDGET"`), year (`"2026"`), and colour (`"RED"`). Print each on its own line.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex07_sku_parts.py)

### Hard

Build a formatted two-line report from a messy CSV row string `"  north , Q1 , 1245000.00  "`. Parse it with `.strip()` and `.split(",")`, convert the amount to a float, then print:
```
Region  : North
Revenue : $1,245,000.00
```
Handle leading and trailing whitespace in every field before displaying.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex08_growth_rate.py)
