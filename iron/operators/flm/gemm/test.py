#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os

import pytest
import aie.utils as aie_utils

from aie.dialects.aie import get_target_model
from aie.dialects._aie_enum_gen import AIEArch

from iron.operators import GEMM as GenericGEMM
from iron.operators.flm.gemm.design import (
    BFP16_GROUP,
    BFP16_GROUP_BYTES,
    CT_MAX_K_FOR_N,
    Epilogue,
    M_TILE,
    R,
    Rounding,
    _b_depth_for,
    _default_l1,
)
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


def check_on_device(operator, golden_ref, K, rounding=CONV_EVEN):
    """Run ``operator`` against its golden reference and return run_test's result.

    Bounds the error in ABSOLUTE terms as a fraction of the accumulated mass,
    i.e. the expected size of the K reduction before cancellation,
    K * mean|a| * mean|b|. A plain relative tolerance cannot work: with signed A
    the K-sum cancels by ~sqrt(K), so |C| ends up far smaller than the mass
    while the error tracks the mass, leaving near-zero outputs uncheckable.

    The fraction is per-architecture, because the two lower the same 8x8x8 mmul
    onto very different arithmetic: NPU2 emulates it with bfp16, which drops
    mantissa bits, while NPU1 has no bfp16 and lowers onto four native bf16 macs
    accumulating in f32 -- exact up to the f32->bf16 store, so ~20x tighter.
    floor truncates rather than rounding to nearest, so its bias accumulates
    over the K reduction instead of cancelling and gets a looser bound on both.
    """
    mass = (
        K
        * golden_ref["input"].abs().float().mean()
        * golden_ref["input_b"].abs().float().mean()
    )
    if aie_utils.get_current_device().resolve().name == "npu1":
        budget = 0.002 if rounding is FLOOR else 0.0002
    else:
        budget = 0.05 if rounding is FLOOR else 0.004
    return run_test(
        operator,
        {
            "A": golden_ref["input"].flatten(),
            # B is consumed pre-packed; see GEMM.pack_B.
            "B": operator.pack_B(golden_ref["input_b"]),
        },
        {"C": golden_ref["output"].flatten()},
        rel_tol=0.04,
        abs_tol=float(budget * mass),
    )


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

    errors, latency_us, bandwidth_gbps = check_on_device(
        operator, golden_ref, K, rounding
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


def test_gemm_split_leg_windowing_runs(aie_context):
    """Execute the two-sided split path, not just compile it.

    test_gemm_split_leg_windowing above only compiles this shape: the failure
    mode it guards against -- BD-id aliasing and shim task-queue overrun (see
    that test's docstring) -- is a runtime device hang or silent corruption,
    which compiling the MLIR cannot exercise. This dispatches the same shape on
    hardware and checks the result.

    Regular rather than extensive despite being the largest shape here. What it
    catches is a hang or silently wrong output, not a wrong number, and its
    compile-only sibling is already regular, so leaving the executing half out
    of the default run is the wrong side to err on. Costs ~8s against the
    regular suite's ~13s.
    """
    M, K, N = 512, 10240, 10240
    golden_ref = generate_golden_reference(M=M, K=K, N=N)

    operator = GEMM(M=M, K=K, N=N, context=aie_context)

    errors, _latency_us, _bandwidth_gbps = check_on_device(operator, golden_ref, K)
    assert not errors, "Test failed"


def tile_option_params():
    """Every (tile_n, tile_ma) the design accepts on this device.

    The shape parameters above exercise only the DEFAULT tile geometry, because
    __post_init__ resolves both knobs from the shape and the device. These cover
    the knobs themselves, which change the blocked L1 layout: tile_n selects
    CT_MAX_K and the B object width, tile_ma sets the mmul's rowA and the A
    object height, and pack_B, the four stream-dimension lists and gather_dims
    all key off them. A mismatch is silently wrong output rather than a build
    error, so each combination has to actually run on hardware.

    The default tile_ma per tile_n stays in the regular suite; the overrides are
    extensive, since each is its own kernel object and xclbin.
    """
    dev = aie_utils.get_current_device()
    if dev is None or dev.resolve().name not in ("npu1", "npu2"):
        return []
    l1 = get_target_model(dev.resolve()).get_local_memory_size()
    b_elem = BFP16_GROUP_BYTES / BFP16_GROUP if dev.arch == AIEArch.AIE2p else 2

    params = []
    for tile_n, ct_k in sorted(CT_MAX_K_FOR_N.items()):
        default_ma = _default_l1(tile_n, ct_k, b_elem, l1)[0]
        # One full sweep of the grid at this tile_n, so every column has work.
        M, K, N = 256, 512, tile_n * dev.cols
        for tile_ma in (16, 32, 64):
            if M_TILE % tile_ma or tile_ma % (2 * R):
                continue
            try:
                _b_depth_for(tile_ma, tile_n, ct_k, b_elem, l1)
            except ValueError:
                continue  # this A height leaves no room for B at this width
            marks = [] if tile_ma == default_ma else [pytest.mark.extensive]
            params.append(
                pytest.param(
                    M,
                    K,
                    N,
                    tile_n,
                    tile_ma,
                    marks=marks,
                    id=f"tn{tile_n}-ma{tile_ma}" + ("-default" if not marks else ""),
                )
            )
    return params


@pytest.mark.parametrize("M,K,N,tile_n,tile_ma", tile_option_params())
def test_gemm_tile_options(M, K, N, tile_n, tile_ma, aie_context):
    """Each accepted (tile_n, tile_ma) computes the right answer on hardware."""
    golden_ref = generate_golden_reference(M=M, K=K, N=N, scale=INPUT_SCALE)
    operator = GEMM(M=M, K=K, N=N, tile_n=tile_n, tile_ma=tile_ma, context=aie_context)
    assert operator.tile_n == tile_n and operator.tile_ma == tile_ma
    errors, _latency_us, _bandwidth_gbps = check_on_device(operator, golden_ref, K)
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


def test_one_xclbin_serves_every_shape(aie_context):
    """Several shapes back to back on one loaded xclbin.

    This is what the runtime parameters are for, and the parametrised tests
    above cannot cover it: each gets a fresh context, so the array is
    reconfigured between cases and any state a dispatch leaves behind is
    wiped. Here the shapes share one.

    They disagree on every parameter -- M, K, N, whether a column sits a block
    out, and the activation -- and none of them may rebuild the xclbin.
    """
    shapes = [
        (256, 1536, 2048, "none"),
        (256, 1536, 256, "none"),  # only 4 of 8 columns compute
        (512, 2048, 1536, "none"),
        (256, 1536, 6144, "gelu"),
        (256, 1536, 2048, "none"),  # back to the first, after the rest
    ]
    xclbin = None
    for M, K, N, epilogue in shapes:
        operator = GEMM(M=M, K=K, N=N, epilogue=epilogue, context=aie_context)
        golden_ref = generate_golden_reference(
            M=M, K=K, N=N, epilogue=epilogue, scale=4.0 if epilogue == "none" else 0.5
        )
        mass = (
            K
            * golden_ref["input"].abs().float().mean()
            * golden_ref["input_b"].abs().float().mean()
        )
        errors, _, _ = run_test(
            operator,
            {
                "A": golden_ref["input"].flatten(),
                "B": operator.pack_B(golden_ref["input_b"]),
            },
            {"C": golden_ref["output"].flatten()},
            rel_tol=0.04,
            abs_tol=float(0.004 * mass),
        )
        assert not errors, f"{M}x{K}x{N} {epilogue} failed"

        stamp = (
            operator.xclbin_artifact.filename,
            os.path.getmtime(operator.xclbin_artifact.filename),
        )
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"{M}x{K}x{N} rebuilt the xclbin"
