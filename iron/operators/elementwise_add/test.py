#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.elementwise_add.op import ElementwiseAdd
from iron.common.test_utils import golden, run_test, make_binary_elementwise_params


def get_params():
    return [
        pytest.param(il, nac, ts, marks=[] if not ext else [pytest.mark.extensive])
        for il, nac, ts, ext in make_binary_elementwise_params([1024, 2048, 4096, 8192])
    ]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,tile_size",
    get_params(),
)
def test_elementwise_add(input_length, num_aie_columns, tile_size, aie_context):
    operator = ElementwiseAdd(
        size=input_length,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
        context=aie_context,
    )

    data = golden(operator)

    errors, latency_us, bandwidth_gbps = run_test(
        operator, data.inputs, data.outputs, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
