# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""bf16 GEMM over a 4-row compute-tile grid, as wide as the device.

The GEMM ``F.linear`` runs for more than one row. Same dataflow as
``iron.operators.gemm`` -- A broadcast along each compute row, B down each
column, C joined through the memtile -- but with a fixed m tile, B read as
stored or quantized to bfp16ebs8 and pre-packed into consumption order, an
activation fused into the C drain, and asymmetric tile buffering so
the A tile and the accumulator need not share a height.

README.md has the per-choice breakdown against both the shipped FastFlowLM
overlay and ``iron.operators.GEMM``.

The constants below are the single source of truth: ``op.py`` passes them to
the ``fused_mm`` kernel factory, so the C++ and the dataflow cannot drift apart.

The array itself is ``ProjectionGEMM.build`` and the runtime sequence is
``ProjectionGEMM.sequence`` in ``op.py``; this module keeps the geometry, the L1 and
memtile budget helpers and the parameter-buffer layout they and
the shipped overlay (``iron/tests/support/shipped.py``) share.
"""

from collections.abc import Callable
from enum import StrEnum
from typing import NamedTuple

import numpy as np
from aie.dialects.aie import (
    get_target_model,
)
from aie.utils import bfp
from aie.utils.compile.jit.params import divisors

# GEMM tiling per compute tile, and the register tiling inside it. K_TILE is
# the default for ProjectionGEMM's k_tile field.
M_TILE, K_TILE = 64, 512
# 64 doubles A fetches but gives the mmul colA=8 instead of 4.
N_TILE_DEFAULT = 64
# The n widths a compute tile takes. n=256 is absent because its f32
# accumulator alone (M_TILE*256*4) fills all of L1.
TILE_NS = (16, 32, 64, 128)
# Register tiling, shared by both architectures. pack_B, the stream-dimension
# lists and gather_dims all key off these; changing one alone is silently
# wrong.
R, S, T = 8, 8, 8


def compute_rows(dev) -> int:
    """Compute-tile rows: the array less the shim row and the memtile rows."""
    tm = get_target_model(dev.resolve())
    return tm.rows() - 1 - tm.get_num_mem_tile_rows()


CT_OUT_LEN = 512  # the core's C slice, streamed out in chunks this size
C_DEPTH = 2  # C fifo depth; also the core-body unroll
# C's joins per column, one per shim S2MM channel: each half of the core rows
# takes its own range of row blocks.
C_JOINS = 2
B_DEPTH = 2  # the deepest L1 B ring the budget below tries
A_DEPTH = 2
# B does not go through an ObjectFifo. A fifo's memtile BDs are part of the
# device configuration, so holding a column-block there would put K (the buffer
# size) and M (the replay count) into the one xclbin every shape shares.
# Instead the memtile holds a fixed pool of k-block slots and the runtime
# sequence, which is per shape, programs both of its B channels.
#
# Slots in the pool, each one k-block. Bounded by the BDs a memtile channel's
# parity half has left after the static objectfifo BDs, and, below that, by
# what the memtile has left after A and C; see ProjectionGEMM.build().
B_MAX_SLOTS = 8


class _Slab(NamedTuple):
    """A run of row-block units the sequence arms B for at once; see
    ProjectionGEMM.sequence().
    """

    first: int  # the first unit
    units: int
    b_resident: bool
    b_slots: int  # memtile slots walked
    b_uses: int  # units served per fill


class Epilogue(StrEnum):
    """Activation folded into the C drain.

    Declaration order is the wire format: it is both the kernel's
    epilogue mode argument and the shipped overlay's ``output_mode``.
    """

    NONE = "none"
    GELU = "gelu"
    SILU = "silu"
    SIGMOID = "sigmoid"

    @property
    def mode(self) -> int:
        """The integer the kernel and the shipped overlay both select on."""
        return list(Epilogue).index(self)

    def apply(self, C):
        """This output stage alone, on an already-accumulated ``C``: what a
        test of the epilogue without the accumulation compares against
        (test.py's, on the shipped image's own accumulator).

        ``gelu`` is the sigmoid approximation ``x * sigmoid(1.702x)``, the
        kernel's: not torch's erf-exact gelu, and not the tanh approximation
        the standalone GELU operator uses.
        """
        match self:
            case Epilogue.GELU:
                C = C * _sigmoid(np.float32(1.702) * C)
            case Epilogue.SILU:
                C = C * _sigmoid(C)
            case Epilogue.SIGMOID:
                C = _sigmoid(C)
        return C


def _sigmoid(x):
    """``1 / (1 + exp(-x))`` in float32, rounded once back to ``x``'s dtype."""
    f = x.astype(np.float32)
    return (1 / (1 + np.exp(-f))).astype(x.dtype)


class Rounding(StrEnum):
    """Rounding for every f32->bf16 conversion.

    conv_even by default: truncation biases every conversion the same way, so
    the error accumulates over the K reduction. floor matches the overlay.
    """

    CONV_EVEN = "conv_even"
    FLOOR = "floor"


class Gelu(StrEnum):
    """Arithmetic of the gelu epilogue, ``x * sigmoid(1.702x)``.

    fp32 by default: the activation runs on the f32 accumulator and rounds once.
    bf16_steps reproduces the shipped overlay: it rounds the accumulator to
    bf16 and rounds again after each step of the activation. With
    ``Rounding.FLOOR`` the result matches the overlay bit for bit.
    """

    FP32 = "fp32"
    BF16_STEPS = "bf16_steps"


def _b_bytes(elems: int, bfp16_b: bool) -> int:
    """Bytes B occupies in L1/L2. bfp16ebs8 packs 8 values as 8 mantissa bytes
    plus one shared exponent; bf16 is a plain 2 bytes each.
    """
    if not bfp16_b:
        return elems * 2
    assert elems % bfp.BLOCK == 0
    return elems // bfp.BLOCK * bfp.BLOCK_BYTES


def k_slices(k_tile: int) -> tuple[int, ...]:
    """The k slices a compute tile can hold of a ``k_tile``, deepest first:
    ``k_tile`` and its halvings down to the mmul's ``S``.
    """
    return divisors(k_tile, of=k_tile, step=S)


def l1_tiles(
    n_tile: int,
    b_elem_bytes: float,
    budget: int,
    frame: Callable[[int, int], int],
    m_chunk: int = 1,
    k_tile: int = K_TILE,
    t_ma: int | None = None,
    ct_k: int | None = None,
) -> tuple[int, int, int]:
    """The working set that fits L1: (k slice, A-tile height, L1 B depth).

    Double-buffered B first, then the deepest k slice, then the tallest A
    that still fits. Each k slice reloads and stores the f32 accumulator, so
    a deeper one runs the kernel's macs longer between them: on npu1, at
    n=16, ct_k 128 takes 1932 cycles a call where 16 takes 4254, while the
    A height moves nothing. ``t_ma`` and ``ct_k`` fix their values instead. A
    depth divides the ``k_tile // ct_k`` B chunks a k step consumes, since
    the core walks the ring that many at a time. ``budget`` is the whole
    local memory; ``frame(height, ct_k)``, what the core's kernel holds
    beside its buffers at an A band ``height`` and that k slice (its data,
    AIE2's LUT tables among it, and stack), comes off it here.
    """
    # m_chunk accumulators, since the core holds a B chunk across that many
    # row-blocks. The only term that scales with it.
    acc = m_chunk * M_TILE * n_tile * 4
    cout = CT_OUT_LEN * 2 * C_DEPTH
    heights = (M_TILE, M_TILE // 2, M_TILE // 4) if t_ma is None else (t_ma,)
    slices = k_slices(k_tile) if ct_k is None else (ct_k,)
    for b_depth in (B_DEPTH, 1):
        for slice_k in slices:
            if (k_tile // slice_k) % b_depth:
                continue
            b = int(slice_k * n_tile * b_elem_bytes) * b_depth
            for height in heights:
                a = (2 * R * slice_k) * (height // R // 2) * 2 * A_DEPTH
                if acc + a + b + cout + frame(height, slice_k) <= budget:
                    return slice_k, height, b_depth
    fixed = ", ".join(
        f"{name} ({value})"
        for name, value in (("tile_ma", t_ma), ("ct_k", ct_k))
        if value is not None
    )
    raise ValueError(
        f"flm.ProjectionGEMM: tile_n ({n_tile}) does not fit L1"
        + (f" at {fixed}" if fixed else "")
        + "; even single-buffered B overflows the budget"
    )
