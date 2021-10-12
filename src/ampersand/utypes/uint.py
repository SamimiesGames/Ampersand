from typing import Union


class UInt:
    def __init__(self, value: Union[int, float], bits: Union[int, float]):
        self.value = value
        self.bits = bits

        self._format()

    def _format(self):
        self.value = self.bits if self.value > self.bits else self.value
        self.value = -self.bits if self.value < -self.bits else self.value

    @staticmethod
    def _format_other(other) -> int:
        if hasattr(other, "value"):
            return other.value
        else:
            return other

    def __add__(self, other):
        value = self._format_other(other)
        return UInt(self.value + value, self.bits)

    def __sub__(self, other):
        value = self._format_other(other)
        return UInt(self.value - value, self.bits)

    def __mul__(self, other):
        value = self._format_other(other)
        return UInt(self.value * value, self.bits)

    def __divmod__(self, other):
        value = self._format_other(other)
        return UInt(self.value / value, self.bits)

    def __lt__(self, other):
        value = self._format_other(other)
        return self.value < value

    def __le__(self, other):
        value = self._format_other(other)
        return self.value <= value

    def __eq__(self, other):
        value = self._format_other(other)
        return self.value == value

    def __repr__(self):
        return f"<{self.__class__.__name__}, {self.value=}, {self.bits}>"
