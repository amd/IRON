# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from typing import Any

import numpy as np
from aie.dialects.aie import AIETileType
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
    Auto,
    Param,
    Built,
    Operand,
)
from iron.common.design import BdLimits
from iron.common.testing import Case, Testing


class Repeat(Operator):
    """AIE-accelerated repeat-interleave: a memtile pass-through, no cores; the
    repeat is all in the runtime sequence's descriptors.
    """

    # Rows either side of one BD slot's reach (2046 elements) split differently.
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
            Case(
                dict(rows=8, cols=2048 * 64, repeat=4, tile_size=64),
                extensive=True,
                bench=True,
            ),
        ],
    )

    rows: int = Param()
    cols: int = Param()
    repeat: int = Param()
    seq: int | None = Param(default=None)  # the stack's middle axis; absent when None
    out_rows: int = Param(derive=lambda op: op.rows * op.repeat, repr=False)
    tile_size: int = Auto(repr=False)  # None: cols
    dtype: Any = Param(default=bfloat16, repr=False)

    valid_rows = Extent(rows)
    valid_seq = Extent(seq)

    x = In(rows, seq, cols, dtype=dtype, obj_type=(tile_size,))
    y = Out(out_rows, seq, cols, dtype=dtype, obj_type=(tile_size,))

    def validate(self) -> None:
        self.check_derived("out_rows")

    def resolve(self, dev):
        # A row is one run over the descriptor's two innermost dimensions.
        shim = BdLimits.of(dev, AIETileType.ShimNOCTile)
        row, gran = (self.seq or 1) * self.cols, shim.granule(self.dtype)
        if shim.factor(row, gran) is None:
            raise Unresolvable(
                f"Cannot split cols={row} for one descriptor: a row must "
                f"factor into at most {shim.wrap} runs of at most "
                f"{shim.wrap} {gran}-element words each"
            )
        return dataclasses.replace(self, tile_size=self.tile_size or self.cols)

    class Array(Operator.Array):
        dtype: Any
        tile_size: int
        x: Operand
        y: Operand

        def build(self) -> Built:
            fifo_in = ObjectFifo(self.x.obj_type, depth=2)
            fifo_out = fifo_in.cons().forward(depth=2)
            self.x.bind(fifo_in.prod())
            self.y.bind(fifo_out.cons())
            return Built([])

    def sequence(self, rt):
        """The input re-read ``repeat`` times by the iteration slot's zero stride,
        the output interleaved, one descriptor each way.
        """
        rows, seq, cols, repeat = self.rows, self.seq or 1, self.cols, self.repeat
        shim = BdLimits.of(self.dev, AIETileType.ShimNOCTile)
        row, gran = seq * cols, shim.granule(self.dtype)
        bound = self.bound_extents
        x = TensorAccessPattern.full((rows, seq, cols))
        y = TensorAccessPattern.full((rows, repeat, seq, cols))
        if "valid_seq" in bound:
            if "valid_rows" in bound:
                raise ValueError("Repeat takes one bounded axis, not rows and seq")
            # A patched length bounds D2, so the stack axis goes there.
            taps = (x.permute((1, 0, 2)).repeat(repeat), y.permute((1, 2, 0, 3)))
            unit, word = rows * cols, "valid_seq"
        else:
            halves = shim.factor(row, gran)
            assert halves is not None  # resolve() refused a row without one
            chunk = halves[1]
            taps = (
                x.merge(1).split(1, chunk).repeat(repeat),
                y.merge(2).permute((1, 0, 2)).split(2, chunk),
            )
            unit, word = row, "valid_rows"
        tg = TaskGroup()
        self.x.fill(
            taps[0],
            group=tg,
            length_parameter=self.value(f"{word}_x") if bound else None,
            length_unit=unit,
        )
        self.y.drain(
            taps[1],
            group=tg,
            wait=True,
            length_parameter=self.value(f"{word}_y") if bound else None,
            length_unit=unit,
        )
        tg.finish()

    def ops(self) -> int:
        return 0  # a data mover: its figure is bandwidth

    def reference(self, x):
        """Each row of the leading dimension repeated ``repeat`` times in place."""
        return np.repeat(x, self.repeat, axis=0)

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()
