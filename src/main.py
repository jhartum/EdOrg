"""Main entry point for the application."""

from src.application.app import create_app
from src.infrastructure.settings import app_settings


app = create_app(app_settings=app_settings)
