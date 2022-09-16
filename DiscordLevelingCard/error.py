class DiscordLevelingCardError(Exception):
    """Base exception for :class:`DiscordLevelingCard`"""
    def __init__(self, message: str):
        super().__init__(message)

class InvalidImageType(DiscordLevelingCardError):
    """Raised when the image type is not supported"""
    def __init__(self, message: str):
        super().__init__(message)

class InvalidImageUrl(DiscordLevelingCardError):
    """Raised when the image URL is invalid"""
    def __init__(self, message: str):
        super().__init__(message)