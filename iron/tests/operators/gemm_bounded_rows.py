#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GEMM under a per-call row bound, on a device.

A prompt chunk projects ``x[:n]``: the cores compute the row blocks ``n``
covers and pass the rest through. One compiled graph is driven at bounds
on both sides of a row block, long ones before short ones and back, so a
count one call left must not reach the next; on an xclbin, whose cores
outlive the call, that is the runtime parameter the sequence writes.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.harness import verify_buffer
from iron.operators.gemm import GEMM
from iron.tests.common.bounded_graphs import Project

M, K, N = 512, 512, 512
BOUNDS = (M, 1, 300, 64, 65, M, 17, 128, 3)


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
def test_the_rows_of_a_bound_are_computed(npu_runtime, boundaries):
    project = Project().compile(x=(M, K), w=(N, K), boundaries=boundaries)
    op = GEMM(M=M, K=K, N=N, b_col_maj=True)
    tolerance = op.resolved().tolerance()

    rng = np.random.default_rng(0)
    for n in BOUNDS:
        x = rng.standard_normal((M, K)).astype(bfloat16)
        w = rng.standard_normal((N, K)).astype(bfloat16)
        got = np.asarray(project(x, w, n=n)).reshape(M, N)
        verdict = verify_buffer(
            got[:n],
            "C",
            op.reference(x[:n], w),
            tolerance,
            bound=tolerance.bound(x[:n], w),
        )
        assert verdict, f"n={n}: {verdict.detail}"
