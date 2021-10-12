from .memory import DynamicMemory
from .instruc import BACKENDS
from .utypes import UInt, UIntr


class Core:
    def __init__(self, bits: int, backend: str):
        print(f"Creating Virtual Machine with {backend = } {bits = }")
        self.size = bits ** 2

        self.a, self.b, self.c = UInt(0, self.size), UInt(0, self.size), UInt(0, self.size)
        self.z, self.o, self.u = False, False, False

        self.pc, self.sp = UInt(0, self.size), UInt(0, self.size)

        self.backend = BACKENDS[backend]

        self.memory = DynamicMemory(self.size)

    def run(self):
        while self.pc <= self.size:
            value = self.memory[self.pc]
            instruc = self.backend[value]

            if isinstance(instruc, UIntr):
                if instruc.breaks:
                    break
            else:
                instruc(self)

            self.pc += 1
        print("exit")
