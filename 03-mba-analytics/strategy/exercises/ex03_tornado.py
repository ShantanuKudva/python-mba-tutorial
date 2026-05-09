"""
Exercise 3 — Tornado chart.

Build sensitivity DataFrame for ±20% on each input.
Save tornado.png next to this script.
Print the sensitivity table sorted by abs_swing.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

HERE = Path(__file__).parent

# 🛠️ Reuse revenue_5y. Build the sensitivity DataFrame.
# 🛠️ Print it.
# 🛠️ Save tornado.png to HERE / "tornado.png".
