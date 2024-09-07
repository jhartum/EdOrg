from pathlib import Path

from src.core.infrastructure.settings import app_settings


class ImageRepository:
    def __init__(self):
        self.base_dir = app_settings.db_dir / "news_article_images"
        Path(self.base_dir).mkdir(exist_ok=True)

    def save_file(self, file_name: str, file_content: bytes):
        with open(self.base_dir / file_name, "wb") as f:
            f.write(file_content)

    def delete_file(self, file_name: str):
        if (file := Path(self.base_dir / file_name)).exists():
            file.unlink()
        else:
            raise ValueError("Image not found")

    def get_file_content(self, file_name: str):
        if (file := Path(self.base_dir / file_name)).exists():
            file.unlink()
        else:
            raise ValueError("Image not found")


async def get_image_repository():
    yield ImageRepository()
