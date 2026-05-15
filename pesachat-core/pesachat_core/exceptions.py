class PesaChatError(Exception):
    """Base exception for all PesaChat errors."""


class AnchorError(PesaChatError):
    """Raised when an anchor operation fails."""


class AuthError(PesaChatError):
    """Raised when authentication or authorisation fails."""