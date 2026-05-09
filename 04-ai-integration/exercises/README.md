# Exercises — Week 10 · AI Integration

> Practice problems for the lessons in this module. Each exercise opens directly in the browser playground — fill in the steps and click ▶ Run.

> **Before starting:** you need a [Groq API key](https://console.groq.com). Enter it when each exercise prompts you, or set the `GROQ_API_KEY` environment variable. All exercises install the `groq` package — click the "Install packages" button the first time.

## 📚 Read first

Skim these before attempting the harder exercises:
- [Lesson 01 — First API Call](../lessons/01-first-call.md)
- [Lesson 02 — Prompt Design](../lessons/02-prompts.md)
- [Lesson 03 — Data to Prompt](../lessons/03-data-to-prompt.md)
- [Groq API docs](https://console.groq.com/docs/openai)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## 🟢 Easy

- [ex01 — Hello, Groq!](#play/04-ai-integration/exercises/ex01_hello_groq.py) — first API call, system/user roles, print the response.
- [ex02 — Executive summary](#play/04-ai-integration/exercises/ex02_summarize.py) — summarise bullet points in four concise bullets.

## 🟡 Medium

- [ex03 — Extract structured JSON](#play/04-ai-integration/exercises/ex03_extract_json.py) — extract prompt pattern, `json.loads`, low temperature.
- [ex05 — Batch sentiment scoring](#play/04-ai-integration/exercises/ex05_sentiment_score.py) — loop over reviews, parse JSON responses, tally sentiment counts.
- [ex06 — Expense classification pipeline](#play/04-ai-integration/exercises/ex06_classification_pipeline.py) — few-shot prompting, classify descriptions, aggregate with pandas.

## 🔴 Hard

- [ex04 — Data → narrative summary](#play/04-ai-integration/exercises/ex04_data_summary.py) — aggregate real order data, render as text, send to Groq, parse 5-bullet exec summary.
