"""
In-memory store for uploaded files and analysis results.

NOT production-grade — restarts wipe state. For a real deployment, swap this
out for S3 (files) and a database / Redis (metadata).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class StoredFile:
    file_id: str
    original_name: str
    path: Path
    metrics: dict[str, Any] = field(default_factory=dict)
    summary: str | None = None
    report_path: Path | None = None


_FILES: dict[str, StoredFile] = {}


def put(stored: StoredFile) -> None:
    _FILES[stored.file_id] = stored


def get(file_id: str) -> StoredFile | None:
    return _FILES.get(file_id)


def all_ids() -> list[str]:
    return list(_FILES.keys())
