#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A copy of a bounded view, by head, on a device.

``Copy(x[:n].reshape(T, H, D).transpose(1, 0, 2))`` moves the ``n`` valid
rows of each head: into a fresh output and into a cache given whole, both
bounded alike, so the drain ends where the fill does.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.operators.copy import Copy
from iron.operators.relu import ReLU

T, H, D = 256, 4, 64

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
def test_a_copy_moves_the_valid_rows_of_each_head(npu_runtime):
    cache = iron.state((H, T, D), name="cache")

    class ByHead(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            k = ReLU(x[:n]).reshape(T, H, D).transpose(1, 0, 2)
            Copy(k, cache)
            return Copy(k)

    step = ByHead()
    net = step.compile(x=(T, H * D))
    rng = np.random.default_rng(0)
    for n in (1, 50, 129, T):
        x = rng.standard_normal((T, H * D)).astype(bfloat16)
        net.write(cache, np.zeros((H, T, D), dtype=np.float32))
        out = np.asarray(net(x, n=n), dtype=np.float32).reshape(H, T, D)
        want = np.maximum(x[:n].astype(np.float32), 0).astype(bfloat16)
        want = want.astype(np.float32).reshape(n, H, D).transpose(1, 0, 2)
        assert np.array_equal(out[:, :n], want), f"{n=}: the output's valid rows"
        got = np.asarray(net.read(cache), dtype=np.float32).reshape(H, T, D)
        assert np.array_equal(got[:, :n], want), f"{n=}: the cache's valid rows"
        assert not got[:, n:].any(), f"{n=}: a row past the bound was written"
