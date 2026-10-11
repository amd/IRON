# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.MaxPool2d device-free: its reference is the convolution-free,
per-channel max in each of SPP's three kernel sizes, independent of its
own gather (``exact()``) and of a from-scratch numpy sliding-window loop.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm.blocks import MaxPool2d

pytestmark = pytest.mark.usefixtures("npu2")

# SPP's own shape: dark5's 13x13, 128-channel feature map, its three
# parallel kernel sizes.
ROWS, WIDTH, CHANNELS = 13, 13, 128


def naive_max_pool(x, rows, width, channels, kernel):
    """A dead-simple sliding-window max-pool, sharing no code with
    MaxPool2d: Python loops, ``-inf`` padding, one window at a time.
    """
    pad = kernel // 2
    image = np.asarray(x, np.float32).reshape(rows, width, channels)
    padded = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), constant_values=-np.inf)
    out = np.empty((rows, width, channels), np.float32)
    for r in range(rows):
        for f in range(width):
            out[r, f] = padded[r : r + kernel, f : f + kernel].max(axis=(0, 1))
    return out.reshape(rows, width * channels)


@pytest.mark.parametrize("kernel", [5, 9, 13])
def test_the_reference_matches_an_independent_max_pool(kernel):
    rng = np.random.default_rng(0)
    # Centered near zero, like SPP's real input (post-SiLU, can be slightly
    # negative): the case a zero-padding bug would get wrong.
    x = (rng.standard_normal((ROWS, WIDTH * CHANNELS)) - 0.2).astype(bfloat16)
    pool = MaxPool2d(rows=ROWS, width=WIDTH, channels=CHANNELS, kernel=kernel)

    got = np.asarray(pool.reference(x), np.float32)
    exact = pool.exact(x)
    independent = naive_max_pool(x, ROWS, WIDTH, CHANNELS, kernel)

    assert np.array_equal(exact, independent)
    assert np.abs(got - exact).max() < 0.5  # one bf16 rounding in ElementwiseMax


def test_an_even_kernel_is_refused():
    with pytest.raises(ValueError, match="must be odd"):
        MaxPool2d(rows=ROWS, width=WIDTH, channels=CHANNELS, kernel=4)
