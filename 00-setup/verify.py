"""
Setup verifier. Run after `pip install -r requirements.txt`.

Usage:
    python 00-setup/verify.py
"""

from __future__ import annotations

import importlib
import sys


REQUIRED = [
    ("pandas", "2.0"),
    ("numpy", "1.20"),
    ("openpyxl", "3.0"),
    ("matplotlib", "3.5"),
    ("numpy_financial", "1.0"),
    ("scipy", "1.10"),
    ("statsmodels", "0.13"),
    ("groq", "0.10"),
    ("dotenv", "1.0"),
    ("httpx", "0.25"),
    ("requests", "2.28"),
]


def check_python() -> bool:
    major, minor = sys.version_info[:2]
    ok = (major, minor) >= (3, 10)
    mark = "✅" if ok else "❌"
    print(f"{mark} Python {major}.{minor}.{sys.version_info.micro} (need >= 3.10)")
    return ok


def check_module(name: str, min_version: str) -> bool:
    try:
        mod = importlib.import_module(name)
        version = getattr(mod, "__version__", "?")
        print(f"✅ {name} {version}")
        return True
    except Exception as exc:
        print(f"❌ {name} — {exc}")
        return False


def main() -> int:
    print("Checking your Python environment...\n")
    results = [check_python()]
    for name, min_v in REQUIRED:
        results.append(check_module(name, min_v))
    print()
    if all(results):
        print("🎉 You're ready for Week 1.")
        return 0
    print("Some packages are missing. Run:  pip install -r requirements.txt")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
