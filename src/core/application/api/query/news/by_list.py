"""Get news articles by list endpoints."""

from litestar import get
from litestar.contrib.htmx.response import HTMXTemplate

from src.core.infrastructure.repository.news_article import (
    NewsArticlePaginator,
    NewsArticleRepository,
)


@get("get_news_articles", name="get_news_articles", exclude_from_auth=True)
async def get_news_articles(
    page: int, news_article_repository: NewsArticleRepository
) -> HTMXTemplate:
    """News Articles template."""
    paginator = NewsArticlePaginator(news_article_repository)(1, page)

    return HTMXTemplate(
        template_name="news_article/news_articles.html",
        context=dict(data={"paginator": paginator}),
    )
