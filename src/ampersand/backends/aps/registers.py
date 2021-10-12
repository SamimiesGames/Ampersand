# Registers

LDA = 0xF1  # Load A to C
LDB = 0xF2  # Load B to C
LDM = 0xF3  # Load Immidiate to C
STA = 0xF4  # Load C to A
STB = 0xF5  # Load C to B


def lda(core):
    core.c = core.a


def ldb(core):
    core.c = core.a


def ldm(core):
    core.c = core.memory[core.pc + 1]
    core.pc += 1


def sta(core):
    core.a = core.c


def stb(core):
    core.b = core.c


REGISTER_EXPORT_TABLE = {
    LDA: lda,
    LDB: ldb,
    LDM: ldm,
    STA: sta,
    STB: stb
}
