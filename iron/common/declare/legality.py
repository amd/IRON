# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whether one shim descriptor can be issued in one DMA direction.

The slot rules are :mod:`iron.common.tiling`'s (read from mlir-aie's
``verifyStridesWraps`` and the shim BD fields). What this adds is the
direction: a read (MM2S) may re-read, in the iteration slot only; a write
(S2MM) may not, since writing one address twice from one stream keeps the
last and loses the rest.
"""

from __future__ import annotations

import enum

import numpy as np

from ..tiling import (
    DMA_BD_MAX_WRAP,
    Access,
    granule_elements,
    max_stride_elements,
)

_ITER_MAX = 64  # 6-bit iteration wrap, biased by one


class Direction(enum.Enum):
    """Which way a shim channel moves data."""

    MM2S = "mm2s"  # DDR to the array: a read
    S2MM = "s2mm"  # the array to DDR: a write


def access_legal(acc: Access, direction: Direction, dtype) -> str | None:
    """Why ``acc`` cannot be one shim descriptor in ``direction``; ``None`` if it can."""
    gran = granule_elements(dtype)
    if acc.offset % gran:
        return f"offset {acc.offset} is not a whole {gran}-element granule"
    it, d2, d1, d0 = acc.sizes
    it_s, d2_s, d1_s, d0_s = acc.strides
    if direction is Direction.S2MM:
        for n, s in zip(acc.sizes, acc.strides):
            if n > 1 and s == 0:
                return "a write cannot repeat: a zero stride rewrites one address"
    if (it, d2, d1) == (1, 1, 1) and d0_s == 1:
        # One linear transfer: the 32-bit length field, any run.
        return None if d0 % gran == 0 else f"a run of {d0} is not whole granules"
    if d0_s != 1:
        return f"the innermost stride is {d0_s}; the shim's is 1"
    if d0 % gran or d0 // gran > DMA_BD_MAX_WRAP:
        return f"innermost size {d0} is not at most {DMA_BD_MAX_WRAP} whole granules"
    if d1 > DMA_BD_MAX_WRAP:
        return f"d1 size {d1} exceeds {DMA_BD_MAX_WRAP}"
    if it > _ITER_MAX:
        return f"iteration size {it} exceeds {_ITER_MAX}"
    for name, n, s in (("d2", d2, d2_s), ("d1", d1, d1_s)):
        if n > 1 and s < 1:
            return (
                f"{name} has size {n} at stride {s}; only the iteration slot re-reads"
            )
    if it > 1 and it_s < 0:
        return f"iteration stride {it_s} is negative"
    max_stride = max_stride_elements(np.int8) // 4 * gran
    for name, n, s in (("iteration", it, it_s), ("d2", d2, d2_s), ("d1", d1, d1_s)):
        if n > 1 and (s % gran or s > max_stride):
            return f"{name} stride {s} is not a whole granule within the 20-bit field"
    span = acc.offset + sum((n - 1) * s for n, s in zip(acc.sizes, acc.strides)) + 1
    if span > acc.elements:
        return f"the descriptor spans {span} elements of a buffer of {acc.elements}"
    return None
