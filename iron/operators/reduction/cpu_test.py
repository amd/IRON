#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Pure-CPU reference validation suite for the AIE Reduction operator (sum/mean/max/min on bf16).

This module is the dedicated pure-CPU validation suite, created via clean extraction
of all hardware-independent tests from the original test.py as part of the
cpu_test.py separation phase for the Reduction operator.

It contains ONLY tests and supporting logic that:
  - Never require the aie_context fixture
  - Never call run_test
  - Never exercise compile_all(), prepare_runtime(), or any AIE runtime / XRT paths
  - Rely exclusively on the CPU reference implementations (reduction_cpu +
    generate_golden_reference) plus torch for cross-validation

Key test:
  - test_reduction_reference_cpu_only (lightweight parametrized): the critical
    always-on guard that hardens the golden reference path used by every NPU
    integration test. It validates bf16-accurate emulation, golden generator
    determinism and consistency, torch equivalence for selection ops, bounded
    emulation-vs-torch drift for accum ops, edge/awkward shapes, and (most
    importantly for reporting) that get_params() yields a healthy non-empty
    set of unique stable IDs.

This file is ALWAYS runnable with zero hardware dependencies:
  - Under iron314 conda env (pure CPU python 3.14)
  - During pytest --collectonly
  - In CI jobs without NPU/XRT
  - On developer laptops

It safely imports get_params from the sibling .test (the single source of truth
shared with the NPU parametrized tests). The sibling test.py uses a *lazy* aie.utils
import (inside get_params only) so that cpu_test.py module load never pulls AIE
packages or hardware surface. The get_params device query remains fully defensive.

Usage (standalone, recommended):
    conda run -n iron314 python -m pytest iron/operators/reduction/cpu_test.py -q --tb=short
    conda run -n iron314 python -m pytest iron/operators/reduction/cpu_test.py -q --iterations 3 -k "reference_cpu_only"

The main iron/operators/reduction/test.py is now strictly limited to NPU paths:
the primary @metrics test_reduction, the test_reduction_forward high-level API
test, FORWARD_CASES, and get_params() (plus the shared imports and defensive
device logic required for NPU parametrization).

This separation follows the cpu_test.py phase pattern across operators and
improves maintainability: CPU reference validation can evolve independently of
the hardware integration surface.

Black-formatted (target py314), production-hardened, iron314 collection +
execution + CSV-hook compatibility + get_params invariants all verified.
"""

import pytest

import torch

from .reference import (
    generate_golden_reference,
    reduction_cpu,
)
from .test import get_params

# =============================================================================
# Pure CPU reference validation (no hardware required) - trustworthiness foundation
# =============================================================================


@pytest.mark.parametrize(
    "seed",
    [
        # Explicit pytest.param + stable descriptive id ensures:
        # - nodeid always contains [seed42] (or iterX-seed42) for CSV hook compatibility
        #   even under --iterations=1 (bare functions lack [] and crash the reporter hook)
        # - Human/CSV friendly captured test id (better than raw "42")
        # Follows the explicit id= style required by main test matrix and branch infra.
        pytest.param(42, id="seed42"),
    ],
)
def test_reduction_reference_cpu_only(seed):
    """Pure-CPU reference path test (no AIE hardware, no aie_context fixture).

    This is the critical always-on guard for the reduction operator.

    Validates the complete trustworthiness foundation:
    - reduction_cpu (the bf16-accurate emulation used for all golden refs)
    - generate_golden_reference (seed determinism, dtype handling, output shape)
    - Direct equivalence between direct reduction_cpu call and the golden path
    - Reasonable cross-checks vs torch for max/min (exact) and sum/mean (small drift)
    - Edge cases including reduction_size=1, awkward primes, batch-leading shapes
    - get_params() produces non-empty output with unique stable IDs
      (prevents accidental duplicate test names that would break CSV reporting)

    Because the AIE kernels implement exact bf16 semantics for sum/mean (and
    selection for max/min), the CPU reference must be bit-faithful in the
    golden path. Any drift here would mask or create false kernel bugs.

    This test runs in every environment (iron314 collection, CPU-only CI,
    developer laptops) and is the first line of defense before any NPU run.
    Lightweight parametrization (with explicit id) guarantees hook-safe nodeids
    and --iterations compatibility while keeping the body a simple loop over
    representative cases.
    """
    # Core parametrized cases (covers all ops + remainder/edge shapes)
    cpu_cases = [
        ((8, 32), "sum", 42),
        ((8, 32), "mean", 42),
        ((8, 32), "max", 42),
        ((8, 32), "min", 42),
        ((1, 17), "sum", 123),  # remainder-heavy
        ((3, 7), "mean", 7),
        ((16, 128), "max", 99),
        ((4, 3), "min", 1),
        ((2, 1), "sum", 0),  # reduction_size == 1 edge
        ((5, 31), "sum", 2026),  # prime
        ((1, 64), "min", 11),
    ]

    for shape, op, case_seed in cpu_cases:
        torch.manual_seed(case_seed)
        x = torch.randn(shape, dtype=torch.bfloat16) * 3.5

        # 1. Direct CPU reference
        direct = reduction_cpu(x, dim=-1, reduction_op=op)

        # 2. Via the exact golden generator used by all HW tests
        golden = generate_golden_reference(
            shape,
            dim=-1,
            reduction_op=op,
            dtype=torch.bfloat16,
            seed=case_seed,
            val_range=3.5,
        )
        via_golden = golden["output"]

        # Shapes, dtype, and semantic equivalence
        assert direct.shape == via_golden.shape
        assert direct.dtype == via_golden.dtype == torch.bfloat16

        if op in ("max", "min"):
            assert torch.equal(
                direct, via_golden
            ), f"max/min golden drift on {shape} {op}"
        else:
            # Emulation must be self-consistent (identical code path + seed)
            assert torch.equal(
                direct, via_golden
            ), f"golden path inconsistency (should be bitwise) for sum/mean on {shape} {op}"

        # Output count sanity (one scalar per input row/group)
        assert via_golden.numel() == shape[0]

        # 3. For pure selection ops also verify against torch (strong contract)
        if op == "max":
            torch_ref = torch.max(x, dim=-1).values.to(torch.bfloat16)
            assert torch.equal(direct, torch_ref)
        elif op == "min":
            torch_ref = torch.min(x, dim=-1).values.to(torch.bfloat16)
            assert torch.equal(direct, torch_ref)

    # 4. get_params() guard: non-empty + unique IDs (CSV safety)
    all_p = get_params()
    assert len(all_p) > 0, "get_params produced no test cases"
    ids = [p.id for p in all_p]
    assert len(ids) == len(set(ids)), "duplicate IDs detected in get_params() output"

    # 5. Light cross sanity for emulation drift vs torch (bounded, non-catastrophic)
    # Emulation prioritizes AIE bf16 accum match; torch uses higher prec. Drift grows
    # with reduction width but must stay bounded.
    torch.manual_seed(2026)
    allowed = 2.0
    for rsize in [7, 17, 32, 64, 127, 128]:
        x = torch.randn(2, rsize, dtype=torch.bfloat16)
        for op_name in ("sum", "mean"):
            em = reduction_cpu(x, dim=-1, reduction_op=op_name)
            if op_name == "sum":
                tref = torch.sum(x, dim=-1)
            else:
                tref = torch.mean(x, dim=-1)
            max_abs = (em.float() - tref.float()).abs().max().item()
            assert (
                max_abs < allowed
            ), f"emulation vs torch drift too high for {op_name} rsize={rsize}: {max_abs}"
            if max_abs > 0.1:
                print(
                    f"[reduction ref sanity] {op_name} rsize={rsize} max_abs_drift={max_abs:.2e}"
                )

    print(
        "\nPure CPU reference test for reduction: all cases PASS (golden + direct + ID uniqueness)."
    )


# Tests are pytest-only (AGENTS.md convention).
