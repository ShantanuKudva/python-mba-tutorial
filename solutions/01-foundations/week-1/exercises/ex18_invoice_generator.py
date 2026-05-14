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

BULK_THRESHOLD = 100
BULK_DISCOUNT  = 0.10

customer = input("Customer name: ")
product  = input("Product name: ")

try:
    quantity = int(input("Quantity: "))
except ValueError:
    print("Invalid quantity.")
    quantity = 0

try:
    unit_price = float(input("Unit price ($): "))
except ValueError:
    print("Invalid price.")
    unit_price = 0.0

subtotal        = quantity * unit_price
discount_amount = subtotal * BULK_DISCOUNT if quantity >= BULK_THRESHOLD else 0.0
total           = subtotal - discount_amount

SEP_THICK = "=" * 60
SEP_THIN  = "-" * 60
LBL = 16   # label column width
VAL = 12   # value column width

print(SEP_THICK)
print("INVOICE")
print(f"{'Customer':<9}: {customer}")
print(f"{'Product':<9}: {product}")
print(SEP_THICK)
print(f"{'Quantity':<{LBL}}: {quantity:>{VAL},}")
print(f"{'Unit price':<{LBL}}: ${unit_price:>{VAL-1},.2f}")
print(f"{'Subtotal':<{LBL}}: ${subtotal:>{VAL-1},.2f}")
print(f"{'Bulk discount':<{LBL}}: ${-discount_amount:>{VAL-1},.2f}" if discount_amount else f"{'Bulk discount':<{LBL}}: {'$0.00':>{VAL}}")
print(SEP_THIN)
print(f"{'Total due':<{LBL}}: ${total:>{VAL-1},.2f}")
print(SEP_THICK)
