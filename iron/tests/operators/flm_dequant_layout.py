#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The dequant design's descriptors must land B exactly where pack_b puts it.

A buffer descriptor with the wrong stride produces a wrongly ordered buffer of
the RIGHT SIZE, so the GEMM reads it without complaint and computes nonsense.
No hardware check catches that cheaply -- a value landing in the wrong place is
still a plausible value. These tests compose the three stages of the dataflow
as index arithmetic and compare against the packer the GEMM is validated
against.

The same composition is applied to the shipped bf16 dequant layout, whose
expected mapping is known independently (the sidecar generator reproduces the
NPU's output byte for byte). Reproducing that one is what makes the bfp16
result trustworthy: it tests the model of the dataflow, not just the arithmetic.
"""

import numpy as np
import pytest
import torch

from iron.operators.flm.dequant.design import (
    CORE_BLOCKS,
    CORE_JOIN_OFFSETS,
    CT_K,
    DRAIN_DIMS,
    GROUP,
    HALF_BLOCKS,
    K_TILE,
    K_TILE_B,
    M_TILE,
    N_TILE,
    S,
    T,
    TILE_BLOCKS,
)
from iron.operators.flm.packing import f32_to_bfp16ebs8, pack_b

ROWS = 4


def _apply(stream_idx, sizes, strides):
    """Destination index for a value arriving at stream_idx under (sizes, strides)."""
    out = np.zeros_like(stream_idx)
    rem = stream_idx.copy()
    for dim in range(len(sizes) - 1, -1, -1):
        out = out + (rem % sizes[dim]) * strides[dim]
        rem = rem // sizes[dim]
    return out


def _model(K, N):
    """Composed DDR block index for every (k, n), through the three stages."""
    n = np.arange(N)[:, None]
    k = np.arange(K)[None, :]

    # stage 1: the kernel's own emission order, dense in its output buffer
    kslice_loc, tb_loc = (k % K_TILE) // CT_K, (n % M_TILE) // T
    i, t_in = (k % CT_K) // S, n % T
    emit = ((kslice_loc * (M_TILE // T) + tb_loc) * (CT_K // S) + i) * T + t_in

    # stage 2: the join. A column has one memtile object per k-half of the
    # tile, each holding the two cores of that half back to back.
    n_half, k_half = (n % N_TILE) // M_TILE, (k % K_TILE_B) // K_TILE
    mt = np.array(CORE_JOIN_OFFSETS)[n_half] + emit

    # stage 3: the drain, which does the whole reorder within one half
    pos = _apply(mt, [d[0] for d in DRAIN_DIMS], [d[1] for d in DRAIN_DIMS])
    cb, kb = n // N_TILE, k // K_TILE_B
    tile_base = (cb * (K // K_TILE_B) + kb) * TILE_BLOCKS
    return tile_base + k_half * HALF_BLOCKS + pos


def _pack_b_block(K, N):
    """Which bfp16 block pack_b puts (k, n) in."""
    n = np.arange(N)[:, None]
    k = np.arange(K)[None, :]
    cb, kb = n // N_TILE, k // K_TILE_B
    kslice, i = (k % K_TILE_B) // CT_K, (k % CT_K) // S
    tb, t_in = (n % N_TILE) // T, n % T
    blk = (cb * (K // K_TILE_B) + kb) * (K_TILE_B // CT_K) + kslice
    blk = ((blk * (N_TILE // T) + tb) * (CT_K // S) + i) * T + t_in
    return blk


@pytest.mark.parametrize(
    "K, N", [(512, 64), (1024, 128), (2048, 256), (1536, 640), (2048, 2048)]
)
def test_block_index_matches_pack_b(K, N):
    assert np.array_equal(_model(K, N), _pack_b_block(K, N))


@pytest.mark.parametrize("K, N", [(512, 64), (1024, 128), (2048, 256)])
def test_bytes_match_pack_b(K, N):
    """End to end, including the conversion: the same bytes, in the same order."""
    rng = np.random.default_rng(0)
    B = rng.standard_normal((K, N)).astype(np.float32)
    # The cores round to bf16 before converting, so the reference has to as
    # well; otherwise this compares rounding, not ordering.
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


def test_drain_dims_are_dma_expressible():
    """Every stride must be a whole number of 4-byte words.

    A bfp16 block is 9 bytes and the DMA steps in 4, so only groups of blocks
    are addressable. DRAIN_DIMS is written in blocks; this is the check that
    the grouping survives translation to bytes.
    """
    block_bytes = T + 1
    for size, stride in DRAIN_DIMS[:-1]:
        assert (stride * block_bytes) % 4 == 0, (size, stride)
    assert (DRAIN_DIMS[-1][0] * block_bytes) % 4 == 0
    assert DRAIN_DIMS[-1][1] == 1
    # The innermost size rides a 10-bit field.
    assert DRAIN_DIMS[-1][0] <= 1023


def test_drain_covers_its_half_exactly():
    """The reorder must be a bijection: no overlap, no gap, nothing dropped."""
    sizes = [d[0] for d in DRAIN_DIMS]
    strides = [d[1] for d in DRAIN_DIMS]
    assert int(np.prod(sizes)) == HALF_BLOCKS
    covered = _apply(np.arange(HALF_BLOCKS), sizes, strides)
    assert np.array_equal(np.sort(covered), np.arange(HALF_BLOCKS))


def test_join_offsets_ascend_and_tile_the_buffer():
    """aie.objectfifo.link requires ascending segment offsets, and the four
    segments must exactly fill the memtile object."""
    assert CORE_JOIN_OFFSETS == sorted(CORE_JOIN_OFFSETS)
    assert len(set(CORE_JOIN_OFFSETS)) == len(CORE_JOIN_OFFSETS)
    assert CORE_JOIN_OFFSETS[-1] + CORE_BLOCKS == HALF_BLOCKS


# Every weight matrix dequant must serve for Gemma4 E2B, as (K in-features,
# N out-features). Derived from hidden_size 1536, intermediate_size 6144,
# DQ/DK/DV 4096/512/512 and the SWA and skip variants; 20 in all, deduplicated
# here to the 9 distinct shapes.
E2B_SHAPES = [
    (1536, 5120),  # global qkv
    (4096, 1536),  # global o, global o skip
    (1536, 6144),  # gate, up (global and swa)
    (6144, 1536),  # down (global and swa)
    (1536, 4096),  # global qkv skip
    (1536, 12288),  # gate/up skip
    (12288, 1536),  # down skip
    (1536, 2560),  # swa qkv
    (2048, 1536),  # swa o
    (1536, 2048),  # swa qkv skip
]


@pytest.mark.parametrize("K, N", E2B_SHAPES)
def test_e2b_shapes_are_servable(K, N):
    """Replacing the stock GEMM means dequantizing every E2B weight on device.

    The constraints are K a multiple of K_TILE_B, N a multiple of N_TILE, and
    more than one k iteration -- flm.GEMM switches to tile_n = 128 at a single
    iteration, which is a different packed order. E2B's smallest K is 1536, so
    none of its projections reach that case, and this pins that: a model or a
    tiling rule that changes it should fail here rather than at a GEMM reading
    a wrongly ordered buffer.
    """
    assert K % K_TILE_B == 0, f"K={K} does not tile"
    assert N % N_TILE == 0, f"N={N} does not tile"
    assert K // K_TILE_B > 1, f"K={K} would make flm.GEMM pick tile_n=128"
    # Enough column blocks to fill the grid, so no column sits idle.
    assert N // N_TILE >= 8, f"N={N} leaves columns without work"


@pytest.mark.parametrize("K", [512, 1024, 1536, 3072, 12288])
def test_engine_order_matches_file_order(K):
    """A linear read of engine order must deliver exactly what the gather does.

    This is what lets QwLayout be a descriptor switch rather than a redesign.
    If the two sequences differed, each core would get a different q4nx block
    and the output would be a permutation of itself -- right size, real values,
    wrong order.
    """
    bpr = K // K_TILE
    block_bytes = M_TILE * K_TILE * 5 // 8

    for cb in range(3):
        # file order, through the 4-D gather the design emits
        base = 2 * cb * bpr * block_bytes
        gathered = [
            (base + bc * block_bytes + br_off * bpr * block_bytes) // block_bytes
            for bc in range(bpr)
            for br_off in range(2)
        ]
        # engine order, read linearly from the same offset
        engine_of = {}
        for br in range(2 * (cb + 1)):
            for bc in range(bpr):
                engine_of[(br // 2) * 2 * bpr + bc * 2 + br % 2] = br * bpr + bc
        linear = [engine_of[2 * cb * bpr + i] for i in range(2 * bpr)]

        assert gathered == linear, f"K={K} cb={cb}"


@pytest.mark.parametrize("K", [1024, 12288])
def test_engine_descriptor_fits_the_bd_fields(K):
    """The linear read spends its whole length on two dimensions."""
    bpr = K // K_TILE
    block_bytes = M_TILE * K_TILE * 5 // 8
    outer = 2 * bpr * block_bytes // 512
    assert outer <= 1023, outer
    assert (512 // 4) <= 1023


def test_gate_up_runs_reach_every_column_block():
    """gate and up share a blob, so a projection's blocks come in runs.

    E2B interleaves them 512 out-features at a time in a 1024 period, which is
    8 column blocks of 64 in a period of 16.
    """
    N, run, period = 6144, 512, 1024
    n_blocks, run_blocks, period_blocks = N // N_TILE, run // N_TILE, period // N_TILE
    assert (run_blocks, period_blocks) == (8, 16)

    offsets = [
        (cb // run_blocks) * period_blocks + cb % run_blocks for cb in range(n_blocks)
    ]
    assert len(set(offsets)) == n_blocks  # no two blocks share a slot
    assert offsets[:9] == [0, 1, 2, 3, 4, 5, 6, 7, 16]  # the gap after a run
    # The other matrix's slots are exactly the ones this one skips.
    assert sorted(set(range(max(offsets) + 1)) - set(offsets)) == [
        p + i for p in range(8, max(offsets), period_blocks) for i in range(8)
    ]


def test_q4nx_block_is_a_whole_number_of_bfp16_blocks():
    """A scale group must not straddle two bfp16 blocks.

    The file shares one scale and min across GROUP consecutive k for one n; the
    output shares one exponent across S. If S did not divide GROUP the kernel
    would need two scales to fill one block.
    """
    assert GROUP % S == 0
    assert (M_TILE * K_TILE) % 8 == 0
