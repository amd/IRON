#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.dialects._aie_enum_gen import AIEArch
from aie.utils.verify import Tolerance

from iron.common.design.build import build_design
from iron.common.harness import run_test, vectors
from iron.common.image import OperatorImage
from iron.operators import GEMM as GenericGEMM
from iron.operators.flm.gemm.design import (
    BFP16_GROUP,
    BFP16_GROUP_BYTES,
    CT_MAX_K_FOR_N,
    M_CHUNK_FOR_N,
    M_TILE,
    Epilogue,
    Gelu,
    R,
    Rounding,
    _b_depth_for,
    _default_l1,
    l1_budget,
)
from iron.operators.flm.gemm.op import GEMM
from iron.operators.flm.gemm.shipped import Shipped

# Unpacked so the parameter tables below stay column-aligned.
NONE, GELU, SILU, SIGMOID = Epilogue
CONV_EVEN, FLOOR = Rounding

# Activation tests run at a smaller scale so the result lands where the curve
# is not flat. The golden product grows like sqrt(K)*scale**2,
# so at the default 4.0 a K=512 product sits around +-200, where gelu and silu
# are indistinguishable from the identity.
INPUT_SCALE = 4.0
ACTIVATION_INPUT_SCALE = 0.5


def get_params():
    dev = aie_utils.get_current_device()
    if dev is None:
        return []
    if dev.arch not in (AIEArch.AIE2, AIEArch.AIE2p):
        return []

    # One full sweep is N_TILE * COLS wide, so both it and the N values that
    # leave a trailing partial column-block differ per device. The trailing
    # case is the interesting one: some columns compute the block while the
    # rest only drain the A broadcast, and real o/down projections always land
    # there. At K = 512 tile_n defaults to 128, halving at K >= 1024.
    # fmt: off
    if dev.arch is AIEArch.AIE2p:
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
            # mega_row iteration step, so the compiler cuts that leg into
            # pieces, bounded by its queue polls and BD reclaim. These are the
            # real E4B FFN projections, and M=2048 doubles the pieces.
            ( 1024, 10240,  2560, NONE,     None,       CONV_EVEN),  # E4B down
            ( 1024,  2560, 10240, NONE,     None,       CONV_EVEN),  # E4B gateup
            ( 2048, 10240,  2560, NONE,     None,       CONV_EVEN),  # E4B down, 2x
            ( 2048,  2560, 10240, NONE,     None,       CONV_EVEN),  # E4B gateup, 2x
            # 64 row-block units, past the 63 a lock can count, so B is armed
            # twice: two slabs, each resident.
            (16384,  512,  1024, NONE,     None,       CONV_EVEN),
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
            # Two slabs, as on NPU2.
            (16384,  512,   256, NONE,     None,       CONV_EVEN),
        ]
    # fmt: on

    # Shapes that run for milliseconds. The default suite's shapes finish near
    # the dispatch cost, where the measurement carries no trend.
    bench_shapes = (
        {(1024, 2560, 10240), (2048, 2560, 10240)}
        if dev.arch is AIEArch.AIE2p
        else {(1024, 2560, 2560), (2048, 2048, 1024)}
    )

    def marks_for(p, extensive):
        marks = [pytest.mark.extensive] if extensive else []
        M, K, N, epilogue, clamp, rounding = p
        if (M, K, N) in bench_shapes and epilogue is NONE and clamp is None:
            marks.append(pytest.mark.bench)
        return marks

    params = []
    for p in regular_params:
        params.append(pytest.param(*p, marks=marks_for(p, extensive=False)))
    for p in extensive_params:
        params.append(pytest.param(*p, marks=marks_for(p, extensive=True)))
    return params


def flm_vectors(operator, scale=4.0):
    """Random A (signed) and B (non-negative) at ``scale``, and epilogue(A @ B).

    ``scale`` matters for the epilogue tests: the result grows like
    ``sqrt(K) * scale**2``, and at the default scale a K=512 product lands
    around +-200, where gelu/silu are indistinguishable from the identity (or
    from zero). Activation tests pass a smaller scale so the result sits in the
    range where the curve is actually interesting. B is drawn row-major
    ``(K, N)``, which the operator consumes packed (see ``GEMM.pack_B``), or
    ``(N, K)`` as stored under ``b_col_maj``.
    """
    K, N = operator.K, operator.N
    B = (N, K) if operator.b_col_maj else (K, N)
    return vectors(operator, normal=("A",), scale=scale, B=B)


def accumulated_mass(K, A, B):
    """K * mean|a| * mean|b|: the magnitude the accumulator's error tracks."""
    return float(
        K * np.abs(A.astype(np.float32)).mean() * np.abs(B.astype(np.float32)).mean()
    )


def check_on_device(operator, data, rounding=CONV_EVEN, record=None):
    """Run ``operator`` against its drawn vectors and return run_test's result.

    Bounds the error absolutely, as a fraction of the accumulated mass
    K * mean|a| * mean|b|. A relative tolerance cannot work: with signed A the
    K-sum cancels by ~sqrt(K), so |C| ends up far smaller than the mass the
    error tracks, leaving near-zero outputs uncheckable.

    The fraction is per-architecture, since NPU2 emulates the mmul with bfp16
    while NPU1 accumulates four native bf16 macs in f32 (~20x tighter). floor
    truncates, so its bias accumulates and gets a looser bound on both.
    ``record`` is run_test's.
    """
    A, B = data["A"], data["B"]
    mass = accumulated_mass(operator.K, A, B)
    dev = aie_utils.get_current_device()
    assert dev is not None
    if dev.arch is AIEArch.AIE2:
        budget = 0.002 if rounding is FLOOR else 0.0002
    else:
        budget = 0.05 if rounding is FLOOR else 0.004
    return run_test(
        operator,
        {
            "A": A.flatten(),
            "B": B.flatten() if operator.b_col_maj else operator.pack_B(B),
        },
        {"C": data["C"].flatten()},
        tolerance=Tolerance.relative(0.04, budget * mass),
        record=record,
    )


@pytest.mark.parametrize("M,K,N,epilogue,clamp,rounding", get_params())
def test_gemm(M, K, N, epilogue, clamp, rounding, npu_runtime, record_property):
    scale = INPUT_SCALE if epilogue is NONE else ACTIVATION_INPUT_SCALE
    operator = GEMM(
        M=M,
        K=K,
        N=N,
        epilogue=epilogue,
        clamp=clamp,
        rounding=rounding,
    )

    errors, _, _ = check_on_device(
        operator, flm_vectors(operator, scale), rounding, record=record_property
    )

    assert not errors, "Test failed"


@pytest.mark.parametrize("M,K,N", [(256, 512, 256), (512, 1024, 512)])
def test_gemm_without_activations(M, K, N, npu_runtime, record_property):
    """Compiling no activation links no LUT tables, so on AIE2 the bytes they
    held go to B and the tiles differ from every case above."""
    operator = GEMM(M=M, K=K, N=N, epilogue_modes=(NONE,))

    errors, _, _ = check_on_device(
        operator, flm_vectors(operator), record=record_property
    )

    assert not errors, "Test failed"


def b_col_maj_params():
    """Where B as stored reaches the kernel by another path than packed B: a
    resident and a streamed memtile pool, a trailing column, every tile width
    and two slabs, on each kind of mac the device has: AIE2P's bfp16 and bf16
    macs, AIE2's bf16 ones.
    """
    dev = aie_utils.get_current_device()
    if dev is None:
        return []
    cols = dev.cols
    params = [
        pytest.param(256, 512, 64 * cols, None, (NONE,), id="resident"),
        pytest.param(256, 512, 64 * cols + 64, None, (NONE,), id="trailing-col"),
        pytest.param(512, 6144, 64 * cols, None, (NONE,), id="streamed"),
        pytest.param(256, 512, 64 * cols, None, tuple(Epilogue), id="tables-linked"),
    ]
    for tile_n in sorted(set(CT_MAX_K_FOR_N) - {64}):
        params.append(
            pytest.param(256, 512, tile_n * cols, tile_n, (NONE,), id=f"tn{tile_n}")
        )
    params.append(
        pytest.param(
            16384,
            512,
            64 * cols,
            None,
            (NONE,),
            marks=pytest.mark.extensive,
            id="slabs",
        )
    )
    macs = (True, False) if dev.arch is AIEArch.AIE2p else (False,)
    return [
        pytest.param(
            *p.values,
            emulate,
            marks=p.marks,
            id=f"{p.id}-{'bfp16' if emulate else 'bf16'}",
        )
        for emulate in macs
        for p in params
    ]


@pytest.mark.parametrize("M,K,N,tile_n,epilogue_modes,emulate", b_col_maj_params())
def test_gemm_b_col_maj(
    M, K, N, tile_n, epilogue_modes, emulate, npu_runtime, record_property
):
    operator = GEMM(
        M=M,
        K=K,
        N=N,
        tile_n=tile_n,
        epilogue_modes=epilogue_modes,
        b_col_maj=True,
        emulate_bf16_mmul_with_bfp16=emulate,
    )
    errors, _, _ = check_on_device(
        operator, flm_vectors(operator), record=record_property
    )
    assert not errors, "Test failed"


def test_gemm_split_leg_bounds_runs(npu_runtime):
    """K or N = 10240 overflows the shim BD's 20-bit mega_row step, so the
    compiler cuts that leg into pieces, bounded by its queue polls and BD
    reclaim. Overrunning either hangs or corrupts silently, which only running
    can show.

    The square case splits both legs, which the real Gemma shapes never do
    (E4B's down overflows on K and its gate/up on N, never both), so it is
    the only cover for the two-sided path. Regular rather than extensive
    despite the size: ~8s against the suite's ~13s.
    """
    M, K, N = 512, 10240, 10240
    operator = GEMM(M=M, K=K, N=N)

    errors, _latency_us, _bandwidth_gbps = check_on_device(
        operator, flm_vectors(operator)
    )
    assert not errors, "Test failed"


def tile_option_params():
    """Every (tile_n, tile_ma) the design accepts on this device.

    The shape parameters above only exercise the default geometry, since
    __post_init__ resolves both tunables. These cover the tunables themselves, which
    change the blocked L1 layout, and a mismatch is silently wrong output
    rather than a build error, so each has to run on hardware. The defaults
    stay in the regular suite; the overrides are extensive, since each is its
    own kernel object and xclbin.
    """
    dev = aie_utils.get_current_device()
    if dev is None or dev.arch not in (AIEArch.AIE2, AIEArch.AIE2p):
        return []
    l1 = l1_budget(dev, tuple(Epilogue))
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


@pytest.mark.parametrize(
    "M,K,N", [(512, 1024, 1024), (512, 6144, 1024), (512, 1024, 10240)]
)
def test_sequence_programs_b_and_awaits_only_each_columns_last_c(M, K, N, npu2):
    """Device-free: B is resident (K=1024), streamed (K=6144) or behind a leg
    the compiler cuts (N=10240); in each, B has no fifo, nothing is pinned,
    the memtile locks are armed per dispatch, and one slab awaits one C per
    column.
    """
    mlir = str(build_design(GEMM(M=M, K=K, N=N)))
    assert "aie.objectfifo @B" not in mlir
    assert "bd_id" not in mlir
    assert "aiex.set_lock" in mlir
    assert mlir.count("aiex.dma_await_task") == npu2.cols


@pytest.mark.parametrize("M,K,N,tile_n,tile_ma", tile_option_params())
def test_gemm_tile_options(M, K, N, tile_n, tile_ma, npu_runtime):
    """Each accepted (tile_n, tile_ma) computes the right answer on hardware."""
    operator = GEMM(M=M, K=K, N=N, tile_n=tile_n, tile_ma=tile_ma)
    assert (operator._tuned.tile_n, operator._tuned.tile_ma) == (tile_n, tile_ma)
    errors, _latency_us, _bandwidth_gbps = check_on_device(
        operator, flm_vectors(operator, INPUT_SCALE)
    )
    assert not errors, "Test failed"


@pytest.mark.parametrize("K", [256, 768])
def test_gemm_k_tile(K, npu_runtime):
    """A k tile other than the default 512 computes the right answer.

    Gemma 4's per-layer-input projection has K = 256, which the default does
    not divide. K = 768 takes three k steps, so the accumulator carries
    across tiles of the smaller size too.
    """
    dev = aie_utils.get_current_device()
    assert dev is not None
    operator = GEMM(M=256, K=K, N=64 * dev.cols, tile_n=64, k_tile=256)
    errors, _latency_us, _bandwidth_gbps = check_on_device(
        operator, flm_vectors(operator, INPUT_SCALE)
    )
    assert not errors, "Test failed"


@pytest.mark.parametrize("M,K,N", [(256, 512, 1024), (512, 1024, 2048)])
def test_artifact_stem_differs_from_generic_gemm(M, K, N, npu_runtime):
    """``flm.GEMM`` must never share an artifact stem with ``GEMM``.

    Both classes are named ``GEMM`` and Operator.name derives the stem from
    the class name, so with the cache keyed on filename the two operators would
    silently satisfy each other's builds in one build dir.
    """
    assert GEMM(M=M, K=K, N=N).name != GenericGEMM(M=M, K=K, N=N).name


def test_one_xclbin_serves_every_shape(npu_runtime):
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
        operator = GEMM(M=M, K=K, N=N, epilogue=epilogue)
        data = flm_vectors(operator, 4.0 if epilogue == "none" else 0.5)
        mass = accumulated_mass(K, data["A"], data["B"])
        errors, _, _ = run_test(
            operator,
            {"A": data["A"].flatten(), "B": operator.pack_B(data["B"])},
            {"C": data["C"].flatten()},
            tolerance=Tolerance.relative(0.04, 0.004 * mass),
        )
        assert not errors, f"{M}x{K}x{N} {epilogue} failed"

        # A cache hit: the image run_test built and ran.
        image = OperatorImage(operator).compile().artifacts.image
        stamp = (str(image), os.path.getmtime(image))
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"{M}x{K}x{N} rebuilt the xclbin"


def test_one_xclbin_serves_every_clamp_bound(npu_runtime):
    """Different clamp bounds back to back on one loaded xclbin.

    The bounds are runtime parameters, so they must not rebuild anything.
    Separate from test_one_xclbin_serves_every_shape, which never clamps and so
    cannot catch bounds leaking back into the configuration.
    """
    M, K, N = 256, 512, 1024
    bounds = [(-2.0, 2.0), (-4.0, 4.0), (-0.5, 0.5)]
    xclbin = None
    for clamp in bounds:
        operator = GEMM(M=M, K=K, N=N, clamp=clamp)
        errors, _, _ = check_on_device(operator, flm_vectors(operator, INPUT_SCALE))
        assert not errors, f"clamp={clamp} produced wrong output"

        # A cache hit: the image run_test built and ran.
        image = OperatorImage(operator).compile().artifacts.image
        stamp = (str(image), os.path.getmtime(image))
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"clamp={clamp} rebuilt the xclbin"

    # ...and neither does dropping the clamp: the kernel always clamps, and an
    # unclamped caller neutralises it with (-inf, +inf) rather than compiling
    # a second build. config_name rather than the image, which only exists
    # once compile() has run.
    clamped = GEMM(M=M, K=K, N=N, clamp=bounds[0])
    unclamped = GEMM(M=M, K=K, N=N)
    assert unclamped.config_name == clamped.config_name
    # The bounds do reach the instruction stream, though, so they must reach
    # its stem or the build cache serves one caller's stream to another.
    assert unclamped.name != clamped.name
    assert clamped.name != GEMM(M=M, K=K, N=N, clamp=bounds[1]).name


# The shipped overlay: the binary the port was ported from, as its second
# reference. Extensive (a download) and NPU2 only.
# ##########################################################################

# Largest |d/dx| of each epilogue, used to carry the accumulator's error bound
# through to the output. sigmoid's is exactly 1/4; silu and gelu both peak at
# 1.0998 (gelu here being the x*sigmoid(1.702x) approximation the overlay
# implements, whose derivative happens to share silu's maximum), rounded up.
MAX_SLOPE = {NONE: 1.0, SIGMOID: 0.25, SILU: 1.1, GELU: 1.1}


def _shipped_marks():
    """Extensive, since constructing the operator downloads the image; and
    NPU2 with eight columns, which the binary was built for.
    """
    dev = aie_utils.get_current_device()
    unfit = dev is None or dev.arch is not AIEArch.AIE2p or dev.cols < 8
    return [
        pytest.mark.extensive,
        pytest.mark.skipif(
            unfit, reason="the shipped overlay is an 8-column NPU2 binary"
        ),
    ]


SHIPPED = _shipped_marks()

# The overlay never calls set_rounding, so it runs in the core's power-up floor
# mode and carries a ~1% truncation bias -- not a bug. See gemm/benchmark.py.
BUDGET_FLOOR = 2e-2


@pytest.mark.parametrize(
    "M,K,N,epilogue,clamp",
    [
        pytest.param(
            256, 512, 1024, NONE, None, marks=SHIPPED
        ),  # exactly one full 8-column sweep
        pytest.param(512, 1024, 2048, NONE, None, marks=SHIPPED),  # two full sweeps
        pytest.param(
            256, 512, 640, NONE, None, marks=SHIPPED
        ),  # remainder only: 5 of 8 cols
        pytest.param(
            256, 512, 1280, NONE, None, marks=SHIPPED
        ),  # full sweep + remainder: 1 of 8 cols
        pytest.param(256, 512, 1024, SILU, None, marks=SHIPPED),
        pytest.param(256, 512, 1024, GELU, None, marks=SHIPPED),
    ],
)
def test_shipped_overlay(M, K, N, epilogue, clamp, npu_runtime, record_property):
    """The shipped binary through the same operator: the second reference."""
    operator = Shipped(M=M, K=K, N=N, epilogue=epilogue, clamp=clamp)
    # B drawn row-major (K, N); the operator consumes it packed (pack_B).
    data = vectors(operator, normal=("A",), B=(K, N))

    input_buffers = {"A": data["A"].flatten(), "B": operator.pack_B(data["B"])}
    output_buffers = {"C": data["C"].flatten()}

    # The overlay's error is made in the ACCUMULATOR -- it runs in the core's
    # power-up floor rounding, worth about BUDGET_FLOOR of the accumulated mass
    # -- and the epilogue then maps that accumulator through an activation. So
    # the output bound is the accumulator bound carried through the activation,
    # |f(x+e) - f(x)| <= max|f'| * |e|, rather than a tolerance invented in the
    # output domain.
    #
    # Only the unbounded epilogues are checked this way. For sigmoid and clamp
    # no bound over this reference can be both correct and useful -- the
    # accumulator error alone exceeds their whole output range -- so they are
    # covered functionally by test_mm_prebuilt_epilogue_matches_accumulator.
    mass = accumulated_mass(K, data["A"], data["B"])
    abs_tol = MAX_SLOPE[epilogue] * BUDGET_FLOOR * mass
    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        tolerance=Tolerance.relative(0.04, abs_tol),
        record=record_property,
    )
    assert not errors, "Test failed"


@pytest.mark.parametrize(
    "epilogue,clamp",
    [
        pytest.param(SIGMOID, None, marks=SHIPPED),
        pytest.param(NONE, (-2.0, 2.0), marks=SHIPPED),
        pytest.param(SILU, None, marks=SHIPPED),
        pytest.param(GELU, None, marks=SHIPPED),
    ],
)
def test_shipped_epilogue_matches_accumulator(epilogue, clamp, npu_runtime):
    """The epilogue is the right function of the accumulator the device produced.

    Checking a bounded epilogue against the idealized CPU reference cannot work.
    The overlay accumulates in the core's power-up floor rounding, worth ~2% of
    the accumulated mass, which here is ~65 -- larger than sigmoid's entire (0,1)
    range and than this clamp's (-2, 2). Any bound wide enough to admit that
    accumulator error also admits an all-zero result, and any bound tight enough
    to reject all-zeros also rejects correct hardware. That is why the earlier
    flat tolerance failed on working arithmetic.

    So compare the epilogue against the device's OWN accumulator instead: run
    the same inputs with no epilogue, apply the activation and clamp to that on
    the host, and require the epilogue build to agree. The accumulator error is
    then common to both sides and cancels, leaving only the epilogue under test.
    An all-zero result still fails, because the reference side is not zero.
    """
    M, K, N = 256, 512, 1024
    # A small input scale keeps the accumulator in the range where these curves
    # are actually curved; at the default scale the product lands around +-900,
    # where gelu and silu are indistinguishable from the identity.
    probe = Shipped(M=M, K=K, N=N)
    data = vectors(probe, normal=("A",), scale=0.5, B=(K, N))
    A, B = data["A"], data["B"]

    def run(epi, clm):
        op = Shipped(M=M, K=K, N=N, epilogue=epi, clamp=clm)
        tensor = aie_utils.DEFAULT_TENSOR_CLASS
        out = tensor((M, N), dtype=np.dtype("bfloat16"))
        OperatorImage(op)(tensor(A.flatten()), tensor(op.pack_B(B)), out)
        return out.numpy().reshape(M, N).astype(np.float32)

    acc = run(NONE, None)
    got = run(epilogue, clamp)
    expected = Epilogue(epilogue).apply(acc, clamp)

    # Both sides see the same accumulator, so what is left is the epilogue.
    # Two terms, and they are different in kind.
    #
    # The bf16 term is per element rather than one global number: the
    # accumulator read back is bf16, good to ~2^-8 RELATIVELY, and clamp is only
    # sensitive near its boundary, so a tolerance taken from the accumulator's
    # largest magnitude would be wider there than the clamp range itself -- i.e.
    # vacuous.
    #
    # The activation term covers what bf16 rounding does NOT explain. Checked by
    # bounding the true accumulator to its bf16 rounding interval and evaluating
    # the epilogue across it: clamp lands inside for all 262144 elements, but
    # sigmoid, silu and gelu land outside for about half, by up to 0.018. That
    # residual is the overlay's own activation approximation -- a LUT or native
    # instruction, not exact math -- which no exact-sigmoid reference can
    # reproduce. 0.05 is ~3x the measured worst case and still ~20x below
    # where the bound would go vacuous; the assertion at the end pins that down.
    approx = 0.0 if epilogue is NONE else 0.05
    tol = MAX_SLOPE[epilogue] * np.abs(acc) * 2.0**-8 + 2.0**-8 + approx
    err = np.abs(got - expected)
    over = err > tol
    assert not over.any(), (
        f"{epilogue} clamp={clamp}: {int(over.sum())} of {over.size} elements "
        f"differ from epilogue(device accumulator) by more than the bf16 bound; "
        f"worst {float((err - tol).max()):.4f} over"
    )
    # The bound must not be wide enough to admit a dead device.
    assert (
        np.abs(expected) > tol
    ).any(), f"{epilogue}: tolerance is vacuous -- an all-zero result would pass"


@pytest.mark.parametrize(
    "M,K,N",
    [
        pytest.param(256, 512, 1024, marks=SHIPPED),  # tile_n 128
        pytest.param(512, 1536, 6144, marks=SHIPPED),  # Gemma 4 E2B gate_proj
        pytest.param(512, 1536, 256, marks=SHIPPED),  # Gemma 4 E2B per-layer gate
    ],
)
def test_gemm_gelu_bf16_steps_matches_overlay(M, K, N, npu_runtime):
    """``gelu=bf16_steps`` with ``rounding=floor`` matches the shipped overlay's
    gelu bit for bit, on identical inputs.
    """
    probe = Shipped(M=M, K=K, N=N)
    data = vectors(probe, normal=("A",), scale=ACTIVATION_INPUT_SCALE, B=(K, N))
    A, B = data["A"], data["B"]

    def run(op):
        tensor = aie_utils.DEFAULT_TENSOR_CLASS
        out = tensor((M, N), dtype=np.dtype("bfloat16"))
        OperatorImage(op)(tensor(A.flatten()), tensor(op.pack_B(B)), out)
        return out.numpy().reshape(M, N).copy()

    shipped = run(Shipped(M=M, K=K, N=N, epilogue=GELU))
    ported = run(
        GEMM(M=M, K=K, N=N, epilogue=GELU, rounding=FLOOR, gelu=Gelu.BF16_STEPS)
    )
    # The accumulator reaches about -15 at this scale. gelu's minimum is
    # about -0.17, so a lower minimum means the activation did not run.
    assert float(shipped.astype(np.float32).min()) > -0.5, "the overlay applied no gelu"
    same = int((shipped.view(np.int16) == ported.view(np.int16)).sum())
    assert same == M * N, f"{M * N - same} of {M * N} elements differ"
