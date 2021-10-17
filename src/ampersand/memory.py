from dataclasses import dataclass, field
from .utypes import UInt

from typing import Union


@dataclass(repr=True)
class DynamicMemory:
    size: int
    memory: dict = field(default_factory=dict)

    def __setitem__(self, key: Union[UInt, int], value: Union[UInt, int]):
        key, value = UInt.format_other(key), UInt.format_other(value)
        print(type(key), type(value))
        self.memory.setdefault(key, value)

    def __getitem__(self, item: UInt):
        try:
            value = self.memory[item.value]
        except KeyError:
            value = 0

        return value
