"""
Exercise 7 — Pull parts out of a SKU code.

Concepts: string slicing, .split(), f-strings.
Lesson: lessons/04-strings.md
Difficulty: Medium
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

parts = sku.split("-")
category, year, color = parts

print(f"{'Category:':<10}{category}")
print(f"{'Year:':<10}{year}")
print(f"{'Color:':<10}{color}")
