# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import Buffer, ObjectFifo, Worker, WorkerRuntimeBarrier
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise
from ml_dtypes import bfloat16

from iron.common import UnaryElementwise, Value, param
from iron.common.testing import Case, Sweep, Testing


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
        draw=dict(centered=("x",)),
    )

    low: float = param()
    high: float = param()

    low_bits = Value(np.int32, derive=lambda op: op.scalars()[0])
    high_bits = Value(np.int32, derive=lambda op: op.scalars()[1])

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

    def array(self, target) -> list:
        cores = self.cores
        kernel = self.kernel()
        depth = target.fifo_depth(self.tile_size, bfloat16)
        of_ins = [
            ObjectFifo(self.x.tile, name=f"in_{k}", depth=depth) for k in range(cores)
        ]
        of_outs = [
            ObjectFifo(self.y.tile, name=f"out_{k}", depth=depth) for k in range(cores)
        ]
        # [count, low, high] per core; the count is a scratchpad word instead
        # when a graph bounds the extent.
        dynamic = self.uses_value("count") and target.image == "elf"
        words = (
            ["low_bits", "high_bits"] if dynamic else ["count", "low_bits", "high_bits"]
        )
        rtps = [
            Buffer(
                np.ndarray[(len(words),), np.dtype[np.int32]],
                name=f"rtp_{k}",
                use_write_rtp=True,
            )
            for k in range(cores)
        ]
        barriers = [WorkerRuntimeBarrier() for _ in range(cores)]
        params = [self.count.param] if dynamic else []

        def core_fn(of_in, of_out, kernel_fn, rtp, barrier, *count):
            barrier.wait_for_value(1)
            n = count[0].read() if dynamic else rtp[words.index("count")]
            low, high = rtp[words.index("low_bits")], rtp[words.index("high_bits")]
            for _ in range_(n):
                x, y = of_in.acquire(1), of_out.acquire(1)
                kernel_fn(x, y, self.tile_size, low, high)
                of_in.release(1)
                of_out.release(1)

        workers = [
            Worker(
                core_fn,
                [of_ins[k].cons(), of_outs[k].prod(), kernel, rtps[k], barriers[k]]
                + params,
            )
            for k in range(cores)
        ]
        for k in range(cores):
            self.x.lane(k).bind(of_ins[k].prod())
            self.y.lane(k).bind(of_outs[k].cons())
        for name in words:
            self.value(name).bind(rtps, words.index(name))
        return workers + barriers
