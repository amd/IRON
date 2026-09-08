# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""bf16 GEMM over a fixed 4x8 compute-tile grid.

This is a different design from ``iron.operators.gemm``, not a retuning of it.
The distinguishing choices, all of which the kernel's L1 layout depends on:

  * **A is broadcast along each compute row.** Four shim tiles (columns 0/2/4/6)
    each feed one row of the grid, and every one of the 8 tiles in that row
    consumes the same A object. B is broadcast down each column. So an A tile is
    fetched once per row rather than once per tile.
  * **C is joined at the memtile.** Each of the 4 tiles in a column writes its
    own 64x128 slice into one memtile buffer, which drains to DDR as a single
    256x128 block, rather than each tile draining separately.
  * **The mmul keeps A in a single ObjectFifo object** spanning every z slice
    (``flm_gemm_mmul.h``), instead of a ping/pong pair the kernel locks itself.
  * **The epilogue is fused**: the f32->bf16 conversion, an optional activation
    and an optional clamp all happen while the values are still in registers,
    on the way into the C object.

Geometry is fixed (m/k/n = 64/512/128, r/s/t = 8/8/8, 4x8 grid). The constants
below are the single source of truth: ``op.py`` passes them to the kernels as
-D flags, so the C++ and the dataflow cannot drift apart.
"""

import numpy as np
from ml_dtypes import bfloat16

from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.iron.device import Tile
from iron.operators._trace import maybe_enable_trace

# --- Fixed geometry -------------------------------------------------------
# GEMM tiling per compute tile, and the register tiling inside it.
M_TILE, K_TILE, N_TILE = 64, 512, 128
R, S, T = 8, 8, 8
ROWS, COLS = 4, 8

# Which shim column sources the A broadcast for each compute row. Spreading
# them over alternate columns keeps four independent MM2S paths; the existing
# gemm operator pins A the same way in the 8-column case.
A_SOURCE_COL = [0, 2, 4, 6]

# Must match compute_CT_k_max_n<N_TILE>() in flm_gemm_geometry.h: with n=128,
# a compute tile holds 32 of K at a time.
CT_MAX_K = 32
K_DIV_CT_K_MAX = K_TILE // CT_MAX_K

# Buffer lengths, in elements.
CT_A_LEN = 2 * R * CT_MAX_K  # one z slice
CT_A_OBJ = CT_A_LEN * (M_TILE // R // 2)  # A object: every z slice of one mmul
CT_OUT_LEN = 512  # the core's C slice, streamed out in chunks this size
C_SLICE_LEN = M_TILE * N_TILE  # one compute tile's C contribution
O_CHUNKS = C_SLICE_LEN // CT_OUT_LEN  # C objects one accumulator drains as
C_DEPTH = 2  # C fifo depth; also the core-body unroll
B_ITERS = K_TILE // CT_MAX_K  # B chunks the core consumes per k step
B_DEPTH = 2  # B fifo depth; also the core-body unroll
A_DEPTH = 2

STACK_SIZE = 4096

EPILOGUE_MODES = {"none": 0, "gelu": 1, "silu": 2, "sigmoid": 3}

# Minimum problem size, i.e. one pass of the whole grid.
MIN_M = M_TILE * ROWS  # 256
MIN_K = K_TILE  # 512
MIN_N = N_TILE * COLS  # 1024


def flm_gemm(
    dev,
    M,
    K,
    N,
    epilogue="none",
    kernel_object="flm_gemm.o",
    epilogue_object="flm_gemm_epilogue.o",
    trace_size=0,
):
    """Emit the MLIR module for an M x K @ K x N bf16 GEMM.

    A is (M, K) row-major, B is (K, N) row-major and C is (M, N) row-major, all
    bf16 and all plain dense tensors -- the block-major reordering B needs on
    the way in is done by the fill descriptor, not by the caller.
    """
    if epilogue not in EPILOGUE_MODES:
        raise ValueError(
            f"epilogue must be one of {sorted(EPILOGUE_MODES)}, got {epilogue!r}"
        )
    # The design has no partial-block path: a compute tile either does a full
    # m x n block of work or none at all. The existing gemm operator constrains
    # its shapes the same way.
    for name, value, unit in (("M", M, MIN_M), ("K", K, MIN_K), ("N", N, MIN_N)):
        if value % unit != 0:
            raise ValueError(f"{name} ({value}) must be a multiple of {unit}")

    bf16_ty = np.dtype[bfloat16]
    f32 = np.dtype[np.float32]

    # How many times the whole grid sweeps, in each dimension.
    n_col_blocks = N // MIN_N
    m_row_blocks = M // MIN_M
    k_iters = K // K_TILE

    # L1 (per compute tile)
    ct_a_obj_ty = np.ndarray[(CT_A_OBJ,), bf16_ty]
    ct_b_ty = np.ndarray[(CT_MAX_K * N_TILE,), bf16_ty]
    ct_out_ty = np.ndarray[(CT_OUT_LEN,), bf16_ty]
    ct_acc_ty = np.ndarray[(M_TILE * N_TILE,), f32]
    # L2 (per memtile)
    mt_a_ty = np.ndarray[(M_TILE * K_TILE,), bf16_ty]
    mt_b_ty = np.ndarray[(K_TILE * N_TILE,), bf16_ty]
    mt_out_ty = np.ndarray[(C_SLICE_LEN * ROWS,), bf16_ty]
    # L3 (DDR), flat -- the taps below index them linearly.
    a_l3_ty = np.ndarray[(M * K,), bf16_ty]
    b_l3_ty = np.ndarray[(K * N,), bf16_ty]
    c_l3_ty = np.ndarray[(M * N,), bf16_ty]

    acc_init = Kernel("flm_gemm_acc_init", kernel_object, [ct_acc_ty])
    k_step = Kernel(
        "flm_gemm_k_step", kernel_object, [ct_a_obj_ty, ct_b_ty, ct_acc_ty]
    )
    epilogue_chunk = Kernel(
        "flm_gemm_epilogue_chunk",
        epilogue_object,
        [ct_out_ty, ct_acc_ty, np.int32, np.int32],
    )

    # --- Data movement ----------------------------------------------------
    #
    # These stream-dimension lists are the load-bearing part of the design:
    # they are what turns a row-major DDR tile into the r x s / s x t blocked
    # layout the mmul indexes, and they are tightly coupled to it. A mismatch
    # here produces silently wrong results, not a build error.

    # C: de-block each core's r x t tiled output back into row-major within its
    # 64x128 slice, on the way into the memtile.
    gather_dims = [(M_TILE // R, R * N_TILE), (N_TILE // T, T), (R, N_TILE), (T, 1)]
    # B: DDR row-major (k x n) -> s x t blocks (recv), then split into the
    # CT_MAX_K-deep chunks a single mmul call consumes (send).
    b_recv_dims = [(N_TILE // T, K_TILE * T), (T, S), (K_TILE // S, S * T), (S, 1)]
    b_send_dims = [
        (K_DIV_CT_K_MAX, T * CT_MAX_K),
        (N_TILE // T, K_TILE * T),
        (T * CT_MAX_K, 1),
    ]
    # A: same idea, r x s blocks.
    a_recv_dims = [(M_TILE // R, R * K_TILE), (R, S), (K_TILE // S, R * S), (S, 1)]
    a_send_dims = [
        (K_DIV_CT_K_MAX, R * CT_MAX_K),
        (M_TILE // R, R * K_TILE),
        (R * CT_MAX_K, 1),
    ]

    # C: one join per column. Each of the ROWS cores in the column drops its
    # slice at its own offset in a single memtile buffer, which then drains to
    # DDR as one contiguous (ROWS*M_TILE) x N_TILE block.
    c_l2l3_fifos = []
    c_prod = {}
    for c in range(COLS):
        of_c = ObjectFifo(mt_out_ty, name=f"C_L2L3_{c}", depth=C_DEPTH)
        c_l2l3_fifos.append(of_c)
        sub = of_c.prod().join(
            [C_SLICE_LEN * r for r in range(ROWS)],
            obj_types=[ct_out_ty] * ROWS,
            names=[f"C_L1L2_{c}_{r}" for r in range(ROWS)],
            dims_from_stream=[gather_dims] * ROWS,
            tile=Tile(c, 1),
        )
        for r in range(ROWS):
            c_prod[(r, c)] = sub[r]

    # A: shim -> memtile -> broadcast along the compute row. The reblocking
    # rides the forward(): inbound on cons(dims_from_stream=), outbound on
    # forward(dims_to_stream=), sharing one memtile buffer.
    a_l3l2_fifos = []
    a_cons = {}
    for r in range(ROWS):
        src = A_SOURCE_COL[r]
        of_a_in = ObjectFifo(mt_a_ty, name=f"A_L3L2_{r}", depth=A_DEPTH)
        a_l3l2_fifos.append(of_a_in)
        of_a = of_a_in.cons(dims_from_stream=a_recv_dims).forward(
            tile=Tile(src, 1),
            obj_type=ct_a_obj_ty,
            depth=A_DEPTH,
            name=f"A_L2L1_{r}",
            dims_to_stream=a_send_dims,
        )
        # One cons() handle per column: every tile in the row sees this object.
        for c in range(COLS):
            a_cons[(r, c)] = of_a.cons()

    # B: shim -> memtile -> broadcast down the compute column.
    b_l3l2_fifos = []
    b_cons = {}
    for c in range(COLS):
        of_b_in = ObjectFifo(mt_b_ty, name=f"B_L3L2_{c}", depth=B_DEPTH)
        b_l3l2_fifos.append(of_b_in)
        of_b = of_b_in.cons(dims_from_stream=b_recv_dims).forward(
            tile=Tile(c, 1),
            obj_type=ct_b_ty,
            depth=B_DEPTH,
            name=f"B_L2L1_{c}",
            dims_to_stream=b_send_dims,
        )
        for r in range(ROWS):
            b_cons[(r, c)] = of_b.cons()

    # --- Compute ----------------------------------------------------------
    def core_fn(acc, o_h, b_h, a_h, init_k, kstep_k, epi_k):
        # The loop nest lives here rather than inside the kernel so that every
        # level has an ObjectFifo acquire point. With M/K/N known at compile
        # time all the trip counts are constants.
        for _ in range_(n_col_blocks):
            for _ in range_(m_row_blocks):
                init_k(acc)
                for _ in range_(k_iters):
                    # The l loop is unrolled by the B fifo depth so the
                    # acquired buffer index stays a compile-time constant.
                    for _ in range_(B_ITERS // B_DEPTH):
                        for _ in range(B_DEPTH):
                            b = b_h.acquire(1)
                            a = a_h.acquire(1)
                            kstep_k(a, b, acc)
                            a_h.release(1)
                            b_h.release(1)
                # Drain the accumulator. Unrolled by C_DEPTH for the same
                # reason; a full O_CHUNKS unroll overflows program memory.
                for chunk in range_(O_CHUNKS // C_DEPTH):
                    for half in range(C_DEPTH):
                        o = o_h.acquire(1)
                        epi_k(o, acc, chunk, half)
                        o_h.release(1)

    workers = []
    for r in range(ROWS):
        for c in range(COLS):
            tile = Tile(c, r + 2)
            acc = Buffer(tile=tile, type=ct_acc_ty, name=f"c_acc_{r}_{c}")
            workers.append(
                Worker(
                    core_fn,
                    [
                        acc,
                        c_prod[(r, c)].prod(),
                        b_cons[(r, c)],
                        a_cons[(r, c)],
                        acc_init,
                        k_step,
                        epilogue_chunk,
                    ],
                    tile=tile,
                    stack_size=STACK_SIZE,
                )
            )

    # --- Runtime ----------------------------------------------------------
    #
    # Every wrap below stays under the shim's 10-bit (1023) size field: the
    # largest are K_TILE=512 and ROWS*M_TILE=256.
    def a_tap(mega_row, r, kb):
        # One M_TILE x K_TILE block of A, row-major -- which is exactly the
        # order the memtile's dims_from_stream expects, so no reordering is
        # needed here (unlike B).
        #
        # Issued one k-block at a time, like B. Packing all k_iters blocks into
        # a single BD also describes the right bytes, but that one BD then has
        # to stall part-way through whenever k_iters exceeds the fifo depth,
        # while still holding its shim channel -- which deadlocks against the
        # C drain sharing that channel. It survives k_iters <= A_DEPTH and
        # hangs above it, so the failure only appears at larger K.
        return TensorAccessPattern(
            tensor_dims=(M * K,),
            offset=(mega_row * ROWS + r) * M_TILE * K + kb * K_TILE,
            sizes=[1, 1, M_TILE, K_TILE],
            strides=[0, 0, K, 1],
        )

    def b_tap(mega_col, c, kb):
        # One K_TILE x N_TILE chunk of B's column stripe, reordered on the fly.
        #
        # B is a plain row-major (K, N) tensor, but the memtile's
        # dims_from_stream expects the elements in t-block-major order --
        # (n//T, k%S, k//S, n%T), outermost first -- not row-major. Rather than
        # make the caller pre-pack B (which is what the design this came from
        # did on the host), the gather is expressed here, so B stays an ordinary
        # dense tensor. Getting this order wrong yields silently wrong results,
        # not a build error.
        #
        # Only one k-block fits in the 4 available dimensions, so the caller
        # issues one of these per k iteration; each delivers exactly one
        # memtile object.
        return TensorAccessPattern(
            tensor_dims=(K * N,),
            offset=(mega_col * COLS + c) * N_TILE + kb * K_TILE * N,
            sizes=[N_TILE // T, S, K_TILE // S, T],
            strides=[T, N, S * N, 1],
        )

    def c_tap(mega_col, mega_row, c):
        # One joined block: ROWS*M_TILE rows of this column's N_TILE-wide slice.
        return TensorAccessPattern(
            tensor_dims=(M * N,),
            offset=mega_row * ROWS * M_TILE * N + (mega_col * COLS + c) * N_TILE,
            sizes=[1, 1, ROWS * M_TILE, N_TILE],
            strides=[0, 0, N, 1],
        )

    # A shim tile supports only SHIM_BD_LIMIT simultaneously active buffer
    # descriptors, and shim column 0 carries three legs at once: the A fills
    # for compute row 0, the B fills for compute column 0, and the C drain for
    # compute column 0. So each k iteration in flight costs 2 BDs there, plus
    # one for the drain -- and exceeding the limit is a hard compile error, not
    # a slowdown. Retire the fills in batches sized to stay under it.
    SHIM_BD_LIMIT = 16
    K_BATCH = max(1, (SHIM_BD_LIMIT - 2) // 2)  # leave room for the C drain

    def sequence(A, B, C, a_prods, b_prods, c_conses):
        for mega_col in range(n_col_blocks):
            for mega_row in range(m_row_blocks):
                # The drain is issued first and retired last: it is an S2MM
                # that simply waits for the cores to produce, so having it
                # outstanding across the whole sweep is what lets compute and
                # write-back overlap. It must NOT share a task group with the
                # fills -- finishing a group that contains it before the fills
                # it depends on have been issued would deadlock.
                tg_c = TaskGroup()
                for c in range(COLS):
                    c_conses[c].drain(
                        C, c_tap(mega_col, mega_row, c), group=tg_c, wait=True
                    )

                # One A and one B object per k iteration, matching the core's
                # k_iters x B_ITERS acquires on each leg.
                for batch in range(0, k_iters, K_BATCH):
                    tg_f = TaskGroup()
                    for kb in range(batch, min(batch + K_BATCH, k_iters)):
                        for r in range(ROWS):
                            a_prods[r].fill(A, a_tap(mega_row, r, kb), group=tg_f)
                        for c in range(COLS):
                            b_prods[c].fill(B, b_tap(mega_col, c, kb), group=tg_f)
                    tg_f.finish()
                tg_c.finish()

    rt = Runtime(
        sequence,
        [
            a_l3_ty,
            b_l3_ty,
            c_l3_ty,
            [
                f.prod(tile=Tile(A_SOURCE_COL[r], 0))
                for r, f in enumerate(a_l3l2_fifos)
            ],
            [f.prod(tile=Tile(c, 0)) for c, f in enumerate(b_l3l2_fifos)],
            [f.cons(tile=Tile(c, 0)) for c, f in enumerate(c_l2l3_fifos)],
        ],
    )

    my_program = Program(dev, rt, workers=workers)
    maybe_enable_trace(my_program, trace_size, workers)
    return my_program.resolve_program()
