import logging

logger = logging.getLogger(__name__)


class PesaChatBot:
    """A Telegram bot for cross-border remittance on the Stellar network.

    Handles user interactions for sending and receiving money across borders
    using Stellar-based stablecoins. Integrates with pesachat-core for
    SEP-10 authentication, SEP-24 anchor deposits, and SEP-31 direct payments.

    Args:
        token (str): Telegram Bot API token obtained from BotFather.
        network (str): Stellar network to connect to. Either ``"testnet"``
            or ``"public"``. Defaults to ``"testnet"``.
        anchor_domain (str): Domain of the Stellar anchor used for fiat
            on-ramp and off-ramp operations. Defaults to
            ``"testanchor.stellar.org"``.
    """

    def __init__(
        self,
        token: str,
        network: str = "testnet",
        anchor_domain: str = "testanchor.stellar.org",
    ) -> None:
        self.token = token
        self.network = network
        self.anchor_domain = anchor_domain


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logger.info("pesachat-bot starting")


if __name__ == "__main__":
    main()