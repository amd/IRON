#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""flm.GEMM under a per-call row bound, on a device.

A prompt chunk projects ``x[:n]``: A and C move, and the cores compute, the
256-row units ``n`` reaches, and past them the cores drain each column
block's B replay without computing. One compiled graph is driven at bounds
on both sides of a unit, long ones before short ones and back, so a count
or a replay one call leaves must not reach the next. B is resident in the
memtile at the first shape and streamed per unit at the second; the third
is Llama 3.2 1B's q projection at a prompt chunk's bounds.
"""

import numpy as np
import pytest
from aie.utils.verify import compare
from ml_dtypes import bfloat16

from iron.operators.flm.gemm.op import GEMM as FLMGEMM
from iron.tests.common.graphs import ProjectAsStored

SHORT = (512, 1, 300, 256, 257, 512, 17, 3)
# A Llama 3.2 1B q projection's shape, at a prompt chunk's bounds.
CHUNK = (2048, 1, 15, 512, 2048, 15)


@pytest.mark.parametrize(
    "M,K,N,bounds",
    [
        (512, 512, 1024, SHORT),
        (512, 3072, 512, SHORT),
        (2048, 2048, 2048, CHUNK),
    ],
    ids=["resident_b", "streamed_b", "llama_q"],
)
@pytest.mark.parametrize(
    "full_elf",
    [
        pytest.param(None, id="full_elf", marks=pytest.mark.supported_devices("npu2")),
        pytest.param(
            False,
            id="xclbin",
            marks=pytest.mark.supported_devices("npu1", "npu2"),
        ),
    ],
)
def test_the_units_a_bound_reaches_are_computed(full_elf, M, K, N, bounds):
    project = ProjectAsStored().compile(x=(M, K), w=(N, K), full_elf=full_elf)
    op = FLMGEMM(M=M, K=K, N=N, b_col_maj=True)
    tolerance = op.resolved().tolerance()

    rng = np.random.default_rng(0)
    for n in bounds:
        x = rng.standard_normal((M, K)).astype(bfloat16)
        w = rng.standard_normal((N, K)).astype(bfloat16)
        got = np.asarray(project(x, w, n=n)).reshape(M, N)
        verdict = compare(
            got[:n],
            op.reference(x[:n], w),
            tolerance,
            bound=tolerance.bound(x[:n], w),
        )
        assert verdict, f"n={n}: {verdict.detail}"
