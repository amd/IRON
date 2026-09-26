#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import math

import pytest

from iron.operators.mha.op import MHA
from iron.common.harness import run_test, vectors


def get_params():
    # (seq_len, head_dim, heads, number_of_pipeline, num_kv_heads)
    # Constraints (from design.py):
    #   - head_dim must be 64
    #   - num_kv_heads == 0 means standard MHA (treated as num_kv_heads == num_heads internally)
    #   - For GQA: 0 < num_kv_heads < num_heads, and num_heads % num_kv_heads == 0
    #   - number_of_pipelines determines how many AIE tile columns are used (col=0..N-1)
    return [
        # Standard MHA configuration (default suite)
        pytest.param(16384, 64, 1, 8, 0),
        # GQA configuration: 8 query heads with 2 KV heads (group factor = 4)
        # num_heads=8, num_KV_heads=2 satisfies: 8 % 2 == 0 and 2 < 8
        pytest.param(16384, 64, 8, 8, 2, marks=pytest.mark.extensive),
        # Multi-pipeline variant with 4 pipelines instead of 8
        # Uses fewer AIE columns; seq_len=16384, standard MHA (num_kv_heads=0)
        pytest.param(16384, 64, 1, 4, 0, marks=pytest.mark.extensive),
    ]


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "seq_len,dim,num_heads,num_pipelines,num_kv_heads", get_params()
)
def test_mha(seq_len, dim, num_heads, num_pipelines, num_kv_heads, npu_runtime):
    operator = MHA(
        num_heads=num_heads,
        seq_len=seq_len,
        d=dim,
        num_KV_heads=num_kv_heads,
        num_of_pipelines=num_pipelines,
    )

    data = vectors(operator)

    errors, latency_us, bandwidth_gbps = run_test(
        operator, data.inputs, data.outputs, rel_tol=4.0e-2, abs_tol=1.5e-1
    )

    error_threshold = 0.005
    max_acceptable_errors = int(seq_len * dim * num_heads * error_threshold)

    print(
        "({} errors out of {} max allowable)".format(
            len(errors["O"]), max_acceptable_errors
        )
    )

    assert (
        len(errors["O"]) <= max_acceptable_errors
    ), f"Test failed with {len(errors['O'])} errors (max allowable: {max_acceptable_errors})"


@pytest.mark.parametrize(
    "seq_len,dim,num_heads,num_pipelines,num_kv_heads",
    [
        (16384, 64, 8, 8, 2),
        # num_kv_heads == 0 means plain MHA.
        (16384, 64, 1, 8, 0),
    ],
)
def test_arg_spec_matches_design_shapes(
    seq_len, dim, num_heads, num_pipelines, num_kv_heads
):
    """The declared buffers size the runtime buffers; design.py declares the MLIR arg
    types. The two must agree.
    """
    op = MHA(
        num_heads=num_heads,
        seq_len=seq_len,
        d=dim,
        num_KV_heads=num_kv_heads,
        num_of_pipelines=num_pipelines,
    )
    q, k, v, o = (math.prod(b.shape) for b in op.buffers)

    pad = op.ov.seq_padding(seq_len)
    kv_heads = num_kv_heads if num_kv_heads else num_heads
    assert q == num_heads * pad * dim
    assert o == num_heads * pad * dim
    assert k == kv_heads * pad * dim
    assert v == kv_heads * pad * dim
