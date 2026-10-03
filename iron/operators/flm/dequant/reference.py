# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU reference for :class:`iron.operators.flm.DequantBFP`, bit-exact against
the device. See the operator's README.md for the layout and the rounding."""

import numpy as np
from aie.iron.kernels import q4nx_dequant_ref

from iron.operators.flm.dequant.design import (
    CT_K,
    K_TILE_B,
    N_TILE,
    S,
    T,
    qw_bytes_for,
)
from iron.operators.flm.aie2p_math_emulation import f32_to_bf16_floor
from iron.operators.flm.q4nx import (
    BLOCK_BYTES,
    GROUP,
    K_TILE,
    M_TILE,
    bf16_to_f32,
    packed_bytes,
)

# Out-features one run of code bytes spans.
PARALLEL = 16


def _blocks(qw):
    """The q4nx blob as rows of BLOCK_BYTES."""
    qw = np.asarray(qw, dtype=np.uint8).ravel()
    if qw.size % BLOCK_BYTES:
        raise ValueError(
            f"q4nx blob of {qw.size} bytes is not a whole number of blocks"
        )
    return qw.reshape(-1, BLOCK_BYTES)


def _block_origins(n_blocks, K):
    """(first out-feature, first in-feature) of each block of the blob.

    Block i of the blob is the i'th block that the cores consume: README.md
    layers 6-9.
    """
    k_tiles = K // K_TILE_B
    for i in range(n_blocks):
        cb, rest = divmod(i, 4 * k_tiles)
        kb, rest = divmod(rest, 4)
        k_half, n_half = divmod(rest, 2)
        yield (2 * cb + n_half) * M_TILE, (2 * kb + k_half) * K_TILE


def dequantize(qw, K, N):
    """q4nx blob to f32, shaped (N out-features, K in-features)."""
    b = _blocks(qw)
    n_blocks = len(b)

    n_groups = K_TILE // GROUP
    sm = n_groups * M_TILE * 2
    scales = bf16_to_f32(b[:, :sm].view(np.uint16).reshape(n_blocks, n_groups, M_TILE))
    mins = bf16_to_f32(
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

    out = np.empty((N, K), dtype=np.float32)
    for i, (r0, c0) in enumerate(_block_origins(n_blocks, K)):
        out[r0 : r0 + M_TILE, c0 : c0 + K_TILE] = vals[i]
    return out


def reference(qw, K, N):
    """The bytes the operator must produce, as a flat uint8 array."""
    b = _blocks(qw)
    enc = q4nx_dequant_ref(
        b, m_tile=M_TILE, k_tile=K_TILE, group=GROUP, ct_k=CT_K, s=S, t=T
    )
    # Each block's bytes are indexed [k slice, n // T, k // S in the slice,
    # n % T, 9]. Place the blocks in one such array for the whole matrix.
    enc = enc.reshape(len(b), K_TILE // CT_K, M_TILE // T, CT_K // S, T, 9)
    out = np.empty((K // CT_K, N // T, CT_K // S, T, 9), dtype=np.uint8)
    for i, (r0, c0) in enumerate(_block_origins(len(b), K)):
        out[c0 // CT_K : (c0 + K_TILE) // CT_K, r0 // T : (r0 + M_TILE) // T] = enc[i]
    # pack_b's order: (cb, kb, k slice, n // T in cb, k // S in the slice, n % T).
    out = out.reshape(
        K // K_TILE_B, K_TILE_B // CT_K, N // N_TILE, N_TILE // T, CT_K // S, T, 9
    )
    return out.transpose(2, 0, 1, 3, 4, 5, 6).ravel()


def scatter_runs(qw, K, N, run_out_features, run_period_out_features, seed=0):
    """Place a matrix's column blocks at their offsets in an interleaved
    buffer. The gaps hold noise, so an operator that reads them fails."""
    cb_bytes = packed_bytes(N_TILE * K)
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
