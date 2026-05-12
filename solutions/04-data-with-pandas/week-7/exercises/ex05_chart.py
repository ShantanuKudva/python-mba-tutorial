"""
Exercise 5 — Plot monthly revenue as a bar chart.

Concepts: matplotlib bar chart, labels, titles, plt.show().
Lesson: 04-data-with-pandas/week-7/lessons/05-plotting.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: use the monthly revenue Series below and draw a bar chart with
labeled axes and a title. The chart will appear in the playground output area.

Expected output:
    A bar chart with months on the x-axis and revenue on the y-axis.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Setup — monthly revenue data.
monthly = pd.Series(
    [9_300, 17_300, 4_100, 9_500, 7_600, 12_400, 8_200, 11_100, 9_300, 6_500],
    index=[f"2026-{m:02d}" for m in range(1, 11)],
    name="revenue",
)

fig, ax = plt.subplots(figsize=(10, 4))
monthly.plot(kind="bar", ax=ax, color="steelblue")

ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($)")
ax.set_title("Monthly Revenue — 2026")
ax.tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
