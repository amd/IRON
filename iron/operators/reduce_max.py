# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A streaming maximum over an array, using mlir-aie's tile reduction."""

import numpy as np
from aie.dialects import arith
from aie.iron import Buffer, In, ObjectFifo, Out, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import reduce_max
from aie.utils.compile.jit.params import divisors, param, per_call, tunable
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing


def _tiles(op) -> int:
    if op.valid <= 0 or op.valid % op.tile_size:
        raise ValueError(
            "ReduceMax: the valid extent must contain whole, nonempty tiles"
        )
    return op.valid // op.tile_size


class ReduceMax(Operator):
    """Reduce bf16 elements to their maximum, repeated to fill one DMA word."""

    size: int = param()
    tile_size: int = tunable(
        default=1024,
        domain=lambda op, dev, t: divisors(t, of=op.size, step=32, cap=4096),
    )
    valid = per_call(bounds=size)
    count = per_call(derive=_tiles)
    x = In(size, obj_shape=(tile_size,), depth=1)
    y = Out(2, obj_shape=(2,), depth=1)

    test = Testing(
        [
            Case(dict(size=2048, tile_size=1024), lower=True),
            Case(dict(size=1 << 20, tile_size=1024), bench=True),
        ],
        draw=lambda op: dict(centered=(op.x,)),
    )

    def compatible(self) -> None:
        if self.size % self.tile_size or self.tile_size % 32:
            raise ValueError(
                "ReduceMax: size must be whole tiles of 32-element vectors"
            )

    def build(self) -> Built:
        kernel = reduce_max(self.tile_size, dtype=bfloat16)
        source = ObjectFifo(self.x.obj_type, depth=1)
        result = ObjectFifo(self.y.obj_type, depth=1)
        partial = Buffer(np.ndarray[(2,), np.dtype[bfloat16]])
        rtp = Rtp([self.count])

        def core(src, dst, scratch, kernel, rtp):
            out = dst.acquire(1)
            first = src.acquire(1)
            kernel(first, out, self.tile_size)
            src.release(1)
            for _ in range_(1, rtp.read()[self.count]):
                x = src.acquire(1)
                kernel(x, scratch, self.tile_size)
                out[0] = arith.maximumf(out[0], scratch[0])
                src.release(1)
            out[1] = out[0]
            dst.release(1)

        self.x.bind(source.prod())
        self.y.bind(result.cons())
        return Built(
            [Worker(core, [source.cons(), result.prod(), partial, kernel, rtp])], [rtp]
        )

    def reference(self, x):
        return np.full(2, np.max(x), dtype=bfloat16)

    def tolerance(self):
        return Tolerance.exact(note="maximum selects an input element without rounding")
