from src.application.repository import Entity


class NewsArticle(Entity):
    """Domain model for news articles."""

    id: int
    title: str
    description: str

    image_path: str

    @classmethod
    def description_to_html(cls, text: str) -> str:
        return "<p>" + text.replace("\n", "<br>") + "</p>"
