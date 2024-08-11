from contextlib import asynccontextmanager
import subprocess

from litestar import Litestar
from src.infrastructure import settings


@asynccontextmanager
async def tailwind(app: Litestar):
    try:
        subprocess.run(
            [
                "tailwindcss",
                "-i",
                str(
                    settings.APP_DIR / "infrastructure" / "static" / "css" / "input.css"
                ),
                "-o",
                str(
                    settings.APP_DIR
                    / "infrastructure"
                    / "static"
                    / "css"
                    / "output.css"
                ),
            ]
        )
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield
