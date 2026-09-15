# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""CPU reference for :class:`iron.operators.flm.DequantBFP`.

Bit-exact against the device, not approximate, which is what lets the test
compare bytes. Two details make that possible and both are load-bearing:

* The cores round f32 to bf16 toward negative infinity. That is the AIE's
  power-up mode, and nothing in the kernel calls ``set_rounding``. Truncating
  the bit pattern instead rounds toward zero and differs on every inexact
  negative -- about 11% of a normal weight tensor.
* The bf16 result is converted to bfp16ebs8 under the same mode, so ``pack_b``
  is called with ``round_conv_even=False``.

This matches the q4nx reader in FastFlowLM_IRON's sidecar generator, which was
validated byte for byte against the shipped dequant xclbin.
"""

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
)
from iron.operators.flm.packing import pack_b

BLOCK_BYTES = M_TILE * K_TILE * 5 // 8
# A byte holds two out-features at one in-feature. PARALLEL is the row span the
# file interleaves them over.
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
    blocks_per_row = K // K_TILE
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
    # The min is added, not subtracted: it is an offset, despite the zero-point
    # name the shipped kernel gives its buffer.
    vals = m + s * q

    out = np.empty((N, K), dtype=np.float32)
    for i in range(n_blocks):
        r0 = (i // blocks_per_row) * M_TILE
        c0 = (i % blocks_per_row) * K_TILE
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


def to_engine_order(qw, K, N):
    """Permute a file-order blob into the order FastFlowLM's engine writes.

    The engine interleaves pairs of block-rows as it reads from disk, so block
    ``(br, bc)`` lands at ``(br // 2) * 2 * blocks_per_row + bc * 2 + br % 2``
    instead of ``br * blocks_per_row + bc``.
    """
    bpr = K // K_TILE
    blocks = np.asarray(qw, dtype=np.uint8).reshape(-1, BLOCK_BYTES)
    out = np.empty_like(blocks)
    for br in range(blocks.shape[0] // bpr):
        for bc in range(bpr):
            out[(br // 2) * 2 * bpr + bc * 2 + br % 2] = blocks[br * bpr + bc]
    return out.ravel()


def column_block_bytes(K):
    """Bytes one N_TILE-wide column block occupies. Contiguous in both layouts."""
    return N_TILE * K * 5 // 8


def scatter_runs(qw, K, N, run_out_features, run_period_out_features, seed=0):
    """Place a matrix's column blocks at their offsets in an interleaved buffer.

    FastFlowLM packs gate and up into one blob, so a projection's column blocks
    come in runs with a gap between them. The gap is filled with noise here, to
    catch an operator that reads it.
    """
    from iron.operators.flm.dequant.design import qw_bytes_for

    cb_bytes = column_block_bytes(K)
    run_blocks = run_out_features // N_TILE
    period_blocks = run_period_out_features // N_TILE

    total = qw_bytes_for(K, N, run_out_features, run_period_out_features)
    rng = np.random.default_rng(seed + 1)
    out = rng.integers(0, 256, total, dtype=np.uint8)

    src = np.asarray(qw, dtype=np.uint8).reshape(-1, cb_bytes)
    for cb in range(N // N_TILE):
        at = ((cb // run_blocks) * period_blocks + cb % run_blocks) * cb_bytes
        out[at : at + cb_bytes] = src[cb]
    return out


def random_q4nx(K, N, seed=0):
    """A random q4nx blob, for tests. Scales and mins are bf16 in the file, so
    they are generated there and widened, not rounded afterwards."""
    rng = np.random.default_rng(seed)
    n_blocks = (K // K_TILE) * (N // M_TILE)
    n_groups = K_TILE // GROUP
    sm = n_groups * M_TILE

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
