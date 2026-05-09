"""
Exercise 9 — Mutate a shopping cart.

Concepts: list mutation — append, index-assignment, remove, slicing.
Lesson: lessons/01-lists-and-loops.md
Difficulty: Easy
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: practice the four core list mutations on a single cart, then print
the final state and a slice.

Expected final state:
    cart       = ['Notebook', 'Blue Pen', 'Stapler', 'Mouse', 'Keyboard']
    first_two  = ['Notebook', 'Blue Pen']
    last_two   = ['Mouse', 'Keyboard']
"""

cart = []

cart.append("Notebook")
cart.append("Pen")
cart.append("Eraser")
cart.append("Mouse")
cart.append("Keyboard")

cart[1] = "Blue Pen"

cart.remove("Eraser")

cart.insert(2, "Stapler")

first_two = cart[:2]
last_two  = cart[-2:]

print(cart)
print(first_two)
print(last_two)
