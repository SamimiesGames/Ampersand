from .memory import DynamicMemory
from .backends import BACKENDS
from .utypes import UInt, UIntr
from .utils import sizeof

import click


__all__ = [
    "Core"
]


class Core:
    def __init__(self, bits: int, backend: str):
        self.size = sizeof.in_bits(bits)

        self.a, self.b, self.c = UInt(0, self.size), UInt(0, self.size), UInt(0, self.size)
        self.z, self.o, self.u = False, False, False

        self.backend = BACKENDS[backend]

        vectors = self.backend["vectors"]
        self.pc_vector, self.sp_vector = UInt(vectors["pc"], self.size), UInt(vectors["sp"], self.size)

        self.pc, self.sp = UInt(self.pc_vector.value, self.size), UInt(self.sp_vector.value, self.size)

        self.memory = DynamicMemory(self.size)

    def reset(self):
        self.a.value, self.b.value, self.c.value = 0, 0, 0
        self.z, self.o, self.u = False, False, False
        self.pc.value = self.pc_vector
        self.sp.value = self.sp_vector

    def run(self):
        print("running...")
        while self.pc < self.size:
            value = self.memory[self.pc]
            instruc = self.backend[value]

            if isinstance(instruc, UIntr):
                if instruc.breaks:
                    break
            else:
                instruc(self)

            self.pc += 1

    def __str__(self):
        return f"{self.__class__.__name__}\n{self.a = } {self.b = } {self.c = }\n{self.z = } {self.o = } {self.u = }"
