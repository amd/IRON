#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils
from iron.operators.rope.op import RoPE
from iron.operators.rope.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    max_cols = aie_utils.get_current_device().cols
    num_aie_columns_options = [c for c in [1, 2, 4, 8] if c <= max_cols]

    # Combine all options
    input_rows = [32, 64]
    input_cols = [128, 512]
    input_angle_rows = [8, 16, 32]
    method_types = [0, 1]  # 0: Two-halves method, 1: interleaved method

    params = []
    for num_aie_columns in num_aie_columns_options:
        for n_rows in input_rows:
            for n_angle_rows in input_angle_rows:
                for n_cols in input_cols:
                    for method_type in method_types:
                        is_regular = (
                            n_rows == 32
                            and n_cols == 512
                            and n_angle_rows in [8, 32]
                            and method_type == 0
                        )

                        is_extensive_valid = n_cols == 128

                        if not is_regular and not is_extensive_valid:
                            continue

                        marks = [] if is_regular else [pytest.mark.extensive]

                        params.append(
                            pytest.param(
                                n_rows,
                                n_cols,
                                n_angle_rows,
                                num_aie_columns,
                                method_type,
                                marks=marks,
                            )
                        )
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    "rows,cols,angle_rows,aie_columns,method_type",
    get_params(),
)
def test_rope(rows, cols, angle_rows, aie_columns, method_type, aie_context):
    golden_ref = generate_golden_reference(
        rows=rows, cols=cols, context_len=angle_rows, method_type=method_type
    )

    operator = RoPE(
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

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
