"""
Exercise 4 — A/B test on conversion data.

Concepts: scipy.stats.ttest_ind, p-value, statistical significance.
Lesson: 05-mba-analytics/marketing/lessons/03-ab-test.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: run a two-sample t-test on two synthetic groups.
Print means, lift %, p-value, and a clear significance verdict.

Expected output (approximate):
    Mean A      :  50.1
    Mean B      :  52.9
    Lift        : +5.6%
    p-value     :  0.0023
    Significant : True (at α = 0.05)
"""

import numpy as np
from scipy import stats

# Setup — two synthetic customer groups (e.g., weekly revenue per customer).
rng = np.random.default_rng(42)
a = rng.normal(50, 12, size=400)   # control group
b = rng.normal(53, 12, size=400)   # treatment group (3-unit lift)

mean_a = a.mean()
mean_b = b.mean()

lift_pct = (mean_b - mean_a) / mean_a

t_stat, p_value = stats.ttest_ind(a, b)

significant = p_value < 0.05

print(f"Mean A      : {mean_a:>6.1f}")
print(f"Mean B      : {mean_b:>6.1f}")
print(f"Lift        : {lift_pct:>+6.1%}")
print(f"p-value     : {p_value:>6.4f}")
print(f"Significant : {significant} (at α = 0.05)")
