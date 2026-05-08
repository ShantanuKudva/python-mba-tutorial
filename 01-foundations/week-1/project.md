# Week 1 Project — Break-even Calculator (CLI)

## What you're building

A command-line tool that asks for three numbers, computes the break-even point, and tells the user whether their business is viable.

## The math

```
Break-even units = Fixed Costs / (Price per Unit − Variable Cost per Unit)
```

The denominator is the **contribution margin per unit**. If it's zero or negative, there is no break-even point and you should say so.

## Spec

When run, your program should:

1. Ask the user for **fixed costs**.
2. Ask for **price per unit**.
3. Ask for **variable cost per unit**.
4. Compute and print:
   - Contribution margin per unit.
   - Break-even units (rounded up to the next whole unit).
   - Break-even revenue (units × price).
   - A verdict line based on contribution margin.

### Example session

```
Fixed costs ($): 50000
Price per unit ($): 25
Variable cost per unit ($): 15

Contribution margin per unit: $10.00
Break-even units: 5,000
Break-even revenue: $125,000.00
Verdict: Viable — each unit contributes $10.00 toward fixed costs.
```

If contribution margin is ≤ 0:

```
Verdict: NOT VIABLE — variable cost is at or above price. Lower cost or raise price.
```

## How to read user input

```python
fixed_costs = float(input("Fixed costs ($): "))
```

`input(...)` always returns a **string** — wrap it in `float(...)` so you can do math.

## Hints (in order — read only when stuck)

1. Build the calculator with **hard-coded values first**. Once the math is right, replace those with `input(...)` calls.
2. Use `import math` and `math.ceil(x)` to round up to the next whole unit.
3. Use `:,.2f` in your f-strings for the dollar formatting.

## File to create

`01-foundations/week-1/breakeven.py`

## Done when

- It runs without errors on viable and non-viable inputs.
- The verdict line correctly distinguishes the two cases.
- You committed the code.

🛠️ Stretch: handle the case where the user types something that isn't a number (use `try/except` — week 3 preview).
