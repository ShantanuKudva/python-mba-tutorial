"""POST /summarize — feed metrics into Groq, get a narrative back."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import store
from llm.groq_client import summarize_metrics

router = APIRouter(tags=["summarize"])


class SummarizeRequest(BaseModel):
    file_id: str
    focus: str | None = None    # optional steering ("financial health", "growth risk", etc.)


class SummarizeResponse(BaseModel):
    file_id: str
    summary: str
    model: str


@router.post("/summarize", response_model=SummarizeResponse)
def summarize(req: SummarizeRequest) -> SummarizeResponse:
    stored = store.get(req.file_id)
    if not stored:
        raise HTTPException(status_code=404, detail="file_id not found")
    if not stored.metrics:
        raise HTTPException(
            status_code=400,
            detail="No metrics yet. Call /analyze first.",
        )

    text, model = summarize_metrics(stored.metrics, focus=req.focus)
    stored.summary = text

    return SummarizeResponse(file_id=req.file_id, summary=text, model=model)
