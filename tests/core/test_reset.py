from ampersand import Core

core = Core(16, "aps")


def test_reset():
    core.reset()

    assert core.a == 0
    assert core.b == 0
    assert core.c == 0

    assert core.z is False
    assert core.o is False
    assert core.u is False

    assert sum(core.memory.memory.values()) == 0

    assert core.pc == core.pc_vector
    assert core.sp == core.sp_vector

