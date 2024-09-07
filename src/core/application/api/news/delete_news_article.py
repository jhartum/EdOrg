"""Delete news article router."""

from typing import Annotated

import msgspec
from litestar import Response, delete, post
from litestar.contrib.htmx.response import ClientRefresh
from litestar.enums import RequestEncodingType
from litestar.params import Body

from src.core.domain.news import NewsArticle
from src.core.infrastructure.repository.image import ImageRepository
from src.core.infrastructure.repository.news_article import NewsArticleRepository


class DeleteImageFromNewsArticleFormData(msgspec.Struct):
    article_id: int
    image: str


@post("delete_image_from_news_article", name="delete_image_from_news_article")
async def delete_image_from_news_article(
    data: Annotated[
        DeleteImageFromNewsArticleFormData, Body(media_type=RequestEncodingType.URL_ENCODED)
    ],
    news_article_repository: NewsArticleRepository,
    image_repository: ImageRepository,
) -> Response:
    old_state = news_article_repository.get(data.article_id)
    image_repository.delete_file(data.image)
    news_article_repository.update(
        NewsArticle(
            **old_state.to_dict(exclude={"images"}),
            images=[i for i in old_state.images if i != data.image],
        )
    )
    return ClientRefresh()


@delete("delete_news_article/{article_id:int}", name="delete_news_article", status_code=200)
async def delete_news_article(
    article_id: int,
    news_article_repository: NewsArticleRepository,
    image_repository: ImageRepository,
) -> Response:
    article = news_article_repository.get(article_id)

    for image in article.images:
        image_repository.delete_file(image)
    news_article_repository.delete(article.id)

    return ClientRefresh()
