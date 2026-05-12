/*
Exercise 2 — Filter with WHERE

Concepts: SELECT, WHERE, string equality
Lesson: 03-sql/week-5/lessons/01-select-from-where.md
Difficulty: Easy

Goal: return the name and signup_date of every customer in the 'East' region.

Expected output:
    name        signup_date
    ----------  -----------
    Globex      2024-02-03
    Pied Piper  2024-04-01
*/

-- 📦 SETUP
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT, signup_date TEXT);
INSERT INTO customers VALUES
    (1,'Acme Corp','North','2024-01-15'),(2,'Globex','East','2024-02-03'),
    (3,'Initech','West','2024-02-20'),(4,'Hooli','North','2024-03-11'),
    (5,'Pied Piper','East','2024-04-01'),(6,'Stark Industries','West','2024-04-22');

-- 🛠️ Step 1: select name and signup_date from customers, filtered to region 'East'.
-- Single quotes around the string. Single = sign for equality.

SELECT
FROM customers
WHERE
