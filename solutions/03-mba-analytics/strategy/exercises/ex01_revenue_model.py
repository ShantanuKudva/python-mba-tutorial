"""
Exercise 1 — 5-year revenue model.

Concepts: function definition, loops, compounding growth.
Lesson: 03-mba-analytics/strategy/lessons/01-scenarios.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: implement revenue_5y and verify it with the base-case parameters below.

Formula for year t (starting from t=1):
    units_t     = starting_units * (1 + growth_rate - churn_rate) ** t
    revenue_t   = units_t * price
    total       = sum(revenue_t for t in 1..5)

Expected output (approximate):
    Year 1 revenue: $2,400,000
    Year 2 revenue: $2,592,000
    ...
    5-year total:   $12,674,506
"""

# Setup — base-case parameters.
starting_units = 1_000
price          = 2_400   # $ per unit per year
growth_rate    = 0.12    # 12% new customer growth
churn_rate     = 0.05    # 5% annual churn

def revenue_5y(starting_units, price, growth_rate, churn_rate):
    total = 0.0
    for t in range(1, 6):
        units_t = starting_units * (1 + growth_rate - churn_rate) ** t
        year_rev = units_t * price
        print(f"Year {t} revenue: ${year_rev:,.0f}")
        total += year_rev
    print(f"5-year total:   ${total:,.0f}")
    return total

revenue_5y(starting_units, price, growth_rate, churn_rate)
