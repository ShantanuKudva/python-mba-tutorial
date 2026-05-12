"""
Exercise 3 — Merge two DataFrames.

Concepts: merge, left join, how="left".
Lesson: 04-data-with-pandas/week-7/lessons/03-merge.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: merge the orders table with the customers table on customer_id (left join).
Print the merged DataFrame and the count of orders per customer name.

Expected output (approximate):
    merged head:
       order_id  customer_id  amount          name    segment
    0         1          101    4200          Acme  Enterprise
    ...
"""

import pandas as pd

# Setup — two tables to merge.
orders = pd.DataFrame({
    "order_id":    [1, 2, 3, 4, 5, 6],
    "customer_id": [101, 102, 103, 101, 104, 102],
    "amount":      [4200, 8100, 2300, 5100, 3400, 9200],
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105],
    "name":        ["Acme", "Globex", "Initech", "Umbrella", "Stark"],
    "segment":     ["Enterprise", "Enterprise", "SMB", "Enterprise", "SMB"],
})

merged = orders.merge(customers, on="customer_id", how="left")

print("Merged head:")
print(merged.head())

orders_per_customer = merged.groupby("name")["order_id"].count().sort_values(ascending=False)
print("\nOrders per customer:")
print(orders_per_customer)
