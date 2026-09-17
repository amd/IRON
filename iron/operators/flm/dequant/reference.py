# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU reference for :class:`iron.operators.flm.DequantBFP`, bit-exact against
the device. See the operator's README.md for the layout and the rounding."""

import numpy as np
import torch

from iron.operators.flm.dequant.design import (
    CT_K,
    GROUP,
    K_TILE,
    K_TILE_B,
    M_TILE,
    N_TILE,
    S,
    T,
    qw_bytes_for,
)
from iron.operators.flm.packing import pack_b

BLOCK_BYTES = M_TILE * K_TILE * 5 // 8
# Out-features one run of code bytes spans.
PARALLEL = 16


def _bf16_to_f32(u16):
    return (u16.astype(np.uint32) << 16).view(np.float32)


def f32_to_bf16_floor(x):
    """Round f32 to bf16 toward negative infinity, as the cores do."""
    u = np.ascontiguousarray(x, dtype=np.float32).view(np.uint32)
    inexact = (u & 0xFFFF) != 0
    negative = (u >> 31) != 0
    return ((u >> 16) + (inexact & negative)).astype(np.uint16)


def dequantize(qw, K, N):
    """q4nx blob to f32, shaped (N out-features, K in-features)."""
    k_tiles = K // K_TILE_B
    n_blocks = qw.size // BLOCK_BYTES
    if n_blocks * BLOCK_BYTES != qw.size:
        raise ValueError(
            f"q4nx blob of {qw.size} bytes is not a whole number of blocks"
        )
    b = qw.reshape(n_blocks, BLOCK_BYTES)

    n_groups = K_TILE // GROUP
    sm = n_groups * M_TILE * 2
    scales = _bf16_to_f32(b[:, :sm].view(np.uint16).reshape(n_blocks, n_groups, M_TILE))
    mins = _bf16_to_f32(
        b[:, sm : 2 * sm].view(np.uint16).reshape(n_blocks, n_groups, M_TILE)
    )

    qs = b[:, 2 * sm :].reshape(n_blocks, M_TILE // PARALLEL, K_TILE, PARALLEL // 2)
    q = np.empty((n_blocks, M_TILE // PARALLEL, K_TILE, PARALLEL), dtype=np.float32)
    q[..., 0::2] = (qs & 0xF).astype(np.float32)
    q[..., 1::2] = (qs >> 4).astype(np.float32)
    q = q.transpose(0, 1, 3, 2).reshape(n_blocks, M_TILE, K_TILE)

    grp = np.arange(K_TILE) // GROUP
    s = scales[:, grp, :].transpose(0, 2, 1)
    m = mins[:, grp, :].transpose(0, 2, 1)
    vals = m + s * q

    # Block i of the blob is the i'th the cores consume: README.md layers 6-9.
    out = np.empty((N, K), dtype=np.float32)
    for i in range(n_blocks):
        cb, rest = divmod(i, 4 * k_tiles)
        kb, rest = divmod(rest, 4)
        k_half, n_half = divmod(rest, 2)
        r0 = (2 * cb + n_half) * M_TILE
        c0 = (2 * kb + k_half) * K_TILE
        out[r0 : r0 + M_TILE, c0 : c0 + K_TILE] = vals[i]
    return out


def reference(qw, K, N):
    """The bytes the operator must produce, as a flat uint8 array."""
    w = dequantize(np.asarray(qw, dtype=np.uint8).ravel(), K, N)
    w = _bf16_to_f32(f32_to_bf16_floor(w))
    return pack_b(
        torch.from_numpy(np.ascontiguousarray(w.T)),
        K_TILE_B,
        N_TILE,
        S,
        T,
        CT_K,
        bfp16=True,
        round_conv_even=False,
    ).numpy()


def scatter_runs(qw, K, N, run_out_features, run_period_out_features, seed=0):
    """Place a matrix's column blocks at their offsets in an interleaved
    buffer. The gaps hold noise, so an operator that reads them fails."""
    cb_bytes = N_TILE * K * 5 // 8
    run_blocks = run_out_features // N_TILE
    period_blocks = run_period_out_features // N_TILE

    total = qw_bytes_for(K, N, run_out_features, run_period_out_features)
    out = np.random.default_rng(seed + 1).integers(0, 256, total, dtype=np.uint8)
    src = np.asarray(qw, dtype=np.uint8).reshape(-1, cb_bytes)
    for cb in range(N // N_TILE):
        at = ((cb // run_blocks) * period_blocks + cb % run_blocks) * cb_bytes
        out[at : at + cb_bytes] = src[cb]
    return out


def random_q4nx(K, N, seed=0):
    """A random q4nx blob. Scales and mins are bf16 in the file, so they are
    generated there and widened."""
    rng = np.random.default_rng(seed)
    n_blocks = (K // K_TILE) * (N // M_TILE)
    sm = (K_TILE // GROUP) * M_TILE

    scales = f32_to_bf16_floor(
        rng.uniform(0.002, 0.05, (n_blocks, sm)).astype(np.float32)
    )
    mins = f32_to_bf16_floor(rng.uniform(-0.4, 0.4, (n_blocks, sm)).astype(np.float32))
    codes = rng.integers(0, 256, (n_blocks, M_TILE * K_TILE // 2), dtype=np.uint8)
    return np.concatenate(
        [
            scales.view(np.uint8).reshape(n_blocks, -1),
            mins.view(np.uint8).reshape(n_blocks, -1),
            codes,
        ],
        axis=1,
    ).ravel()
