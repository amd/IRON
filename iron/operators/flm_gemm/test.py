#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators.flm_gemm.op import FLMGEMM
from iron.operators.flm_gemm.reference import generate_golden_reference
from iron.common.test_utils import run_test


def get_params():
    dev = aie_utils.get_current_device()
    if dev is None:
        return []
    dev_name = dev.resolve().name
    if dev_name not in ("npu1", "npu2"):
        return []

    # The grid is 4 rows by as many columns as the device has, so the width of
    # one full sweep -- N_TILE * COLS -- differs per device, and so do the N
    # values that leave a trailing PARTIAL column-block. That trailing case is
    # the interesting one: some columns compute the block while the rest only
    # drain the A broadcast, and real transformer o/down projections always
    # land there, since N = model dim is essentially never a multiple of the
    # sweep width.
    #
    # At K = 512 there is a single k iteration, so tile_n defaults to 128 and a
    # sweep is 1024 wide on NPU2 and 512 on NPU1; at K >= 1024 tile_n drops to
    # 64, halving both.
    # fmt: off
    if dev_name == "npu2":
        #      M,    K,     N, epilogue,    clamp,     rounding
        regular_params = [
            (  256,  512,  1024, "none",     None,       "conv_even"),  # smallest full sweep
            (  512, 1024,  2048, "none",     None,       "conv_even"),
            (  256,  512,  1536, "none",     None,       "conv_even"),  # remainder: 4 of 8 cols
            (  256,  512,   128, "none",     None,       "conv_even"),  # remainder only: 1 col
            (  256,  512,  1024, "silu",     None,       "conv_even"),
            (  256,  512,  1024, "gelu",     None,       "conv_even"),
            (  256,  512,  1024, "none", (-2.0, 2.0),    "conv_even"),
            # floor reproduces the shipped FastFlowLM overlay bit for bit; it is
            # much less accurate, so it gets its own bound below.
            (  256,  512,  1024, "none",     None,       "floor"),
        ]
        extensive_params = [
            ( 1024, 2048,  2048, "none",     None,       "conv_even"),
            ( 2048, 2048,  2048, "none",     None,       "conv_even"),
            ( 1024, 2560,  2560, "none",     None,       "conv_even"),  # E4B o-proj
            (  512, 1536,  1536, "silu",     None,       "conv_even"),  # E2B down-proj
            (  256,  512,  1024, "sigmoid",  None,       "conv_even"),
            (  512, 1024,  2048, "silu", (-4.0, 4.0),    "conv_even"),
            (  256,  512,  1024, "silu",     None,       "floor"),
        ]
    else:  # npu1: 4 columns, so every sweep width above halves
        #      M,    K,     N, epilogue,    clamp,     rounding
        regular_params = [
            (  256,  512,   512, "none",     None,       "conv_even"),  # smallest full sweep
            (  512, 1024,  1024, "none",     None,       "conv_even"),
            (  256,  512,   256, "none",     None,       "conv_even"),  # remainder: 2 of 4 cols
            (  256,  512,   128, "none",     None,       "conv_even"),  # remainder only: 1 col
            (  256,  512,   640, "none",     None,       "conv_even"),  # full sweep + 1 col
            (  256,  512,   512, "silu",     None,       "conv_even"),
            (  256,  512,   512, "gelu",     None,       "conv_even"),
            (  256,  512,   512, "none", (-2.0, 2.0),    "conv_even"),
            (  256,  512,   512, "none",     None,       "floor"),
        ]
        extensive_params = [
            ( 1024, 2048,  1024, "none",     None,       "conv_even"),
            ( 2048, 2048,  1024, "none",     None,       "conv_even"),
            ( 1024, 2560,  2560, "none",     None,       "conv_even"),  # E4B o-proj
            (  512, 1536,  1536, "silu",     None,       "conv_even"),  # E2B down-proj
            (  256,  512,   512, "sigmoid",  None,       "conv_even"),
            (  512, 1024,  1024, "silu", (-4.0, 4.0),    "conv_even"),
            (  256,  512,   512, "silu",     None,       "floor"),
        ]
    # fmt: on

    params = []
    for p in regular_params:
        params.append(pytest.param(*p))
    for p in extensive_params:
        params.append(pytest.param(*p, marks=[pytest.mark.extensive]))
    return params


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
    Throughput=r"Throughput: (?P<value>[\d\.e\+-]+) GFLOP/s",
)
@pytest.mark.parametrize("M,K,N,epilogue,clamp,rounding", get_params())
def test_flm_gemm(M, K, N, epilogue, clamp, rounding, aie_context):
    # Keep the activation tests in the range where the curve is not flat.
    scale = 4.0 if epilogue == "none" else 0.5
    golden_ref = generate_golden_reference(
        M=M, K=K, N=N, epilogue=epilogue, clamp=clamp, scale=scale
    )

    operator = FLMGEMM(
        M=M,
        K=K,
        N=N,
        epilogue=epilogue,
        clamp=clamp,
        rounding=rounding,
        context=aie_context,
    )

    input_buffers = {
        "A": golden_ref["input"].flatten(),
        # B is consumed pre-packed; see FLMGEMM.pack_B.
        "B": operator.pack_B(golden_ref["input_b"]),
    }
    output_buffers = {"C": golden_ref["output"].flatten()}

    # A pure relative tolerance cannot work: with signed A the K-term sum
    # cancels by ~sqrt(K), so |C| is ~20x smaller than the accumulated
    # magnitude while the error tracks that magnitude, leaving near-zero
    # outputs relatively uncheckable. So the error is bounded in ABSOLUTE terms
    # against the accumulated mass, which is what the error actually scales
    # with.
    mass = (
        K
        * golden_ref["input"].abs().float().mean()
        * (golden_ref["input_b"].abs().float().mean())
    )
    #
    # The budget is per-architecture, because the two lower the same 8x8x8 mmul
    # shape onto very different arithmetic:
    #
    #   NPU2 emulates it with bfp16, which drops mantissa bits. Measured mean
    #     |err| is 0.00042 of mass (worst element 0.0025) -- marginally better
    #     than the GEMM operator run in the same emulated mode (0.00044 /
    #     0.0031), so this budget is not papering over a regression.
    #   NPU1 has no bfp16 and lowers it onto four NATIVE bf16 macs accumulating
    #     in f32, which is exact up to the f32->bf16 store. Measured mean |err|
    #     is under 1e-6 of mass with conv_even and 0.00015 with floor -- 7x and
    #     66x better than NPU2 respectively. Inheriting NPU2's budget here would
    #     leave ~70x of slack and stop the test being able to catch anything.
    #
    # floor rounding truncates rather than rounding to nearest, so its bias
    # accumulates over the K reduction instead of cancelling rather than
    # averaging out, hence the separate, looser bound on both.
    #
    # NOTE the "floor is bit-identical to the shipped FastFlowLM overlay" claim
    # holds on NPU2 only. NPU1 sums the K reduction in a different order, so it
    # reproduces the overlay's rounding MODE but not its exact results.
    if aie_utils.get_current_device().resolve().name == "npu1":
        budget = 0.002 if rounding == "floor" else 0.0002
    else:
        budget = 0.05 if rounding == "floor" else 0.004
    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        rel_tol=0.04,
        abs_tol=float(budget * mass),
    )

    gflops = (2.0 * M * K * N) / (latency_us * 1e-6) / 1e9
    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s")
    print(f"Throughput: {gflops:.6e} GFLOP/s\n")

    assert not errors, "Test failed"
