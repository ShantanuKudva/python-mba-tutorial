"""GET /report/{file_id} — return a polished xlsx report."""

from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

import store
from pipelines.report_writer import write_report

router = APIRouter(tags=["report"])

REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"


@router.get("/report/{file_id}")
def get_report(file_id: str):
    stored = store.get(file_id)
    if not stored:
        raise HTTPException(status_code=404, detail="file_id not found")
    if not stored.metrics:
        raise HTTPException(
            status_code=400,
            detail="No metrics yet. Call /analyze first.",
        )

    if stored.report_path is None or not stored.report_path.exists():
        out_path = REPORTS_DIR / f"{file_id}.xlsx"
        write_report(
            metrics=stored.metrics,
            summary=stored.summary or "",
            source_path=stored.path,
            out_path=out_path,
        )
        stored.report_path = out_path

    return FileResponse(
        path=stored.report_path,
        media_type=(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ),
        filename=f"{stored.original_name.rsplit('.', 1)[0]}_report.xlsx",
    )
