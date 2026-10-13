#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""flm.GEMM under a per-call row bound, on a device.

A prompt chunk projects ``x[:n]``: on an xclbin A and C move, and the cores
compute, the 256-row units ``n`` reaches, and past them the cores drain each
column block's B replay without computing. A full ELF still computes every
row; its case checks the rows the call asked for all the same. One compiled graph is driven at bounds
on both sides of a unit, long ones before short ones and back, so a count
or a replay one call leaves must not reach the next. B is resident in the
memtile at the first shape and streamed per unit at the second.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.harness import verify_buffer
from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.tests.common.graphs import ProjectAsStored

BOUNDS = (512, 1, 300, 256, 257, 512, 17, 3)


@pytest.mark.parametrize(
    "M,K,N", [(512, 512, 1024), (512, 3072, 512)], ids=["resident_b", "streamed_b"]
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
def test_the_units_a_bound_reaches_are_computed(npu_runtime, boundaries, M, K, N):
    project = ProjectAsStored().compile(x=(M, K), w=(N, K), boundaries=boundaries)
    op = FLMGEMM(M=M, K=K, N=N, b_col_maj=True)
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
