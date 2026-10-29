# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-2 example: a graph of two operators, compiled once and called.

``ReluThenAxpy`` records ``ReLU`` then ``AXPY`` into one image: the
intermediate between them never leaves the device.
"""

import argparse

import numpy as np
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron.operators import AXPY, ReLU


class ReluThenAxpy(iron.Graph):
    """``scalar_factor * relu(x) + y``, two operators as one compiled image."""

    def __init__(self, scalar_factor=2.0):
        self.scalar_factor = scalar_factor

    def body(self, x, y):
        activated = ReLU.step(x)
        return AXPY.step(activated, y, scalar_factor=self.scalar_factor)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 2: your first graph")
    parser.add_argument("--size", type=int, default=2048)
    args = parser.parse_args(argv)

    graph = ReluThenAxpy(scalar_factor=2.0)
    compiled = graph.compile(x=(args.size,), y=(args.size,))

    rng = np.random.default_rng(0)
    x = rng.standard_normal(args.size).astype(bfloat16)
    y = rng.standard_normal(args.size).astype(bfloat16)

    reference = graph.reference(x, y)
    result = graph(x, y)

    # relu() is exact in bf16; AXPY is the one step that rounds, so its own
    # tolerance is the whole chain's.
    (axpy,) = (s.op for s in compiled.recording.steps if type(s.op).__name__ == "AXPY")
    verdict = compare(result, reference, axpy.resolved().tolerance())
    print(f"device call vs. graph.reference(): {verdict.detail}")
    assert verdict, verdict.detail
    print("PASS!")


if __name__ == "__main__":
    main()
