# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The q4nx and packed-bfp16 geometry. The array and the sequence are in op.py.

See README.md for the layout this describes.
"""

# flm.GEMM's B tiling, imported rather than restated: this design has to write
# the buffer in the order that one reads it, and two copies would drift.
from iron.exports.flm.gemm.design import (
    BFP16_GROUP,
    CT_MAX_K_FOR_N,
    S,
    T,
)
from iron.exports.flm.gemm.design import (
    K_TILE as K_TILE_B,
)
from iron.exports.flm.gemm.design import (
    N_TILE_DEFAULT as N_TILE,
)

# q4nx block: 32 out-features x 256 in-features, 32 weights per scale and min.
M_TILE, K_TILE, GROUP = 32, 256, 32
BLOCK_BYTES = M_TILE * K_TILE * 5 // 8

CT_K = CT_MAX_K_FOR_N[N_TILE]

# Four cores per column: each takes one n-half and one k-half of the column
# block. The column count is the device's, so it lives on the overlay.
ROWS = 4

CORE_BLOCKS = M_TILE * K_TILE // BFP16_GROUP
SLAB_BLOCKS = N_TILE * K_TILE_B // BFP16_GROUP
HALF_BLOCKS = SLAB_BLOCKS // 2

# One core's contiguous run: every n it owns over one k slice.
RUN = (M_TILE // T) * (CT_K // S) * T
SPLIT = 2

# Outermost first: n-half, k slice, then the core's run, split so the innermost
# size stays inside the BD's field.
DRAIN_SIZES = (N_TILE // M_TILE, K_TILE // CT_K, SPLIT, RUN // SPLIT)
DRAIN_STRIDES = (RUN, (N_TILE // T) * (CT_K // S) * T, RUN // SPLIT, 1)
DRAIN_DIMS = list(zip(DRAIN_SIZES, DRAIN_STRIDES))

# Core i takes n-half i % 2 and k-half i // 2, so cores 0/1 form the k-half 0
# object and cores 2/3 the k-half 1 object.
CORE_JOIN_OFFSETS = [0, CORE_BLOCKS]
HALVES = 2


def run_geometry(run_out_features, run_period_out_features, n_blocks):
    if run_out_features is None and run_period_out_features is None:
        return n_blocks, n_blocks
    if run_out_features is None or run_period_out_features is None:
        raise ValueError("run_out_features and run_period_out_features go together")
    for name, v in (
        ("run_out_features", run_out_features),
        ("run_period_out_features", run_period_out_features),
    ):
        if v % N_TILE:
            raise ValueError(f"{name} ({v}) must be a multiple of {N_TILE}")
    if run_period_out_features < run_out_features:
        raise ValueError("run_period_out_features must be at least run_out_features")
    return run_out_features // N_TILE, run_period_out_features // N_TILE


def qw_bytes_for(K, N, run_out_features=None, run_period_out_features=None):
    """Bytes the operator reads, counting any gap it strides over."""
    n_blocks = N // N_TILE
    run_blocks, period_blocks = run_geometry(
        run_out_features, run_period_out_features, n_blocks
    )
    last = n_blocks - 1
    cb = (last // run_blocks) * period_blocks + last % run_blocks + 1
    return cb * N_TILE * K * 5 // 8
