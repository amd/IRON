# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field

import numpy as np
import torch
from ml_dtypes import bfloat16

from iron.common.declare import (
    In,
    Operator,
    Out,
    Overlay,
    StreamIn,
    StreamOut,
    dim,
    operator,
    tunable,
)
from iron.common.tiling import Access, granule_elements
from iron.common.utils import DMA_BD_MAX_WRAP


@operator
class RepeatOverlay(Overlay):
    """A memtile pass-through of ``transfer_size`` elements; no cores.

    The repeat is entirely in the runtime sequence's descriptors: the input
    is re-read ``repeat`` times and the output interleaved. ``cols`` sizes
    the pass-through and is therefore overlay-tier.
    """

    cols: int = dim()
    transfer_size: int | None = tunable(None, repr=False)
    dtype: object = field(default=bfloat16, repr=False)

    s = StreamIn(transfer_size, dtype=dtype)
    d = StreamOut(transfer_size, dtype=dtype)

    def tuning(self, dev) -> "RepeatOverlay":
        return dataclasses.replace(self, transfer_size=self.transfer_size or self.cols)

    def design(self, target) -> list:
        from aie.iron import ObjectFifo

        fifo_in = ObjectFifo(self.s.tile, name="fifo_in", depth=2)
        fifo_out = fifo_in.cons().forward(name="fifo_out", depth=2)
        self.s.bind(fifo_in.prod())
        self.d.bind(fifo_out.cons())
        return []


@operator
class Repeat(Operator[RepeatOverlay]):
    """AIE-accelerated repeat-interleave operator"""

    rows: int = dim()
    repeat: int = dim()
    # rows * repeat; derived unless given, since a shape may not be an expression.
    out_rows: int | None = dim(None, repr=False)

    x = In(rows, RepeatOverlay.cols, dtype=RepeatOverlay.dtype, to=RepeatOverlay.s)
    y = Out(
        out_rows, RepeatOverlay.cols, dtype=RepeatOverlay.dtype, from_=RepeatOverlay.d
    )

    @property
    def dtype(self):
        return self.ov.dtype

    def validate(self) -> None:
        expected = self.rows * self.repeat
        if self.out_rows is None:
            self.out_rows = expected
        elif self.out_rows != expected:
            raise ValueError(
                f"out_rows={self.out_rows} is not rows * repeat ({expected})"
            )
        self._cols_split()  # reject an unsplittable cols at construction

    @property
    def cols(self) -> int:
        return self.ov.cols

    def _cols_split(self) -> int:
        """Split cols into cols_split chunks of cols // cols_split.

        The chunk length is the innermost descriptor dimension, at most 1023
        and a whole number of 32-bit words; the chunk count is the next
        dimension out, at most 1023. An odd cols has only odd divisors, so
        no split of it is ever word-aligned at bf16; that is reported here
        rather than left to the BD verifier.
        """
        cols = self.ov.cols
        granule = granule_elements(self.ov.dtype)
        for divisor in range(1, cols + 1):
            if cols % divisor:
                continue
            chunk = cols // divisor
            if (
                chunk <= DMA_BD_MAX_WRAP
                and divisor <= DMA_BD_MAX_WRAP
                and chunk % granule == 0
            ):
                return divisor
        elem_bytes = np.dtype(self.ov.dtype).itemsize
        raise ValueError(
            f"Cannot split cols={cols} at {elem_bytes} bytes/element: need a divisor d "
            f"with cols//d <= 1023, d <= 1023, and cols//d a multiple of {granule} "
            f"({granule} elements = one 32-bit word). No divisor of {cols} satisfies all three."
        )

    def design(self, rt):
        rows, cols, repeat = self.rows, self.ov.cols, self.repeat
        cols_split = self._cols_split()
        chunk = cols // cols_split
        # The chunk length is innermost so the contiguous run is the innermost
        # dimension; the chunk count sits outside it. The input's outermost
        # (iteration) dimension re-reads the whole matrix ``repeat`` times with
        # a zero stride; the output's interleaves.
        input_tap = Access(
            self.x.elements, 0, (repeat, rows, cols_split, chunk), (0, cols, chunk, 1)
        )
        output_tap = Access(
            self.y.elements,
            0,
            (repeat, rows, cols_split, chunk),
            (cols, cols * repeat, chunk, 1),
        )
        with rt.group() as tg:
            rt.fill(self.ov.s, (self.x, input_tap), group=tg)
            rt.drain(self.ov.d, (self.y, output_tap), group=tg, wait=True)

    def reference(self, x):
        """CPU reference: repeat-interleave along the leading dimension."""
        return reference(x, self.repeat)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(x, repeat):
    """CPU reference: repeat-interleave along the leading dimension (ground truth)."""
    return x.repeat_interleave(repeat, dim=0)
