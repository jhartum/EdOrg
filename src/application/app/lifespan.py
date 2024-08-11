from contextlib import asynccontextmanager
import subprocess

from litestar import Litestar
from src.infrastructure.settings import app_settings


@asynccontextmanager
async def tailwind(app: Litestar):
    try:
        subprocess.run(
            [
                "tailwindcss",
                "-i",
                str(app_settings.static_path / "assets" / "css" / "input.css"),
                "-o",
                str(app_settings.static_path / "assets" / "css" / "output.css"),
            ]
        )
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield
