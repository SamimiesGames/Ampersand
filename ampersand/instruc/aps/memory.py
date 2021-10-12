# Memory

STM = 0xF6  # Load B at C in memory
RTM = 0xF7  # Set C in memory to B


def stm(core):
    core.memory[core.c] = core.b


def rtm(core):
    core.b = core.memory[core.c]


MEMORY_EXPORT_TABLE = {
    RTM: rtm,
    STM: stm
}

