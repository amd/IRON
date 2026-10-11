#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""iron.lm.MaxPool2d on a device, at SPP's own shape (one of its three
kernel sizes): held to its device-free exact() convolution-free max,
independently checked against a from-scratch numpy loop in
iron/tests/common/maxpool2d_graph.py.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.lm.blocks import MaxPool2d

pytestmark = pytest.mark.supported_devices("npu2")

ROWS, WIDTH, CHANNELS, KERNEL = 13, 13, 128, 5


def test_max_pool2d(module_npu_runtime):
    rng = np.random.default_rng(0)
    x = (rng.standard_normal((ROWS, WIDTH * CHANNELS)) - 0.2).astype(bfloat16)

    pool = MaxPool2d(rows=ROWS, width=WIDTH, channels=CHANNELS, kernel=KERNEL)
    version = pool.compile(x=((ROWS, WIDTH * CHANNELS), bfloat16))
    version.load()
    got = np.asarray(version(x).numpy(), np.float32).reshape(ROWS, WIDTH * CHANNELS)
    want = pool.exact(x)

    assert np.abs(got - want).max() < 0.5
