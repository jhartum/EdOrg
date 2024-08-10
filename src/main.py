"""Main entry point for the application."""

from src.application.app import create_app
from src.infrastucture.settings import AppSettings


app_settings = AppSettings.from_env()

app = create_app(app_settings=app_settings)
