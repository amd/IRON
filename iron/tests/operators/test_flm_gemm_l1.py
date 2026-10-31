# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""FLM's tile selection must leave room for what its kernel holds beside its buffers.

Its data, AIE2's activation LUT tables among it, and its stack.
"""

import pytest
from aie.iron.device import from_name
from aie.utils import bfp, set_current_device

from iron import Precision
from iron.operators.flm.gemm.design import (
    A_DEPTH,
    C_DEPTH,
    CT_OUT_LEN,
    M_TILE,
    TILE_NS,
    Epilogue,
    k_slices,
    l1_tiles,
)
from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.tests.support.tools import requires

NPU1 = from_name("npu1", n_cols=4)
L1 = 65536
# What l1_tiles is handed for a core's frame at every A band height: a stack,
# and on AIE2 with an activation also lut_based_ops' 5248 bytes of tables.
FRAME = {"npu1": 2560 + 5248, "npu2": 2560}
ACTIVATED = tuple(Epilogue)


def _fits(tile_n, ct_k, height, b_depth, b_bytes, frame, m_chunk=1):
    return (
        m_chunk * M_TILE * tile_n * 4
        + height * ct_k * 2 * A_DEPTH
        + int(ct_k * tile_n * b_bytes) * b_depth
        + CT_OUT_LEN * 2 * C_DEPTH
        + frame
        <= L1
    )


@pytest.mark.parametrize(
    "device,b_bytes,tile_n,expected",
    [
        ("npu1", 2, 64, (64, 64, 2)),
        ("npu1", 2, 128, (32, 32, 2)),
        ("npu2", bfp.BLOCK_BYTES / bfp.BLOCK, 64, (128, 32, 2)),
        ("npu2", bfp.BLOCK_BYTES / bfp.BLOCK, 128, (64, 32, 2)),
    ],
)
def test_default_tiles_account_for_the_frame(device, b_bytes, tile_n, expected):
    frame = FRAME[device]
    assert l1_tiles(tile_n, b_bytes, L1, lambda height, ct_k: frame) == expected
    ct_k, height, b_depth = expected
    assert _fits(tile_n, ct_k, height, b_depth, b_bytes, frame)
    fixed = l1_tiles(tile_n, b_bytes, L1, lambda h, c: frame, t_ma=height, ct_k=ct_k)
    assert fixed == expected


@pytest.mark.parametrize("tile_n", TILE_NS)
@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_default_k_slice_is_the_deepest_that_fits_double_buffered(device, tile_n):
    """No deeper slice fits with double-buffered B at any A height."""
    frame, b_bytes = FRAME[device], 2
    ct_k, _, b_depth = l1_tiles(tile_n, b_bytes, L1, lambda h, c: frame)
    assert b_depth == 2
    for deeper in (c for c in k_slices(512) if c > ct_k):
        assert not any(
            _fits(tile_n, deeper, height, 2, b_bytes, frame) for height in (16, 32, 64)
        )


@requires("peano")  # frame_bytes reads 0 without it
def test_aie2_activations_bring_their_lut_tables_into_the_frame():
    """Measured, an activated core's frame holds lut_based_ops' tables.

    An unactivated one's bytes go to a deeper k slice.
    """
    shape = dict(M=512, K=1024, N=1024, tile_n=64, k_tile=512)
    shape.update(precision=Precision.MEDIUM)
    frames = {}
    for modes in ((Epilogue.NONE,), ACTIVATED):
        with set_current_device(NPU1):
            op = ProjectionGEMM(**shape, epilogue_modes=modes).resolved(NPU1)
        frames[modes] = op.frame(NPU1, 64, 512, 64, 16, False, False)
    assert frames[ACTIVATED] - frames[(Epilogue.NONE,)] >= 5248
    plain = frames[(Epilogue.NONE,)]
    assert l1_tiles(64, 2, L1, lambda height, ct_k: plain) == (128, 16, 2)


def test_explicit_aie2_tile_falls_back_to_single_buffered_b():
    frame = FRAME["npu1"]
    assert l1_tiles(64, 2, L1, lambda h, c: frame, t_ma=16, ct_k=128) == (128, 16, 1)
    with pytest.raises(ValueError, match="does not fit L1"):
        l1_tiles(64, 2, L1, lambda h, c: frame, t_ma=64, ct_k=128)


@pytest.mark.parametrize("chunks", [1, 3])
@pytest.mark.parametrize("ct_k", [32, 64])
def test_b_ring_divides_the_chunks_a_k_step_consumes(ct_k, chunks):
    frame = FRAME["npu2"]
    _, _, b_depth = l1_tiles(
        32, 2, L1, lambda h, c: frame, k_tile=chunks * ct_k, ct_k=ct_k
    )
    assert b_depth == 1


@pytest.mark.parametrize("tile_n", TILE_NS)
@pytest.mark.parametrize("tile_ma", [16, 32, 64])
@pytest.mark.parametrize("ct_k", [32, 128])
@pytest.mark.parametrize("m_chunk", [1, 2])
def test_aie2_tile_validation_includes_the_frame(tile_n, tile_ma, ct_k, m_chunk):
    frame = FRAME["npu1"]
    fitting_depths = [
        depth
        for depth in (2, 1)
        if (512 // ct_k) % depth == 0
        and _fits(tile_n, ct_k, tile_ma, depth, 2, frame, m_chunk)
    ]
    fixed = dict(t_ma=tile_ma, ct_k=ct_k)
    if fitting_depths:
        assert l1_tiles(tile_n, 2, L1, lambda h, c: frame, m_chunk, **fixed) == (
            ct_k,
            tile_ma,
            fitting_depths[0],
        )
    else:
        with pytest.raises(ValueError, match="does not fit L1"):
            l1_tiles(tile_n, 2, L1, lambda h, c: frame, m_chunk, **fixed)
