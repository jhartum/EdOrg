"""Database models."""

from datetime import datetime
from uuid import UUID

from src.infrastructure.types import BaseStruct


class DBModel(BaseStruct, frozen=True, kw_only=True):
    updated_at: datetime | None = None
    created_at: datetime


class NewsArticle(DBModel, frozen=True):
    id: UUID
    title: str
    description: str

    images_path: list[str]
