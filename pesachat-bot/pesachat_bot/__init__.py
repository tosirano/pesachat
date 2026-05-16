from __future__ import annotations


class PesaChatBot:
    """Telegram bot for cross-border remittance powered by the Stellar network.

    Handles incoming Telegram updates, routes commands to the appropriate
    handlers, and delegates all on-chain operations to *pesachat-core* via HTTP.

    Args:
        token: Telegram Bot API token issued by @BotFather.
        core_url: Base URL of the running pesachat-core service
            (e.g. ``http://localhost:8000``).
        locale: BCP-47 language tag used for localised response strings.
            Defaults to ``"en"``.
    """

    def __init__(self, token: str, core_url: str, locale: str = "en") -> None:
        self.token = token
        self.core_url = core_url
        self.locale = locale
