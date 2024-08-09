"""Main entry point for the application."""

from src.app import create_app
from src.settings import AppSettings


app_settings = AppSettings.from_env()

app = create_app(app_settings=app_settings)
