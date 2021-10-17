from ampersand.backends.aps import flow, registers
import ampersand

core = ampersand.Core(16, "aps")

core.memory[core.pc_vector + 1] = registers.LDM
core.memory[core.pc_vector + 2] = 5

core.memory[core.size] = flow.HLT

core.run()

print(core)

