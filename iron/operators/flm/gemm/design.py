# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""bf16 GEMM over a 4-row compute-tile grid, as wide as the device.

The GEMM ``F.linear`` runs for more than one row. Same dataflow as
``iron.operators.gemm`` -- A broadcast along each compute row, B down each
column, C joined through the memtile -- but with a fixed m tile, B read as
stored or quantized to bfp16ebs8 and pre-packed into consumption order, an
activation and clamp fused into the C drain, and asymmetric tile buffering so
the A tile and the accumulator need not share a height.

README.md has the per-choice breakdown against both the shipped FastFlowLM
overlay and ``iron.operators.GEMM``.

The constants below are the single source of truth: ``op.py`` passes them to
the ``fused_mm`` kernel factory, so the C++ and the dataflow cannot drift apart.

The array itself is ``GEMM.Array.build`` and the runtime sequence is
``GEMM.sequence`` in ``op.py``; this module keeps the geometry, the L1 and
memtile budget helpers and the parameter-buffer layout they and
the shipped overlay (``iron/tests/common/shipped.py``) share.
"""

from enum import StrEnum
from typing import NamedTuple

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.dialects.aie import (
    get_target_model,
)
from aie.utils import bfp

# GEMM tiling per compute tile, and the register tiling inside it. K_TILE is
# the default for GEMM's k_tile field.
M_TILE, K_TILE = 64, 512
# 64 doubles A fetches but gives the mmul colA=8 instead of 4.
N_TILE_DEFAULT = 64
# How much of K one compute tile holds at a time, per n width. It is a fixed
# L1 budget split two ways, passed to the kernel as its ``chunk_k``. n=256 is
# absent because its f32 accumulator alone (M_TILE*256*4) fills all of L1.
CT_MAX_K_FOR_N = {16: 16, 32: 32, 64: 128, 128: 32}
# Register tiling, shared by both architectures. pack_B, the stream-dimension
# lists and gather_dims all key off these; changing one alone is silently
# wrong.
R, S, T = 8, 8, 8


def compute_rows(dev):
    """Compute-tile rows: the array less the shim row and the memtile rows."""
    tm = get_target_model(dev.resolve())
    return tm.rows() - 1 - tm.get_num_mem_tile_rows()


CT_OUT_LEN = 512  # the core's C slice, streamed out in chunks this size
C_DEPTH = 2  # C fifo depth; also the core-body unroll
B_DEPTH = 2  # the deepest L1 B ring the budget below tries
A_DEPTH = 2
# L1 bytes reserved for the core's stack: past the device default of 1024,
# the most aiecc measures a build needing is 2304 (AIE2P's bf16 B^T kernel).
STACK_SIZE = 2560
# L1 bytes the activation LUT tables occupy, which the buffer budget must not
# hand out either. On AIE2 the activations come from lut_based_ops, whose
# tables are bank-pinned in local memory; AIE2P computes its activations and
# links no tables, so it reserves nothing.
LUT_STATIC_SIZE = 5248


def l1_budget(dev, epilogue_modes):
    """Local memory the buffer sizing may spend on this device.

    Args:
        dev: The device the array is built for.
        epilogue_modes: The activations compiled in. Without one the kernel
            links no LUT tables, so their bytes go to the buffers.
    """
    budget = get_target_model(dev.resolve()).get_local_memory_size()
    activated = any(Epilogue(m) is not Epilogue.NONE for m in epilogue_modes)
    return budget - (LUT_STATIC_SIZE if dev.arch == AIEArch.AIE2 and activated else 0)


# B does not go through an ObjectFifo. A fifo's memtile BDs are part of the
# device configuration, so holding a column-block there would put K (the buffer
# size) and M (the replay count) into the one xclbin every shape shares.
# Instead the memtile holds a fixed pool of k-block slots and the runtime
# sequence, which is per shape, programs both of its B channels.
#
# Slots in the pool, each one k-block. Bounded by the BDs a memtile channel's
# parity half has left after the static objectfifo BDs, and, below that, by
# what the memtile has left after A and C; see GEMM.Array.build().
B_MAX_SLOTS = 8


class _Slab(NamedTuple):
    """A run of row-block units the sequence arms B for at once; see
    GEMM.sequence().
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

    def apply(self, C, clamp=None):
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
        return C if clamp is None else np.clip(C, clamp[0], clamp[1])


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


def _b_bytes(elems, bfp16_b):
    """Bytes B occupies in L1/L2. bfp16ebs8 packs 8 values as 8 mantissa bytes
    plus one shared exponent; bf16 is a plain 2 bytes each.
    """
    if not bfp16_b:
        return elems * 2
    assert elems % bfp.BLOCK == 0
    return elems // bfp.BLOCK * bfp.BLOCK_BYTES


def _default_l1(n_tile, ct_max_k, b_elem_bytes, budget, m_chunk=1, k_tile=K_TILE):
    """Pick the largest working set that fits: (A-tile height, L1 B depth).

    Deeper B first, then the tallest A that still fits, since colA is worth
    far more than B's L1 prefetch. ``budget`` is the whole local memory; the
    stack comes off it here so callers can keep passing the raw size. A depth
    divides the ``k_tile // ct_max_k`` B chunks a k step consumes, since the
    core walks the ring that many at a time.
    """
    budget -= STACK_SIZE
    # m_chunk accumulators, since the core holds a B chunk across that many
    # row-blocks. The only term that scales with it.
    acc = m_chunk * M_TILE * n_tile * 4
    cout = CT_OUT_LEN * 2 * C_DEPTH
    for b_depth in (B_DEPTH, 1):
        if (k_tile // ct_max_k) % b_depth:
            continue
        b = int(ct_max_k * n_tile * b_elem_bytes) * b_depth
        for t_ma in (M_TILE, M_TILE // 2, M_TILE // 4):
            if t_ma < 2 * R:
                continue
            a = (2 * R * ct_max_k) * (t_ma // R // 2) * 2 * A_DEPTH
            if acc + a + b + cout <= budget:
                return t_ma, b_depth
    raise ValueError(
        f"flm.GEMM: tile_n ({n_tile}) leaves no A tile fitting L1 at ct_max_k "
        f"({ct_max_k})"
    )


def _b_depth_for(
    t_ma, n_tile, ct_max_k, b_elem_bytes, budget, m_chunk=1, k_tile=K_TILE
):
    """Deepest B fifo depth that fits L1 alongside an explicit A-tile height,
    and divides the ``k_tile // ct_max_k`` B chunks a k step consumes.

    ``_default_l1``'s depth is chosen with its own t_ma, which need not fit a
    caller-overridden one. Raise rather than reuse a depth that does not fit.
    """
    budget -= STACK_SIZE
    # Same terms as _default_l1; acc is the only one that scales with m_chunk.
    acc = m_chunk * M_TILE * n_tile * 4
    cout = CT_OUT_LEN * 2 * C_DEPTH
    a = (2 * R * ct_max_k) * (t_ma // R // 2) * 2 * A_DEPTH
    for b_depth in (B_DEPTH, 1):
        if (k_tile // ct_max_k) % b_depth:
            continue
        b = int(ct_max_k * n_tile * b_elem_bytes) * b_depth
        if acc + a + b + cout <= budget:
            return b_depth
    raise ValueError(
        f"flm.GEMM: tile_ma ({t_ma}) does not fit L1 at tile_n ({n_tile}) and "
        f"ct_max_k ({ct_max_k}); even single-buffered B overflows the budget"
    )
