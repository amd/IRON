#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.common.test_utils import run_test
from iron.common.utils import get_shim_dma_limit
from iron.operators.swiglu_prefill_front_fused.op import SwigluFrontFused
from iron.operators.swiglu_prefill_front_fused.reference import generate_golden_reference


def get_params():
    dev = aie_utils.get_current_device()
    num_aie_columns = get_shim_dma_limit(dev) // 2

    # Match swiglu_prefill/test.py. Its sequential and fused-front variants
    # share this shape, so the fused operator needs one parameterization.
    return [
        pytest.param(256, 2048, 2048, num_aie_columns, 64, 64, 64),
        pytest.param(256, 2048, 2048, num_aie_columns, 64, 64, 64)
    ]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize("M,K,N,num_aie_columns,m,k,n", get_params())
def test_swiglu_fused_front(M, K, N, num_aie_columns, m, k, n, aie_context):
    golden_ref = generate_golden_reference(
        M=M,
        K=K,
        N=N,
        tile_k=k,
        tile_n=n,
        num_aie_columns=num_aie_columns,
    )
    operator = SwigluFrontFused(
        M=M,
        K=K,
        N=N,
        tile_m=m,
        tile_k=k,
        tile_n=n,
        num_aie_columns=num_aie_columns,
        context=aie_context,
    )

    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers={
            "A": golden_ref["input"].flatten(),
            "B": golden_ref["input_b"][0].flatten(),
        },
        output_buffers={"C": golden_ref["output"][0].flatten()},
        rel_tol=0.08,
        abs_tol=0.4,
        max_error_rate=0.05,
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
