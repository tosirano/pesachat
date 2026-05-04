"""SEP-31: Cross-border payments API client."""
from __future__ import annotations


class Sep31Client:
    async def get_info(self, auth_token: str) -> dict:
        raise NotImplementedError

    async def post_transaction(self, auth_token: str, payload: dict) -> dict:
        raise NotImplementedError

    async def get_transaction(self, transaction_id: str, auth_token: str) -> dict:
        raise NotImplementedError
