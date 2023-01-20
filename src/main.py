from ampersand.architectures.aps import flow, registers, math, stack
import ampersand

core = ampersand.Core(16, "aps")

# section _start
core.load(0x1, registers.LDM)
core.load(0x2, 1)
core.load(0x3, registers.STA)

# section .data
core.load(0x6, math.ADD)
core.load(0x7, stack.PSH)

core.load(0x8, registers.LDB)
core.load(0x9, registers.STA)

core.load(0xa, stack.POP)
core.load(0xb, registers.STB)

# footer
core.memory[core.size] = flow.HLT

core.run()

print(core)

