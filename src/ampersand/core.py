from ampersand.memory import DynamicMemory
from ampersand.architectures import ARCHITECTURES
from ampersand.utypes import UIntr
from ampersand.utils import sizeof

import click


__all__ = [
    "Core"
]


class Core:
    def __init__(self, bits: int, architecture: str):
        self.size = sizeof.in_bits(bits)

        self.a, self.b, self.c = 0, 0, 0
        self.z, self.o, self.u = False, False, False

        self.architecture = ARCHITECTURES[architecture]

        vectors = self.architecture["vectors"]
        self.pc_vector, self.sp_vector = vectors["pc"], vectors["sp"]

        self.pc, self.sp = self.pc_vector, self.sp_vector

        self.memory = DynamicMemory(self.size)

    def load(self, index, instruc):
        self.memory[index] = instruc

    def reset(self):
        self.a, self.b, self.c = 0, 0, 0
        self.z, self.o, self.u = False, False, False
        self.pc = self.pc_vector
        self.sp = self.sp_vector

    def run(self):
        print("running...")
        while self.pc < self.size:
            optcode = self.memory[self.pc]
            instruc = self.architecture[optcode]

            if isinstance(instruc, UIntr):
                if instruc.breaks:
                    break
            else:
                instruc(self)

            self.pc += 1

    def __str__(self):
        return f"{self.__class__.__name__}\n{self.a = } {self.b = } {self.c = }\n{self.z = } {self.o = } {self.u = }"
