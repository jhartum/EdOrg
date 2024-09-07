import subprocess
from contextlib import asynccontextmanager

from litestar import Litestar

from src.core.infrastructure.settings import app_settings


@asynccontextmanager
async def tailwind(app: Litestar):
    try:
        subprocess.run(
            [
                "tailwindcss",
                "-i",
                str(app_settings.static_dir / "css" / "input.css"),
                "-o",
                str(app_settings.static_dir / "assets" / "css" / "output.css"),
            ]
        )
    except Exception as e:
        print(f"Error running tailwindcss: {e}")  # noqa: T201

    yield
