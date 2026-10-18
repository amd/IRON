# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise
from ml_dtypes import bfloat16

from iron.common import Built, KernelCall, Operand, Param, Rtp, UnaryElementwise, Value
from iron.common.elementwise import Sweep
from iron.common.testing import Case, Testing


class Clamp(UnaryElementwise):
    """`x` clamped to `[low, high]`, elementwise, the bounds rounded to bf16."""

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

    low_bits = Value(derive=lambda op: op.bits()[0])
    high_bits = Value(derive=lambda op: op.bits()[1])

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

    def bits(self) -> tuple:
        """The bounds as the kernel takes them: each bf16's bits."""
        return tuple(
            int(np.array(b, bfloat16).view(np.uint16)) for b in (self.low, self.high)
        )

    def chain(self) -> tuple[KernelCall, ...]:
        # The bounds are words a core reads, not part of the array: a step's own.
        extra = {b.name for b in self.finish_inputs}
        operands = tuple(b for b in self.inputs if b.name not in extra)
        return (KernelCall(self.array_config().kernel(), self.bits(), operands),)

    def at_line(self, line: int, dtype, dev, ordered: bool = True, at: int = 0):
        # A step's chain is baked into its producer's array; the bounds are not array-tier.
        raise ValueError("Clamp's cores run an array of their own")

    class Array(UnaryElementwise.Array):
        x: Operand
        y: Operand
        low_bits: Value
        high_bits: Value

        def kernel(self):
            return eltwise.clamp(self.tile_size)

        def build(self) -> Built:
            cores = self.cores
            kernel = self.kernel()
            depth = self.x.l1_depth
            of_ins = [ObjectFifo(self.x.obj_type, depth=depth) for k in range(cores)]
            of_outs = [ObjectFifo(self.y.obj_type, depth=depth) for k in range(cores)]
            rtps = [
                Rtp([self.count, self.low_bits, self.high_bits]) for _ in range(cores)
            ]

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
            return Built(workers, rtps)
