# Lesson 5 — Python ↔ SQL

SQL on its own is great for ad-hoc analysis. But the real win is **calling SQL from Python** — the database does the heavy filter / group / join work, and pandas only sees the small result set.

This lesson covers two ways to do that:

1. `sqlite3` — Python's built-in driver. Zero install, perfect for learning and small scripts.
2. **SQLAlchemy** — the production-grade toolkit used by almost every Python codebase that touches a database. Same Python code works against SQLite, Postgres, MySQL, BigQuery.

Both run inside this in-browser Python via Pyodide. The first time you click ▶ Run on a SQLAlchemy block, the page will install the package — give it ~15 seconds.

## Option 1 — `sqlite3` (stdlib)

```python
import sqlite3

# Open a fresh in-memory database. Same database WASM was running in lessons 1–4,
# just driven from Python now.
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.executescript("""
    CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT);
    INSERT INTO customers VALUES (1,'Acme','North'),(2,'Globex','East'),(3,'Initech','West');
""")

# Parametrize EVERY user-supplied value with ?  — never f-string SQL.
region = "North"
cur.execute("SELECT name FROM customers WHERE region = ?", (region,))
for row in cur.fetchall():
    print(row)

conn.close()
```

Three things to internalize:

- `?` placeholders + a tuple of values. This is how you avoid SQL injection. F-strings inside a query string are a one-way ticket to a CVE.
- `executescript` runs multiple statements separated by `;`. `execute` runs one.
- `fetchall()` returns a list of tuples. `fetchone()` returns one tuple. Iterating the cursor streams rows lazily.

## Option 2 — pandas straight from SQL

The fastest "SQL → DataFrame" path in the Python ecosystem:

```python
import sqlite3, pandas as pd

conn = sqlite3.connect(":memory:")
conn.executescript("""
    CREATE TABLE orders (id INTEGER, customer_id INTEGER, qty INTEGER);
    INSERT INTO orders VALUES (1,1,10),(2,1,5),(3,2,20),(4,3,7);
""")

df = pd.read_sql_query(
    "SELECT customer_id, SUM(qty) AS total_qty FROM orders GROUP BY customer_id",
    conn,
)
print(df)
print("Type:", type(df).__name__)
```

The `GROUP BY` runs in SQLite (compiled C, fast). Only the 3-row result crosses into Python. This pattern scales: on a real database that table could have 50 million rows.

## Option 3 — SQLAlchemy (the production answer)

```python
import micropip
await micropip.install("sqlalchemy")

from sqlalchemy import create_engine, text
import pandas as pd

# An "engine" is a connection pool. One per app, not one per query.
engine = create_engine("sqlite:///:memory:")

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE products (id INTEGER, name TEXT, category TEXT, price REAL);
    """))
    conn.execute(
        text("INSERT INTO products VALUES (:id, :name, :cat, :price)"),
        [
            {"id": 1, "name": "Widget", "cat": "Hardware", "price": 9.99},
            {"id": 2, "name": "Gadget", "cat": "Hardware", "price": 19.99},
            {"id": 3, "name": "License","cat": "Software", "price": 99.00},
        ],
    )

# Same pandas trick — but now you can swap the engine URL to point at Postgres
# and nothing else changes.
df = pd.read_sql_query(
    text("SELECT category, AVG(price) AS avg_price FROM products GROUP BY category"),
    engine,
)
print(df)
```

What you got by switching:

- **One connection URL changes everything.** `sqlite:///mydata.db` → `postgresql+psycopg://user:pwd@host/db`. Same Python code.
- **Named bind params** (`:id`, `:name`) instead of positional `?`. Easier to read with 8 parameters.
- **Connection pooling** built in. `engine.begin()` gives you a transaction; on exception it rolls back.
- **The ORM** (optional) — define Python classes that map to tables. Out of scope here; see the Resources block.

> 💡 The ORM is *optional*. Many production codebases use SQLAlchemy purely as a "connection pool + safe parameter binding" layer with raw SQL strings. That is a perfectly respected choice — start there.

## Reading vs writing

- **Read-heavy code** (reports, dashboards): use `pd.read_sql_query` with `text(...)`. Push aggregation into SQL.
- **Write-heavy code** (insert / update / delete): use `engine.begin()` for a transaction so partial failures roll back cleanly.

```python
with engine.begin() as conn:
    conn.execute(text("UPDATE products SET price = price * 1.10 WHERE category = :cat"),
                 {"cat": "Hardware"})
    # If this line raises, the UPDATE above is rolled back automatically.
    conn.execute(text("INSERT INTO audit_log (action) VALUES ('price_bump')"))
```

## Cheat sheet — choosing a tool

| Situation | Use |
|---|---|
| Learning, 1-off scripts, no deps | `sqlite3` stdlib |
| "Run a query, hand result to pandas" | `pd.read_sql_query(sql, conn_or_engine)` |
| Production app, multiple environments | SQLAlchemy `Engine` + raw `text()` queries |
| Lots of Python-side modelling, validation | SQLAlchemy ORM |

## Pitfalls

- `await micropip.install(...)` only works in async runtimes (Pyodide is one). In normal CPython you'd `pip install sqlalchemy`.
- Forgetting `engine.dispose()` at the end of a script leaks connections — not visible on SQLite, very visible on Postgres.
- f-string SQL: `f"SELECT * FROM t WHERE name = '{user_input}'"` is **never** the right answer. Always parametrize.

---

## 📚 Resources

**Official docs**
- [Python `sqlite3` module](https://docs.python.org/3/library/sqlite3.html)
- [SQLAlchemy 2.0 — unified tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- [pandas — `read_sql_query`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)

**Deep dives**
- [SQLAlchemy ORM quickstart](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [SQL injection — why parameters matter (OWASP)](https://owasp.org/www-community/attacks/SQL_Injection)

**Video**
- [ArjanCodes — SQLAlchemy in 10 minutes](https://www.youtube.com/results?search_query=sqlalchemy+tutorial)

---

## 🏋️ Practice

### Easy

Work through a fresh SELECT problem in the editor below:
[ex01 — Basic SELECT](#play/03-sql/week-5/exercises/ex01_basic_select.sql)

### Medium

Practice joins and group-by:
[ex06 — INNER JOIN](#play/03-sql/week-5/exercises/ex06_inner_join.sql)

### Hard

Run a SQL aggregate from Python and pull the result into a pandas DataFrame:
[ex08 — Python + SQLAlchemy](#play/03-sql/week-5/exercises/ex08_python_sqlalchemy.py)

---

You finished the SQL phase. Next stop — the capstone, [`07-capstone-app/README.md`](../../../07-capstone-app/README.md).
