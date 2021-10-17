from ampersand.backends.aps import flow
from ampersand import Core
import pytest


core = Core(16, "aps")


def test_halt():
    core.reset()

    core.memory[core.pc + 1] = flow.HLT

    core.run()

    assert core.pc.value == core.pc_vector + 1


@pytest.mark.parametrize(
    "address",
    [
        0xf, 0xff
    ]
)
def test_jmp(address):
    core.reset()

    core.c = address
    core.memory[core.pc.value + 1] = flow.JMP
    core.memory[core.pc.value + 2] = flow.HLT

    assert core.pc.value == address


