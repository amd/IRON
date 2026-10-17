# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from typing import Any

import numpy as np
from aie.iron import Buffer, ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import reduce
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Auto, Built, In, Operand, Operator, Out, Param, Rtp, Value
from iron.common.testing import Case, Testing

# A tile's elements: the largest the kernel's vector loop takes in one call.
TILE = 4096


class ReduceMax(Operator):
    """The largest of ``size`` elements, on one core: each tile's maximum
    (``reduce.reduce_max``) folded into a running one (``compute_max``).
    The output is a shim transfer's 4 bytes, every element the maximum.
    """

    test = Testing(
        [
            Case(dict(size=4096), lower=True),
            Case(dict(size=16 * 4096), bench=True),
            Case(dict(size=4096 * 3, dtype=np.int32), id="int32"),
        ],
        draw=lambda op: dict(normal=(op.x,)),
    )

    size: int = Param()
    dtype: Any = Param(default=bfloat16, repr=False)
    tile_size: int = Auto()
    # The elements of the output's 4 bytes.
    out_size: int = Param(derive=lambda op: 4 // np.dtype(op.dtype).itemsize)

    # The tiles after the first.
    count = Value(derive=lambda op: op.size // op.tile_size - 1)

    x = In(size, dtype=dtype, obj_type=(tile_size,))
    y = Out(out_size, dtype=dtype, obj_type=(out_size,))

    def validate(self) -> None:
        self.check_derived("out_size")

    def resolve(self, dev):
        tile = self.tile_size or min(self.size, TILE)
        return dataclasses.replace(self, tile_size=tile)

    def compatible(self) -> None:
        if self.size % self.tile_size:
            raise ValueError(
                f"ReduceMax: {self.size} elements are no whole number of "
                f"{self.tile_size}-element tiles"
            )

    class Array(Operator.Array):
        dtype: Any
        tile_size: int
        out_size: int
        count: Value
        x: Operand
        y: Operand

        def build(self) -> Built:
            tile_max = reduce.reduce_max(tile_size=self.tile_size, dtype=self.dtype)
            fold = reduce.compute_max(dtype=self.dtype)
            one = np.ndarray[(self.out_size,), np.dtype[self.dtype]]
            of_x = ObjectFifo(self.x.obj_type, depth=2)
            of_y = ObjectFifo(self.y.obj_type, depth=1)
            rtp = Rtp([self.count])
            size, out = self.tile_size, self.out_size

            def core_fn(of_x, of_y, tile_max, fold, running, held, rtp):
                n = rtp.read()[self.count]
                x = of_x.acquire(1)
                tile_max(x, running, size)
                of_x.release(1)
                for _ in range_(n):
                    x = of_x.acquire(1)
                    tile_max(x, held, size)
                    fold(running, held, running)
                    of_x.release(1)
                y = of_y.acquire(1)
                for k in range(out):
                    y[k] = running[0]
                of_y.release(1)

            worker = Worker(
                core_fn,
                [
                    of_x.cons(),
                    of_y.prod(),
                    tile_max,
                    fold,
                    Buffer(one, initial_value=np.zeros(self.out_size, self.dtype)),
                    Buffer(one, initial_value=np.zeros(self.out_size, self.dtype)),
                    rtp,
                ],
            )
            self.x.bind(of_x.prod())
            self.y.bind(of_y.cons())
            return Built([worker], [rtp])

    def ops(self) -> int:
        return self.size

    def reference(self, x):
        """The maximum, in every element of the output."""
        return np.full(self.out_size, np.max(x), self.dtype)

    def tolerance(self) -> Tolerance:
        return Tolerance.exact(note="a selection")
