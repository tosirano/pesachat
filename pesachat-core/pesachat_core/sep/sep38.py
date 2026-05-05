"""SEP-38: Quotes API client."""
from __future__ import annotations

from typing import Any


class Sep38Client:
    async def get_prices(self, sell_asset: str, sell_amount: str) -> dict[str, Any]:
        raise NotImplementedError

    async def post_quote(self, payload: dict[str, Any], auth_token: str) -> dict[str, Any]:
        raise NotImplementedError