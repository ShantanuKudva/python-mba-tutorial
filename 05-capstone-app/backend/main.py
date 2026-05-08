"""FastAPI entrypoint for the Excel Insights capstone backend."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import analyze, report, summarize, upload

load_dotenv()

app = FastAPI(
    title="Excel Insights API",
    description="Upload an Excel file. Get metrics, AI summary, and a polished report.",
    version="0.1.0",
)

origins_env = os.getenv("CORS_ORIGINS")
allowed_origins = (
    [o.strip() for o in origins_env.split(",")] if origins_env else ["*"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REPORTS_DIR = Path(__file__).parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)


@app.get("/health")
def health():
    return {"status": "ok", "version": app.version}


app.include_router(upload.router)
app.include_router(analyze.router)
app.include_router(summarize.router)
app.include_router(report.router)
