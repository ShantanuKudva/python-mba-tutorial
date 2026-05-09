"""
Exercise 5 — Use a helper function.

Concepts: defining functions, calling functions from the same script,
          reusability.
Lesson: 01-foundations/week-3/lessons/04-modules.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: the `format_currency` helper is defined in the setup cell below.
Call it to format three numbers and print the results.

Expected output:
    $1,234.50
    $0.00
    $9,999,999.99
"""

# Setup — helper function (in a real project this would live in a separate module).
def format_currency(amount: float, symbol: str = "$") -> str:
    """Return amount formatted as e.g. '$1,234.50'."""
    return f"{symbol}{amount:,.2f}"

print(format_currency(1234.50))
print(format_currency(0))
print(format_currency(9_999_999.99))
