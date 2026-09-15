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
    M_CHUNK_FOR_N,
    Epilogue,
    M_TILE,
    R,
    Rounding,
    SHIM_TASK_QUEUE,
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

    # One full sweep is N_TILE * COLS wide, so both it and the N values that
    # leave a trailing partial column-block differ per device. The trailing
    # case is the interesting one: some columns compute the block while the
    # rest only drain the A broadcast, and real o/down projections always land
    # there. At K = 512 tile_n defaults to 128, halving at K >= 1024.
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
            # mega_row iteration step, so that leg goes out as one transfer
            # per mega_row against a bounded outstanding count. These are the
            # real E4B FFN projections, unsupported until that landed, and
            # M=2048 is what pushes past the bound.
            ( 1024, 10240,  2560, NONE,     None,       CONV_EVEN),  # E4B down
            ( 1024,  2560, 10240, NONE,     None,       CONV_EVEN),  # E4B gateup
            ( 2048, 10240,  2560, NONE,     None,       CONV_EVEN),  # E4B down, 2x
            ( 2048,  2560, 10240, NONE,     None,       CONV_EVEN),  # E4B gateup, 2x
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

    Bounds the error absolutely, as a fraction of the accumulated mass
    K * mean|a| * mean|b|. A relative tolerance cannot work: with signed A the
    K-sum cancels by ~sqrt(K), so |C| ends up far smaller than the mass the
    error tracks, leaving near-zero outputs uncheckable.

    The fraction is per-architecture, since NPU2 emulates the mmul with bfp16
    while NPU1 accumulates four native bf16 macs in f32 (~20x tighter). floor
    truncates, so its bias accumulates and gets a looser bound on both.
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


def test_gemm_split_leg_bounds(aie_context):
    """K or N = 10240 overflows the shim BD's 20-bit mega_row step, so that leg
    goes out one transfer per mega_row. Two unmodelled shim resources bound how
    many may be live -- BD ids and the channel task queue -- and overrunning
    either hangs silently. The live set is 4 + 2 + 2 = 8 of 16 descriptors;
    assert that here, since retuning SHIM_TASK_QUEUE could break it silently.
    """
    dev = aie_utils.get_current_device()
    available = get_target_model(dev.resolve()).get_num_bds(0, 0)
    worst = SHIM_TASK_QUEUE + 2 + 2
    assert worst <= available, (
        f"a fully split block needs {worst} shim BDs of {available}; "
        "the split shapes will hang"
    )

    # The square case splits both legs, which the real Gemma shapes never do
    # (E4B's down overflows on K and its gate/up on N, never both), so it is
    # the only cover for the two-sided path.
    GEMM(M=512, K=10240, N=10240, context=aie_context).compile()


def test_gemm_split_leg_bounds_runs(aie_context):
    """Execute the two-sided split path, not just compile it.

    The failure the sibling test guards against is a runtime hang or silent
    corruption, which compiling cannot exercise. Regular rather than extensive
    despite the size: ~8s against the suite's ~13s.
    """
    M, K, N = 512, 10240, 10240
    golden_ref = generate_golden_reference(M=M, K=K, N=N)

    operator = GEMM(M=M, K=K, N=N, context=aie_context)

    errors, _latency_us, _bandwidth_gbps = check_on_device(operator, golden_ref, K)
    assert not errors, "Test failed"


def tile_option_params():
    """Every (tile_n, tile_ma) the design accepts on this device.

    The shape parameters above only exercise the default geometry, since
    __post_init__ resolves both knobs. These cover the knobs themselves, which
    change the blocked L1 layout, and a mismatch is silently wrong output
    rather than a build error, so each has to run on hardware. The defaults
    stay in the regular suite; the overrides are extensive, since each is its
    own kernel object and xclbin.
    """
    dev = aie_utils.get_current_device()
    if dev is None or dev.resolve().name not in ("npu1", "npu2"):
        return []
    l1 = get_target_model(dev.resolve()).get_local_memory_size()
    b_elem = BFP16_GROUP_BYTES / BFP16_GROUP if dev.arch == AIEArch.AIE2p else 2

    params = []
    for tile_n, ct_k in sorted(CT_MAX_K_FOR_N.items()):
        # m_chunk matters: the core holds a B chunk across that many
        # accumulators, so it is what decides which A heights still fit.
        m_chunk = M_CHUNK_FOR_N[tile_n]
        default_ma = _default_l1(tile_n, ct_k, b_elem, l1, m_chunk)[0]
        # One full sweep of the grid at this tile_n, so every column has work.
        M, K, N = 256, 512, tile_n * dev.cols
        for tile_ma in (16, 32, 64):
            if M_TILE % tile_ma or tile_ma % (2 * R):
                continue
            try:
                _b_depth_for(tile_ma, tile_n, ct_k, b_elem, l1, m_chunk)
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

    Both classes are named ``GEMM`` and MLIROperator.name derives the stem from
    the class name, so with the cache keyed on filename the two operators would
    silently satisfy each other's builds in one build dir.
    """
    assert (
        GEMM(M=M, K=K, N=N, context=aie_context).name
        != GenericGEMM(M=M, K=K, N=N, context=aie_context).name
    )


def test_one_xclbin_serves_every_shape(aie_context):
    """Several shapes back to back on one loaded xclbin.

    The parametrised tests cannot cover this: each gets a fresh context, so
    the array is reconfigured between cases. Here the shapes share one, they
    disagree on every parameter, and none may rebuild the xclbin.
    """
    # Every shape must resolve to the same m_chunk, which shapes the core
    # program and so the xclbin. These are all even in m_row_blocks and exclude
    # the K that would overflow the A descriptor's step.
    shapes = [
        (512, 1536, 2048, "none"),
        (512, 1536, 256, "none"),  # only 4 of 8 columns compute
        (1024, 2048, 1536, "none"),
        (512, 1536, 6144, "gelu"),
        (512, 1536, 2048, "none"),  # back to the first, after the rest
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


def test_one_xclbin_serves_every_clamp_bound(aie_context):
    """Different clamp bounds back to back on one loaded xclbin.

    The bounds are runtime parameters, so they must not rebuild anything.
    Separate from test_one_xclbin_serves_every_shape, which never clamps and so
    cannot catch bounds leaking back into the configuration.
    """
    M, K, N = 256, 512, 1024
    bounds = [(-2.0, 2.0), (-4.0, 4.0), (-0.5, 0.5)]
    xclbin = None
    for clamp in bounds:
        operator = GEMM(M=M, K=K, N=N, clamp=clamp, context=aie_context)
        golden_ref = generate_golden_reference(
            M=M, K=K, N=N, clamp=clamp, scale=INPUT_SCALE
        )
        errors, _, _ = check_on_device(operator, golden_ref, K)
        assert not errors, f"clamp={clamp} produced wrong output"

        stamp = (
            operator.xclbin_artifact.filename,
            os.path.getmtime(operator.xclbin_artifact.filename),
        )
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"clamp={clamp} rebuilt the xclbin"

    # ...and neither does dropping the clamp: the kernel always clamps, and an
    # unclamped caller neutralises it with (-inf, +inf) rather than compiling
    # a second build. config_name rather than xclbin_artifact, which only
    # exists once compile() has run.
    clamped = GEMM(M=M, K=K, N=N, clamp=bounds[0], context=aie_context)
    unclamped = GEMM(M=M, K=K, N=N, context=aie_context)
    assert unclamped.config_name == clamped.config_name
    # The bounds do reach the instruction stream, though, so they must reach
    # its stem or the build cache serves one caller's stream to another.
    assert unclamped.name != clamped.name
    assert (
        clamped.name != GEMM(M=M, K=K, N=N, clamp=bounds[1], context=aie_context).name
    )
