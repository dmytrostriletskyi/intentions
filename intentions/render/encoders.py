from __future__ import annotations

from enum import Enum
from json import JSONEncoder
from typing import Union


class JsonEncoderWithEnumSupport(JSONEncoder):

    def default(self, obj: Union[Enum, object]) -> object:
        if isinstance(obj, Enum):
            return obj.value

        return super().default(obj)
