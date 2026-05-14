# Phase 3 — Python + SQL (Week 5)

**Goal:** read and reshape relational data with SQL — then drive it from Python.

SQL is the second language you need for analytics. Most real business data lives in databases, not in CSV files. By Friday of Week 5 you can answer a question like *"which 10 customers drove the most revenue last quarter?"* with a single query — and call that query from a Python script.

> 🪶 **Runs in the browser.** Every SQL block on these pages is backed by a real SQLite database compiled to WebAssembly. No install. State is per-page — refreshing resets the data to the seed.

## What you'll learn

- The relational mental model: tables, rows, columns, primary/foreign keys.
- The core SQL verbs: `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`, `GROUP BY`, `HAVING`, `JOIN`.
- How to read a query top-down (write it bottom-up).
- How to call SQL from Python with `sqlite3` (stdlib) and SQLAlchemy (the production choice).
- Why "do it in SQL" usually beats "load everything into pandas and filter".

## Map

| File | Topic | Open |
|---|---|---|
| Lesson 01 | `SELECT … FROM … WHERE` — the core triple | [01-select-from-where.md](week-5/lessons/01-select-from-where.md) |
| Lesson 02 | `ORDER BY`, `LIMIT`, `DISTINCT` | [02-sorting-limit-distinct.md](week-5/lessons/02-sorting-limit-distinct.md) |
| Lesson 03 | Aggregates + `GROUP BY` + `HAVING` | [03-aggregates-groupby.md](week-5/lessons/03-aggregates-groupby.md) |
| Lesson 04 | Joining tables | [04-joins.md](week-5/lessons/04-joins.md) |
| Lesson 05 | Python ↔ SQL with `sqlite3` and SQLAlchemy | [05-python-sqlalchemy.md](week-5/lessons/05-python-sqlalchemy.md) |
| Lesson 06 | Subqueries: scalar, IN, correlated | [06-subqueries.md](week-5/lessons/06-subqueries.md) |
| Lesson 07 | Window functions: ROW_NUMBER, RANK, LAG, LEAD, running totals | [07-window-functions.md](week-5/lessons/07-window-functions.md) |
| Lesson 08 | NULLs & data types: COALESCE, NULLIF, CAST, type affinity | [08-nulls-and-data-types.md](week-5/lessons/08-nulls-and-data-types.md) |
| Lesson 09 | Data modeling: keys, normalization, when to denormalize | [09-data-modeling.md](week-5/lessons/09-data-modeling.md) |
| Exercises | 🟢 Easy → 🟡 Medium → 🔴 Hard | [exercises index](week-5/exercises/README.md) |

## The dataset (mini-store)

Every lesson and exercise on this phase shares the same toy schema:

```
customers(id, name, region, signup_date)
products (id, name, category, price)
orders   (id, customer_id, product_id, qty, order_date)
```

You will see it again and again — that repetition is the point. Same tables, harder questions.

## Done when

- You can write `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT …` from scratch.
- You can join two or three tables without copying from a previous example.
- You can run a SQL query from Python and pull the result into a pandas DataFrame.
- All nine lessons and ≥14 of the 20 exercises are marked complete.

## Why SQL comes before pandas

Most real business data lives in relational databases. Learning SQL first means you can pull just the slice you need — by date range, by segment, by region — before any Python work begins. Phase 4 (pandas) then takes whatever SQL hands it and reshapes for the harder analyses. "Filter in SQL, reshape in pandas" is the production pattern; doing it in this order trains the right reflex.
