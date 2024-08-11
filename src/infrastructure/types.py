import msgspec


class BaseStruct(msgspec.Struct, frozen=True, kw_only=True):
    def to_dict(self):
        return {f: getattr(self, f) for f in self.__struct_fields__}
