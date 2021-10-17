from ampersand.utypes import UInt
import pytest


@pytest.mark.parametrize(
    "uint",
    [
        UInt(256, 256)
    ]
)
def test_uint_equal(uint: UInt):
    assert uint.value == uint.bits


@pytest.mark.parametrize(
    "uint",
    [
        UInt(257, 256)
    ]
)
def test_uint_overflow_init(uint: UInt):
    assert uint.value == uint.bits


def test_uint_add():
    assert isinstance(UInt(1, 4) + 1, UInt)
