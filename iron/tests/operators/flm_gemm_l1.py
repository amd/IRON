# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""FLM's tile selection must leave room for the linked activation LUTs."""

import pytest
from aie.iron.device import from_name

from iron.exports.flm.gemm.design import (
    A_DEPTH,
    BFP16_GROUP,
    BFP16_GROUP_BYTES,
    C_DEPTH,
    CT_MAX_K_FOR_N,
    CT_OUT_LEN,
    LUT_STATIC_SIZE,
    M_TILE,
    STACK_SIZE,
    _b_depth_for,
    _default_l1,
    l1_budget,
)


@pytest.mark.parametrize(
    "device,b_bytes,tile_n,expected",
    [
        (from_name("npu1", n_cols=4), 2, 64, (32, 1)),
        (from_name("npu1", n_cols=4), 2, 128, (32, 2)),
        (from_name("npu2", n_cols=8), BFP16_GROUP_BYTES / BFP16_GROUP, 64, (32, 2)),
        (from_name("npu2", n_cols=8), BFP16_GROUP_BYTES / BFP16_GROUP, 128, (64, 2)),
    ],
)
def test_default_tiles_account_for_static_memory(device, b_bytes, tile_n, expected):
    ct_k = CT_MAX_K_FOR_N[tile_n]
    budget = l1_budget(device)
    assert _default_l1(tile_n, ct_k, b_bytes, budget) == expected
    tile_ma, b_depth = expected
    assert _b_depth_for(tile_ma, tile_n, ct_k, b_bytes, budget) == b_depth


def test_explicit_aie2_tile_falls_back_to_single_buffered_b():
    assert _b_depth_for(16, 64, 128, 2, l1_budget(from_name("npu1", n_cols=4))) == 1
    with pytest.raises(ValueError, match="does not fit L1"):
        _b_depth_for(64, 64, 128, 2, l1_budget(from_name("npu1", n_cols=4)))


@pytest.mark.parametrize("tile_n", CT_MAX_K_FOR_N)
@pytest.mark.parametrize("tile_ma", [16, 32, 64])
@pytest.mark.parametrize("m_chunk", [1, 2])
def test_aie2_tile_validation_includes_lut_data(tile_n, tile_ma, m_chunk):
    ct_k = CT_MAX_K_FOR_N[tile_n]
    fixed_bytes = (
        m_chunk * M_TILE * tile_n * 4
        + tile_ma * ct_k * 2 * A_DEPTH
        + CT_OUT_LEN * 2 * C_DEPTH
        + STACK_SIZE
        + LUT_STATIC_SIZE
    )
    fitting_depths = [
        depth for depth in (2, 1) if fixed_bytes + ct_k * tile_n * 2 * depth <= 65536
    ]
    if fitting_depths:
        assert (
            _b_depth_for(
                tile_ma,
                tile_n,
                ct_k,
                2,
                l1_budget(from_name("npu1", n_cols=4)),
                m_chunk,
            )
            == fitting_depths[0]
        )
    else:
        with pytest.raises(ValueError, match="does not fit L1"):
            _b_depth_for(
                tile_ma,
                tile_n,
                ct_k,
                2,
                l1_budget(from_name("npu1", n_cols=4)),
                m_chunk,
            )
