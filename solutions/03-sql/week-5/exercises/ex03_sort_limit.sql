/*
Reference solution — Exercise 3.
*/

-- 📦 SETUP
DROP TABLE IF EXISTS products;
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);
INSERT INTO products VALUES
    (1,'Widget','Hardware',9.99),(2,'Gadget','Hardware',19.99),
    (3,'License','Software',99.00),(4,'Service','Service',149.00),
    (5,'Cable','Hardware',4.50),(6,'Plugin','Software',29.00);

-- 🛠️ Step 1: top 3 by price.
SELECT name, price
FROM products
ORDER BY price DESC
LIMIT 3;
