"""Main router."""

from litestar import Router, get
from litestar.contrib.htmx.response import HTMXTemplate
from tinydb import TinyDB


from src.application.repository import Repository


@get("/", name="index")
async def index(db_session: TinyDB) -> HTMXTemplate:
    """Index page."""
    news_repository = Repository(db_session, "news_articles")

    return HTMXTemplate(
        template_name="index.html",
        context={"articles": news_repository.get_all()[:2]},
    )


index_router = Router(
    route_handlers=[
        index,
    ],
    path="/",
)
