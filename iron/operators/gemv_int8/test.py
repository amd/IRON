#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.gemv_int8.op import GEMVInt8
from iron.operators.gemv_int8.reference import generate_golden_reference, pack_payload
from iron.common.test_utils import run_test


def get_params():
    """(M, K, num_aie_columns, tile_size_input, tile_size_output).

    K must be a multiple of GROUP_SIZE=128 and of the kernel vector width (128);
    M must divide evenly by the column count and by tile_size_output.  The int8
    payload keeps every weight exact in bf16, so the only error source is the
    bf16 accumulation over K.
    """
    max_aie_columns = aie_utils.get_current_device().cols

    params_list = [
        (512, 1024, 1, 2, 32),
        (2048, 4096, 1, 2, 128),
        (2048, 4096, 2, 2, 64),
        (4096, 2048, 4, 2, 64),
        (2048, 4096, 8, 2, 32),
        (8192, 2048, 8, 4, 64),
    ]
    params = []
    for p in params_list:
        if p[2] > max_aie_columns:
            continue
        params.append(pytest.param(*p, id=f"m{p[0]}k{p[1]}c{p[2]}tsi{p[3]}"))
    return params


@pytest.mark.supported_devices("npu2")
@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize(
    "M,K,num_aie_columns,tile_size_input,tile_size_output", get_params()
)
@pytest.mark.parametrize("domain", ["biased", "signed"])
def test_gemv_int8(M, K, num_aie_columns, tile_size_input, tile_size_output, domain,
                   aie_context):
    from iron.common.context import AIEContext
    ctx = AIEContext(
        build_dir=f"build/test_gemv_int8/{domain}_m{M}k{K}c{num_aie_columns}"
                  f"tsi{tile_size_input}"
    )
    golden = generate_golden_reference(M=M, K=K)

    operator = GEMVInt8(
        M=M,
        K=K,
        num_aie_columns=num_aie_columns,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        kernel_source=None if domain == "biased" else "mv_int8_signed.cc",
        context=ctx,
    )

    wire = pack_payload(golden["w_int8"], golden["scales"], num_aie_columns,
                        tile_size_input, domain)
    spec = operator.get_arg_spec()
    assert wire.numel() == spec[0].shape[0], (wire.numel(), spec[0].shape)

    input_buffers = {"weights": wire.flatten(), "vector": golden["B"]}
    output_buffers = {"output": golden["C"]}

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.04, abs_tol=1e-2
    )

    print(f"\nLatency: {latency_us:.1f} us")
    gbps = (M * K) / (latency_us * 1e-6) / 1e9
    print(f"Throughput: {gbps:.6e} GFLOP/s")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"
