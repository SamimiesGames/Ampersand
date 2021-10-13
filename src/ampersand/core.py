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
        click.secho(f"I: Create AVM", fg="cyan", bold=True)
        self.size = sizeof.in_bits(bits)

        self.a, self.b, self.c = UInt(0, self.size), UInt(0, self.size), UInt(0, self.size)
        self.z, self.o, self.u = False, False, False

        self.backend = BACKENDS[backend]

        vectors = self.backend["vectors"]
        pc_vector, sp_vector = vectors["pc"], vectors["sp"]

        self.pc, self.sp = UInt(pc_vector, self.size), UInt(sp_vector, self.size)

        self.memory = DynamicMemory(self.size)

    def run(self):
        while self.pc < self.size:
            value = self.memory[self.pc]
            instruc = self.backend[value]

            if isinstance(instruc, UIntr):
                if instruc.breaks:
                    break
            else:
                instruc(self)

            self.pc += 1
