# Lesson 1 — First Groq Call

## Install (already in requirements.txt)

```bash
pip install groq python-dotenv
```

## Make the call

```python
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()   # reads .env

client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a concise financial analyst."},
        {"role": "user", "content": "Explain gross margin in one sentence."},
    ],
    max_completion_tokens=150,
    temperature=0.3,
)

print(response.choices[0].message.content)
```

## Roles

- `system` — tone, persona, rules. Set it once at the top.
- `user` — the actual question.
- `assistant` — model's prior responses (only when continuing a conversation).

## Parameters worth knowing

| Param | What it does |
|---|---|
| `model` | which Groq-hosted model. Browse at console.groq.com/docs. |
| `temperature` | 0 = deterministic, 1 = creative. For analysis use 0–0.3. |
| `max_completion_tokens` | hard cap on output length. Saves cost. |

## Error handling

```python
from groq import Groq, APIError

try:
    response = client.chat.completions.create(...)
except APIError as exc:
    print(f"Groq returned an error: {exc}")
    # fall back to a placeholder summary, OR re-raise
```

Common errors: invalid key, rate limited (429), model busy.

---

Next: [`02-prompts.md`](02-prompts.md).
