"""SEP-38: Quotes API client."""
from __future__ import annotations


class Sep38Client:
    async def get_prices(self, sell_asset: str, sell_amount: str) -> dict:
        raise NotImplementedError

    async def post_quote(self, payload: dict, auth_token: str) -> dict:
        raise NotImplementedError
