#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""DynamicSoftmax's per-call row length, on a device.

Decode masks every attention row to ``position + 1`` keys through a per-call
value, and the kernels only run over that length rounded up to their vector
step. This drives one compiled graph across positions on both sides of a
step boundary, long ones before short ones, so a row whose tail a longer call
wrote must still come back with exact zeros past the position.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.device import from_name
from aie.utils.verify import compare

import iron
from iron.common.declare import Scratchpad
from iron.operators.softmax import Softmax, reference

# Llama decode's attention rows: one per head, one column per cache slot.
HEADS, SEQ = 32, 2048
POSITIONS = (SEQ, 300, 1, 2047, 31, 32, 33, 1000, 64, 2)


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


@pytest.mark.supported_devices("npu2")
def test_rows_are_masked_to_the_per_call_length(npu_runtime):
    @iron.graph
    def attend(x, *, n: Scratchpad[np.int32]):
        return Softmax(x, vector_size=n)

    net = attend.compile(x=(HEADS, SEQ))
    assert net.plan.image == "elf", "only the full ELF carries a scratchpad"

    rng = np.random.default_rng(0)
    for n in POSITIONS:
        x = rng.standard_normal((HEADS, SEQ)).astype(bfloat16)
        got = np.asarray(attend(x, n=n)).reshape(HEADS, SEQ)
        tail = got[:, n:].view(np.uint16)
        assert not tail.any(), f"n={n}: {np.count_nonzero(tail)} tail elements not +0"
        verdict = compare(got, reference(x, n), Softmax.test.tolerance)
        assert verdict, f"n={n}: {verdict.detail}"
