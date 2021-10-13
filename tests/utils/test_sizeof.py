from ampersand.utils import sizeof
import pytest


@pytest.mark.parametrize(
    "bits",
    [
        2, 8, 16, 32, 64
    ]
)
def test_sizeof(bits: int):
    assert sizeof.in_bits(bits) == 2 ** bits
