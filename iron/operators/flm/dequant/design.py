# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""q4nx to bfp16, emitting B in ``flm.GEMM``'s packed order. See README.md."""

import numpy as np

from aie.dialects._aie_enum_gen import AIEArch
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker

from iron.common.device_utils import get_kernel_dir

# flm.GEMM's B tiling, imported rather than restated: this design has to write
# the buffer in the order that one reads it, and two copies would drift.
from iron.operators.flm.gemm.design import (
    BFP16_GROUP,
    CT_MAX_K_FOR_N,
    K_TILE as K_TILE_B,
    N_TILE_DEFAULT as N_TILE,
    S,
    T,
)

# q4nx block: 32 out-features x 256 in-features, 32 weights per scale and min.
M_TILE, K_TILE, GROUP = 32, 256, 32
BLOCK_BYTES = M_TILE * K_TILE * 5 // 8

CT_K = CT_MAX_K_FOR_N[N_TILE]

ROWS, COLS = 4, 8

CORE_BLOCKS = M_TILE * K_TILE // BFP16_GROUP
SLAB_BLOCKS = N_TILE * K_TILE_B // BFP16_GROUP
HALF_BLOCKS = SLAB_BLOCKS // 2

# One core's contiguous run: every n it owns over one k slice.
RUN = (M_TILE // T) * (CT_K // S) * T
SPLIT = 2

# Outermost first: n-half, k slice, then the core's run, split so the innermost
# size stays inside the BD's field.
DRAIN_DIMS = [
    (N_TILE // M_TILE, RUN),
    (K_TILE // CT_K, (N_TILE // T) * (CT_K // S) * T),
    (SPLIT, RUN // SPLIT),
    (RUN // SPLIT, 1),
]
DRAIN_SIZES = [d[0] for d in DRAIN_DIMS]
DRAIN_STRIDES = [d[1] for d in DRAIN_DIMS]

# Core i takes n-half i % 2 and k-half i // 2, so cores 0/1 form the k-half 0
# object and cores 2/3 the k-half 1 object.
CORE_JOIN_OFFSETS = [0, CORE_BLOCKS]
HALVES = 2


def _run_geometry(run_out_features, run_period_out_features, n_blocks):
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
    run_blocks, period_blocks = _run_geometry(
        run_out_features, run_period_out_features, n_blocks
    )
    last = n_blocks - 1
    cb = (last // run_blocks) * period_blocks + last % run_blocks + 1
    return cb * N_TILE * K * 5 // 8


def dequant_bfp(
    dev,
    K,
    N,
    tile_n=N_TILE,
    run_out_features=None,
    run_period_out_features=None,
    trace_size=0,
):
    """K in-features, N out-features. B reaches the GEMM as (K, N)."""
    if dev.arch != AIEArch.AIE2p:
        raise NotImplementedError("bfp16ebs8 exists only on AIE2P")
    if tile_n != N_TILE:
        raise NotImplementedError(
            f"tile_n must be {N_TILE}; flm.GEMM picks {tile_n} for this shape, "
            "and the two must agree or the GEMM reads B in the wrong order"
        )
    if K % K_TILE_B:
        raise ValueError(f"K ({K}) must be a multiple of {K_TILE_B}")
    if N % N_TILE:
        raise ValueError(f"N ({N}) must be a multiple of {N_TILE}")

    k_tiles = K // K_TILE_B
    blocks_per_row = K // K_TILE
    n_blocks = N // N_TILE

    cb_bytes = N_TILE * K * 5 // 8
    run_blocks, period_blocks = _run_geometry(
        run_out_features, run_period_out_features, n_blocks
    )

    qw_bytes = qw_bytes_for(K, N, run_out_features, run_period_out_features)
    out_blocks = K * N // BFP16_GROUP

    qw_l3_ty = np.ndarray[(qw_bytes,), np.dtype[np.uint8]]
    out_l3_ty = np.ndarray[(out_blocks,), np.dtype[v8bfp16ebs8]]
    qw_col_ty = np.ndarray[(ROWS * BLOCK_BYTES,), np.dtype[np.uint8]]
    qw_blk_ty = np.ndarray[(BLOCK_BYTES,), np.dtype[np.uint8]]
    out_half_ty = np.ndarray[(HALF_BLOCKS,), np.dtype[v8bfp16ebs8]]
    out_blk_ty = np.ndarray[(CORE_BLOCKS,), np.dtype[v8bfp16ebs8]]

    kernel = Kernel(
        "q4nx_dequant_bfp",
        f"q4nx_dequant_{get_kernel_dir(dev)}.o",
        [qw_blk_ty, out_blk_ty],
    )

    def core_body(qw_in, out_of, k):
        qw = qw_in.acquire(1)
        out = out_of.acquire(1)
        k(qw, out)
        qw_in.release(1)
        out_of.release(1)

    workers = []
    qw_prods, out_conses = [], []

    for c in range(COLS):
        of_qw = ObjectFifo(qw_col_ty, name=f"qw_{c}", depth=2)
        qw_prods.append(of_qw.prod())
        qw_cores = of_qw.cons().split(
            [BLOCK_BYTES * r for r in range(ROWS)],
            obj_types=[qw_blk_ty] * ROWS,
            names=[f"qw_{c}_{r}" for r in range(ROWS)],
        )

        out_cores, halves = [], []
        for h in range(HALVES):
            of_out = ObjectFifo(out_half_ty, name=f"w_{c}_{h}", depth=2)
            halves.append(of_out.cons())
            out_cores += of_out.prod().join(
                CORE_JOIN_OFFSETS,
                obj_types=[out_blk_ty] * (ROWS // HALVES),
                names=[f"w_{c}_{h}_{r}" for r in range(ROWS // HALVES)],
            )
        out_conses.append(halves)

        # aiecc measures 1216 bytes against the 1024-byte device default.
        workers += [
            Worker(
                core_body,
                [qw_cores[r].cons(), out_cores[r].prod(), kernel],
                stack_size=2048,
            )
            for r in range(ROWS)
        ]

    # A column block is read straight through. The block is split 10 x 512 so
    # the innermost size stays inside the BD's field.
    qw_sizes = [blocks_per_row, 2, BLOCK_BYTES // 512, 512]
    qw_strides = [2 * BLOCK_BYTES, BLOCK_BYTES, 512, 1]

    def sequence(QW, OUT, qw_prod_hs, out_cons_hs):
        for cb0 in range(0, n_blocks, COLS):
            columns = [(c, cb0 + c) for c in range(COLS) if cb0 + c < n_blocks]

            tg_fill = TaskGroup()
            for c, cb in columns:
                offset = (
                    (cb // run_blocks) * period_blocks + cb % run_blocks
                ) * cb_bytes
                qw_prod_hs[c].fill(
                    QW,
                    TensorAccessPattern((1, qw_bytes), offset, qw_sizes, qw_strides),
                    group=tg_fill,
                )

            prev = None
            for kb in range(k_tiles):
                tg = TaskGroup()
                for c, cb in columns:
                    for h in range(HALVES):
                        out_cons_hs[c][h].drain(
                            OUT,
                            TensorAccessPattern(
                                (1, out_blocks),
                                (cb * k_tiles + kb) * SLAB_BLOCKS + h * HALF_BLOCKS,
                                DRAIN_SIZES,
                                DRAIN_STRIDES,
                            ),
                            wait=True,
                            group=tg,
                        )
                # finish() awaits the group, so closing the previous k-tile
                # here overlaps its wait with this one, already running.
                if prev is not None:
                    prev.finish()
                prev = tg
            prev.finish()
            # The fill is not awaited. A core reads it before it writes the
            # output a drain takes, so a completed drain implies a completed
            # fill.
            tg_fill.finish()

    rt = Runtime(sequence, [qw_l3_ty, out_l3_ty, qw_prods, out_conses])
    prog = Program(dev, rt, workers=workers)
    if trace_size > 0:
        prog.enable_trace(trace_size)
    return prog.resolve_program()
