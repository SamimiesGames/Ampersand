from ampersand.architectures.aps import flow, registers, math
import ampersand

core = ampersand.Core(16, "aps")

# section _start
core.load(0x1, registers.LDM)
core.load(0x2, 1)
core.load(0x3, registers.STA)
core.load(0x4, registers.STB)

core.load(0x5, math.ADD)


core.memory[core.size] = flow.HLT

core.run()

print(core)

