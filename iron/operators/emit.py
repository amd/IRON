# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Emit: the words the next call's scratchpad and carried state start from.

Every output word is one row of a program the host writes once:

```text
v = clamp(((planes[plane, index] * scale + bias) >> down) * mul + add, lo, hi)
out[r] = (v & mask) << shift
```

``planes`` is ``(2, carried)``: the values this call started from, then
those it computed. ``shift`` is 2 for a core-read parameter (the scratchpad
holds those shifted) and 0 otherwise; ``>> down`` floors. A row that holds
nothing to a range has ``lo``/``hi`` int32's own (``UNCLAMPED``), and one
that does not wrap a ``mask`` of -1.
"""

import numpy as np
from aie.extras.dialects import arith
from aie.iron import ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance

from iron.common import In, Operator, Out, Param, Built, Operand, Rtp, Value
from iron.common.testing import Case, Testing

# A program row: (plane, index, scale, bias, down, mul, add, lo, hi, mask, shift).
ROW = 11
UNCLAMPED = (np.iinfo(np.int32).min, np.iinfo(np.int32).max)


def reference(program, planes, slots: int):
    """``(image, state)``: every row evaluated in wrapping int32, split at ``slots``."""
    program = np.asarray(program, dtype=np.int32).reshape(-1, ROW)
    planes = np.asarray(planes, dtype=np.int32).reshape(2, -1)
    plane, index, scale, bias, down, mul, add, lo, hi, mask, shift = program.T
    out = np.clip(((planes[plane, index] * scale + bias) >> down) * mul + add, lo, hi)
    out = (out & mask) << shift
    return out[:slots].astype(np.int32), out[slots:].astype(np.int32)


def _program(op: "Emit") -> dict:
    """A program whose rows each pick a real value, most held to a range,
    and some unused rows."""
    rng = np.random.default_rng(7)
    lo = rng.integers(-(1 << 22), 1 << 22, op.rows)
    hi = lo + rng.integers(0, 1 << 23, op.rows)
    lo[rng.random(op.rows) < 0.3] = UNCLAMPED[0]
    hi[rng.random(op.rows) < 0.3] = UNCLAMPED[1]
    mask = (1 << rng.integers(4, 21, op.rows)) - 1
    mask[rng.random(op.rows) < 0.4] = -1
    program = np.stack(
        [
            rng.integers(0, 2, op.rows),
            rng.integers(0, op.carried, op.rows),
            rng.integers(-3, 4, op.rows),
            rng.integers(-1000, 1000, op.rows),
            rng.integers(0, 7, op.rows),
            rng.integers(-3, 4, op.rows),
            rng.integers(-1000, 1000, op.rows),
            lo,
            hi,
            mask,
            rng.choice([0, 2], op.rows),
        ],
        axis=1,
    ).astype(np.int32)
    program[rng.random(op.rows) < 0.25] = 0
    planes = rng.integers(-(1 << 20), 1 << 20, (2, op.carried)).astype(np.int32)
    return dict(given={op.program: program, op.planes: planes})


class Emit(Operator):
    """Evaluate an emit program: the next call's scratchpad image and state."""

    # Integer arithmetic; anything but exact is wrong.
    test = Testing(
        [
            Case(dict(slots=32, carried=1), id="one_carried"),
            # Benched though near the dispatch cost: no input takes it past.
            Case(dict(slots=32, carried=8), id="eight_carried", bench=True),
        ],
        draw=_program,
    )

    slots: int = Param()
    carried: int = Param()
    rows: int = Param(derive=lambda op: op.slots + op.carried, repr=False)

    program = In(rows, ROW, dtype=np.int32, obj_type=(rows, ROW), depth=1)
    planes = In(2, carried, dtype=np.int32, obj_type=(2, carried), depth=1)
    image = Out(slots, dtype=np.int32, obj_type=(slots,), depth=1)
    state = Out(carried, dtype=np.int32, obj_type=(carried,), depth=1)

    def validate(self) -> None:
        if self.rows != self.slots + self.carried:
            raise ValueError(
                f"rows ({self.rows}) must be slots + carried "
                f"({self.slots} + {self.carried})"
            )

    class Array(Operator.Array):
        carried: int
        rows: int
        slots: int
        image: Operand
        planes: Operand
        program: Operand
        state: Operand

        def build(self) -> Built:
            slots, carried = self.slots, self.carried
            of_program = ObjectFifo(self.program.obj_type, depth=1)
            of_planes = ObjectFifo(self.planes.obj_type, depth=1)
            of_image = ObjectFifo(self.image.obj_type, depth=1)
            of_state = ObjectFifo(self.state.obj_type, depth=1)
            self.program.bind(of_program.prod())
            self.planes.bind(of_planes.prod())
            self.image.bind(of_image.cons())
            self.state.bind(of_state.cons())

            def core_body(of_p, of_v, of_i, of_s):
                program = of_p.acquire(1)
                planes = of_v.acquire(1)
                image = of_i.acquire(1)
                state = of_s.acquire(1)

                def floor_shift(v, k):
                    # Not arith.shrsi, which lowers to a rounding ups + srs.
                    i32 = v.type
                    sign = arith.subi(
                        arith.constant(0, i32), arith.shrui(v, arith.constant(31, i32))
                    )
                    return arith.xori(arith.shrui(arith.xori(v, sign), k), sign)

                def row(r):
                    plane = arith.index_cast(program[r, 0])
                    index = arith.index_cast(program[r, 1])
                    v = planes[plane, index] * program[r, 2] + program[r, 3]
                    v = floor_shift(v, program[r, 4]) * program[r, 5] + program[r, 6]
                    v = arith.minsi(arith.maxsi(v, program[r, 7]), program[r, 8])
                    return arith.shli(arith.andi(v, program[r, 9]), program[r, 10])

                for r in range_(slots):
                    image[r] = row(r)
                for r in range_(carried):
                    state[r] = row(r + slots)
                of_p.release(1)
                of_v.release(1)
                of_i.release(1)
                of_s.release(1)

            return Built(
                [
                    Worker(
                        core_body,
                        [
                            of_program.cons(),
                            of_planes.cons(),
                            of_image.prod(),
                            of_state.prod(),
                        ],
                    )
                ]
            )

    def ops(self) -> int:
        return 0  # a handful of words: its figure is latency

    def reference(self, program, planes):
        return reference(program, planes, self.slots)

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()
