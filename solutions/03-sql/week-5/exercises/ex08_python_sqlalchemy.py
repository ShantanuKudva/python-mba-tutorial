"""
Reference solution — Exercise 8.
"""

import micropip
await micropip.install("sqlalchemy")

from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine("sqlite:///:memory:")

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);
        CREATE TABLE orders   (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, qty INTEGER, order_date TEXT);
    """))
    conn.execute(text("INSERT INTO products VALUES (:i,:n,:c,:p)"), [
        {"i":1,"n":"Widget", "c":"Hardware","p":9.99},
        {"i":2,"n":"Gadget", "c":"Hardware","p":19.99},
        {"i":3,"n":"License","c":"Software","p":99.00},
        {"i":4,"n":"Service","c":"Service", "p":149.00},
        {"i":5,"n":"Cable",  "c":"Hardware","p":4.50},
        {"i":6,"n":"Plugin", "c":"Software","p":29.00},
    ])
    conn.execute(text("INSERT INTO orders VALUES (:i,:c,:p,:q,:d)"), [
        {"i":101,"c":1,"p":1,"q":10,"d":"2024-05-02"},
        {"i":102,"c":1,"p":3,"q":1, "d":"2024-05-04"},
        {"i":103,"c":2,"p":2,"q":5, "d":"2024-05-09"},
        {"i":104,"c":3,"p":5,"q":20,"d":"2024-05-12"},
        {"i":105,"c":4,"p":4,"q":2, "d":"2024-06-01"},
        {"i":106,"c":5,"p":1,"q":30,"d":"2024-06-04"},
        {"i":107,"c":2,"p":4,"q":1, "d":"2024-06-15"},
        {"i":108,"c":1,"p":2,"q":3, "d":"2024-07-01"},
        {"i":109,"c":6,"p":6,"q":4, "d":"2024-07-12"},
        {"i":110,"c":3,"p":3,"q":2, "d":"2024-07-20"},
    ])

query = text("""
    SELECT  p.category,
            SUM(o.qty * p.price) AS total_revenue
    FROM    orders o
    JOIN    products p ON o.product_id = p.id
    GROUP BY p.category
    ORDER BY total_revenue DESC
""")
df = pd.read_sql_query(query, engine)
print(df)
