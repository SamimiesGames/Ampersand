from dataclasses import dataclass, field
from .utypes import UInt


@dataclass(repr=True)
class DynamicMemory:
    size: int
    memory: dict = field(default_factory=dict)

    def __setitem__(self, key: UInt, value: UInt):
        self.memory.setdefault(key.value, value.value)

    def __getitem__(self, item: UInt):
        try:
            value = self.memory[item.value]
        except KeyError:
            value = 0

        return value
