"""Helpers used by ex05_module_import.py."""


def format_currency(amount: float, symbol: str = "$") -> str:
    """Return amount as e.g. '$1,234.50'."""
    return f"{symbol}{amount:,.2f}"
