# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import os

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.dialects._aie_enum_gen import AIEArch
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Precision
from iron.common.testing import run_test, vectors
from iron.operators.flm.gemm.design import (
    M_TILE,
    TILE_NS,
    Epilogue,
    Gelu,
    R,
    Rounding,
    k_slices,
)
from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.tests.support.shipped import Shipped
from iron.tests.support.tools import DEVICES

# Unpacked so the parameter tables below stay column-aligned.
NONE, GELU, SILU, SIGMOID = Epilogue
CONV_EVEN, FLOOR = Rounding

# Activation tests run at a smaller scale so the result lands where the curve
# is not flat. The golden product grows like sqrt(K)*scale**2,
# so at the default 4.0 a K=512 product sits around +-200, where gelu and silu
# are indistinguishable from the identity.
INPUT_SCALE = 4.0
ACTIVATION_INPUT_SCALE = 0.5


def get_params(device: str):
    """``test_gemm``'s shapes on ``device``, run only there.

    Declared for its model in ``DEVICES``, so collecting opens no device.
    """
    dev = DEVICES[device]()

    # One full sweep is N_TILE * COLS wide, so both it and the N values that
    # leave a trailing partial column-block differ per device. The trailing
    # case is the interesting one: some columns compute the block while the
    # rest only drain the A broadcast, and real o/down projections always land
    # there. At K = 512 tile_n defaults to 128, halving at K >= 1024.
    # fmt: off
    if dev.arch is AIEArch.AIE2p:
        #      M,    K,     N, epilogue, rounding
        regular_params = [
            (  256,  512,  1024, NONE,     CONV_EVEN),  # smallest full sweep
            (  256,  512,  1536, NONE,     CONV_EVEN),  # remainder: 4 of 8 cols
            (  256,  512,   128, NONE,     CONV_EVEN),  # remainder only: 1 col
            # Qwen3.5's gate projection: tile_n 16, at a scale no other case
            # or tile_option_params reaches.
            ( 2048, 1024,    16, NONE,     CONV_EVEN),
            (  256,  512,  1024, SILU,     CONV_EVEN),
            (  256,  512,  1024, GELU,     CONV_EVEN),
            # floor reproduces the shipped FastFlowLM overlay's rounding mode
            # (bit for bit on NPU2; NPU1 sums the K reduction in a different
            # order). It is much less accurate, so it gets its own bound below.
            (  256,  512,  1024, NONE,     FLOOR),
        ]
        extensive_params = [
            (  256,  512,  1024, SIGMOID,  CONV_EVEN),
            # K or N = 10240 at M > 256 overflows the shim BD's 20-bit
            # mega_row iteration step, so the compiler cuts that leg into
            # pieces, bounded by its queue polls and BD reclaim. These are the
            # real E4B FFN projections, and M=2048 doubles the pieces.
            ( 1024, 10240,  2560, NONE,     CONV_EVEN),  # E4B down
            ( 1024,  2560, 10240, NONE,     CONV_EVEN),  # E4B gateup
            ( 2048,  2560, 10240, NONE,     CONV_EVEN),  # E4B gateup, 2x
            # 64 row-block units, past the 63 a lock can count, so B is armed
            # twice: two slabs, each resident.
            (16384,  512,  1024, NONE,     CONV_EVEN),
        ]
    else:  # npu1: _default_tile_n always returns 64 here, so with 4 columns
        # every sweep is N_TILE*COLS = 256 wide, not the 128*4=512 an
        # NPU2-shaped sweep would give.
        #      M,    K,     N, epilogue, rounding
        regular_params = [
            (  256,  512,   256, NONE,     CONV_EVEN),  # smallest full sweep
            (  256,  512,   128, NONE,     CONV_EVEN),  # remainder: 2 of 4 cols
            (  256,  512,    64, NONE,     CONV_EVEN),  # remainder only: 1 col
            (  256,  512,   320, NONE,     CONV_EVEN),  # full sweep + 1 col
            (  256,  512,   512, SILU,     CONV_EVEN),
            (  256,  512,   512, GELU,     CONV_EVEN),
            (  256,  512,   512, NONE,     FLOOR),
        ]
        extensive_params = [
            ( 2048, 2048,  1024, NONE,     CONV_EVEN),  # bench-tracked below
            ( 1024, 2560,  2560, NONE,     CONV_EVEN),  # E4B o-proj, bench-tracked
            (  256,  512,   512, SIGMOID,  CONV_EVEN),
            # Two slabs, as on NPU2.
            (16384,  512,   256, NONE,     CONV_EVEN),
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
        marks = [pytest.mark.supported_devices(device)]
        marks += [pytest.mark.extensive] if extensive else []
        M, K, N, epilogue, rounding = p
        if (M, K, N) in bench_shapes and epilogue is NONE:
            marks.append(pytest.mark.bench)
        return marks

    params = []
    for p in regular_params:
        params.append(pytest.param(*p, marks=marks_for(p, extensive=False)))
    for p in extensive_params:
        params.append(pytest.param(*p, marks=marks_for(p, extensive=True)))
    names = ("M", "K", "N", "epilogue", "rounding")
    return [
        pytest.param(
            *q.values,
            marks=q.marks,
            id="-".join([device, *(f"{n}_{v}" for n, v in zip(names, q.values))]),
        )
        for q in params
    ]


def flm_vectors(operator, scale=4.0):
    """Random A (signed) and B (non-negative) at ``scale``, and epilogue(A @ B).

    A small ``scale`` keeps K=512 products away from +-200, where gelu/silu
    are indistinguishable from the identity; B is row-major ``(K, N)``,
    packed by ``ProjectionGEMM.pack_b``, or ``(N, K)`` as stored under
    ``b_col_maj``.
    """
    K, N = operator.K, operator.N
    B = (N, K) if operator.b_col_maj else (K, N)
    return vectors(operator, normal=(operator.A,), scale=scale, given={operator.B: B})


def accumulated_mass(K, A, B):
    """K * mean|a| * mean|b|: the magnitude the accumulator's error tracks."""
    return float(
        K * np.abs(A.astype(np.float32)).mean() * np.abs(B.astype(np.float32)).mean()
    )


def check_on_device(operator, data, rounding=CONV_EVEN, record=None):
    """Run ``operator`` against its drawn vectors and return run_test's result.

    Bounds error absolutely as a fraction of the accumulated mass
    K * mean|a| * mean|b|: a relative tolerance can't work, since signed A's
    K-sum cancels by ~sqrt(K), leaving near-zero outputs uncheckable. The
    fraction is per-architecture and loosens under ``floor``'s truncation bias.
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
            "B": B.flatten() if operator.b_col_maj else operator.pack_b(B),
        },
        {"C": data["C"].flatten()},
        tolerance=Tolerance.relative(0.04, budget * mass),
        record=record,
    )


@pytest.mark.parametrize(
    "M,K,N,epilogue,rounding", [*get_params("npu1"), *get_params("npu2")]
)
def test_gemm(M, K, N, epilogue, rounding, record_property):
    scale = INPUT_SCALE if epilogue is NONE else ACTIVATION_INPUT_SCALE
    operator = ProjectionGEMM(
        M=M,
        K=K,
        N=N,
        rounding=rounding,
        epilogue=epilogue,
        precision=Precision.MEDIUM,
    )

    errors = check_on_device(
        operator, flm_vectors(operator, scale), rounding, record=record_property
    )

    assert not errors, "Test failed"


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("M,K,N", [(256, 512, 256), (512, 1024, 512)])
def test_gemm_without_activations(M, K, N, record_property):
    """Compiling no activation links no LUT tables.

    So on AIE2 the bytes they held go to B and the tiles differ from every
    case above.
    """
    operator = ProjectionGEMM(
        M=M, K=K, N=N, epilogue_modes=(NONE,), precision=Precision.MEDIUM
    )

    errors = check_on_device(operator, flm_vectors(operator), record=record_property)

    assert not errors, "Test failed"


def b_col_maj_params(device: str):
    """Where B as stored reaches the kernel by another path than packed B.

    A resident and streamed memtile pool, a trailing column, every tile
    width and two slabs, on each mac kind ``device`` has (AIE2P's
    bfp16/bf16, AIE2's bf16).
    """
    dev = DEVICES[device]()
    cols = dev.cols
    params = [
        pytest.param(256, 512, 64 * cols, None, (NONE,), id="resident"),
        pytest.param(256, 512, 64 * cols + 64, None, (NONE,), id="trailing-col"),
        pytest.param(512, 6144, 64 * cols, None, (NONE,), id="streamed"),
        pytest.param(256, 512, 64 * cols, None, tuple(Epilogue), id="tables-linked"),
    ]
    for tile_n in sorted(set(TILE_NS) - {64}):
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
    levels = (
        (Precision.MEDIUM, Precision.HIGH)
        if dev.arch is AIEArch.AIE2p
        else (Precision.HIGH,)
    )
    return [
        pytest.param(
            *p.values,
            precision,
            marks=[*p.marks, pytest.mark.supported_devices(device)],
            id=f"{device}-{p.id}-{precision}",
        )
        for precision in levels
        for p in params
    ]


@pytest.mark.parametrize(
    "M,K,N,tile_n,epilogue_modes,precision",
    [*b_col_maj_params("npu1"), *b_col_maj_params("npu2")],
)
def test_gemm_b_col_maj(M, K, N, tile_n, epilogue_modes, precision, record_property):
    operator = ProjectionGEMM(
        M=M,
        K=K,
        N=N,
        tile_n=tile_n,
        epilogue_modes=epilogue_modes,
        b_col_maj=True,
        precision=precision,
    )
    errors = check_on_device(operator, flm_vectors(operator), record=record_property)
    assert not errors, "Test failed"


@pytest.mark.supported_devices("npu1", "npu2")
def test_gemm_split_leg_bounds_runs():
    """Check that cutting both legs into pieces does not hang or corrupt silently.

    N = 20480 overflows the shim BD's 20-bit step from one row-block to the
    next, and m_chunk = 2 gives A's leg a fifth dimension, so the compiler
    cuts both legs into pieces; overrunning either hangs or corrupts
    silently, and no model shape cuts a leg at m_chunk = 1, so this is
    their only cover.
    """
    M, K, N = 512, 512, 20480
    operator = ProjectionGEMM(M=M, K=K, N=N, m_chunk=2, precision=Precision.MEDIUM)

    errors = check_on_device(operator, flm_vectors(operator))
    assert not errors, "Test failed"


def tile_option_params(device: str):
    """Every (tile_n, tile_ma) to try on ``device``.

    The shapes above only exercise the default geometry, and a mismatched
    override is silently wrong output rather than a build error, so it
    must run on hardware. The default stays in the regular suite;
    overrides are extensive.
    """
    dev = DEVICES[device]()
    params = []
    for tile_n in sorted(TILE_NS):
        # One full sweep of the grid at this tile_n, so every column has work.
        N = tile_n * dev.cols
        for tile_ma in (None, 16, 32, 64):
            if tile_ma is not None and (M_TILE % tile_ma or tile_ma % (2 * R)):
                continue
            params.append(
                pytest.param(
                    256,
                    512,
                    N,
                    tile_n,
                    tile_ma,
                    marks=[
                        pytest.mark.supported_devices(device),
                        *([] if tile_ma is None else [pytest.mark.extensive]),
                    ],
                    id=f"{device}-tn{tile_n}-"
                    + ("default" if tile_ma is None else f"ma{tile_ma}"),
                )
            )
    return params


@pytest.mark.parametrize(
    "M,K,N,tile_n,tile_ma",
    [*tile_option_params("npu1"), *tile_option_params("npu2")],
)
def test_gemm_tile_options(M, K, N, tile_n, tile_ma):
    """Check that each (tile_n, tile_ma) the design accepts computes the right answer.

    The default, and each other A height the design accepts, on hardware.
    """
    shape = dict(M=M, K=K, N=N, tile_n=tile_n, precision=Precision.MEDIUM)
    default = ProjectionGEMM(**shape).resolved().tile_ma
    if tile_ma == default:
        pytest.skip(f"tile_ma {default} is the default, run as -default")
    try:
        operator = ProjectionGEMM(**shape, tile_ma=tile_ma or default)
        resolved = operator.resolved()
    except ValueError as e:
        pytest.skip(f"this A height leaves no room for B at this width: {e}")
    assert (resolved.tile_n, resolved.tile_ma) == (tile_n, tile_ma or default)
    errors = check_on_device(operator, flm_vectors(operator, INPUT_SCALE))
    assert not errors, "Test failed"


def k_slice_params(device: str):
    """Every k slice to try at the default tile_n on ``device``.

    Like the tiles above, a mismatch is silently wrong rather than a build
    error; the default stays in the regular suite, the others are extensive.
    """
    return [
        pytest.param(
            ct_k,
            marks=[
                pytest.mark.supported_devices(device),
                *([] if ct_k is None else [pytest.mark.extensive]),
            ],
            id=f"{device}-" + ("default" if ct_k is None else f"ck{ct_k}"),
        )
        for ct_k in (None, *k_slices(512))
    ]


@pytest.mark.parametrize("ct_k", [*k_slice_params("npu1"), *k_slice_params("npu2")])
def test_gemm_k_slices(ct_k):
    """Check that each k slice the design accepts computes the right answer.

    The default, and each other, on hardware.
    """
    dev = aie_utils.get_current_device()
    assert dev is not None
    shape = dict(M=256, K=512, N=64 * dev.cols, precision=Precision.MEDIUM)
    default = ProjectionGEMM(**shape).resolved().ct_k
    if ct_k == default:
        pytest.skip(f"ct_k {default} is the default, run as -default")
    try:
        operator = ProjectionGEMM(**shape, ct_k=ct_k or default)
        resolved = operator.resolved()
    except ValueError as e:
        pytest.skip(f"this slice leaves no room for the tiles in L1: {e}")
    assert resolved.ct_k == (ct_k or default)
    errors = check_on_device(operator, flm_vectors(operator, INPUT_SCALE))
    assert not errors, "Test failed"


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("K", [256, 768])
def test_gemm_k_tile(K):
    """Check that a k tile other than the default 512 computes the right answer.

    Gemma 4's per-layer-input projection has K=256 (512 doesn't divide
    it); K=768 takes three k steps, carrying the accumulator across
    smaller tiles too.
    """
    dev = aie_utils.get_current_device()
    assert dev is not None
    operator = ProjectionGEMM(
        M=256, K=K, N=64 * dev.cols, tile_n=64, k_tile=256, precision=Precision.MEDIUM
    )
    errors = check_on_device(operator, flm_vectors(operator, INPUT_SCALE))
    assert not errors, "Test failed"


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "precision", [Precision.MEDIUM, Precision.HIGH], ids=["medium", "high"]
)
@pytest.mark.parametrize(
    "K,tile_n,k_tile,ct_k",
    [(512, 64, 128, 128), (16, 16, 16, 16), (64, 32, 64, 32), (96, 32, 96, 32)],
)
def test_gemm_k_tile_of_few_chunks(K, tile_n, k_tile, ct_k, precision):
    """Check that a k step of one or an odd count of B chunks walks every chunk.

    ``k_tile`` is the compute tile's k slice. Small integers are exact in
    bfp16 and bf16, since check_on_device's bound is only fitted at K >=
    256. Covers both MEDIUM's bfp16 macs and HIGH's bf16 macs.
    """
    dev = aie_utils.get_current_device()
    assert dev is not None
    N = tile_n * dev.cols
    operator = ProjectionGEMM(
        M=256,
        K=K,
        N=N,
        tile_n=tile_n,
        k_tile=k_tile,
        ct_k=ct_k,
        precision=precision,
    )
    rng = np.random.default_rng(0)
    A = rng.integers(-3, 4, (256, K)).astype(bfloat16)
    B = rng.integers(0, 4, (K, N)).astype(bfloat16)
    C = (A.astype(np.float32) @ B.astype(np.float32)).astype(bfloat16)
    errors = run_test(
        operator,
        {"A": A.flatten(), "B": operator.pack_b(B)},
        {"C": C.flatten()},
        tolerance=Tolerance.exact(note="integers, exact in every sum"),
    )
    assert not errors, errors


@pytest.mark.supported_devices("npu1", "npu2")
def test_one_xclbin_serves_every_shape():
    """Run several shapes back to back on one loaded xclbin.

    The parametrised tests can't cover this, since each gets a fresh
    context. Here the shapes share one, disagree on every parameter, and
    none may rebuild the xclbin.
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
        operator = ProjectionGEMM(
            M=M, K=K, N=N, epilogue=epilogue, precision=Precision.MEDIUM
        )
        data = flm_vectors(operator, 4.0 if epilogue == "none" else 0.5)
        mass = accumulated_mass(K, data["A"], data["B"])
        errors = run_test(
            operator,
            {"A": data["A"].flatten(), "B": operator.pack_b(data["B"])},
            {"C": data["C"].flatten()},
            tolerance=Tolerance.relative(0.04, 0.004 * mass),
        )
        assert not errors, f"{M}x{K}x{N} {epilogue} failed"

        # A cache hit: the image run_test built and ran.
        image = operator.compile().image
        stamp = (str(image), os.path.getmtime(image))
        if xclbin is None:
            xclbin = stamp
        assert stamp == xclbin, f"{M}x{K}x{N} rebuilt the xclbin"


# The shipped overlay, the port's second reference: extensive (a download)
# and NPU2 only.

# Largest |d/dx| of each epilogue, used to carry the accumulator's error bound
# through to the output. sigmoid's is exactly 1/4; silu and gelu both peak at
# 1.0998 (gelu here being the x*sigmoid(1.702x) approximation the overlay
# implements, whose derivative happens to share silu's maximum), rounded up.
MAX_SLOPE = {NONE: 1.0, SIGMOID: 0.25, SILU: 1.1, GELU: 1.1}


# Extensive, since constructing the operator downloads the image.
SHIPPED = pytest.mark.extensive


@pytest.fixture
def eight_column_npu2():
    """Skip unless the attached NPU is the eight-column NPU2.

    The shipped binary was built for it.
    """
    dev = aie_utils.get_current_device()
    if dev.arch is not AIEArch.AIE2p or dev.cols < 8:
        pytest.skip("the shipped overlay is an 8-column NPU2 binary")


# The overlay never calls set_rounding, so it runs in the core's power-up floor
# mode and carries a ~1% truncation bias -- not a bug. See README.md.
BUDGET_FLOOR = 2e-2


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "M,K,N,epilogue",
    [
        pytest.param(
            256, 512, 1024, NONE, marks=SHIPPED
        ),  # exactly one full 8-column sweep
        pytest.param(512, 1024, 2048, NONE, marks=SHIPPED),  # two full sweeps
        pytest.param(256, 512, 640, NONE, marks=SHIPPED),  # remainder only: 5 of 8 cols
        pytest.param(
            256, 512, 1280, NONE, marks=SHIPPED
        ),  # full sweep + remainder: 1 of 8 cols
        pytest.param(256, 512, 1024, SILU, marks=SHIPPED),
        pytest.param(256, 512, 1024, GELU, marks=SHIPPED),
    ],
)
def test_shipped_overlay(M, K, N, epilogue, record_property, eight_column_npu2):
    """The shipped binary through the same operator: the second reference."""
    operator = Shipped(M=M, K=K, N=N, epilogue=epilogue)
    # B drawn row-major (K, N); the operator consumes it packed (pack_b).
    data = vectors(operator, normal=(operator.A,), given={operator.B: (K, N)})

    input_buffers = {"A": data["A"].flatten(), "B": operator.pack_b(data["B"])}
    output_buffers = {"C": data["C"].flatten()}

    # The overlay's error is made in the ACCUMULATOR -- it runs in the core's
    # power-up floor rounding, worth about BUDGET_FLOOR of the accumulated mass
    # -- and the epilogue then maps that accumulator through an activation. So
    # the output bound is the accumulator bound carried through the activation,
    # |f(x+e) - f(x)| <= max|f'| * |e|, rather than a tolerance invented in the
    # output domain.
    #
    # Only the unbounded epilogues are checked this way. For sigmoid no bound over this reference can be both correct and useful -- the
    # accumulator error alone exceeds their whole output range -- so they are
    # covered functionally by test_shipped_epilogue_matches_accumulator.
    mass = accumulated_mass(K, data["A"], data["B"])
    abs_tol = MAX_SLOPE[epilogue] * BUDGET_FLOOR * mass
    errors = run_test(
        operator,
        input_buffers,
        output_buffers,
        tolerance=Tolerance.relative(0.04, abs_tol),
        record=record_property,
    )
    assert not errors, "Test failed"


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "epilogue",
    [
        pytest.param(SIGMOID, marks=SHIPPED),
        pytest.param(SILU, marks=SHIPPED),
    ],
)
def test_shipped_epilogue_matches_accumulator(epilogue, eight_column_npu2):
    """Check that the epilogue is the right function of the device's accumulator.

    A bounded check against the idealized CPU reference can't work: the
    overlay's floor-rounded accumulator error (~2% of the accumulated
    mass) dwarfs sigmoid's (0,1) range, so a bound wide enough to admit it
    also admits an all-zero result. Instead this compares against the
    device's own no-epilogue accumulator, run through the same activation
    on the host, so the accumulator error cancels and an all-zero result
    still fails. gelu doesn't need this: its wider output range lets
    test_shipped_overlay check it directly against the accumulator-mass
    bound, and test_gemm_gelu_bf16_steps_matches_overlay checks it bit for
    bit.
    """
    M, K, N = 256, 512, 1024
    # A small input scale keeps the accumulator in the range where these curves
    # are actually curved; at the default scale the product lands around +-900,
    # where gelu and silu are indistinguishable from the identity.
    probe = Shipped(M=M, K=K, N=N)
    data = vectors(probe, normal=(probe.A,), scale=0.5, given={probe.B: (K, N)})
    A, B = data["A"], data["B"]

    def run(epi):
        op = Shipped(M=M, K=K, N=N, epilogue=epi)
        tensor = aie_utils.DEFAULT_TENSOR_CLASS
        out = tensor((M, N), dtype=np.dtype("bfloat16"))
        op(tensor(A.flatten()), tensor(op.pack_b(B)), out)
        return out.numpy().reshape(M, N).astype(np.float32)

    acc = run(NONE)
    got = run(epilogue)
    expected = Epilogue(epilogue).apply(acc)

    # Both sides see the same accumulator, so what is left is the epilogue.
    # The bf16 term is per element (the read-back accumulator is good to 2^-8
    # relatively; one global bound would be wider than sigmoid's range). The
    # activation term is the overlay's own approximation, a LUT or native
    # instruction: up to 0.018 past the bf16 interval, so 0.05, ~20x below
    # where the bound would go vacuous (the last assertion).
    approx = 0.0 if epilogue is NONE else 0.05
    tol = MAX_SLOPE[epilogue] * np.abs(acc) * 2.0**-8 + 2.0**-8 + approx
    err = np.abs(got - expected)
    over = err > tol
    assert not over.any(), (
        f"{epilogue}: {int(over.sum())} of {over.size} elements "
        f"differ from epilogue(device accumulator) by more than the bf16 bound; "
        f"worst {float((err - tol).max()):.4f} over"
    )
    # The bound must not be wide enough to admit a dead device.
    assert (
        np.abs(expected) > tol
    ).any(), f"{epilogue}: tolerance is vacuous -- an all-zero result would pass"


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize(
    "M,K,N",
    [
        pytest.param(256, 512, 1024, marks=SHIPPED),  # tile_n 128
        pytest.param(512, 1536, 6144, marks=SHIPPED),  # Gemma 4 E2B gate_proj
        pytest.param(512, 1536, 256, marks=SHIPPED),  # Gemma 4 E2B per-layer gate
    ],
)
def test_gemm_gelu_bf16_steps_matches_overlay(M, K, N, eight_column_npu2):
    """Check that ``gelu=bf16_steps``/``rounding=floor`` matches the overlay's gelu.

    Bit for bit, on identical inputs.
    """
    probe = Shipped(M=M, K=K, N=N)
    data = vectors(
        probe, normal=(probe.A,), scale=ACTIVATION_INPUT_SCALE, given={probe.B: (K, N)}
    )
    A, B = data["A"], data["B"]

    def run(op):
        tensor = aie_utils.DEFAULT_TENSOR_CLASS
        out = tensor((M, N), dtype=np.dtype("bfloat16"))
        op(tensor(A.flatten()), tensor(op.pack_b(B)), out)
        return out.numpy().reshape(M, N).copy()

    shipped = run(Shipped(M=M, K=K, N=N, epilogue=GELU))
    ported = run(
        ProjectionGEMM(
            M=M,
            K=K,
            N=N,
            epilogue=GELU,
            rounding=FLOOR,
            gelu=Gelu.BF16_STEPS,
            precision=Precision.MEDIUM,
        )
    )
    # The accumulator reaches about -15 at this scale. gelu's minimum is
    # about -0.17, so a lower minimum means the activation did not run.
    assert float(shipped.astype(np.float32).min()) > -0.5, "the overlay applied no gelu"
    same = int((shipped.view(np.int16) == ported.view(np.int16)).sum())
    assert same == M * N, f"{M * N - same} of {M * N} elements differ"
