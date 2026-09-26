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

The array itself is ``GEMM.array`` and the runtime sequence is
``FLMGEMM.design`` in ``op.py``; this module keeps the geometry, the L1
budget helpers and the parameter-buffer layout they and ``shipped.py``
share.
"""

from enum import StrEnum

from aie.dialects._aie_enum_gen import AIEArch
from aie.dialects.aie import (
    get_target_model,  # pyright: ignore[reportAttributeAccessIssue]  # not in _aie.pyi
)

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
# L1 bytes the activation LUT tables occupy, which the buffer budget must not
# hand out either. On AIE2 the activations come from lut_based_ops, whose
# tables are bank-pinned in local memory; AIE2P computes its activations and
# links no tables, so it reserves nothing. The tables grew past the slack the
# budget happened to leave when mlir-aie reorganized the kernel library, which
# is why this is reserved explicitly rather than left to chance.
LUT_STATIC_SIZE = 5248


def l1_budget(dev):
    """Local memory the buffer sizing may spend on this device."""
    budget = get_target_model(dev.resolve()).get_local_memory_size()
    return budget - (LUT_STATIC_SIZE if dev.arch == AIEArch.AIE2 else 0)


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
