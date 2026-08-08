#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pure-CPU tests for AIEConv2d reference + benchmark helpers (no XRT/NPU)."""

import math

import pytest

import torch
import torch.nn.functional as F

from .reference import (
    generate_golden_reference,
    conv2d_cpu,
    calculate_output_dim,
)
from .test import get_params


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


# ---------------------------------------------------------------------------
# Benchmark harness (pure CPU: FLOPs, stats, CSV schema — no NPU)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("dummy", [pytest.param(None, id="bench_shapes")])
def test_benchmark_shapes_frozen_and_divisible(dummy):
    """B1–B6 exist; each shape has positive OH/OW and legal groups."""
    from .benchmark import BENCHMARK_SHAPES, shape_flops, shapes_for_ids

    ids = {s.id for s in BENCHMARK_SHAPES}
    assert ids == {"B1", "B2", "B3", "B4", "B5", "B6"}
    assert len(shapes_for_ids(["B2"])) == 2
    for s in BENCHMARK_SHAPES:
        assert s.out_h > 0 and s.out_w > 0
        assert s.in_channels % s.groups == 0
        assert s.out_channels % s.groups == 0
        assert shape_flops(s) > 0


@pytest.mark.parametrize("dummy", [pytest.param(None, id="bench_flops")])
def test_benchmark_flops_and_gflops_formula(dummy):
    """FLOPs = 2*N*Cout*OH*OW*(Cin/G)*KH*KW; GFLOPS uses latency_us."""
    from .benchmark import arithmetic_intensity, conv2d_flops, gflops

    # N=1, 16→32, 8x8 out, k=3, g=1 → 2*1*32*8*8*16*3*3 = 589824
    flops = conv2d_flops(1, 16, 32, 8, 8, 3, 3, 1)
    assert flops == 2 * 1 * 32 * 8 * 8 * 16 * 3 * 3
    # 1e6 µs = 1 s → GFLOP/s = flops / 1e9
    assert abs(gflops(flops, 1e6) - flops / 1e9) < 1e-12
    assert math.isnan(gflops(flops, 0.0))
    assert arithmetic_intensity(1000, 100) == 10.0
    assert math.isnan(arithmetic_intensity(1000, 0))


@pytest.mark.parametrize("dummy", [pytest.param(None, id="bench_stats")])
def test_benchmark_latency_stats_and_percentile(dummy):
    from .benchmark import latency_stats_us, percentile_nearest

    # 1000, 2000, 3000 ns → 1.0, 2.0, 3.0 µs
    stats = latency_stats_us([1000.0, 2000.0, 3000.0])
    assert stats["mean_us"] == 2.0
    assert stats["median_us"] == 2.0
    assert stats["p99_us"] == 3.0
    ordered = [1.0, 2.0, 3.0, 4.0]
    assert percentile_nearest(ordered, 0) == 1.0
    assert percentile_nearest(ordered, 100) == 4.0
    assert math.isnan(percentile_nearest([], 50))


@pytest.mark.parametrize("dummy", [pytest.param(None, id="bench_csv")])
def test_benchmark_csv_roundtrip(dummy, tmp_path):
    from .benchmark import (
        BENCHMARK_SHAPES,
        BenchResult,
        shape_flops,
        write_csv,
        CSV_FIELDNAMES,
    )

    s = BENCHMARK_SHAPES[0]
    r = BenchResult(
        shape=s,
        flops=shape_flops(s),
        warmup_iters=5,
        timed_iters=20,
        latency_mean_us=10.0,
        latency_median_us=9.5,
        latency_p99_us=12.0,
        gflops_median=1.23e2,
        bandwidth_gbps_median=4.56e0,
        correctness="pass",
        device="NPU2_cols8",
        commit="deadbee",
        total_bytes=4096,
        arithmetic_intensity=12.5,
        cpu_latency_median_us=100.0,
    )
    path = tmp_path / "conv2d_bench.csv"
    write_csv(path, [r])
    text = path.read_text()
    header = text.splitlines()[0].split(",")
    assert header == list(CSV_FIELDNAMES)
    assert "B1" in text and "deadbee" in text and "pass" in text
    assert "arithmetic_intensity" in header
    assert "cpu_latency_median_us" in header
    # scientific format from BenchResult.to_csv_row
    assert "1.250000e+01" in text
    assert "100.0000" in text


@pytest.mark.parametrize("dummy", [pytest.param(None, id="bench_cpu_wall")])
def test_benchmark_torch_cpu_wall_clock(dummy):
    """Ring 4 helper: positive median µs and AI on a small frozen shape."""
    from .benchmark import BENCHMARK_SHAPES, run_shape_on_torch_cpu

    # B1 pointwise 1-col is small and stable for host timing.
    shape = next(s for s in BENCHMARK_SHAPES if s.id == "B1" and s.num_aie_columns == 1)
    stats = run_shape_on_torch_cpu(shape, warmup_iters=1, timed_iters=3)
    assert stats["median_us"] > 0
    assert stats["mean_us"] > 0
    assert stats["flops"] > 0
    assert stats["arithmetic_intensity"] > 0


@pytest.mark.parametrize("dummy", [pytest.param(None, id="bench_peer_protocol")])
def test_benchmark_peer_and_mlir_aie_protocol(dummy):
    """Peer ring notes and mlir-aie comparison protocol stay documented in code."""
    from .benchmark import (
        MLIR_AIE_COMPARISON_PROTOCOL,
        PEER_BW_REFERENCES,
        PEER_CSV_FIELDNAMES,
        PeerBenchResult,
        write_peer_csv,
    )

    assert len(PEER_BW_REFERENCES) >= 3
    for row in PEER_BW_REFERENCES:
        assert "peer" in row and "do_not_claim" in row
        assert "runner" in row
    proto = MLIR_AIE_COMPARISON_PROTOCOL
    assert len(proto["examples"]) == 2
    assert "hard_disclaimers" in proto and len(proto["hard_disclaimers"]) >= 2
    assert "procedure" in proto and len(proto["procedure"]) >= 3
    assert "dtype" in proto["required_columns"]
    assert "peer" in PEER_CSV_FIELDNAMES and "disclaimer" in PEER_CSV_FIELDNAMES


@pytest.mark.parametrize("dummy", [pytest.param(None, id="hw_tolerances_audit")])
def test_hw_tolerances_tighter_than_legacy(dummy):
    """Audit policy is centralized and stricter than pre-audit MVP defaults."""
    from iron.operators.conv2d.tolerances import (
        HW_DEFAULT,
        HW_LEGACY_LOOSE,
        hw_tolerances,
    )

    t = hw_tolerances()
    assert t is HW_DEFAULT
    assert t.rel_tol < HW_LEGACY_LOOSE.rel_tol
    assert t.abs_tol < HW_LEGACY_LOOSE.abs_tol
    assert 0 < t.max_error_rate <= HW_LEGACY_LOOSE.max_error_rate
    assert t.rel_tol < 1.0 and t.abs_tol > 0


@pytest.mark.parametrize("dummy", [pytest.param(None, id="pack_weights_bias")])
def test_pack_weights_with_bias_layout(dummy):
    """Tile-interleaved W‖B pack matches design contract (groups==1, 2 cols)."""
    import numpy as np
    from ml_dtypes import bfloat16

    from iron.operators.conv2d.design import pack_weights_with_bias

    oc, ic, kh, kw = 8, 4, 3, 3
    wpo = ic * kh * kw
    w = np.arange(oc * wpo, dtype=np.float32).astype(bfloat16)
    b = (np.arange(oc, dtype=np.float32) + 100).astype(bfloat16)
    packed = pack_weights_with_bias(
        w,
        b,
        out_channels=oc,
        in_channels=ic,
        groups=1,
        kernel_h=kh,
        kernel_w=kw,
        num_columns=2,
        is_depthwise=False,
        tile_channels=4,
    )
    # 2 cols × 1 tile × (4*wpo + 4 bias)
    assert packed.shape[0] == oc * wpo + oc
    # First tile: OCs 0..3
    assert np.array_equal(packed[: 4 * wpo], w[: 4 * wpo])
    assert np.array_equal(packed[4 * wpo : 4 * wpo + 4], b[:4])


@pytest.mark.parametrize("dummy", [pytest.param(None, id="pack_weights_bias_grouped_2c")])
def test_pack_weights_with_bias_grouped_multicol(dummy):
    """Grouped multi-col pack: OC blocks per column (groups % cols == 0)."""
    import numpy as np
    from ml_dtypes import bfloat16

    from iron.operators.conv2d.design import (
        _resolve_num_columns,
        pack_weights_with_bias,
    )

    # g=2, IC=8, OC=16 → 2 cols ⇒ g_per_col=1, ic_per_col=4, oc_per_col=8
    oc, ic, g, kh, kw = 16, 8, 2, 3, 3
    wpo = (ic // g) * kh * kw
    assert _resolve_num_columns(2, oc, ic, g, False, max_cols=8) == 2
    assert _resolve_num_columns(3, oc, ic, g, False, max_cols=8) == 2  # clamp
    assert _resolve_num_columns(8, oc, ic, g, False, max_cols=8) == 2
    w = np.arange(oc * wpo, dtype=np.float32).astype(bfloat16)
    b = (np.arange(oc, dtype=np.float32) + 50).astype(bfloat16)
    packed = pack_weights_with_bias(
        w,
        b,
        out_channels=oc,
        in_channels=ic,
        groups=g,
        kernel_h=kh,
        kernel_w=kw,
        num_columns=2,
        is_depthwise=False,
        tile_channels=8,  # full oc_per_col
    )
    assert packed.shape[0] == oc * wpo + oc
    # Col0 tile: OC 0..7 weights then bias
    assert np.array_equal(packed[: 8 * wpo], w[: 8 * wpo])
    assert np.array_equal(packed[8 * wpo : 8 * wpo + 8], b[:8])
    # Col1 tile: OC 8..15
    mid = 8 * wpo + 8
    assert np.array_equal(packed[mid : mid + 8 * wpo], w[8 * wpo :])
    assert np.array_equal(packed[mid + 8 * wpo :], b[8:])


@pytest.mark.parametrize("dummy", [pytest.param(None, id="bench_peer_csv_schema")])
def test_peer_csv_schema(dummy, tmp_path):
    """Peer CSV writer emits documented columns without inventing metrics."""
    from .benchmark import PEER_CSV_FIELDNAMES, PeerBenchResult, write_peer_csv

    r = PeerBenchResult(
        peer="relu",
        role="BW ceiling",
        align_to="B1_in_elems",
        problem_shape="size=32768",
        total_bytes=131072,
        flops=32768,
        arithmetic_intensity=0.25,
        warmup_iters=2,
        timed_iters=5,
        latency_median_us=12.5,
        bandwidth_gbps_median=1.0,
        gflops_median=0.5,
        correctness="pass",
        disclaimer="Ring-2 only",
        device="NPU2_cols8",
        commit="abc1234",
    )
    path = tmp_path / "peer.csv"
    write_peer_csv(path, [r])
    header = path.read_text().splitlines()[0].split(",")
    assert header == list(PEER_CSV_FIELDNAMES)
    assert "relu" in path.read_text() and "Ring-2" in path.read_text()


# Tests are pytest-only (AGENTS.md convention).
