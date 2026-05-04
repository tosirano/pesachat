"""SEP-12: KYC API client."""
from __future__ import annotations


class Sep12Client:
    async def get_customer(self, account: str, auth_token: str) -> dict:
        raise NotImplementedError

    async def put_customer(self, account: str, auth_token: str, fields: dict) -> dict:
        raise NotImplementedError
