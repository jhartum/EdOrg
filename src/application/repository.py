import msgspec
from tinydb import Query, TinyDB

from src.infrastructure.settings import app_settings


class Entity(msgspec.Struct):
    def to_dict(self):
        return {f: getattr(self, f) for f in self.__struct_fields__}


class Repository:
    def __init__(self, session: TinyDB, table: str) -> None:
        self.session = session
        self.table = self.session.table(table)
        self.query = Query()

    def get(self, id: int):
        instance = self.table.get(self.query.id == id)
        if not instance:
            raise ValueError("No record found")

        return instance

    def create(self, data: Entity):
        self.table.insert(data.to_dict())

    def update(self, id: int, data: Entity):
        self.table.update(data.to_dict(), self.query.id == id)

    def delete(self, id: int):
        self.table.remove(self.query.id == id)

    def get_all(self):
        return self.table.all()


async def provide_news_repository():
    yield Repository(TinyDB(app_settings.db_path / "storage.json"), "news_articles")
