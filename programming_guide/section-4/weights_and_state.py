# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-4 example: a held weight, and device-resident state.

``Scale`` holds a weight the host never passes again. ``Accumulate`` holds
state: a device-resident row per ``pos`` that persists from call to call,
added into at each one.
"""

import argparse

import numpy as np
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.operators.copy import Copy


class Scale(iron.Graph):
    """``x * weight``, elementwise, against a weight this graph holds."""

    def __init__(self, weight):
        self.weight = iron.param(weight)

    def body(self, x):
        return x * self.weight


class Accumulate(iron.Graph):
    """A running total at row ``pos`` of a device-resident state: each call
    adds ``x`` into ``total[pos]`` and returns the new value."""

    def __init__(self, rows, width):
        self.total = iron.state((rows, width), name="total")

    def body(self, x, *, pos: Scratchpad[np.int32]):
        old = Copy.step(self.total[pos])
        new = x + old
        Copy.step(new, self.total[pos])
        return new


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 4: weights and state")
    parser.add_argument("--width", type=int, default=256)
    args = parser.parse_args(argv)
    rng = np.random.default_rng(0)

    weight = rng.standard_normal(args.width).astype(bfloat16)
    scale = Scale(weight)
    x = rng.standard_normal(args.width).astype(bfloat16)
    reference = scale.reference(x)
    compiled = scale.compile(x=(args.width,))
    (mul,) = (s.op for s in compiled.recording.steps)
    result = scale(x)
    verdict = compare(result, reference, mul.resolved().tolerance())
    print(f"Scale: {verdict.detail}")
    assert verdict, verdict.detail

    rows = 4
    accumulate = Accumulate(rows, args.width)
    compiled = accumulate.compile(x=(args.width,))
    # Copy (read, write) is exact; ElementwiseAdd is the one step that rounds.
    (add,) = (
        s.op
        for s in compiled.recording.steps
        if type(s.op).__name__ == "ElementwiseAdd"
    )
    tolerance = add.resolved().tolerance()
    for pos in (0, 1, 0, 2):
        x = rng.standard_normal(args.width).astype(bfloat16)
        # Each call advances the device's state and the reference's own
        # host-side mirror (accumulate.total.host) in step; both start zero.
        reference = accumulate.reference(x, pos=pos)
        result = accumulate(x, pos=pos)
        verdict = compare(result, reference, tolerance)
        print(f"Accumulate at pos={pos}: {verdict.detail}")
        assert verdict, verdict.detail
    print("PASS!")


if __name__ == "__main__":
    main()
