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
    # The design is a fixed 4x8 grid, so it needs all 8 columns.
    if dev.cols < 8 or dev.resolve().name != "npu2":
        return []

    # N values that are NOT a multiple of N_TILE*COLS=1024 exercise the
    # trailing partial column-block, where some columns compute it and the
    # rest only drain the A broadcast. Real transformer o/down projections
    # have N = model dim, so they always land here: 1536 leaves 4 active
    # columns, 2560 leaves 4, and 128 leaves just 1.
    # fmt: off
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

    # This design's r=8 mmul shape exists only on the bfp16-emulated path, so
    # its error budget is that of an emulated GEMM, not of the exact one the
    # GEMM operator's test asserts on (that test opts into r=4 via
    # emulate_bf16_mmul_with_bfp16=False, which is not available here).
    #
    # A pure relative tolerance cannot work: with signed A the K-term sum
    # cancels by ~sqrt(K), so |C| is ~20x smaller than the accumulated
    # magnitude while the error tracks that magnitude, leaving near-zero
    # outputs relatively uncheckable. So the error is bounded in ABSOLUTE terms
    # against the accumulated mass, which is what bfp16 error actually scales
    # with. Measured on this data: mean |err| is 0.00042 of the mass and the
    # worst element 0.0025 -- both marginally better than the GEMM operator run
    # in the same emulated mode (0.00044 / 0.0031), so the budget below is not
    # papering over a regression in this port. The bound is tight enough to
    # have caught a real bug: leaving the core in its default floor rounding
    # mode pushes mean error to 0.0099 of mass, ~7x over.
    mass = K * golden_ref["input"].abs().float().mean() * (
        golden_ref["input_b"].abs().float().mean()
    )
    #
    # floor rounding truncates rather than rounding to nearest, so its bias
    # accumulates over the K reduction instead of cancelling: ~0.0099 of mass
    # rather than ~0.00042, measured, and bit-identical to the shipped overlay.
    # It gets a bound to match; holding it to the conv_even budget would just
    # fail.
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


@pytest.mark.parametrize(
    "M,K,N",
    [
        (1024, 10240, 2560),  # E4B down-proj: K overflows the shim's 20-bit stride
        (1024, 2560, 10240),  # E4B gateup-proj: N overflows it instead
    ],
)
def test_flm_gemm_stride_overflow_rejected(M, K, N, aie_context):
    # K or N > ~8191 at M > 256 needs a shim DMA descriptor stride that
    # exceeds the AIE2p shim's 20-bit step field. Splitting the transfer
    # into multiple descriptors compiles but hangs real hardware (see
    # design.py's comment above this check) -- so this must keep failing
    # fast at construction, not silently emit a build that hangs.
    with pytest.raises(ValueError, match="20-bit step field"):
        FLMGEMM(M=M, K=K, N=N, context=aie_context).compile()
