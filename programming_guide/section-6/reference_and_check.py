# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-6 example: the host reference, and a device run checked step by step.

``Pipeline`` chains two operators that each round, so no single step's
tolerance covers the whole output. ``main()`` checks ``graph.reference(...)``
against the two operators' references chained by hand, runs the graph on
the device, then runs a ``compile(check=True)`` version, which dispatches
each step on its own and raises at the first step outside its tolerance.
"""

import argparse

import numpy as np
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron.operators import ElementwiseMul, SiLU


class Pipeline(iron.Graph):
    """``silu(x) * y``, two operators as one compiled image."""

    def body(self, x, y):
        return ElementwiseMul.step(SiLU.step(x), y)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 6: reference and check")
    parser.add_argument("--size", type=int, default=2048)
    args = parser.parse_args(argv)

    rng = np.random.default_rng(0)
    x = rng.standard_normal(args.size).astype(bfloat16)
    y = rng.standard_normal(args.size).astype(bfloat16)

    graph = Pipeline()
    host_reference = graph.reference(x, y)
    silu = SiLU(size=args.size, num_aie_columns=1, tile_size=args.size)
    mul = ElementwiseMul(size=args.size, num_aie_columns=1, tile_size=args.size)
    by_hand = mul.reference(silu.reference(x), y)
    verdict = compare(host_reference, by_hand, Tolerance.exact())
    print(f"graph.reference() vs. its operators chained by hand: {verdict.detail}")
    assert verdict, verdict.detail

    graph.compile(x=(args.size,), y=(args.size,))
    result = graph(x, y)

    checked = Pipeline()
    checked.compile(x=(args.size,), y=(args.size,), check=True)
    checked_result = checked(x, y)

    # Both packagings run the same kernels on the same inputs.
    verdict = compare(result, checked_result, Tolerance.exact())
    print(f"normal call vs. check=True call: {verdict.detail}")
    assert verdict, verdict.detail
    print("PASS!")


if __name__ == "__main__":
    main()
