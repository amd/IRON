# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field
from typing import Any

import numpy as np
from aie.iron import ObjectFifo
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Extent, In, Operator, Out, auto, optional, param
from iron.common.testing import Case, Testing
from iron.common.tiling import DMA_BD_MAX_WRAP, Access, granule_elements, split_run


class Repeat(Operator):
    """AIE-accelerated repeat-interleave operator: a memtile pass-through of
    ``tile_size`` elements, no cores.

    The repeat is entirely in the runtime sequence's descriptors: the input
    is re-read ``repeat`` times and the output interleaved. The input is
    ``(rows, cols)`` or a stack ``(rows, seq, cols)``, repeated along its
    first axis either way; a row is ``seq * cols`` elements.
    """

    # rows, cols, repeat, tile_size. The sequence splits cols into chunks
    # <= 1023 by the smallest divisor that gets under the hardware limit, so
    # cols on either side of 1023 take different paths and both need
    # covering. The llama arm is the shape the only caller dispatches:
    # n_kv_groups=8 groups expanded to n_heads=32 over a max_seq_len=2048
    # context of head_dim=64, i.e. repeat=4 with cols=2048*64.
    #
    # Repeat moves data and computes nothing, so the gate is exact equality.
    # A tolerance would accept a permutation that reads the wrong group,
    # which is the failure mode here: a misrouted KV group is numerically
    # plausible.
    test = Testing(
        [
            Case(dict(rows=8, cols=64, repeat=4, tile_size=None)),
            Case(dict(rows=8, cols=512, repeat=4, tile_size=64)),
            Case(dict(rows=4, cols=1024, repeat=2, tile_size=None)),
            Case(dict(rows=4, cols=2048, repeat=2, tile_size=None), extensive=True),
            Case(
                dict(rows=8, cols=2048 * 64, repeat=4, tile_size=64),
                extensive=True,
            ),
        ],
        tolerance=Tolerance.exact(),
    )

    rows: int = param()
    cols: int = param()
    repeat: int = param()
    seq: int = param(default=1)  # the stack's middle axis; absent when one
    out_rows: int = param(default=lambda op: op.rows * op.repeat, repr=False)
    tile_size: int = auto(repr=False)  # None: cols
    dtype: Any = field(default=bfloat16, repr=False)

    # Either may be bounded per call: the rows of a matrix (``x[:n]``) or
    # the middle axis of a stack, a KV cache's context (``keys[:, :c]``).
    valid_rows = Extent(rows)
    valid_seq = Extent(seq)

    x = In(rows, optional(seq), cols, dtype=dtype, tile=(tile_size,))
    y = Out(out_rows, optional(seq), cols, dtype=dtype, tile=(tile_size,))

    def validate(self) -> None:
        self.check_derived("out_rows")
        self._cols_split()  # reject an unsplittable cols at construction

    def resolve(self, dev):
        return dataclasses.replace(self, tile_size=self.tile_size or self.cols)

    @property
    def row(self) -> int:
        """Elements per row: ``seq * cols``."""
        return self.seq * self.cols

    def _cols_split(self) -> int:
        """Split a row into cols_split chunks of row // cols_split.

        The chunk length is the innermost descriptor dimension, at most 1023
        and a whole number of 32-bit words; the chunk count is the next
        dimension out, at most 1023. An odd cols has only odd divisors, so
        no split of it is ever word-aligned at bf16; that is reported here
        rather than left to the BD verifier.
        """
        cols = self.row
        granule = granule_elements(self.dtype)
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
        elem_bytes = np.dtype(self.dtype).itemsize
        raise ValueError(
            f"Cannot split cols={cols} at {elem_bytes} bytes/element: need a divisor d "
            f"with cols//d <= 1023, d <= 1023, and cols//d a multiple of {granule} "
            f"({granule} elements = one 32-bit word). No divisor of {cols} satisfies all three."
        )

    def array(self, target) -> list:

        fifo_in = ObjectFifo(self.x.tile, name="fifo_in", depth=2)
        fifo_out = fifo_in.cons().forward(name="fifo_out", depth=2)
        self.x.bind(fifo_in.prod())
        self.y.bind(fifo_out.cons())
        return []

    def sequence(self, rt):
        if self.bound_extents:
            self._bounded_sequence(rt)
            return
        rows, cols, repeat = self.rows, self.row, self.repeat
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
            rt.fill(self.x, input_tap, group=tg)
            rt.drain(self.y, output_tap, group=tg, wait=True)

    def _bounded_sequence(self, rt):
        """The same movement with the bounded axis in a slot of its own,
        patched per call from its word: ``(repeat, rows, seq, cols)`` for a
        bounded stack axis, ``(repeat, rows, chunks, chunk)`` for bounded
        rows. One descriptor each way; a shape that does not fit is refused.
        """
        rows, seq, cols, repeat = self.rows, self.seq, self.cols, self.repeat
        gran = granule_elements(self.dtype)
        if "valid_seq" in self.bound_extents:
            if "valid_rows" in self.bound_extents:
                raise ValueError("Repeat takes one bounded axis, not rows and seq")
            if cols % gran or cols > DMA_BD_MAX_WRAP:
                raise ValueError(
                    f"cols={cols} must be a whole number of words at most "
                    f"{DMA_BD_MAX_WRAP} to bound the stack axis"
                )
            row = seq * cols
            sizes = (repeat, rows, seq, cols)
            in_strides, out_strides = (0, row, cols, 1), (row, repeat * row, cols, 1)
            dim, word = 2, "valid_seq"
        else:
            halves = split_run(self.row, gran)
            if halves is None:
                raise ValueError(
                    f"a row of {self.row} elements does not fit one descriptor"
                )
            chunks, chunk = halves
            sizes = (repeat, rows, chunks, chunk)
            in_strides = (0, self.row, chunk, 1)
            out_strides = (self.row, self.row * repeat, chunk, 1)
            dim, word = 1, "valid_rows"
        with rt.group() as tg:
            rt.fill(
                self.x,
                Access(self.x.elements, 0, sizes, in_strides),
                group=tg,
                size_by={dim: self.value(f"{word}_x")},
            )
            rt.drain(
                self.y,
                Access(self.y.elements, 0, sizes, out_strides),
                group=tg,
                wait=True,
                size_by={dim: self.value(f"{word}_y")},
            )

    def reference(self, x):
        """CPU reference: repeat-interleave along the leading dimension."""
        return reference(x, self.repeat)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(x, repeat):
    """CPU reference: repeat-interleave along the leading dimension (ground truth)."""
    return np.repeat(x, repeat, axis=0)
