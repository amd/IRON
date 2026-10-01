#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.gelu import GELUOverlay
from iron.operators.gemv.op import GEMV, gelu_tanh_approx
import numpy as np
from ml_dtypes import bfloat16
from iron.common.harness import record_metric, run_test, vectors


def get_params():
    max_aie_columns = aie_utils.get_current_device().cols

    params_list = [
        (128, 128, 1, 32, 128),
        (2048, 8192, 1, 1, 2048),
        (8192, 2048, 1, 4, 1024),
        (2048, 8192, 2, 1, 1024),
        (8192, 2048, 2, 4, 1024),
        (2048, 8192, 4, 1, 512),
        (8192, 2048, 4, 4, 1024),
        (2048, 8192, 8, 1, 256),
        (8192, 2048, 8, 4, 1024),
    ]

    params = []
    for p in params_list:
        M, K, num_aie_columns, tile_size_input, tile_size_output = p
        # Skip tests that require more columns than available on the device
        if num_aie_columns > max_aie_columns:
            continue
        params.append(pytest.param(*p))
    return params


@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output", get_params()
)
def test_gemv(M, K, num_aie_columns, tile_size_input, tile_size_output, npu_runtime):
    operator = GEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
    )
    data = vectors(operator, normal=("A", "B"))

    errors, latency_us, bandwidth_gbps = run_test(
        operator, data.inputs, data.outputs, rel_tol=0.04, abs_tol=1e-3
    )

    record_metric("Throughput", (2.0 * M * K) / (latency_us * 1e-6) / 1e9)

    assert not errors, f"Test failed with errors: {errors}"


def get_batched_params():
    max_cols = aie_utils.get_current_device().cols
    # (M, K, cols, tsi, tso, num_batches): exercise the coalesced path + fallback.
    plist = [
        (256, 128, 1, 1, 256, 4),  # tiny, coalesced
        (256, 128, 8, 1, 32, 100),  # large num_batches -> the size-uncapped dim
        (448, 64, 8, 1, 56, 192),  # multi-dim run split + large num_batches together
        (64, 1536, 1, 1, 64, 8),  # large K
        (1026, 64, 1, 1, 2, 2),  # run needs an even (granularity-aligned) split
        (1024, 1024, 1, 1, 64, 2),  # batch stride > 2**20 -> falls back to per-batch
        (512, 64, 8, 4, 64, 32),  # attn-style: tile_size_input>1, num_batches=heads
    ]
    out = []
    for p in plist:
        if p[2] > max_cols:
            continue
        out.append(pytest.param(*p))
    return out


@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output,num_batches",
    get_batched_params(),
)
def test_gemv_batched(
    M, K, num_aie_columns, tile_size_input, tile_size_output, num_batches, npu_runtime
):
    operator = GEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        num_batches=num_batches,
    )
    data = vectors(operator, normal=("A", "B"))
    errors, latency_us, bandwidth_gbps = run_test(
        operator, data.inputs, data.outputs, rel_tol=0.04, abs_tol=1e-3
    )

    record_metric("Throughput", (2.0 * M * K * num_batches) / (latency_us * 1e-6) / 1e9)

    assert not errors, f"batched GEMV failed: {errors}"


def _device_output(operator, *inputs):
    """``operator``'s one output, run once on the device on ``inputs``."""
    run = operator.get_callable()
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    (out,) = operator.outputs
    args = [tensor(x) for x in inputs] + [tensor(out.host_shape, dtype=out.host_dtype)]
    run(*args)
    # A copy: the tensor's numpy view does not keep its device buffer alive.
    return args[-1].numpy().copy()


@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output,num_batches,repeat",
    [
        # Llama 3.2 1B's decode scores: 8 key groups, 4 query heads each,
        # over the 2048-row cache.
        pytest.param(2048, 64, 8, 4, 256, 32, 4),
        pytest.param(512, 64, 8, 4, 64, 32, 4),
        pytest.param(256, 128, 2, 1, 64, 8, 2),
        pytest.param(256, 128, 1, 1, 256, 4, 4),  # one matrix for every batch
        pytest.param(1024, 1024, 1, 1, 64, 4, 2),  # per-batch descriptors
    ],
)
def test_gemv_repeated(
    M,
    K,
    num_aie_columns,
    tile_size_input,
    tile_size_output,
    num_batches,
    repeat,
    npu_runtime,
):
    """Each matrix of A read once per batch it serves: against the reference,
    and bit for bit against the unrepeated GEMV on A repeated on the host."""
    if num_aie_columns > aie_utils.get_current_device().cols:
        pytest.skip(f"needs {num_aie_columns} columns")
    shape = dict(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        num_batches=num_batches,
    )
    operator = GEMV(**shape, repeat=repeat)
    data = vectors(operator, normal=("A", "B"))
    errors, latency_us, bandwidth_gbps = run_test(
        operator, data.inputs, data.outputs, rel_tol=0.04, abs_tol=1e-3
    )
    record_metric("Throughput", (2.0 * M * K * num_batches) / (latency_us * 1e-6) / 1e9)
    assert not errors, f"repeated GEMV failed: {errors}"

    A, B = data["A"], data["B"]
    A_all = np.repeat(A.reshape(-1, M, K), repeat, axis=0)
    repeated = _device_output(operator, A, B)
    materialized = _device_output(GEMV(**shape), A_all, B)
    assert np.array_equal(
        repeated.view(np.uint16), materialized.view(np.uint16)
    ), "repeated GEMV differs from the GEMV of the repeated matrices"


@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output",
    [
        pytest.param(128, 128, 1, 32, 128),
        pytest.param(2048, 8192, 1, 1, 2048),
        pytest.param(8192, 2048, 1, 4, 1024),
    ],
)
def test_gemv_gelu(
    M, K, num_aie_columns, tile_size_input, tile_size_output, npu_runtime
):
    """GEMV with GELU's kernel as its epilogue vs a gelu(A @ B) golden."""
    operator = GEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        epilogue=GELUOverlay(),
    )
    # The reference is the plain product; the epilogue is applied here.
    data = vectors(operator, normal=("A", "B"))
    c_gelu = gelu_tanh_approx(data["C"].astype(np.float32)).astype(bfloat16)
    input_buffers = data.inputs
    output_buffers = {"C": c_gelu}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.06, abs_tol=2e-2
    )

    record_metric("Throughput", (2.0 * M * K) / (latency_us * 1e-6) / 1e9)

    assert not errors, f"Test failed with errors: {errors}"
