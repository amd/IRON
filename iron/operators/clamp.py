# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.dialects import arith
from aie.ir import BF16Type, F32Type, IntegerType
from aie.iron import In, ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise
from aie.utils.compile.jit.params import param, per_call
from ml_dtypes import bfloat16

from iron.common import Built, KernelCall, Operator, Rtp, UnaryElementwise
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

    low: float = param(default=-np.inf)
    high: float = param(default=np.inf)
    dynamic_low: bool = param(default=False, array=True)
    low_offset: float = param(default=0.0, array=True)
    floor = In(2, obj_shape=(2,), when=dynamic_low, depth=1)

    low_bits = per_call(derive=lambda op: op.bits()[0])
    high_bits = per_call(derive=lambda op: op.bits()[1])

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
        """Return the bounds as the kernel takes them: each bf16's bits."""
        return tuple(
            int(np.array(b, bfloat16).view(np.uint16)) for b in (self.low, self.high)
        )

    def chain(self) -> tuple[KernelCall, ...]:
        # The bounds are words a core reads, not part of the array.
        return (KernelCall(self.layout().kernel(), self.bits(), (self.x,)),)

    def kernel(self):
        return eltwise.clamp(self.tile_size)

    def build(self) -> Built:
        cores = self.cores
        kernel = self.kernel()
        depth = self.x.l1_depth
        of_ins = [ObjectFifo(self.x.obj_type, depth=depth) for k in range(cores)]
        of_outs = [ObjectFifo(self.y.obj_type, depth=depth) for k in range(cores)]
        rtps = [Rtp([self.count, self.low_bits, self.high_bits]) for _ in range(cores)]

        def core_fn(of_in, of_out, kernel_fn, rtp, floor):
            words = rtp.read()
            n = words[self.count]
            low, high = words[self.low_bits], words[self.high_bits]
            if self.dynamic_low:
                bound = floor.acquire(1)
                value = arith.addf(
                    arith.extf(F32Type.get(), bound[0]),
                    arith.constant(F32Type.get(), self.low_offset),
                )
                low = arith.extui(
                    IntegerType.get_signless(32),
                    arith.bitcast(
                        IntegerType.get_signless(16),
                        arith.truncf(BF16Type.get(), value),
                    ),
                )
            for _ in range_(n):
                x, y = of_in.acquire(1), of_out.acquire(1)
                kernel_fn(x, y, self.tile_size, low, high)
                of_in.release(1)
                of_out.release(1)
            if self.dynamic_low:
                floor.release(1)

        floor = ObjectFifo(self.floor.obj_type, depth=1) if self.dynamic_low else None
        workers = [
            Worker(
                core_fn,
                [
                    of_ins[k].cons(),
                    of_outs[k].prod(),
                    kernel,
                    rtps[k],
                    floor and floor.cons(),
                ],
            )
            for k in range(cores)
        ]
        self.x.bind([f.prod() for f in of_ins])
        self.y.bind([f.cons() for f in of_outs])
        if floor is not None:
            self.floor.bind(floor.prod())
        return Built(workers, rtps)

    def reference(self, x, floor=None) -> np.ndarray:
        low = (
            self.low
            if floor is None
            else float(np.asarray(floor).reshape(-1)[0]) + self.low_offset
        )
        return np.clip(
            np.asarray(x, np.float32), float(bfloat16(low)), float(bfloat16(self.high))
        ).astype(bfloat16)

    def judge(self, inputs, written, tolerance=None, expected=None):
        if self.dynamic_low:
            return Operator.judge(self, inputs, written, tolerance, expected)
        return super().judge(inputs, written, tolerance, expected)
