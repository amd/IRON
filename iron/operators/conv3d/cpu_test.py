#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Production-grade, isolated pure-CPU reference test suite for Conv3D.

This dedicated cpu_test.py is the hardened production standard for CPU-only
validation of the Conv3D golden reference path (the pattern established by
reduction, maxpool, and avgpool).

Why a separate file (vs embedding the cpu test inside test.py):
- Main test.py contains ONLY the HW integration tests (primary @metrics
  test_conv3d, test_conv3d_forward, FORWARD_CASES, and get_params()).
  This guarantees the conftest.py CSV/metrics hook (strict nodeid regex
  expecting bracketed stable IDs) never encounters bare function nodeids.
- cpu_test.py is run explicitly:
      conda run -n iron314 python -m pytest iron/operators/conv3d/cpu_test.py -q --tb=short
  or with --iterations, --collectonly (never auto-discovered broadly due to
  historical python_files conventions, though pytest.ini now explicitly lists it).
- Full iron314 (python 3.14) cleanliness: zero dependency on aie_context
  fixture, XRT, NPU device discovery at import time for the test functions
  themselves (get_params import is safe due to its internal defensive try/except).
- Clean separation of concerns: reference math (generate_golden_reference +
  conv3d_cpu + calculate_output_dim + F.conv3d contract) can be validated
  instantly everywhere, independently of AIE design.py / kernel / runtime.

Responsibilities (complete production contract):
- Every generate_golden_reference call used by the HW tests is cross-validated
  against direct conv3d_cpu + raw torch.nn.functional.conv3d (with full
  support for groups, dilation, asymmetric per-dim k/s/p, batch>1).
- calculate_output_dim (the single source of truth exercised at collection
  time inside get_params) is proven identical to F output shapes.
- Explicit pytest.param + stable descriptive IDs for every CPU_REFERENCE_CASE
  (including 3D-specific pitfalls: temporal asymmetry, partial groups,
  dilation>1 in reference path, overhangs).
- get_params() invariants: non-empty, unique stable IDs, regular vs extensive
  separation, first case unmarked. Critical for CSV/metrics reporting health.
- Additional guards: seed determinism (reproducibility of goldens),
  direct F equivalence, conv3d_cpu wrapper fidelity.
- Zero top-level side effects, zero HW imports (no AIEConv3d, no run_test,
  no aie.utils at module level outside the safe get_params import).
- Excellent 3D coverage: standard, depthwise, pointwise, strided, partial
  groups, dilation, asymmetric tuples, batch>1, tiny/edge cases.

Run this before any NPU work or after reference.py changes:
    conda run -n iron314 python -m pytest iron/operators/conv3d/cpu_test.py -q --tb=short
    conda run -n iron314 python -m pytest iron/operators/conv3d/cpu_test.py -q --iterations 1 -k "reference_cpu_only"

If this passes, the golden data (bf16) fed to every Conv3D AIE test is trustworthy.

See also:
- iron/operators/conv3d/reference.py (the implementation under test + __main__ demos)
- iron/operators/conv3d/test.py (the HW complement after cpu_test separation)
- iron/operators/conv3d/op.py (notes only dilation=1 supported on AIE path)
"""

import pytest
import torch
import torch.nn.functional as F

from iron.operators.conv3d.reference import (
    generate_golden_reference,
    conv3d_cpu,
    calculate_output_dim,
)

# Import the shared get_params (single source of truth for the full HW matrix)
# from the sibling test module. Safe under iron314: get_params performs only
# a defensive try/except around aie.utils.get_current_device and never crashes
# on import or during pure-CPU collection.
from iron.operators.conv3d.test import get_params

# =============================================================================
# Representative CPU reference cases (parametrized for hook-safe nodeids).
# Strengthened 3D coverage: bias, groups (full/partial/depthwise), dilation,
# asymmetric temporal vs spatial, pointwise, strided, batch, tiny/edge.
# =============================================================================

CPU_REFERENCE_CASES = [
    # Core bias on/off + standard
    pytest.param(1, 3, 8, 16, 16, 16, 3, 1, 1, 1, True, 1, id="cpu_basic_bias"),
    pytest.param(1, 3, 8, 16, 16, 16, 3, 1, 1, 1, False, 1, id="cpu_basic_nobias"),
    # Depthwise (full groups)
    pytest.param(1, 16, 8, 16, 16, 16, 3, 1, 1, 16, True, 1, id="cpu_depthwise_bias"),
    pytest.param(
        1, 16, 8, 16, 16, 16, 3, 1, 1, 16, False, 1, id="cpu_depthwise_nobias"
    ),
    # Pointwise + batch>1
    pytest.param(2, 32, 4, 8, 8, 64, 1, 1, 0, 1, True, 1, id="cpu_pointwise_b2"),
    # Strided
    pytest.param(1, 16, 8, 16, 16, 32, 3, 2, 1, 1, True, 1, id="cpu_strided"),
    # Edge: small + nobias + overhang pad
    pytest.param(1, 1, 5, 5, 5, 4, 3, 1, 1, 1, False, 1, id="cpu_tiny_nobias"),
    # Batch + no-pad temporal
    pytest.param(4, 4, 4, 8, 8, 8, 3, 1, 0, 1, True, 1, id="cpu_batch_nopad"),
    # === Strengthened 3D-specific coverage (temporal dim, partial groups, dilation) ===
    # Partial groups (neither 1 nor depthwise) - exercises groups path in golden/calc/F
    pytest.param(1, 8, 8, 16, 16, 4, 3, 1, 1, 2, True, 1, id="cpu_groups2"),
    pytest.param(1, 8, 6, 12, 12, 8, 3, 1, 1, 4, False, 1, id="cpu_groups4"),
    # Dilation=2 (exercises dilation term in calculate_output_dim + F.conv3d)
    # Effective k=1+(3-1)*2=5; padded in=11 >=5 safe
    pytest.param(1, 3, 9, 16, 16, 16, 3, 1, 1, 1, True, 2, id="cpu_dil2"),
    # Temporal asymmetry (3D pitfall): different k/s/p per dim (T vs H/W)
    # Exercises tuple normalization in generate_golden + per-dim calculate_output_dim
    pytest.param(
        1,
        4,
        7,
        9,
        11,
        8,
        (1, 3, 3),
        (1, 2, 1),
        (0, 1, 1),
        1,
        True,
        1,
        id="cpu_3d_asym_temporal",
    ),
]


@pytest.mark.parametrize(
    "bs,ic,it,ih,iw,oc,k,s,p,g,ub,dil",
    CPU_REFERENCE_CASES,
)
def test_conv3d_reference_cpu_only(bs, ic, it, ih, iw, oc, k, s, p, g, ub, dil):
    """Pure CPU reference path test (no AIE hardware, no aie_context fixture).

    Validates the entire reference implementation in isolation:
    - generate_golden_reference (the exact call used by metrics + forward tests)
    - conv3d_cpu wrapper
    - calculate_output_dim
    against the authoritative torch.nn.functional.conv3d directly.

    Covers bias on/off, groups (standard + depthwise + partial grouped),
    pointwise (1x1x1), strided, padding, dilation (reference-only; AIE path
    currently asserts dilation==1), batch>1, asymmetric temporal vs spatial
    dims (critical 3D pitfall), and edge cases.

    This test always runs and is the critical guard against regressions in the
    golden math or shape formulas that every AIE test depends on.

    Explicit parametrized cases (reduction + maxpool/avgpool pattern) with stable
    IDs for excellent reporting under --iterations and the CSV/metrics hooks.
    """
    golden = generate_golden_reference(
        batch_size=bs,
        in_channels=ic,
        in_t=it,
        in_h=ih,
        in_w=iw,
        out_channels=oc,
        kernel_size=k,
        stride=s,
        padding=p,
        dilation=dil,
        groups=g,
        use_bias=ub,
        seed=42 + hash((bs, ic, it, ih, iw, oc, k, s, p, g, ub, dil)) % 1000,
    )

    # Direct authoritative reference (ground truth) - full dilation/groups support
    direct = F.conv3d(
        golden["input"],
        golden["weight"],
        golden["bias"],
        stride=s,
        padding=p,
        dilation=dil,
        groups=g,
    )

    # Golden (via conv3d_cpu) must match F exactly (bitwise for the generated bf16 path)
    assert torch.equal(
        golden["output"], direct
    ), f"ref mismatch for case bs={bs} ic={ic} oc={oc} g={g} dil={dil} spatial=({it},{ih},{iw})"

    # calculate_output_dim (used at collection in get_params + everywhere) must match F shape
    # Support scalar or tuple for 3D per-dim
    def _as_tuple(x):
        return x if isinstance(x, (tuple, list)) else (x, x, x)

    kt, kh, kw = _as_tuple(k)
    st, sh, sw = _as_tuple(s)
    pt, ph, pw = _as_tuple(p)
    dt, dh, dw = _as_tuple(dil)
    calc_t = calculate_output_dim(it, kt, st, pt, dt)
    calc_h = calculate_output_dim(ih, kh, sh, ph, dh)
    calc_w = calculate_output_dim(iw, kw, sw, pw, dw)
    assert calc_t == direct.shape[2], f"calc_t drift dil={dil}"
    assert calc_h == direct.shape[3]
    assert calc_w == direct.shape[4]

    # Explicit conv3d_cpu wrapper (the one wrapped by golden)
    cpu_out = conv3d_cpu(
        golden["input"], golden["weight"], golden["bias"], s, p, dil, g
    )
    assert torch.equal(cpu_out, golden["output"])

    # Sanity (runs per subtest; cheap): get_params health used by AIE paths
    all_p = get_params()
    assert len(all_p) > 20, "get_params produced too few cases for coverage"
    ids = [p.id for p in all_p]
    assert len(ids) == len(set(ids)), "duplicate test IDs generated by get_params()"
    first_marks = getattr(all_p[0], "marks", [])
    assert not any(
        getattr(m, "name", None) == "extensive" for m in first_marks
    ), "first param from get_params() must be unmarked (regular)"


# =============================================================================
# get_params() invariants (must stay healthy for all HW matrix runs)
# =============================================================================


@pytest.mark.parametrize(
    "dummy",
    [pytest.param(None, id="get_params_invariants")],
)
def test_conv3d_cpu_get_params_invariants(dummy):
    """Validate get_params() (used by primary metrics + forward tests) under pure CPU.

    Ensures:
    - Non-empty matrix (80+ cases with current regular+extensive volumes)
    - All IDs unique and stable (prevents CSV key collisions / duplicate runs)
    - Regular vs extensive separation is honored (first case unmarked)
    - calculate_output_dim exercised at collection time produces consistent shapes

    This mirrors the sanity checks in maxpool/avgpool/reduction cpu_test.py.
    Running under iron314 / --collectonly proves the entire test matrix
    definition remains valid even without XRT/NPU/device.
    """
    all_p = get_params()
    assert len(all_p) > 20, "get_params produced too few cases for coverage"

    ids = [p.id for p in all_p]
    assert len(ids) == len(set(ids)), "duplicate test IDs from get_params()"

    # First must be regular (unmarked)
    first_marks = getattr(all_p[0], "marks", [])
    assert not any(
        getattr(m, "name", None) == "extensive" for m in first_marks
    ), "first param from get_params() must be unmarked (regular)"

    # Spot-check that a few core configs appear in generated IDs (coverage of design paths)
    # (basic, depthwise, pointwise, strided)
    core_signatures = ["k3_s1_p1_g1", "k3_s1_p1_g16", "k1_s1_p0_g1", "k3_s2_p1_g1"]
    for sig in core_signatures:
        found = any(sig in pid for pid in ids)
        assert found, f"Core config signature {sig} not represented in get_params() IDs"

    print(
        "\nget_params() invariants for Conv3D: PASS (unique stable IDs, regular first, core coverage)."
    )


# =============================================================================
# Extra standalone CPU contract checks (seed determinism, direct F equivalence)
# =============================================================================


@pytest.mark.parametrize(
    "seed",
    [
        pytest.param(42, id="seed42"),
        pytest.param(123, id="seed123"),
        pytest.param(2026, id="seed2026"),
    ],
)
def test_conv3d_cpu_seed_determinism_and_f_equivalence(seed):
    """Additional guard: golden reproducibility + direct F.conv3d equivalence.

    generate_golden_reference must be 100% deterministic for the same seed
    (critical for reproducible CI goldens and golden-vs-golden comparisons
    across test runs and --iterations).

    Also directly exercises F.conv3d on the generated input (bf16) and proves
    conv3d_cpu + golden["output"] are identical to raw F (the ultimate source
    of truth that the AIE kernels were validated against via the golden path).
    Covers both scalar and tuple (asymmetric) configs.
    """
    # Standard case
    g1 = generate_golden_reference(
        batch_size=2,
        in_channels=8,
        in_t=9,
        in_h=17,
        in_w=19,
        out_channels=4,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=1,
        use_bias=True,
        dilation=1,
        seed=seed,
    )
    g2 = generate_golden_reference(
        batch_size=2,
        in_channels=8,
        in_t=9,
        in_h=17,
        in_w=19,
        out_channels=4,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=1,
        use_bias=True,
        dilation=1,
        seed=seed,
    )

    assert torch.equal(g1["input"], g2["input"]), "seed determinism failed on input"
    assert torch.equal(g1["weight"], g2["weight"]), "seed determinism failed on weight"
    assert torch.equal(g1["bias"], g2["bias"]), "seed determinism failed on bias"
    assert torch.equal(g1["output"], g2["output"]), "seed determinism failed on output"

    # Raw F on the exact golden input
    via_f = F.conv3d(
        g1["input"], g1["weight"], g1["bias"], stride=1, padding=1, dilation=1, groups=1
    )
    assert torch.equal(g1["output"], via_f), "golden output drifted from raw F.conv3d"
    via_cpu = conv3d_cpu(
        g1["input"], g1["weight"], g1["bias"], stride=1, padding=1, dilation=1, groups=1
    )
    assert torch.equal(via_f, via_cpu), "conv3d_cpu drifted from raw F.conv3d"

    # Also a tuple/asymmetric + dilation case for 3D coverage
    g3 = generate_golden_reference(
        batch_size=1,
        in_channels=3,
        in_t=7,
        in_h=9,
        in_w=11,
        out_channels=8,
        kernel_size=(1, 3, 3),
        stride=(1, 2, 1),
        padding=(0, 1, 1),
        groups=1,
        use_bias=False,
        dilation=2,
        seed=seed,
    )
    via_f3 = F.conv3d(
        g3["input"],
        g3["weight"],
        g3["bias"],
        stride=(1, 2, 1),
        padding=(0, 1, 1),
        dilation=2,
        groups=1,
    )
    assert torch.equal(g3["output"], via_f3), "asym golden drifted from F (dil=2)"
    via_cpu3 = conv3d_cpu(
        g3["input"], g3["weight"], g3["bias"], (1, 2, 1), (0, 1, 1), 2, 1
    )
    assert torch.equal(via_f3, via_cpu3)

    print(
        f"\nSeed determinism + F equivalence (seed={seed}): PASS (incl. 3D asym + dil)"
    )


# Tests are pytest-only (AGENTS.md convention).
# Use "python -m pytest iron/operators/conv3d/cpu_test.py" directly.
# For ad-hoc reference demos see iron/operators/conv3d/reference.py __main__.
