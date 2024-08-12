"""router."""

from litestar import Router, get
from litestar.contrib.htmx.response import HTMXTemplate
from tinydb import TinyDB

from src.application.repository import Repository
from src.infrastructure.db import get_db_session


@get("/add_news_article", name="add_news_article_page")
async def add_news_article_page(db_session: TinyDB) -> HTMXTemplate:
    """Index page."""
    Repository(db_session, "news_articles")

    return HTMXTemplate(
        template_name="add_news_article.html",
        # context={"articles": news_repository.get_all()[:2]},
    )


router = Router(
    route_handlers=[
        add_news_article_page,
    ],
    path="/",
    dependencies={"db_session": get_db_session},
)
