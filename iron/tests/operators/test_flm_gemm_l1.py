# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""FLM's tile selection must leave room for the activation LUTs it links."""

import pytest
from aie.iron.device import from_name
from aie.utils import bfp

from iron.operators.flm.gemm.design import (
    A_DEPTH,
    C_DEPTH,
    CT_MAX_K_FOR_N,
    CT_OUT_LEN,
    LUT_STATIC_SIZE,
    M_TILE,
    Epilogue,
    l1_budget,
    l1_tiles,
)

NPU1 = from_name("npu1", n_cols=4)
# A core's stack at every A band height, as l1_tiles takes it.
STACK = 2560
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
def test_default_tiles_account_for_static_memory(device, b_bytes, tile_n, expected):
    ct_k = CT_MAX_K_FOR_N[tile_n]
    budget = l1_budget(
        from_name(device, n_cols={"npu1": 4, "npu2": 8}[device]), ACTIVATED
    )
    assert l1_tiles(tile_n, ct_k, b_bytes, budget, lambda height: STACK) == expected
    assert (
        l1_tiles(tile_n, ct_k, b_bytes, budget, lambda height: STACK, t_ma=expected[0])
        == expected
    )


def test_aie2_without_an_activation_spends_the_lut_bytes_on_b():
    budget = l1_budget(NPU1, (Epilogue.NONE,))
    assert budget == l1_budget(NPU1, ACTIVATED) + LUT_STATIC_SIZE
    assert l1_tiles(64, CT_MAX_K_FOR_N[64], 2, budget, lambda height: STACK) == (16, 2)


def test_explicit_aie2_tile_falls_back_to_single_buffered_b():
    assert l1_tiles(
        64, 128, 2, l1_budget(NPU1, ACTIVATED), lambda height: STACK, t_ma=16
    ) == (16, 1)
    with pytest.raises(ValueError, match="does not fit L1"):
        l1_tiles(64, 128, 2, l1_budget(NPU1, ACTIVATED), lambda height: STACK, t_ma=64)


@pytest.mark.parametrize("chunks", [1, 3])
@pytest.mark.parametrize("tile_n", CT_MAX_K_FOR_N)
def test_b_ring_divides_the_chunks_a_k_step_consumes(tile_n, chunks):
    ct_k = CT_MAX_K_FOR_N[tile_n]
    budget = l1_budget(from_name("npu2", n_cols=8), ACTIVATED)
    _, b_depth = l1_tiles(
        tile_n, ct_k, 2, budget, lambda height: STACK, k_tile=chunks * ct_k
    )
    assert b_depth == 1
    assert l1_tiles(
        tile_n, ct_k, 2, budget, lambda height: STACK, k_tile=chunks * ct_k, t_ma=16
    ) == (16, 1)


@pytest.mark.parametrize("tile_n", CT_MAX_K_FOR_N)
@pytest.mark.parametrize("tile_ma", [16, 32, 64])
@pytest.mark.parametrize("m_chunk", [1, 2])
def test_aie2_tile_validation_includes_lut_data(tile_n, tile_ma, m_chunk):
    ct_k = CT_MAX_K_FOR_N[tile_n]
    fixed_bytes = (
        m_chunk * M_TILE * tile_n * 4
        + tile_ma * ct_k * 2 * A_DEPTH
        + CT_OUT_LEN * 2 * C_DEPTH
        + STACK
        + LUT_STATIC_SIZE
    )
    fitting_depths = [
        depth for depth in (2, 1) if fixed_bytes + ct_k * tile_n * 2 * depth <= 65536
    ]
    if fitting_depths:
        assert l1_tiles(
            tile_n,
            ct_k,
            2,
            l1_budget(NPU1, ACTIVATED),
            lambda height: STACK,
            m_chunk,
            t_ma=tile_ma,
        ) == (tile_ma, fitting_depths[0])
    else:
        with pytest.raises(ValueError, match="does not fit L1"):
            l1_tiles(
                tile_n,
                ct_k,
                2,
                l1_budget(NPU1, ACTIVATED),
                lambda height: STACK,
                m_chunk,
                t_ma=tile_ma,
            )
