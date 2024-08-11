from tinydb import TinyDB

from src.infrastructure.settings import app_settings


async def get_db_session():
    yield TinyDB(app_settings.db_path / "storage.json")
