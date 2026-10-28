# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-1 example: one operator, called on its own, no graph.

``AXPY`` computes ``scalar_factor * a + b``. Construction is keyword-only and
declares the shape; the first call compiles for the device, later calls with
the same shape reuse that compile. Outside a graph, a call takes one device
tensor per declared buffer, in order (every input, then every output).
"""

import argparse

import aie.utils as aie_utils
import numpy as np
from aie.utils.verify import compare
from ml_dtypes import bfloat16

from iron.operators import AXPY


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 1: AXPY standalone")
    parser.add_argument("--size", type=int, default=2048)
    parser.add_argument("--scalar", type=float, default=1.5)
    args = parser.parse_args(argv)

    op = AXPY(
        size=args.size,
        num_aie_columns=1,
        tile_size=args.size,
        scalar_factor=args.scalar,
    )

    rng = np.random.default_rng(0)
    a_np = rng.standard_normal(args.size).astype(bfloat16)
    b_np = rng.standard_normal(args.size).astype(bfloat16)
    reference = op.reference(a_np, b_np)

    Tensor = aie_utils.DEFAULT_TENSOR_CLASS
    a, b = Tensor(a_np), Tensor(b_np)
    y = Tensor(a_np.shape, dtype=a_np.dtype)
    op(a, b, y)
    result = y.numpy()

    verdict = compare(result, reference, op.resolved().tolerance())
    print(f"AXPY vs. its own reference: {verdict.detail}")
    assert verdict, verdict.detail
    print("PASS!")


if __name__ == "__main__":
    main()
