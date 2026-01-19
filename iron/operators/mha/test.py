#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
import pytest
from pathlib import Path


from iron.operators.mha.op import AIEMHA
from iron.operators.mha.reference import generate_golden_reference
from iron.common.test_utils import run_test


def generate_test_params(extensive=False):
    params = [(16384, 64, 1, 8)]
    names = ["mha"]
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
@pytest.mark.parametrize("seq_len,dim,num_heads,num_pipelines", all_params)
def test_mha(seq_len, dim, num_heads, num_pipelines, aie_context):
    golden_ref = generate_golden_reference(
        S_q=seq_len,
        S_kv=seq_len,
        d=dim,
        heads=num_heads,
        num_kv_heads=num_heads,
        num_pipeline=num_pipelines,
    )

    operator = AIEMHA(
        num_heads=num_heads,
        seq_len=seq_len,
        d=dim,
        num_KV_heads=num_heads,
        num_of_pipelines=num_pipelines,
        context=aie_context,
    )

    input_buffers = {
        "Q": golden_ref["Q"].flatten(),
        "K": golden_ref["K"].flatten(),
        "V": golden_ref["V"].flatten(),
    }
    output_buffers = {"O": golden_ref["O"].flatten()}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=4.0e-2, abs_tol=1.5e-1
    )

    error_threshold = 0.005
    max_acceptable_errors = int(seq_len * dim * num_heads * error_threshold)

    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")
    print(
        "({} errors out of {} max allowable)".format(
            len(errors["O"]), max_acceptable_errors
        )
    )

    assert (
        len(errors["O"]) <= max_acceptable_errors
    ), f"Test failed with {len(errors['O'])} errors (max allowable: {max_acceptable_errors})"
