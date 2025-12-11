#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import pytest
from operators.rope.op import AIERope
from operators.rope.reference import generate_golden_reference
from operators.common.test_utils import run_test


def generate_test_params(extensive=False):
    params = []
    names = []

    max_aie_columns = 8
    num_channels = 2

    if not extensive:
        input_lengths = [4096]
        method_types = [0]  # 0: Two-halves method
    else:
        input_lengths = [1024, 8192]
        method_types = [0, 1]  # 0: Two-halves method, 1: interleaved method

    for input_length in input_lengths:
        for num_aie_columns in range(1, max_aie_columns + 1):
            tile_size = input_length // num_aie_columns
            if tile_size > 4096:
                tile_size = 4096
            check_length = tile_size * num_aie_columns
            if check_length == input_length:
                for method_type in method_types:
                    names.append(
                        f"rope_{num_aie_columns}_cols_{num_channels}_channels_{input_length}_tile_{tile_size}_{method_type}"
                    )
                    params.append(
                        (
                            input_length,
                            num_aie_columns,
                            num_channels,
                            tile_size,
                            method_type,
                        )
                    )

    return params, names


regular_params, regular_names = generate_test_params(extensive=False)
extensive_params, extensive_names = generate_test_params(extensive=True)

# Combine params with marks - extensive params get pytest.mark.extensive
all_params = [
    pytest.param(*params, id=name)
    for params, name in zip(regular_params, regular_names)
] + [
    pytest.param(*params, marks=pytest.mark.extensive, id=name)
    for params, name in zip(extensive_params, extensive_names)
]


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "length,aie_columns,channels,tile_size,method_type",
    all_params,
)
def test_rope(length, aie_columns, channels, tile_size, method_type, aie_context):
    rows = length // tile_size
    cols = tile_size

    golden_ref = generate_golden_reference(
        rows=rows, cols=cols, method_type=method_type
    )

    operator = AIERope(
        size=length,
        num_aie_columns=aie_columns,
        num_channels=channels,
        last_dim=tile_size,
        method_type=method_type,
        context=aie_context,
    )

    input_buffers = {
        "in": golden_ref["A"].flatten(),
        "angles": golden_ref["B"].flatten(),
    }
    output_buffers = {"output": golden_ref["C"].flatten()}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.05, abs_tol=0.5
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
