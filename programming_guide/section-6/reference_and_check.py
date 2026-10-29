# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-6 example: the host reference, and a device run checked step by step.

``Pipeline`` chains two operators that each round (unlike Section 2's,
where only one did), so there is no single step whose tolerance covers the
whole output. ``main()`` checks it three ways: ``graph.reference(...)``
against the same two operators' own ``reference()`` chained by hand, which
is exact (no device, no rounding, either way); a normal device call; and a
``compile(check=True))`` version, which dispatches each step on its own and
raises at the first one outside its own tolerance, rather than only
comparing the whole graph's final output.
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

    # 1. No NPU: body() runs on the host, through each operator's own
    # reference(), chained exactly as `main()` does it by hand below - the
    # same numpy, no device rounding either way.
    graph = Pipeline()
    host_reference = graph.reference(x, y)
    silu = SiLU(size=args.size, num_aie_columns=1, tile_size=args.size)
    mul = ElementwiseMul(size=args.size, num_aie_columns=1, tile_size=args.size)
    by_hand = mul.reference(silu.reference(x), y)
    verdict = compare(host_reference, by_hand, Tolerance.exact())
    print(f"graph.reference() vs. its operators chained by hand: {verdict.detail}")
    assert verdict, verdict.detail

    # 2. A normal device call, dispatched as one image.
    graph.compile(x=(args.size,), y=(args.size,))
    result = graph(x, y)

    # 3. check=True: each step dispatched and checked on its own device-side,
    # against its own operator's reference() and tolerance() - raising at
    # the first step outside it, which is what actually verifies a
    # multi-step graph, rather than one number invented for the whole chain.
    checked = Pipeline()
    checked.compile(x=(args.size,), y=(args.size,), check=True)
    checked_result = checked(x, y)  # raises here if either step missed its tolerance

    # The two packagings - one image, one dispatch per step - run the same
    # kernels, so they agree exactly.
    verdict = compare(result, checked_result, Tolerance.exact())
    print(f"normal call vs. check=True call: {verdict.detail}")
    assert verdict, verdict.detail
    print("PASS!")


if __name__ == "__main__":
    main()
