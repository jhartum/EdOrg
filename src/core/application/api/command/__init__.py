"""Comamnd main router."""

from litestar import Router

from src.core.application.api.command import news

router = Router(route_handlers=[news.router], path="/")
