#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import aie.utils as aie_utils

from iron.operators import GEMM as GenericGEMM
from iron.operators.flm.gemm.design import Epilogue, Rounding
from iron.operators.flm.gemm.op import GEMM
from iron.operators.flm.gemm.reference import generate_golden_reference
from iron.common.test_utils import run_test

# Unpacked so the parameter tables below stay column-aligned.
NONE, GELU, SILU, SIGMOID = Epilogue
CONV_EVEN, FLOOR = Rounding

# Activation tests run at a smaller scale so the result lands where the curve
# is not flat. generate_golden_reference grows the result like sqrt(K)*scale**2,
# so at the default 4.0 a K=512 product sits around +-200, where gelu and silu
# are indistinguishable from the identity.
INPUT_SCALE = 4.0
ACTIVATION_INPUT_SCALE = 0.5


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
            (  256,  512,  1024, NONE,     None,       CONV_EVEN),  # smallest full sweep
            (  512, 1024,  2048, NONE,     None,       CONV_EVEN),
            (  256,  512,  1536, NONE,     None,       CONV_EVEN),  # remainder: 4 of 8 cols
            (  256,  512,   128, NONE,     None,       CONV_EVEN),  # remainder only: 1 col
            (  256,  512,  1024, SILU,     None,       CONV_EVEN),
            (  256,  512,  1024, GELU,     None,       CONV_EVEN),
            (  256,  512,  1024, NONE, (-2.0, 2.0),    CONV_EVEN),
            # floor reproduces the shipped FastFlowLM overlay's rounding mode
            # (bit for bit on NPU2; NPU1 sums the K reduction in a different
            # order). It is much less accurate, so it gets its own bound below.
            (  256,  512,  1024, NONE,     None,       FLOOR),
        ]
        extensive_params = [
            ( 1024, 2048,  2048, NONE,     None,       CONV_EVEN),
            ( 2048, 2048,  2048, NONE,     None,       CONV_EVEN),
            ( 1024, 2560,  2560, NONE,     None,       CONV_EVEN),  # E4B o-proj
            (  512, 1536,  1536, SILU,     None,       CONV_EVEN),  # E2B down-proj
            (  256,  512,  1024, SIGMOID,  None,       CONV_EVEN),
            (  512, 1024,  2048, SILU, (-4.0, 4.0),    CONV_EVEN),
            (  256,  512,  1024, SILU,     None,       FLOOR),
            # K or N = 10240 at M > 256 overflows the shim BD's 20-bit
            # mega_row iteration step, so that leg is issued as one transfer
            # per mega_row, retired in windows. These are the real E4B FFN
            # projections and were unsupported until that landed; they are
            # the regression cover for it. M=2048 needs two windows, which is
            # what exercises the windowing.
            ( 1024, 10240,  2560, NONE,     None,       CONV_EVEN),  # E4B down
            ( 1024,  2560, 10240, NONE,     None,       CONV_EVEN),  # E4B gateup
            ( 2048, 10240,  2560, NONE,     None,       CONV_EVEN),  # A, 2 windows
            ( 2048,  2560, 10240, NONE,     None,       CONV_EVEN),  # C, 2 windows
        ]
    else:  # npu1: _default_tile_n always returns 64 here, so with 4 columns
        # every sweep is N_TILE*COLS = 256 wide, not the 128*4=512 an
        # NPU2-shaped sweep would give.
        #      M,    K,     N, epilogue,    clamp,     rounding
        regular_params = [
            (  256,  512,   256, NONE,     None,       CONV_EVEN),  # smallest full sweep
            (  512, 1024,   512, NONE,     None,       CONV_EVEN),
            (  256,  512,   128, NONE,     None,       CONV_EVEN),  # remainder: 2 of 4 cols
            (  256,  512,    64, NONE,     None,       CONV_EVEN),  # remainder only: 1 col
            (  256,  512,   320, NONE,     None,       CONV_EVEN),  # full sweep + 1 col
            (  256,  512,   512, SILU,     None,       CONV_EVEN),
            (  256,  512,   512, GELU,     None,       CONV_EVEN),
            (  256,  512,   512, NONE, (-2.0, 2.0),    CONV_EVEN),
            (  256,  512,   512, NONE,     None,       FLOOR),
        ]
        extensive_params = [
            ( 1024, 2048,  1024, NONE,     None,       CONV_EVEN),
            ( 2048, 2048,  1024, NONE,     None,       CONV_EVEN),
            ( 1024, 2560,  2560, NONE,     None,       CONV_EVEN),  # E4B o-proj
            (  512, 1536,  1536, SILU,     None,       CONV_EVEN),  # E2B down-proj
            (  256,  512,   512, SIGMOID,  None,       CONV_EVEN),
            (  512, 1024,  1024, SILU, (-4.0, 4.0),    CONV_EVEN),
            (  256,  512,   512, SILU,     None,       FLOOR),
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
def test_gemm(M, K, N, epilogue, clamp, rounding, aie_context):
    scale = INPUT_SCALE if epilogue is NONE else ACTIVATION_INPUT_SCALE
    golden_ref = generate_golden_reference(
        M=M, K=K, N=N, epilogue=epilogue, clamp=clamp, scale=scale
    )

    operator = GEMM(
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
        # B is consumed pre-packed; see GEMM.pack_B.
        "B": operator.pack_B(golden_ref["input_b"]),
    }
    output_buffers = {"C": golden_ref["output"].flatten()}

    # The rule: bound the error in ABSOLUTE terms as a fraction of the
    # accumulated mass, i.e. the expected size of the K reduction before
    # cancellation, K * mean|a| * mean|b|. A plain relative tolerance cannot
    # work, because with signed A the K-sum cancels by ~sqrt(K), so |C| is far
    # smaller than the mass while the error tracks the mass -- which leaves
    # near-zero outputs relatively uncheckable.
    mass = (
        K
        * golden_ref["input"].abs().float().mean()
        * (golden_ref["input_b"].abs().float().mean())
    )
    # The fraction is per-architecture, because the two lower the same 8x8x8
    # mmul shape onto very different arithmetic: NPU2 emulates it with bfp16,
    # which drops mantissa bits, while NPU1 has no bfp16 and lowers it onto
    # four native bf16 macs accumulating in f32, which is exact up to the
    # f32->bf16 store and so gets a ~20x tighter budget.
    #
    # floor rounding truncates rather than rounding to nearest, so its bias
    # accumulates over the K reduction instead of cancelling, hence the
    # separate, looser bound on both.
    if aie_utils.get_current_device().resolve().name == "npu1":
        budget = 0.002 if rounding is FLOOR else 0.0002
    else:
        budget = 0.05 if rounding is FLOOR else 0.004
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


def test_gemm_split_leg_windowing(aie_context):
    """K or N = 10240 at M > 256 overflows the shim BD's 20-bit mega_row
    iteration step, so that leg is issued as one transfer per mega_row,
    retired in windows of at most SHIM_TASK_QUEUE. Two shim resources bound it
    and NEITHER is modelled by the toolchain -- the BD ids (16/tile, freed
    without a completion check) and the channel task queue (4 deep, pushed
    unconditionally) -- so overrunning either is a silent device hang rather
    than a diagnostic.

    Windowing keeps both inside their limits for every shape: at most
    1 B + 4 A + 4 C = 9 of 16 descriptors, and at most 4 outstanding per
    channel. Assert that arithmetic here, since the numbers come from the
    hardware and a future retune of SHIM_TASK_QUEUE could break it silently.
    """
    from aie.dialects.aie import get_target_model
    from iron.operators.flm.gemm.design import SHIM_TASK_QUEUE

    dev = aie_utils.get_current_device()
    available = get_target_model(dev.resolve()).get_num_bds(0, 0)
    worst = 1 + 2 * SHIM_TASK_QUEUE
    assert worst <= available, (
        f"a fully split block needs {worst} shim BDs of {available}; "
        "windowing no longer fits and the split shapes will hang"
    )

    # The square case splits BOTH legs, which the real Gemma shapes never do
    # (E4B's down-proj overflows on K and its gate/up on N, never both), so it
    # is the only cover for the two-sided path.
    GEMM(M=512, K=10240, N=10240, context=aie_context).compile()


@pytest.mark.extensive
def test_gemm_split_leg_windowing_runs(aie_context):
    """Execute the two-sided split path, not just compile it.

    test_gemm_split_leg_windowing above only compiles this shape: the failure
    mode it guards against -- BD-id aliasing and shim task-queue overrun (see
    that test's docstring) -- is a runtime device hang or silent corruption,
    which compiling the MLIR can't exercise. This dispatches the same shape on
    hardware and checks the result.
    """
    M, K, N = 512, 10240, 10240
    golden_ref = generate_golden_reference(M=M, K=K, N=N)

    operator = GEMM(M=M, K=K, N=N, context=aie_context)

    input_buffers = {
        "A": golden_ref["input"].flatten(),
        "B": operator.pack_B(golden_ref["input_b"]),
    }
    output_buffers = {"C": golden_ref["output"].flatten()}

    # Same mass-based bound as test_gemm, at the non-floor budget for whichever
    # architecture this runs on.
    mass = (
        K
        * golden_ref["input"].abs().float().mean()
        * golden_ref["input_b"].abs().float().mean()
    )
    budget = (
        0.0002 if aie_utils.get_current_device().resolve().name == "npu1" else 0.004
    )
    errors, _latency_us, _bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        rel_tol=0.04,
        abs_tol=float(budget * mass),
    )
    assert not errors, "Test failed"


@pytest.mark.parametrize("M,K,N", [(256, 512, 1024), (512, 1024, 2048)])
def test_artifact_stem_differs_from_generic_gemm(M, K, N, aie_context):
    """``flm.GEMM`` must never share an artifact stem with ``GEMM``.

    Both classes are named ``GEMM``, and MLIROperator.name derives the stem
    from the class name, while this repo's build cache keys on filename and
    mtime rather than on source or flags -- so a shared stem would let the two
    operators silently satisfy each other's builds in one build dir.
    """
    assert (
        GEMM(M=M, K=K, N=N, context=aie_context).name
        != GenericGEMM(M=M, K=K, N=N, context=aie_context).name
    )
