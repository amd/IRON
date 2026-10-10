#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Softmax's per-call row length, on a device.

Decode bounds every attention row to ``position + 1`` keys, ``Softmax(x[:,
:n])``: the rows stream the blocks ``n`` covers, or a core holds each whole
where it has more rows than a streamed core fits, and the kernels only run
over the last block's valid elements rounded up to their vector step. This drives
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


@pytest.mark.parametrize(
    "rows,seq,block,positions",
    [
        # Llama decode's attention rows, one a head: one column per cache slot.
        pytest.param(
            32,
            2048,
            1024,
            (2048, 300, 1, 2047, 31, 32, 33, 1000, 1024, 1025, 64, 2),
            id="llama",
        ),
        # A row 1024 does not divide streams in the longest block that does.
        pytest.param(
            32,
            1280,
            640,
            (1280, 300, 1, 1279, 31, 32, 33, 639, 640, 641, 64, 2),
            id="unaligned",
        ),
        # EmbeddingGemma 2's image scores, a row a query: held whole.
        pytest.param(
            1280,
            1280,
            1280,
            (1280, 300, 1, 1279, 31, 32, 33, 639, 640, 641, 64, 2),
            id="vision",
        ),
    ],
)
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
def test_rows_are_masked_to_the_per_call_length(
    npu_runtime, boundaries, rows, seq, block, positions
):
    class Attend(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return Softmax(x[:, :n])

    attend = Attend()
    net = attend.compile(x=(rows, seq), boundaries=boundaries)
    (step,) = net.traced.steps
    assert step.op.resolved().block == block
    op = Softmax(rows=rows, cols=seq, block=block)
    tolerance = op.tolerance()
    assert tolerance is not None

    rng = np.random.default_rng(0)
    for n in positions:
        x = rng.standard_normal((rows, seq)).astype(bfloat16)
        got = np.asarray(net(x, n=n)).reshape(rows, seq)
        end = -(-n // op.block) * op.block
        tail = got[:, n:end].view(np.uint16)
        assert not tail.any(), f"n={n}: {np.count_nonzero(tail)} tail elements not +0"
        want = attend.reference(x, n=n)
        verdict = verify_buffer(got[:, :n], "y", want, tolerance)
        assert verdict, f"n={n}: {verdict.detail}"
