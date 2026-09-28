#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Softmax's per-call row length, on a device.

Decode masks every attention row to ``position + 1`` keys through a per-call
value, and the kernels only run over that length rounded up to their vector
step. This drives one compiled graph across positions on both sides of a
step boundary, long ones before short ones, so a row whose tail a longer call
wrote must still come back with exact zeros past the position.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.harness import verify_buffer
from iron.operators.softmax import Softmax

# Llama decode's attention rows: one per head, one column per cache slot.
HEADS, SEQ = 32, 2048
POSITIONS = (SEQ, 300, 1, 2047, 31, 32, 33, 1000, 64, 2)


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


@pytest.mark.supported_devices("npu2")
def test_rows_are_masked_to_the_per_call_length(npu_runtime):
    class Attend(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Softmax(x, vector_size=n)

    attend = Attend()
    net = attend.compile(x=(HEADS, SEQ))
    reference = Softmax(rows=HEADS, cols=SEQ)

    rng = np.random.default_rng(0)
    for n in POSITIONS:
        x = rng.standard_normal((HEADS, SEQ)).astype(bfloat16)
        got = np.asarray(net(x, n=n)).reshape(HEADS, SEQ)
        tail = got[:, n:].view(np.uint16)
        assert not tail.any(), f"n={n}: {np.count_nonzero(tail)} tail elements not +0"
        errors = verify_buffer(
            got,
            "y",
            reference.reference(x, n),
            tolerance=reference.tolerance(),
        )
        assert not errors, f"n={n}: {len(errors)} mismatches"
