"""Settings module."""

import os
from pathlib import Path

import msgspec
from dotenv import load_dotenv

APP_DIR = Path(__file__).resolve().parent.parent


class AppSettings(msgspec.Struct):
    """Settings for the application."""

    debug: bool = False
    root_dir: Path = APP_DIR
    db_path: Path = APP_DIR / "infrastructure" / "db"

    @classmethod
    def from_env(
        cls, env_file: Path = Path(".env"), prefix: str = "APP_"
    ) -> "AppSettings":
        """Load settings from environment variables."""
        load_dotenv(env_file, verbose=True)
        transformed_keys = {
            k.replace(prefix, "").lower(): v
            for k, v in os.environ.items()
            if k.startswith(prefix)
        }
        return msgspec.convert(
            transformed_keys,
            type=AppSettings,
            strict=False,
        )
