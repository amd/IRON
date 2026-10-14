# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise
from ml_dtypes import bfloat16

from iron.common import UnaryElementwise, Value, Param
from iron.common.elementwise import Sweep
from iron.common.testing import Case, Testing


class Clamp(UnaryElementwise):
    """`x` clamped to `[low, high]`, elementwise, the bounds rounded to bf16.

    The bounds are `Value`s each core reads from its runtime parameters, not
    part of the array, so one array serves every pair of bounds.
    """

    test = Testing(
        [
            Sweep(low=-0.75, high=1.25),
            # Bounds of one sign, and one past every input: the identity.
            Case(dict(size=2048, num_aie_columns=1, tile_size=2048, low=0.5, high=1.5)),
            Case(
                dict(size=2048, num_aie_columns=2, tile_size=1024, low=-3e4, high=3e4)
            ),
        ],
        draw=lambda op: dict(centered=(op.x,)),
    )

    low: float = Param(probe=-np.inf)
    high: float = Param(probe=np.inf)

    low_bits = Value(derive=lambda op: op.scalars()[0])
    high_bits = Value(derive=lambda op: op.scalars()[1])

    def validate(self) -> None:
        if not np.float32(self.low) <= np.float32(self.high):
            raise ValueError(f"Clamp: low ({self.low}) exceeds high ({self.high})")

    def compatible(self) -> None:
        super().compatible()
        if self.tile_size % 32:
            raise ValueError(
                f"Clamp: tile_size ({self.tile_size}) is not a whole number of "
                f"32-element vectors"
            )

    def kernel(self):
        return eltwise.clamp(self.tile_size)

    def scalars(self) -> tuple:
        return tuple(
            int(np.array(b, bfloat16).view(np.uint16)) for b in (self.low, self.high)
        )

    def array(self) -> list:
        cores = self.cores
        kernel = self.kernel()
        depth = self.x.l1_depth
        of_ins = [
            ObjectFifo(self.x.tile, name=f"in_{k}", depth=depth) for k in range(cores)
        ]
        of_outs = [
            ObjectFifo(self.y.tile, name=f"out_{k}", depth=depth) for k in range(cores)
        ]
        rtps = self.rtp([self.count, self.low_bits, self.high_bits], cores=cores)

        def core_fn(of_in, of_out, kernel_fn, rtp):
            words = rtp.read()
            n = words[self.count]
            low, high = words[self.low_bits], words[self.high_bits]
            for _ in range_(n):
                x, y = of_in.acquire(1), of_out.acquire(1)
                kernel_fn(x, y, self.tile_size, low, high)
                of_in.release(1)
                of_out.release(1)

        workers = [
            Worker(
                core_fn,
                [of_ins[k].cons(), of_outs[k].prod(), kernel, rtps[k]],
            )
            for k in range(cores)
        ]
        self.x.bind([f.prod() for f in of_ins])
        self.y.bind([f.cons() for f in of_outs])
        return workers
