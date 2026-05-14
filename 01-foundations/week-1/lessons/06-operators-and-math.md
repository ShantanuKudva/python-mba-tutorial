# Lesson 6 — Operators & Math

## 🧠 The big idea

Python is a calculator that never makes rounding mistakes in your formula cell. Every Excel arithmetic operator has a Python equivalent — plus a few extra ones that are genuinely useful in business analysis.

---

## Arithmetic operators

| Operator | Meaning             | Example          | Result   |
|----------|---------------------|------------------|----------|
| `+`      | addition            | `1_200 + 350`    | `1550`   |
| `-`      | subtraction         | `9_800 - 2_100`  | `7700`   |
| `*`      | multiplication      | `150 * 9.99`     | `1498.5` |
| `/`      | division (float)    | `7 / 2`          | `3.5`    |
| `//`     | floor division (int)| `7 // 2`         | `3`      |
| `%`      | modulo (remainder)  | `7 % 2`          | `1`      |
| `**`     | exponentiation      | `1.08 ** 3`      | `1.2597…`|

```python
days_on_market = 100
weeks = days_on_market // 7      # 14  (complete weeks)
leftover_days = days_on_market % 7   # 2  (remaining days)
print(f"{days_on_market} days = {weeks} weeks and {leftover_days} days")
```

`//` and `%` are especially handy for converting totals (days → weeks, minutes → hours, units → full pallets).

---

## Comparison operators

These return `True` or `False` — the raw ingredients of every business rule.

| Operator | Meaning              |
|----------|----------------------|
| `==`     | equal to             |
| `!=`     | not equal to         |
| `<`      | less than            |
| `<=`     | less than or equal   |
| `>`      | greater than         |
| `>=`     | greater than or equal|
| `is`     | same object in memory|
| `in`     | membership test      |

```python
margin = 14.2
region = "North"
approved_regions = ["North", "South", "East"]

print(margin >= 10)           # True
print(region in approved_regions)   # True
print(region == "West")       # False
```

`in` works on lists, strings, and dictionaries — great for quick membership checks instead of a long `or` chain.

---

## Logical operators

Combine comparisons to express multi-condition rules.

```python
revenue   = 980_000
headcount = 45
is_public = False

# Qualifies for a fast-growth grant?
qualifies = revenue >= 500_000 and headcount < 50 and not is_public
print(f"Grant eligible: {qualifies}")  # True

# At least one reason to escalate?
escalate = revenue < 0 or margin < 5
print(f"Escalate: {escalate}")
```

---

## Augmented assignment

Shorthand for updating a variable in place — you'll use `+=` constantly inside loops.

```python
total_sales  = 0
total_sales += 12_400   # same as: total_sales = total_sales + 12_400
total_sales += 8_750
total_sales += 15_100
print(f"Total: ${total_sales:,}")   # $36,250

discount = 100.0
discount *= 0.90   # apply 10% discount
discount *= 0.90   # apply again
print(f"After two discounts: ${discount:.2f}")  # $81.00
```

The full set: `+=  -=  *=  /=  //=  %=  **=`

---

## Order of operations (PEMDAS)

Python follows the same precedence as mathematics and Excel.

```python
# Wrong (no parentheses):
margin_wrong = 9_800 - 8_200 / 9_800 * 100   # divides first!

# Right (parentheses make intent explicit):
revenue = 9_800
cost    = 8_200
margin_pct = (revenue - cost) / revenue * 100
print(f"Gross margin: {margin_pct:.1f}%")     # 16.3%
```

**Rule of thumb:** any time you compute a fraction or percentage, wrap the numerator in parentheses.

---

## 🛠️ Try it

Run this to see floor division and modulo in action — then try changing the inputs.

```python
total_units = 500
units_per_pallet = 48

full_pallets = total_units // units_per_pallet
leftover     = total_units % units_per_pallet

print(f"{total_units} units → {full_pallets} full pallets + {leftover} loose units")
```

---

## Common confusions

**`/` vs `//`** — `7 / 2` gives `3.5`; `7 // 2` gives `3`. Use `//` when you need a whole number result.

**`=` vs `==`** — `=` assigns, `==` compares. Using `=` inside an `if` is a `SyntaxError` in Python 3.

**`is` vs `==`** — use `==` to compare values. `is` checks identity (same object in memory) — only use it for `None` checks: `if result is None`.

**Operator precedence** — when in doubt, add parentheses. They make code clearer *and* correct.

---

## 📚 Resources

**Official docs**
- [Operator precedence table](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [Numeric types — int, float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

**Deep dives**
- [Real Python — Operators and expressions](https://realpython.com/python-operators-expressions/)
- [Real Python — The modulo operator](https://realpython.com/python-modulo-operator/)

---

Next: [`07-input-and-print.md`](07-input-and-print.md).

---

## 🏋️ Practice

### Easy

Given `total_days = 250`, compute full weeks and leftover days using `//` and `%`. Also compute compound growth: start with revenue `1_000_000` and apply 8% annual growth for 3 years using `**`. Print both results.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex13_weeks_and_growth.py)

### Medium

Given three products with `units_sold` and `unit_price`, compute revenue for each using `*`. Use `+=` to accumulate the total. Then compute each product's share of total revenue using `/`. Print a three-row table with product name, revenue, and share (as a percentage).

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex14_revenue_share.py)

### Hard

Build a shipping cost calculator. Given `total_units = 500` and `pallet_capacity = 48`, use `//` and `%` to compute full pallets and loose units. Full pallets cost $120 each; loose units ship in a partial pallet at $120 × (loose / pallet_capacity), rounded up. Use `math.ceil` for the partial pallet cost. Apply a 5% surcharge if the total order value exceeds $5,000. Print a full cost breakdown.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex15_shipping_cost.py)
