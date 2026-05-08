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
