from tinydb import TinyDB
from src.infrastucture.settings import APP_DIR


async def get_db_session():
    yield TinyDB(APP_DIR / "infrastucture" / "db" / "storage.json")
