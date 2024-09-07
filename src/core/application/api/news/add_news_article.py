"""Add news article router."""

from datetime import datetime
from typing import Annotated

from litestar import Response, get, post
from litestar.contrib.htmx.response import HTMXTemplate
from litestar.datastructures import UploadFile
from litestar.enums import RequestEncodingType
from litestar.params import Body

from src.core.domain.news import NewsArticle
from src.core.infrastructure.repository.image import ImageRepository
from src.core.infrastructure.repository.news_article import NewsArticleRepository
from src.core.infrastructure.types import BaseStruct


class AddNewsArticleFormData(BaseStruct):
    title: str
    description: str
    images: list[UploadFile]


@post("/add_news_article_from", name="add_news_article_form")
async def add_news_article_form(
    data: Annotated[AddNewsArticleFormData, Body(media_type=RequestEncodingType.MULTI_PART)],
    news_article_repository: NewsArticleRepository,
    image_repository: ImageRepository,
) -> Response:
    article_id = news_article_repository.table._get_next_id()

    images = {
        f"{article_id}_{count}.{image_ext}": image
        for count, image in enumerate(data.images)
        for image_ext in [image.filename.split(".")[1]]
    }

    article = NewsArticle(
        created_at=datetime.now(),
        id=article_id,
        title=data.title,
        description=data.description,
        images=list(images.keys()),
    )

    for image_name, image in images.items():
        content = await image.read()
        image_repository.save_file(image_name, content)

    news_article_repository.create(article)

    return Response(content="Article submitted successfully", status_code=200)


@get("/add_news_article", name="add_news_article_page")
async def add_news_article_page() -> HTMXTemplate:
    """Add news article page."""
    return HTMXTemplate(template_name="news/add_news_article.html")
