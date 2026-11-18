# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``firings()`` against operators whose core bodies are read by hand first.

Device-free: each case builds an operator's array alone, never a toolchain.
"""

import pytest

from iron.common import Precision
from iron.common.graph.firing import Access, firings
from iron.operators.depthwise_conv1d import TAPS, DepthwiseConv1d
from iron.operators.gemm import GEMM
from iron.operators.relu import ReLU
from iron.operators.rms_norm import RMSNorm

pytestmark = pytest.mark.usefixtures("npu2")


def test_a_depthwise_conv1ds_window_ramps_up_and_drains():
    """Its input's window grows by one row a firing, slides at five, drains four."""
    pattern = firings(DepthwiseConv1d(rows=64, channels=64, num_aie_columns=1))
    assert pattern["x"].prologue == tuple(Access(True, held) for held in range(1, TAPS))
    assert pattern["x"].steady == (Access(True, TAPS), Access(False, 1))
    assert pattern["x"].steady_depth == 1
    assert pattern["x"].epilogue == (Access(False, TAPS - 1),)
    # Every column reads the same weight row once, whole, the call through.
    assert pattern["weight"].prologue == (Access(True, TAPS),)
    assert pattern["weight"].steady == ()
    assert pattern["weight"].epilogue == (Access(False, TAPS),)
    # The output has no window: one row out for every firing, ramp-up included.
    assert pattern["y"].prologue == (
        Access(True, 1),
        Access(False, 1),
    ) * (TAPS - 1)
    assert pattern["y"].steady == (Access(True, 1), Access(False, 1))
    assert pattern["y"].epilogue == ()


def test_a_depthwise_conv1ds_window_is_the_same_split_over_two_columns():
    """More columns split the rows; a column's own window is unchanged."""
    one = firings(DepthwiseConv1d(rows=64, channels=64, num_aie_columns=1))
    two = firings(DepthwiseConv1d(rows=64, channels=256, num_aie_columns=2))
    assert one["x"] == two["x"]
    assert one["weight"] == two["weight"]


def test_an_elementwise_op_acquires_and_releases_one_a_firing():
    pattern = firings(ReLU(size=2048, num_aie_columns=1, tile_size=2048))
    assert pattern["x"].prologue == pattern["x"].epilogue == ()
    assert pattern["x"].steady == (Access(True, 1), Access(False, 1))
    assert pattern["x"].steady_depth == 1
    assert pattern["y"] == pattern["x"]


def test_a_weighted_rms_norms_row_is_held_the_whole_call():
    """The weight is acquired once, outside the per-row loop, and released once."""
    pattern = firings(RMSNorm(rows=4, tile_size=2048, num_aie_columns=1, weighted=True))
    assert pattern["weight"].prologue == (Access(True, 1),)
    assert pattern["weight"].steady == ()
    assert pattern["weight"].epilogue == (Access(False, 1),)
    assert pattern["x"].steady == (Access(True, 1), Access(False, 1))
    assert pattern["y"].steady == (Access(True, 1), Access(False, 1))


@pytest.mark.parametrize(
    "tile_m, tile_k, tile_n, num_aie_columns",
    [(32, 32, 32, 1), (64, 64, 64, 2)],
    ids=["32", "64"],
)
def test_gemm_acquires_one_object_a_firing_whatever_its_tile_sizes(
    tile_m, tile_k, tile_n, num_aie_columns
):
    """A tile's shape sets the objectFIFOs' sizes, not how many a firing moves.

    A and B are the K loop's firings, nested inside the tile loop C's own
    firing wraps; a tile size only sizes each memref the kernel reads.
    """
    op = GEMM(
        M=128 * num_aie_columns,
        K=128,
        N=128 * num_aie_columns,
        num_aie_columns=num_aie_columns,
        tile_m=tile_m,
        tile_k=tile_k,
        tile_n=tile_n,
        precision=Precision.HIGHEST,
    )
    pattern = firings(op)
    for name in ("A", "B"):
        assert pattern[name].prologue == pattern[name].epilogue == ()
        assert pattern[name].steady == (Access(True, 1), Access(False, 1))
        assert pattern[name].steady_depth == 2
    assert pattern["C"].prologue == pattern["C"].epilogue == ()
    assert pattern["C"].steady == (Access(True, 1), Access(False, 1))
    assert pattern["C"].steady_depth == 1
