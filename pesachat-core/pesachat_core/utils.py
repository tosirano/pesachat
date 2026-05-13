"""Utility helpers for pesachat_core."""
from __future__ import annotations

from decimal import Decimal


def format_amount(amount: Decimal, asset_code: str) -> str:
    """Format a Stellar asset amount for display.

    Args:
        amount: The raw decimal amount.
        asset_code: The Stellar asset code (e.g. `"USDC"`).

    Returns:
        A human-readable string such as `"10.50 USDC"`.
    """
    return f"{amount:.2f} {asset_code}"