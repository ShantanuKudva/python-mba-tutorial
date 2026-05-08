"""POST /analyze — run a domain-specific pandas pipeline on an uploaded file."""

from __future__ import annotations

from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import store
from pipelines import finance, marketing, operations, strategy

router = APIRouter(tags=["analyze"])

Domain = Literal["finance", "marketing", "operations", "strategy"]

PIPELINES = {
    "finance": finance.run,
    "marketing": marketing.run,
    "operations": operations.run,
    "strategy": strategy.run,
}


class AnalyzeRequest(BaseModel):
    file_id: str
    domain: Domain


class AnalyzeResponse(BaseModel):
    file_id: str
    domain: Domain
    metrics: dict
    headline: str


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest) -> AnalyzeResponse:
    stored = store.get(req.file_id)
    if not stored:
        raise HTTPException(status_code=404, detail="file_id not found")

    runner = PIPELINES[req.domain]
    result = runner(stored.path)

    stored.metrics = result["metrics"]
    return AnalyzeResponse(
        file_id=req.file_id,
        domain=req.domain,
        metrics=result["metrics"],
        headline=result["headline"],
    )
