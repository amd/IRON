#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest

from iron.operators.gelu.op import GELU
from iron.operators.gelu.reference import generate_golden_reference
from iron.common.test_utils import run_test, make_channeled_unary_params


def get_params():
    def _marks(ext, ts):
        marks = []
        if ext:
            marks.append(pytest.mark.extensive)
        # TODO: temporary - disable tile_size=8192 for GeLU, issue #113
        if ts == 8192:
            marks.append(
                pytest.mark.skip(
                    reason="temporary: tile_size=8192 disabled for GeLU, see issue #113"
                )
            )
        return marks

    return [
        pytest.param(il, nac, nc, ts, marks=_marks(ext, ts))
        for il, nac, nc, ts, ext in make_channeled_unary_params(
            [1024, 2048, 4096, 8192], 8192, [1, 2]
        )
    ]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "input_length,num_aie_columns,num_channels,tile_size",
    get_params(),
)
def test_gelu(input_length, num_aie_columns, num_channels, tile_size, aie_context):
    golden_ref = generate_golden_reference(input_length=input_length)

    operator = GELU(
        size=input_length,
        num_aie_columns=num_aie_columns,
        num_channels=num_channels,
        tile_size=tile_size,
        context=aie_context,
    )

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
