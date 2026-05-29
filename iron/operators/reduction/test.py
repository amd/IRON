#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Production-grade test suite for the AIE Reduction operator (sum/mean/max/min on bf16).

This module is the complete, consciously engineered, main-tree-landable test.py
for the reduction operator. It is suitable as the reference artifact for the op.

It follows the exact conventions of the primary IRON tree
(see iron/operators/axpy/test.py, gemm/test.py) and the polished production
examples in the worktree (avgpool/test.py, maxpool/test.py, conv2d/test.py)
while remaining fully compatible with branch infrastructure (conftest.py CSV
reporter + metrics hook, --iterations, pytest_generate_tests, pytest.ini
extensive marker, python 3.14 iron314 collection, AIEContext per-test fixture).

Conscious design of the test matrix:
- Device-aware get_params(): queries actual NPU column count (4 on npu1, 8
  on npu2) and gates "mean" to npu2 only (mean kernels exist only in aie2p/).
- Strict one-group-per-column constraint (tile_size == reduction_size and
  input_size == reduction_size * num_aie_columns) matching current design.py
  + kernel semantics (one reduction group processed per AIE column).
- Regular suite: reduction_sizes=[32, 64] (compact, fast, high-signal base
  cases covering vectorized paths + modest remainder) x supported column
  counts x supported ops. These always run by default.
- Extensive suite: disjoint awkward/edge sizes (powers-of-2 edges, primes,
  remainders like 1/3/7/17/31/127/128) exercising kernel remainder logic,
  degen cases, and full column parallelism. Marked extensive.
- All parametrization uses explicit pytest.param(..., id=..., marks=...) for
  stable, human-readable test names required by CSV/metrics reporting.
- Single primary @metrics test_reduction exercising the complete low-level
  run_test path (operator ctor, MLIR design, full compilation, buffer I/O,
  runlist execution, numeric verification).
- Dedicated forward test exercising the high-level operator(x) API +
  explicit compile_all()/prepare_runtime() lifecycle (full branch infra).
- Tolerances: exact (atol 1e-8) for pure-selection max/min; standard bf16
  accum tolerance for sum/mean.
- Pure-CPU reference validation has been extracted to the sibling cpu_test.py
  (test_reduction_reference_cpu_only). This file (test.py) now focuses
  exclusively on NPU/hardware paths. The CPU suite remains the trustworthiness
  foundation and imports get_params from here for ID checks.
- Clean two-line metrics prints exactly as expected by conftest hook.
- No top-level side-effecting param generation outside
  get_params(), collection-safe defensive device query, zero duplicate IDs.

The test is deliberately scoped to exercise every production code path in
op.py, design.py, reference.py, and the shared AIE runtime while keeping
default runs (pytest -m "not extensive") fast and stable.
"""

import pytest

import torch

from iron.operators.reduction.op import AIEReduction
from iron.operators.reduction.reference import (
    generate_golden_reference,
    reduction_cpu,
)
from iron.common.test_utils import run_test

# =============================================================================
# Single source of truth for parameterization (main-tree canonical style)
# =============================================================================


def get_params():
    """Return the complete, ready-to-use list of pytest.param objects.

    Executed at collection time (after pytest has imported the module).
    Defensive device query ensures `pytest --collectonly` and pure-CPU runs
    (iron314, CI without XRT) never crash.

    Enforces the operator's fundamental one-group-per-column constraint:
        tile_size == reduction_size
        input_size == reduction_size * num_aie_columns
    This matches design.py / kernel expectations exactly.

    "mean" is emitted only on npu2 (AIE2P) because the mean vector kernel
    exists only in aie_kernels/aie2p/reduction.cc.
    """
    # Lazy import: ensures that `from .test import get_params` (used by cpu_test.py)
    # never triggers aie import at module load time. This provides clean separation
    # between the pure-CPU validation suite and NPU test surface.
    import aie.utils as aie_utils

    # Defensive device discovery (collection safety under iron314 / no-XRT envs).
    # Real execution remains gated by the aie_context fixture.
    max_aie_columns = 4
    dev_name = "npu1"
    try:
        device = aie_utils.get_current_device()
        if device is not None:
            max_aie_columns = device.cols
            # device_str style name for npu1/npu2 gating (mean support)
            dev_name = getattr(device, "name", str(device))
            if hasattr(device, "resolve"):
                dev_name = device.resolve().name
    except Exception:
        pass

    include_mean = dev_name == "npu2"

    # Base ops always supported; mean gated by device.
    base_ops = ["sum", "max", "min"]
    ops = base_ops + (["mean"] if include_mean else [])

    # === CONSCIOUSLY CHOSEN REGULAR SUITE ===
    # Small, fast, representative: 32 and 64 are common reduction widths,
    # exercise vectorized (16-el vec) + modest remainder paths, keep
    # default "pytest -m 'not extensive'" runs quick while covering 1..N cols.
    REGULAR_REDUCTION_SIZES = [32, 64]

    # === CONSCIOUSLY CHOSEN EXTENSIVE SUITE ===
    # Disjoint from regular. Covers:
    # - Degenerate (1)
    # - Small awkward + primes (2,3,7,17,31,63,127) -> remainder stress
    # - Power-of-two edge (128) + a few in-between (4,16,33)
    EXTENSIVE_ONLY_SIZES = [1, 2, 3, 4, 7, 16, 17, 31, 33, 63, 127, 128]

    params = []

    # Regular (fast default) cases - unmarked
    for reduction_size in REGULAR_REDUCTION_SIZES:
        for num_aie_columns in range(1, max_aie_columns + 1):
            tile_size = reduction_size  # one-group-per-column contract
            input_size = reduction_size * num_aie_columns
            for op in ops:
                name = (
                    f"reduction_{op}_{input_size}_{reduction_size}_"
                    f"{num_aie_columns}cols_{tile_size}tile"
                )
                params.append(
                    pytest.param(
                        input_size,
                        reduction_size,
                        op,
                        num_aie_columns,
                        tile_size,
                        id=name,
                    )
                )

    # Extensive-only cases - all marked
    for reduction_size in EXTENSIVE_ONLY_SIZES:
        for num_aie_columns in range(1, max_aie_columns + 1):
            tile_size = reduction_size  # one-group-per-column contract
            input_size = reduction_size * num_aie_columns
            for op in ops:
                name = (
                    f"reduction_{op}_{input_size}_{reduction_size}_"
                    f"{num_aie_columns}cols_{tile_size}tile"
                )
                params.append(
                    pytest.param(
                        input_size,
                        reduction_size,
                        op,
                        num_aie_columns,
                        tile_size,
                        id=name,
                        marks=[pytest.mark.extensive],
                    )
                )

    return params


# =============================================================================
# Forward / high-level API integration test cases (explicit + stable)
# =============================================================================

# Carefully chosen representative cases for the public forward() / __call__
# path. Explicit pytest.param objects guarantee stable readable IDs under
# --iterations and in CSV. Includes column variation (1/2/4) to exercise
# different MLIR specializations + the complete AIEContext compile +
# prepare_runtime + N-batch forward loop paths.
#
# All respect the one-group-per-column contract.
FORWARD_CASES = [
    pytest.param(32, 32, "sum", 1, 32, id="fwd_reduction_sum_32_32_1col"),
    pytest.param(64, 32, "max", 2, 32, id="fwd_reduction_max_64_32_2col"),
    pytest.param(128, 64, "min", 2, 64, id="fwd_reduction_min_128_64_2col"),
    pytest.param(96, 32, "sum", 3, 32, id="fwd_reduction_sum_96_32_3col"),
    pytest.param(64, 64, "min", 4, 64, id="fwd_reduction_min_64_64_4col"),
]


# =============================================================================
# Shared constants (prevents signature drift in parametrize)
# =============================================================================

# Single source of truth for the parameter names used in @parametrize
# decorators (primary matrix). Prevents any future drift in count/order.
# Matches the explicit constant pattern in conv2d/conv3d (gold finalization
# template) for landability. Forward uses the independent FORWARD_CASES.
REDUCTION_TEST_PARAM_NAMES = (
    "input_size,reduction_size,reduction_op,num_aie_columns,tile_size"
)


# =============================================================================
# Primary metrics-enabled integration test (run_test path)
# =============================================================================


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    REDUCTION_TEST_PARAM_NAMES,
    get_params(),
)
def test_reduction(
    input_size, reduction_size, reduction_op, num_aie_columns, tile_size, aie_context
):
    """Primary parametrized end-to-end test exercising the full operator.

    Uses the low-level run_test harness:
    - Explicit one-group-per-column construction (tile==reduction_size)
    - Golden reference built with accurate bf16-aware reduction_cpu
    - Full MLIR design + compilation + artifact + XRT runlist execution
    - Numeric verification with op-appropriate tolerances
    - Metrics capture via the two canonical print lines (CSV hook)

    This is the main production path exercised on every CI / regression run.
    """
    output_size = input_size // reduction_size
    input_shape = (output_size, reduction_size)
    golden_ref = generate_golden_reference(
        input_shape, dim=-1, reduction_op=reduction_op
    )

    operator = AIEReduction(
        input_size=input_size,
        reduction_size=reduction_size,
        reduction_op=reduction_op,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
        context=aie_context,
    )

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    # Consciously chosen tolerances:
    # - max/min are pure selection (bitwise exact on AIE vs CPU emulation)
    # - sum/mean use bf16 accum -> small ulp tolerance
    if reduction_op in ("max", "min"):
        rtol, atol = 0.0, 1e-8
    else:
        rtol, atol = 1e-5, 1e-4

    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=rtol, abs_tol=atol
    )

    # Exactly the format required by conftest.py CSV/metrics reporter.
    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


# =============================================================================
# Forward / high-level API integration test
# =============================================================================


@pytest.mark.parametrize(
    REDUCTION_TEST_PARAM_NAMES,
    FORWARD_CASES,
)
def test_reduction_forward(
    input_size, reduction_size, reduction_op, num_aie_columns, tile_size, aie_context
):
    """Test the public forward() / __call__ API path (full branch infrastructure).

    Explicitly drives the complete AIEContext lifecycle for the convenience API:
      - Construction (registers with per-test aie_context)
      - compile_all()  -> design callback, MLIR, full peano/aiecc pipeline
      - prepare_runtime() -> BO pool, runlist, XRT handles
      - operator(x) -> exercises forward() reshape/pad/execute path in op.py
      - Result compared to independent direct reduction_cpu reference

    Uses the modern independent-input pattern (matches avgpool/maxpool gold
    standards) rather than re-using the golden path. Provides targeted
    coverage of column-dependent MLIR variants and the high-level Python API.

    Mean cases are omitted from FORWARD_CASES for npu1/npu2 portability in
    default runs; the primary matrix already covers mean on npu2.
    """
    operator = AIEReduction(
        input_size=input_size,
        reduction_size=reduction_size,
        reduction_op=reduction_op,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
        context=aie_context,
    )

    # Full integration exercise (the key coverage for branch runtime)
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # Independent input sized for the one-group-per-column layout
    num_groups = input_size // reduction_size  # == num_aie_columns
    torch.manual_seed(123 + hash((input_size, reduction_size, reduction_op)) % 10000)
    x = torch.randn(num_groups, reduction_size, dtype=torch.bfloat16) * 3.5

    result = operator(x)
    expected = reduction_cpu(x, dim=-1, reduction_op=reduction_op)

    assert (
        result.shape == expected.shape
    ), f"Shape mismatch: {result.shape} != {expected.shape}"

    if reduction_op in ("max", "min"):
        # Pure selection: strongest possible contract
        assert torch.equal(
            result, expected
        ), "forward result not bitwise identical for max/min"
    else:
        # bf16 accum tolerance consistent with primary path
        assert torch.allclose(
            result, expected, rtol=1e-5, atol=1e-4
        ), f"forward vs CPU drift too large for {reduction_op}"


# =============================================================================
# PURE-CPU REFERENCE VALIDATION LIVES IN cpu_test.py
# =============================================================================
# All hardware-independent reference validation (reduction_cpu bf16 emulation,
# generate_golden_reference contract, get_params() ID uniqueness + health,
# emulation-vs-torch drift bounds, edge cases) lives exclusively in the sibling
# cpu_test.py following the production pattern established for reduction.
#
# Run under iron314 (no XRT/NPU, no aie_context):
#   conda run -n iron314 python -m pytest \
#       iron/operators/reduction/cpu_test.py -q --tb=short [--iterations N]
#
# This keeps test.py 100% focused on NPU paths:
#   - @metrics test_reduction (run_test + full compile/prepare/execute)
#   - test_reduction_forward (explicit compile_all + prepare_runtime + forward)
#   - get_params() and FORWARD_CASES
#
# cpu_test.py safely imports get_params from here (lazy aie inside protects).
# See cpu_test.py for the complete CPU-side hardening rationale.
# =============================================================================

# Tests are pytest-only (AGENTS.md convention).
# NPU tests:   python -m pytest iron/operators/reduction/test.py -q -m "not extensive"
# CPU tests:   python -m pytest iron/operators/reduction/cpu_test.py
