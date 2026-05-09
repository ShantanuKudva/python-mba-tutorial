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

## 🛠️ Try it

Run this to see set operations on customer data. Think: what does the difference set tell a marketing team?

```python
last_q = {"acme", "globex", "umbrella", "initech"}
this_q = {"acme", "stark", "umbrella"}

retained  = last_q & this_q      # in both
churned   = last_q - this_q      # left
new       = this_q - last_q      # joined this quarter

print("Retained:", retained)
print("Churned: ", churned)
print("New:     ", new)
```

---

## Common confusions

**`{}` is an empty dict, not a set.** For an empty set use `set()`.

**Tuples need a comma.** `(5)` is just the number 5 in parens. A 1-tuple is `(5,)`.

**Sets are unordered** — don't expect `print(my_set)` to come out in insertion order. If order matters, use a list and dedupe with `list(dict.fromkeys(items))`.

---

## 📚 Resources

**Official docs**
- [Tuples and sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [`set` reference](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

**Deep dives**
- [Real Python — Sets](https://realpython.com/python-sets/)

**Video tutorials**
- [YouTube — tuples vs lists](https://www.youtube.com/results?search_query=python+tuples+vs+lists+tutorial)
- [YouTube — sets explained](https://www.youtube.com/results?search_query=python+sets+tutorial)


---

Next: [exercises](../exercises/) and [project](../project.md).

---

## 🏋️ Practice

### Easy

Given two raw customer lists (with duplicates), convert them to sets and use set operations to find: all unique customers, customers in both quarters, customers who churned, and new customers this quarter. Print each group with a label.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex07_unique_skus.py)

### Medium

Given a list of sales tuples in the form `(region, quarter, revenue)`, loop through them with tuple unpacking. Print a formatted line for each row, then use a comprehension to build a list of only the revenues and compute the total and average.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex06_top_n_customers.py)

### Hard

Build a duplicate-detection tool. Given a list of order dicts (each with `"order_id"` and `"customer_id"`), find all `order_id` values that appear more than once. Also find customers who placed orders in both `"North"` and `"South"` regions. Use sets for both checks and print the results with counts.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex07_unique_skus.py)
