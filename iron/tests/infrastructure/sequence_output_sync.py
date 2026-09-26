#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every dispatch of an xclbin chain hands back its own output.

A dispatch writes its output buffers on the device, which the host-side coherence
map does not observe. ``to("cpu")`` transfers only the ranges the map holds as
device-resident, so a range left marked ``cpu`` by the previous pull is skipped
and the next dispatch hands back the previous one's output.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.operators import ElementwiseAdd

SIZE = 1024


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.parametrize("calls", [2, 3])
def test_every_dispatch_returns_its_own_output(calls, npu_runtime):
    add = ElementwiseAdd(size=SIZE, tile_size=128)
    w = np.ones(SIZE, dtype=bfloat16)

    @iron.graph
    def f(x):
        return add(x, w)

    net = f.compile(boundaries=iron.each_step, image=iron.XCLBIN, x=(SIZE,))
    assert net.plan.dispatch == "separate"
    for call in range(calls):
        x = np.full(SIZE, call, dtype=bfloat16)
        got = net(x).numpy().astype(np.float32)
        assert np.all(got == call + 1), f"call {call} returned {got[:4]}"
