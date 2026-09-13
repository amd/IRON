# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""bf16 GEMM over a 4-row compute-tile grid, as wide as the device.

A second GEMM design alongside ``iron.operators.gemm``, specialised for
transformer projection shapes. The overall dataflow is the same whole-array
shape as that operator's -- A broadcast along each compute row, B down each
column, C joined through the memtile -- so those are NOT what distinguishes it.
What does:

  * **B is quantized to bfp16ebs8 on NPU2** by ``GEMM.pack_B``, not bf16.
    ``iron.operators.GEMM`` only ever moves bf16. This is not primarily a DMA
    saving: it is what makes NPU2's fast mmul lowering available at all --
    ``aie::mmul<8,8,8>`` needs bfp16 operands to decompose into two emulated
    macs instead of four, which is most of the NPU2 speedup (see NPU1 in
    README.md's Performance section, where B stays bf16 and the margin over
    ``iron.operators.GEMM`` is correspondingly smaller). Quantizing is
    numerically free -- the mmul only multiplies bfp16 regardless, so this
    hoists a rounding that already happened on every mac -- provided it
    reproduces the core's rounding mode; see ``packing.py``.
  * **The tile shape is fixed, not parameterised** -- but fixedness alone is
    not the advantage: ``iron.operators.GEMM`` is equally fixed once compiled
    with a choice of tile args. What differs is *which* shape is fixed. r/s/t
    stays 8/8/8 on both architectures for the reason below. m/k = 64/512 (n
    defaults to 64) is chosen for the L1-budget tradeoff documented next to
    ``CT_MAX_K_FOR_N`` below: n=64 gives the mmul a colA of 8 rather than 4,
    which wins whenever compute is the critical path, at the cost of A being
    re-read more often. Only the grid WIDTH varies with the device: 8 columns
    on NPU2, 4 on NPU1.
  * **A fused epilogue.** The f32->bf16 conversion, an optional activation and
    an optional clamp all happen while the values are still in registers, on the
    way into the C object, instead of a separate pass over L1.
  * **B arrives pre-packed** by ``GEMM.pack_B``, in the order the cores consume
    it, so both B hops are plain linear descriptors instead of the 128-byte
    scattered bursts ``iron.operators.GEMM`` reorders in the descriptor.
  * **Asymmetric tile buffering (ATB)**, so the A tile and the accumulator need
    not share a height -- this is what buys the deep k slice (K_TILE=512)
    within the L1 budget; see README.md's ATB reference.

None of these helps alone -- see README.md's Performance section for the
measured, per-choice breakdown of the gap against both the shipped FastFlowLM
overlay and ``iron.operators.GEMM``.

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
from enum import StrEnum
from functools import partial

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
    WorkerRuntimeBarrier,
)
from aie.iron.controlflow import range_
from aie.dialects.aie import get_target_model
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron.device import NPU1, NPU2, Tile
from iron.common.utils import split_run
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
# n=256 is deliberately absent: at that width the f32 accumulator alone
# (M_TILE * 256 * 4 = 65536 bytes) already fills the whole of L1, before A, B
# or C are even counted, so no ct_max_k could ever make it fit.
CT_MAX_K_FOR_N = {16: 16, 32: 32, 64: 128, 128: 32}
# Register tiling, shared by both architectures. These set the blocked L1
# layout, so ``pack_B``, the four stream-dimension lists below and
# ``gather_dims`` all key off them; changing one without the others is silently
# wrong rather than a build error.
#
# Matching AIE2's native 4x8x4 mac shape instead is a measured dead end, at
# 22-30% slower: the kernel is load-port bound rather than shuffle bound, and
# 4/8/4 needs 1.62 loads per mac against 8/8/8's 1.06, because the 2x2 register
# block amortizes each load over four macs either way but over far less work.
# Retrying it needs a wider register block on the native shape, i.e. a 4x4 mmul
# kernel, not just a different r/s/t here.
R, S, T = 8, 8, 8


def compute_rows(dev):
    """Compute-tile rows: the array less the shim row and the memtile rows."""
    tm = get_target_model(dev.resolve())
    return tm.rows() - 1 - tm.get_num_mem_tile_rows()


CT_OUT_LEN = 512  # the core's C slice, streamed out in chunks this size
C_DEPTH = 2  # C fifo depth; also the core-body unroll
B_DEPTH = 2  # B fifo depth; also the core-body unroll
A_DEPTH = 2
# Row-blocks a core folds into one B fetch: it HOLDS a B chunk across M_CHUNK
# accumulators instead of releasing it after one, so DDR reads B
# m_row_blocks/M_CHUNK times instead of m_row_blocks. This is what replaces the
# B residency the runtime parameters cost us -- residency sized the memtile
# buffer from k_iters and replayed it m_row_blocks times, putting both K and M
# in the device configuration, whereas M_CHUNK is a configuration constant and
# leaves both runtime.
#
# Two things it costs:
#   * L1: M_CHUNK accumulators instead of one. At tile_n=64 the k slice is
#     unaffected (ct_k stays 128, colA 16) and only tile_ma drops 32 -> 16;
#     at tile_n=128 nothing fits, so M_CHUNK is resolved per tile_n below.
#   * A is issued once per chunk-group rather than once per column-block.
#     Holding B means streaming A k-major -- A[mc0][k0], A[mc1][k0],
#     A[mc0][k1], ... -- which wants five dimensions, and a shim BD carries
#     four: the outermost lands in the ITERATION field and the inner three are
#     its ND dims (getBDMaxDims is 3 off a memtile). So the chunk-group
#     dimension comes out of the descriptor and becomes separate transfers
#     carrying the jump in the OFFSET, which has no such limit -- exactly the
#     trick a_split already uses for the mega_row dimension, and it reuses the
#     same windowing. What is left per transfer is
#     [k_iters, M_CHUNK, M_TILE, K_TILE], which fits.
# DEFAULT 1 EVERYWHERE -- i.e. off. The mechanism is correct and tested, but
# interleaved A/B at K=1024 N=4096 (10 rounds, round-robin in one process)
# does not show a consistent win:
#
#     M      m_chunk=1 min/med    m_chunk=2 min/med     min      med
#      512    525.4 /  622.7       502.1 /  566.3      -4.4%    -9.1%
#     1024    959.0 / 1081.6      1092.4 / 1162.9     +13.9%    +7.5%
#     2048   1902.8 / 1986.0      1837.1 / 1940.0      -3.5%    -2.3%
#
# B's DDR traffic really does fall by m_chunk, but something else eats it --
# most likely the per-unit A descriptors, since m_chunk forces the split path
# for A (see a_split). The M=1024 regression is not monotonic in n_units and
# is not explained; do not turn this on by default without understanding it.
#
# An earlier NON-interleaved measurement showed -11%/-15% and was wrong; see
# the bimodal-timing discipline in README.md. Interleave before believing any
# number here.
M_CHUNK_FOR_N = {16: 1, 32: 1, 64: 1, 128: 1}
# How many column-blocks the runtime sequence keeps in flight. A block costs 3
# shim buffer descriptors on a column (A + B + C) against 16 available, so the
# ceiling is 5; 2 is enough to keep the fills ahead of the cores.
OVERLAP_DEFAULT = 2


class Epilogue(StrEnum):
    """Activation folded into the C drain.

    Declaration order is the wire format -- it is both the kernel's
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


# The runtime parameter buffer each core reads once its barrier opens.
#
# The clamp bounds are the one non-obvious entry: they are floats, but
# npu_write_rtp only writes i32 words, so they travel as raw bit patterns and
# the kernel bit-casts them back. Whether a clamped path exists at all stays
# compile-time (op.py's -DMM_FUSED_CLAMP), because it costs program memory;
# only the enable and the bounds are runtime, so every pair of bounds shares
# one build.
(
    RTP_N_WORK,
    RTP_N_DRAIN,
    RTP_M_ROW_BLOCKS,
    RTP_K_ITERS,
    RTP_EPILOGUE,
    RTP_CLAMP_ENABLED,
    RTP_CLAMP_MIN_BITS,
    RTP_CLAMP_MAX_BITS,
    # Row-blocks split into M_CHUNK-wide groups plus a leftover: m_row_blocks
    # need not divide by M_CHUNK (M=256 is one row-block, M=768 is three), so
    # the core runs a wide pass n_chunks times and a single-wide pass n_rem
    # times. Both counts are runtime, so any M still rides one xclbin.
    RTP_N_CHUNKS,
    RTP_N_UNITS,
) = range(10)
RTP_WORDS = 10


class Rounding(StrEnum):
    """Rounding for every f32->bf16 conversion.

    The core powers up in floor; conv_even is the default because truncation
    biases every conversion the same way and the error then accumulates over
    the K reduction. floor reproduces the shipped overlay.
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
# Hardware facts the Python bindings do not expose: gemm() reads AIETargetModel
# directly for the L1 ceiling, BD count and grid, but neither getDmaBdStepBits
# nor getDmaBdWrapSizeBits is bound, and nothing models the channel task queue.
# gemv/design.py and repeat/design.py hardcode the same fields.
#
# Step field width. An IR-level bf16-element stride S is re-expressed as
# (S - 1) * 2 bytes / 4-byte granularity before AIEXDialect.cpp checks it.
_SHIM_STEP_BITS = 20
_BF16_BYTES = 2
_ADDR_GRANULARITY_BYTES = 4
# Entries in a shim DMA channel's task queue. AIEDmaToNpu's NpuPushQueueOp
# pushes unconditionally, so overrunning this is a silent device hang rather
# than a diagnostic. Measured at K=10240 M=1024: 4 outstanding tasks on one
# channel run, 8 hang.
SHIM_TASK_QUEUE = 4


def _hw_stride_ok(stride_elems):
    hw_stride = (stride_elems - 1) * _BF16_BYTES // _ADDR_GRANULARITY_BYTES
    return hw_stride <= (1 << _SHIM_STEP_BITS) - 1


def _default_l1(n_tile, ct_max_k, b_elem_bytes, budget, m_chunk=1):
    """Pick (A-tile height, L1 B depth) -- the largest working set that fits.

    ``b_elem_bytes`` is 9/8 where B is bfp16ebs8 and 2 where it is bf16, and
    ``budget`` is the core's data memory, so the search below reflects what B
    actually costs on this device.

    No stack is reserved out of ``budget``: the cores leave ``stack_size``
    unset and aiecc measures each core's requirement and fails the build if it
    does not fit, so the stack is the toolchain's to enforce. This kernel
    measures 192 bytes against the >=6 KB the search leaves unused anyway.

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
    # m_chunk accumulators, because the core holds a B chunk across that
    # many row-blocks; see M_CHUNK_FOR_N. This is the ONLY term that
    # scales with it -- A is acquired and released one band at a time
    # inside the group loop, and C drains the accumulators in turn.
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

    ``_default_l1`` picks L1_B_DEPTH together with the t_ma IT chooses; that
    pairing need not fit a caller-overridden t_ma; a taller A tile leaves less
    L1 for B, and can push a working set that fit at the default t_ma over
    budget. Raise rather than silently reusing a depth that doesn't fit.

    How much the depth is worth, measured on npu2 (turbo, 12 interleaved rounds
    of 20 dispatches, min of per-round medians) by forcing depth 1 against the
    default: 1.2% at M=1024 K=1536 N=6144, and within noise at K=1024 N=4096 and
    K=512 N=1024. So the prefetch earns its L1 at the largest shapes and is
    close to free elsewhere -- worth keeping, but not worth contorting the
    search for.
    """
    # m_chunk accumulators, because the core holds a B chunk across that
    # many row-blocks; see M_CHUNK_FOR_N. This is the ONLY term that
    # scales with it -- A is acquired and released one band at a time
    # inside the group loop, and C drains the accumulators in turn.
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
    overlap=None,
    kernel_object="mm_fused.o",
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
    # Everything shape-related below comes from the device rather than a
    # constant, so the same dataflow covers NPU2's 4x8 and NPU1's 4x4.
    tm = get_target_model(dev.resolve())
    COLS, ROWS = dev.cols, compute_rows(dev)
    MIN_M = M_TILE * ROWS
    SHIM_BDS = tm.get_num_bds(0, 0)
    N_TILE = tile_n
    CT_MAX_K = CT_MAX_K_FOR_N[N_TILE]
    M_CHUNK = M_CHUNK_FOR_N[N_TILE] if m_chunk is None else m_chunk
    # B is bfp16ebs8 on AIE2P and bf16 on AIE2: the scalar BFP types are gated
    # on __AIE_API_SCALAR_BFP_TYPES__, which only aie_api/detail/aie2p/config.hpp
    # defines, so on AIE2 B stays bf16 and the mmul lowers onto four native
    # 4x8x4 macs. That choice drives every B type and extent below. B_GROUP is
    # the number of B values per element of the MLIR type, so a length in values
    # becomes a length in elements by dividing.
    BFP16_B = dev.arch == AIEArch.AIE2p
    B_GROUP = BFP16_GROUP if BFP16_B else 1
    b_elem_bytes = BFP16_GROUP_BYTES / BFP16_GROUP if BFP16_B else 2
    # Asymmetric tile buffering: the A tile spans T_MA rows while the
    # accumulator spans M_TILE, so the core folds RHO bands into one C tile.
    # A is dead the moment it is consumed while C lives across the whole K
    # reduction, so sizing both to M_TILE pays the peak L1 cost twice.
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
    OVERLAP = OVERLAP_DEFAULT if overlap is None else overlap
    K_DIV_CT_K_MAX = K_TILE // CT_MAX_K
    CT_A_LEN = 2 * R * CT_MAX_K  # one z slice
    CT_A_OBJ = CT_A_LEN * (T_MA // R // 2)  # every z slice of one mmul
    C_SLICE_LEN = M_TILE * N_TILE  # one compute tile's C contribution
    O_CHUNKS = C_SLICE_LEN // CT_OUT_LEN  # C objects an accumulator drains as
    B_ITERS = K_TILE // CT_MAX_K  # B chunks consumed per k step
    MIN_N = N_TILE * COLS

    epilogue = Epilogue(epilogue)
    # Clamp bounds ride the RTP buffer as raw int32 bit patterns: npu_write_rtp
    # writes i32 words only, so the kernel bit-casts them back. Bounds being
    # runtime is what lets every pair share one build; whether a clamped path
    # exists at all is still op.py's -DMM_FUSED_CLAMP, because it costs
    # program memory.
    clamp_enabled = 1 if clamp is not None else 0
    clamp_lo, clamp_hi = clamp if clamp is not None else (0.0, 0.0)
    clamp_min_bits = int(np.float32(clamp_lo).view(np.int32))
    clamp_max_bits = int(np.float32(clamp_hi).view(np.int32))
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
    # Row-blocks grouped M_CHUNK at a time, so one B fetch feeds M_CHUNK of
    # them (see M_CHUNK_FOR_N). A "unit" below is one such group, or one of the
    # n_rem leftovers when M_CHUNK does not divide m_row_blocks. Every leg is
    # issued per unit, so A, B and C stay aligned with each other and with the
    # core's loop nest.
    n_chunks, n_rem = divmod(m_row_blocks, M_CHUNK)
    if n_rem:
        # op.py resolves m_chunk so this cannot fire. A partial group is
        # genuinely inexpressible: its object is M_CHUNK tiles wide and the
        # forward always drains that much, so the rest would have to be filled
        # by repeating the row-block -- and every way of saying that is
        # rejected or mis-lowered. Stride 0 in an inner dimension is refused
        # ("Stride 2 must be a positive integer"); stride 0 in the outermost
        # slot IS the BD repeat count, which releases one object per
        # repetition rather than one object in total; and several sub-object
        # fills do not coalesce into one object either. All three were tried
        # on hardware. Hence op.py falls back to m_chunk=1 instead.
        raise ValueError(
            f"m_row_blocks ({m_row_blocks}) must be a multiple of m_chunk "
            f"({M_CHUNK}); op.py should have resolved m_chunk to 1 here"
        )
    n_units = n_chunks

    def unit_rows(u):
        """(first row-block, how many) for unit ``u`` -- always a full group."""
        return u * M_CHUNK, M_CHUNK

    # A mega_row dimension with stride ROWS*M_TILE*{K,N} lands in the shim
    # BD's ITERATION field, whose step is 20 bits, so it overflows once K or N
    # crosses ~8191 elements -- E4B's FFN width (10240) does, E2B's max (6144)
    # does not. Only relevant once M walks more than one mega_row; at M=256 the
    # dimension is degenerate (size 1) and is stripped before the stride is
    # ever encoded, so it never fails there regardless of K/N.
    #
    # Such a leg is instead issued as m_row_blocks separate transfers, each
    # carrying the mega_row jump in its OFFSET (unbounded) rather than a shared
    # STRIDE. The two legs are independent -- E4B's down-proj overflows on K
    # (A only) and its gate/up on N (C only) -- so neither shape pays for both.
    #
    # Those transfers must stay live in their TaskGroup until awaited.
    # TaskGroup.finish() emits dma_free_task, which returns the buffer
    # descriptor id to a COMPILE-TIME allocator that does not check the
    # transfer finished (mlir-aie AIEAssignRuntimeSequenceBDIDs::recycle,
    # isAwait=false); ids are per shim TILE, shared across channels and
    # directions, so retiring one early lets the next task reprogram a live
    # descriptor. Verify with aie-opt --aie-substitute-shim-dma-allocations
    # --aie-assign-runtime-sequence-bd-ids: the ids on a shim tile must be
    # distinct.
    # M_CHUNK > 1 forces the split path for A: holding B makes the core's A
    # order k-major within a group, which wants a fifth dimension, so the unit
    # dimension comes out of the descriptor and becomes one transfer each.
    # At n_units == 1 there is nothing to split -- a single transfer already
    # covers the block -- so the cheaper unsplit path still applies.
    a_split = n_units > 1 and (M_CHUNK > 1 or not _hw_stride_ok(ROWS * M_TILE * K))
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
    # A window is counted in TRANSFERS, not units: under c_split a unit emits
    # one C descriptor per row-block (M_CHUNK of them, see c_taps), so a
    # window of SHIM_TASK_QUEUE units would push M_CHUNK times that many onto
    # one channel and hang.
    _per_unit = M_CHUNK if c_split else 1
    MB_WINDOW = (
        min(n_units, max(1, SHIM_TASK_QUEUE // _per_unit))
        if (a_split or c_split)
        else 1
    )
    bds_per_block = (
        1 + (MB_WINDOW if a_split else 1) + (MB_WINDOW * _per_unit if c_split else 1)
    )
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
    # Only a block that spans MORE THAN ONE window awaits inside itself; that
    # is what makes a second block in flight refill the queue the windowing
    # just drained. A single-window block has no intra-block await, so it can
    # still overlap -- and it must, because m_chunk forces a_split on for the
    # descriptor's sake even when nothing needs windowing, and losing the
    # pipelining costs far more than the B traffic m_chunk saves (measured
    # +13% at M=1024 before this).
    if (a_split or c_split) and n_units > MB_WINDOW:
        OVERLAP = 1
    else:
        OVERLAP = max(1, min(OVERLAP, SHIM_BDS // bds_per_block))
    # Sweeps where all COLS columns have work, plus a trailing group of
    # rem_blocks columns (0 <= rem_blocks < COLS) that do one block more.
    n_full = N // MIN_N
    rem_blocks = (N % MIN_N) // N_TILE
    # Every column is instantiated for every shape, because which columns
    # exist is configuration and this design has one configuration. A column
    # with no work for this shape gets n_work = 0 and drains instead.
    n_active_cols = COLS
    # Per column: how many column-blocks it computes, and how many it sits out
    # while still draining the A broadcast for its row. Every block issues A
    # for every compute row, so a column that does not compute a block must
    # still take that block's A or the row stalls -- the memtile will not
    # release an A object until all COLS consumers have taken it.
    total_blocks = n_full + (1 if rem_blocks else 0)
    col_work = [n_full + (1 if c < rem_blocks else 0) for c in range(COLS)]
    col_drain = [total_blocks - w for w in col_work]

    # B's element type: one v8bfp16ebs8 per 8 values on AIE2P, one bf16 per
    # value on AIE2. Every B extent below is therefore in values // B_GROUP.
    b_elem_ty = np.dtype[v8bfp16ebs8] if BFP16_B else bf16_ty
    # L1 (per compute tile)
    ct_a_obj_ty = np.ndarray[(CT_A_OBJ,), bf16_ty]
    ct_b_ty = np.ndarray[(CT_MAX_K * N_TILE // B_GROUP,), b_elem_ty]
    ct_out_ty = np.ndarray[(CT_OUT_LEN,), bf16_ty]
    ct_acc_ty = np.ndarray[(M_TILE * N_TILE,), f32]
    # L2 (per memtile)
    # M_CHUNK stacked row-block tiles, so the forward below can interleave
    # them on the way out -- see a_send_dims.
    mt_a_ty = np.ndarray[(M_CHUNK * M_TILE * K_TILE,), bf16_ty]
    mt_a_bytes = M_CHUNK * M_TILE * K_TILE * 2
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
    # Same object as the mmul: the epilogue is compiled into mm_fused.cc, so
    # one -D flag set and one artifact cover both.
    epilogue_chunk = Kernel(
        EPILOGUE_SYMBOL,
        kernel_object,
        # outer, half, mode, clamp_enabled, clamp_min_bits, clamp_max_bits
        [ct_out_ty, ct_acc_ty] + [np.int32] * 6,
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
    # B needs no reblocking on either hop: pack_B already emits it in the
    # order the cores consume, so the memtile just streams it through. That
    # frees every descriptor dimension B used to spend -- which is what lets
    # CT_MAX_K reach 128 (the innermost run would otherwise overflow the BD's
    # 10-bit size field and need a split dimension) at the same time as
    # residency (which spends one on its outer k walk).
    b_recv_dims = None
    b_send_dims = None
    # A: same idea, r x s blocks.
    # The outermost row-group dimension spans M_CHUNK tiles rather than one.
    # That is the whole trick: mc's stride is M_TILE*K_TILE, which is exactly
    # this dimension's size*stride, so the two are contiguous and merge -- the
    # walk stays within the memtile BD's four dimensions while gaining an
    # interleave it could not otherwise express.
    a_recv_dims = [
        (M_CHUNK * M_TILE // R, R * K_TILE),
        (R, S),
        (K_TILE // S, R * S),
        (S, 1),
    ]
    # Emits (b_iter, mc, band) -- b_iter outermost, then all M_CHUNK tiles'
    # row-groups. That is the order the core acquires A in when it holds a B
    # chunk across the group, and it is why ONE fifo suffices: a second would
    # need a third core input DMA channel, and a tile has two.
    a_send_dims = [
        (K_DIV_CT_K_MAX, R * CT_MAX_K),
        (M_CHUNK * M_TILE // R, R * K_TILE),
    ] + split_run(R * CT_MAX_K)

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
        )
        for r in range(ROWS):
            c_prod[(r, c)] = sub[r]

    # A: shim -> memtile -> broadcast along the compute row. The reblocking
    # rides the forward(): inbound on cons(dims_from_stream=), outbound on
    # forward(dims_to_stream=), sharing one memtile buffer.
    # ONE fifo per row, even at M_CHUNK > 1. The interleave the core needs
    # lives in a_send_dims above, not in extra fifos: a second A fifo would
    # make the core want 3 input DMA channels and a compute tile has 2 (the
    # design already spends both, on A and B).
    a_l3l2_fifos = []
    a_cons = {}
    for r in range(ROWS):
        of_a_in = ObjectFifo(mt_a_ty, name=f"A_L3L2_{r}", depth=A_DEPTH)
        a_l3l2_fifos.append(of_a_in)
        of_a = of_a_in.cons(dims_from_stream=a_recv_dims).forward(
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
    # B residency is gone: it sizes the memtile buffer from k_iters and
    # replays it m_row_blocks times through the forward()'s repeat_count, so
    # it carries both K and M into the configuration, which is what the
    # runtime parameters exist to remove. See README.md for what that cost.
    b_resident = False

    b_l3l2_fifos = []
    b_cons = {}
    for c in range(n_active_cols):
        of_b_in = ObjectFifo(mt_b_ty, name=f"B_L3L2_{c}", depth=B_DEPTH)
        b_l3l2_fifos.append(of_b_in)
        of_b = of_b_in.cons(dims_from_stream=b_recv_dims).forward(
            # The one placement pin this design keeps. Everything else -- the
            # workers, the accumulator buffers, the C join, the A forward and
            # the shim ends -- is left to the placer, and measures the same.
            #
            # Without it, aie-place-tiles merges the 20 logical memtiles (4 A
            # relays + 8 B relays + 8 C joins) onto the 8 physical ones in a way
            # that aie-objectFifo-stateful-transform then rejects with "number
            # of input DMA channel exceeded". Spreading B one-per-column is
            # enough to steer it to a legal assignment; see the mlir-aie issue
            # referenced in README.md. Reproduces at M=1024 K=2048 N=2048, which
            # test.py covers.
            tile=Tile(c, 1),
            obj_type=ct_b_ty,
            depth=L1_B_DEPTH,
            name=f"B_L2L1_{c}",
            dims_to_stream=b_send_dims,
        )
        for r in range(ROWS):
            b_cons[(r, c)] = of_b.cons()

    # --- Runtime parameters -----------------------------------------------
    rtps = [
        [
            Buffer(
                np.ndarray[(RTP_WORDS,), np.dtype[np.int32]],
                name=f"rtp_{r}_{c}",
                initial_value=np.zeros(RTP_WORDS, dtype=np.int32),
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
    def core_fn(accs, o_h, b_h, a_h, init_k, kstep_k, epi_k, my_rtp, barrier):
        """Core body. Every trip count and the activation come from the
        runtime parameter buffer, so one core program serves every shape."""
        # The loop nest lives here rather than inside the kernel so that
        # every level has an ObjectFifo acquire point.
        barrier.wait_for_value(1)
        n_work = my_rtp[RTP_N_WORK]
        n_drain = my_rtp[RTP_N_DRAIN]
        n_row_blocks = my_rtp[RTP_M_ROW_BLOCKS]
        n_k_iters = my_rtp[RTP_K_ITERS]
        epi_mode = my_rtp[RTP_EPILOGUE]
        clamp_enabled = my_rtp[RTP_CLAMP_ENABLED]
        clamp_min_bits = my_rtp[RTP_CLAMP_MIN_BITS]
        clamp_max_bits = my_rtp[RTP_CLAMP_MAX_BITS]
        n_chunks = my_rtp[RTP_N_CHUNKS]
        n_units_rt = my_rtp[RTP_N_UNITS]
        # Acquire does not consume the barrier, so take it back to zero or the
        # next dispatch reads these parameters again instead of waiting. Safe
        # before the work: the sequence cannot set the barrier again until it
        # has drained this dispatch's C.
        barrier.release_with_value(1)

        def sweep(group):
            """One k reduction feeding ``group`` accumulators off a shared B.

            ``group`` is a Python list, so its length is compile-time: the mc
            loops below unroll. Calling this with every accumulator is the
            wide pass; calling it with one is the leftover pass.

            Holding B across the group is the whole point -- b_h is acquired
            once outside the mc loop and released after all of them, so DDR
            reads B once per len(group) row-blocks instead of once each.
            """
            for a_acc in group:
                init_k(a_acc)
            for _ in range_(n_k_iters):
                # The l loop is unrolled by the B fifo depth so the
                # acquired buffer index stays a compile-time constant.
                for _ in range_(B_ITERS // B_DEPTH):
                    for _ in range(B_DEPTH):
                        # One B chunk feeds every A band of every accumulator
                        # in the group, so B is acquired once around both.
                        # Each accumulator draws A from its OWN fifo, which is
                        # what makes this interleave legal -- see the a_cons
                        # construction above.
                        b = b_h.acquire(1)
                        for a_acc in group:
                            for band in range(RHO):
                                a = a_h.acquire(1)
                                kstep_k(a, b, a_acc, band)
                                a_h.release(1)
                        b_h.release(1)
            # Drain the accumulators. Unrolled by C_DEPTH for the same
            # reason; a full O_CHUNKS unroll overflows program memory.
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
                            clamp_enabled,
                            clamp_min_bits,
                            clamp_max_bits,
                        )
                        o_h.release(1)

        for _ in range_(n_work):
            for _ in range_(n_chunks):
                sweep(accs)

        # Column-blocks this column sits out. A is broadcast along the whole
        # compute row, so it must still consume its share or the columns that
        # DO have work stall waiting for the fifo to advance. No B and no C
        # here -- the runtime sequence issues neither for it.
        for _ in range_(n_drain):
            # Every unit delivers a full M_CHUNK tiles of A, leftover or not,
            # so an idle column drains that much per unit.
            for _ in range_(n_units_rt):
                for _ in range_(n_k_iters):
                    for _ in range_(B_ITERS // B_DEPTH):
                        for _ in range(B_DEPTH):
                            for _ in range(M_CHUNK * RHO):
                                a_h.acquire(1)
                                a_h.release(1)

    workers = []
    for r in range(ROWS):
        for c in range(n_active_cols):
            # One accumulator per row-block in a chunk group. Worker flattens
            # nested fn_args, so the list arrives in core_fn as a list and its
            # length stays compile-time.
            accs = [
                Buffer(type=ct_acc_ty, name=f"c_acc_{r}_{c}_{mc}")
                for mc in range(M_CHUNK)
            ]
            workers.append(
                Worker(
                    core_fn,
                    [
                        accs,
                        c_prod[(r, c)].prod(),
                        b_cons[(r, c)],
                        a_cons[(r, c)],
                        acc_init,
                        k_step,
                        epilogue_chunk,
                        rtps[r][c],
                        barriers[r][c],
                    ],
                )
            )

    # --- Runtime ----------------------------------------------------------
    #
    # Every wrap below stays under the shim's wrap/size field (DMA_BD_MAX_WRAP): the
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
    # wrap/size field (largest are K_TILE=512 and ROWS*M_TILE=256).
    def a_taps(mega_col, r, units):
        # Every (row-block, k) block this compute row consumes for one
        # column-block. A does not depend on mega_col; it is re-fetched per
        # column-block because the cores re-consume it.
        #
        # k OUTERMOST, then the group's M_CHUNK row-blocks: one memtile object
        # per k holding M_CHUNK stacked tiles, which a_send_dims then emits
        # interleaved as (b_iter, mc, band) -- the order the core acquires in
        # while holding a B chunk across the group.
        #
        # A leftover unit is one row-block wide but fills the same object, so
        # its mc dimension has stride 0: the row-block is repeated, and the
        # core drains the duplicate (see sweep). It costs one extra read of
        # that row-block, on at most one unit per column-block.
        if M_CHUNK == 1 and not a_split:
            return [
                TensorAccessPattern(
                    tensor_dims=(M * K,),
                    offset=r * M_TILE * K,
                    sizes=[m_row_blocks, k_iters, M_TILE, K_TILE],
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
            # One k sweep per UNIT, not per row-block: the cores hold each B
            # chunk across the M_CHUNK row-blocks of a group, so DDR reads B
            # n_units times instead of m_row_blocks. That is the whole win --
            # see M_CHUNK_FOR_N. The unit dimension keeps stride 0, replaying
            # the same k-blocks, exactly as the row-block dimension used to.
            sizes=(
                [1, 1, 1, k_iters * K_TILE * N_TILE // B_GROUP]
                if b_resident
                else [n_units, k_iters, 1, K_TILE * N_TILE // B_GROUP]
            ),
            strides=(
                [0, 0, 0, 1] if b_resident else [0, K_TILE * N_TILE // B_GROUP, 0, 1]
            ),
        )

    def c_taps(mega_col, c, units):
        # Every joined block this column produces for one column-block: one
        # ROWS*M_TILE x N_TILE block per row-block. Returns a LIST, for the
        # same reason a_taps does -- one descriptor per unit when N makes the
        # row-block stride overflow the shim BD's iteration step.
        #
        # C drains in plain row-block order even under M_CHUNK, because the
        # core drains a group's accumulators one after another, so no
        # reordering is needed here; a unit just covers `count` consecutive
        # row-blocks.
        if c_split:
            taps = []
            for u in units:
                first, count = unit_rows(u)
                # One descriptor PER ROW-BLOCK, not one per unit. Grouping a
                # unit's row-blocks into a count dimension would put a
                # ROWS*M_TILE*N stride back inside the descriptor, which is
                # exactly what c_split exists to avoid -- it overflows the
                # shim BD's 20-bit step at N=10240. C drains in plain
                # row-block order even under M_CHUNK (the core drains a
                # group's accumulators one after another), so splitting them
                # costs nothing but the extra descriptors.
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
        return [_c_tap_unsplit(mega_col, c)]

    def _c_tap_unsplit(mega_col, c):
        return TensorAccessPattern(
            tensor_dims=(M * N,),
            offset=(mega_col * COLS + c) * N_TILE,
            sizes=[1, m_row_blocks, ROWS * M_TILE, N_TILE],
            strides=[0, ROWS * M_TILE * N, N, 1],
        )

    def sequence(A, B, C, a_prods, b_prods, c_conses):
        # Write every core's parameters, then open every barrier. Both loops
        # run to completion before the first fill is issued, so no core can
        # read a half-written buffer.
        for r in range(ROWS):
            for c in range(n_active_cols):
                rtps[r][c][RTP_N_WORK] = col_work[c]
                rtps[r][c][RTP_N_DRAIN] = col_drain[c]
                rtps[r][c][RTP_M_ROW_BLOCKS] = m_row_blocks
                rtps[r][c][RTP_K_ITERS] = k_iters
                rtps[r][c][RTP_EPILOGUE] = epilogue.mode
                rtps[r][c][RTP_CLAMP_ENABLED] = clamp_enabled
                rtps[r][c][RTP_CLAMP_MIN_BITS] = clamp_min_bits
                rtps[r][c][RTP_CLAMP_MAX_BITS] = clamp_max_bits
                rtps[r][c][RTP_N_CHUNKS] = n_chunks
                rtps[r][c][RTP_N_UNITS] = n_units
        for r in range(ROWS):
            for c in range(n_active_cols):
                barriers[r][c].set(1)

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
        # column-block. Per-object tasks need 1 + 2*k_iters and cannot be
        # overlapped at all.
        # Keep OVERLAP column-blocks in flight, against SHIM_BDS buffer
        # descriptors per column; the operator is DDR-rate bound rather than
        # byte bound, so how deeply the fills are pipelined is what decides the
        # rate.
        #
        # Every task of a block stays LIVE in its TaskGroup until the block is
        # retired here. That is load-bearing, not tidiness -- see the
        # dma_free_task note on a_split above.
        # Units, not row-blocks: every leg is issued per unit so A, B and C
        # stay aligned with each other and with the core's nest. At
        # M_CHUNK == 1 a unit IS a row-block and this is the old list.
        all_mb = list(range(n_units))

        # One emitter per leg, so the two paths below differ only in HOW they
        # group and retire, not in how a leg is issued.
        def issue_a(mega_col, mbs, group, wait=False):
            for r in range(ROWS):
                taps = a_taps(mega_col, r, mbs)
                for i, tap in enumerate(taps):
                    # A leftover unit emits k_iters*M_CHUNK fills back to back
                    # on ONE channel (see a_taps), and that channel's task
                    # queue is SHIM_TASK_QUEUE deep -- overrunning it HANGS
                    # rather than diagnoses, the same limit a_split windows
                    # for. Await every SHIM_TASK_QUEUE-th fill so no more than
                    # that many are ever outstanding.
                    bounded = (
                        len(taps) > SHIM_TASK_QUEUE and (i + 1) % SHIM_TASK_QUEUE == 0
                    )
                    a_prods[r].fill(A, tap, group=group, wait=wait or bounded)

        def issue_b(mega_col, active_cols, group):
            for c in range(active_cols):
                b_prods[c].fill(B, b_tap(mega_col, c), group=group)

        def issue_c(mega_col, active_cols, mbs, group):
            for c in range(active_cols):
                for tap in c_taps(mega_col, c, mbs):
                    c_conses[c].drain(C, tap, group=group, wait=True)

        def emit_unsplit():
            pending = []
            for mega_col, active_cols in blocks:
                # C in its own group, issued first and retired last: it is an
                # S2MM that waits on the cores, so keeping it outstanding is
                # what overlaps compute with write-back, and it must not share
                # a group with the fills it depends on.
                tg_c = TaskGroup()
                issue_c(mega_col, active_cols, all_mb, tg_c)
                tg_f = TaskGroup()
                issue_a(mega_col, all_mb, tg_f)
                issue_b(mega_col, active_cols, tg_f)

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
                issue_b(mega_col, active_cols, tg_b)

                # The leg that did NOT split is still one task for the whole
                # block -- its single descriptor already spans every mega_row,
                # so re-issuing it per window would transfer the block twice.
                # It stays live alongside the windows and retires with them.
                tg_whole = TaskGroup()
                if not c_split:
                    issue_c(mega_col, active_cols, all_mb, tg_whole)
                if not a_split:
                    issue_a(mega_col, all_mb, tg_whole)

                for w in range(0, n_units, MB_WINDOW):
                    mbs = all_mb[w : w + MB_WINDOW]
                    tg_w = TaskGroup()
                    if c_split:
                        issue_c(mega_col, active_cols, mbs, tg_w)
                    if a_split:
                        # wait=True: the await is what makes this window's
                        # descriptors reusable by the next.
                        issue_a(mega_col, mbs, tg_w, wait=True)
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
            [f.prod() for f in a_l3l2_fifos],
            [f.prod() for f in b_l3l2_fifos],
            [f.cons() for f in c_l2l3_fifos],
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
