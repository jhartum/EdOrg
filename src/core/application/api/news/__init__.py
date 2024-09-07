"""News article router."""

from litestar import Router

from src.core.application.api.news.add_news_article import (
    add_news_article_form,
    add_news_article_page,
)
from src.core.application.api.news.delete_news_article import (
    delete_image_from_news_article,
    delete_news_article,
)
from src.core.application.api.news.edit_news_article import (
    edit_news_article_form,
    edit_news_article_page,
)
from src.core.infrastructure.repository.image import get_image_repository
from src.core.infrastructure.repository.news_article import get_news_article_repository

router = Router(
    route_handlers=[
        add_news_article_page,
        add_news_article_form,
        edit_news_article_page,
        edit_news_article_form,
        delete_image_from_news_article,
        delete_news_article,
    ],
    path="/",
    dependencies={
        "news_article_repository": get_news_article_repository,
        "image_repository": get_image_repository,
    },
)
