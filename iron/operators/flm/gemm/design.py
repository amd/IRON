# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""bf16 GEMM over a 4-row compute-tile grid, as wide as the device.

A second GEMM design alongside ``iron.operators.gemm``, specialised for
transformer projection shapes. The overall dataflow is the same whole-array
shape as that operator's -- A broadcast along each compute row, B down each
column, C joined through the memtile -- so those are NOT what distinguishes it.
What does:

  * **Fixed tiling.** m/k/n = 64/512/128 and r/s/t = 8/8/8, rather than
    parameterised tiles. Only the grid WIDTH varies with the device: 8 columns
    on NPU2, 4 on NPU1.
  * **A fused epilogue.** The f32->bf16 conversion, an optional activation and
    an optional clamp all happen while the values are still in registers, on the
    way into the C object, instead of a separate pass over L1.
  * **B arrives pre-packed** by ``GEMM.pack_B``, in the order the cores consume
    it, so both B hops are plain linear descriptors. On NPU2 it is also
    quantized to bfp16ebs8.
  * **Asymmetric tile buffering**, so the A tile and the accumulator need not
    share a height.

The constants below are the single source of truth: ``op.py`` passes them to the
kernels as -D flags, so the C++ and the dataflow cannot drift apart.

r/s/t stays 8/8/8 on both architectures. AIE2's native bf16 mac is 4x8x4, but
``aie::mmul<8,8,8>`` decomposes onto it as exactly four native macs with no
wasted lanes, so the whole blocked L1 layout -- ``pack_B``, the four stream
dimension lists below, and ``gather_dims`` -- is shared verbatim. Only AIE2P has
the bfp16-emulated path that does the same shape in two macs, which is why
``op.py`` passes ``AIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16`` there and not here.
"""

import argparse

import numpy as np
from ml_dtypes import bfloat16

from aie.helpers.util import v8bfp16ebs8

from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Buffer,
    Kernel,
    ObjectFifo,
    Program,
    Runtime,
    TaskGroup,
    Worker,
)
from aie.iron.controlflow import range_
from aie.iron.device import NPU1, NPU2, Tile
from iron.common.device_utils import get_kernel_dir
from iron.operators._trace import maybe_enable_trace

# --- Fixed geometry -------------------------------------------------------
# GEMM tiling per compute tile, and the register tiling inside it.
M_TILE, K_TILE = 64, 512
# Default n tile. 64 gives the mmul a colA of 8 rather than 4, halving the
# accumulator traffic per mac, at the cost of doubling A fetches (the grid
# then covers 512 columns of N per pass instead of 1024). That trade wins
# whenever compute is the critical path, which is the usual case; see
# README.md for the measured sweep, including the small-K shape where it
# loses.
N_TILE_DEFAULT = 64
# How much of K one compute tile holds at a time, per n width. This is a fixed
# L1 budget split two ways, so a wider n tile leaves less room for B's k slice
# and the product stays roughly constant. op.py passes the chosen value to the
# kernel as -DMM_FUSED_CT_K, making this table the only place it is decided.
CT_MAX_K_FOR_N = {16: 16, 32: 32, 64: 128, 128: 32, 256: 16}
# Register tiling. 8/8/8 on both architectures today; register_tiling() is the
# single source of truth and returns exactly these.
R, S, T = 8, 8, 8
ROWS = 4
# Widest grid this design supports, i.e. NPU2. The actual width comes from the
# device (see grid_cols); this is only what op.py uses to name artifacts.
MAX_COLS = 8


def grid_cols(dev):
    """Grid width: 8 on NPU2 (Strix/Krackan), 4 on NPU1 (Phoenix)."""
    return min(dev.cols, MAX_COLS)


def register_tiling(dev_name):
    """The mmul's r/s/t, as (r, s, t). 8/8/8 on both architectures.

    A function rather than a bare constant because r/t is the natural thing to
    retune per device, and because getting it wrong is silent: these set the
    blocked L1 layout, so ``pack_B``, the four stream-dimension lists below and
    ``gather_dims`` all key off them.

    Matching AIE2's native 4x8x4 mac shape here is a dead end -- it measures
    22-30% slower. The kernel is load-port bound, not shuffle bound, and 4/8/4
    needs 1.62 loads per mac against 8/8/8's 1.06, because the 2x2 register
    block amortizes each load over four macs either way but over far less work.
    Retrying it needs a wider register block on the native shape, i.e. a 4x4
    mmul kernel, not just a different r/s/t here.
    """
    return (R, S, T)


def a_source_cols(cols):
    """Which shim column sources the A broadcast for each compute row.

    On an 8-column grid the four A streams go to alternate columns, so each gets
    its own shim MM2S path and never contends with a B fill; the existing gemm
    operator pins A the same way. A 4-column grid has no such slack -- every
    column must source one A row AND one B column AND drain C, which is 2 MM2S +
    1 S2MM, exactly saturating a shim tile's channels.
    """
    return [2 * r for r in range(ROWS)] if cols >= 2 * ROWS else list(range(ROWS))


CT_OUT_LEN = 512  # the core's C slice, streamed out in chunks this size
C_DEPTH = 2  # C fifo depth; also the core-body unroll
B_DEPTH = 2  # B fifo depth; also the core-body unroll
A_DEPTH = 2
# How many column-blocks the runtime sequence keeps in flight. A block costs 3
# shim buffer descriptors on a column (A + B + C) against 16 available, so the
# ceiling is 5; 2 is enough to keep the fills ahead of the cores.
OVERLAP_DEFAULT = 2

STACK_SIZE = 4096
# Usable L1 per compute tile: 64 KB less the stack and a little slack.
L1_BUDGET = 60 * 1024

EPILOGUE_MODES = {"none": 0, "gelu": 1, "silu": 2, "sigmoid": 3}
# The epilogue entry point, shared by the design and op.py (which needs it
# to mark the symbol alwaysinline when building the inline .ll variant).
EPILOGUE_SYMBOL = "mm_fused_epilogue_chunk"

# Minimum problem size, i.e. one pass of the whole grid. MIN_N depends on the
# chosen n tile, so it is computed per call.
MIN_M = M_TILE * ROWS  # 256
MIN_K = K_TILE  # 512


# B is bfp16ebs8 on AIE2P and bf16 on AIE2 -- the scalar BFP types exist only
# on AIE2P (see GEMM._bfp16_b). BFP16_GROUP is how many B values one element
# of the MLIR type holds: v8bfp16ebs8 holds 8, bf16 holds 1.
BFP16_GROUP = 8


def bfp16_b_for(dev):
    """Whether B is stored as bfp16ebs8 for this device. AIE2P only."""
    return get_kernel_dir(dev) == "aie2p"


def _b_bytes(elems, bfp16_b):
    """Bytes B occupies in L1/L2. bfp16ebs8 packs 8 values as 8 mantissa bytes
    plus one shared exponent; bf16 is a plain 2 bytes each."""
    if not bfp16_b:
        return elems * 2
    assert elems % BFP16_GROUP == 0
    return elems // BFP16_GROUP * 9


# Shim-tile DMA BD step field is 20 bits wide (AIE2p; see mlir-aie's
# AIETargetModel::getDmaBdStepBits and AIEXDialect.cpp's "Stride N exceeds"
# verifier). An IR-level bf16-element stride S is re-expressed in hardware
# units as (S - 1) * 2 bytes / 4-byte address granularity before that check,
# so S must satisfy hw_stride_bf16(S) <= (1 << 20) - 1.
_SHIM_STEP_BITS = 20
_BF16_BYTES = 2
_ADDR_GRANULARITY_BYTES = 4
# Buffer descriptors per shim tile (AIETargetModel::getNumBDs, ShimNOCTile).
# A per-TILE resource shared by every channel and both directions, so the A, B
# and C legs on one column all draw from the same 16.
SHIM_BDS = 16
# Entries in a shim DMA channel's task queue. Nothing in mlir-aie models this
# -- AIEDmaToNpu's NpuPushQueueOp pushes unconditionally -- so overrunning it
# is a silent device hang, not a diagnostic. Measured here at K=10240 M=1024:
# 4 outstanding tasks on one channel run, 8 hang.
SHIM_TASK_QUEUE = 4


def _hw_stride_ok(stride_elems):
    hw_stride = (stride_elems - 1) * _BF16_BYTES // _ADDR_GRANULARITY_BYTES
    return hw_stride <= (1 << _SHIM_STEP_BITS) - 1


def _default_l1(n_tile, ct_max_k, b_elem_bytes):
    """Pick (A-tile height, L1 B depth) -- the largest working set that fits.

    ``b_elem_bytes`` is 9/8 where B is bfp16ebs8 and 2 where it is bf16, so the
    L1 budget below reflects what B actually costs on this device.

    A dies as soon as it is consumed while the accumulator lives across the
    whole K reduction, so they need not share a height; shrinking A is what
    pays for a k slice deep enough to halve the accumulator traffic per mac.
    B's depth is searched too because at n=128 the k=128 slice makes the B
    object 18 KB, and a double-buffered pair simply does not fit -- giving that
    up is what buys colA=16 there, and colA is worth far more than B's L1
    prefetch (3.67 -> 2.28 cycles per mac, measured).

    Deeper B first, then the tallest A that still fits, so the n=64 default is
    unchanged at (32, 2).
    """
    acc = M_TILE * n_tile * 4
    cout = CT_OUT_LEN * 2 * C_DEPTH
    for b_depth in (B_DEPTH, 1):
        b = int(ct_max_k * n_tile * b_elem_bytes) * b_depth
        for t_ma in (M_TILE, M_TILE // 2, M_TILE // 4):
            if t_ma < 2 * R:
                continue
            a = (2 * R * ct_max_k) * (t_ma // R // 2) * 2 * A_DEPTH
            if acc + a + b + cout <= L1_BUDGET:
                return t_ma, b_depth
    raise ValueError(f"nothing fits L1 for tile_n={n_tile}, ct_max_k={ct_max_k}")


def gemm(
    dev,
    M,
    K,
    N,
    epilogue="none",
    tile_n=N_TILE_DEFAULT,
    tile_ma=None,
    overlap=None,
    kernel_object="mm_fused.o",
    epilogue_object="mm_fused_epilogue.o",
    trace_size=0,
):
    """Emit the MLIR module for an M x K @ K x N bf16 GEMM.

    A is (M, K) row-major, B is (K, N) row-major and C is (M, N) row-major, all
    bf16 and all plain dense tensors, except that B must arrive pre-packed by
    ``GEMM.pack_B`` -- it emits B in the order the cores consume it, so both
    B hops are plain linear descriptors.
    """
    if tile_n not in CT_MAX_K_FOR_N:
        raise ValueError(
            f"tile_n must be one of {sorted(CT_MAX_K_FOR_N)}, got {tile_n}"
        )
    # Grid width, and the shim columns feeding the A broadcast, both follow the
    # device. Everything below is written against these rather than a constant,
    # so the same dataflow covers NPU2's 4x8 and NPU1's 4x4.
    COLS = grid_cols(dev)
    A_SOURCE_COL = a_source_cols(COLS)
    # r/t are the device's native mac shape; every blocked layout below is
    # expressed in terms of them.
    R, _S, T = register_tiling(dev.resolve().name)
    N_TILE = tile_n
    CT_MAX_K = CT_MAX_K_FOR_N[N_TILE]
    # B's storage format follows the device, and with it every B type and every
    # B extent below. B_GROUP is the number of B values per element of the MLIR
    # type, so a length in values becomes a length in elements by dividing.
    BFP16_B = bfp16_b_for(dev)
    B_GROUP = BFP16_GROUP if BFP16_B else 1
    b_elem_bytes = 9 / BFP16_GROUP if BFP16_B else 2
    # Asymmetric tile buffering: the A tile spans T_MA rows while the
    # accumulator spans M_TILE, so the core folds RHO bands into one C tile.
    # A is dead the moment it is consumed while C lives across the whole K
    # reduction, so sizing both to M_TILE pays the peak L1 cost twice.
    _t_ma_fit, L1_B_DEPTH = _default_l1(N_TILE, CT_MAX_K, b_elem_bytes)
    T_MA = _t_ma_fit if tile_ma is None else tile_ma
    if M_TILE % T_MA or T_MA % (2 * R):
        raise ValueError(
            f"tile_ma ({T_MA}) must divide {M_TILE} and be a multiple of {2 * R}"
        )
    RHO = M_TILE // T_MA
    OVERLAP = OVERLAP_DEFAULT if overlap is None else overlap
    K_DIV_CT_K_MAX = K_TILE // CT_MAX_K
    CT_A_LEN = 2 * R * CT_MAX_K  # one z slice
    CT_A_OBJ = CT_A_LEN * (T_MA // R // 2)  # every z slice of one mmul
    C_SLICE_LEN = M_TILE * N_TILE  # one compute tile's C contribution
    O_CHUNKS = C_SLICE_LEN // CT_OUT_LEN  # C objects an accumulator drains as
    B_ITERS = K_TILE // CT_MAX_K  # B chunks consumed per k step
    MIN_N = N_TILE * COLS

    if epilogue not in EPILOGUE_MODES:
        raise ValueError(
            f"epilogue must be one of {sorted(EPILOGUE_MODES)}, got {epilogue!r}"
        )
    # A compute tile does a whole m x n block or nothing, so M and K must tile
    # exactly. N need only be a multiple of N_TILE: a trailing group of fewer
    # than COLS blocks is handled by giving the columns different trip counts
    # (see col_work / col_drain below). That matters in practice -- for a
    # transformer the o and down projections have N = model dim, which is
    # essentially never a multiple of N_TILE*COLS.
    for name, value, unit in (("M", M, MIN_M), ("K", K, MIN_K), ("N", N, N_TILE)):
        if value % unit != 0:
            raise ValueError(f"{name} ({value}) must be a multiple of {unit}")

    bf16_ty = np.dtype[bfloat16]
    f32 = np.dtype[np.float32]

    # How many times the whole grid sweeps, in each dimension.
    m_row_blocks = M // MIN_M
    k_iters = K // K_TILE
    # A mega_row dimension with stride ROWS*M_TILE*{K,N} lands in the shim
    # BD's ITERATION field, whose step is 20 bits, so it overflows once K or N
    # crosses ~8191 elements -- E4B's FFN width (10240) does, E2B's max (6144)
    # does not. Only relevant once M walks more than one mega_row; at M=256 the
    # dimension is degenerate (size 1) and is stripped before the stride is
    # ever encoded, so it never fails there regardless of K/N.
    #
    # Fix: issue that leg as m_row_blocks separate transfers, each carrying the
    # mega_row jump in its OFFSET (unbounded) instead of a shared STRIDE. The
    # two legs are independent -- E4B's down-proj overflows on K (A only) and
    # its gate/up on N (C only) -- so neither shape pays for both.
    #
    # This was long recorded as an unfixable firmware hang. It was not. The
    # earlier attempt retired each mega_row's TaskGroup immediately, and
    # TaskGroup.finish() emits dma_free_task, which hands the buffer descriptor
    # id back to a COMPILE-TIME allocator that never checks the transfer
    # finished (mlir-aie AIEAssignRuntimeSequenceBDIDs::recycle, isAwait=false).
    # Ids are per shim TILE, shared across channels and directions, so every
    # task on a column collapsed onto bd_id 0 and reprogrammed it mid-flight --
    # including B, whose descriptor streams across every mega_row. Verify with
    # aie-opt --aie-substitute-shim-dma-allocations
    # --aie-assign-runtime-sequence-bd-ids: the ids on a shim tile must be
    # distinct, and were all 0.
    a_split = m_row_blocks > 1 and not _hw_stride_ok(ROWS * M_TILE * K)
    c_split = m_row_blocks > 1 and not _hw_stride_ok(ROWS * M_TILE * N)
    # A split leg issues one transfer per mega_row back to back on ONE channel,
    # so they must also fit that channel's task queue -- a limit nothing in the
    # toolchain models, and overrunning it hangs rather than diagnoses.
    # Measured at K=10240 M=1024: 4 outstanding run, 8 hang.
    #
    # So a split block is emitted in WINDOWS of at most SHIM_TASK_QUEUE
    # mega_rows, each window awaited before the next is issued (see sequence()).
    # Awaiting is what makes the window's descriptors safe to reuse, and it
    # bounds both resources at once. M<=1024 is a single window, so the shapes
    # that already worked are unaffected.
    MB_WINDOW = min(m_row_blocks, SHIM_TASK_QUEUE) if (a_split or c_split) else 1
    bds_per_block = 1 + (MB_WINDOW if a_split else 1) + (MB_WINDOW if c_split else 1)
    # Unreachable while SHIM_TASK_QUEUE is 4 (the worst case is 1 + 4 + 4 = 9
    # of 16), so this guards a future retune of the window rather than any
    # shape reachable today. test_flm_gemm_split_leg_windowing asserts the same
    # arithmetic from the outside.
    if bds_per_block > SHIM_BDS:
        raise ValueError(
            f"M={M} K={K} N={N} needs {bds_per_block} shim buffer descriptors "
            f"per window (1 B + {MB_WINDOW if a_split else 1} A + "
            f"{MB_WINDOW if c_split else 1} C) but a shim tile has only "
            f"{SHIM_BDS}."
        )
    # Cross-block overlap only applies to the unsplit path; a split block
    # already awaits inside itself, so keeping a second one in flight would
    # refill the very queue the windowing just drained.
    if a_split or c_split:
        OVERLAP = 1
    else:
        OVERLAP = max(1, min(OVERLAP, SHIM_BDS // bds_per_block))
    # Sweeps where all COLS columns have work, plus a trailing group of
    # rem_blocks columns (0 <= rem_blocks < COLS) that do one block more.
    n_full = N // MIN_N
    rem_blocks = (N % MIN_N) // N_TILE
    # Columns that participate at all. With no full sweep (N below the grid's
    # COLS*N_TILE stride) only the first rem_blocks columns do, and the rest
    # are not instantiated -- giving them fifos that nothing ever drains builds
    # dead dataflow, which newer mlir-aie rejects outright with
    # "objectfifo.pool op segment 0 has no drainer".
    n_active_cols = COLS if n_full else rem_blocks
    # Per column: how many column-blocks it computes, and whether it sits out a
    # trailing one while still draining the A broadcast for its row. That drain
    # only arises for a column that exists and skips the trailing block, which
    # requires at least one full sweep.
    col_work = [n_full + (1 if c < rem_blocks else 0) for c in range(n_active_cols)]
    col_drain = [
        1 if (rem_blocks and n_full and c >= rem_blocks) else 0
        for c in range(n_active_cols)
    ]

    # B's element type: one v8bfp16ebs8 per 8 values on AIE2P, one bf16 per
    # value on AIE2. Every B extent below is therefore in values // B_GROUP.
    b_elem_ty = np.dtype[v8bfp16ebs8] if BFP16_B else bf16_ty
    # L1 (per compute tile)
    ct_a_obj_ty = np.ndarray[(CT_A_OBJ,), bf16_ty]
    ct_b_ty = np.ndarray[(CT_MAX_K * N_TILE // B_GROUP,), b_elem_ty]
    ct_out_ty = np.ndarray[(CT_OUT_LEN,), bf16_ty]
    ct_acc_ty = np.ndarray[(M_TILE * N_TILE,), f32]
    # L2 (per memtile)
    mt_a_ty = np.ndarray[(M_TILE * K_TILE,), bf16_ty]
    mt_a_bytes = M_TILE * K_TILE * 2
    mt_b_ty = np.ndarray[(K_TILE * N_TILE // B_GROUP,), b_elem_ty]
    mt_b_bytes = _b_bytes(K_TILE * N_TILE, BFP16_B)
    mt_out_ty = np.ndarray[(C_SLICE_LEN * ROWS,), bf16_ty]
    mt_out_bytes = C_SLICE_LEN * ROWS * 2
    # L3 (DDR), flat -- the taps below index them linearly.
    a_l3_ty = np.ndarray[(M * K,), bf16_ty]
    b_l3_ty = np.ndarray[(K * N // B_GROUP,), b_elem_ty]
    c_l3_ty = np.ndarray[(M * N,), bf16_ty]

    acc_init = Kernel("mm_fused_acc_init", kernel_object, [ct_acc_ty])
    # The trailing int32 is the A band index: under asymmetric tile buffering
    # the core folds RHO A bands into one accumulator, so the kernel needs to
    # know which band it is writing.
    k_step = Kernel(
        "mm_fused_k_step",
        kernel_object,
        [ct_a_obj_ty, ct_b_ty, ct_acc_ty, np.int32],
    )
    epilogue_chunk = Kernel(
        EPILOGUE_SYMBOL,
        epilogue_object,
        [ct_out_ty, ct_acc_ty, np.int32, np.int32],
    )

    # --- Data movement ----------------------------------------------------
    #
    # These stream-dimension lists are the load-bearing part of the design:
    # they are what turns a row-major DDR tile into the r x s / s x t blocked
    # layout the mmul indexes, and they are tightly coupled to it. A mismatch
    # here produces silently wrong results, not a build error.

    def _split_run(run):
        # A BD wrap may not exceed 1023; the run is contiguous, so a longer one
        # re-encodes as two dimensions at the cost of one of the four.
        return [(run, 1)] if run <= 1023 else [(2, run // 2), (run // 2, 1)]

    # C: de-block each core's r x t tiled output back into row-major within its
    # 64x128 slice, on the way into the memtile.
    gather_dims = [(M_TILE // R, R * N_TILE), (N_TILE // T, T), (R, N_TILE), (T, 1)]
    # B: DDR row-major (k x n) -> s x t blocks (recv), then split into the
    # CT_MAX_K-deep chunks a single mmul call consumes (send).
    # B needs no reblocking on either hop: pack_B already emits it in the
    # order the cores consume, so the memtile just streams it through. That
    # frees every descriptor dimension B used to spend -- which is what lets
    # CT_MAX_K reach 128 (the innermost run would otherwise overflow the BD's
    # 10-bit size field and need a split dimension) at the same time as
    # residency (which spends one on its outer k walk).
    b_recv_dims = None
    b_send_dims = None
    # A: same idea, r x s blocks.
    a_recv_dims = [(M_TILE // R, R * K_TILE), (R, S), (K_TILE // S, R * S), (S, 1)]
    a_send_dims = [
        (K_DIV_CT_K_MAX, R * CT_MAX_K),
        (M_TILE // R, R * K_TILE),
    ] + _split_run(R * CT_MAX_K)

    # C: one join per column. Each of the ROWS cores in the column drops its
    # slice at its own offset in a single memtile buffer, which then drains to
    # DDR as one contiguous (ROWS*M_TILE) x N_TILE block.
    c_l2l3_fifos = []
    c_prod = {}
    for c in range(n_active_cols):
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
        # One cons() handle per active column; every tile in the row sees
        # this object, so inactive columns must not be consumers at all.
        for c in range(n_active_cols):
            a_cons[(r, c)] = of_a.cons()

    # B: shim -> memtile -> broadcast down the compute column.
    #
    # Where it fits, a whole column-block's B is held in the memtile as ONE
    # object and re-walked per row-block, so DDR reads it once instead of
    # m_row_blocks times. B is the dominant DDR leg, so that is roughly 43% less
    # total traffic; the latency it buys grows with M, because B's re-reads
    # scale with m_row_blocks. Larger K does not fit and falls back to
    # re-reading. See README.md for the measured effect.
    #
    # Three things here are load-bearing rather than tuning:
    #
    #   * ONE object spanning every k-block, not a pool of k_iters objects.
    #     Iterating a pool replays each object in turn (k0,k0,k1,k1,...) rather
    #     than the k0..kn sequence the cores accumulate in.
    #   * repeat_count on the forward() below is what re-sends an object.
    #     iter_count only bounds how many times an end cycles through all its
    #     buffers, so it is in units of depth-cycles; getting it wrong hangs
    #     rather than mis-computing.
    #   * The depth search takes the deepest that fits, not depth 1. Single
    #     buffering stops the next column-block prefetching behind this one's
    #     replay, which measures worse than not being resident at all.
    #
    # The budget must count what A and C actually occupy: at tile_n=128 C
    # doubles and a resident B is 432 KB, and a budget that assumed C's size
    # admitted a configuration that then failed address assignment. Placement
    # has zero slack -- the eight memtiles pack to exactly 512 KB, relying on
    # aie-objectfifo-allocate spilling one buffer to an adjacent tile -- so
    # re-verify it after any change to the A, B or C buffer sizes.
    mt_free = 512 * 1024 - mt_a_bytes * A_DEPTH - mt_out_bytes * C_DEPTH
    MT_B_DEPTH = next(
        (d for d in (B_DEPTH, 1) if k_iters * mt_b_bytes * d <= mt_free), 0
    )
    b_resident = MT_B_DEPTH > 0
    if b_resident:
        # Just a bigger buffer. With B packed in consumption order the walk is
        # linear, so spanning every k-block needs no extra descriptor
        # dimension -- the objects simply come out in k order. (The previous
        # blocked layout had to widen one dim inbound and add an outermost k
        # dim outbound, which is what collided with CT_MAX_K=128.)
        mt_b_ty = np.ndarray[(k_iters * K_TILE * N_TILE // B_GROUP,), b_elem_ty]

    b_l3l2_fifos = []
    b_cons = {}
    for c in range(n_active_cols):
        of_b_in = ObjectFifo(
            mt_b_ty, name=f"B_L3L2_{c}", depth=MT_B_DEPTH if b_resident else B_DEPTH
        )
        b_l3l2_fifos.append(of_b_in)
        of_b = of_b_in.cons(dims_from_stream=b_recv_dims).forward(
            tile=Tile(c, 1),
            obj_type=ct_b_ty,
            depth=L1_B_DEPTH,
            name=f"B_L2L1_{c}",
            dims_to_stream=b_send_dims,
            # Replay the resident memtile object once per row-block. This is
            # the mechanism that actually re-sends an object; iter_count only
            # bounds how many chain iterations happen in total. Correct
            # ordering depends on the memtile holding ONE object spanning every
            # k-block: replicating a pool of k_iters smaller objects would
            # emit k0,k0,k1,k1,... rather than the k0..kn sequence the cores
            # accumulate in.
            repeat_count=m_row_blocks if b_resident else None,
        )
        for r in range(ROWS):
            b_cons[(r, c)] = of_b.cons()

    # --- Compute ----------------------------------------------------------
    def make_core_fn(n_work, n_drain):
        """Core body for a column that computes ``n_work`` column-blocks and
        then drains A for ``n_drain`` more (0 or 1)."""

        def core_fn(acc, o_h, b_h, a_h, init_k, kstep_k, epi_k):
            # The loop nest lives here rather than inside the kernel so that
            # every level has an ObjectFifo acquire point. With M/K/N known at
            # compile time all the trip counts are constants.
            if n_work:
                for _ in range_(n_work):
                    for _ in range_(m_row_blocks):
                        init_k(acc)
                        for _ in range_(k_iters):
                            # The l loop is unrolled by the B fifo depth so the
                            # acquired buffer index stays a compile-time
                            # constant.
                            for _ in range_(B_ITERS // B_DEPTH):
                                for _ in range(B_DEPTH):
                                    # One B chunk feeds every A band, so B is
                                    # acquired once around the band loop.
                                    b = b_h.acquire(1)
                                    for band in range(RHO):
                                        a = a_h.acquire(1)
                                        kstep_k(a, b, acc, band)
                                        a_h.release(1)
                                    b_h.release(1)
                        # Drain the accumulator. Unrolled by C_DEPTH for the
                        # same reason; a full O_CHUNKS unroll overflows program
                        # memory.
                        for chunk in range_(O_CHUNKS // C_DEPTH):
                            for half in range(C_DEPTH):
                                o = o_h.acquire(1)
                                epi_k(o, acc, chunk, half)
                                o_h.release(1)
            if n_drain:
                # The trailing partial column-block, for a column that sits it
                # out. A is broadcast along the whole compute row, so this
                # column must still consume its share or the columns that DO
                # have work stall waiting for the fifo to advance. No B and no
                # C here -- the runtime sequence issues neither for it.
                for _ in range_(n_drain):
                    for _ in range_(m_row_blocks):
                        for _ in range_(k_iters):
                            for _ in range_(B_ITERS // B_DEPTH):
                                for _ in range(B_DEPTH):
                                    for _ in range(RHO):
                                        a_h.acquire(1)
                                        a_h.release(1)

        return core_fn

    workers = []
    for r in range(ROWS):
        for c in range(n_active_cols):
            tile = Tile(c, r + 2)
            acc = Buffer(tile=tile, type=ct_acc_ty, name=f"c_acc_{r}_{c}")
            workers.append(
                Worker(
                    make_core_fn(col_work[c], col_drain[c]),
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
    # One transfer per (column-block, leg) instead of one per object.
    #
    # A single fill/drain may span MANY fifo objects -- the descriptor just
    # walks them in the order the cores consume -- so a whole column-block's
    # worth of A, B and C each go out as one task. Issuing per object instead
    # meant a host-side await for every sweep, and those awaits were the
    # serialisation: the next sweep could not start until the previous sweep's
    # C had come all the way back.
    #
    # Dimension order must match the core loop nest exactly: for each
    # column-block it walks mega_row, then k. Every wrap stays under the shim's
    # 10-bit size field (largest are K_TILE=512 and ROWS*M_TILE=256).
    def a_taps(mega_col, r, mbs):
        # Every (mega_row, k) block this compute row consumes for one
        # column-block. A does not depend on mega_col; it is re-fetched per
        # column-block because the cores re-consume it.
        #
        # Returns a LIST: one 4D descriptor normally, or one 3D descriptor per
        # mega_row when the mega_row stride would overflow the shim BD's 20-bit
        # iteration step (see a_split above). The split form carries the
        # mega_row jump in the offset, which has no such limit.
        if not a_split:
            return [
                TensorAccessPattern(
                    tensor_dims=(M * K,),
                    offset=r * M_TILE * K,
                    sizes=[m_row_blocks, k_iters, M_TILE, K_TILE],
                    strides=[ROWS * M_TILE * K, K_TILE, K, 1],
                )
            ]
        return [
            TensorAccessPattern(
                tensor_dims=(M * K,),
                offset=mb * ROWS * M_TILE * K + r * M_TILE * K,
                sizes=[1, k_iters, M_TILE, K_TILE],
                strides=[0, K_TILE, K, 1],
            )
            for mb in mbs
        ]

    def b_tap(mega_col, c):
        # Every (mega_row, k) chunk this column consumes. B does not depend on
        # mega_row, hence the 0 stride: the same k-blocks are replayed for each
        # row-block, which is what the cores expect.
        #
        # B must arrive PRE-PACKED (see GEMM.pack_B) so each k-block is one
        # contiguous run. Expressing that reorder in the descriptor instead
        # gives an innermost run of T=8 bf16, turning each 128 KB transfer into
        # 8192 scattered bursts -- measured 5.4x slower end to end.
        return TensorAccessPattern(
            tensor_dims=(K * N // B_GROUP,),
            offset=(mega_col * COLS + c) * N_TILE * K // B_GROUP,
            sizes=(
                [1, 1, 1, k_iters * K_TILE * N_TILE // B_GROUP]
                if b_resident
                else [m_row_blocks, k_iters, 1, K_TILE * N_TILE // B_GROUP]
            ),
            strides=(
                [0, 0, 0, 1] if b_resident else [0, K_TILE * N_TILE // B_GROUP, 0, 1]
            ),
        )

    def c_taps(mega_col, c, mbs):
        # Every joined block this column produces for one column-block: one
        # ROWS*M_TILE x N_TILE block per row-block. Returns a LIST, for the
        # same reason a_taps does -- one descriptor per mega_row when N makes
        # the mega_row stride overflow the shim BD's iteration step.
        if c_split:
            return [
                TensorAccessPattern(
                    tensor_dims=(M * N,),
                    offset=(mega_col * COLS + c) * N_TILE + mb * ROWS * M_TILE * N,
                    sizes=[1, 1, ROWS * M_TILE, N_TILE],
                    strides=[0, 0, N, 1],
                )
                for mb in mbs
            ]
        return [_c_tap_unsplit(mega_col, c)]

    def _c_tap_unsplit(mega_col, c):
        return TensorAccessPattern(
            tensor_dims=(M * N,),
            offset=(mega_col * COLS + c) * N_TILE,
            sizes=[1, m_row_blocks, ROWS * M_TILE, N_TILE],
            strides=[0, ROWS * M_TILE * N, N, 1],
        )

    def sequence(A, B, C, a_prods, b_prods, c_conses):
        # Column-blocks 0..n_full-1 use every column; the trailing one (when N
        # is not a multiple of N_TILE*COLS) uses only the first rem_blocks. A
        # is always issued for every row, because the columns sitting the
        # trailing block out still drain their share of the broadcast.
        blocks = [(mc, COLS) for mc in range(n_full)]
        if rem_blocks:
            blocks.append((n_full, rem_blocks))

        # One task per (column-block, leg): three per column instead of one per
        # object, so a whole column-block retires on a single await rather than
        # one per row-block. The C drain is issued first and retired last -- it
        # is an S2MM that simply waits for the cores, so keeping it outstanding
        # is what overlaps compute with write-back, and it must not share a
        # group with the fills it depends on.
        # Depth-2: issue column-block i+1 before retiring i, so its transfers
        # are already moving while i computes. Retiring a block before issuing
        # the next serialises on the C await, which waits for the cores.
        #
        # This is affordable only because each leg is a single task per
        # column-block. Per-object tasks needed 1 + 2*k_iters and could not be
        # overlapped at all.
        # Keep OVERLAP column-blocks in flight, against 16 shim buffer
        # descriptors per column; the operator is DDR-rate bound rather than
        # byte bound (53 GB/s of a 63-70 GB/s roof), so how deeply the fills
        # are pipelined is what decides the rate.
        #
        # Every task of a block stays LIVE in its TaskGroup until the block is
        # retired here. That is load-bearing, not tidiness: finish() emits
        # dma_free_task, which returns the buffer descriptor id to a
        # compile-time allocator that does not check the transfer completed, so
        # retiring a leg early lets the next task reprogram a live descriptor.
        # See the a_split comment above for what that cost.
        all_mb = list(range(m_row_blocks))

        def emit_unsplit():
            pending = []
            for mega_col, active_cols in blocks:
                tg_c = TaskGroup()
                for c in range(active_cols):
                    for tap in c_taps(mega_col, c, all_mb):
                        c_conses[c].drain(C, tap, group=tg_c, wait=True)
                tg_f = TaskGroup()
                for r in range(ROWS):
                    for tap in a_taps(mega_col, r, all_mb):
                        a_prods[r].fill(A, tap, group=tg_f)
                for c in range(active_cols):
                    b_prods[c].fill(B, b_tap(mega_col, c), group=tg_f)

                pending.append([tg_f, tg_c])
                while len(pending) >= OVERLAP:
                    for tg in pending.pop(0):
                        tg.finish()

            for group in pending:
                for tg in group:
                    tg.finish()

        def emit_split():
            # A split leg is one transfer per mega_row, so a whole block at
            # once would overrun the shim channel's task queue. Emit MB_WINDOW
            # mega_rows at a time and retire each window before the next, which
            # both drains the queue and -- because the window's transfers are
            # awaited, not merely freed -- makes its descriptors safe to reuse.
            #
            # B stays live across the whole block: its descriptor replays over
            # every mega_row, so freeing it per window would hand its
            # descriptor away mid-flight. It is retired last, after every
            # window's C has been awaited, which is what guarantees it drained.
            for mega_col, active_cols in blocks:
                tg_b = TaskGroup()
                for c in range(active_cols):
                    b_prods[c].fill(B, b_tap(mega_col, c), group=tg_b)

                # The leg that did NOT split is still one task for the whole
                # block -- its single descriptor already spans every mega_row,
                # so re-issuing it per window would transfer the block twice.
                # It stays live alongside the windows and retires with them.
                tg_whole = TaskGroup()
                if not c_split:
                    for c in range(active_cols):
                        for tap in c_taps(mega_col, c, all_mb):
                            c_conses[c].drain(C, tap, group=tg_whole, wait=True)
                if not a_split:
                    for r in range(ROWS):
                        for tap in a_taps(mega_col, r, all_mb):
                            a_prods[r].fill(A, tap, group=tg_whole)

                for w in range(0, m_row_blocks, MB_WINDOW):
                    mbs = all_mb[w : w + MB_WINDOW]
                    tg_w = TaskGroup()
                    if c_split:
                        for c in range(active_cols):
                            for tap in c_taps(mega_col, c, mbs):
                                c_conses[c].drain(C, tap, group=tg_w, wait=True)
                    if a_split:
                        for r in range(ROWS):
                            for tap in a_taps(mega_col, r, mbs):
                                # wait=True: the await is what makes this
                                # window's descriptors reusable by the next.
                                a_prods[r].fill(A, tap, group=tg_w, wait=True)
                    tg_w.finish()

                tg_whole.finish()
                tg_b.finish()

        emit_split() if (a_split or c_split) else emit_unsplit()

    rt = Runtime(
        sequence,
        [
            a_l3_ty,
            b_l3_ty,
            c_l3_ty,
            [f.prod(tile=Tile(A_SOURCE_COL[r], 0)) for r, f in enumerate(a_l3l2_fifos)],
            [f.prod(tile=Tile(c, 0)) for c, f in enumerate(b_l3l2_fifos)],
            [f.cons(tile=Tile(c, 0)) for c, f in enumerate(c_l2l3_fifos)],
        ],
    )

    my_program = Program(dev, rt, workers=workers)
    maybe_enable_trace(my_program, trace_size, workers)
    return my_program.resolve_program()


def main():
    argparser = argparse.ArgumentParser(
        prog="FLM GEMM MLIR Design",
        description="Emits MLIR code for a row-broadcast bf16 GEMM of the given input size",
    )
    argparser.add_argument("--dev", type=str, choices=["npu1", "npu2"], default="npu2")
    argparser.add_argument("-M", type=int, default=MIN_M)
    argparser.add_argument("-K", type=int, default=MIN_K)
    argparser.add_argument("-N", type=int, default=1024)
    argparser.add_argument(
        "--tile-n",
        type=int,
        choices=sorted(CT_MAX_K_FOR_N),
        default=N_TILE_DEFAULT,
    )
    argparser.add_argument(
        "--tile-ma",
        type=int,
        default=None,
        help="Rows of A held in L1 at a time; defaults to the largest that fits",
    )
    argparser.add_argument(
        "--epilogue", type=str, choices=sorted(EPILOGUE_MODES), default="none"
    )
    argparser.add_argument("--trace_size", type=int, default=0)

    args = argparser.parse_args()
    print(
        gemm(
            NPU1() if args.dev == "npu1" else NPU2(),
            args.M,
            args.K,
            args.N,
            epilogue=args.epilogue,
            tile_n=args.tile_n,
            tile_ma=args.tile_ma,
            trace_size=args.trace_size,
        )
    )


if __name__ == "__main__":
    main()
