# Lesson 3 — Passing Data to an LLM

You cannot send 100,000 rows to an LLM. You can — and should — send a **summary**.

## Pattern: aggregate → render as text → prompt

```python
import pandas as pd

orders = pd.read_excel("datasets/marketing/sample_orders.xlsx", sheet_name="orders")
orders["order_date"] = pd.to_datetime(orders["order_date"])

monthly = orders.groupby(orders["order_date"].dt.to_period("M"))["amount"].sum()
top5 = orders.groupby("customer_id")["amount"].sum().nlargest(5)

summary = f"""
Monthly revenue:
{monthly.to_string()}

Top 5 customers by revenue:
{top5.to_string()}
"""

prompt = f"""You are an analyst. Given the data below, write a 4-bullet exec summary
focused on trends and concentration risk.

{summary}
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
    max_completion_tokens=300,
)

print(response.choices[0].message.content)
```

## Rules

1. **Never paste raw data** if you can summarize first. Saves tokens, reduces hallucinations, protects PII.
2. **Strip PII** before sending — names, emails, IDs. Use anonymized labels.
3. **Pin the model** — record the model name in your output so you can reproduce later.
4. **Log the prompt + response** during development. You'll iterate on the prompt 10 times.

## Anti-patterns

- Sending an entire DataFrame as JSON ("just so it has all the context"). Costs a fortune, gets worse output.
- Asking the LLM to do math it could trivially do in pandas. Compute first, narrate second.
- Prompting like a search query ("top customers"). Spell it out.

---

Done. Move to [`exercises/`](../exercises/) and [`project.md`](../project.md).
