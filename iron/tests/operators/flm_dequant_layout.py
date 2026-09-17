#!/usr/bin/env python3
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
import torch

from iron.operators.flm.dequant.design import (
    CORE_JOIN_OFFSETS,
    CT_K,
    DRAIN_DIMS,
    HALF_BLOCKS,
    K_TILE,
    K_TILE_B,
    M_TILE,
    N_TILE,
    S,
    SLAB_BLOCKS,
    T,
)
from iron.operators.flm.packing import f32_to_bfp16ebs8, pack_b

# Every distinct (K in-features, N out-features) Gemma4 E2B needs, from
# hidden_size 1536, intermediate_size 6144, DQ/DK/DV 4096/512/512 and the SWA
# and skip variants.
E2B_SHAPES = [
    (1536, 5120),
    (4096, 1536),
    (1536, 6144),
    (6144, 1536),
    (1536, 4096),
    (1536, 12288),
    (12288, 1536),
    (1536, 2560),
    (2048, 1536),
    (1536, 2048),
]


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
    then the drain."""
    n = np.arange(N)[:, None]
    k = np.arange(K)[None, :]

    kslice_loc, tb_loc = (k % K_TILE) // CT_K, (n % M_TILE) // T
    i, t_in = (k % CT_K) // S, n % T
    emit = ((kslice_loc * (M_TILE // T) + tb_loc) * (CT_K // S) + i) * T + t_in

    n_half, k_half = (n % N_TILE) // M_TILE, (k % K_TILE_B) // K_TILE
    mt = np.array(CORE_JOIN_OFFSETS)[n_half] + emit

    pos = _apply(mt, [d[0] for d in DRAIN_DIMS], [d[1] for d in DRAIN_DIMS])
    cb, kb = n // N_TILE, k // K_TILE_B
    return (cb * (K // K_TILE_B) + kb) * SLAB_BLOCKS + k_half * HALF_BLOCKS + pos


def _pack_b_block(K, N):
    """Which bfp16 block pack_b puts (k, n) in."""
    n = np.arange(N)[:, None]
    k = np.arange(K)[None, :]
    cb, kb = n // N_TILE, k // K_TILE_B
    kslice, i = (k % K_TILE_B) // CT_K, (k % CT_K) // S
    tb, t_in = (n % N_TILE) // T, n % T
    blk = (cb * (K // K_TILE_B) + kb) * (K_TILE_B // CT_K) + kslice
    return ((blk * (N_TILE // T) + tb) * (CT_K // S) + i) * T + t_in


@pytest.mark.parametrize(
    "K, N", [(512, 64), (1024, 128), (2048, 256), (1536, 640), (2048, 2048)]
)
def test_block_index_matches_pack_b(K, N):
    assert np.array_equal(_model(K, N), _pack_b_block(K, N))


@pytest.mark.parametrize("K, N", [(512, 64), (1024, 128), (2048, 256)])
def test_bytes_match_pack_b(K, N):
    """End to end, including the conversion."""
    rng = np.random.default_rng(0)
    B = rng.standard_normal((K, N)).astype(np.float32)
    # The cores round to bf16 before converting, so the reference must too.
    u = B.view(np.uint32)
    bf = ((u >> 16) + (((u & 0xFFFF) != 0) & ((u >> 31) != 0))).astype(np.uint16)
    B = (bf.astype(np.uint32) << 16).view(np.float32)

    golden = pack_b(
        torch.from_numpy(B),
        K_TILE_B,
        N_TILE,
        S,
        T,
        CT_K,
        bfp16=True,
        round_conv_even=False,
    ).numpy()

    blk = _model(K, N)
    slot = np.broadcast_to(np.arange(K)[None, :] % S, blk.shape)
    flat = np.empty(K * N, dtype=np.float32)
    flat[(blk * S + slot).ravel()] = B.T.ravel()
    mine = f32_to_bfp16ebs8(flat.reshape(-1, 8), round_conv_even=False).numpy()

    assert np.array_equal(mine, golden)


def test_descriptors_are_dma_expressible():
    """A bfp16 block is 9 bytes and the DMA steps in 4, so only groups of
    blocks are addressable. DRAIN_DIMS is written in blocks; this checks the
    grouping survives translation to bytes and the field widths."""
    block_bytes = T + 1
    for size, stride in DRAIN_DIMS[:-1]:
        assert (stride * block_bytes) % 4 == 0, (size, stride)
    assert (DRAIN_DIMS[-1][0] * block_bytes) % 4 == 0
    assert DRAIN_DIMS[-1][1] == 1
    assert DRAIN_DIMS[-1][0] <= 1023
    assert int(np.prod([d[0] for d in DRAIN_DIMS])) == HALF_BLOCKS


@pytest.mark.parametrize("K, N", E2B_SHAPES)
def test_e2b_shapes_are_servable(K, N):
    """Replacing the stock GEMM means dequantizing every E2B weight on device,
    so a model or a tiling rule that breaks one of these must fail here."""
    assert K % K_TILE_B == 0, f"K={K} does not tile"
    assert N % N_TILE == 0, f"N={N} does not tile"
    assert K // K_TILE_B > 1, f"K={K} would make flm.GEMM pick tile_n=128"
    assert N // N_TILE >= 8, f"N={N} leaves columns without work"
