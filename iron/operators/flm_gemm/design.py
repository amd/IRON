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
from aie.iron.device import Tile
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
# k-slice per n width; must match compute_CT_k_max_n<N> in flm_gemm_geometry.h
CT_MAX_K_FOR_N = {16: 16, 32: 32, 64: 128, 128: 32, 256: 16}
R, S, T = 8, 8, 8
ROWS, COLS = 4, 8

# Which shim column sources the A broadcast for each compute row. Spreading
# them over alternate columns keeps four independent MM2S paths; the existing
# gemm operator pins A the same way in the 8-column case.
A_SOURCE_COL = [0, 2, 4, 6]

CT_OUT_LEN = 512  # the core's C slice, streamed out in chunks this size
C_DEPTH = 2  # C fifo depth; also the core-body unroll
B_DEPTH = 2  # B fifo depth; also the core-body unroll
A_DEPTH = 2

STACK_SIZE = 4096
# Usable L1 per compute tile: 64 KB less the stack and a little slack.
L1_BUDGET = 60 * 1024

EPILOGUE_MODES = {"none": 0, "gelu": 1, "silu": 2, "sigmoid": 3}
# The epilogue entry point, shared by the design and op.py (which needs it
# to mark the symbol alwaysinline when building the inline .ll variant).
EPILOGUE_SYMBOL = "flm_gemm_epilogue_chunk"

# Minimum problem size, i.e. one pass of the whole grid. MIN_N depends on the
# chosen n tile, so it is computed per call.
MIN_M = M_TILE * ROWS  # 256
MIN_K = K_TILE  # 512


def _default_tile_ma(n_tile, ct_max_k):
    """Largest A-tile height whose L1 working set fits.

    A is dead as soon as it is consumed while the accumulator lives across the
    whole K reduction, so they need not share a height. Shrinking A is what
    pays for a k slice deep enough to halve the accumulator traffic per mac
    (ct_max_k=128 at n=64), which measured 3.67 -> 2.64 cycles per 8x8x8 mac.
    """
    acc = M_TILE * n_tile * 4
    b = ct_max_k * n_tile * 2 * B_DEPTH
    cout = CT_OUT_LEN * 2 * C_DEPTH
    for t_ma in (M_TILE, M_TILE // 2, M_TILE // 4, M_TILE // 8):
        if t_ma < 2 * R:
            break
        a = (2 * R * ct_max_k) * (t_ma // R // 2) * 2 * A_DEPTH
        if acc + a + b + cout <= L1_BUDGET:
            return t_ma
    raise ValueError(
        f"no A-tile height fits L1 for tile_n={n_tile}, ct_max_k={ct_max_k}"
    )


def flm_gemm(
    dev,
    M,
    K,
    N,
    epilogue="none",
    tile_n=N_TILE_DEFAULT,
    tile_ma=None,
    kernel_object="flm_gemm.o",
    epilogue_object="flm_gemm_epilogue.o",
    trace_size=0,
):
    """Emit the MLIR module for an M x K @ K x N bf16 GEMM.

    A is (M, K) row-major, B is (K, N) row-major and C is (M, N) row-major, all
    bf16 and all plain dense tensors, except that B must arrive pre-packed by
    ``FLMGEMM.pack_B`` -- it emits B in the order the cores consume it, so both
    B hops are plain linear descriptors.
    """
    if tile_n not in CT_MAX_K_FOR_N:
        raise ValueError(
            f"tile_n must be one of {sorted(CT_MAX_K_FOR_N)}, got {tile_n}"
        )
    N_TILE = tile_n
    CT_MAX_K = CT_MAX_K_FOR_N[N_TILE]
    # Asymmetric tile buffering: the A tile spans T_MA rows while the
    # accumulator spans M_TILE, so the core folds RHO bands into one C tile.
    # A is dead the moment it is consumed while C lives across the whole K
    # reduction, so sizing both to M_TILE pays the peak L1 cost twice.
    T_MA = _default_tile_ma(N_TILE, CT_MAX_K) if tile_ma is None else tile_ma
    if M_TILE % T_MA or T_MA % (2 * R):
        raise ValueError(
            f"tile_ma ({T_MA}) must divide {M_TILE} and be a multiple of {2 * R}"
        )
    RHO = M_TILE // T_MA
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

    # L1 (per compute tile)
    ct_a_obj_ty = np.ndarray[(CT_A_OBJ,), bf16_ty]
    ct_b_ty = np.ndarray[(CT_MAX_K * N_TILE,), bf16_ty]
    ct_out_ty = np.ndarray[(CT_OUT_LEN,), bf16_ty]
    ct_acc_ty = np.ndarray[(M_TILE * N_TILE,), f32]
    # L2 (per memtile)
    mt_a_ty = np.ndarray[(M_TILE * K_TILE,), bf16_ty]
    mt_b_ty = np.ndarray[(K_TILE * N_TILE,), bf16_ty]
    mt_b_bytes = K_TILE * N_TILE * 2
    mt_out_ty = np.ndarray[(C_SLICE_LEN * ROWS,), bf16_ty]
    # L3 (DDR), flat -- the taps below index them linearly.
    a_l3_ty = np.ndarray[(M * K,), bf16_ty]
    b_l3_ty = np.ndarray[(K * N,), bf16_ty]
    c_l3_ty = np.ndarray[(M * N,), bf16_ty]

    acc_init = Kernel("flm_gemm_acc_init", kernel_object, [ct_acc_ty])
    k_step = Kernel(
        "flm_gemm_k_step",
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
    # Resident B: hold a whole column-block's B in the memtile as ONE object
    # and re-walk it per row-block, so DDR sees it once instead of
    # m_row_blocks times. B is the dominant DDR leg -- at M=1024 K=1536 N=6144
    # it is 75 MB of the 126 MB moved -- so this is ~43% less total traffic.
    #
    # It saves power and time both, and the time is worth more the taller the
    # problem is, because B's DDR re-reads scale with m_row_blocks. Measured at
    # K=1024 N=4096 (full builds, min of interleaved rounds):
    #
    #   M=512  (2 row-blocks)  470.8 -> 468.5 us   0.5%
    #   M=1024 (4 row-blocks)  860.4 -> 846.5 us   1.6%
    #   M=2048 (8 row-blocks) 1760.1 -> 1622.8 us  7.8%
    #
    # The operator IS DDR-bandwidth bound: with the mmul nulled out, the
    # non-resident floor at M=2048 is 1739 us for 118 MB, i.e. 68 GB/s, against
    # a measured 63-70 GB/s roof. Residency drops that floor to 1135 us.
    #
    # Note the gap between that 604 us of floor and the 137 us actually
    # captured: repeat_count restarts the memtile BD chain at every replay
    # boundary, and ~77% of the win goes there. Closing it is the largest known
    # remaining lever on this design. Do not measure it at small M -- at M=512
    # the effect is inside the noise, which is how it was first mistaken for a
    # power-only optimisation.
    #
    # One object, not k_iters of them: iterating a pool replays each object in
    # turn (k0,k0,k1,k1,...) rather than the sequence. Fitting k into the
    # descriptors within the 4-dimension limit takes both hops -- inbound the
    # outermost dim already steps by (N_TILE//T)*(K_TILE*T), exactly
    # K_TILE*N_TILE, so widening its COUNT walks into the next k-block;
    # outbound k becomes a new outermost dim, which also keeps one emitted
    # object per CT_MAX_K slice.
    #
    # Replay is repeat_count, on the forward() below. iter_count cannot do this
    # job: it only bounds how many times an end cycles through all its buffers
    # (objects = iter_count * elemNumber * repeat_count), so it is in units of
    # depth-cycles rather than objects, and getting it wrong hangs rather than
    # mis-computes.
    #
    # Gated on the buffer fitting DOUBLE-buffered, so the next column-block
    # still prefetches. B_DEPTH is load-bearing, not a safety margin:
    # single-buffering would let the lowering use the DMA's native repeat field
    # instead of a duplicated BD chain, but it also stops the next
    # column-block's B prefetching behind this one's replay, and that costs
    # more than it saves -- 1720 us against 1600 at M=2048 K=1024 N=4096,
    # i.e. worse than not being resident at all.
    #
    # The budget counts only C's 64 KB, not A's 128 KB, so it admits k_iters
    # <= 3 (K <= 1536 at tile_n=64) rather than 2. That deliberately overcommits
    # the A-carrying memtiles by 64 KB and relies on aie-objectfifo-allocate
    # spilling one buffer to the least-loaded adjacent memtile, which packs all
    # eight to exactly 512 KB (C_L2L3_6 lands on mem_tile_7_1). There is ZERO
    # slack: re-verify placement after any change to the A, B or C buffer
    # sizes, or the build will fail address assignment rather than silently
    # mis-run.
    #
    # Residency only pays once compute is off the critical path -- it was
    # measured latency-neutral while the mmul was the wall, and worth 260 us
    # immediately after the mmul loop was re-rolled. Larger K still falls back
    # to non-resident, so check this gate before believing any measurement that
    # claims to be testing residency.
    b_resident = (k_iters * mt_b_bytes * 2) <= (512 - 64) * 1024
    if b_resident:
        # Just a bigger buffer. With B packed in consumption order the walk is
        # linear, so spanning every k-block needs no extra descriptor
        # dimension -- the objects simply come out in k order. (The previous
        # blocked layout had to widen one dim inbound and add an outermost k
        # dim outbound, which is what collided with CT_MAX_K=128.)
        mt_b_ty = np.ndarray[(k_iters * K_TILE * N_TILE,), bf16_ty]

    b_l3l2_fifos = []
    b_cons = {}
    for c in range(n_active_cols):
        of_b_in = ObjectFifo(mt_b_ty, name=f"B_L3L2_{c}", depth=B_DEPTH)
        b_l3l2_fifos.append(of_b_in)
        of_b = of_b_in.cons(dims_from_stream=b_recv_dims).forward(
            tile=Tile(c, 1),
            obj_type=ct_b_ty,
            depth=B_DEPTH,
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
    def a_tap(mega_col, r):
        # Every (mega_row, k) block this compute row consumes for one
        # column-block. A does not depend on mega_col; it is re-fetched per
        # column-block because the cores re-consume it.
        return TensorAccessPattern(
            tensor_dims=(M * K,),
            offset=r * M_TILE * K,
            sizes=[m_row_blocks, k_iters, M_TILE, K_TILE],
            strides=[ROWS * M_TILE * K, K_TILE, K, 1],
        )

    def b_tap(mega_col, c):
        # Every (mega_row, k) chunk this column consumes. B does not depend on
        # mega_row, hence the 0 stride: the same k-blocks are replayed for each
        # row-block, which is what the cores expect.
        #
        # B must arrive PRE-PACKED (see FLMGEMM.pack_B) so each k-block is one
        # contiguous run. Expressing that reorder in the descriptor instead
        # gives an innermost run of T=8 bf16, turning each 128 KB transfer into
        # 8192 scattered bursts -- measured 5.4x slower end to end.
        return TensorAccessPattern(
            tensor_dims=(K * N,),
            offset=(mega_col * COLS + c) * N_TILE * K,
            sizes=(
                [1, 1, 1, k_iters * K_TILE * N_TILE]
                if b_resident
                else [m_row_blocks, k_iters, 1, K_TILE * N_TILE]
            ),
            strides=([0, 0, 0, 1] if b_resident else [0, K_TILE * N_TILE, 0, 1]),
        )

    def c_tap(mega_col, c):
        # Every joined block this column produces for one column-block: one
        # ROWS*M_TILE x N_TILE block per row-block.
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
        # This is affordable only because each leg is now a single task: a
        # block costs 3 buffer descriptors on a shim column (A + B + C), so two
        # in flight is 6 of 16. Per-object tasks needed 1 + 2*k_iters and could
        # not be overlapped at all.
        prev = None
        for mega_col, active_cols in blocks:
            tg_c = TaskGroup()
            for c in range(active_cols):
                c_conses[c].drain(C, c_tap(mega_col, c), group=tg_c, wait=True)
            tg_f = TaskGroup()
            for r in range(ROWS):
                a_prods[r].fill(A, a_tap(mega_col, r), group=tg_f)
            for c in range(active_cols):
                b_prods[c].fill(B, b_tap(mega_col, c), group=tg_f)

            if prev is not None:
                for tg in prev:
                    tg.finish()
            prev = [tg_f, tg_c]

        for tg in prev or []:
            tg.finish()

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
