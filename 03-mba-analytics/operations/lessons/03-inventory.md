# Lesson 3 — EOQ, Safety Stock, Reorder Point

## EOQ

```
EOQ = √(2 × D × S / H)
```

- D = annual demand (units)
- S = ordering cost per order
- H = holding cost per unit per year

```python
import math

def eoq(annual_demand, order_cost, holding_cost):
    return math.sqrt(2 * annual_demand * order_cost / holding_cost)

print(eoq(annual_demand=12_000, order_cost=50, holding_cost=2))  # ~775
```

## Safety stock

```python
def safety_stock(demand_std, lead_time_weeks, z=1.65):
    """z=1.65 ≈ 95% service level. Assumes demand_std is per-week."""
    return z * demand_std * (lead_time_weeks ** 0.5)
```

`z` is the desired service level. Common picks: 1.28 (90%), 1.65 (95%), 2.33 (99%).

## Reorder point

```python
def reorder_point(weekly_demand_avg, lead_time_weeks, ss):
    return weekly_demand_avg * lead_time_weeks + ss
```

When stock falls below this, reorder one EOQ batch.

## Putting it together

```python
weekly = demand.resample("W").sum()
weekly_avg = weekly.mean()
weekly_std = weekly.std()

ss = safety_stock(weekly_std, lead_time_weeks=4)
rop = reorder_point(weekly_avg, 4, ss)
order_qty = eoq(annual_demand=weekly_avg * 52, order_cost=75, holding_cost=3)

print(f"Reorder when stock <= {rop:.0f}, order {order_qty:.0f} at a time.")
```

---

Done with operations lessons. Move to [`exercises/`](../exercises/) and [`project.md`](../project.md).

---

## 🏋️ Practice

### Easy

Given `annual_demand=12000`, `order_cost=50`, `holding_cost=2`, compute the EOQ. Print the result and interpret it: how many orders per year does this imply?

[▶ Open exercise](#play/03-mba-analytics/operations/exercises/ex03_eoq.py)

### Medium

Compute safety stock and reorder point for a product with weekly demand average of 230 units, weekly demand standard deviation of 40 units, and a 4-week lead time. Use a 95% service level (z = 1.65). Then compute EOQ using `annual_demand = weekly_avg * 52` and `order_cost=75`, `holding_cost=3`. Print all three values.

[▶ Open exercise](#play/03-mba-analytics/operations/exercises/ex04_reorder.py)

### Hard

Build a full inventory policy report for three SKUs with different demand and cost profiles. For each SKU, compute EOQ, safety stock, and reorder point. Present the results in a formatted table and calculate the total annual holding cost if all SKUs maintain safety stock at all times.

[▶ Open exercise](#play/03-mba-analytics/operations/exercises/ex04_reorder.py)

---

## 📚 Resources

**Official docs**
- [Investopedia — EOQ](https://www.investopedia.com/terms/e/economicorderquantity.asp)
- [Investopedia — safety stock](https://www.investopedia.com/terms/s/safetystock.asp)

**Deep dives**
- [CFI — inventory management](https://corporatefinanceinstitute.com/resources/management/inventory-management/)

**Video tutorials**
- [YouTube — EOQ & safety stock explained](https://www.youtube.com/results?search_query=EOQ+economic+order+quantity+safety+stock+explained)

