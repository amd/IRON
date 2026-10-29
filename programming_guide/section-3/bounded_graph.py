# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-3 example: one compile, any extent up to the compiled size.

``BoundedRelu`` compiles for a fixed ``x`` shape, but each call bounds how
many of its leading elements the device actually touches, with ``n`` given
per call rather than baked into the image.
"""

import argparse

import numpy as np
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.operators import ReLU


class BoundedRelu(iron.Graph):
    """``relu(x[:n])``: one compile serves any ``n`` up to ``len(x)``."""

    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(x[:n])


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 3: per-call bounds")
    parser.add_argument("--size", type=int, default=256)
    args = parser.parse_args(argv)

    graph = BoundedRelu()
    compiled = graph.compile(x=(args.size,))
    (relu,) = (s.op for s in compiled.recording.steps)
    tolerance = relu.resolved().tolerance()

    rng = np.random.default_rng(0)
    x = rng.standard_normal(args.size).astype(bfloat16)

    for n in (16, args.size // 2, args.size):
        # graph.reference(...) trims its output to n elements; a device call
        # always returns the compiled (full) buffer, only the first n of
        # which this call wrote.
        reference = graph.reference(x, n=n)
        result = graph(x, n=n)
        assert result.shape == (args.size,)
        assert reference.shape == (n,)
        verdict = compare(result[:n], reference, tolerance)
        print(f"n={n}: {verdict.detail}")
        assert verdict, verdict.detail
    print("PASS!")


if __name__ == "__main__":
    main()
