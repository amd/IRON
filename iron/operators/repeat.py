# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field
from typing import Any

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import ObjectFifo, TaskGroup
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Extent,
    In,
    Operator,
    Out,
    Unresolvable,
    auto,
    OptionalDim,
    param,
)
from iron.common.design import BdLimits
from iron.common.testing import Case, Testing


class Repeat(Operator):
    """AIE-accelerated repeat-interleave operator: a memtile pass-through of
    ``tile_size`` elements, no cores.

    The repeat is entirely in the runtime sequence's descriptors: the input
    is re-read ``repeat`` times and the output interleaved. The input is
    ``(rows, cols)`` or a stack ``(rows, seq, cols)``, repeated along its
    first axis either way; a row is ``seq * cols`` elements.
    """

    # rows, cols, repeat, tile_size. A row is one run the sequence splits
    # for the descriptor's two innermost slots, so rows either side of one
    # slot's reach (2046 bf16 elements) take different splits and both need
    # covering; the last is a row of 2048 * 64, a long context of 64-wide
    # heads, far past it.
    #
    # Repeat moves data and computes nothing, so the gate is exact equality.
    # A tolerance would accept a permutation that reads the wrong row, which
    # is the failure mode here: a misrouted row is numerically plausible.
    test = Testing(
        [
            Case(dict(rows=8, cols=64, repeat=4, tile_size=None)),
            Case(
                dict(rows=8, cols=64, repeat=4, tile_size=None, dtype=np.int32),
                id="int32",
                lower=True,
            ),
            Case(dict(rows=8, cols=512, repeat=4, tile_size=64)),
            Case(dict(rows=4, cols=1024, repeat=2, tile_size=None)),
            Case(dict(rows=4, cols=2048, repeat=2, tile_size=None), extensive=True),
            Case(
                dict(rows=8, cols=2048 * 64, repeat=4, tile_size=64),
                extensive=True,
                bench=True,
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

    x = In(rows, OptionalDim(seq), cols, dtype=dtype, tile=(tile_size,))
    y = Out(out_rows, OptionalDim(seq), cols, dtype=dtype, tile=(tile_size,))

    def validate(self) -> None:
        self.check_derived("out_rows")

    def resolve(self, dev):
        # A row is one run over the descriptor's two innermost dimensions.
        shim = BdLimits.of(dev, 0, 0)
        row, gran = self.seq * self.cols, shim.granule(self.dtype)
        if shim.factor(row, gran) is None:
            raise Unresolvable(
                f"Cannot split cols={row} for one descriptor: a row must "
                f"factor into at most {shim.wrap} runs of at most "
                f"{shim.wrap} {gran}-element words each"
            )
        return dataclasses.replace(self, tile_size=self.tile_size or self.cols)

    def array(self, target) -> list:
        fifo_in = ObjectFifo(self.x.tile, name="fifo_in", depth=2)
        fifo_out = fifo_in.cons().forward(name="fifo_out", depth=2)
        self.x.bind(fifo_in.prod())
        self.y.bind(fifo_out.cons())
        return []

    def sequence(self, rt):
        """The input re-read ``repeat`` times by the iteration slot's zero
        stride, the output interleaved, one descriptor each way. A row is
        one run split over the two innermost slots; a bounded axis is D2,
        patched per call from its word: the rows' (the split row beneath
        them), or the stack's, ``(repeat, seq, rows, cols)``.
        """
        rows, seq, cols, repeat = self.rows, self.seq, self.cols, self.repeat
        shim = BdLimits.of(self.dev, 0, 0)
        row, gran = seq * cols, shim.granule(self.dtype)
        bound = self.bound_extents
        x = TensorAccessPattern.full((rows, seq, cols))
        y = TensorAccessPattern.full((rows, repeat, seq, cols))
        if "valid_seq" in bound:
            if "valid_rows" in bound:
                raise ValueError("Repeat takes one bounded axis, not rows and seq")
            # A patched length bounds D2 (the dimension inside the
            # iteration), so the stack axis goes there and the rows inside
            # it: the same bytes both ways, in (copy, seq, row) order.
            taps = (x.permute((1, 0, 2)).repeat(repeat), y.permute((1, 2, 0, 3)))
            dim, word = 1, "valid_seq"
        else:
            halves = shim.factor(row, gran)
            assert halves is not None  # resolve() refused a row without one
            chunk = halves[1]
            taps = (
                x.merge(1).split(1, chunk).repeat(repeat),
                y.merge(2).permute((1, 0, 2)).split(2, chunk),
            )
            dim, word = 1, "valid_rows"
        tg = TaskGroup()
        rt.fill(
            self.x,
            taps[0],
            group=tg,
            size_by={dim: self.value(f"{word}_x")} if bound else None,
        )
        rt.drain(
            self.y,
            taps[1],
            group=tg,
            wait=True,
            size_by={dim: self.value(f"{word}_y")} if bound else None,
        )
        tg.finish()

    def ops(self) -> int:
        return 0  # a data mover: its figure is bandwidth

    def reference(self, x):
        """Each row of the leading dimension repeated ``repeat`` times in place."""
        # A DMA pattern: no kernel, so no contract to take it from.
        return np.repeat(x, self.repeat, axis=0)
