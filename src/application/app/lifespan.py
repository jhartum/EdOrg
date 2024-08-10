from contextlib import asynccontextmanager
import subprocess

from litestar import Litestar
from src.infrastucture import settings


@asynccontextmanager
async def tailwind(app: Litestar):
    try:
        subprocess.run(
            [
                "tailwindcss",
                "-i",
                str(
                    settings.APP_DIR / "infrastucture" / "static" / "css" / "input.css"
                ),
                "-o",
                str(
                    settings.APP_DIR / "infrastucture" / "static" / "css" / "output.css"
                ),
            ]
        )
    except Exception as e:
        print(f"Error running tailwindcss: {e}")

    yield
