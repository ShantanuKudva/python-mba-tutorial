# Week 1 Project — Break-even Calculator

## What you're building

A break-even calculator that asks for three numbers, computes the break-even point, and tells you whether the business is viable.

## The math

```
Break-even units = Fixed Costs / (Price per Unit − Variable Cost per Unit)
```

The denominator is the **contribution margin per unit**. If it is zero or negative, there is no break-even point.

## Spec

Your playground should:

1. Ask the user for **fixed costs** (using `input()`).
2. Ask for **price per unit**.
3. Ask for **variable cost per unit**.
4. Compute and print:
   - Contribution margin per unit.
   - Break-even units (rounded up to the next whole unit using `math.ceil`).
   - Break-even revenue (units × price).
   - A verdict line based on contribution margin.

### Example output

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

## Hints

1. Build the calculator with hard-coded values first. Once the math is right, replace those values with `input()` calls.
2. Use `import math` and `math.ceil(x)` to round up to the next whole unit.
3. Use `:,.2f` in your f-strings for dollar formatting.

## Done when

- The output matches the format above for viable and non-viable inputs.
- The verdict line correctly distinguishes the two cases.

**Stretch:** wrap the `input()` calls in `try/except ValueError` so a non-numeric entry prints a friendly error instead of crashing.

[▶ Open project playground](#play/01-foundations/week-1/project.py)
