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

## 📚 Resources

**Official docs**
- [Groq — quickstart](https://console.groq.com/docs/quickstart)
- [Groq — chat completions](https://console.groq.com/docs/api-reference#chat)
- [OpenAI Python SDK (Groq is API-compatible)](https://github.com/openai/openai-python)

**Deep dives**
- [Groq — model list](https://console.groq.com/docs/models)

**Video tutorials**
- [YouTube — Groq API tutorial](https://www.youtube.com/results?search_query=groq+api+python+tutorial)


---

Next: [`02-prompts.md`](02-prompts.md).

---

## 🏋️ Practice

### Easy

Make a Groq API call using the pattern from the lesson. Ask the model to define "gross margin" in exactly one sentence. Print the response.

[▶ Open exercise](#play/06-ai-integration/exercises/ex01_hello_groq.py)

### Medium

Make two Groq calls: one with `temperature=0.0` and one with `temperature=0.9`. Ask both to explain "WACC" in two sentences. Print both responses and note any differences in tone or detail.

[▶ Open exercise](#play/06-ai-integration/exercises/ex01_hello_groq.py)

### Hard

Write a function `groq_with_retry(client, messages, max_attempts=3)` that calls the API and retries on `APIError` with a 2-second delay between attempts. Wrap the function with error handling that prints which attempt failed. Call it with a sample financial analysis prompt.

[▶ Open exercise](#play/06-ai-integration/exercises/ex01_hello_groq.py)
