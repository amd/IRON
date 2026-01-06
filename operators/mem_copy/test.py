#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from operators.mem_copy.op import AIEMemCopy
from operators.mem_copy.reference import generate_golden_reference
from operators.common.test_utils import run_test


def generate_test_params(extensive=False):
    input_lengths = [2048] if not extensive else [1024, 2048, 4096, 8192]
    bypass_modes = [False] if not extensive else [False, True]

    params = []
    names = []

    for input_length in input_lengths:
        for num_cores in range(1, 17):  # 1 to 16 cores
            for num_channels in range(1, 3):  # 1 or 2 channels
                for bypass in bypass_modes:
                    # Calculate the maximum cores that can be utilized with 1 or 2 shim channels
                    max_cores = 8 * num_channels  # MAX_COLUMNS (8) * num_channels

                    if max_cores >= num_cores and num_cores >= num_channels:
                        tile_size = input_length // num_cores

                        # Cap tile_size at 8192
                        if tile_size > 8192:
                            tile_size = 8192

                        # Only proceed if tile_size * num_cores == input_length (exact division)
                        if tile_size * num_cores == input_length:
                            names.append(
                                f"mem_copy_{num_cores}_cores_{num_channels}_chans_{input_length}_tile_{tile_size}_{str(bypass)}"
                            )
                            params.append(
                                (
                                    input_length,
                                    num_cores,
                                    num_channels,
                                    bypass,
                                    tile_size,
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
    "input_length,num_cores,num_channels,bypass,tile_size",
    all_params,
)
def test_mem_copy(
    input_length, num_cores, num_channels, bypass, tile_size, aie_context
):
    golden_ref = generate_golden_reference(input_length=input_length)

    operator = AIEMemCopy(
        size=input_length,
        num_cores=num_cores,
        num_channels=num_channels,
        bypass=bypass,
        tile_size=tile_size,
        context=aie_context,
    )

    input_buffers = {"input": golden_ref["inout"]}
    output_buffers = {"output": golden_ref["inout"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.01, abs_tol=1e-6
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
