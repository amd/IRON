# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""bf16 GEMM over a 4-row compute-tile grid, as wide as the device.

A second GEMM design alongside ``iron.operators.gemm``, specialised for
transformer projection shapes. Same dataflow -- A broadcast along each compute
row, B down each column, C joined through the memtile -- but with a fixed tile
shape, B quantized to bfp16ebs8 and pre-packed into consumption order, an
activation and clamp fused into the C drain, and asymmetric tile buffering so
the A tile and the accumulator need not share a height.

README.md has the per-choice breakdown against both the shipped FastFlowLM
overlay and ``iron.operators.GEMM``.

The constants below are the single source of truth: ``op.py`` passes them to
the kernels as -D flags, so the C++ and the dataflow cannot drift apart.
"""

import argparse
from enum import StrEnum
from functools import partial
from typing import NamedTuple

import numpy as np
from ml_dtypes import bfloat16

from aie.helpers.util import v8bfp16ebs8

from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    Acquire,
    Bd,
    Buffer,
    DmaChannel,
    Flow,
    Kernel,
    Lock,
    ObjectFifo,
    Program,
    Release,
    Runtime,
    TaskGroup,
    TileDma,
    Worker,
    WorkerRuntimeBarrier,
)
from aie.iron.controlflow import range_
from aie.dialects.aie import (
    EndOp,
    bds,
    dma_bd,
    get_target_model,
    next_bd,
    use_lock,
)
from aie.dialects.aiex import (
    dma_configure_task,
    dma_free_task,
    dma_start_task,
    npu_push_queue,
    set_lock,
    shim_dma_single_bd_task,
)
from aie.dialects._aie_enum_gen import AIEArch, AIETileType, DMAChannelDir, LockAction
from aie.iron.device import NPU1, NPU2, Tile
from iron.common.utils import split_run
from iron.operators._trace import maybe_enable_trace

# --- Fixed geometry -------------------------------------------------------
# GEMM tiling per compute tile, and the register tiling inside it.
M_TILE, K_TILE = 64, 512
# Default n tile. 64 doubles A fetches but gives the mmul colA=8 instead of 4,
# which wins when compute is the critical path. op.py picks per shape.
N_TILE_DEFAULT = 64
# How much of K one compute tile holds at a time, per n width. It is a fixed
# L1 budget split two ways, passed to the kernel as -DMM_FUSED_CT_K. n=256 is
# absent because its f32 accumulator alone (M_TILE*256*4) fills all of L1.
CT_MAX_K_FOR_N = {16: 16, 32: 32, 64: 128, 128: 32}
# (tile_n, ct_max_k) pairs verified on hardware. The table above looks tunable
# but is not, and a wrong value fails SILENTLY: ct_k=64 at tile_n=64 gives
# err/mass 3.45e-02 against 2.42e-04, and tile_n=128 NaNs. Cause unknown, so
# refuse rather than miscompute.
_VERIFIED_CT_K = {(16, 16), (32, 32), (64, 128), (128, 32)}
# Register tiling, shared by both architectures. pack_B, the stream-dimension
# lists and gather_dims all key off these; changing one alone is silently
# wrong. AIE2's native 4x8x4 shape measured 22-30% slower (load-port bound).
R, S, T = 8, 8, 8


def compute_rows(dev):
    """Compute-tile rows: the array less the shim row and the memtile rows."""
    tm = get_target_model(dev.resolve())
    return tm.rows() - 1 - tm.get_num_mem_tile_rows()


CT_OUT_LEN = 512  # the core's C slice, streamed out in chunks this size
C_DEPTH = 2  # C fifo depth; also the core-body unroll
B_DEPTH = 2  # B fifo depth; also the core-body unroll
A_DEPTH = 2
# L1 bytes reserved for the core's stack, which the buffer budget below must
# not hand out. The device default is 1024 and aiecc measures what a build
# actually needs: 1088 on NPU1, which is the activation LUT path plus the
# epilogue's clamp vectors, so the default fails the build outright. 2048
# leaves headroom; aiecc names the exact requirement if a change outgrows it.
STACK_SIZE = 2048
# Row-blocks a core folds into one B fetch, cutting B's DDR reads by M_CHUNK
# at the cost of that many L1 accumulators and forcing a_split. Off everywhere
# for a contractual reason: it must divide m_row_blocks (M % 512 == 0) while
# the overlay this replaces takes any multiple of 256, so a shape that cannot
# use it forks config_name. See README.md.
M_CHUNK_FOR_N = {16: 1, 32: 1, 64: 1, 128: 1}
# How many column-blocks the runtime sequence keeps in flight. A block costs 3
# shim buffer descriptors on a column (A + B + C) of the 16 available, so the
# ceiling is 5. 2 is enough to keep the fills ahead of the cores.
OVERLAP_DEFAULT = 2

# --- B's explicit memtile path ---------------------------------------------
#
# B does not go through an ObjectFifo. A fifo's memtile BDs are part of the
# device configuration, so holding a column-block there would put K (the buffer
# size) and M (the replay count) into the one xclbin every shape shares.
# Instead the memtile holds a fixed pool of k-block slots and the runtime
# sequence, which is per shape, programs both of its B channels.
#
# Channels on the memtile, core and shim. No objectfifo knows about these:
# DMAChannelAnalysis reserves channels named by a static DMA program or a shim
# allocation, not by a Flow. So they sit above anything A and C take once
# those are pinned below: C's join uses memtile S2MM 0-3 and MM2S 0, A's
# forward one more of each, and A arrives on core S2MM 0.
B_MT_S2MM, B_MT_MM2S = 5, 4
B_CT_S2MM = 1
B_SHIM_MM2S = 1
# BD ids for those two memtile channels, pinned so a per-shape sequence cannot
# collide with the static objectfifo BDs. A memtile channel can only reach the
# half of the 48 BDs matching its parity (even: 0-23, odd: 24-47) and the static
# allocator fills each half from the bottom, reaching 11 and 35 at most here.
B_MT_S2MM_BD0, B_MT_MM2S_BD0 = 40, 16
# Slots in the pool, each one k-block. Bounded by the eight pinned ids above
# and, below that, by what the memtile has left after A and C; see gemm().
B_MAX_SLOTS = 8
# The largest value a lock holds. A resident slot is released once per
# row-block unit, so this caps m_row_blocks for residency. The Python bindings
# do not expose it; AIE2 and AIE2P both have 6-bit lock values.
LOCK_MAX = 63
# Passes one memtile task may make over its chain: repeat_count is 8 bits.
MT_TASK_PASSES = 256


class _Slab(NamedTuple):
    """A run of row-block units the sequence arms B for at once; see gemm()."""

    first: int  # the first unit
    units: int
    a_split: bool
    c_split: bool
    b_resident: bool
    b_slots: int  # memtile slots walked
    b_uses: int  # units served per fill


class Epilogue(StrEnum):
    """Activation folded into the C drain.

    Declaration order is the wire format: it is both the kernel's
    ``-DMM_FUSED_EPILOGUE_MODE`` and the shipped overlay's ``output_mode``.
    """

    NONE = "none"
    GELU = "gelu"
    SILU = "silu"
    SIGMOID = "sigmoid"

    @property
    def mode(self) -> int:
        """The integer the kernel and the shipped overlay both select on."""
        return list(Epilogue).index(self)


# The parameter buffer each core reads once its barrier opens. These six are
# always present; conditional words follow at offsets rtp_layout() computes,
# so a word a build cannot use is never allocated.
#
# The clamp bounds are unconditional even though most callers do not clamp,
# because the alternative is a second xclbin: the kernel's clamp is not
# compiled out, it is neutralised by sending (-inf, +inf). Two words is the
# price of that, and a clamping caller now pays one word less than it did.
(
    RTP_N_VAL,
    RTP_M_ROW_BLOCKS,
    RTP_K_ITERS,
    RTP_EPILOGUE,
    RTP_CLAMP_MIN,
    RTP_CLAMP_MAX,
) = range(6)


def rtp_layout(m_chunk):
    """Slot index for each optional parameter, and the total word count.

    A word is not free: the sequence writes one per core, costing ~2 us of
    dispatch latency against a ~107 us floor. So optional groups are omitted
    rather than defaulted.
    """
    slots = {}
    n = 6
    if m_chunk > 1:
        slots["n_chunks"] = n
        slots["n_units"] = n + 1
        n += 2
    return slots, n


class Rounding(StrEnum):
    """Rounding for every f32->bf16 conversion.

    conv_even by default: truncation biases every conversion the same way, so
    the error accumulates over the K reduction. floor matches the overlay.
    """

    CONV_EVEN = "conv_even"
    FLOOR = "floor"


# The epilogue entry point, shared by the design and op.py (which needs it
# to mark the symbol alwaysinline when building the inline .ll variant).
EPILOGUE_SYMBOL = "mm_fused_epilogue_chunk"

# Minimum problem size in K. The minimum in M is M_TILE * compute_rows(dev) and
# in N is the chosen n tile, both of which depend on the device or the config.
MIN_K = K_TILE  # 512


# B values per element of the MLIR type, and the bytes they occupy: v8bfp16ebs8
# packs 8 values into 8 mantissa bytes plus one shared exponent. mlir-aie
# exposes no width query on the type, hence the literals.
BFP16_GROUP, BFP16_GROUP_BYTES = 8, 9


def _b_bytes(elems, bfp16_b):
    """Bytes B occupies in L1/L2. bfp16ebs8 packs 8 values as 8 mantissa bytes
    plus one shared exponent; bf16 is a plain 2 bytes each."""
    if not bfp16_b:
        return elems * 2
    assert elems % BFP16_GROUP == 0
    return elems // BFP16_GROUP * BFP16_GROUP_BYTES


# --- Shim DMA limits ------------------------------------------------------
#
# Hardware facts the Python bindings do not expose: getDmaBdStepBits and
# getDmaBdWrapSizeBits are unbound, and nothing models the channel task queue.
# gemv/design.py and repeat/design.py hardcode the same fields. An IR-level
# bf16 stride S is re-expressed as (S-1)*2 bytes / 4-byte granularity before
# AIEXDialect.cpp checks it.
_SHIM_STEP_BITS = 20
_BF16_BYTES = 2
_ADDR_GRANULARITY_BYTES = 4
# Entries in a shim DMA channel's task queue. NpuPushQueueOp pushes
# unconditionally, so overrunning this hangs silently. Measured: 4 run, 8 hang.
SHIM_TASK_QUEUE = 4
# The largest size a shim BD's outermost dimension takes; aie-opt's verifier
# enforces it, the bindings do not expose it.
SHIM_OUTER_MAX = 64


def _hw_stride_ok(stride_elems):
    hw_stride = (stride_elems - 1) * _BF16_BYTES // _ADDR_GRANULARITY_BYTES
    return hw_stride <= (1 << _SHIM_STEP_BITS) - 1


def _default_l1(n_tile, ct_max_k, b_elem_bytes, budget, m_chunk=1):
    """Pick the largest working set that fits: (A-tile height, L1 B depth).

    Deeper B first, then the tallest A that still fits, since colA is worth
    far more than B's L1 prefetch. ``budget`` is the whole local memory; the
    stack comes off it here so callers can keep passing the raw size.
    """
    budget -= STACK_SIZE
    # m_chunk accumulators, since the core holds a B chunk across that many
    # row-blocks. The only term that scales with it.
    acc = m_chunk * M_TILE * n_tile * 4
    cout = CT_OUT_LEN * 2 * C_DEPTH
    for b_depth in (B_DEPTH, 1):
        b = int(ct_max_k * n_tile * b_elem_bytes) * b_depth
        for t_ma in (M_TILE, M_TILE // 2, M_TILE // 4):
            if t_ma < 2 * R:
                continue
            a = (2 * R * ct_max_k) * (t_ma // R // 2) * 2 * A_DEPTH
            if acc + a + b + cout <= budget:
                return t_ma, b_depth
    raise ValueError(f"nothing fits L1 for tile_n={n_tile}, ct_max_k={ct_max_k}")


def _b_depth_for(t_ma, n_tile, ct_max_k, b_elem_bytes, budget, m_chunk=1):
    """Deepest B fifo depth that fits L1 alongside an explicit A-tile height.

    ``_default_l1``'s depth is chosen with its own t_ma, which need not fit a
    caller-overridden one. Raise rather than reuse a depth that does not fit.
    """
    budget -= STACK_SIZE
    # Same terms as _default_l1; acc is the only one that scales with m_chunk.
    acc = m_chunk * M_TILE * n_tile * 4
    cout = CT_OUT_LEN * 2 * C_DEPTH
    a = (2 * R * ct_max_k) * (t_ma // R // 2) * 2 * A_DEPTH
    for b_depth in (B_DEPTH, 1):
        b = int(ct_max_k * n_tile * b_elem_bytes) * b_depth
        if acc + a + b + cout <= budget:
            return b_depth
    raise ValueError(
        f"tile_ma={t_ma} does not fit L1 for tile_n={n_tile} "
        f"(ct_max_k={ct_max_k}); even single-buffered B overflows the budget"
    )


def gemm(
    dev,
    M,
    K,
    N,
    epilogue=Epilogue.NONE,
    clamp=None,
    tile_n=N_TILE_DEFAULT,
    m_chunk=None,
    tile_ma=None,
    kernel_object="mm_fused.o",
    trace_size=0,
):
    """Emit the MLIR module for an M x K @ K x N bf16 GEMM.

    A, B and C are row-major bf16 dense tensors, except that B must arrive
    pre-packed by ``GEMM.pack_B`` in the order the cores consume it.
    """
    if tile_n not in CT_MAX_K_FOR_N:
        raise ValueError(
            f"tile_n must be one of {sorted(CT_MAX_K_FOR_N)}, got {tile_n}"
        )
    # From the device, not constants, so one dataflow covers 4x8 and 4x4.
    tm = get_target_model(dev.resolve())
    COLS, ROWS = dev.cols, compute_rows(dev)
    MIN_M = M_TILE * ROWS
    SHIM_BDS = tm.get_num_bds(0, 0)
    N_TILE = tile_n
    CT_MAX_K = CT_MAX_K_FOR_N[N_TILE]
    if (N_TILE, CT_MAX_K) not in _VERIFIED_CT_K:
        raise ValueError(
            f"tile_n={N_TILE} with ct_max_k={CT_MAX_K} is not a verified "
            f"combination (verified: {sorted(_VERIFIED_CT_K)}). It would build, "
            f"run, and compute the WRONG ANSWER -- see _VERIFIED_CT_K. If you "
            f"are retuning CT_MAX_K_FOR_N, fix that coupling first and add the "
            f"pair here once a hardware test passes."
        )
    M_CHUNK = M_CHUNK_FOR_N[N_TILE] if m_chunk is None else m_chunk
    # B is bfp16ebs8 on AIE2P and bf16 on AIE2. B_GROUP is the B values per
    # element of the MLIR type, so a length in values divides to elements.
    BFP16_B = dev.arch == AIEArch.AIE2p
    B_GROUP = BFP16_GROUP if BFP16_B else 1
    b_elem_bytes = BFP16_GROUP_BYTES / BFP16_GROUP if BFP16_B else 2
    # Asymmetric tile buffering: A spans T_MA rows and the accumulator M_TILE,
    # so the core folds RHO bands into one C tile. A dies on consumption while
    # C lives across the K reduction, so sizing both to M_TILE pays twice.
    if tile_ma is None:
        T_MA, L1_B_DEPTH = _default_l1(
            N_TILE, CT_MAX_K, b_elem_bytes, tm.get_local_memory_size(), M_CHUNK
        )
    else:
        T_MA = tile_ma
        if M_TILE % T_MA or T_MA % (2 * R):
            raise ValueError(
                f"tile_ma ({T_MA}) must divide {M_TILE} and be a multiple of {2 * R}"
            )
        L1_B_DEPTH = _b_depth_for(
            T_MA,
            N_TILE,
            CT_MAX_K,
            b_elem_bytes,
            tm.get_local_memory_size(),
            M_CHUNK,
        )
    RHO = M_TILE // T_MA
    OVERLAP = OVERLAP_DEFAULT
    K_DIV_CT_K_MAX = K_TILE // CT_MAX_K
    CT_A_LEN = 2 * R * CT_MAX_K  # one z slice
    CT_A_OBJ = CT_A_LEN * (T_MA // R // 2)  # every z slice of one mmul
    C_SLICE_LEN = M_TILE * N_TILE  # one compute tile's C contribution
    O_CHUNKS = C_SLICE_LEN // CT_OUT_LEN  # C objects an accumulator drains as
    B_ITERS = K_TILE // CT_MAX_K  # B chunks consumed per k step
    MIN_N = N_TILE * COLS

    epilogue = Epilogue(epilogue)
    # Clamp bounds ride the RTP buffer as raw int32 bit patterns, since
    # npu_write_rtp writes i32 only. No clamp means the identity bounds rather
    # than a different build: min(x, +inf) and max(x, -inf) leave every finite
    # value bit-identical, so an unclamped dispatch is numerically unchanged.
    rtp_slots, rtp_words = rtp_layout(M_CHUNK)
    clamp_lo, clamp_hi = clamp if clamp is not None else (-np.inf, np.inf)
    clamp_min_bits = int(np.float32(clamp_lo).view(np.int32))
    clamp_max_bits = int(np.float32(clamp_hi).view(np.int32))
    # A tile does a whole m x n block or nothing, so M and K must tile
    # exactly. N need only be a multiple of N_TILE: a short trailing group is
    # handled by per-column trip counts, which matters because o and down
    # have N = model dim.
    for name, value, unit in (("M", M, MIN_M), ("K", K, MIN_K), ("N", N, N_TILE)):
        if value % unit != 0:
            raise ValueError(f"{name} ({value}) must be a multiple of {unit}")

    bf16_ty = np.dtype[bfloat16]
    f32 = np.dtype[np.float32]

    m_row_blocks = M // MIN_M
    k_iters = K // K_TILE
    # A "unit" is one group of M_CHUNK row-blocks. Every leg is issued per
    # unit, so A, B and C stay aligned with each other and the core's nest.
    n_chunks, n_rem = divmod(m_row_blocks, M_CHUNK)
    if n_rem:
        # op.py resolves m_chunk, so this cannot fire. A partial group is
        # inexpressible: the object is M_CHUNK tiles wide and the forward
        # always drains that much, and no way of padding it lowers correctly.
        raise ValueError(
            f"m_row_blocks ({m_row_blocks}) must be a multiple of m_chunk "
            f"({M_CHUNK}); op.py should have resolved m_chunk to 1 here"
        )
    n_units = n_chunks

    def unit_rows(u):
        """(first row-block, how many) for unit ``u``; always a full group."""
        return u * M_CHUNK, M_CHUNK

    # A mega_row stride lands in the shim BD's 20-bit iteration step, so it
    # overflows once K or N passes ~8191 elements; only E4B's 10240 does. Such
    # a leg goes out as one transfer per mega_row, carrying the jump in its
    # unbounded offset. M_CHUNK > 1 forces the same path for A. Decided per
    # slab of units (see slabs below), since a slab of one needs no stride.
    #
    # Those transfers must stay live in their TaskGroup until awaited: the
    # BD-id allocator is compile-time and does not check that a transfer
    # finished, so freeing one early lets the next task reprogram a live
    # descriptor and corrupt silently.
    def a_split_for(units):
        return units > 1 and (M_CHUNK > 1 or not _hw_stride_ok(ROWS * M_TILE * K))

    def c_split_for(units):
        return units * M_CHUNK > 1 and not _hw_stride_ok(ROWS * M_TILE * N)

    # Split legs share one channel, whose task queue is 4 deep and modelled
    # nowhere; overrunning it hangs (4 outstanding run, 8 hang). emit_split()
    # bounds it by retiring the oldest as it issues the next, which also keeps
    # the channel full -- do not simplify that to awaiting a whole batch, which
    # drains the channel at every boundary and costs up to 12.4%. The bound
    # counts transfers, not units: under c_split a unit drains M_CHUNK of them.
    #
    # Checked at the whole M: a slab splits only if the whole M would.
    a_split, c_split = a_split_for(n_units), c_split_for(n_units)
    # Live descriptors on a shim tile: SHIM_TASK_QUEUE from the rolling window,
    # plus B and the unsplit leg for each of the two blocks a boundary spans.
    bds_per_block = SHIM_TASK_QUEUE + 2 + 2
    if (a_split or c_split) and bds_per_block > SHIM_BDS:
        raise ValueError(
            f"M={M} K={K} N={N} needs {bds_per_block} shim buffer descriptors "
            f"for the split path but a shim tile has only {SHIM_BDS}."
        )
    # The unsplit path pipelines whole column-blocks instead, at 3 descriptors
    # each (A + B + C). The split path does its own bounding above and ignores
    # this.
    OVERLAP = max(1, min(OVERLAP, SHIM_BDS // 3))
    # Sweeps where all COLS columns have work, plus a trailing group of
    # rem_blocks columns (0 <= rem_blocks < COLS) that do one block more.
    n_full = N // MIN_N
    rem_blocks = (N % MIN_N) // N_TILE
    # Every column is instantiated for every shape. Which columns exist is
    # configuration, and this design has only one. A column with no work for
    # the current shape gets n_work = 0 and drains instead.
    n_active_cols = COLS
    # B's element type: one v8bfp16ebs8 per 8 values on AIE2P, one bf16 per
    # value on AIE2. Every B extent below is therefore in values // B_GROUP.
    b_elem_ty = np.dtype[v8bfp16ebs8] if BFP16_B else bf16_ty
    # L1 (per compute tile)
    ct_a_obj_ty = np.ndarray[(CT_A_OBJ,), bf16_ty]
    ct_b_ty = np.ndarray[(CT_MAX_K * N_TILE // B_GROUP,), b_elem_ty]
    ct_out_ty = np.ndarray[(CT_OUT_LEN,), bf16_ty]
    ct_acc_ty = np.ndarray[(M_TILE * N_TILE,), f32]
    # L2 (per memtile). M_CHUNK stacked row-block tiles, so the forward below
    # can interleave them on the way out; see a_send_dims.
    mt_a_ty = np.ndarray[(M_CHUNK * M_TILE * K_TILE,), bf16_ty]
    mt_out_ty = np.ndarray[(C_SLICE_LEN * ROWS,), bf16_ty]
    # L3 (DDR), flat; the taps below index them linearly.
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
    # Same object as the mmul: the epilogue is compiled into mm_fused.cc, so
    # one -D flag set and one artifact cover both.
    epilogue_chunk = Kernel(
        EPILOGUE_SYMBOL,
        kernel_object,
        # outer, half, mode, clamp_min_bits, clamp_max_bits
        [ct_out_ty, ct_acc_ty] + [np.int32] * 5,
    )

    # --- Data movement ----------------------------------------------------
    #
    # These turn a row-major DDR tile into the blocked layout the mmul
    # indexes. A mismatch is silently wrong, not a build error.

    # C: de-block each core's r x t tiled output back into row-major within its
    # 64x128 slice, on the way into the memtile.
    gather_dims = [(M_TILE // R, R * N_TILE), (N_TILE // T, T), (R, N_TILE), (T, 1)]
    # B needs no reblocking on either hop: pack_B emits it in consume order.
    # That frees the descriptor dimensions that let CT_MAX_K reach 128.
    # A: same idea, r x s blocks. The outermost row-group dimension spans
    # M_CHUNK tiles. mc's stride is exactly this dimension's size*stride, so
    # the two merge and the walk stays within the memtile BD's four dims.
    a_recv_dims = [
        (M_CHUNK * M_TILE // R, R * K_TILE),
        (R, S),
        (K_TILE // S, R * S),
        (S, 1),
    ]
    # Emits (b_iter, mc, band): the order the core acquires A in while holding
    # a B chunk across the group.
    a_send_dims = [
        (K_DIV_CT_K_MAX, R * CT_MAX_K),
        (M_CHUNK * M_TILE // R, R * K_TILE),
    ] + split_run(R * CT_MAX_K)

    # Every tile is pinned. B's explicit path names its memtile and core
    # channels (B_MT_*, B_CT_S2MM), which only stays clear of A and C if the
    # placer cannot stack them differently: one C join per memtile, one A
    # forward on every (COLS // ROWS)-th, and each core at its grid position.
    # Typed up front: Flow reads tile_type to find its shim end, and nothing
    # else stamps these.
    shim_tiles = [
        Tile(c, 0, tile_type=AIETileType.ShimNOCTile) for c in range(n_active_cols)
    ]
    mt_tiles = [Tile(c, 1, tile_type=AIETileType.MemTile) for c in range(n_active_cols)]
    ct_tiles = [
        [Tile(c, 2 + r, tile_type=AIETileType.CoreTile) for c in range(n_active_cols)]
        for r in range(ROWS)
    ]

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
            tile=mt_tiles[c],
            obj_types=[ct_out_ty] * ROWS,
            names=[f"C_L1L2_{c}_{r}" for r in range(ROWS)],
            dims_from_stream=[gather_dims] * ROWS,
        )
        for r in range(ROWS):
            c_prod[(r, c)] = sub[r]

    # A: shim -> memtile -> broadcast along the compute row, reblocking on
    # the forward(). One fifo per row even at M_CHUNK > 1: a second would
    # want a third core input DMA channel, and a tile has two.
    a_l3l2_fifos = []
    a_cons = {}
    for r in range(ROWS):
        of_a_in = ObjectFifo(mt_a_ty, name=f"A_L3L2_{r}", depth=A_DEPTH)
        a_l3l2_fifos.append(of_a_in)
        of_a = of_a_in.cons(dims_from_stream=a_recv_dims).forward(
            tile=mt_tiles[r * n_active_cols // ROWS],
            obj_type=ct_a_obj_ty,
            depth=A_DEPTH,
            name=f"A_L2L1_{r}",
            dims_to_stream=a_send_dims,
        )
        # Every tile in the row sees this object, so inactive columns must
        # not be consumers at all.
        for c in range(n_active_cols):
            a_cons[(r, c)] = of_a.cons()

    # B: shim -> memtile slot pool -> broadcast down the compute column, over
    # explicit flows, buffers and locks; see B_MT_S2MM. Everything declared
    # here is shape-independent, so it can live in the shared xclbin. What
    # varies per shape -- how the slots are filled and replayed -- is BD
    # programming in the runtime sequence below.
    #
    # The pool takes what the memtile has left once A and C are placed, capped
    # by the pinned BD ids. Budgeted as if every memtile held an A forward,
    # though only every (COLS // ROWS)-th does, so a slot count is the same on
    # every column.
    b_slot_elems = K_TILE * N_TILE // B_GROUP
    b_slot_bytes = _b_bytes(K_TILE * N_TILE, BFP16_B)
    mt_free = (
        tm.get_mem_tile_size()
        - A_DEPTH * M_CHUNK * M_TILE * K_TILE * 2
        - C_DEPTH * C_SLICE_LEN * ROWS * 2
    )
    B_SLOTS = min(B_MAX_SLOTS, mt_free // b_slot_bytes)
    if B_SLOTS < 1:
        raise ValueError(
            f"no room for a {b_slot_bytes}-byte B slot in the memtile at "
            f"tile_n={N_TILE}; {mt_free} bytes remain after A and C"
        )
    b_mt_ty = np.ndarray[(B_SLOTS * b_slot_elems,), b_elem_ty]
    b_mt_bufs = []
    # One lock pair per slot, not per pool: a resident slot is consumed once
    # per unit and refilled only when all of them have, independently of the
    # other slots, so the next column-block's refill trails the replay by one
    # slot instead of waiting for the whole block.
    b_mt_prod = []
    b_mt_cons = []
    for c in range(n_active_cols):
        b_mt_bufs.append(Buffer(b_mt_ty, name=f"b_mt_{c}", tile=mt_tiles[c]))
        b_mt_prod.append(
            [
                Lock(mt_tiles[c], init=0, name=f"b_mt_prod_{c}_{i}")
                for i in range(B_SLOTS)
            ]
        )
        b_mt_cons.append(
            [
                Lock(mt_tiles[c], init=0, name=f"b_mt_cons_{c}_{i}")
                for i in range(B_SLOTS)
            ]
        )
    b_flows = []
    for c in range(n_active_cols):
        b_flows.append(
            Flow(
                shim_tiles[c],
                mt_tiles[c],
                src_channel=B_SHIM_MM2S,
                dst_channel=B_MT_S2MM,
                shim_symbol=f"B_L3L2_{c}",
            )
        )
        # One source, ROWS destinations: a circuit-switched broadcast.
        for r in range(ROWS):
            b_flows.append(
                Flow(
                    mt_tiles[c],
                    ct_tiles[r][c],
                    src_channel=B_MT_MM2S,
                    dst_channel=B_CT_S2MM,
                )
            )

    # The cores' end is static: a ring of L1_B_DEPTH buffers any shape uses the
    # same way, filled by a looping BD chain and consumed under the same
    # prod/cons lock pair an ObjectFifo would have generated.
    b_l1 = {}
    b_l1_dmas = []
    for r in range(ROWS):
        for c in range(n_active_cols):
            tile = ct_tiles[r][c]
            bufs = [
                Buffer(ct_b_ty, name=f"b_l1_{r}_{c}_{d}", tile=tile)
                for d in range(L1_B_DEPTH)
            ]
            prod = Lock(tile, init=L1_B_DEPTH, name=f"b_l1_prod_{r}_{c}")
            cons = Lock(tile, init=0, name=f"b_l1_cons_{r}_{c}")
            b_l1[(r, c)] = (bufs, prod, cons)
            b_l1_dmas.append(
                TileDma(
                    tile,
                    [
                        DmaChannel(
                            DMAChannelDir.S2MM,
                            B_CT_S2MM,
                            [
                                Bd(
                                    buf,
                                    acquires=[Acquire(prod)],
                                    releases=[Release(cons)],
                                    next=(d + 1) % L1_B_DEPTH,
                                )
                                for d, buf in enumerate(bufs)
                            ],
                        )
                    ],
                )
            )

    # Data, not an immediate folded into the program: the core programs differ
    # only in symbol names, and baking this in as code would foreclose a
    # one-program xclbin. Written once, so it costs nothing per dispatch.
    my_cols = [
        [
            Buffer(
                np.ndarray[(1,), np.dtype[np.int32]],
                name=f"my_col_{r}_{c}",
                initial_value=np.array([c], dtype=np.int32),
            )
            for c in range(n_active_cols)
        ]
        for r in range(ROWS)
    ]

    # --- Runtime parameters -----------------------------------------------
    rtps = [
        [
            Buffer(
                np.ndarray[(rtp_words,), np.dtype[np.int32]],
                name=f"rtp_{r}_{c}",
                initial_value=np.zeros(rtp_words, dtype=np.int32),
                use_write_rtp=True,
            )
            for c in range(n_active_cols)
        ]
        for r in range(ROWS)
    ]
    barriers = [
        [WorkerRuntimeBarrier() for _ in range(n_active_cols)] for _ in range(ROWS)
    ]

    # --- Compute ----------------------------------------------------------
    def core_fn(
        accs,
        o_h,
        b_bufs,
        b_prod,
        b_cons,
        a_h,
        init_k,
        kstep_k,
        epi_k,
        my_rtp,
        my_col,
        barrier,
        _placed,
    ):
        """Core body. Every trip count and the activation come from the
        runtime parameter buffer, so one core program serves every shape.

        ``_placed`` is unused: it carries objects that no core touches but that
        must be resolved, which only a Worker's arguments guarantee.
        """
        # The nest is here, not in the kernel, so every level has an acquire.
        barrier.wait_for_value(1)
        # Derived rather than sent, saving an RTP word: column c has work in
        # block j iff (j*COLS + c)*N_TILE < N. Both divisors are powers of two,
        # so this must leave no __divsi3 -- check the .o, not the .ll. Use //
        # rather than >>; ScalarValue has no shift operators.
        n_tiles = my_rtp[RTP_N_VAL] // N_TILE
        n_work = (n_tiles - my_col[0] + COLS - 1) // COLS
        n_drain = ((n_tiles + COLS - 1) // COLS) - n_work
        n_row_blocks = my_rtp[RTP_M_ROW_BLOCKS]
        n_k_iters = my_rtp[RTP_K_ITERS]
        epi_mode = my_rtp[RTP_EPILOGUE]
        clamp_min_bits = my_rtp[RTP_CLAMP_MIN]
        clamp_max_bits = my_rtp[RTP_CLAMP_MAX]
        # An absent slot becomes a compile-time constant rather than a load: at
        # M_CHUNK == 1 both chunk counts are just n_row_blocks.
        if "n_chunks" in rtp_slots:
            n_chunks = my_rtp[rtp_slots["n_chunks"]]
            n_units_rt = my_rtp[rtp_slots["n_units"]]
        else:
            n_chunks = n_row_blocks
            n_units_rt = n_row_blocks
        # Acquire does not consume the barrier, so take it back to zero or the
        # next dispatch re-reads these instead of waiting. Safe before the
        # work: the sequence cannot re-set it until this dispatch's C drains.
        barrier.release_with_value(1)

        def sweep(group):
            """One k reduction feeding ``group`` accumulators off a shared B.

            ``group`` is a Python list, so the mc loops unroll. B is acquired
            outside them, so DDR reads B once per len(group) row-blocks.
            """
            for a_acc in group:
                init_k(a_acc)
            for _ in range_(n_k_iters):
                # Unrolled by the ring depth, so each buffer is a fixed symbol.
                # The DMA's ring and this walk stay in step because a k step
                # consumes B_ITERS chunks, which the depth divides.
                for _ in range_(B_ITERS // L1_B_DEPTH):
                    for b in b_bufs:
                        b_cons.acquire(1)
                        for a_acc in group:
                            for band in range(RHO):
                                a = a_h.acquire(1)
                                kstep_k(a, b, a_acc, band)
                                a_h.release(1)
                        b_prod.release(1)
            # Unrolled by C_DEPTH; a full O_CHUNKS unroll overflows program
            # memory.
            for a_acc in group:
                for chunk in range_(O_CHUNKS // C_DEPTH):
                    for half in range(C_DEPTH):
                        o = o_h.acquire(1)
                        epi_k(
                            o,
                            a_acc,
                            chunk,
                            half,
                            epi_mode,
                            clamp_min_bits,
                            clamp_max_bits,
                        )
                        o_h.release(1)

        for _ in range_(n_work):
            for _ in range_(n_chunks):
                sweep(accs)

        # Column-blocks this column sits out. A is broadcast along the row, so
        # it must still consume its share or the columns that do have work will
        # stall on the fifo. No B and no C; the sequence issues neither.
        for _ in range_(n_drain):
            # Every unit delivers a full M_CHUNK tiles of A, leftover or not,
            # so an idle column drains that much per unit.
            for _ in range_(n_units_rt):
                for _ in range_(n_k_iters):
                    for _ in range_(B_ITERS // L1_B_DEPTH):
                        for _ in range(L1_B_DEPTH):
                            for _ in range(M_CHUNK * RHO):
                                a_h.acquire(1)
                                a_h.release(1)

    workers = []
    for r in range(ROWS):
        for c in range(n_active_cols):
            # Worker flattens nested fn_args, so the length stays
            # compile-time in core_fn.
            accs = [
                Buffer(type=ct_acc_ty, name=f"c_acc_{r}_{c}_{mc}")
                for mc in range(M_CHUNK)
            ]
            b_bufs, b_prod, b_cons = b_l1[(r, c)]
            workers.append(
                Worker(
                    core_fn,
                    [
                        accs,
                        c_prod[(r, c)].prod(),
                        b_bufs,
                        b_prod,
                        b_cons,
                        a_cons[(r, c)],
                        acc_init,
                        k_step,
                        epilogue_chunk,
                        rtps[r][c],
                        my_cols[r][c],
                        barriers[r][c],
                        # The column's memtile pool, which only DMAs touch.
                        [b_mt_bufs[c]] if r == 0 else [],
                    ],
                    tile=ct_tiles[r][c],
                    stack_size=STACK_SIZE,
                )
            )

    # --- Runtime ----------------------------------------------------------
    #
    # One transfer per (column-block, leg), not one per object: a descriptor
    # walks many fifo objects in consume order, and per-object issue meant a
    # host await per sweep. Dimension order must match the core's nest.
    def a_taps(mega_col, r, units, slab):
        # Every (row-block, k) block this row consumes for one column-block,
        # k outermost. A does not depend on mega_col; it is re-fetched because
        # the cores re-consume it.
        if M_CHUNK == 1 and not slab.a_split:
            return [
                TensorAccessPattern(
                    tensor_dims=(M * K,),
                    offset=slab.first * ROWS * M_TILE * K + r * M_TILE * K,
                    sizes=[slab.units, k_iters, M_TILE, K_TILE],
                    strides=[ROWS * M_TILE * K, K_TILE, K, 1],
                )
            ]
        taps = []
        for u in units:
            first, count = unit_rows(u)
            taps.append(
                TensorAccessPattern(
                    tensor_dims=(M * K,),
                    offset=first * ROWS * M_TILE * K + r * M_TILE * K,
                    sizes=[k_iters, M_CHUNK, M_TILE, K_TILE],
                    strides=[K_TILE, ROWS * M_TILE * K, K, 1],
                )
            )
        return taps

    # B's slot pool, per shape. Resident where the column-block fits: DDR
    # reads it once and the memtile replays it n_units times. Otherwise the
    # pool is a plain ring and DDR re-reads B per unit, as a fifo would.
    #
    # Each slot is filled when its producer lock reaches b_uses and released
    # by b_uses per fill, then drained once per use. So a resident slot is not
    # refilled until every unit has read it, while a streamed one turns over
    # like a fifo object. Both return the producer lock to b_uses by the end of
    # the slab, which the sequence re-arms per slab since the previous one may
    # have been a different shape.
    def make_slab(first, units):
        """The plan for ``units`` units from unit ``first``, armed at once."""
        if k_iters <= B_SLOTS and units <= LOCK_MAX:
            resident, b_slots, b_uses = True, k_iters, units
        else:
            # Streamed, a chain pass must cover whole units, so the ring must
            # divide what one takes.
            b_slots = max(
                s for s in range(1, B_SLOTS + 1) if (units * k_iters) % s == 0
            )
            resident, b_uses = False, 1
        return _Slab(
            first,
            units,
            a_split_for(units),
            c_split_for(units),
            resident,
            b_slots,
            b_uses,
        )

    def b_mt_passes(c, slab):
        """(fill, drain) passes over the used slots for column ``c``."""
        n_work = n_full + (1 if c < rem_blocks else 0)
        if slab.b_resident:
            return n_work, n_work * slab.units
        passes = n_work * slab.units * k_iters // slab.b_slots
        return passes, passes

    # What one arming queues on a memtile channel must fit its task queue,
    # since a memtile task cannot be awaited without a token route back to the
    # shim. So M is cut into slabs of units, each armed once the last one's C
    # has drained -- the state between two dispatches, which the cores cannot
    # tell from one. Also cut where it keeps B resident past LOCK_MAX units: B
    # is then read once per slab instead of once per unit. And cut past
    # SHIM_OUTER_MAX units, which the unsplit A leg and a streamed B leg both
    # carry in their outermost dimension.
    def slab_fits(slab):
        return slab.units <= SHIM_OUTER_MAX and all(
            passes <= SHIM_TASK_QUEUE * MT_TASK_PASSES
            for c in range(n_active_cols)
            for passes in b_mt_passes(c, slab)
        )

    def cut(n_slabs):
        size, extra = divmod(n_units, n_slabs)
        slabs, first = [], 0
        for i in range(n_slabs):
            units = size + (1 if i < extra else 0)
            slabs.append(make_slab(first, units))
            first += units
        return slabs

    for n_slabs in range(1, n_units + 1):
        slabs = cut(n_slabs)
        if all(map(slab_fits, slabs)) and (
            k_iters > B_SLOTS or all(s.b_resident for s in slabs)
        ):
            break
    else:
        raise ValueError(
            f"M={M} K={K} N={N}: even one unit per slab needs more passes over "
            f"a B pool than the {SHIM_TASK_QUEUE} x {MT_TASK_PASSES} one "
            f"memtile channel can queue"
        )

    def b_tap(mega_col, c, slab):
        # Every (mega_row, k) chunk this column consumes. B must arrive
        # pre-packed so each k-block is one contiguous run; reordering in the
        # descriptor instead gives an innermost run of T=8 bf16 and measured
        # 5.4x slower.
        return TensorAccessPattern(
            tensor_dims=(K * N // B_GROUP,),
            offset=(mega_col * COLS + c) * N_TILE * K // B_GROUP,
            # Resident, one k sweep for the whole column-block. Otherwise one
            # per unit, not per row-block: the cores hold each B chunk across a
            # group. The unit dimension has stride 0 because B does not depend
            # on the row.
            sizes=[1 if slab.b_resident else slab.units, k_iters, 1, b_slot_elems],
            strides=[0, b_slot_elems, 0, 1],
        )

    def start_b_mt(c, direction, passes, slab):
        """Program and start one of column ``c``'s memtile B channels.

        The chain is one BD per used slot, walked ``passes`` times. The task is
        returned for freeing, and never awaited: C completing implies both.
        """
        fill = direction == DMAChannelDir.S2MM
        channel, bd0 = (
            (B_MT_S2MM, B_MT_S2MM_BD0) if fill else (B_MT_MM2S, B_MT_MM2S_BD0)
        )
        chunks = [MT_TASK_PASSES] * (passes // MT_TASK_PASSES)
        if passes % MT_TASK_PASSES:
            chunks.append(passes % MT_TASK_PASSES)
        task = dma_configure_task(
            mt_tiles[c].op, direction, channel, repeat_count=chunks[0] - 1
        )
        with bds(task) as bd:
            for i in range(slab.b_slots):
                prod, cons = b_mt_prod[c][i], b_mt_cons[c][i]
                wait, post = (prod, cons) if fill else (cons, prod)
                with bd[i]:
                    use_lock(
                        wait.op,
                        LockAction.AcquireGreaterEqual,
                        value=slab.b_uses if fill else 1,
                    )
                    dma_bd(
                        b_mt_bufs[c].op,
                        offset=i * b_slot_elems,
                        transfer_len=b_slot_elems,
                        bd_id=bd0 + i,
                    )
                    use_lock(
                        post.op,
                        LockAction.Release,
                        value=slab.b_uses if fill else 1,
                    )
                    if i + 1 < slab.b_slots:
                        next_bd(bd[i + 1])
                    else:
                        EndOp()
        dma_start_task(task)
        # Past one task's repeat count, queue the same chain again rather than
        # configure another task: its BDs are pinned, so the allocator would
        # refuse them while the first is live, and they are already written.
        tile = mt_tiles[c]
        for n in chunks[1:]:
            npu_push_queue(tile.col, tile.row, direction, channel, False, n - 1, bd0)
        return task

    def c_taps(mega_col, c, units, slab):
        # Every joined block this column produces: one ROWS*M_TILE x N_TILE
        # per row-block, in plain row-block order even under M_CHUNK.
        if slab.c_split:
            taps = []
            for u in units:
                first, count = unit_rows(u)
                # One descriptor per row-block: grouping them would put the
                # ROWS*M_TILE*N stride back in, which c_split exists to avoid.
                for i in range(count):
                    taps.append(
                        TensorAccessPattern(
                            tensor_dims=(M * N,),
                            offset=(mega_col * COLS + c) * N_TILE
                            + (first + i) * ROWS * M_TILE * N,
                            sizes=[1, 1, ROWS * M_TILE, N_TILE],
                            strides=[0, 0, N, 1],
                        )
                    )
            return taps
        return [_c_tap_unsplit(mega_col, c, slab)]

    def _c_tap_unsplit(mega_col, c, slab):
        return TensorAccessPattern(
            tensor_dims=(M * N,),
            offset=(mega_col * COLS + c) * N_TILE
            + slab.first * M_CHUNK * ROWS * M_TILE * N,
            sizes=[1, slab.units * M_CHUNK, ROWS * M_TILE, N_TILE],
            strides=[0, ROWS * M_TILE * N, N, 1],
        )

    def emit_slab(slab, A, B, C, a_prods, c_conses):
        # Per-slab setup: arming B's memtile channels and the cores'
        # parameters. Neither is free -- together tens of microseconds of
        # command-processor time -- so it goes out *behind* the first block's A
        # and B fills, overlapping their DDR latency. A fill running ahead of
        # it is harmless: A only lands in fifo buffers, and B backs up in the
        # stream until its memtile channel has a task. Measured on the
        # benchmark shapes, arming first cost up to +30 us (+9%) at M=256.
        #
        # The unsplit path issues each row's A for a block as one transfer, so
        # nothing ahead of this awaits; a fill awaited before the cores are
        # released would never complete.
        b_mt_tasks = []
        set_up = []

        def set_up_once():
            if set_up:
                return
            set_up.append(True)
            # Arm B's pools: only the slots this slab uses. A consumer lock is
            # always back at 0 by the end of a slab, so only the producer side
            # needs setting, and before its channel starts.
            for c in range(n_active_cols):
                fill_passes, drain_passes = b_mt_passes(c, slab)
                if not fill_passes:
                    continue
                for i in range(slab.b_slots):
                    set_lock(b_mt_prod[c][i].op, slab.b_uses)
                for direction, passes in (
                    (DMAChannelDir.S2MM, fill_passes),
                    (DMAChannelDir.MM2S, drain_passes),
                ):
                    b_mt_tasks.append(start_b_mt(c, direction, passes, slab))

            # Write every core's parameters, then open every barrier. Both
            # loops run to completion before any barrier opens, so no core can
            # read a half-written buffer.
            for r in range(ROWS):
                for c in range(n_active_cols):
                    rtps[r][c][RTP_N_VAL] = N
                    rtps[r][c][RTP_M_ROW_BLOCKS] = slab.units * M_CHUNK
                    rtps[r][c][RTP_K_ITERS] = k_iters
                    rtps[r][c][RTP_EPILOGUE] = epilogue.mode
                    rtps[r][c][RTP_CLAMP_MIN] = clamp_min_bits
                    rtps[r][c][RTP_CLAMP_MAX] = clamp_max_bits
                    # Only what this configuration actually reads; see
                    # rtp_layout.
                    if "n_chunks" in rtp_slots:
                        rtps[r][c][rtp_slots["n_chunks"]] = slab.units
                        rtps[r][c][rtp_slots["n_units"]] = slab.units
            for r in range(ROWS):
                for c in range(n_active_cols):
                    barriers[r][c].set(1)

        # A trailing block uses only the first rem_blocks columns. A is still
        # issued for every row, since the sitting-out columns drain it.
        blocks = [(mc, COLS) for mc in range(n_full)]
        if rem_blocks:
            blocks.append((n_full, rem_blocks))

        # C is issued with its block's fills and retired last: keeping that
        # S2MM outstanding overlaps compute with write-back, and it must not
        # share a group with the fills it depends on. It goes out after them,
        # since the first C only arrives after a whole k sweep. Tasks stay live
        # until retired here.
        all_mb = list(range(slab.first, slab.first + slab.units))

        # One emitter per leg, so the paths below differ only in how they
        # group and retire.
        def issue_a(mega_col, mbs, group, wait=False):
            for r in range(ROWS):
                taps = a_taps(mega_col, r, mbs, slab)
                for i, tap in enumerate(taps):
                    # A leftover unit emits many fills back to back on one
                    # channel, so await every SHIM_TASK_QUEUE-th to stay inside
                    # the queue depth.
                    bounded = (
                        len(taps) > SHIM_TASK_QUEUE and (i + 1) % SHIM_TASK_QUEUE == 0
                    )
                    a_prods[r].fill(A, tap, group=group, wait=wait or bounded)

        def issue_b(mega_col, active_cols, group):
            # B's shim end is a Flow's allocation, not a fifo, so there is no
            # fill(). This is what fill() emits, freed with its group the same
            # way.
            for c in range(active_cols):
                task = shim_dma_single_bd_task(
                    f"B_L3L2_{c}", B.op, tap=b_tap(mega_col, c, slab)
                )
                dma_start_task(task)
                group._actions.append((dma_free_task, [task]))

        def issue_c(mega_col, active_cols, mbs, group):
            for c in range(active_cols):
                for tap in c_taps(mega_col, c, mbs, slab):
                    c_conses[c].drain(C, tap, group=group, wait=True)

        def emit_unsplit():
            pending = []
            for mega_col, active_cols in blocks:
                # C in its own group so it does not share one with the fills
                # it depends on; see above.
                tg_c = TaskGroup()
                tg_f = TaskGroup()
                issue_a(mega_col, all_mb, tg_f)
                issue_b(mega_col, active_cols, tg_f)
                set_up_once()
                issue_c(mega_col, active_cols, all_mb, tg_c)

                pending.append([tg_f, tg_c])
                while len(pending) >= OVERLAP:
                    for tg in pending.pop(0):
                        tg.finish()

            for group in pending:
                for tg in group:
                    tg.finish()

        def emit_split():
            """Issue split legs one unit at a time, retiring the oldest.

            One TaskGroup per unit, retired only when a new one would exceed
            SHIM_TASK_QUEUE outstanding. ``pending`` is retired in append
            order, which keeps a block's B and unsplit-leg descriptors alive
            until its units have been awaited.
            """
            # What a unit costs on the busiest channel. Under c_split it
            # drains M_CHUNK C descriptors onto one, so counting units instead
            # would overrun the queue by that factor.
            unit_cost = M_CHUNK if slab.c_split else 1
            pending = []  # (group, queue cost), oldest first

            def retire(limit):
                while sum(q for _, q in pending) > limit:
                    pending.pop(0)[0].finish()

            for mega_col, active_cols in blocks:
                tg_b = TaskGroup()
                issue_b(mega_col, active_cols, tg_b)

                tg_whole = TaskGroup()
                if not slab.a_split:
                    issue_a(mega_col, all_mb, tg_whole)
                set_up_once()
                if not slab.c_split:
                    issue_c(mega_col, active_cols, all_mb, tg_whole)

                for u in all_mb:
                    # Before issuing, not after: fill/drain pushes the task
                    # immediately while TaskGroup.finish() emits the await, so
                    # retiring afterwards would leave the queue transiently one
                    # over. Await down to where this unit's transfers fit.
                    retire(SHIM_TASK_QUEUE - unit_cost)
                    tg_u = TaskGroup()
                    if slab.c_split:
                        issue_c(mega_col, active_cols, [u], tg_u)
                    if slab.a_split:
                        issue_a(mega_col, [u], tg_u, wait=True)
                    pending.append((tg_u, unit_cost))

                # Not queue-counted: B and the unsplit leg ride channels the
                # units do not contend for. Still retired in order.
                pending.append((tg_whole, 0))
                pending.append((tg_b, 0))

            # Drain everything, not retire(0): the tail groups are weighted 0,
            # so a count-driven loop stops with them still open and the build
            # fails with "Failed to close task groups".
            for tg, _ in pending:
                tg.finish()

        emit_split() if (slab.a_split or slab.c_split) else emit_unsplit()
        # Every C has been awaited, so B's memtile tasks are done.
        for task in b_mt_tasks:
            dma_free_task(task)

    def sequence(A, B, C, a_prods, c_conses):
        # Back to back: a slab returns only once its C has all drained.
        for slab in slabs:
            emit_slab(slab, A, B, C, a_prods, c_conses)

    rt = Runtime(
        sequence,
        [
            a_l3_ty,
            b_l3_ty,
            c_l3_ty,
            [f.prod() for f in a_l3l2_fifos],
            [f.cons() for f in c_l2l3_fifos],
        ],
    )
    for flow in b_flows:
        rt.add_flow(flow)
    for c in range(n_active_cols):
        for lock in b_mt_prod[c] + b_mt_cons[c]:
            rt.add_lock(lock)
    for (r, c), (_, prod, cons) in b_l1.items():
        rt.add_lock(prod)
        rt.add_lock(cons)
    for td in b_l1_dmas:
        rt.add_tile_dma(td)

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
        "--epilogue", type=Epilogue, choices=list(Epilogue), default=Epilogue.NONE
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
