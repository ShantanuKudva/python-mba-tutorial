# Lesson 5 — Tuples & Sets

You already know **lists** (ordered, changeable) and **dicts** (key → value). Two more collections complete the picture.

---

## Tuples — fixed records

A tuple is **like a list, but you can't change it**. Round brackets, commas inside.

```python
sale = ("North", "Q1", 12_450)
sale[0]   # "North"
sale[2]   # 12450

sale[0] = "South"   # ❌ TypeError — tuples are immutable
```

### Why bother — when lists exist?

- **Signals "this is one record"**, not a growing list. A `(region, quarter, revenue)` triple is conceptually one thing.
- **Safer**: code downstream can't accidentally mutate it.
- **Functions can return multiple values** by returning a tuple:

```python
def split_name(full):
    first, _, last = full.partition(" ")
    return first, last        # implicitly a tuple

f, l = split_name("Ada Lovelace")
print(f, l)                    # Ada Lovelace
```

That last bit is **tuple unpacking** — assigning multiple variables in one go. Used everywhere in idiomatic Python.

---

## Looping with unpacking

```python
sales = [
    ("North", "Q1", 12_450),
    ("South", "Q1",  9_300),
    ("East",  "Q1", 14_100),
]

for region, quarter, revenue in sales:
    print(f"{region} {quarter}: ${revenue:,}")
```

Cleaner than `row[0]`, `row[1]`, `row[2]`.

---

## Sets — unique values, no order

A set holds **only unique items**. Curly brackets, no key/value.

```python
regions = {"North", "South", "North", "East", "South"}
print(regions)        # {'North', 'South', 'East'}  — duplicates gone
```

### What sets are great at

**Deduping:**

```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
unique = set(emails)              # {"a@x.com", "b@x.com"}
unique_list = list(unique)        # back to a list if needed
```

**Membership checks (fast):**

```python
vip = {"acme", "globex", "initech"}
"acme" in vip          # True — instant, even with 1M entries
```

`in` on a list scans every item; `in` on a set is near-instant. For lookup-heavy code, that's the difference between 1 sec and 10 min.

**Set math:**

```python
last_month = {"acme", "globex", "umbrella"}
this_month = {"acme", "initech", "umbrella"}

last_month & this_month      # {'acme', 'umbrella'}  — kept (intersection)
this_month - last_month      # {'initech'}           — new (difference)
last_month - this_month      # {'globex'}            — churned
last_month | this_month      # union (everyone seen)
```

That's customer churn analysis in 4 lines.

---

## When to pick what

| Need                        | Use     |
|-----------------------------|---------|
| Ordered, will grow/change   | list    |
| Fixed record (one row)      | tuple   |
| Unique items, fast lookup   | set     |
| Key → value lookup          | dict    |

---

## 🛠️ Your turn

```python
# Customers who ordered last quarter and this quarter:
last_q = ["acme", "globex", "acme", "umbrella", "initech"]
this_q = ["acme", "stark", "umbrella", "umbrella"]

# 1. Print unique customers across both quarters.
# 2. Print customers who appeared in BOTH.
# 3. Print customers who churned (in last_q but not this_q).
```

---

## Common confusions

**`{}` is an empty dict, not a set.** For an empty set use `set()`.

**Tuples need a comma.** `(5)` is just the number 5 in parens. A 1-tuple is `(5,)`.

**Sets are unordered** — don't expect `print(my_set)` to come out in insertion order. If order matters, use a list and dedupe with `list(dict.fromkeys(items))`.

---

Next: [exercises](../exercises/) and [project](../project.md).
