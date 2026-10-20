# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""FLM's tile selection must leave room for what its kernel holds beside its
buffers: its data, AIE2's activation LUT tables among it, and its stack.
"""

import pytest
from aie.iron.device import from_name
from aie.utils import bfp

from iron.operators.flm.gemm.design import (
    A_DEPTH,
    C_DEPTH,
    CT_MAX_K_FOR_N,
    CT_OUT_LEN,
    M_TILE,
    Epilogue,
    l1_tiles,
)
from iron.operators.flm.gemm.op import ProjectionGEMM

NPU1 = from_name("npu1", n_cols=4)
L1 = 65536
# What l1_tiles is handed for a core's frame at every A band height: a stack,
# and on AIE2 with an activation also lut_based_ops' 5248 bytes of tables.
FRAME = {"npu1": 2560 + 5248, "npu2": 2560}
ACTIVATED = tuple(Epilogue)


@pytest.mark.parametrize(
    "device,b_bytes,tile_n,expected",
    [
        ("npu1", 2, 64, (32, 1)),
        ("npu1", 2, 128, (32, 2)),
        ("npu2", bfp.BLOCK_BYTES / bfp.BLOCK, 64, (32, 2)),
        ("npu2", bfp.BLOCK_BYTES / bfp.BLOCK, 128, (64, 2)),
    ],
)
def test_default_tiles_account_for_the_frame(device, b_bytes, tile_n, expected):
    ct_k, frame = CT_MAX_K_FOR_N[tile_n], FRAME[device]
    assert l1_tiles(tile_n, ct_k, b_bytes, L1, lambda height: frame) == expected
    assert (
        l1_tiles(tile_n, ct_k, b_bytes, L1, lambda height: frame, t_ma=expected[0])
        == expected
    )


def test_aie2_activations_bring_their_lut_tables_into_the_frame():
    """Measured, an activated core's frame holds lut_based_ops' tables; an
    unactivated one's bytes go to B.
    """
    shape = dict(M=512, K=1024, N=1024, tile_n=64, k_tile=512)
    frames = {}
    for modes in ((Epilogue.NONE,), ACTIVATED):
        op = ProjectionGEMM(**shape, epilogue_modes=modes).resolved(NPU1)
        frames[modes] = op.frame(NPU1, 64, 512, 16, False, False)
    assert frames[ACTIVATED] - frames[(Epilogue.NONE,)] >= 5248
    plain = frames[(Epilogue.NONE,)]
    assert l1_tiles(64, CT_MAX_K_FOR_N[64], 2, L1, lambda height: plain) == (16, 2)


def test_explicit_aie2_tile_falls_back_to_single_buffered_b():
    frame = FRAME["npu1"]
    assert l1_tiles(64, 128, 2, L1, lambda height: frame, t_ma=16) == (16, 1)
    with pytest.raises(ValueError, match="does not fit L1"):
        l1_tiles(64, 128, 2, L1, lambda height: frame, t_ma=64)


@pytest.mark.parametrize("chunks", [1, 3])
@pytest.mark.parametrize("tile_n", CT_MAX_K_FOR_N)
def test_b_ring_divides_the_chunks_a_k_step_consumes(tile_n, chunks):
    ct_k, frame = CT_MAX_K_FOR_N[tile_n], FRAME["npu2"]
    _, b_depth = l1_tiles(
        tile_n, ct_k, 2, L1, lambda height: frame, k_tile=chunks * ct_k
    )
    assert b_depth == 1
    assert l1_tiles(
        tile_n, ct_k, 2, L1, lambda height: frame, k_tile=chunks * ct_k, t_ma=16
    ) == (16, 1)


@pytest.mark.parametrize("tile_n", CT_MAX_K_FOR_N)
@pytest.mark.parametrize("tile_ma", [16, 32, 64])
@pytest.mark.parametrize("m_chunk", [1, 2])
def test_aie2_tile_validation_includes_the_frame(tile_n, tile_ma, m_chunk):
    ct_k, frame = CT_MAX_K_FOR_N[tile_n], FRAME["npu1"]
    fixed_bytes = (
        m_chunk * M_TILE * tile_n * 4
        + tile_ma * ct_k * 2 * A_DEPTH
        + CT_OUT_LEN * 2 * C_DEPTH
        + frame
    )
    fitting_depths = [
        depth for depth in (2, 1) if fixed_bytes + ct_k * tile_n * 2 * depth <= L1
    ]
    if fitting_depths:
        assert l1_tiles(
            tile_n, ct_k, 2, L1, lambda height: frame, m_chunk, t_ma=tile_ma
        ) == (tile_ma, fitting_depths[0])
    else:
        with pytest.raises(ValueError, match="does not fit L1"):
            l1_tiles(tile_n, ct_k, 2, L1, lambda height: frame, m_chunk, t_ma=tile_ma)
