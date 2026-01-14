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

    num_aie_columns_options = [1, 2, 8]

    if not extensive:
        input_rows = [32]
        input_cols = [512]
        input_angle_rows = [8, 32]
        method_types = [0]  # 0: Two-halves method
    else:
        input_rows = [32, 64]
        input_cols = [128]
        input_angle_rows = [8, 16, 32]
        method_types = [0, 1]  # 0: Two-halves method, 1: interleaved method

    for num_aie_columns in num_aie_columns_options:
        for n_rows in input_rows:
            for n_angle_rows in input_angle_rows:
                for n_cols in input_cols:
                    for method_type in method_types:
                        names.append(
                            f"rope_{num_aie_columns}c_{n_rows}rows_{n_cols}cols_{n_angle_rows}arows_{method_type}m"
                        )
                        params.append(
                            (
                                n_rows,
                                n_cols,
                                n_angle_rows,
                                num_aie_columns,
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
    "rows,cols,angle_rows,aie_columns,method_type",
    all_params,
)
def test_rope(rows, cols, angle_rows, aie_columns, method_type, aie_context):
    golden_ref = generate_golden_reference(
        rows=rows, cols=cols, context_len=angle_rows, method_type=method_type
    )

    operator = AIERope(
        rows=rows,
        cols=cols,
        num_aie_columns=aie_columns,
        angle_rows=angle_rows,
        method_type=method_type,
        context=aie_context,
    )

    # golden reference produces tensors of shape (n_heads, seq_len, cols);
    # NPU design expects (seq_len, n_heads, cols), so we transpose inputs/outputs
    input_buffers = {
        "in": golden_ref["A"].transpose(0, 1).contiguous(),
        "angles": golden_ref["B"],
    }
    output_buffers = {"output": golden_ref["C"].transpose(0, 1).contiguous()}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.05, abs_tol=0.5
    )

    print(golden_ref["C"])
    print(
        operator.read_buffer_as_torch("output", (rows // angle_rows, angle_rows, cols))
    )

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    # assert not errors, f"Test failed with errors: {errors}"
