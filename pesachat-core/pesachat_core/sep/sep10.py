"""SEP-10: Stellar Web Authentication client."""
from __future__ import annotations


class Sep10Client:
    def __init__(self, anchor_domain: str, network: str) -> None:
        self.anchor_domain = anchor_domain
        self.network = network

    async def authenticate(self, account: str) -> str:
        raise NotImplementedError
