"""
Exercise 1 — 5-year revenue model.

Concepts: function definition, loops, compounding growth.
Lesson: 05-mba-analytics/strategy/lessons/01-scenarios.md
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

# 🛠️ Step 1: define revenue_5y(starting_units, price, growth_rate, churn_rate).
#    Loop from t=1 to t=5. Each year, compute units and year revenue.

# 🛠️ Step 2: print each year's revenue inside the loop.
#    print(f"Year {t} revenue: ${year_rev:,.0f}")

# 🛠️ Step 3: accumulate the total and print it after the loop.
#    print(f"5-year total: ${total:,.0f}")

# 🛠️ Step 4: call revenue_5y with the parameters above.
