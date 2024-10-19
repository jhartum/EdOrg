"""Query index router."""

from litestar import Router, get
from litestar.contrib.htmx.response import HTMXTemplate

from src.core.infrastructure.repository.news_article import (
    NewsArticlePaginator,
    NewsArticleRepository,
)


@get("/", name="index", exclude_from_auth=True)
async def index_page(news_article_repository: NewsArticleRepository) -> HTMXTemplate:
    """Index page."""

    paginator = NewsArticlePaginator(news_article_repository)(1, 0)

    return HTMXTemplate(template_name="index.html", context=dict(data={"paginator": paginator}))


router = Router(route_handlers=[index_page], path="/")
