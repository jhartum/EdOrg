import msgspec


class FrozenStruct(msgspec.Struct, frozen=True, kw_only=True):
    pass


class BaseStruct(FrozenStruct):  # type: ignore
    def to_dict(self):
        return {f: getattr(self, f) for f in self.__struct_fields__}
