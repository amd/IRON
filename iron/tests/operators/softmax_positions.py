#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Softmax's per-call row length, on a device.

Decode bounds every attention row to ``position + 1`` keys, ``Softmax(x[:,
:n])``: the rows stream the blocks ``n`` covers, and the kernels only run over
the last block's valid elements rounded up to their vector step. This drives
one compiled graph across positions on both sides of a step and a block
boundary, long ones before short ones, so a block whose tail a longer call
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
POSITIONS = (SEQ, 300, 1, 2047, 31, 32, 33, 1000, 1024, 1025, 64, 2)


@pytest.mark.parametrize(
    "boundaries",
    [
        pytest.param(None, id="full_elf", marks=pytest.mark.supported_devices("npu2")),
        pytest.param(
            iron.each_step,
            id="xclbin",
            marks=pytest.mark.supported_devices("npu1", "npu2"),
        ),
    ],
)
def test_rows_are_masked_to_the_per_call_length(npu_runtime, boundaries):
    class Attend(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Softmax(x[:, :n])

    attend = Attend()
    net = attend.compile(x=(HEADS, SEQ), boundaries=boundaries)
    op = Softmax(rows=HEADS, cols=SEQ, block=1024)
    tolerance = op.tolerance()
    assert tolerance is not None

    rng = np.random.default_rng(0)
    for n in POSITIONS:
        x = rng.standard_normal((HEADS, SEQ)).astype(bfloat16)
        got = np.asarray(net(x, n=n)).reshape(HEADS, SEQ)
        end = -(-n // op.block) * op.block
        tail = got[:, n:end].view(np.uint16)
        assert not tail.any(), f"n={n}: {np.count_nonzero(tail)} tail elements not +0"
        want = attend.reference(x, n=n)
        verdict = verify_buffer(got[:, :n], "y", want, tolerance)
        assert verdict, f"n={n}: {verdict.detail}"
