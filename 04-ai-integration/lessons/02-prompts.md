# Lesson 2 — Prompt Patterns

Three patterns cover 90% of business use cases.

## 1. Summarize

```
You are an analyst. Given the metrics below, write a 4-bullet executive summary.
Focus on what is unusual or actionable. Do not restate the numbers verbatim.

Metrics:
- Revenue YoY: +18%
- Gross margin: 47% (up 3 pts)
- Customer churn: 7.2% (up from 5.1%)
- New customers: 1,420 (down 9%)
```

🧠 Tell the model **what to focus on** and **what to omit**. "Don't restate the numbers" forces interpretation.

## 2. Extract

```
Extract the company name, revenue, and CEO from the text below.
Return as JSON with keys: company, revenue, ceo. If a field is missing, use null.

Text:
"Acme Corp reported $2.4B in 2025 revenue under CEO Jane Doe..."
```

🧠 Asking for **structured output** (JSON) makes the answer easy to parse with `json.loads`.

## 3. Classify

```
Classify the following customer feedback into one of:
[Praise, Bug Report, Feature Request, Billing Issue, Other].
Return only the label.

Feedback:
"The dashboard keeps freezing when I export more than 5,000 rows."
```

## Quality guidelines

- **Be specific.** "Summarize" → vague. "4 bullets, ≤15 words each, focus on risks" → predictable.
- **Show the format.** A one-line example beats two paragraphs of instructions.
- **Cap length.** Use `max_completion_tokens` AND say it in the prompt.
- **Lower temperature for facts.** 0.0–0.3 for analysis. 0.7+ only for ideation.

---

Next: [`03-data-to-prompt.md`](03-data-to-prompt.md).
