"""Pytest configuration and shared fixtures."""
from __future__ import annotations

import pytest


@pytest.fixture
def stellar_network() -> str:
    return "testnet"