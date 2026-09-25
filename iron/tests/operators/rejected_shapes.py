#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Shapes an operator must refuse rather than build.

Each of these lowers, builds and then hangs the device or computes the wrong
answer, with no diagnostic worth reading -- so the operator rejects it at
construction. Host-only: what is checked is the refusal, not a dispatch.
"""

import pytest

from aie.iron.device import NPU2

from iron.common.declare import Incompatible
from iron.operators.repeat import Repeat
from iron.operators.strided_copy import StridedCopy, _flat
from iron.operators.transpose import Transpose


@pytest.mark.parametrize(
    "cols,why",
    [
        (513, "odd: every divisor is odd, so no chunk is a whole 32-bit word"),
        (1031, "prime > 1023: the only divisors are 1 and cols, neither legal"),
        (2062, "2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count"),
    ],
)
def test_repeat_cols_without_a_legal_split_is_rejected(cols, why):
    """A split has to satisfy the innermost dim AND the dim holding the chunk
    count. Both land on a 10-bit wrap field, and the innermost is denominated
    in 32-bit words, so bounding the chunk length alone lets through taps the
    BD verifier then rejects with a much less legible error.

    Refused when the shape is asked for, not when it is built: nothing about
    the device can make it legal.
    """
    with pytest.raises(ValueError, match="Cannot split cols"):
        Repeat(rows=8, cols=cols, repeat=4)


def test_transfer_size_not_dividing_the_per_channel_share_is_rejected():
    """A BD shorter than the ObjectFifo object hangs the device.

    4 channels over 1024 elements is a 256-element BD; a 512-element object
    leaves the memtile's S2MM waiting for a second half that no channel
    sends, and the drain's dma_await_task returns ERT_CMD_STATE_TIMEOUT with
    no diagnostic.
    """
    operator = StridedCopy(**_flat(1024, num_aie_channels=4, transfer_size=512))
    with pytest.raises(
        (AssertionError, ValueError), match="must divide the per-channel transfer"
    ):
        operator.compile()


# Shapes whose M*N is divisible by every factor while one per-dimension quotient is not
# a whole number of tiles. Without the guard these reach the transfer as sizes
# [8, 0, 256, 32]. compatible() runs at tuned(), so that is where the refusal lands.
@pytest.mark.parametrize(
    "M,N,aie_columns,channels,m,n,bad",
    [
        (2048, 128, 8, 1, 256, 32, "num_aie_columns"),
        (256, 2048, 1, 2, 256, 32, "num_channels"),
    ],
)
def test_transpose_dimension_that_does_not_tile_is_refused_by_name(
    M, N, aie_columns, channels, m, n, bad
):
    op = Transpose(
        M=M, N=N, num_aie_columns=aie_columns, num_channels=channels, m=m, n=n, s=8
    )
    with pytest.raises(Incompatible, match=bad):
        op.tuned(NPU2())


@pytest.mark.parametrize("aie_columns", [1, 2, 4])
def test_transpose_tiling_that_fits_is_still_accepted(aie_columns):
    """The guard must not narrow the accepted set: 1/2/4 columns all tile N=128 by n=32."""
    Transpose(
        M=2048, N=128, num_aie_columns=aie_columns, num_channels=1, m=256, n=32, s=8
    ).tuned(NPU2())
