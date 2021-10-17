from dataclasses import dataclass, field


@dataclass(repr=True)
class DynamicMemory:
    size: int
    memory: dict = field(default_factory=dict)

    def __setitem__(self, key: int, value: int):
        if key <= self.size:
            self.memory.setdefault(key, value)
        else:
            raise KeyError("Segmentation Fault")

    def __getitem__(self, item: int):
        try:
            value = self.memory[item]
        except KeyError:
            value = 0

        return value
