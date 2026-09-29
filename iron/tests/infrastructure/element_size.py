# SPDX-License-Identifier: Apache-2.0
"""The fused arena's byte<->element rate, which used to be a hardcoded bf16 itemsize."""

import pytest
from aie import ir

from iron.common.compilation.sequence import element_size_bytes


@pytest.fixture
def ctx():
    with ir.Context(), ir.Location.unknown():
        yield


@pytest.mark.parametrize(
    "make, expected",
    [
        (lambda: ir.IntegerType.get_signless(8), 1),
        (lambda: ir.IntegerType.get_signless(16), 2),
        (lambda: ir.IntegerType.get_signless(32), 4),
        (lambda: ir.BF16Type.get(), 2),
        (lambda: ir.F16Type.get(), 2),
        (lambda: ir.F32Type.get(), 4),
    ],
)
def test_element_size_bytes(ctx, make, expected):
    assert element_size_bytes(make()) == expected


def test_sub_byte_types_are_rejected_not_rounded(ctx):
    """A packed 4-bit buffer must declare the byte type it occupies.

    Rounding i4 to 1 byte would silently quadruple a quantized weight buffer's apparent size,
    which is the same class of error as the bf16 itemsize this function replaced.
    """
    with pytest.raises(ValueError, match="sub-byte"):
        element_size_bytes(ir.IntegerType.get_signless(4))
