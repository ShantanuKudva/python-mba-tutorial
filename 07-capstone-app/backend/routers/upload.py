"""POST /upload — accepts an .xlsx and returns a file_id."""

from __future__ import annotations

import uuid
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

import store

router = APIRouter(tags=["upload"])

UPLOAD_DIR = Path(__file__).resolve().parent.parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_EXTS = {".xlsx", ".xls"}


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)) -> dict:
    """
    Accept an Excel file. Persist it to disk. Return a file_id the client
    can use for /analyze, /summarize, and /report.
    """
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in ALLOWED_EXTS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type {suffix}. Use .xlsx or .xls.",
        )

    file_id = uuid.uuid4().hex[:12]
    out_path = UPLOAD_DIR / f"{file_id}{suffix}"
    contents = await file.read()
    out_path.write_bytes(contents)

    store.put(
        store.StoredFile(
            file_id=file_id,
            original_name=file.filename or out_path.name,
            path=out_path,
        )
    )

    return {
        "file_id": file_id,
        "original_name": file.filename,
        "size_bytes": len(contents),
    }
