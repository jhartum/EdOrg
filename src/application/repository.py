import msgspec
from tinydb import TinyDB, Query
from src.infrastructure.settings import app_settings
from src.infrastructure.db import models
from src.infrastructure.types import BaseStruct


class Entity(BaseStruct, frozen=True):
    pass


class NewsRepository:
    def __init__(self, session: TinyDB) -> None:
        self.session = session
        self.table = self.session.table("news_articles")
        self.query = Query()

    def get(self, id: int):
        instance = self.table.get(self.query.id == id)
        if not instance:
            raise ValueError("No record found")

        return instance

    def create_news_article(self, data: models.NewsArticle):
        data_json = msgspec.json.encode(data)
        self.table.insert(msgspec.json.decode(data_json))

    def update(self, id: int, data: Entity):
        self.table.update(data.to_dict(), self.query.id == id)

    def delete(self, id: int):
        self.table.remove(self.query.id == id)

    def get_all(self):
        return self.table.all()


async def provide_news_repository():
    yield NewsRepository(TinyDB(app_settings.db_path / "storage.json"))
