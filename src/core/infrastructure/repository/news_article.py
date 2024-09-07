import msgspec
from tinydb import Query
from tinydb.table import Document

from src.core.domain.news import NewsArticle
from src.core.infrastructure.db import DBSession
from src.core.infrastructure.settings import app_settings


class NewsArticleRepository:
    def __init__(self) -> None:
        self.session = DBSession(app_settings.db_path)
        self.table = self.session.table("news_articles")
        self.news_article = Query()

    def get(self, id: int) -> NewsArticle:
        instance = self.table.get(doc_id=id)

        if not instance:
            raise ValueError("No record found")

        return msgspec.convert(instance, NewsArticle)

    def get_all(self):
        return self.table.all()

    def create(self, data: NewsArticle):
        data_json = msgspec.json.encode(data.to_dict())

        self.table.insert(Document(msgspec.json.decode(data_json), doc_id=data.id))

    def update(self, data: NewsArticle):
        data_json = msgspec.json.encode(data.to_dict())

        self.table.update(Document(msgspec.json.decode(data_json), doc_id=data.id))

    def delete(self, id: int):
        self.table.remove(doc_ids=[id])


async def get_news_article_repository():
    yield NewsArticleRepository()
