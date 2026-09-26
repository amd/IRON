# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Emit: the words the next call's scratchpad and carried state start from.

A graph whose carried values are computed on the device ends each call here.
The next call reads its per-call parameters from a scratchpad; this step
writes that scratchpad's image (through the run's feedback argument), and the
carried values the call after it starts from.

Every output word is one row of a program the host writes once::

    out[r] = (planes[plane, index] * scale + bias) << shift

``planes`` is ``(2, carried)``: plane 0 the values this call started from,
plane 1 the ones it computed. ``shift`` is 2 for a core-read parameter (the
scratchpad holds those shifted, see ``ParameterScratchpad.writeBits``) and 0
for an address or a carried value. An all-zero row emits 0. The first
``slots`` rows are the image, the rest the next state.
"""

import numpy as np

from aie.extras.dialects import arith
from aie.iron import ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance

from iron.common.declare import (
    In,
    Operator,
    Out,
    Overlay,
    StreamIn,
    StreamOut,
    dim,
    operator,
)
from iron.common.testing import Case, Testing

# A program row: (plane, index, scale, bias, shift).
ROW = 5


@operator
class EmitOverlay(Overlay):
    """One core evaluating the program's rows over the carried values."""

    slots: int = dim()
    carried: int = dim()
    # slots + carried; derived unless given.
    rows: int | None = dim(None, repr=False)

    program = StreamIn(rows, ROW, dtype=np.int32, depth=1)
    planes = StreamIn(2, carried, dtype=np.int32, depth=1)
    image = StreamOut(slots, dtype=np.int32, depth=1)
    state = StreamOut(carried, dtype=np.int32, depth=1)

    def validate(self) -> None:
        if self.rows is None:
            self.rows = self.slots + self.carried
        elif self.rows != self.slots + self.carried:
            raise ValueError(
                f"rows ({self.rows}) must be slots + carried "
                f"({self.slots} + {self.carried})"
            )

    def design(self, target) -> list:
        slots, carried = self.slots, self.carried
        of_program = ObjectFifo(self.program.tile, name="program", depth=1)
        of_planes = ObjectFifo(self.planes.tile, name="planes", depth=1)
        of_image = ObjectFifo(self.image.tile, name="image", depth=1)
        of_state = ObjectFifo(self.state.tile, name="state", depth=1)

        def core_body(of_p, of_v, of_i, of_s):
            program = of_p.acquire(1)
            planes = of_v.acquire(1)
            image = of_i.acquire(1)
            state = of_s.acquire(1)

            def row(r):
                plane = arith.index_cast(program[r, 0])
                index = arith.index_cast(program[r, 1])
                v = planes[plane, index] * program[r, 2] + program[r, 3]
                return arith.shli(v, program[r, 4])

            for r in range_(slots):
                image[r] = row(r)
            for r in range_(carried):
                state[r] = row(r + slots)
            of_p.release(1)
            of_v.release(1)
            of_i.release(1)
            of_s.release(1)

        self.program.bind(of_program.prod())
        self.planes.bind(of_planes.prod())
        self.image.bind(of_image.cons())
        self.state.bind(of_state.cons())
        return [
            Worker(
                core_body,
                [of_program.cons(), of_planes.cons(), of_image.prod(), of_state.prod()],
            )
        ]


def _program(op: "Emit") -> dict:
    """A program whose rows each pick a real value, and some unused rows."""
    ov = op.ov
    rng = np.random.default_rng(7)
    program = np.stack(
        [
            rng.integers(0, 2, ov.rows),
            rng.integers(0, ov.carried, ov.rows),
            rng.integers(-3, 4, ov.rows),
            rng.integers(-1000, 1000, ov.rows),
            rng.choice([0, 2], ov.rows),
        ],
        axis=1,
    ).astype(np.int32)
    program[rng.random(ov.rows) < 0.25] = 0
    planes = rng.integers(-(1 << 20), 1 << 20, (2, ov.carried)).astype(np.int32)
    return dict(program=program, planes=planes)


@operator
class Emit(Operator[EmitOverlay]):
    """Evaluate an emit program: the next call's scratchpad image and state."""

    # Integer arithmetic; anything but exact is wrong.
    test = Testing(
        [
            Case(dict(slots=32, carried=1), id="one_carried"),
            Case(dict(slots=32, carried=2), id="two_carried"),
            Case(dict(slots=32, carried=8), id="eight_carried"),
        ],
        tolerance=Tolerance.exact(),
        draw=_program,
    )

    program = In(EmitOverlay.rows, ROW, dtype=np.int32, to=EmitOverlay.program)
    planes = In(2, EmitOverlay.carried, dtype=np.int32, to=EmitOverlay.planes)
    image = Out(EmitOverlay.slots, dtype=np.int32, from_=EmitOverlay.image)
    state = Out(EmitOverlay.carried, dtype=np.int32, from_=EmitOverlay.state)

    def reference(self, program, planes):
        return reference(program, planes, self.ov.slots)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(program, planes, slots):
    """``(image, state)``: every row evaluated in wrapping int32, split at ``slots``."""
    program = np.asarray(program, dtype=np.int32).reshape(-1, ROW)
    planes = np.asarray(planes, dtype=np.int32).reshape(2, -1)
    plane, index, scale, bias, shift = program.T
    out = (planes[plane, index] * scale + bias) << shift
    return out[:slots].astype(np.int32), out[slots:].astype(np.int32)
