#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A bound that ends inside a tile, on a device.

``x[:p + 1]`` bounds a graph by an expression of a per-call value, and
``p + 1`` rows need not be a whole number of the tiles a core takes: the
transfers and the trip counts round up to the tile the last row is in, so
every valid row is computed, whatever ``p`` is.
"""

import numpy as np
import pytest
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.harness import verify_buffer
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.rms_norm import RMSNorm

ROWS, COLS = 64, 512

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
def test_every_row_of_a_bound_is_computed(npu_runtime):
    class Step(iron.Graph):
        def body(self, x, y, *, p: Scratchpad[np.int32]):
            return RMSNorm(ElementwiseAdd(x[: p + 1], y[: p + 1]))

    step = Step()

    rng = np.random.default_rng(0)
    x = rng.standard_normal((ROWS, COLS)).astype(bfloat16)
    y = rng.standard_normal((ROWS, COLS)).astype(bfloat16)
    net = step.compile(x=x.shape, y=y.shape)
    # The add takes 8 columns of 256 elements at once, 4 rows: every p but
    # the last ends its bound inside one.
    for p in (0, 4, 12, 40, ROWS - 1):
        out = np.asarray(net(x, y, p=p), dtype=np.float32).reshape(ROWS, COLS)
        expected = np.asarray(step.reference(x, y, p=p), dtype=np.float32)
        verdict = verify_buffer(
            out[: p + 1],
            "out",
            expected.reshape(p + 1, COLS),
            tolerance=Tolerance.relative(0.04, 1e-2),
        )
        assert verdict, f"{p=}: the valid rows differ: {verdict.detail}"


@pytest.mark.supported_devices("npu2")
def test_a_bound_past_a_wrap_of_tiles_per_lane(npu_runtime):
    class Step(iron.Graph):
        def body(self, x, y, *, n: Scratchpad[np.int32]):
            return ElementwiseAdd(x[:n], y[:n])

    step = Step()
    # 8 lanes of 256-element tiles: 1024 tiles each, one past a D1 wrap.
    rows, cols = 1024, 2048
    rng = np.random.default_rng(0)
    x = rng.standard_normal((rows, cols)).astype(bfloat16)
    y = rng.standard_normal((rows, cols)).astype(bfloat16)
    net = step.compile(x=x.shape, y=y.shape)
    for n in (1, 777, rows):
        out = np.asarray(net(x, y, n=n), dtype=np.float32).reshape(rows, cols)
        expected = np.asarray(step.reference(x, y, n=n), dtype=np.float32)
        verdict = verify_buffer(
            out[:n],
            "out",
            expected.reshape(n, cols),
            tolerance=Tolerance.relative(0.04, 1e-2),
        )
        assert verdict, f"{n=}: the valid rows differ: {verdict.detail}"
