"""
Exercise 7 — Running total (cumulative sum) over time.

Concepts: sort_values, cumsum, derived columns.
Lesson: lessons/04-dates.md
Difficulty: Hard
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: given a sales DataFrame, sort by date and add a `running_total`
column that accumulates revenue.

Expected output:
            date  revenue  running_total
    0 2026-01-05      300            300
    1 2026-01-09      450            750
    2 2026-01-15      120            870
    3 2026-01-22      800           1670
"""

import pandas as pd

df = pd.DataFrame({
    "date":    pd.to_datetime(
        ["2026-01-09", "2026-01-22", "2026-01-05", "2026-01-15"]
    ),
    "revenue": [450, 800, 300, 120],
})

# 🛠️ Step 1: df = df.sort_values("date").reset_index(drop=True)
# 🛠️ Step 2: df["running_total"] = df["revenue"].cumsum()
# 🛠️ Step 3: print(df)
