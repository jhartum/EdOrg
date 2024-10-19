"""Query main router."""

from litestar import Router

from src.core.application.api.query import index, news

router = Router(
    route_handlers=[news.router, index.router],
    path="/",
)
