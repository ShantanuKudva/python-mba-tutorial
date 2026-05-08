# Week 10 — AI Integration with Groq

**Goal:** turn raw analysis output into plain-English insight by calling a free LLM.

This week is short on code but high on concepts. By Friday, you can hand any DataFrame summary to Groq and get back a paragraph a non-technical exec would actually read.

## Concepts (read first)

- **API keys + env vars** — never hardcode, never commit. — [`python-dotenv`](https://github.com/theskumar/python-dotenv)
- **HTTP basics** — request, response, status codes. — [MDN HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- **Groq Python SDK** — chat completions wrapper. — [github.com/groq/groq-python](https://github.com/groq/groq-python)
- **Prompting** — what makes an LLM produce good output. — [Prompting Guide](https://www.promptingguide.ai/techniques)
- **Rate limits + cost** — Groq's free tier is generous but not infinite. — [rate limits](https://console.groq.com/docs/rate-limits), [pricing](https://groq.com/pricing/)

## Steps

1. Sign up at https://console.groq.com/ (free).
2. Generate an API key.
3. Create a `.env` file at the repo root (already in `.gitignore`):

   ```
   GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

4. Verify with [`exercises/ex01_hello_groq.py`](exercises/ex01_hello_groq.py).

⚠️ **Never commit your `.env`.** If you ever accidentally do — rotate the key immediately at console.groq.com.

## Map

| File | Topic |
|---|---|
| [`lessons/01-first-call.md`](lessons/01-first-call.md) | First Groq API call |
| [`lessons/02-prompts.md`](lessons/02-prompts.md) | Prompt patterns: summarize, extract, classify |
| [`lessons/03-data-to-prompt.md`](lessons/03-data-to-prompt.md) | Pass a DataFrame to an LLM safely |
| [`exercises/`](exercises/) | 4 problems |
| [`project.md`](project.md) | "Explain this dataset" tool |

## Done when

- Your API key is in `.env`, never in code.
- You can pass a pandas summary to Groq and get a sensible paragraph back.
- You handled the case where Groq returns an error or times out.
- You finished the "explain this dataset" project.
