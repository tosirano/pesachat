"""SEP-31: Cross-border payments (direct payment) protocol client.

SEP-31 defines a standard for Stellar-based cross-border payment flows where a
sending anchor initiates a direct payment on behalf of a sender to a receiving
anchor that then disburses funds to the final recipient.

Typical flow
------------
1. Discover anchor capabilities via get_info — returns supported asset pairs,
   required sender/receiver KYC fields, and fee schedules.
2. Ensure the sender is KYC-verified with the receiving anchor using SEP-10
   (authentication) and SEP-12 (KYC).
3. Open a transaction with post_transaction — the anchor returns a
   transaction_id and a Stellar account to send funds to.
4. Poll get_transaction until the transaction reaches a terminal state
   (completed or error).
"""
from __future__ import annotations


class Sep31Client:
    async def get_info(self, auth_token: str) -> dict:
        raise NotImplementedError

    async def post_transaction(self, auth_token: str, payload: dict) -> dict:
        raise NotImplementedError

    async def get_transaction(self, transaction_id: str, auth_token: str) -> dict:
        raise NotImplementedError
