# Calculations

ADD = 0x7  # Load A + B to C
SUB = 0x8  # Load A - B to C
DIV = 0x9  # Load A / B to C
MUL = 0xa  # Load A * B to C
EXP = 0xb  # Load A ** B to C


def add(core):
    core.c = core.a + core.b


def sub(core):
    core.c = core.a - core.b


def div(core):
    core.c = core.a / core.b


def mul(core):
    core.c = core.a * core.b


def exp(core):
    core.c = core.a ** core.b


MATH_EXPORT_TABLE = {
    ADD: add,
    SUB: sub,
    DIV: div,
    MUL: mul,
    EXP: exp
}
