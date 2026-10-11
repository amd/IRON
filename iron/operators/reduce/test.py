#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reduce on a device: each row's max (and min, and sum) held to a plain
numpy reduction over its own ``axis=-1``, independent of ``Reduce.reference()``.
Only element 0 of the 2-wide output row is defined (``_min_dma_aligned_elems``'s
padding), so the comparison reads it alone rather than the generic full-buffer
harness, which would also compare the undefined element.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common.harness import verify_buffer
from iron.common.image import OperatorImage
from iron.operators.reduce.op import Reduce

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

CASES = {
    "max": (lambda x: x.max(axis=-1)),
    "min": (lambda x: x.min(axis=-1)),
    "add": (lambda x: x.sum(axis=-1)),
}


WINDOWS = {
    "vectorized": 96,  # a vector width (32) multiple, not a power of two
    "scalar": 26,  # SPP's own 5x5 window (25), padded by one to an even count
}


@pytest.mark.parametrize("op_name", list(CASES))
@pytest.mark.parametrize("window", list(WINDOWS))
def test_reduce(op_name, window, module_npu_runtime):
    rows, tile = 17, WINDOWS[window]
    rng = np.random.default_rng(0)
    x = (rng.standard_normal((rows, tile)) * 4).astype(bfloat16)

    op = Reduce(rows=rows, window=tile, op=op_name)
    fn = OperatorImage(op).compile()
    tensor_class = aie_utils.DEFAULT_TENSOR_CLASS
    x_buf = tensor_class(x)
    y_buf = tensor_class((rows, 2), dtype=bfloat16)
    fn(x_buf, y_buf)

    got = y_buf.numpy()[:, 0]
    want = CASES[op_name](x.astype(np.float32)).astype(bfloat16).astype(np.float32)
    tolerance = Tolerance.exact(note="an exact selection or reproducible bf16 sum")
    verdict = verify_buffer(got, "y", want, tolerance)
    assert verdict, verdict.detail


def test_an_odd_window_is_refused():
    with pytest.raises(ValueError, match="window .* is odd"):
        Reduce(rows=4, window=25, op="max")
