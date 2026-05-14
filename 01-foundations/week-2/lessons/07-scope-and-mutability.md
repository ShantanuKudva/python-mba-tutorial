# Lesson 7 — Scope and Mutability

## Variable scope

A variable's **scope** is the part of the program that can see it. Python uses the **LEGB** rule: Local → Enclosing → Global → Built-in.

```python
TAX_RATE = 0.18          # global — visible everywhere in this file

def calculate_total(subtotal):
    tax = subtotal * TAX_RATE   # local 'tax'; reads global TAX_RATE
    return subtotal + tax

print(calculate_total(100))    # 118.0
# print(tax)                   # NameError — 'tax' only lives inside the function
```

Variables created inside a function die when the function returns. This is usually what you want — functions stay self-contained.

---

## `global` and `nonlocal` (brief)

You can reach up and modify a global from inside a function with the `global` keyword. In practice, **avoid this** — it makes code hard to test and reason about. Pass values in as arguments and return new values instead.

```python
call_count = 0   # global counter

def process_order(order):
    global call_count
    call_count += 1
    return order["amount"] * 1.18

# Better pattern: return the count from the function or use a class.
```

`nonlocal` works the same way but targets the enclosing function's scope in nested functions. You will rarely need it; just know the word exists.

---

## Mutable vs immutable

The most important rule in Python:

| Type | Mutable? | Example |
|------|----------|---------|
| `int`, `float`, `bool` | No | `price = 9.99` |
| `str` | No | `"hello"` |
| `tuple` | No | `(1, 2, 3)` |
| `list` | **Yes** | `[1, 2, 3]` |
| `dict` | **Yes** | `{"a": 1}` |
| `set` | **Yes** | `{1, 2, 3}` |

**Immutable** means the value cannot change in-place; a new object is created.

```python
name = "acme"
name.upper()        # returns "ACME" — does NOT change 'name'
print(name)         # still "acme"

name = name.upper() # NOW 'name' points to a new string "ACME"
print(name)         # ACME
```

**Mutable** means the value can change in-place — and that can surprise you.

```python
prices = [10, 20, 30]
copy   = prices        # NOT a copy — both names point to the same list

copy.append(40)
print(prices)          # [10, 20, 30, 40]  ← prices changed too!

# Real copy:
safe_copy = prices.copy()    # or list(prices) or prices[:]
```

---

## The mutable default argument trap

This is one of the most common Python bugs — default mutable arguments are shared across all calls.

```python
# WRONG — the list is created once and reused:
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("Pen"))      # ['Pen']
print(add_item("Notebook")) # ['Pen', 'Notebook']  ← oops, carried over!

# CORRECT — use None as the default:
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_item("Pen"))      # ['Pen']
print(add_item("Notebook")) # ['Notebook']   ← fresh list each time
```

Always use `None` as the default when the parameter is a list, dict, or set.

---

## 🛠️ Try it

Run this to see mutability in action. Notice that `update_prices` modifies the list in-place, so the caller's list also changes. Then switch to the version that returns a new list and compare.

```python
def update_prices(price_list, markup=0.10):
    """Adds markup in-place — mutates the original list."""
    for i in range(len(price_list)):
        price_list[i] = round(price_list[i] * (1 + markup), 2)

catalog_prices = [9.99, 14.50, 7.00]
update_prices(catalog_prices)
print(catalog_prices)   # [10.99, 15.95, 7.7]  — original changed!

# Safer version — returns a new list:
def updated_prices(price_list, markup=0.10):
    return [round(p * (1 + markup), 2) for p in price_list]

catalog_prices = [9.99, 14.50, 7.00]
new_prices = updated_prices(catalog_prices)
print(catalog_prices)   # [9.99, 14.5, 7.0]    — unchanged
print(new_prices)       # [10.99, 15.95, 7.7]
```

---

## Common confusions

**Strings look mutable but aren't.** Every string method (`upper`, `strip`, `replace`) returns a new string. You must assign the result.

**`is` vs `==`** — `==` compares values; `is` compares identity (same object in memory). Two separate lists with identical content are `==` but not `is`.

**Copies are shallow by default.** `list.copy()` and `dict.copy()` copy the container but not nested objects inside it. For deeply nested structures, use `copy.deepcopy()`.

---

## 📚 Resources

**Official docs**
- [Python scopes and namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [Python data model — objects and types](https://docs.python.org/3/reference/datamodel.html)

**Deep dives**
- [Real Python — Mutable vs Immutable](https://realpython.com/python-mutable-vs-immutable-types/)
- [Real Python — Python scope](https://realpython.com/python-scope-legb-rule/)

---

Next: [`08-args-and-unpacking.md`](08-args-and-unpacking.md).

---

## 🏋️ Practice

### Easy

Write a function `apply_markup(prices, rate=0.15)` that uses `None` as the default for a result list, builds a new list with the marked-up prices, and returns it. Call it with the default rate, then with `rate=0.25`. Confirm that the original prices list is not modified.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex16_markup_safe.py)

### Medium

Write a function `region_totals(orders)` where `orders` is a list of `(region, amount)` tuples. The function must build a fresh dict internally (not a mutable default) and return it. Then write a second function `top_region(totals)` that returns the region name with the highest total. Test with orders spanning four regions.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex17_scope_regions.py)

### Hard

Demonstrate the mutable default bug: write a function `record_sale(amount, ledger=[])` that appends to the default list, call it three times, and print what `ledger` contains — showing the shared-state problem. Then fix it with `ledger=None`, write a wrapper `make_ledger()` that owns a private list and exposes `record(amount)` and `total()` methods (using a closure or a class). Call `record` four times and print the running total after each call.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex18_mutable_default.py)
