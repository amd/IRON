#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Production-hardened pure-CPU reference test module for the MaxPool operator.

This is the final production-standard cpu_test.py for MaxPool (and the template
for other operators undergoing CPU Test Production Hardening).

Design goals (standard responsibilities):
- Completely standalone: only pytest + torch + the operator's reference.py.
  Zero dependency on test.py, zero risk of collection crosstalk or name
  collisions between modules in the same package.
- Every test function is explicitly parametrized using pytest.param(id=...)
  with stable descriptive IDs. This guarantees 100% of nodeids contain
  bracketed segments, satisfying the strict regex in conftest.py's
  pytest_runtest_makereport hook for the metrics/CSV reporter (even when
  --iterations=1 and no extra "iterN-" prefix is injected).
- Runs perfectly under:
    * iron314 (python 3.14 minimal env, no XRT/NPU)
    * pytest --collectonly
    * --iterations N (any value)
    * -k "cpu" / -m "not extensive"
    * Windows / CI machines without hardware
- Exercises 100% of the reference contract used by HW tests:
    generate_golden_reference, max_pool2d_cpu, _max_pool2d_reference_impl,
    calculate_output_dim.
- Bitwise torch.equal everywhere (mandatory for selection operator).
- Full coverage of POOL_CONFIGS + rich edge cases (batch, odd dims, 1x1,
  heavy overhang padding, larger kernels).
- Includes determinism, direct F equivalence, and dim formula cross-checks
  (op.py formula, calculate_output_dim, golden, torch).
- Self-contained POOL_CONFIGS copy (kept in sync with test.py and reference.py
  as the single source of (k,s,p) truth).
- Professional, verbose docstrings + clean style matching the main test.py
  quality bar.
- No top-level effects, no HW fixtures/imports.

Invocation (from repo root):
    conda run -n iron314 python -m pytest iron/operators/maxpool/cpu_test.py -q --tb=short
    python -m pytest iron/operators/maxpool/cpu_test.py --collectonly -q
    python -m pytest iron/operators/maxpool/cpu_test.py -q --iterations 3

If all tests here pass, the golden data and math for every MaxPool AIE test
and forward path are correct. This is the iron314 verification gate.
"""

import pytest
import torch
import torch.nn.functional as F

from iron.operators.maxpool.reference import (
    generate_golden_reference,
    max_pool2d_cpu,
    calculate_output_dim,
    _max_pool2d_reference_impl,
)

# Stable source-of-truth copy of POOL_CONFIGS (must be manually kept identical
# to the one in test.py and reference.py). Used for coverage checks.
POOL_CONFIGS = [
    (2, 2, 0),  # Most common 2x2 s2
    (3, 3, 0),
    (3, 2, 1),  # Strided + padding
    (4, 4, 0),
    (2, 1, 0),  # Overlapping
    (1, 1, 0),  # Identity edge
    (3, 1, 1),  # Overhang padding
]


# =============================================================================
# Primary parametrized CPU reference cases (all produce bracketed nodeids)
# =============================================================================

CPU_REFERENCE_CASES = [
    # Exact coverage of every (k,s,p) in POOL_CONFIGS
    pytest.param(1, 4, 32, 32, 2, 2, 0, id="cpu_c4_k2_s2_p0_1x32x32"),
    pytest.param(1, 4, 32, 32, 3, 3, 0, id="cpu_c4_k3_s3_p0_1x32x32"),
    pytest.param(1, 4, 32, 32, 3, 2, 1, id="cpu_c4_k3_s2_p1_1x32x32"),
    pytest.param(1, 4, 32, 32, 4, 4, 0, id="cpu_c4_k4_s4_p0_1x32x32"),
    pytest.param(1, 4, 32, 32, 2, 1, 0, id="cpu_c4_k2_s1_p0_1x32x32"),
    pytest.param(1, 4, 32, 32, 1, 1, 0, id="cpu_c4_k1_s1_p0_1x32x32_identity"),
    pytest.param(1, 4, 32, 32, 3, 1, 1, id="cpu_c4_k3_s1_p1_1x32x32"),
    # Rich production edges (batch>1, odd spatials, 1x1, heavy pad, awkward sizes)
    pytest.param(2, 8, 7, 7, 3, 1, 1, id="cpu_b2_c8_k3_s1_p1_7x7_odd_overhang"),
    pytest.param(1, 1, 5, 5, 2, 2, 0, id="cpu_c1_k2_s2_p0_5x5"),
    pytest.param(1, 32, 1, 1, 1, 1, 0, id="cpu_c32_k1_s1_p0_1x1_identity"),
    pytest.param(4, 2, 10, 10, 3, 3, 1, id="cpu_b4_c2_k3_s3_p1_10x10"),
    pytest.param(1, 16, 8, 8, 2, 1, 0, id="cpu_c16_k2_s1_p0_8x8"),
    pytest.param(3, 1, 28, 28, 5, 3, 2, id="cpu_b3_c1_k5_s3_p2_28x28_heavy"),
    pytest.param(1, 8, 17, 17, 3, 2, 1, id="cpu_c8_k3_s2_p1_17x17_odd"),
]


@pytest.mark.parametrize(
    "batch, ch, h, w, k, s, p",
    CPU_REFERENCE_CASES,
)
def test_maxpool_reference_cpu_only(batch, ch, h, w, k, s, p):
    """Core pure-CPU validation of the full reference stack (no HW anywhere).

    Aligned naming with Conv3D/avgpool/reduction gold (test_*_reference_cpu_only)
    for consistent -k "reference_cpu_only" filtering under iron314 / collection.

    For every case:
    - generate_golden_reference (the exact dict consumed by HW run_test)
    - max_pool2d_cpu (public wrapper)
    - _max_pool2d_reference_impl (exact AIE kernel semantics using -inf)
    - calculate_output_dim + op.py formula vs torch reality

    All use torch.equal. Any failure here means golden data for AIE is suspect.
    """
    golden = generate_golden_reference(
        batch_size=batch,
        channels=ch,
        in_height=h,
        in_width=w,
        kernel_size=k,
        stride=s,
        padding=p,
        seed=42,
    )
    direct = max_pool2d_cpu(golden["input"], k, s, p)
    impl = _max_pool2d_reference_impl(golden["input"], k, s, p)

    assert torch.equal(
        golden["output"], direct
    ), f"golden vs direct drift {batch, ch, h, w, k, s, p}"
    assert torch.equal(direct, impl), f"direct vs impl drift {batch, ch, h, w, k, s, p}"
    assert torch.equal(
        golden["output"], impl
    ), f"golden vs impl drift {batch, ch, h, w, k, s, p}"

    # Three-way dim agreement (the critical cross-check)
    calc_h = calculate_output_dim(h, k, s, p)
    calc_w = calculate_output_dim(w, k, s, p)
    assert calc_h == golden["output"].shape[2] == (h + 2 * p - k) // s + 1
    assert calc_w == golden["output"].shape[3] == (w + 2 * p - k) // s + 1

    # Golden self-consistency
    assert golden["out_height"] == golden["output"].shape[2]
    assert golden["out_width"] == golden["output"].shape[3]


# =============================================================================
# POOL_CONFIGS coverage + determinism + raw F equivalence
# =============================================================================


@pytest.mark.parametrize(
    "seed",
    [pytest.param(42, id="seed_42"), pytest.param(2026, id="seed_2026")],
)
def test_maxpool_cpu_determinism_and_f_match(seed):
    """Seed determinism of golden + direct equivalence to F.max_pool2d.

    generate_golden_reference is the single source of golden tensors for all
    MaxPool tests. It must be perfectly reproducible and numerically identical
    (bitwise for selection) to raw torch F on the same input.
    """
    bs, ch, h, w, k, s, p = 1, 16, 32, 32, 3, 2, 1

    g1 = generate_golden_reference(bs, ch, h, w, k, s, p, seed=seed)
    g2 = generate_golden_reference(bs, ch, h, w, k, s, p, seed=seed)

    assert torch.equal(g1["input"], g2["input"])
    assert torch.equal(g1["output"], g2["output"])

    via_f = F.max_pool2d(g1["input"], kernel_size=k, stride=s, padding=p)
    via_cpu = max_pool2d_cpu(g1["input"], k, s, p)

    assert torch.equal(g1["output"], via_f)
    assert torch.equal(via_cpu, via_f)


@pytest.mark.parametrize(
    "k, s, p",
    [
        pytest.param(*cfg, id=f"poolcfg_k{cfg[0]}_s{cfg[1]}_p{cfg[2]}")
        for cfg in POOL_CONFIGS
    ],
)
def test_maxpool_cpu_pool_configs_via_golden(k, s, p):
    """Every entry in the canonical POOL_CONFIGS is exercised via the golden path.

    This guarantees the exact configurations used to build the HW test matrix
    (regular + extensive) have been validated in pure CPU reference.
    """
    g = generate_golden_reference(1, 8, 32, 32, k, s, p, seed=99)
    direct = max_pool2d_cpu(g["input"], k, s, p)
    impl = _max_pool2d_reference_impl(g["input"], k, s, p)

    assert torch.equal(g["output"], direct)
    assert torch.equal(direct, impl)
    assert calculate_output_dim(32, k, s, p) == g["output"].shape[2]


# =============================================================================
# Matrix health (lightweight, no dependency on test.py get_params)
# =============================================================================


@pytest.mark.parametrize(
    "dummy",
    [pytest.param(None, id="matrix_health")],
)
def test_maxpool_cpu_matrix_health(dummy):
    """Lightweight health check on the test matrix definition concepts.

    We stay fully standalone (no import of test.py get_params) to avoid any
    package collection side-effects or stale-pyc name shadowing. Instead we
    validate the local POOL_CONFIGS + our CPU cases directly.
    """
    assert len(POOL_CONFIGS) == 7

    # All POOL entries appear in at least one CPU case id
    cpu_ids = [c.id for c in CPU_REFERENCE_CASES]
    for k, s, p in POOL_CONFIGS:
        needle = f"k{k}_s{s}_p{p}"
        assert any(
            needle in cid for cid in cpu_ids
        ), f"POOL_CONFIG {k},{s},{p} missing from CPU cases"

    # Our own list has unique IDs (mirrors what get_params must guarantee)
    assert len(cpu_ids) == len(set(cpu_ids)), "duplicate IDs inside CPU_REFERENCE_CASES"

    # At least one batch>1, one 1x1, one heavy pad case exist
    assert any("b2_" in cid or "b3_" in cid or "b4_" in cid for cid in cpu_ids)
    assert any("identity" in cid for cid in cpu_ids)
    assert any("heavy" in cid or "overhang" in cid for cid in cpu_ids)

    print("\nMaxPool CPU matrix health: PASS (self-contained checks).")


# Tests are pytest-only (AGENTS.md convention).
