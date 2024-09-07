from src.core.infrastructure.types import Entity


class NewsArticle(Entity):
    """Domain model for news articles."""

    title: str
    description: str
    images: list[str]
