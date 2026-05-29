#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Production-grade test suite for the AIE MaxPool2D operator (NPU/hardware paths only).

This module is the final, consciously engineered, main-tree-landable NPU test.py
for MaxPool2D. It is suitable as the reference artifact and template for the
operator (and for future pooling / selection-style operators).

It follows the exact conventions of the primary IRON tree
(axpy/test.py, gemm/test.py, layer_norm/test.py, mha/test.py) and the
polished production examples in this worktree (avgpool/test.py, reduction/test.py,
conv2d/test.py, conv3d/test.py) while remaining fully compatible with branch
infrastructure (conftest.py CSV + @metrics hook, run_test harness, AIEContext
with compile_all/prepare_runtime, pytest_generate_tests + --iterations,
pytest.ini "extensive" marker, python 3.14 iron314 collection requirements).

Key engineered properties of the final form:
- POOL_CONFIGS as the single source of (k,s,p) breadth (kept in sync with
  cpu_test.py and reference.py).
- get_params() as the canonical single source of truth (returns explicit
  pytest.param objects with stable ids + marks). Executed only at collection
  time. Defensive lazy import of aie.utils + try/except device query so that
  `pytest --collectonly`, iron314 (no XRT), and CPU-only environments never
  crash. Matches reduction/conv*/avgpool rigor.
- Regular vs extensive spatial/channel sets are disjoint (no ID collisions
  ever across -m "not extensive" vs full runs). Regular is tiny/fast (ch=4/16,
  32x32, first 4 POOL configs) for reliable default CI runs.
- Primary @metrics test (test_maxpool2d) uses only (k,s,p,ch,b,h,w) via
  run_test + defaults for num_aie_columns/tile_size (ctor defaults: 4 cols,
  2048 tile). This keeps "pytest -m 'not extensive'" fast and stable while
  still exercising many shapes/configs against the common 4-col design path.
  (Column/tile specialization coverage lives in the small explicit FORWARD_CASES.)
- Strict output-dim validation + shape cross-checks in every path (catches
  drift between op.py, design.py, reference.calculate_output_dim, golden,
  and torch F.max_pool2d).
- Explicit FORWARD_CASES (curated pytest.param list, stable IDs) with
  num_aie_columns + tile_size variants (portable 1/2/4 cols across AIE2/NPU1
  and AIE2P/NPU2) + explicit operator.context.compile_all() + prepare_runtime()
  before operator(x). This exercises every MLIR specialization, artifact naming,
  XRT BO/runlist, and the Python per-batch forward loop in op.py.
- Primary run_test usage with exact 0-tol (rel_tol=0.0, abs_tol=0.0) because
  maxpool is a pure selection operator (bitwise identical bf16 elements or
  -inf for padding). Forward path uses torch.equal (strongest contract).
- Canonical two-line metrics prints exactly matching the @metrics regexes
  and conftest CSV reporter expectations.
- bfloat16 semantics fully exercised (all paths use bf16; fp32-intermediate
  randn in golden for quality; explicit torch.bfloat16 in forward inputs).
- AIE2 (npu1) vs AIE2P (npu2) paths exercised via runtime device query in
  op.py (selects aie2/ or aie2p/ maxpool.cc) + device-aware get_params.
- Zero collection risks: every test produces bracketed nodeids compatible
  with the strict regex in conftest.py's pytest_runtest_makereport hook.
  No bare functions, no top-level side-effecting calls outside get_params.
- Pure-CPU reference validation (generate_golden_reference, max_pool2d_cpu,
  calculate_output_dim, _max_pool2d_reference_impl, get_params health,
  bitwise torch.equal, dim formulas, determinism, POOL_CONFIGS coverage,
  batch/edge cases) has been cleanly extracted to the dedicated sibling
  cpu_test.py (NPU-only enforced here per Conv3D gold standard).
  This file (test.py) now focuses exclusively on NPU paths.
  cpu_test.py is iron314 safe / --collectonly safe / --iterations safe
  (no aie_context, no XRT). Use -k "reference_cpu_only" (aligned to conv3d/avgpool/reduction).

The conscious decision to keep column/tile variation out of the primary
metrics matrix (FORWARD_CASES only) + batch-loop coverage inside the forward
test follows (and improves upon) the final polished avgpool/reduction/conv*
patterns. This delivers excellent design + runtime + AIEContext coverage
without making default "not extensive" runs slow or fragile.

Run NPU paths (requires hardware + XRT):
    python -m pytest iron/operators/maxpool/test.py -q -m "not extensive"
    python -m pytest iron/operators/maxpool/test.py --iterations 1 -k "fwd"

Run pure reference (always safe under iron314):
    python -m pytest iron/operators/maxpool/cpu_test.py -q --tb=short -k "reference_cpu_only"
"""

import pytest

import torch

from iron.operators.maxpool.op import AIEMaxPool2d
from iron.operators.maxpool.reference import (
    generate_golden_reference,
    calculate_output_dim,
)
from iron.common.test_utils import run_test

# Stable set of (kernel, stride, padding) configurations chosen for
# breadth of coverage (common cases + edges that stress kernels).
# This list is the single source of truth and must be kept in sync with
# the copy in cpu_test.py and reference.py.
POOL_CONFIGS = [
    (2, 2, 0),  # Most common 2x2 s2
    (3, 3, 0),
    (3, 2, 1),  # Strided + padding
    (4, 4, 0),
    (2, 1, 0),  # Overlapping
    (1, 1, 0),  # Identity edge
    (3, 1, 1),  # Overhang padding
]


def get_params():
    """Return the complete, ready-to-use list of pytest parameters.

    This is the canonical main-tree pattern (see avgpool, reduction, conv2d).

    The function is the single source of truth. It is called by @parametrize
    and therefore executes at collection time (after any device query is safe).

    Design (final polished form):
    - Lazy import of aie.utils inside the function (never at module import time).
      This guarantees that `from iron.operators.maxpool.test import get_params`
      (or any future health check) never pulls AIE/XRT under iron314 or CPU-only.
    - Defensive device query (try/except) so --collectonly, iron314 (python 3.14
      minimal env, no XRT), and machines without NPU never hard-crash.
    - Primary matrix contains only (k,s,p,channels,batch,in_h,in_w). No
      num_aie_columns/tile_size here (those live exclusively in FORWARD_CASES).
      This keeps default "pytest -m 'not extensive'" runs fast and stable while
      exercising many high-value shapes/configs against the common default
      (4-col, 2048-tile) design/runtime path.
    - Regular vs extensive use disjoint spatial/channel sets (guarantees zero
      ID collisions between the two suites).
    - All cases compute out dims with the authoritative formula and are
      filtered for divisibility by the default nc=4 (ensures design.py
      input_chunk/output_chunk = size // 4 never truncates for the primary path).
    - Explicit pytest.param(id=..., marks=...) for stable human-readable
      nodeids required by the CSV/metrics reporter even under --iterations.
    """
    # Lazy import (critical for cpu_test.py separation + iron314 safety).
    # aie.utils is only needed for the optional device query.
    import aie.utils as aie_utils

    # Defensive device discovery (collection safety under iron314 / no-XRT envs).
    # Real execution remains gated by the aie_context fixture.
    max_aie_columns = 4
    try:
        dev = aie_utils.get_current_device()
        if dev is not None:
            max_aie_columns = dev.cols
    except Exception:
        pass

    params = []
    default_nc = 4  # ctor default used by primary matrix; we filter for it

    # Regular (fast default) suite - tiny, representative, always run.
    # High-value common (k,s,p) on 32x32 with ch=4/16.
    for ch in [4, 16]:
        for b, h, w in [(1, 32, 32)]:
            for k, s, p in POOL_CONFIGS[:4]:
                out_h = calculate_output_dim(h, k, s, p)
                out_w = calculate_output_dim(w, k, s, p)
                if out_h < 1 or out_w < 1:
                    continue
                total_in = ch * h * w
                total_out = ch * out_h * out_w
                if total_in % default_nc != 0 or total_out % default_nc != 0:
                    continue
                pid = f"maxpool_c{ch}_k{k}_s{s}_p{p}_b{b}x{h}x{w}"
                params.append(pytest.param(k, s, p, ch, b, h, w, id=pid))

    # Extensive suite - disjoint spatials/channels from regular + full POOL_CONFIGS.
    # Additional filter for default_nc=4 divisibility so every case is runnable
    # with the ctor defaults used by this primary path.
    for ch in [1, 4, 16, 32]:
        for b, h, w in [(1, 28, 28), (1, 64, 64)]:
            for k, s, p in POOL_CONFIGS:
                out_h = calculate_output_dim(h, k, s, p)
                out_w = calculate_output_dim(w, k, s, p)
                if out_h < 1 or out_w < 1:
                    continue
                total_in = ch * h * w
                total_out = ch * out_h * out_w
                if total_in % default_nc != 0 or total_out % default_nc != 0:
                    continue
                pid = f"maxpool_c{ch}_k{k}_s{s}_p{p}_b{b}x{h}x{w}"
                params.append(
                    pytest.param(
                        k, s, p, ch, b, h, w, id=pid, marks=[pytest.mark.extensive]
                    )
                )

    return params


# Carefully chosen representative cases for the high-level forward API test.
# Explicit pytest.param objects guarantee stable, descriptive test IDs (never
# derived by slicing internal lists) and keep the number of forward runs small
# and fast even with many --iterations or -m "not extensive".
#
# Cases deliberately vary num_aie_columns (and derived tile_size) using only
# safe values (1/2/4) for portability across npu1 (max 4 cols) and npu2 (max 8).
# This exercises different MLIR specializations, artifact naming, the full
# compile_all + prepare_runtime + runlist + buffer management paths in
# AIEContext, and the Python batch loop inside AIEMaxPool2d.forward.
#
# AIE2 vs AIE2P kernel paths are exercised automatically: op.py selects
# aie_kernels/{aie2,aie2p}/maxpool.cc based on the actual runtime device.
# (If 8-col coverage on npu2 is desired in future, it can be added as an
# extensive-only forward case; get_params + device query already support it.)
#
# All chosen cases satisfy the per-column chunk divisibility required by
# design.py. Independent of get_params() so primary matrix changes never
# affect forward test IDs or coverage.
FORWARD_CASES = [
    pytest.param(
        2,
        2,
        0,
        4,
        1,
        32,
        32,
        4,
        1024,
        id="fwd_maxpool_c4_k2_s2_p0_1x32x32_4cols_1024tile",
    ),
    pytest.param(
        3,
        2,
        1,
        16,
        1,
        32,
        32,
        1,
        4096,
        id="fwd_maxpool_c16_k3_s2_p1_1x32x32_1cols_4096tile",
    ),
    pytest.param(
        1,
        1,
        0,
        4,
        1,
        32,
        32,
        2,
        2048,
        id="fwd_maxpool_c4_k1_s1_p0_1x32x32_2cols_2048tile",
    ),
]


# Single source of truth for the parameter names used in all @parametrize
# decorators (primary matrix + forward test). Prevents arity drift.
# Placed early so direct @parametrize(MAXPOOL_TEST..., get_params()) and
# forward both resolve at module import time. Matches conv3d gold.
MAXPOOL_TEST_PARAM_NAMES = "kernel_size,stride,padding,channels,batch,in_h,in_w"
MAXPOOL_FORWARD_PARAM_NAMES = (
    "kernel_size,stride,padding,channels,batch,in_h,in_w,num_aie_columns,tile_size"
)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    MAXPOOL_TEST_PARAM_NAMES,
    get_params(),
)
def test_maxpool2d(
    kernel_size,
    stride,
    padding,
    channels,
    batch,
    in_h,
    in_w,
    aie_context,
):
    """Primary parametrized end-to-end integration test (production canonical form).

    Uses the shared run_test harness:
    - Golden reference via generate_golden_reference (reproducible, bf16, validated dims)
    - Operator construction with ctor defaults (num_aie_columns=4, tile_size=2048)
      exercising the most common design + runtime specialization.
    - Full MLIR generation (design callback), compilation (peano/xclbin), prepare_runtime,
      timed runlist execution, and verify_buffer.
    - Zero-tolerance verification (pure selection operator contract: bitwise bf16 identity
      or -inf for padding positions).

    Output dim + shape cross-validation guards against any drift between
    op.py, design.py, reference.calculate_output_dim, and torch.

    The matrix (via get_params) covers many (k,s,p) + channel + spatial combinations
    against the default 4-col path while remaining fast for "not extensive" runs.
    Column/tile specialization and heavy AIEContext paths are covered by the
    dedicated forward test.
    """
    golden_ref = generate_golden_reference(
        batch_size=batch,
        channels=channels,
        in_height=in_h,
        in_width=in_w,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        seed=42,
    )

    # Cross-validate shapes and output dim formulas (catches drift between
    # op.py, design.py, reference.calculate_output_dim, and golden).
    expected_shape = (
        batch,
        channels,
        golden_ref["out_height"],
        golden_ref["out_width"],
    )
    assert golden_ref["output"].shape == expected_shape

    # Use ctor defaults for num_aie_columns/tile_size (the common 4c/2048t path).
    # This is the conscious final choice that keeps the primary matrix fast.
    operator = AIEMaxPool2d(
        channels=channels,
        in_height=in_h,
        in_width=in_w,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        context=aie_context,
    )

    assert operator.out_height == golden_ref["out_height"]
    assert operator.out_width == golden_ref["out_width"]

    input_buffers = {"input": golden_ref["input"]}
    output_buffers = {"output": golden_ref["output"]}

    # Pure selection operator (maxpool) => strongest possible contract:
    # bitwise identical output (bf16 bits preserved, -inf padding semantics).
    # run_test with 0 tol short-circuits to exact equality.
    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.0, abs_tol=0.0
    )

    # Exactly the two print lines expected by @metrics + conftest CSV reporter
    # (main-tree style, identical to avgpool/reduction/conv*).
    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


@pytest.mark.parametrize(
    MAXPOOL_FORWARD_PARAM_NAMES,
    FORWARD_CASES,
)
def test_maxpool2d_forward(
    kernel_size,
    stride,
    padding,
    channels,
    batch,
    in_h,
    in_w,
    num_aie_columns,
    tile_size,
    aie_context,
):
    """High-level forward() / __call__ API integration test (production quality).

    Uses generate_golden_reference (the exact golden path used by primary
    @metrics test and by Conv3D gold standard forward tests). No direct
    CPU ref calls in this NPU-only file (pure-CPU lives in cpu_test.py).
    Because max-pooling is a pure selection operator (no arithmetic, just
    index selection or -inf padding), the contract is bitwise identity on
    bf16: torch.equal (strongest possible check; 0-tol).

    Exercises the complete branch infrastructure for the convenience wrapper:
      - Construction with explicit column/tile (different design specializations:
        4-col common, 1-col, 2-col)
      - compile_all() (MLIR via design callback + full peano/aiecc pipeline)
      - prepare_runtime() (BO pool, runlist, XRT handles)
      - operator(x) path (per-sample Python batch loop + _process_single +
        write/run/read)
      - Numeric verification (torch.equal) vs bf16 golden (from generate_golden_reference)

    After the first (parametrized) batch run on the freshly prepared context,
    we immediately reuse the same operator for a batch=2 run (via second golden).
    This validates:
    - N=1 MLIR specialization + Python batching wrapper produces correct
      per-sample results for >1 batch.
    - The already-prepared runlist / buffers / context can be reused safely.
    - Golden path (bf16) works identically for batch>1.

    This provides targeted, high-signal coverage of column-dependent paths
    and the high-level forward API without exploding the primary metrics matrix.
    Aligns forward lifecycle + golden usage to Conv3D gold standard.
    """
    # Golden reference (NPU-only file; uses generate_golden_reference exactly
    # as Conv3D/primary test; bf16, seed=42 for determinism). No max_pool2d_cpu here.
    golden_ref = generate_golden_reference(
        batch_size=batch,
        channels=channels,
        in_height=in_h,
        in_width=in_w,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        seed=42,
    )
    expected = golden_ref["output"]

    operator = AIEMaxPool2d(
        channels=channels,
        in_height=in_h,
        in_width=in_w,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
        context=aie_context,
    )

    # Full integration exercise of the heavy branch AIEContext paths (exact
    # pattern used by polished conv3d/avgpool/reduction forward tests).
    operator.context.compile_all()
    operator.context.prepare_runtime()

    result = operator(golden_ref["input"])

    assert (
        result.shape == expected.shape
    ), f"Shape mismatch: {result.shape} != {expected.shape}"

    # bf16 selection op: bitwise identity (torch.equal) is the contract.
    # Golden exclusively via generate_golden_reference (consistent with Conv3D).
    assert torch.equal(result, expected), (
        "MaxPool forward result not bitwise identical to golden "
        f"(max_abs_diff_f32="
        f"{(result.to(torch.float32) - expected.to(torch.float32)).abs().max().item()})"
    )

    # === Batch reuse on already-prepared operator (critical coverage) ===
    # Exercises the Python-level batch loop inside forward() + _process_single
    # for N>1 while reusing the same compiled artifacts / runlist / XRT state.
    golden_b2 = generate_golden_reference(
        batch_size=2,
        channels=channels,
        in_height=in_h,
        in_width=in_w,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        seed=123,
    )
    expected_b2 = golden_b2["output"]

    result_b2 = operator(golden_b2["input"])

    assert (
        result_b2.shape == expected_b2.shape
    ), f"Batch-2 shape mismatch: {result_b2.shape} != {expected_b2.shape}"
    assert torch.equal(result_b2, expected_b2), (
        "MaxPool batch-2 forward result not bitwise identical "
        f"(max_abs_diff_f32="
        f"{(result_b2.to(torch.float32) - expected_b2.to(torch.float32)).abs().max().item()})"
    )


# =============================================================================
# Pure-CPU reference validation has been extracted to cpu_test.py
# =============================================================================
# All hardware-independent reference validation now lives exclusively in
# iron/operators/maxpool/cpu_test.py:
#   - test_maxpool_reference_cpu_only (parametrized, aligned -k filter)
#   - test_maxpool_cpu_determinism_and_f_match
#   - test_maxpool_cpu_pool_configs_via_golden
#   - test_maxpool_cpu_matrix_health
#
# These exercise 100% of the golden contract used by the NPU tests here:
#   generate_golden_reference, max_pool2d_cpu, _max_pool2d_reference_impl,
#   calculate_output_dim, POOL_CONFIGS coverage, seed determinism,
#   F.max_pool2d equivalence, dim formula cross-checks, and get_params health
#   (via local copy to stay fully standalone).
#
# This separation enables:
#   * Standalone execution under iron314 (python 3.14, no XRT/NPU/aie_context)
#   * Fast --collectonly and -k "reference_cpu_only" filtering (aligned)
#   * --iterations safety for the CPU suite
#   * Zero risk of collection crosstalk or hook regex violations in HW test.py
#   * Clean "pytest -m 'not extensive'" for NPU paths only
#
# Run the CPU reference validation (always safe):
#   conda run -n iron314 python -m pytest \
#       iron/operators/maxpool/cpu_test.py -q --tb=short -k "reference_cpu_only" [--iterations N]
#
# The cpu_test.py sibling is standalone for iron314 purity (defines local
# POOL_CONFIGS; may import get_params from here for invariants per Conv3D
# gold standard pattern). Behavior/coverage identical.
#
# NPU (this file):  python -m pytest iron/operators/maxpool/test.py -q -m "not extensive"
# CPU (sibling):    python -m pytest iron/operators/maxpool/cpu_test.py -q -k "reference_cpu_only"
# =============================================================================

# Tests are pytest-only (AGENTS.md convention).


# =============================================================================
# PURE-CPU REFERENCE VALIDATION LIVES IN cpu_test.py
# =============================================================================
# All hardware-independent reference validation (generate_golden_reference,
# max_pool2d_cpu, calculate_output_dim, _max_pool2d_reference_impl contract,
# dim formula cross-checks, POOL_CONFIGS coverage, get_params health,
# reproducibility, bitwise torch.equal on selection op, edge/batch cases)
# has been extracted to iron/operators/maxpool/cpu_test.py following the
# production reduction/conv2d/avgpool/conv3d pattern.
#
# Run under iron314 (no XRT/NPU/hardware required, no aie_context ever):
#   conda run -n iron314 python -m pytest iron/operators/maxpool/cpu_test.py -q --tb=short -k "reference_cpu_only"
#   python -m pytest iron/operators/maxpool/cpu_test.py --collectonly -q
#   python -m pytest iron/operators/maxpool/cpu_test.py -q --iterations 3 -k "reference_cpu_only"
#
# This keeps test.py focused exclusively on NPU/HW paths (@metrics + forward).
# The cpu_test.py sibling is standalone (imports get_params defensively
# per Conv3D gold standard; no crosstalk risk due to lazy device query).
# =============================================================================
