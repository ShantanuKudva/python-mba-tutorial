# Phase 4 — AI Integration (Week 10)

**Goal:** turn raw analysis output into plain-English insight by calling a free LLM.

This week is short on code but high on concepts. By Friday you can hand any DataFrame summary to Groq and get back a paragraph a non-technical exec would actually read.

## Concepts (read first)

- **HTTP basics** — request, response, status codes. — [MDN HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- **Groq Python SDK** — chat completions wrapper. — [github.com/groq/groq-python](https://github.com/groq/groq-python)
- **Prompting** — what makes an LLM produce good output. — [Prompting Guide](https://www.promptingguide.ai/techniques)
- **Rate limits + cost** — Groq's free tier is generous but not infinite. — [rate limits](https://console.groq.com/docs/rate-limits), [pricing](https://groq.com/pricing/)

## Map

| File | Topic | Open |
|---|---|---|
| Lesson 01 | First Groq API call | [01-first-call.md](lessons/01-first-call.md) |
| Lesson 02 | Prompt patterns: summarize, extract, classify | [02-prompts.md](lessons/02-prompts.md) |
| Lesson 03 | Pass a DataFrame to an LLM safely | [03-data-to-prompt.md](lessons/03-data-to-prompt.md) |
| Exercises | 🟢 Easy → 🟡 Medium → 🔴 Hard | [exercises index](exercises/README.md) |
| Project | "Explain this dataset" tool | [project.md](project.md) |

## Steps

1. Sign up at [console.groq.com](https://console.groq.com/) (free).
2. Generate an API key in the Groq dashboard.
3. The first time a playground cell asks, paste your key. It's stored in your browser's localStorage only — never sent anywhere except Groq's API.
4. Open [Lesson 01](lessons/01-first-call.md) and click ▶ Run on the first example.

⚠️ **Treat your API key like a password.** Don't paste it into screenshots, public chat, or anyone else's machine. If it leaks, rotate it at console.groq.com.

## Browser note

The Groq SDK is pure-Python and works inside Pyodide. If a request is blocked by browser CORS, the lesson explains the workaround (Groq's OpenAI-compatible REST endpoint).

## Done when

- Your API key is stored locally and your first call returned a sensible response.
- You can pass a pandas summary to Groq and get a clean paragraph back.
- You handle the case where Groq returns an error or times out.
- You finished the "explain this dataset" project.
- Marked all lesson + exercise pages complete.
