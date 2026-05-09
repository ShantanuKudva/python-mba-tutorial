"""
Exercise 7 — Pull parts out of a SKU code.

Concepts: string slicing, .split(), f-strings.
Lesson: lessons/04-strings.md
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

A SKU follows the format: "<CATEGORY>-<YEAR>-<COLOR>"
Example:  "WIDGET-2026-RED"

Goal: parse the parts and print them on labelled lines.

Expected output for sku = "WIDGET-2026-RED":
    Category: WIDGET
    Year:     2026
    Color:    RED
"""

sku = "WIDGET-2026-RED"

# 🛠️ Step 1: split the sku on "-" into a list of 3 parts.
# parts = sku.split("-")

# 🛠️ Step 2: assign category, year, color via tuple-style unpacking:
# category, year, color = parts

# 🛠️ Step 3: print 3 lines using f-strings. Use ":<10" to left-pad labels.
# Hint:
#   print(f"{'Category:':<10}{category}")
