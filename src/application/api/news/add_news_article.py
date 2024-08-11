"""Add news article router."""

import os
import uuid
from datetime import datetime
from typing import Annotated

import msgspec
from litestar import Response, Router, get, post
from litestar.contrib.htmx.response import HTMXTemplate
from litestar.datastructures import UploadFile
from litestar.enums import RequestEncodingType
from litestar.params import Body
from tinydb import TinyDB

from src.application.repository import NewsRepository
from src.infrastructure.db import get_db_session
from src.infrastructure.db import models as db_models
from src.infrastructure.settings import app_settings


class AddNewsArticleFormData(msgspec.Struct):
    title: str
    description: str
    images: list[UploadFile]


@post("/add_news_article_from", name="add_news_article_form")
async def add_news_article_form(
    data: Annotated[
        AddNewsArticleFormData, Body(media_type=RequestEncodingType.MULTI_PART)
    ],
    db_session: TinyDB,
) -> Response:
    repository = NewsRepository(db_session)

    article_id = uuid.uuid4()

    image_by_name = {
        image_name: image.file.read()
        for count, image in enumerate(data.images)
        for image_name in [f'{article_id}_{count}.{image.filename.split('.')[1]}']
    }
    for image_name, image in image_by_name.items():
        image_path = os.path.join(app_settings.static_path / "img" / "news", image_name)
        with open(image_path, "wb") as f:
            f.write(image)

    repository.create_news_article(
        db_models.NewsArticle(
            created_at=datetime.now(),
            id=article_id,
            title=data.title,
            description=data.description,
            images_path=["img/news/" + i for i in image_by_name.keys()],
        )
    )
    return Response(content="Article submitted successfully", status_code=200)


@get("/add_news_article", name="add_news_article_page")
async def add_news_article_page() -> HTMXTemplate:
    """Add news article page."""
    return HTMXTemplate(template_name="news/add_news_article.html")


router = Router(
    route_handlers=[add_news_article_page, add_news_article_form],
    path="/",
    dependencies={"db_session": get_db_session},
)
