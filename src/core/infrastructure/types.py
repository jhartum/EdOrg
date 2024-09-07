from datetime import datetime
from typing import Any

import msgspec

ID = int


class FrozenStruct(msgspec.Struct, frozen=True):
    pass


class BaseStruct(FrozenStruct):  # type: ignore
    def to_dict(self, exclude: set[str] = set()) -> dict:
        return {f: getattr(self, f) for f in self.__struct_fields__ if f not in exclude}


class Entity(BaseStruct, kw_only=True):
    id: ID
    created_at: datetime
    updated_at: datetime | None = None

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return False


class AggregateRoot(Entity):
    pass
