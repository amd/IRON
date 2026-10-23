# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.MaxPool2d device-free: its reference, its operators', is the max
pooling exactly, as ``exact()`` and a window-by-window loop compute it, and
it refuses an even window; and ``F.max_pool2d`` of a feature map.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
import iron.functional as F
from iron.lm import MaxPool2d

pytestmark = pytest.mark.usefixtures("npu2")

# Rows, pixels a row, channels and the window.
CASES = {
    "kernel_5": (13, 13, 128, 5),
    "kernel_13": (13, 13, 128, 13),
    "wide": (6, 10, 32, 3),
}


def windowed(x, rows, width, channels, kernel):
    """The max of each pixel's window, one window at a time."""
    pad = kernel // 2
    image = np.asarray(x, np.float32).reshape(rows, width, channels)
    image = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), constant_values=-np.inf)
    out = np.empty((rows, width, channels), np.float32)
    for r in range(rows):
        for f in range(width):
            out[r, f] = image[r : r + kernel, f : f + kernel].max(axis=(0, 1))
    return out.reshape(rows, width * channels)


@pytest.mark.parametrize("case", list(CASES))
def test_the_reference_is_the_max_pooling(case):
    rows, width, channels, kernel = CASES[case]
    rng = np.random.default_rng(0)
    x = rng.standard_normal((rows, width * channels)).astype(bfloat16)
    pool = MaxPool2d(rows=rows, width=width, channels=channels, kernel=kernel)
    want = windowed(x, rows, width, channels, kernel)
    assert np.array_equal(pool.exact(x), want)
    assert np.array_equal(np.asarray(pool.reference(x), np.float32), want)


def test_an_even_kernel_is_refused():
    with pytest.raises(ValueError, match="must be odd"):
        MaxPool2d(rows=13, width=13, channels=128, kernel=4)


def test_functional_max_pool2d_is_the_max_pooling_at_its_stride():
    rows, width, channels, kernel = CASES["wide"]
    rng = np.random.default_rng(0)
    x = rng.standard_normal((rows, width, channels)).astype(bfloat16)

    class Pool(iron.Graph):
        def __init__(self, stride):
            self.stride = stride

        def body(self, x):
            return F.max_pool2d(x, kernel, self.stride, kernel // 2)

    want = windowed(x, rows, width, channels, kernel)
    for stride in (1, 2, None):
        step = stride or kernel
        strided = want.reshape(rows, width, channels)[::step, ::step]
        got = np.asarray(Pool(stride).reference(x), np.float32)
        assert np.array_equal(got.reshape(strided.shape), strided)
    with pytest.raises(ValueError, match="not a map"):
        Pool(1).record(x=((rows, width * channels), bfloat16))
