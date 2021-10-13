from ampersand.utypes import UIntr
import pytest


@pytest.mark.parametrize(
    "uintr",
    [
        UIntr(False)
    ]
)
def test_uintr_false(uintr: UIntr):
    assert uintr.breaks is False


@pytest.mark.parametrize(
    "uintr",
    [
        UIntr(True)
    ]
)
def test_uintr_true(uintr: UIntr):
    assert uintr.breaks is True
