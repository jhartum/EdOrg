"""Index router."""

from litestar import Router, get
from litestar.contrib.htmx.response import HTMXTemplate

from src.core.infrastructure.repository.news_article import (
    NewsArticleRepository,
    get_news_article_repository,
)


@get("/", name="index", exclude_from_auth=True)
async def index(news_article_repository: NewsArticleRepository) -> HTMXTemplate:
    """Index page."""

    return HTMXTemplate(
        template_name="index.html",
        context={
            "articles": sorted(
                [dict(art) for art in news_article_repository.get_all()[:2]],
                key=lambda art: art["created_at"],
                reverse=True,
            )
        },
    )


router = Router(
    route_handlers=[index],
    path="/",
    dependencies={"news_article_repository": get_news_article_repository},
)
