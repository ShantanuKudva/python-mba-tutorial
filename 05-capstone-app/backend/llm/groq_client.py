"""
Groq client wrapper.

🛠️  STUB — currently returns mock narrative if no API key is set, OR a real
     Groq call if GROQ_API_KEY is present. Tune the prompt in week 12.
"""

from __future__ import annotations

import json
import os
from typing import Any

DEFAULT_MODEL = "llama-3.3-70b-versatile"


def _build_prompt(metrics: dict[str, Any], focus: str | None) -> str:
    focus_line = f"Focus: {focus}." if focus else "Focus on what is unusual or actionable."
    return f"""You are a senior business analyst writing a one-page executive summary.

Given the metrics below, produce 5 bullet points (≤20 words each).
{focus_line}
Do not restate the numbers verbatim — interpret them.

Metrics (JSON):
{json.dumps(metrics, indent=2, default=str)}
"""


def summarize_metrics(
    metrics: dict[str, Any],
    focus: str | None = None,
    model: str = DEFAULT_MODEL,
) -> tuple[str, str]:
    """
    Return (summary_text, model_name).

    If GROQ_API_KEY is unset, returns a deterministic mock so the app keeps working.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key.startswith("replace_"):
        return (
            "(MOCK summary — set GROQ_API_KEY in .env to get a real one.)\n"
            "• Strong fundamentals overall.\n"
            "• Watch the leverage ratio trend.\n"
            "• Concentration risk in top segment.\n"
            "• Cash conversion appears healthy.\n"
            "• Recommend monthly review cadence.",
            f"{model} (mock)",
        )

    try:
        from groq import Groq

        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a concise senior analyst."},
                {"role": "user", "content": _build_prompt(metrics, focus)},
            ],
            temperature=0.2,
            max_completion_tokens=400,
        )
        return response.choices[0].message.content or "", model
    except Exception as exc:
        return (
            f"(LLM error — falling back to mock. Reason: {exc})\n"
            "• Could not reach the Groq API.\n"
            "• Check your key and rate limits.",
            f"{model} (error)",
        )
