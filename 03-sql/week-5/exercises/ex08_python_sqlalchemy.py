"""
Exercise 8 — Python + SQLAlchemy → pandas

Concepts: sqlalchemy.create_engine, text(), parameter binding, pd.read_sql_query
Lesson: 03-sql/week-5/lessons/05-python-sqlalchemy.md
Difficulty: Hard

Goal: drive a SQLite-in-memory database from Python with SQLAlchemy, then pull a
group-by result straight into a pandas DataFrame.

Expected output (DataFrame, may print as):
    category   total_revenue
    Hardware           849.6  (approx — Widget+Gadget+Cable orders)
    Software           297.0
    Service            298.0

Numbers depend on the seed data; just confirm three rows, three columns, sorted
biggest first.
"""

# Setup — install SQLAlchemy on first run.  micropip is a Pyodide-specific tool;
# on a normal machine you would run `pip install sqlalchemy pandas` instead.
import micropip
await micropip.install("sqlalchemy")

from sqlalchemy import create_engine, text
import pandas as pd

# 🛠️ Step 1: build an engine pointing at an in-memory SQLite database.
#     engine = create_engine("sqlite:///:memory:")

# 🛠️ Step 2: open a transaction and create the three tables, then seed them.
#     with engine.begin() as conn:
#         conn.execute(text("""
#             CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT);
#             CREATE TABLE products  (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);
#             CREATE TABLE orders    (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, qty INTEGER, order_date TEXT);
#         """))
#         conn.execute(text("INSERT INTO products VALUES (:i,:n,:c,:p)"), [
#             {"i":1,"n":"Widget", "c":"Hardware","p":9.99},
#             {"i":2,"n":"Gadget", "c":"Hardware","p":19.99},
#             {"i":3,"n":"License","c":"Software","p":99.00},
#             {"i":4,"n":"Service","c":"Service", "p":149.00},
#             {"i":5,"n":"Cable",  "c":"Hardware","p":4.50},
#             {"i":6,"n":"Plugin", "c":"Software","p":29.00},
#         ])
#         conn.execute(text("INSERT INTO orders VALUES (:i,:c,:p,:q,:d)"), [
#             {"i":101,"c":1,"p":1,"q":10,"d":"2024-05-02"},
#             {"i":102,"c":1,"p":3,"q":1, "d":"2024-05-04"},
#             {"i":103,"c":2,"p":2,"q":5, "d":"2024-05-09"},
#             {"i":104,"c":3,"p":5,"q":20,"d":"2024-05-12"},
#             {"i":105,"c":4,"p":4,"q":2, "d":"2024-06-01"},
#             {"i":106,"c":5,"p":1,"q":30,"d":"2024-06-04"},
#             {"i":107,"c":2,"p":4,"q":1, "d":"2024-06-15"},
#             {"i":108,"c":1,"p":2,"q":3, "d":"2024-07-01"},
#             {"i":109,"c":6,"p":6,"q":4, "d":"2024-07-12"},
#             {"i":110,"c":3,"p":3,"q":2, "d":"2024-07-20"},
#         ])

# 🛠️ Step 3: write a SQL query that joins orders to products, groups by
# category, sums (qty * price) as total_revenue, and orders biggest first.
# Pull the result into a DataFrame with pd.read_sql_query and print it.
#
#     query = text("""
#         SELECT  p.category,
#                 SUM(o.qty * p.price) AS total_revenue
#         FROM    orders o
#         JOIN    products p ON o.product_id = p.id
#         GROUP BY p.category
#         ORDER BY total_revenue DESC
#     """)
#     df = pd.read_sql_query(query, engine)
#     print(df)
