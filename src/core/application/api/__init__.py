"""Main API router."""

from litestar import Router

from src.core.application.api import command, query
from src.core.infrastructure.repository.image import get_image_repository
from src.core.infrastructure.repository.news_article import get_news_article_repository

router = Router(
    route_handlers=[command.router, query.router],
    path="/",
    dependencies={
        "news_article_repository": get_news_article_repository,
        "image_repository": get_image_repository,
    },
)
