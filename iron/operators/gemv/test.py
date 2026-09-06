#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils
from ml_dtypes import bfloat16

from iron.operators.gemv.op import GEMV
from iron.operators.gemv.design import _shim_gran_elems, split_run
from iron.operators.gemv.reference import (
    generate_golden_reference,
    generate_golden_reference_batched,
    gelu_tanh_approx,
)
from iron.common.device_utils import get_kernel_dir
import numpy as np
import torch
from iron.common.test_utils import run_test


def test_shim_gran_elems_matches_dtype():
    """GRAN_ELEMS used to be hard-coded to 2 (4-byte shim granule / 2-byte bf16), regardless
    of what dtype was actually being transferred. Assert it now tracks the element width, and
    that split_run's alignment is only correct when it does.
    """
    bf16_ty = np.dtype[bfloat16]
    i8_ty = np.dtype[np.int8]
    f32_ty = np.dtype[np.float32]

    assert _shim_gran_elems(bf16_ty) == 2
    assert _shim_gran_elems(i8_ty) == 4
    assert _shim_gran_elems(f32_ty) == 1

    # Concrete regression: at the old hard-coded gran=2, this run's best split has a lo
    # (514) that is not a multiple of 4 -- illegal for a dtype whose real granule is 4
    # (e.g. int8). Deriving gran from the dtype (as my_matvec's A_gran/C_gran now do)
    # gives the aligned split instead.
    run = 1028
    wrong = split_run(run, gran=2)
    right = split_run(run, gran=_shim_gran_elems(i8_ty))
    assert wrong == (2, 514) and wrong[1] % 4 != 0
    assert right == (257, 4) and right[1] % 4 == 0


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


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output", get_params()
)
def test_gemv(M, K, num_aie_columns, tile_size_input, tile_size_output, aie_context):
    golden_ref = generate_golden_reference(M=M, K=K)

    operator = GEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        context=aie_context,
    )

    input_buffers = {"matrix": golden_ref["A"].flatten(), "vector": golden_ref["B"]}
    output_buffers = {"output": golden_ref["C"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-3
    )

    print(f"\nLatency: {latency_us:.1f} us")

    gflops = (2.0 * M * K) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.6e} GFLOP/s")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

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


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output,num_batches",
    get_batched_params(),
)
def test_gemv_batched(
    M, K, num_aie_columns, tile_size_input, tile_size_output, num_batches, aie_context
):
    golden = generate_golden_reference_batched(M=M, K=K, num_batches=num_batches)
    operator = GEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        num_batches=num_batches,
        context=aie_context,
    )
    input_buffers = {
        "matrix": golden["A"].flatten(),
        "vector": golden["B"].flatten(),
    }
    output_buffers = {"output": golden["C"].flatten()}
    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-3
    )

    print(f"\nLatency: {latency_us:.1f} us")
    gflops = (2.0 * M * K * num_batches) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.6e} GFLOP/s")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"batched GEMV failed: {errors}"


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output",
    [
        pytest.param(128, 128, 1, 32, 128),
        pytest.param(2048, 8192, 1, 1, 2048),
        pytest.param(8192, 2048, 1, 4, 1024),
    ],
)
def test_gemv_gelu(
    M, K, num_aie_columns, tile_size_input, tile_size_output, aie_context
):
    """GEMV with the fused GELU epilogue (NPU2-only) vs a gelu(A @ B) golden."""
    if get_kernel_dir() != "aie2p":
        pytest.skip("gemv gelu epilogue is only available on NPU2 (aie2p)")

    golden_ref = generate_golden_reference(M=M, K=K)
    c_ref = golden_ref["C"].to(torch.float32).numpy()
    c_gelu = torch.from_numpy(gelu_tanh_approx(c_ref).astype(np.float32)).to(
        torch.bfloat16
    )

    operator = GEMV(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        epilogue="gelu",
        context=aie_context,
    )

    input_buffers = {"matrix": golden_ref["A"].flatten(), "vector": golden_ref["B"]}
    output_buffers = {"output": c_gelu}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.06, abs_tol=2e-2
    )

    print(f"\nLatency: {latency_us:.1f} us")
    gflops = (2.0 * M * K) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gflops:.6e} GFLOP/s")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
