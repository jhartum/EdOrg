"""Settings module."""

import os
from pathlib import Path

import msgspec
from dotenv import load_dotenv

APP_DIR = Path(__file__).resolve().parent.parent


class AppSettings(msgspec.Struct):
    """Settings for the application."""

    admin_username: str
    admin_password: str

    debug: bool = False
    root_dir: Path = APP_DIR
    db_path: Path = APP_DIR / "infrastructure" / "db"
    session_store_path: Path = APP_DIR / "infrastructure" / "db" / "session_data"

    static_path: Path = APP_DIR / "infrastructure" / "static"
    templates_path: Path = APP_DIR / "infrastructure" / "templates"

    @classmethod
    def from_env(cls, env_file: Path = Path(".env"), prefix: str = "APP_") -> "AppSettings":
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


app_settings = AppSettings.from_env()
from rich import print

print(app_settings)
