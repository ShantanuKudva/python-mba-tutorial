"""
Exercise 4 — A/B test on synthetic data.

Two groups of revenue-per-user. Compute means, lift %, p-value, and significance.
Use the wrapper from lesson 3.
"""

import numpy as np
from scipy import stats

rng = np.random.default_rng(42)
a = rng.normal(50, 12, size=400)   # group A
b = rng.normal(53, 12, size=400)   # group B (3-unit lift, ~6%)

# 🛠️ Compute and print: mean_a, mean_b, lift_pct, p_value, significant.
