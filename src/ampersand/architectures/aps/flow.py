from ampersand.utypes import UIntr

# Flow Control

NOP = 0x0  # Do Nothing
HLT = 0xFF  # Halt
JMP = 0xa3  # Jump to C
JZ = 0xa4  # Jump to C if zero
JL = 0xa5  # Jump to C if less than
JM = 0xa6  # Jump to C if more than


def jmp(core):
    core.pc = core.c


def jz(core):
    if core.z:
        jmp(core)


def jl(core):
    if core.u:
        jmp(core)


def jm(core):
    if core.o:
        jmp(core)


FLOW_EXPORT_TABLE = {
    JMP: jmp,
    JZ: jz,
    JL: jl,
    JM: jm,
    NOP: UIntr(False),
    HLT: UIntr(True)
}
