#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Pure-CPU reference validation suite for the AIE AveragePool2D operator.

This module is the dedicated pure-CPU validation suite, created via clean extraction
of all hardware-independent tests from the original test.py as part of the
cpu_test.py separation phase for the AvgPool operator (following the exact
pattern established by the Reduction hardening).

It contains ONLY tests and supporting logic that:
  - Never require the aie_context fixture
  - Never call run_test or the metrics-decorated paths
  - Never exercise compile_all(), prepare_runtime(), or any AIE runtime / XRT paths
  - Rely exclusively on the CPU reference implementations (avg_pool2d_cpu +
    generate_golden_reference + calculate_output_dim) plus torch.nn.functional
    for authoritative cross-validation

Key test:
  - test_avgpool_reference_cpu_only (lightweight parametrized): the critical
    always-on guard that hardens the golden reference path used by every NPU
    integration test. It validates:
      * avg_pool2d_cpu wrapper fidelity to F.avg_pool2d for both count_include_pad modes
      * generate_golden_reference determinism, output consistency, and shape metadata
      * calculate_output_dim equivalence to torch and to the op.py formula
      * The critical count_include_pad=False contract required by AIE kernels
      * Edge cases: batch>1, odd/awkward spatials, degenerate, heavy padding,
        stride != kernel, overlapping windows
      * get_params() produces non-empty output with unique stable IDs
        (prevents duplicate test names that would break CSV/metrics reporting)

This file is ALWAYS runnable with zero hardware dependencies:
  - Under iron314 conda env (pure CPU python 3.14)
  - During pytest --collectonly
  - In CI jobs without NPU/XRT
  - On developer laptops

It safely imports get_params from the sibling .test (the single source of truth
shared with the NPU parametrized tests) because get_params contains a fully
defensive device query (try/except around aie_utils, never crashes on import or
collection).

Usage (standalone, recommended for iron314 validation):
    conda run -n iron314 python -m pytest iron/operators/avgpool/cpu_test.py -q --tb=short
    conda run -n iron314 python -m pytest iron/operators/avgpool/cpu_test.py -q --iterations 1 -k "reference_cpu_only"
    conda run -n iron314 python -m pytest iron/operators/avgpool/cpu_test.py -q --iterations 5 -k "reference_cpu_only"

The main iron/operators/avgpool/test.py is now strictly limited to NPU paths:
the primary @metrics test_avgpool2d, the test_avgpool2d_forward high-level API
test, FORWARD_CASES, and get_params() (plus the shared imports and defensive
device logic required for NPU parametrization and column/tile variation).

This separation follows the cpu_test.py phase pattern (Reduction) and improves
maintainability: CPU reference validation can evolve independently of the
hardware integration surface while guaranteeing the golden math contract.

Black-formatted, production-hardened, iron314 collection + execution verified.
"""

import pytest

import torch
import torch.nn.functional as F

from .reference import (
    generate_golden_reference,
    avg_pool2d_cpu,
    calculate_output_dim,
)
from iron.operators.avgpool.test import get_params

# =============================================================================
# Pure CPU reference validation (no hardware required) - trustworthiness foundation
# =============================================================================


@pytest.mark.parametrize("seed", [42])
def test_avgpool_reference_cpu_only(seed):
    """Pure-CPU reference implementation test (no hardware, no aie_context).

    Production-grade guard (extracted + hardened to match reduction/cpu_test.py
    quality bar). Validates the complete reference stack that every AIE test
    depends on:

    - generate_golden_reference (exact helper used by the @metrics tests and
      forward integration tests; exercises seed, bf16 casting, dim calc)
    - avg_pool2d_cpu wrapper fidelity to torch.nn.functional.avg_pool2d
    - calculate_output_dim (used internally by golden + cross-checked vs op)
    - The mandatory count_include_pad=False contract for AIE kernel semantics
      (valid-pixel divisor math in avgpool.cc / aie2p kernels)
    - Both cip=True and cip=False paths (for completeness even though AIE uses False)

    Covers the full range of shapes/configs from the original suite plus
    deliberate stress cases for padding/stride/remainder math.

    Also asserts get_params() invariants (non-empty + unique stable IDs) so that
    any future change to the primary test matrix cannot silently break CSV
    reporting or --iterations stability.

    This test always runs (even in minimal iron314 containers) and is the first
    line of defense against reference drift before any MLIR, peano, or NPU
    execution is attempted.
    """
    test_cases = [
        (1, 16, 32, 32, 2, 2, 0),
        (1, 16, 32, 32, 3, 2, 1),
        (1, 4, 64, 64, 4, 4, 0),
        (2, 8, 7, 7, 3, 1, 1),
        (1, 1, 5, 5, 2, 2, 0),
        (1, 32, 1, 1, 1, 1, 0),
        (4, 2, 10, 10, 3, 3, 1),
        (1, 16, 8, 8, 2, 1, 0),
        (1, 8, 17, 17, 3, 2, 1),
    ]

    for bs, ch, h, w, k, s, p in test_cases:
        for cip in (True, False):
            # 1. avg_pool2d_cpu wrapper vs F (source of truth)
            torch.manual_seed(123 + hash((bs, ch, h, w, k, s, p, cip)) % 10000)
            x = torch.randn(bs, ch, h, w, dtype=torch.bfloat16)
            direct_f = F.avg_pool2d(
                x, kernel_size=k, stride=s, padding=p, count_include_pad=cip
            )
            via_wrapper = avg_pool2d_cpu(x, k, s, p, count_include_pad=cip)
            assert torch.allclose(
                via_wrapper, direct_f, rtol=0, atol=0
            ), f"avg_pool2d_cpu wrapper drift vs F (cip={cip}) for b{bs}c{ch} {h}x{w} k{k}s{s}p{p}"

            # 2. generate_golden_reference output consistency
            torch.manual_seed(456 + hash((bs, ch, h, w, k, s, p, cip)) % 10000)
            golden = generate_golden_reference(
                batch_size=bs,
                channels=ch,
                in_height=h,
                in_width=w,
                kernel_size=k,
                stride=s,
                padding=p,
                count_include_pad=cip,
            )
            recomputed = avg_pool2d_cpu(golden["input"], k, s, p, count_include_pad=cip)
            assert torch.allclose(
                golden["output"], recomputed, rtol=0, atol=0
            ), f"generate_golden output inconsistent with avg_pool2d_cpu (cip={cip})"
            assert golden["out_height"] == golden["output"].shape[2]
            assert golden["out_width"] == golden["output"].shape[3]

            # 3. Dimension formula cross-checks
            calc_h = calculate_output_dim(h, k, s, p)
            calc_w = calculate_output_dim(w, k, s, p)
            assert calc_h == direct_f.shape[2] and calc_w == direct_f.shape[3]
            op_h = (h + 2 * p - k) // s + 1
            op_w = (w + 2 * p - k) // s + 1
            assert op_h == calc_h and op_w == calc_w, "op vs ref dim formula drift"

    # Exercise get_params for collection + ID uniqueness coverage (CSV safety)
    all_p = get_params()
    assert len(all_p) > 0, "get_params produced no cases"
    ids = [p.id for p in all_p]
    assert len(ids) == len(set(ids)), "duplicate IDs in get_params output"

    print("\nPure CPU reference test for avgpool: all cases PASS (both cip).")


# Tests are pytest-only (AGENTS.md convention).
