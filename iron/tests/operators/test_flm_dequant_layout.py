# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The dequant design's descriptors must land B where pack_b puts it.

A wrong stride yields a buffer of the right size holding real weight values in
the wrong order, which the GEMM reads without complaint. These tests compose
the dataflow as index arithmetic and compare against the packer the GEMM is
validated against.
"""

import numpy as np
import pytest
from aie.utils import bfp

from iron.operators.flm.aie2p_math_emulation import rb
from iron.operators.flm.dequant.op import (
    CORE_JOIN_OFFSETS,
    CT_K,
    HALF_BLOCKS,
    K_TILE_B,
    N_TILE,
    SLAB_BLOCKS,
    S,
    T,
    drain_halves,
)
from iron.operators.flm.packing import pack_b
from iron.operators.flm.q4nx import K_TILE, M_TILE

DRAIN = drain_halves(HALF_BLOCKS)[0]


def _apply(stream_idx, sizes, strides):
    """Destination index for a value arriving at stream_idx."""
    out = np.zeros_like(stream_idx)
    rem = stream_idx.copy()
    for dim in range(len(sizes) - 1, -1, -1):
        out = out + (rem % sizes[dim]) * strides[dim]
        rem = rem // sizes[dim]
    return out


def _model(K, N):
    """Composed block index for every (k, n): kernel emission, then the join,
    then the drain.
    """
    n = np.arange(N)[:, None]
    k = np.arange(K)[None, :]

    kslice_loc, tb_loc = (k % K_TILE) // CT_K, (n % M_TILE) // T
    i, t_in = (k % CT_K) // S, n % T
    emit = ((kslice_loc * (M_TILE // T) + tb_loc) * (CT_K // S) + i) * T + t_in

    n_half, k_half = (n % N_TILE) // M_TILE, (k % K_TILE_B) // K_TILE
    mt = np.array(CORE_JOIN_OFFSETS)[n_half] + emit

    pos = _apply(mt, DRAIN.sizes, DRAIN.strides)
    cb, kb = n // N_TILE, k // K_TILE_B
    return (cb * (K // K_TILE_B) + kb) * SLAB_BLOCKS + k_half * HALF_BLOCKS + pos


@pytest.mark.parametrize(
    "K, N", [(512, 64), (1024, 128), (2048, 256), (1536, 640), (2048, 2048)]
)
def test_bytes_match_pack_b(K, N):
    """End to end, including the conversion."""
    rng = np.random.default_rng(0)
    B = rng.standard_normal((K, N)).astype(np.float32)
    # The cores round to bf16 before converting, so the reference must too.
    B = rb(B)

    golden = pack_b(
        B,
        K_TILE_B,
        N_TILE,
        S,
        T,
        CT_K,
        bfp16=True,
        round_conv_even=False,
    )

    blk = _model(K, N)
    slot = np.broadcast_to(np.arange(K)[None, :] % S, blk.shape)
    flat = np.empty(K * N, dtype=np.float32)
    flat[(blk * S + slot).ravel()] = B.T.ravel()
    mine = bfp.encode(flat, rounding="floor")

    assert np.array_equal(mine, golden)


def test_descriptors_are_dma_expressible():
    """A bfp16 block is 9 bytes and the DMA steps in 4, so only groups of
    blocks are addressable. The drain is written in blocks; this checks the
    grouping survives translation to bytes and the field widths.
    """
    block_bytes = T + 1
    dims = DRAIN.transformation_dims
    for size, stride in dims[:-1]:
        assert (stride * block_bytes) % 4 == 0, (size, stride)
    assert (dims[-1][0] * block_bytes) % 4 == 0
    assert dims[-1][1] == 1
    assert dims[-1][0] <= 1023
    assert int(np.prod(DRAIN.sizes)) == HALF_BLOCKS
