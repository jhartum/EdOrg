"""Command news router."""

from litestar import Router

from src.core.application.api.command.news.add import add_news_article_form, add_news_article_page
from src.core.application.api.command.news.delete import (
    delete_image_from_news_article,
    delete_news_article,
)
from src.core.application.api.command.news.edit import (
    edit_news_article_form,
    edit_news_article_page,
)

router = Router(
    route_handlers=[
        add_news_article_form,
        add_news_article_page,
        delete_image_from_news_article,
        delete_news_article,
        edit_news_article_form,
        edit_news_article_page,
    ],
    path="/",
)
