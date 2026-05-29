#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Pure-CPU reference validation suite for the AIE Conv2D operator (bf16).

This module is the dedicated pure-CPU validation suite for Conv2D, created as
part of the cpu_test.py separation phase (following the exact pattern
established by reduction/cpu_test.py).

It contains ONLY tests and supporting logic that:
  - Never require the aie_context fixture
  - Never call run_test or any metrics path
  - Never exercise compile_all(), prepare_runtime(), or any AIE runtime / XRT paths
  - Rely exclusively on the CPU reference implementations (conv2d_cpu +
    generate_golden_reference + calculate_output_dim) plus torch for cross-validation

Primary tests:
  - test_conv2d_reference_cpu_only (parametrized with stable id for hook safety):
    exercises a wide matrix of configs (bias/nobias, depthwise, pointwise, strided,
    grouped, batch>1, awkward padding) + golden vs F.conv2d + conv2d_cpu wrapper +
    calculate_output_dim + op formula cross-checks + live get_params health.
  - test_conv2d_cpu_reference_only (parametrized with stable "cpu_*" ids):
    the direct analogue of reduction's cpu reference test. Guarantees that the
    *exact* generate_golden_reference call used by all HW tests produces output
    bit-identical to direct conv2d_cpu. Covers reproducibility, shape/config
    recording, and full config families.
  - test_conv2d_reference_sanity: reproducibility across seeds, direct conv2d_cpu
    edge usage, and bf16-vs-fp32 drift documentation for tolerance rationale.

This file is ALWAYS runnable with zero hardware dependencies:
  - Under iron314 conda env (pure CPU python 3.14)
  - During pytest --collectonly (critical for collection safety)
  - In CI jobs without NPU/XRT
  - On developer laptops

It safely imports get_params from the sibling .test (the single source of truth
shared with the NPU parametrized tests) because get_params contains a fully
defensive device query (try/except around aie_utils, never crashes on import).

Usage (standalone, recommended for iron314 validation):
    conda run -n iron314 python -m pytest iron/operators/conv2d/cpu_test.py -q --tb=short
    conda run -n iron314 python -m pytest iron/operators/conv2d/cpu_test.py -q --iterations 1 -k "reference_cpu_only"
    conda run -n iron314 python -m pytest iron/operators/conv2d/cpu_test.py -q --iterations 3

The main iron/operators/conv2d/test.py is now strictly limited to NPU paths:
the primary @metrics test_conv2d, the test_conv2d_forward high-level API test,
FORWARD_CASES, and get_params() (plus shared defensive device logic and
calculate_output_dim import required by the parametrization matrix).

This separation improves maintainability: CPU reference validation can evolve
independently of the hardware integration surface, and iron314 / CPU CI can
gate on cpu_test.py alone before any NPU jobs.

All golden data fed to HW verification is now doubly guarded by the contract
tests in this file.
"""

import pytest

import torch
import torch.nn.functional as F

from .reference import (
    generate_golden_reference,
    conv2d_cpu,
    calculate_output_dim,
)
from .test import get_params

# =============================================================================
# Pure CPU reference validation (no hardware required) - trustworthiness foundation
# =============================================================================


@pytest.mark.parametrize(
    "dummy",
    [pytest.param(None, id="reference_cpu_only")],
)
def test_conv2d_reference_cpu_only(dummy):
    """Pure-CPU reference path test (no AIE hardware, no aie_context fixture).

    Validates the entire reference implementation in isolation:
    - generate_golden_reference (the exact helper used by all AIE tests)
    - conv2d_cpu wrapper around F.conv2d
    - calculate_output_dim (used in get_params for out dim + divisibility)
    against the authoritative torch.nn.functional.conv2d directly.

    Covers: bias on/off, standard, depthwise (groups==in==out), pointwise (1x1),
    strided+pad, groups>1, batch>1, multiple spatial sizes, and awkward padding.

    This test *always* runs (even in minimal iron314 containers without XRT/NPU)
    and is the critical regression guard for golden math/shape contract before
    any column-chunked MLIR, ObjectFIFOs, or runtime paths are involved.

    Also performs collection-time sanity on all_params / get_params to ensure
    the matrix (and its regular/extensive marking) remains healthy.
    """
    # Broad representative cases exercising all important golden + dim paths.
    # All cases satisfy F.conv2d validity (spatials after pad >= kernel).
    test_cases = [
        # (bs, ic, h, w, oc, k, s, p, g, use_bias)
        (1, 3, 32, 32, 16, 3, 1, 1, 1, True),  # basic bias (regular style)
        (1, 3, 32, 32, 16, 3, 1, 1, 1, False),  # basic nobias
        (1, 16, 32, 32, 16, 3, 1, 1, 16, True),  # depthwise +bias
        (1, 16, 32, 32, 16, 3, 1, 1, 16, False),  # depthwise nobias
        (2, 32, 16, 16, 64, 1, 1, 0, 1, True),  # pointwise + batch>1
        (1, 16, 32, 32, 32, 3, 2, 1, 1, True),  # strided + pad
        (1, 16, 32, 32, 32, 3, 2, 0, 1, True),  # strided no pad
        (1, 8, 8, 8, 16, 3, 1, 2, 2, True),  # groups=2 + overhang pad
        (1, 4, 7, 9, 8, 3, 1, 1, 2, False),  # groups + small + nobias
        (4, 4, 8, 8, 8, 1, 1, 0, 1, True),  # batch + pointwise no pad
    ]

    for bs, ic, h, w, oc, k, s, p, g, ub in test_cases:
        golden = generate_golden_reference(
            batch_size=bs,
            in_channels=ic,
            in_height=h,
            in_width=w,
            out_channels=oc,
            kernel_size=k,
            stride=s,
            padding=p,
            groups=g,
            use_bias=ub,
            seed=42 + hash((bs, ic, h, w, oc, k, s, p, g, ub)) % 10000,
        )

        # Direct authoritative ground truth
        direct = F.conv2d(
            golden["input"],
            golden["weight"],
            golden["bias"],
            stride=s,
            padding=p,
            groups=g,
        )

        # Golden must match F.conv2d exactly (same contract as conv2d_cpu)
        assert torch.equal(
            golden["output"], direct
        ), f"ref mismatch for case {(bs,ic,h,w,oc,k,s,p,g,ub)}"

        # Exercise conv2d_cpu wrapper itself (the one wrapped by golden)
        cpu_out = conv2d_cpu(
            golden["input"], golden["weight"], golden["bias"], s, p, 1, g
        )
        assert torch.equal(cpu_out, golden["output"])

        # Exercise calculate_output_dim (used by get_params for divis + naming)
        calc_h = calculate_output_dim(h, k, s, p, 1)
        calc_w = calculate_output_dim(w, k, s, p, 1)
        assert calc_h == direct.shape[2]
        assert calc_w == direct.shape[3]

        # Also match operator's internal formula (for cross-guard)
        op_h = (h + 2 * p - k) // s + 1
        op_w = (w + 2 * p - k) // s + 1
        assert op_h == calc_h and op_w == calc_w

    # Live sanity: get_params / all_params must be healthy at collection time
    all_p = get_params()
    assert len(all_p) > 20, "get_params produced too few cases"
    non_ext = [
        p
        for p in all_p
        if not any(
            getattr(m, "name", None) == "extensive" for m in getattr(p, "marks", [])
        )
    ]
    assert len(non_ext) >= 1, "No regular (non-extensive) cases in matrix"
    # The first regular must be unmarked
    first_reg_marks = getattr(non_ext[0], "marks", [])
    assert not any(
        getattr(m, "name", None) == "extensive" for m in first_reg_marks
    ), "First regular case unexpectedly marked extensive"

    print(
        "\nConv2D pure CPU reference test: all cases PASS (exact matches + dim checks)."
    )
    print(f"  all_params count: {len(all_p)} (regular + extensive matrix healthy)")


# Explicit CPU_REFERENCE_CASES using production-grade pytest.param with stable ids.
# These mirror (and are a superset of) the families exercised by get_params and
# the forward tests. IDs are human-readable and safe for CSV/metrics reporting.
CPU_REFERENCE_CASES = [
    # Core + bias variants (matches regular matrix spirit)
    pytest.param(1, 3, 32, 32, 16, 3, 1, 1, 1, True, 42, id="cpu_basic_bias"),
    pytest.param(1, 3, 32, 32, 16, 3, 1, 1, 1, False, 42, id="cpu_basic_nobias"),
    # Depthwise
    pytest.param(1, 16, 32, 32, 16, 3, 1, 1, 16, True, 123, id="cpu_depthwise_bias"),
    pytest.param(1, 16, 32, 32, 16, 3, 1, 1, 16, False, 123, id="cpu_depthwise_nobias"),
    # Pointwise
    pytest.param(1, 32, 32, 32, 64, 1, 1, 0, 1, True, 7, id="cpu_pointwise_bias"),
    pytest.param(1, 32, 32, 32, 64, 1, 1, 0, 1, False, 7, id="cpu_pointwise_nobias"),
    # Strided cases (p=0 and p=1)
    pytest.param(1, 16, 32, 32, 32, 3, 2, 1, 1, True, 99, id="cpu_strided_p1"),
    pytest.param(1, 16, 32, 32, 32, 3, 2, 0, 1, True, 99, id="cpu_strided_p0"),
    # Grouped
    pytest.param(1, 8, 16, 16, 16, 3, 1, 2, 2, True, 2026, id="cpu_groups2"),
    pytest.param(1, 4, 16, 16, 8, 3, 1, 1, 2, True, 11, id="cpu_groups2_small"),
    # batch > 1 (exercises generate path used by forward batch-2 test)
    pytest.param(2, 3, 32, 32, 16, 3, 1, 1, 1, True, 55, id="cpu_batch2"),
    pytest.param(3, 16, 16, 16, 16, 3, 1, 1, 16, False, 88, id="cpu_depthwise_batch3"),
    # Different spatial + seed for reproducibility cross-check
    pytest.param(1, 3, 64, 64, 16, 3, 1, 1, 1, True, 0, id="cpu_large_spatial"),
]


@pytest.mark.parametrize(
    "batch,in_ch,h,w,out_ch,k,s,p,g,use_bias,seed",
    CPU_REFERENCE_CASES,
)
def test_conv2d_cpu_reference_only(
    batch, in_ch, h, w, out_ch, k, s, p, g, use_bias, seed
):
    """Pure-CPU validation of golden reference + conv2d_cpu (no HW, no aie_context).

    This is the Conv2D analogue of reduction's test_reduction_cpu_reference_only.
    It guarantees that the *exact* generate_golden_reference call (with the
    identical args used by the metrics and forward tests) produces an "output"
    that is bit-for-bit / numerically identical to a direct conv2d_cpu invocation
    on the generated tensors.

    Covers:
    - Every major config family in get_params (bias, nobias, depthwise, pointwise,
      strided p=0/1, grouped)
    - batch=1 (the run_test path) and batch>1 (the forward batching path)
    - Multiple seeds for reproducibility
    - Shape/dtype agreement and exact match (same code path inside golden)

    If this test ever fails, the golden data fed to HW verification is suspect.
    """
    # Via the golden path (what HW tests actually use)
    golden = generate_golden_reference(
        batch_size=batch,
        in_channels=in_ch,
        in_height=h,
        in_width=w,
        out_channels=out_ch,
        kernel_size=k,
        stride=s,
        padding=p,
        groups=g,
        use_bias=use_bias,
        dtype=torch.bfloat16,
        seed=seed,
    )
    via_golden = golden["output"]

    # Direct call to the CPU reference (thin F.conv2d wrapper)
    direct = conv2d_cpu(
        input=golden["input"],
        weight=golden["weight"],
        bias=golden["bias"],
        stride=s,
        padding=p,
        dilation=1,
        groups=g,
    )

    # Must be identical (same seed + same deterministic path through conv2d_cpu)
    assert (
        direct.shape == via_golden.shape
    ), f"Shape mismatch direct vs golden: {direct.shape} vs {via_golden.shape}"
    assert direct.dtype == via_golden.dtype == torch.bfloat16

    # Exact match expected (identical computation, no AIE involved)
    assert torch.equal(direct, via_golden), (
        "conv2d_cpu direct result does not bitwise match golden['output'] "
        "(the value passed to run_test / forward). This breaks the reference contract."
    )

    # Sanity: config recorded in golden matches request
    cfg = golden["config"]
    assert cfg["batch_size"] == batch
    assert cfg["groups"] == g
    assert cfg["use_bias"] == use_bias
    # Output spatial from golden must match our shared calculate
    assert via_golden.shape[2] == calculate_output_dim(h, k, s, p, 1)
    assert via_golden.shape[3] == calculate_output_dim(w, k, s, p, 1)


@pytest.mark.parametrize(
    "dummy",
    [pytest.param(None, id="reference_sanity")],
)
def test_conv2d_reference_sanity(dummy):
    """Sanity cross-checks and documentation of bf16 reference behavior (no HW).

    - Verifies generate_golden works for edge-ish sizes not in the main matrix.
    - Documents that we rely on torch F.conv2d(bf16) as the reference (no
      full ml_dtypes emulation like reduction sum/mean because conv MACs are
      more complex).
    - Quick reproducibility check: same seed -> identical golden across calls.
    - Exercises conv2d_cpu directly with dilation=1 (the only supported value).
    """
    torch.manual_seed(2026)

    # Reproducibility: two independent calls with same seed must match exactly
    g1 = generate_golden_reference(
        batch_size=2,
        in_channels=8,
        in_height=17,
        in_width=19,
        out_channels=4,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=1,
        use_bias=True,
        seed=123,
    )
    g2 = generate_golden_reference(
        batch_size=2,
        in_channels=8,
        in_height=17,
        in_width=19,
        out_channels=4,
        kernel_size=3,
        stride=1,
        padding=1,
        groups=1,
        use_bias=True,
        seed=123,
    )
    assert torch.equal(g1["input"], g2["input"])
    assert torch.equal(g1["weight"], g2["weight"])
    assert torch.equal(g1["bias"], g2["bias"])
    assert torch.equal(g1["output"], g2["output"])

    # Direct conv2d_cpu sanity (covers a non-default spatial + stride + no bias)
    x = g1["input"][:1]  # take first batch element
    w = g1["weight"]
    direct_out = conv2d_cpu(x, w, bias=None, stride=2, padding=0, groups=1)
    # Must have the shape predicted by the shared calculator
    exp_h = calculate_output_dim(17, 3, 2, 0, 1)
    exp_w = calculate_output_dim(19, 3, 2, 0, 1)
    assert direct_out.shape == (1, 4, exp_h, exp_w)

    # bf16 vs "higher precision" reference drift note (for future tolerance tuning)
    # We compute a quick fp32 reference for the same bf16-cast inputs to show
    # the magnitude of bf16 rounding effect (not a test failure, just visibility).
    x_fp32 = x.to(torch.float32)
    w_fp32 = w.to(torch.float32)
    fp32_ref = F.conv2d(x_fp32, w_fp32, bias=None, stride=2, padding=0, groups=1)
    bf16_from_fp32 = fp32_ref.to(torch.bfloat16)
    max_abs_drift = (bf16_from_fp32 - direct_out).abs().max().item()
    # Drift is expected; we only log if "surprisingly large" for awareness.
    if max_abs_drift > 0.5:
        print(
            f"[conv2d ref sanity] observed bf16-vs-fp32-ref drift={max_abs_drift:.4f} "
            "(expected for bf16 conv; justifies 0.05 rel tol in HW tests)"
        )
    # Always pass; this is informational only.


# Tests are pytest-only (AGENTS.md convention).
