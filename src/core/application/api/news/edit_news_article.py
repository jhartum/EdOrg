"""Edit news article router."""

from typing import Annotated

import msgspec
from litestar import Response, get, post
from litestar.contrib.htmx.response import ClientRefresh, HTMXTemplate
from litestar.datastructures import UploadFile
from litestar.enums import RequestEncodingType
from litestar.params import Body

from src.core.domain.news import NewsArticle
from src.core.infrastructure.repository.image import ImageRepository
from src.core.infrastructure.repository.news_article import NewsArticleRepository


class EditNewsArticleFormData(msgspec.Struct):
    title: str
    description: str
    images: list[UploadFile] = []


@post("edit_news_article_form/{article_id:int}", name="edit_news_article_form")
async def edit_news_article_form(
    article_id: int,
    data: Annotated[EditNewsArticleFormData, Body(media_type=RequestEncodingType.MULTI_PART)],
    news_article_repository: NewsArticleRepository,
    image_repository: ImageRepository,
) -> Response:
    old_state = news_article_repository.get(article_id)

    new_images = {
        f"{article_id}_{count+len(old_state.images)}.{image_ext}": image
        for count, image in enumerate(data.images)
        for image_ext in [image.filename.split(".")[1]]
    }
    new_state = NewsArticle(
        **old_state.to_dict(exclude={"title", "description", "images"}),
        title=data.title,
        description=data.description,
        images=old_state.images + list(new_images.keys()),
    )

    for image_name, image in new_images.items():
        content = await image.read()
        image_repository.save_file(image_name, content)
    news_article_repository.update(new_state)

    return ClientRefresh()


class DeleteImageFromNewsArticleFormData(msgspec.Struct):
    article_id: int
    image_path: str


@post("delete_image_from_news_article", name="delete_image_from_news_article")
async def delete_image_from_news_article(
    data: Annotated[
        DeleteImageFromNewsArticleFormData, Body(media_type=RequestEncodingType.URL_ENCODED)
    ],
    news_article_repository: NewsArticleRepository,
    image_repository: ImageRepository,
) -> Response:
    old_state = news_article_repository.get(data.article_id)

    image_repository.delete_file(data.image_path)
    news_article_repository.update(
        NewsArticle(
            **old_state.to_dict(exclude={"images_path"}),
            images=[i for i in old_state.images if i != data.image_path],
        )
    )

    return ClientRefresh()


@get("news_articles/{article_id:int}", name="/news_articles")
async def edit_news_article_page(
    article_id: int,
    news_article_repository: NewsArticleRepository,
) -> HTMXTemplate:
    """Edit news article page."""
    article = news_article_repository.get(article_id)
    return HTMXTemplate(
        template_name="news/edit_news_article.html", context={"article": article.to_dict()}
    )
