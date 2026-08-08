#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
NPU end-to-end tests for AIEConv2d.

Parametrized via get_params(); CPU-only reference tests live in cpu_test.py.
Regular (not extensive) cases cover small 1-col and 2-col smokes; larger
shapes and multi-col matrices use @pytest.mark.extensive.
"""

import pytest

import torch

from iron.operators.conv2d.op import AIEConv2d
from iron.operators.conv2d.reference import (
    generate_golden_reference,
    calculate_output_dim,
)
from iron.common import AIEOperatorConstraintError
from iron.common.test_utils import run_test


def get_params():
    """Generate all test parameters for conv2d (single source of truth).

    Canonical main-tree / polished operator style (maxpool/avgpool/conv3d/reduction):
    - Queries actual device column count at collection time (NPU1=4, NPU2=8).
      Defensive try/except so --collectonly and pure-CPU reference environments
      do not hard-crash (mirrors reduction test.py rigor).
    - Varies num_aie_columns + derives matching tile_size (subject to divisibility
      on in/weight/out sizes required by column-parallel chunking + TAPs + FIFO
      element sizes in design.py).
    - Uses explicit pytest.param(..., id=pretty_name, marks=...) so that
      the branch CSV/metrics reporter gets stable human-readable test names.
    - Marks the majority as extensive; only a small core subset (16x16/32x32
      CORE @ 1c plus 16x16 CORE @ 2c multi-col) run by default ("not extensive").

    The divisibility filter (in+weight+out) prevents silent truncation/mismatch
    in (size // num_columns) logic and ensures generated MLIR is valid for the
    chosen parallelism.

    CRITICAL FOR GOLDEN FIDELITY: Output dim computation now uses the shared
    calculate_output_dim from reference.py (single source of truth, matches
    the formula used inside generate_golden_reference and AIEConv2d). This
    eliminates duplication risk with op.py / design.py for padding/stride math.

    Results are consumed via direct get_params() + CONV2D_TEST_PARAM_NAMES (prevents drift).
    """
    import aie.utils as aie_utils

    # Defensive device discovery (pure-CPU reference tests + collectonly safety)
    max_cols = 4
    try:
        dev = aie_utils.get_current_device()
        max_cols = dev.cols
    except Exception:
        pass

    # Core configurations (in_ch, out_ch, k, s, p, g, use_bias)
    # Extended set for good coverage of variants (exercises all golden paths,
    # column chunking, bias ObjectFifo singular broadcast, variant kernels,
    # conditional rt.sequence, and prepare_runtime runlist arity).
    configs = [
        (3, 16, 3, 1, 1, 1, True),  # basic +bias
        (3, 16, 3, 1, 1, 1, False),  # basic nobias
        (16, 16, 3, 1, 1, 1, True),
        (16, 16, 3, 1, 1, 16, True),  # depthwise +bias
        (16, 16, 3, 1, 1, 16, False),  # depthwise nobias
        (32, 64, 1, 1, 0, 1, True),  # pointwise
        (32, 64, 1, 1, 0, 1, False),
        (16, 32, 3, 2, 1, 1, True),  # strided +pad
        (16, 32, 3, 2, 0, 1, True),  # strided no pad
        (8, 16, 3, 1, 2, 2, True),  # groups=2
        (4, 8, 3, 1, 1, 2, True),
    ]

    # Explicit core configs for regular marking (robust vs list order / slicing).
    # Regular CI coverage:
    #   - 3→16 bias/nobias: baseline host-bias + full/near-full L1
    #   - 16→16 groups=1 bias: multi-tile OC path at 32x32 (oc_tile=8)
    #   - 16 depthwise bias: multi-tile channel path at 32x32 (c_tile=8)
    # Also 16x16 CORE @ 2c (OC/channel split, ≤2 DMA, host bias).
    CORE_CONFIGS = [
        (3, 16, 3, 1, 1, 1, True),
        (3, 16, 3, 1, 1, 1, False),
        (16, 16, 3, 1, 1, 1, True),  # standard multi-tile OC
        (16, 16, 3, 1, 1, 16, True),  # depthwise multi-tile channels
    ]

    # 16x16 + 32x32 CORE @ 1c: L1 fit. 16x16 CORE @ 2c: multi-col smoke.
    # 32x32+ multi-col and 64 spatial stay extensive until proven green.
    spatials = [(16, 16), (32, 32), (64, 64)]
    col_candidates = [1, 2, 4, 8]

    params = []
    for h, w in spatials:
        for cfg in configs:
            in_ch, out_ch, k, s, p, g, use_bias = cfg
            for nc in col_candidates:
                if nc > max_cols:
                    continue

                # Dilation is fixed to 1 in current AIEConv2d (asserted in op.py).
                # Use the *shared* calculate_output_dim from reference (exact match
                # to generate_golden_reference + operator + design for d=1).
                # This guarantees the out_h/out_w used for divisibility + naming
                # are identical to those in the golden "output" tensor shape.
                dilation = 1
                out_h = calculate_output_dim(h, k, s, p, dilation)
                out_w = calculate_output_dim(w, k, s, p, dilation)

                # Sizes that must be evenly divisible for column chunking on
                # *flattened* elements (critical: design.py chunks C*H*W, weight,
                # and output by num_aie_columns for parallel columns).
                in_size = in_ch * h * w  # N=1 (MLIR specialization)
                w_size = out_ch * (in_ch // g) * k * k
                out_size = out_ch * out_h * out_w

                if (
                    nc == 0
                    or in_size % nc != 0
                    or w_size % nc != 0
                    or out_size % nc != 0
                ):
                    continue

                tile_size = in_size // nc

                # Regular subset ("not extensive"):
                #   - 16x16 / 32x32 CORE @ 1c — L1 OC/channel tiles
                #   - 16x16 CORE @ 2c — multi-col OC/channel split smoke
                # Bias remains host-side (2 input DMA limit per compute tile).
                # Larger multi-col (4c/8c, 32x32+) stays extensive.
                is_core_config = cfg in CORE_CONFIGS
                is_regular = is_core_config and (
                    (nc == 1 and (h, w) in ((16, 16), (32, 32)))
                    or (nc == 2 and (h, w) == (16, 16))
                )

                marks = [] if is_regular else [pytest.mark.extensive]

                bias_str = "bias" if use_bias else "nobias"
                name = f"conv2d_{in_ch}x{out_ch}_k{k}_s{s}_p{p}_g{g}_{bias_str}_{h}x{w}_{nc}c_{tile_size}t"

                # Note: batch always 1 for the low-level run_test path (N=1 MLIR specialization)
                params.append(
                    pytest.param(
                        in_ch,
                        out_ch,
                        k,
                        s,
                        p,
                        g,
                        use_bias,
                        1,
                        h,
                        w,
                        nc,
                        tile_size,
                        id=name,
                        marks=marks,
                    )
                )

    return params


# get_params() (single source of truth) is invoked *directly* inside @parametrize
# (Conv3D gold "direct only" style; no top-level all_params = get_params()).
# Called at collection time; safe due to defensive device query inside.


# Explicit constant for the parameter names used in @parametrize decorators.
# This is the production hardening (see conv3d) against "N names vs M values"
# collection crashes when get_params or FORWARD_CASES evolve. The order and
# count (12) must exactly match the 12-tuples yielded by get_params() and the
# pytest.param values in FORWARD_CASES.
CONV2D_TEST_PARAM_NAMES = (
    "in_channels,out_channels,kernel_size,stride,padding,groups,"
    "use_bias,batch,in_h,in_w,num_aie_columns,tile_size"
)


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    CONV2D_TEST_PARAM_NAMES,
    get_params(),
)
def test_conv2d(
    in_channels,
    out_channels,
    kernel_size,
    stride,
    padding,
    groups,
    use_bias,
    batch,
    in_h,
    in_w,
    num_aie_columns,
    tile_size,
    aie_context,
):
    """Primary metrics-enabled end-to-end test (production canonical shape).

    Exercises the complete AIE compilation + runtime path via run_test:
    - AIEConv2d construction (explicit nc/tile for column chunking coverage)
    - run_test (which performs operator.compile() + get_callable internally)
    - Buffer registration/IO, timed runlist execution on NPU (AIE2 or AIE2P)
    - nearly_equal verification with documented bf16 tolerances
    - Emission of the exact two metric print lines for CSV/hooks

    Full matrix (varying nc/tile + bias + groups + stride etc) exercises
    all design.py specializations and conditional runtime paths.
    """
    # tile_size now supplied by the test parameter (computed in get_params for
    # the chosen num_aie_columns, guaranteeing the divisibility asserted in design).

    # Generate golden reference (exercises use_bias=True/False paths).
    # Explicit seed for full determinism (matches polished peers).
    golden_ref = generate_golden_reference(
        batch_size=batch,
        in_channels=in_channels,
        in_height=in_h,
        in_width=in_w,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        seed=42,
    )

    # Create operator with explicit column/tile (device-aware).
    # Configs whose min L1 triple (in+weight+out bf16) exceeds the
    # design budget raise AIEOperatorConstraintError at construct time instead
    # of a late aiecc "allocated buffers exceeded" OOM. Skip those as
    # Rejected at construct time when no H-strip plan fits L1.
    try:
        operator = AIEConv2d(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            groups=groups,
            use_bias=use_bias,
            in_height=in_h,
            in_width=in_w,
            num_aie_columns=num_aie_columns,
            tile_size=tile_size,
            context=aie_context,
        )
    except AIEOperatorConstraintError as e:
        pytest.skip(f"Unsupported AIEConv2d config (L1/column constraint): {e}")

    # Cross-validate output dimension math (catches formula drift)
    ref_out_shape = golden_ref["output"].shape
    assert ref_out_shape[0] == batch
    assert ref_out_shape[1] == out_channels
    assert (
        operator.out_height == ref_out_shape[2]
    ), f"out_height mismatch: operator={operator.out_height}, ref={ref_out_shape[2]}"
    assert (
        operator.out_width == ref_out_shape[3]
    ), f"out_width mismatch: operator={operator.out_width}, ref={ref_out_shape[3]}"

    # Prepare buffers (bias only when use_bias)
    input_buffers = {
        "input": golden_ref["input"],
        "weight": golden_ref["weight"],
    }
    if use_bias and golden_ref["bias"] is not None:
        input_buffers["bias"] = golden_ref["bias"]

    output_buffers = {"output": golden_ref["output"]}

    # bf16 Conv2D numerical sensitivity (measured on AIE2P NPU after DMA-safe
    # 1-col path): full-tensor vector kernels accumulate in a different order
    # than torch F.conv2d(bf16). Observed ~2-5% relative drift on large values
    # and absolute O(0.1-0.5) errors on near-zero outputs (sign flips possible).
    # bf16 NPU MAC order can differ from torch; use looser tols than pure CPU.
    # 0.1 rel + 1.0 abs catches catastrophic bugs while accepting AIE bf16 MAC
    # noise. Golden remains conv2d_cpu (F.conv2d) for identical semantics.
    errors, latency_us, bandwidth_gbps = run_test(
        operator,
        input_buffers,
        output_buffers,
        rel_tol=0.1,
        abs_tol=1.0,
        # Allow a small fraction of near-zero outliers (bf16 sign flips).
        max_error_rate=0.02,
    )

    # Exactly the two lines required by the @metrics regexes (main-tree style,
    # identical to maxpool/avgpool/conv3d/reduction). Extra debug prints removed
    # for robust CSV/metrics reporter capture and pre-push hook compatibility.
    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


# Carefully chosen representative cases for the high-level forward API test.
# Explicit pytest.param objects (maxpool/conv3d/avgpool/reduction pattern) guarantee:
# - Stable, descriptive test IDs for CSV/metrics and reports
# - No dependency on ordering/count of get_params() results (uses independent FORWARD_CASES)
# - No fragile slicing or mark introspection
# - Targeted coverage of column/tile variants (different MLIR specializations)
# - Bias on/off + key kernel variants (standard/depthwise/pointwise/strided)
#
# These deliberately stay small/fast even under --iterations while still
# exercising operator.compile() + forward()/__call__ (get_callable + XRTTensor)
# and the python-level batching over N=1-specialized MLIR.
FORWARD_CASES = [
    # 16x16 + 1-col keeps full tensors inside L1 (~64KB) with depth=1.
    # tile_size = in_ch * H * W for nc=1.
    pytest.param(
        3,
        16,
        3,
        1,
        1,
        1,
        True,
        1,
        16,
        16,
        1,
        768,
        id="conv2d_forward_basic_bias_16x16_1c",
    ),
    pytest.param(
        3,
        16,
        3,
        1,
        1,
        1,
        False,
        1,
        16,
        16,
        1,
        768,
        id="conv2d_forward_basic_nobias_16x16_1c",
    ),
    pytest.param(
        16,
        16,
        3,
        1,
        1,
        16,
        True,
        1,
        16,
        16,
        1,
        4096,
        id="conv2d_forward_depthwise_16x16_1c",
    ),
    pytest.param(
        8,
        16,
        1,
        1,
        0,
        1,
        True,
        1,
        16,
        16,
        1,
        2048,
        id="conv2d_forward_pointwise_16x16_1c",
    ),
    pytest.param(
        3,
        16,
        3,
        2,
        1,
        1,
        True,
        1,
        16,
        16,
        1,
        768,
        id="conv2d_forward_strided_16x16_1c",
    ),
]


@pytest.mark.extensive
@pytest.mark.parametrize(
    CONV2D_TEST_PARAM_NAMES,
    FORWARD_CASES,
)
def test_conv2d_forward(
    in_channels,
    out_channels,
    kernel_size,
    stride,
    padding,
    groups,
    use_bias,
    batch,
    in_h,
    in_w,
    num_aie_columns,
    tile_size,
    aie_context,
):
    """Forward / __call__ API integration test (production quality).

    Explicitly drives the modern MLIROperator lifecycle:
      - Construction with explicit nc/tile (different MLIR specializations)
      - operator.compile() (design callback + peano/xclbin toolchain)
      - operator(input, weight, bias) → forward (XRTTensor + get_callable;
        host bias; per-batch Python loop over N=1 MLIR)
      - Reuse of compiled operator for batch=2 (validates batching wrapper)

    Golden data (including for batch=2) is generated exclusively via
    generate_golden_reference / conv2d_cpu (identical contract to metrics path).
    Independent FORWARD_CASES (stable IDs) guarantee coverage of column variants
    without coupling to the main matrix. Complements run_test path.
    Uses bf16 tolerances aligned with metrics (0.1/1.0) for forward + batch loop.
    """
    golden_ref = generate_golden_reference(
        batch_size=batch,
        in_channels=in_channels,
        in_height=in_h,
        in_width=in_w,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        seed=42,
    )

    try:
        operator = AIEConv2d(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            groups=groups,
            use_bias=use_bias,
            in_height=in_h,
            in_width=in_w,
            num_aie_columns=num_aie_columns,
            tile_size=tile_size,
            context=aie_context,
        )
    except AIEOperatorConstraintError as e:
        pytest.skip(f"Unsupported AIEConv2d config (L1/column constraint): {e}")

    # Modern MLIROperator path (AIEContext no longer exposes compile_all /
    # prepare_runtime). Matches maxpool/avgpool forward tests.
    operator.compile()

    # N=1 forward via __call__ / forward (XRTTensor + get_callable + host bias)
    result = operator(
        golden_ref["input"],
        golden_ref["weight"],
        golden_ref["bias"],
    )
    expected = golden_ref["output"]

    assert (
        result.shape == expected.shape
    ), f"Shape mismatch: got {result.shape}, expected {expected.shape}"

    # Forward-path bf16 tolerances (aligned with metrics path; host bias add
    # is exact on top of NPU nobias result).
    rel_tol = 0.1
    abs_tol = 1.0
    if not torch.allclose(result, expected, rtol=rel_tol, atol=abs_tol):
        max_diff = (result - expected).abs().max().item()
        pytest.fail(f"Results don't match. Max diff: {max_diff}")

    # Batch=2 reuse of already-prepared operator/runlist
    # This validates:
    # - N=1 MLIR specialization + Python batching wrapper produces correct
    #   per-sample results matching the full-batch golden from generate_...
    # - Golden generation with batch_size=2 works identically (F.conv2d handles N).
    golden_b2 = generate_golden_reference(
        batch_size=2,
        in_channels=in_channels,
        in_height=in_h,
        in_width=in_w,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        seed=42,
    )
    result_b2 = operator(
        golden_b2["input"],
        golden_b2["weight"],
        golden_b2["bias"],
    )
    expected_b2 = golden_b2["output"]
    assert (
        result_b2.shape == expected_b2.shape
    ), f"Batch-2 shape mismatch: got {result_b2.shape}, expected {expected_b2.shape}"
    if not torch.allclose(result_b2, expected_b2, rtol=rel_tol, atol=abs_tol):
        max_diff = (result_b2 - expected_b2).abs().max().item()
        pytest.fail(f"Batch-2 results don't match. Max diff: {max_diff}")


# =============================================================================
# PURE-CPU REFERENCE VALIDATION LIVES IN cpu_test.py
# =============================================================================
# All hardware-independent reference validation (generate_golden_reference,
# conv2d_cpu contract, calculate_output_dim cross-checks, get_params health,
# reproducibility, bf16 sanity) has been extracted to iron/operators/conv2d/cpu_test.py
# following the production reduction/cpu_test.py (and avgpool/maxpool/conv3d) pattern.
#
# Run under iron314 (no XRT/NPU required, full --collectonly / --iterations safe):
#   conda run -n iron314 python -m pytest iron/operators/conv2d/cpu_test.py -q --tb=short
#   conda run -n iron314 python -m pytest iron/operators/conv2d/cpu_test.py -q --iterations 3 -k "reference_cpu_only"
#
# This keeps test.py focused exclusively on NPU paths (@metrics + forward + design matrix).
# The cpu_test.py sibling imports get_params from here (defensive, collection-safe).
# =============================================================================

# Tests are pytest-only (AGENTS.md convention).
# CPU reference: python -m pytest iron/operators/conv2d/cpu_test.py
# HW (NPU) tests:  python -m pytest iron/operators/conv2d/test.py -q -m "not extensive"
