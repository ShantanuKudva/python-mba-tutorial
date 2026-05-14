"""
Exercise 18 — Mini invoice generator.

Concepts: input(), float(), int(), try/except ValueError, print() with sep/end,
          f-string alignment, conditional discount.
Lesson: 01-foundations/week-1/lessons/07-input-and-print.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: ask for customer name, product, quantity, and unit price. Apply a 10%
bulk discount if quantity >= 100. Guard numeric input with try/except ValueError.
Print a formatted invoice.

Expected output (for "Bright Ideas Ltd", "Monitor Stand", 150, 50.00):
    ============================================================
    INVOICE
    Customer : Bright Ideas Ltd
    Product  : Monitor Stand
    ============================================================
    Quantity        :          150
    Unit price      :       $50.00
    Subtotal        :    $7,500.00
    Bulk discount   :     -$750.00
    ------------------------------------------------------------
    Total due       :    $6,750.00
    ============================================================
"""

BULK_THRESHOLD  = 100
BULK_DISCOUNT   = 0.10

# 🛠️ Step 1: ask for customer and product (strings — no conversion needed).

# 🛠️ Step 2: ask for quantity. Wrap int(input(...)) in try/except ValueError;
#    if conversion fails, print "Invalid quantity." and set quantity = 0.

# 🛠️ Step 3: ask for unit_price. Wrap float(input(...)) in try/except ValueError;
#    if conversion fails, print "Invalid price." and set unit_price = 0.0.

# 🛠️ Step 4: compute subtotal = quantity * unit_price.
#    discount_amount = subtotal * BULK_DISCOUNT if quantity >= BULK_THRESHOLD else 0.
#    total = subtotal - discount_amount.

# 🛠️ Step 5: print the invoice. Use "=" * 60 and "-" * 60 for separators.
#    Label width :<16, value width :>12. Currency values use :>12,.2f with $ prefix.
