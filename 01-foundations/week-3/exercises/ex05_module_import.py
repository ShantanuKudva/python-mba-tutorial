"""
Exercise 5 — Import a helper.

There's a `helpers.py` next to this file with a function `format_currency`.

🛠️ Import it. Use it to format three numbers (try 1234.5, 0, 9999999.99).

If the import fails, you're probably running the file from the wrong directory.
Run it as:
    python 01-foundations/week-3/exercises/ex05_module_import.py

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

import sys
from pathlib import Path

# Make sibling helpers.py importable regardless of where Python runs from.
sys.path.insert(0, str(Path(__file__).parent))

# 🛠️ from helpers import format_currency
# 🛠️ Print three formatted numbers.
