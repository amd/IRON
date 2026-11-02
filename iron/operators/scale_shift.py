# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Scalar affine transforms using mlir-aie's two-phase scale_shift kernel."""

import numpy as np
from aie.iron import Buffer, ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise
from aie.utils.compile.jit.params import param
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp, UnaryElementwise
from iron.common.testing import Case, Testing


class ScaleShift(UnaryElementwise):
    """Compute ``bf16(bf16(x * bf16(scale)) + bf16(shift))`` on the device."""

    scale: float = param(default=1.0, array=True)
    shift: float = param(default=0.0, array=True)
    tile_cap = 1024
    default_tile = 1024

    test = Testing(
        [
            Case(dict(size=2048, tile_size=1024, scale=0.25, shift=1.0), lower=True),
            Case(dict(size=1 << 20, tile_size=1024, scale=0.25, shift=1.0), bench=True),
        ],
        draw=lambda op: dict(centered=(op.x,)),
    )

    def compatible(self) -> None:
        super().compatible()
        if self.tile_size != 1024:
            raise ValueError("ScaleShift: the upstream kernel requires tile_size=1024")

    def kernel(self):
        return eltwise.mul_add(self.tile_size)

    def build(self) -> Built:
        kernel = self.kernel()
        sources = [ObjectFifo(self.x.obj_type, depth=1) for _ in range(self.cores)]
        results = [ObjectFifo(self.y.obj_type, depth=1) for _ in range(self.cores)]
        rtps = [Rtp([self.count]) for _ in range(self.cores)]

        def core(src, dst, factor, bias, scratch, kernel, rtp):
            for _ in range_(rtp.read()[self.count]):
                x, y = src.acquire(1), dst.acquire(1)
                kernel(x, factor, scratch, 1)
                kernel(scratch, bias, y, 0)
                src.release(1)
                dst.release(1)

        workers = []
        for src, dst, rtp in zip(sources, results, rtps):
            factor = Buffer(initial_value=np.full(1024, self.scale, bfloat16))
            bias = Buffer(initial_value=np.full(1024, self.shift, bfloat16))
            scratch = Buffer(np.ndarray[(1024,), np.dtype[bfloat16]])
            workers.append(
                Worker(
                    core, [src.cons(), dst.prod(), factor, bias, scratch, kernel, rtp]
                )
            )
        self.x.bind([s.prod() for s in sources])
        self.y.bind([s.cons() for s in results])
        return Built(workers, rtps)

    def reference(self, x) -> np.ndarray:
        scaled = (np.asarray(x, np.float32) * np.float32(bfloat16(self.scale))).astype(
            bfloat16
        )
        return (scaled.astype(np.float32) + np.float32(bfloat16(self.shift))).astype(
            bfloat16
        )

    def tolerance(self):
        return Tolerance.exact(note="the two upstream bf16 operations round separately")

    def judge(self, inputs, written, tolerance=None, expected=None):
        return Operator.judge(self, inputs, written, tolerance, expected)
