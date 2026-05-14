# Lesson 6 — Classes and Objects

## Why model things with classes?

A function transforms data. A **class** *is* data — bundled together with the functions that act on it.

Think of a spreadsheet row for a product: SKU, name, price, stock level. In Python you could use a dict, but a dict has no rules. A `Product` class enforces structure and gives you methods like `.apply_discount()` or `.is_low_stock()` right on the object itself.

```python
class Product:
    def __init__(self, sku, name, price, stock):
        self.sku   = sku
        self.name  = name
        self.price = price
        self.stock = stock

laptop = Product("LPT-001", "Business Laptop", 1_200, 45)
print(laptop.name)    # Business Laptop
print(laptop.price)   # 1200
```

`__init__` is the **constructor** — it runs automatically when you write `Product(...)`. `self` is the object being created; every attribute is attached to `self`.

---

## Adding methods

A method is a function defined inside a class. It always receives `self` as its first argument.

```python
class Product:
    def __init__(self, sku, name, price, stock):
        self.sku   = sku
        self.name  = name
        self.price = price
        self.stock = stock

    def apply_discount(self, rate=0.10):
        """Return the discounted price (does not mutate the object)."""
        return self.price * (1 - rate)

    def is_low_stock(self, threshold=50):
        return self.stock < threshold

    def __repr__(self):
        return f"Product({self.sku!r}, price={self.price})"

laptop = Product("LPT-001", "Business Laptop", 1_200, 45)
print(laptop.apply_discount(0.15))   # 1020.0
print(laptop.is_low_stock())         # True
print(laptop)                        # Product('LPT-001', price=1200)
```

`__repr__` controls what you see when you `print()` the object. Always define it — it makes debugging much easier.

---

## A realistic Customer class

```python
class Customer:
    def __init__(self, customer_id, name, region, tier="Standard"):
        self.customer_id = customer_id
        self.name        = name
        self.region      = region
        self.tier        = tier
        self.orders      = []          # starts empty — added later

    def add_order(self, amount):
        self.orders.append(amount)

    def lifetime_value(self):
        return sum(self.orders)

    def is_vip(self):
        return self.lifetime_value() >= 10_000

c = Customer("C001", "Acme Corp", "North", tier="Premium")
c.add_order(4_500)
c.add_order(6_200)
print(c.lifetime_value())   # 10700
print(c.is_vip())           # True
```

---

## Using classes in a list

Classes shine when you have many objects of the same type.

```python
catalog = [
    Product("SKU-A", "Widget Alpha",  9.99, 200),
    Product("SKU-B", "Widget Beta",  14.50,  30),
    Product("SKU-C", "Widget Gamma",  7.00, 120),
]

low_stock = [p for p in catalog if p.is_low_stock()]
print([p.name for p in low_stock])   # ['Widget Beta']

discounted = [(p.name, p.apply_discount(0.20)) for p in catalog]
print(discounted)
```

---

## 🛠️ Try it

Run this mini catalog to see objects used in a loop. Try adding a `.restock(qty)` method that increases `self.stock` and print the stock before and after.

```python
class Product:
    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def is_low_stock(self, threshold=50):
        return self.stock < threshold

    def __repr__(self):
        return f"{self.name} (stock={self.stock})"

catalog = [
    Product("Notebook",  4.99, 200),
    Product("Pen Set",   2.49,  15),
    Product("Stapler",   8.99,  40),
]

for p in catalog:
    flag = "⚠ LOW" if p.is_low_stock() else "OK"
    print(f"{p.name:<15} stock={p.stock:>4}  {flag}")
```

---

## Common confusions

**Forgetting `self`** — if you write `def is_low_stock(threshold=50):` instead of `def is_low_stock(self, threshold=50):`, Python raises `TypeError` when you call it.

**`__init__` vs calling the class** — `Product(...)` calls `__init__` automatically. You never call `__init__` directly.

**Class vs instance** — `Product` is the blueprint; `laptop = Product(...)` is one specific product. Attributes live on the instance (`laptop.price`), not on the class.

---

## 📚 Resources

**Official docs**
- [Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html)
- [`__repr__` and `__str__`](https://docs.python.org/3/reference/datamodel.html#object.__repr__)

**Deep dives**
- [Real Python — OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Real Python — `__init__` and Instance Variables](https://realpython.com/python-instance-variables/)

---

Next: [`07-scope-and-mutability.md`](07-scope-and-mutability.md).

---

## 🏋️ Practice

### Easy

Define a `Product` class with `__init__(self, name, price, stock)` and a method `is_low_stock(self, threshold=50)`. Create three product instances from a list of tuples and print each product's name, price, and whether it is low on stock.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex13_product_class.py)

### Medium

Define a `Customer` class that stores `customer_id`, `name`, `region`, and an empty `orders` list. Add methods `add_order(amount)`, `lifetime_value()`, and `tier()` that returns `"Gold"` if LTV ≥ 10 000, `"Silver"` if ≥ 5 000, else `"Bronze"`. Create four customers, add varying orders to each, and print a formatted summary table.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex14_customer_class.py)

### Hard

Define an `Order` class with `order_id`, `customer_name`, `region`, `items` (list of `(name, qty, unit_price)` tuples), and methods `total()`, `item_count()`, and `summary()`. Build a list of at least four orders. Print a report: each order on one line showing ID, customer, region, item count, and total. Then print the overall grand total and the highest-value order.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex15_order_class.py)
