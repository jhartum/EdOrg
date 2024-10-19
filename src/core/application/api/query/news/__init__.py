"""Query news router."""

from litestar import Router

from src.core.application.api.query.news.by_list import get_news_articles

router = Router(route_handlers=[get_news_articles], path="/")
