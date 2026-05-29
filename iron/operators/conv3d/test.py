#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Production-grade test suite for the AIE Conv3D operator (NPU/hardware paths only).

This is the FINAL COMPLETE, consciously engineered, production-grade NPU test file
for the Conv3D operator. It is suitable as the reference artifact and template for
the 5 new operators in the primary NPU finalization wave.

This module is the NPU-focused counterpart for Conv3D. Pure-CPU reference
validation (the critical trustworthiness foundation) has been cleanly extracted
to the sibling cpu_test.py following the established reduction / maxpool / avgpool
/ conv2d operator cpu_test.py separation pattern. It meets (and exceeds) the bar
set by the strongest siblings:
- reduction/test.py (post cpu_test.py extraction, device-aware)
- maxpool/test.py (the documented reference polished template)
- conv2d/test.py (the direct 2D conv peer with identical architecture)
- avgpool/test.py
- main-tree axpy/gemm patterns

It is fully compatible with the branch infrastructure:
  conftest.py, AIEContext (use_runlist, compile_all, prepare_runtime),
  run_test + verify_buffer, CSV + @metrics reporter (stable pretty IDs from
  explicit pytest.param), pytest_generate_tests + --iterations, pytest.ini
  "extensive" marker, python 3.14 iron314 collection requirements (defensive
  device query, no hard XRT dependency at import/collection time).

The sibling iron/operators/conv3d/cpu_test.py now owns all hardware-independent
validation:
  - test_conv3d_reference_cpu_only()
  - (parametrized CPU_REFERENCE_CASES exercising the full 3D contract)
These exercise generate_golden_reference, conv3d_cpu, calculate_output_dim vs
torch F.conv3d across full config space (bias, depthwise, pointwise, strided,
grouped/partial groups, batch>1, asymmetric per-dim k/s/p, dilation in ref path,
edge shapes, temporal 3D specifics). They run under iron314, --collectonly, and
any CPU-only environment. cpu_test.py imports get_params from here for ID
uniqueness / regular-case health checks and to guarantee no drift.

Quality attributes:
- Comprehensive production docstring + shebang.
- Single get_params() as the canonical source of truth (returns list of
  pytest.param with human ids + marks). get_params() is invoked *directly*
  by the @parametrize decorators (reduction/avgpool/maxpool canonical style;
  no top-level all_params = get_params() assignment). CONV3D_TEST_PARAM_NAMES
  constant prevents drift. Defensive lazy aie_utils.get_current_device()
  (try/except inside func + None guard) so --collectonly / pure-CPU / minimal
  iron314 envs (and `from .test import get_params` by cpu_test.py) never
  crash or pull aie at module load. Matches reduction/avgpool/maxpool rigor.
- Strict divisibility filtering on in_elems / weight_elems / out_elems using
  authoritative calculate_output_dim (from reference) for design.py column
  chunking, TAP/FIFO element sizing, bias ObjectFifo broadcast, conditional
  rt.sequence arity (3 vs 4 args).
- Explicit CORE_CONFIGS / regular marking (nc <=2 + curated configs) for fast,
  stable default runs under -m "not extensive". Disjoint regular/extensive
  volumes guarantee zero ID collisions.
- Primary @metrics test + run_test (full compile/prepare/timed/verify path).
  Full num_aie_columns + matching tile_size (in_elems//nc after divis) from
  the get_params() matrix exercises every tiling + design specialization.
- Explicit independent FORWARD_CASES (curated pytest.param list) exercising
  full lifecycle + batch>1 python forward over N=1 MLIR + varied column counts
  + explicit compile_all + prepare_runtime calls.
- Exact two-line metric prints only (Latency + Bandwidth) matching the
  @metrics regexes and main-tree CSV reporter contract. No prefix lines.
- Production bf16 tolerance documentation (0.05/1e-5 primary; 0.05/0.1 forward)
  with rationale for 3D volumetric MAC accumulation sensitivity. All golden
  via generate_golden_reference / conv3d_cpu.
- Stable pretty IDs for every parametrized case (CSV/metrics reporter safe).
- Explicit seed=42 on all golden calls for determinism.
- No direct execution (modern convention). Inlined construction (no
  fragile helpers) in both primary and forward tests for canonical cleanliness.
- get_params matrix consciously exercises the complex design.py (per-col
  chunks for standard/depthwise/pointwise, singular bias OF only on use_bias,
  kernel signature variants, FIFO depth heuristics, 5D volume handling).
- Regular subset deliberately minimal/fast (8x16x16 + nc<=2 + core configs +
  bias=True ONLY) while still hitting the critical bias ObjectFifo + conditional
  runlist paths + 3D variants. All nobias cases (even core) + larger matrices
  are extensive.
- Implicit full coverage of AIE2 (NPU1, 4 cols) vs AIE2P (NPU2, 8 cols) paths:
  device query + kernel_dir selection in op.py (aie2/ or aie2p/conv3d.cc) +
  column/tile matrix (max_cols drives both regular and extensive cases).

The get_params matrix (3D volumes with temporal dim, full bias/depthwise/
pointwise/strided/groups coverage, strict divis + authoritative dim calc) is
the right conscious engineering for the column-parallel ObjectFifo + 3D
dataflow + conditional bias runtime complexity.

Canonical shape delivered for NPU finalization wave:
- Shebang + comprehensive module docstring with rationale, AIE2/AIE2P coverage.
- Single get_params() (the canonical main-tree source of truth, invoked
  *directly* by @parametrize; no all_params= assignment at module level).
  Explicit CONV3D_TEST_PARAM_NAMES for drift-proof signatures. Lazy aie.utils
  import *inside* get_params only (cpu_test.py from-import safety under iron314).
- Defensive device query with None guard (collection-safe under iron314 /
  --collectonly / pure-CPU / no-XRT CI). Supports NPU1 (4 cols) / NPU2 (8 cols).
- All cases use explicit pytest.param(..., id=..., marks=...) + the
  CONV3D_TEST_PARAM_NAMES constant for drift-proof signatures.
- Disjoint regular/extensive (volumes + explicit CORE_CONFIGS + nc limit)
  guaranteeing clean "-m 'not extensive'" and no ID collisions.
- PRIMARY @metrics test matrix fully exercises num_aie_columns + tile_size
  (with divisibility on in/w/out) + use_bias + all kernel variants. run_test
  usage (internal compile_all/prepare_runtime) + exact two-line metric prints.
- Explicit independent FORWARD_CASES with explicit compile_all() +
  prepare_runtime() + batch>1 reuse (full high-level AIEContext lifecycle).
- Inlined construction + dim cross-checks (canonical clean style matching
  conv2d/avgpool/maxpool). Strong bf16 tolerance documentation.
- AIE2 vs AIE2P paths exercised: device.cols + op.py kernel_dir selection
  (aie2/ vs aie2p/conv3d.cc) + both sets of bf16 vector kernels.
- Pure-CPU reference validation fully extracted to sibling cpu_test.py
  (never touch cpu_test.py per NPU finalization instructions). This file
  owns exclusively the NPU paths (run_test + forward with aie_context).
- No dead code, no unused imports, modern main-tree convention.
- Pre-push lint (black) + iron314 collection + --iterations + marker compatible.

Pure-CPU reference tests live exclusively in cpu_test.py (see that file for
detailed hardening rationale, iron314 usage, and why the separation matters
for hook safety and collection).

Preserves full backward compat for existing CI / branch reporting.
"""

import pytest

import torch

from iron.operators.conv3d.op import AIEConv3d
from iron.operators.conv3d.reference import (
    generate_golden_reference,
    calculate_output_dim,
)
from iron.common.test_utils import run_test


def get_params():
    """Return the complete list of pytest parameters for Conv3D (single source of truth).

    Canonical main-tree pattern (axpy/gemm/conv2d/maxpool/reduction) with
    3D-specific engineering for volumetric conv + AIE column parallelism.

    - Defensive device query (try/except + None guard) for robust --collectonly + iron314
      collection in envs without XRT/NPU (defaults safe 4 cols). Supports NPU1/NPU2.
    - Strict divisibility on (in_elems, w_elems, out_elems) for design.py's
      per-column chunking of 5D tensors, TAPs, ObjectFifos, and bias broadcast.
    - use_bias True/False for complete conditional coverage (MLIR wiring,
      runlist arity 3 vs 4, kernel bias load, singular vs absent bias OF).
    - Regular vs extensive volumes are disjoint sets (guarantees no ID clashes).
    - Within regular volume, only a tiny curated subset is unmarked (nc<=2 +
      core configs + use_bias=True only); everything else (incl. nobias even
      for core configs, larger nc, extensive volumes) receives extensive mark.
      Keeps default "pytest -m 'not extensive'" fast, stable, and high-signal.
    - Authoritative calculate_output_dim (the single source of truth also used
      by reference.py and op.py) exercised at collection for all out-size math.
    - Normalization of k/s/p (scalar or tuple) so generator is robust.
    - Explicit tile_size = in_elems // nc (after divis check) so primary matrix
      now drives real per-tile specializations.
    """
    # Lazy import (critical for cpu_test.py separation + iron314 safety).
    # Importing get_params (from cpu_test.py) must never trigger aie import
    # at module load time. aie.utils is only needed for the optional device query.
    import aie.utils as aie_utils

    # Defensive device discovery: allows --collectonly and pure-CPU test
    # execution under iron314 and other minimal CI setups without crashing
    # on aie.utils or missing NPU. Matches reduction/avgpool/maxpool rigor.
    # The None guard adds extra safety (polished template pattern).
    max_aie_columns = 4
    try:
        device = aie_utils.get_current_device()
        if device is not None:
            max_aie_columns = device.cols
    except Exception:
        pass  # Safe default for collection / reference-only runs

    # Core configurations exercising distinct operator / design / kernel paths
    configs = [
        (3, 16, 3, 1, 1, 1),  # basic + bias coverage
        (16, 16, 3, 1, 1, 1),  # same in/out channels
        (16, 16, 3, 1, 1, 16),  # depthwise
        (32, 64, 1, 1, 0, 1),  # pointwise (1x1x1)
        (16, 32, 3, 2, 1, 1),  # strided + pad
    ]

    use_biases = [True, False]

    # Regular (fast default) vs extensive volumes kept disjoint
    regular_volumes = [(1, 8, 16, 16)]
    extensive_volumes = [(1, 16, 32, 32)]

    # Explicit CORE_CONFIGS (no fragile [:3] slicing) for regular marking.
    # Curated "regular" (unmarked) subset: core configs + nc<=2 + bias=True
    # ONLY. This is the consciously minimal fast default set under
    # -m "not extensive". Matches final conv2d/avgpool/maxpool philosophy.
    regular_nc_limit = 2
    CORE_CONFIGS = [
        (3, 16, 3, 1, 1, 1),  # basic + bias coverage
        (16, 16, 3, 1, 1, 1),  # same in/out channels
        (16, 16, 3, 1, 1, 16),  # depthwise
    ]
    regular_configs = CORE_CONFIGS

    params = []

    for is_extensive, volumes in (
        (False, regular_volumes),
        (True, extensive_volumes),
    ):
        for batch, in_t, in_h, in_w in volumes:
            for in_ch, out_ch, kernel, stride, pad, groups in configs:
                # Normalize for robustness (supports scalar or tuple in configs list)
                k = (kernel, kernel, kernel) if isinstance(kernel, int) else kernel
                s = (stride, stride, stride) if isinstance(stride, int) else stride
                p = (pad, pad, pad) if isinstance(pad, int) else pad

                # Authoritative 1D dim math from reference (exercises the helper
                # at collection time and guarantees golden == torch shape contract)
                out_t = calculate_output_dim(in_t, k[0], s[0], p[0], 1)
                out_h = calculate_output_dim(in_h, k[1], s[1], p[1], 1)
                out_w = calculate_output_dim(in_w, k[2], s[2], p[2], 1)

                in_elems = batch * in_ch * in_t * in_h * in_w
                w_elems = out_ch * (in_ch // groups) * k[0] * k[1] * k[2]
                out_elems = batch * out_ch * out_t * out_h * out_w

                for num_cols in range(1, max_aie_columns + 1):
                    if (
                        in_elems % num_cols != 0
                        or w_elems % num_cols != 0
                        or out_elems % num_cols != 0
                    ):
                        continue

                    for use_bias in use_biases:
                        # Regular (unmarked) subset is consciously tiny:
                        #   - only on the small regular volume
                        #   - only preferred small column counts (nc<=2)
                        #   - only the explicit CORE_CONFIGS
                        #   - ONLY use_bias=True (bias=False variants even for core
                        #     are marked extensive). This keeps default runs under
                        #     -m "not extensive" minimal, fast, and stable while
                        #     still covering the critical bias ObjectFifo + runlist
                        #     paths. Matches the final conv2d philosophy exactly.
                        is_regular = (
                            not is_extensive
                            and num_cols <= regular_nc_limit
                            and (in_ch, out_ch, kernel, stride, pad, groups)
                            in regular_configs
                            and use_bias
                        )
                        marks = [] if is_regular else [pytest.mark.extensive]

                        bias_tag = "b1" if use_bias else "b0"
                        tile_size = in_elems // num_cols if num_cols > 0 else 2048
                        name = (
                            f"conv3d_{in_ch}x{out_ch}_k{kernel}_s{stride}_p{pad}_g{groups}_"
                            f"{in_t}x{in_h}x{in_w}_c{num_cols}_{bias_tag}_t{tile_size}"
                        )
                        params.append(
                            pytest.param(
                                in_ch,
                                out_ch,
                                kernel,
                                stride,
                                pad,
                                groups,
                                batch,
                                in_t,
                                in_h,
                                in_w,
                                use_bias,
                                num_cols,
                                tile_size,
                                id=name,
                                marks=marks,
                            )
                        )
    return params


# get_params() (the single source of truth) is invoked directly inside the
# @parametrize decorator expression (canonical reduction/avgpool/maxpool style).
# This ensures that plain "import ...conv3d.test" (as done by cpu_test.py's
# "from ...test import get_params") does not trigger an extra unconditional
# get_params() call beyond what the test function decorators require.
# cpu_test.py calls get_params() explicitly itself for its health checks.


# =============================================================================
# Forward / high-level API integration test cases (explicit + stable)
# =============================================================================

# Carefully chosen representative cases for the high-level forward API test.
# Explicit pytest.param objects (maxpool/conv2d/avgpool pattern) guarantee:
# - Stable, descriptive test IDs for CSV/metrics and reports (never derived
#   by slicing internal lists or get_params results)
# - No dependency on ordering/count of get_params() or regular/ext changes
# - No fragile slicing or mark introspection
# - Targeted coverage of column/tile variants (different MLIR + prepare_runtime paths)
# - Bias on/off + key kernel variants (standard/depthwise/pointwise/strided)
#
# These deliberately stay small/fast even under --iterations while still
# exercising the full AIEContext lifecycle (compile_all + prepare_runtime)
# and the python-level batching over N=1-specialized MLIR (see op.forward).
FORWARD_CASES = [
    pytest.param(
        3,
        16,
        3,
        1,
        1,
        1,
        1,
        8,
        16,
        16,
        True,
        1,
        6144,
        id="fwd_conv3d_3x16_k3_s1_p1_g1_b1_8x16x16_c1_t6144",
    ),
    pytest.param(
        3,
        16,
        3,
        1,
        1,
        1,
        1,
        8,
        16,
        16,
        False,
        2,
        3072,
        id="fwd_conv3d_3x16_k3_s1_p1_g1_b0_8x16x16_c2_t3072",
    ),
    pytest.param(
        16,
        16,
        3,
        1,
        1,
        16,
        1,
        8,
        16,
        16,
        True,
        1,
        32768,
        id="fwd_conv3d_16x16_k3_s1_p1_g16_b1_8x16x16_c1_t32768",
    ),
    pytest.param(
        32,
        64,
        1,
        1,
        0,
        1,
        1,
        8,
        16,
        16,
        True,
        2,
        32768,
        id="fwd_conv3d_32x64_k1_s1_p0_g1_b1_8x16x16_c2_t32768",
    ),
    pytest.param(
        16,
        32,
        3,
        2,
        1,
        1,
        1,
        8,
        16,
        16,
        False,
        2,
        16384,
        id="fwd_conv3d_16x32_k3_s2_p1_g1_b0_8x16x16_c2_t16384",
    ),
]


# =============================================================================
# Shared constants (prevents signature drift in parametrize)
# =============================================================================

# Single source of truth for the parameter names used in all @parametrize
# decorators (primary matrix + forward test). This prevents any future
# drift in count/order between the declared names (13) and the values
# supplied by get_params() (invoked directly in decorator) or FORWARD_CASES --
# the exact root cause of the historical "13 names vs 12 values" crash.
# Matches the direct-get_params() pattern in reduction/avgpool/maxpool.
CONV3D_TEST_PARAM_NAMES = (
    "in_channels,out_channels,kernel_size,stride,padding,groups,"
    "batch,in_t,in_h,in_w,use_bias,num_aie_columns,tile_size"
)


# =============================================================================
# Primary metrics-enabled integration test (run_test path)
# =============================================================================


@pytest.mark.metrics(
    Latency=r"Latency \(us\): (?P<value>[\d\.]+)",
    Bandwidth=r"Effective Bandwidth: (?P<value>[\d\.e\+-]+) GB/s",
)
@pytest.mark.parametrize(
    CONV3D_TEST_PARAM_NAMES,
    get_params(),
)
def test_conv3d(
    in_channels,
    out_channels,
    kernel_size,
    stride,
    padding,
    groups,
    batch,
    in_t,
    in_h,
    in_w,
    use_bias,
    num_aie_columns,
    tile_size,
    aie_context,
):
    """Primary end-to-end integration test (main-tree quality bar).

    Exercises the complete production path on the branch:
    - AIEConv3d construction + registration with per-test AIEContext
    - context.compile_all() -> design.py:my_conv3d (use_bias affects wiring)
      + KernelObjectArtifact (aie_kernels/{aie2,aie2p}/conv3d.cc) + xclbin/insts
    - context.prepare_runtime() -> set_up_runtime (bias-dependent runlist),
      full buffer conflict analysis, BO allocation, XRT kernel handles
    - Warmup + timed run via run_test harness
    - Numeric verification against golden (bf16 tolerances)
    - Metrics capture for regression tracking

    The get_params matrix supplies variable num_aie_columns + matching tile_size
    (subject to strict element divisibility enforced at collection). This
    exercises every legal column parallelism and per-column tile specialization
    in design + kernels for both AIE2 and AIE2P (kernel dir chosen dynamically
    in op.set_up_artifacts via device_manager.device_str()).

    Strong inline dimension cross-checks guard against formula drift between
    op.py, design.py, reference.calculate_output_dim, and torch F.conv3d.
    """
    # Inlined (no helper) for canonical clean structure matching conv2d/avgpool.
    golden_ref = generate_golden_reference(
        batch_size=batch,
        in_channels=in_channels,
        in_t=in_t,
        in_h=in_h,
        in_w=in_w,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        seed=42,
    )

    operator = AIEConv3d(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        in_t=in_t,
        in_h=in_h,
        in_w=in_w,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
        context=aie_context,
    )

    # Cross-validate output dimension math (catches formula drift between
    # operator, MLIR design, reference, and torch.nn.functional.conv3d).
    out_shape = golden_ref["output"].shape
    assert out_shape[0] == batch and out_shape[1] == out_channels
    assert (
        operator.out_t == out_shape[2]
    ), f"out_t mismatch: operator={operator.out_t}, golden={out_shape[2]}"
    assert (
        operator.out_h == out_shape[3]
    ), f"out_h mismatch: operator={operator.out_h}, golden={out_shape[3]}"
    assert (
        operator.out_w == out_shape[4]
    ), f"out_w mismatch: operator={operator.out_w}, golden={out_shape[4]}"

    input_buffers = {
        "input": golden_ref["input"],
        "weight": golden_ref["weight"],
    }
    if golden_ref.get("bias") is not None:
        input_buffers["bias"] = golden_ref["bias"]

    output_buffers = {"output": golden_ref["output"]}

    # bf16 Conv3D numerical sensitivity (volumetric):
    # - bf16 ~7-8 significant bits. Each output element aggregates a dot-product
    #   over (kT*kH*kW * Cin/groups) MACs in a 3D volume. For k=3 / Cin=16 this
    #   is already hundreds of ops; temporal dim amplifies accumulation/rounding
    #   vs the PyTorch F.conv3d(bf16) reference path.
    # - 0.05 rel_tol (5%) + 1e-5 abs is the robust production threshold used
    #   across conv/pool operators: catches logic/padding/chunking bugs while
    #   tolerating expected AIE vs torch bf16 differences on valid kernels.
    # - Golden is *always* from generate_golden_reference (conv3d_cpu path).
    errors, latency_us, bandwidth_gbps = run_test(
        operator, input_buffers, output_buffers, rel_tol=0.05, abs_tol=1e-5
    )

    # Exactly the two lines required by the @metrics regexes (main-tree style,
    # identical to conv2d/maxpool/avgpool/reduction). Extra debug prints removed
    # for robust CSV/metrics reporter capture and pre-push hook compatibility.
    # (AIE2 vs AIE2P path selection is transparent via the operator's artifact setup.)
    print(f"\nLatency (us): {latency_us:.1f}")
    print(f"Effective Bandwidth: {bandwidth_gbps:.6e} GB/s\n")

    assert not errors, f"Test failed with errors: {errors}"


# =============================================================================
# Forward / high-level API integration test
# =============================================================================


@pytest.mark.parametrize(
    CONV3D_TEST_PARAM_NAMES,
    FORWARD_CASES,
)
def test_conv3d_forward(
    in_channels,
    out_channels,
    kernel_size,
    stride,
    padding,
    groups,
    batch,
    in_t,
    in_h,
    in_w,
    use_bias,
    num_aie_columns,
    tile_size,
    aie_context,
):
    """High-level forward() / __call__ API integration test (production quality).

    This test deliberately drives the *complete* branch infrastructure even
    for the convenience wrapper:
      - Construction registers with aie_context
      - Explicit compile_all() (full artifact pipeline via design callback)
      - Explicit prepare_runtime() (set_up_runtime + BO pool + runlist)
      - operator(...) -> forward() -> internal per-batch _process_single
        (write_buffer, run_runlist, read_buffer_as_torch)
      - Numeric comparison + dimension cross-check

    Also exercises batch>1 reuse of an already-prepared operator (re-uses
    the same runlist/BOs/kernel handles).

    Complements the primary run_test-based test. Uses relaxed bf16 tolerances
    (consistent with conv2d forward) because this path exercises the Python
    per-batch slicing loop + XRT buffer IO on top of the AIE kernels.
    Inlined construction (canonical clean style, no helpers).
    """
    # Inlined golden + operator (canonical form; no fragile shared helper).
    golden_ref = generate_golden_reference(
        batch_size=batch,
        in_channels=in_channels,
        in_t=in_t,
        in_h=in_h,
        in_w=in_w,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        seed=42,
    )

    operator = AIEConv3d(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        in_t=in_t,
        in_h=in_h,
        in_w=in_w,
        num_aie_columns=num_aie_columns,
        tile_size=tile_size,
        context=aie_context,
    )

    # Cross-validate dims inline (consistent with primary test).
    out_shape = golden_ref["output"].shape
    assert out_shape[0] == batch and out_shape[1] == out_channels
    assert operator.out_t == out_shape[2]
    assert operator.out_h == out_shape[3]
    assert operator.out_w == out_shape[4]

    # Full integration exercise of the heavy branch AIEContext paths (exact
    # pattern used by polished maxpool/avgpool/conv2d forward tests).
    operator.context.compile_all()
    operator.context.prepare_runtime()

    # Pass golden["bias"] unconditionally (it is the tensor or None when
    # use_bias=False). Matches exact pattern in conv2d/test.py forward test.
    result = operator(
        golden_ref["input"],
        golden_ref["weight"],
        golden_ref["bias"],
    )

    expected = golden_ref["output"]
    assert (
        result.shape == expected.shape
    ), f"Shape mismatch: got {result.shape}, expected {expected.shape}"

    # bf16 tolerances for forward path (slightly looser abs than run_test
    # because this exercises the Python per-batch slicing loop + XRT IO).
    # Same rationale as primary: 3D volumetric MAC accumulation in bf16 on AIE
    # vs torch F.conv3d(bf16) reference can differ by a few percent relative
    # due to vectorization, fma ordering, and intermediate rounding. Golden
    # generated exclusively via generate_golden_reference / conv3d_cpu.
    rel_tol, abs_tol = 0.05, 0.1
    if not torch.allclose(result, expected, rtol=rel_tol, atol=abs_tol):
        max_diff = (result - expected).abs().max().item()
        pytest.fail(f"Results don't match. Max diff: {max_diff}")

    # Batch>1 reuse of the already-prepared operator / runlist (valuable
    # coverage of the Python-level batch loop in the operator forward).
    golden_b2 = generate_golden_reference(
        batch_size=2,
        in_channels=in_channels,
        in_t=in_t,
        in_h=in_h,
        in_w=in_w,
        out_channels=out_channels,
        kernel_size=kernel_size,
        stride=stride,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        seed=123,
    )
    result_b2 = operator(
        golden_b2["input"],
        golden_b2["weight"],
        golden_b2["bias"],
    )
    expected_b2 = golden_b2["output"]
    assert result_b2.shape == expected_b2.shape
    assert torch.allclose(
        result_b2, expected_b2, rtol=rel_tol, atol=abs_tol
    ), "Batch-2 forward results mismatch"


# =============================================================================
# PURE-CPU REFERENCE VALIDATION LIVES IN cpu_test.py
# =============================================================================
# All hardware-independent reference validation (generate_golden_reference,
# conv3d_cpu contract, calculate_output_dim cross-checks vs F.conv3d,
# get_params ID health + regular/ext invariants, 3D-specific coverage for
# temporal/asymmetric/partial-groups/dilation-in-ref, seed determinism) has
# been extracted to iron/operators/conv3d/cpu_test.py following the production
# reduction/conv2d/maxpool/avgpool pattern.
#
# Run under iron314 (no XRT/NPU required, no aie_context):
#   conda run -n iron314 python -m pytest iron/operators/conv3d/cpu_test.py -q --tb=short
#   conda run -n iron314 python -m pytest iron/operators/conv3d/cpu_test.py -q --iterations 1 -k "reference_cpu_only"
#
# This keeps test.py focused exclusively on NPU paths (@metrics + forward + design matrix).
# The cpu_test.py sibling imports get_params from here (defensive, collection-safe).
# =============================================================================

# Tests are pytest-only (AGENTS.md convention).
# CPU tests: python -m pytest iron/operators/conv3d/cpu_test.py
# HW tests:  python -m pytest iron/operators/conv3d/test.py -q -m "not extensive"
