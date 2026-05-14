# Lesson 9 — Data Modeling

## Why this matters

Before you can write a JOIN, someone had to decide which tables exist, which columns live in which table, and how tables relate. That design is called a data model. A good model makes queries simple and data consistent. A bad model forces you into gymnastics every time you need a basic answer. As an MBA analyst, you'll encounter both — and you'll sometimes be the one deciding how to structure a new dataset.

---

## Primary keys

A **primary key** uniquely identifies every row in a table. No two rows can have the same primary key value, and it cannot be NULL.

```sql
CREATE TABLE customers (
    id   INTEGER PRIMARY KEY,  -- surrogate key: system-generated integer
    name TEXT NOT NULL
);

-- Or a natural key (meaningful data):
CREATE TABLE products (
    sku  TEXT PRIMARY KEY,      -- natural key: already unique in the real world
    name TEXT
);
```

**Surrogate key** (id INTEGER PRIMARY KEY): system-generated, meaningless outside the DB. Stable — won't change if the customer renames themselves.

**Natural key** (email, sku, NPI number): drawn from the real world. Convenient but risky — if the value can change, all foreign keys referencing it break.

---

## Foreign keys

A **foreign key** is a column in one table that references the primary key of another table. It enforces referential integrity — you can't insert an order for a customer that doesn't exist.

```sql
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),  -- foreign key
    product_id  INTEGER REFERENCES products(id),   -- foreign key
    qty         INTEGER,
    amount      REAL
);
```

SQLite requires `PRAGMA foreign_keys = ON;` to actually enforce the constraint at runtime (it's off by default). Other databases (PostgreSQL, MySQL) enforce by default.

The relationship: one customer → many orders. One order → one customer. This is a **one-to-many** relationship — the "many" table holds the foreign key.

---

## Entity-Relationship (ER) basics

A simple store schema:

```
customers (id PK, name, region)
    |
    | 1:N
    v
orders (id PK, customer_id FK→customers, product_id FK→products, qty, amount)
    ^
    | N:1
    |
products (id PK, name, category, price)
```

A **many-to-many** relationship (e.g. students and courses) requires a junction table:

```
students (id PK, name)
enrolments (student_id FK, course_id FK, enrolled_date)  ← junction table
courses  (id PK, title, credits)
```

---

## Normalisation basics

Normalisation is the process of organising columns and tables to reduce redundancy and improve data integrity.

### 1NF — First Normal Form

Each cell holds a single, atomic value. No comma-separated lists inside a cell.

**Bad (violates 1NF):**
```
orders: id | customer | products_ordered
        1  | Acme     | "Widget, Gadget, License"
```

**Good (1NF):**
```
order_items: order_id | product_id | qty
             1        | 1          | 2
             1        | 2          | 1
             1        | 3          | 1
```

### 2NF — Second Normal Form

Every non-key column depends on the whole primary key, not just part of it. (Matters when you have composite primary keys.)

**Bad (violates 2NF — product_name depends only on product_id, not on order_id):**
```
order_lines: order_id | product_id | product_name | qty
```

**Good (2NF):** move product_name to a products table.

### 3NF — Third Normal Form

No transitive dependencies: non-key columns must depend on the key, not on other non-key columns.

**Bad (violates 3NF — region_manager depends on region, not on customer_id):**
```
customers: id | name | region | region_manager
```

**Good (3NF):** move region_manager to a regions table.

---

## When to denormalise for analytics

Normalisation is ideal for OLTP (transactional) systems. For analytics ("OLAP"), some denormalisation is acceptable and often preferred:

| Normalised (OLTP) | Denormalised (Analytics) |
|---|---|
| Many small tables | Fewer wide tables |
| Fewer JOIN bugs | Fewer JOINs needed in queries |
| Harder to query for non-SQL users | Easier for BI tools and ad-hoc SQL |

Common analytics denormalisation patterns:
- Store region name in the orders table alongside region_id (avoids a JOIN for every report)
- Pre-compute month/year columns from order_date (avoids YEAR() / MONTH() in every query)
- Flatten a customer's tier into the orders table (avoids a customer lookup on every query)

The trade-off: denormalised tables can go stale if the source data changes (e.g. customer moves region, but old orders still show the old region).

---

## A worked example: minimal CRM schema

```sql
-- 📦 SETUP
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id        INTEGER PRIMARY KEY,
    name      TEXT NOT NULL,
    region    TEXT,
    tier      TEXT CHECK(tier IN ('SMB','Mid-Market','Enterprise'))
);

CREATE TABLE products (
    id        INTEGER PRIMARY KEY,
    sku       TEXT UNIQUE NOT NULL,
    name      TEXT NOT NULL,
    category  TEXT,
    unit_price REAL NOT NULL
);

CREATE TABLE orders (
    id           INTEGER PRIMARY KEY,
    customer_id  INTEGER NOT NULL REFERENCES customers(id),
    order_date   TEXT NOT NULL,
    status       TEXT DEFAULT 'open'
);

CREATE TABLE order_items (
    order_id    INTEGER NOT NULL REFERENCES orders(id),
    product_id  INTEGER NOT NULL REFERENCES products(id),
    qty         INTEGER NOT NULL DEFAULT 1,
    unit_price  REAL NOT NULL,  -- snapshot at time of purchase
    PRIMARY KEY (order_id, product_id)
);

-- Seed data
INSERT INTO customers VALUES
    (1,'Acme Corp','North','Enterprise'),
    (2,'Globex','East','Mid-Market'),
    (3,'Initech','West','SMB');

INSERT INTO products VALUES
    (1,'HW-WIDGET-S','Widget','Hardware',9.99),
    (2,'SW-LICENSE-ENT','License','Software',99.00),
    (3,'SV-SUPPORT-PRO','Support','Service',149.00);

INSERT INTO orders VALUES
    (101,1,'2024-01-15','closed'),
    (102,2,'2024-02-03','open'),
    (103,3,'2024-03-20','closed');

INSERT INTO order_items VALUES
    (101,1,10,9.99),
    (101,2,1,99.00),
    (102,3,2,149.00),
    (103,1,5,9.99);
```

Query the model:

```sql
-- Revenue per customer
SELECT c.name, c.tier,
       SUM(oi.qty * oi.unit_price) AS total_revenue
FROM customers c
JOIN orders o       ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
GROUP BY c.id, c.name, c.tier
ORDER BY total_revenue DESC;
```

---

## Key concepts checklist

- Primary key: unique, non-null identifier for each row
- Foreign key: reference to another table's primary key
- 1NF: atomic cells, no repeating groups
- 2NF: no partial dependencies on composite keys
- 3NF: no transitive dependencies
- Denormalise for analytics when JOINs hurt more than redundancy

---

## Practice in the playground

1. Run the setup block above and query all order items with customer name and product name using two JOINs.
2. Calculate total revenue per order using `SUM(qty * unit_price)` grouped by order_id.
3. Find customers who have no orders using a LEFT JOIN.
