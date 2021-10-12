# Stack

PSH = 0xa1  # Push C
POP = 0xa2  # Pop to C


def psh(core):
    core.sp += 1
    core.memory[core.sp] = core.c


def pop(core):
    core.c = core.memory[core.sp]
    core.sp -= 1


STACK_EXPORT_TABLE = {
    PSH: psh,
    POP: pop
}
