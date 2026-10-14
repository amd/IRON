#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.MaxPool2d on a device: one compile each, its output exactly the
max pooling of its input, a selection of its bf16 values.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm import MaxPool2d

pytestmark = pytest.mark.supported_devices("npu1", "npu2")

# Rows, pixels a row, channels and the window: a 13 by 13 plane, and one
# wider than it is tall.
SHAPES = {"square": (13, 13, 128, 5), "wide": (6, 10, 32, 3)}


@pytest.mark.parametrize("shape", list(SHAPES))
def test_max_pool2d(shape):
    rows, width, channels, kernel = SHAPES[shape]
    rng = np.random.default_rng(0)
    x = rng.standard_normal((rows, width * channels)).astype(bfloat16)
    pool = MaxPool2d(rows=rows, width=width, channels=channels, kernel=kernel)
    pool.compile(x=(x.shape, bfloat16))
    got = np.asarray(pool(x).numpy(), np.float32).reshape(x.shape)
    assert np.array_equal(got, pool.exact(x))
