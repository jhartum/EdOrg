"""Main entry point for the application."""

from src.core.infrastructure.app import create_app
from src.core.infrastructure.settings import app_settings

app = create_app(app_settings=app_settings)
