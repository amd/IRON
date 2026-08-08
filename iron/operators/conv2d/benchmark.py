# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Frozen-shape measurement helpers for AIEConv2d (Ring 1 self-regression).

Semantics for Latency / Effective BW / GFLOPS live in ROADMAP.md §2.
This module freezes B1–B6 shapes and provides FLOPs, percentile stats, CSV
schema, and an optional multi-iter NPU runner. It does not invent baseline
numbers; CSV rows are only written from real runs.
"""

from __future__ import annotations

import csv
import math
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence

from iron.operators.conv2d.reference import calculate_output_dim

# Default protocol (ROADMAP §2.3). Override only for local experiments.
DEFAULT_WARMUP_ITERS = 5
DEFAULT_TIMED_ITERS = 20

CSV_FIELDNAMES = (
    "commit",
    "device",
    "shape_id",
    "kind",
    "batch",
    "in_channels",
    "out_channels",
    "in_h",
    "in_w",
    "kernel",
    "stride",
    "padding",
    "groups",
    "use_bias",
    "num_aie_columns",
    "flops",
    "warmup_iters",
    "timed_iters",
    "latency_mean_us",
    "latency_median_us",
    "latency_p99_us",
    "gflops_median",
    "bandwidth_gbps_median",
    "correctness",
)


@dataclass(frozen=True)
class BenchShape:
    """One frozen benchmark configuration (logical conv + column request)."""

    id: str
    kind: str
    batch: int
    in_channels: int
    out_channels: int
    in_h: int
    in_w: int
    kernel: int
    stride: int
    padding: int
    groups: int
    use_bias: bool
    num_aie_columns: int

    @property
    def out_h(self) -> int:
        return calculate_output_dim(
            self.in_h, self.kernel, self.stride, self.padding, dilation=1
        )

    @property
    def out_w(self) -> int:
        return calculate_output_dim(
            self.in_w, self.kernel, self.stride, self.padding, dilation=1
        )


# Frozen suite (ROADMAP §2.3). Do not expand casually — trends need a stable set.
BENCHMARK_SHAPES: tuple[BenchShape, ...] = (
    # B1 pointwise 32→64, 32×32, k1
    BenchShape("B1", "pointwise", 1, 32, 64, 32, 32, 1, 1, 0, 1, True, 1),
    BenchShape("B1", "pointwise", 1, 32, 64, 32, 32, 1, 1, 0, 1, False, 1),
    BenchShape("B1", "pointwise", 1, 32, 64, 32, 32, 1, 1, 0, 1, True, 2),
    BenchShape("B1", "pointwise", 1, 32, 64, 32, 32, 1, 1, 0, 1, True, 4),
    # B2 standard k3 16→16, 32×32, s1 p1
    BenchShape("B2", "standard_k3", 1, 16, 16, 32, 32, 3, 1, 1, 1, True, 1),
    BenchShape("B2", "standard_k3", 1, 16, 16, 32, 32, 3, 1, 1, 1, True, 2),
    # B3 strided k3 16→16, 64×64, s2
    BenchShape("B3", "strided", 1, 16, 16, 64, 64, 3, 2, 1, 1, True, 1),
    # B4 depthwise C=32, 32×32, k3
    BenchShape("B4", "depthwise", 1, 32, 32, 32, 32, 3, 1, 1, 32, True, 1),
    BenchShape("B4", "depthwise", 1, 32, 32, 32, 32, 3, 1, 1, 32, True, 2),
    # B5 fat pointwise 32→64, 64×64
    BenchShape("B5", "fat_pointwise", 1, 32, 64, 64, 64, 1, 1, 0, 1, True, 1),
    BenchShape("B5", "fat_pointwise", 1, 32, 64, 64, 64, 1, 1, 0, 1, True, 2),
    BenchShape("B5", "fat_pointwise", 1, 32, 64, 64, 64, 1, 1, 0, 1, True, 4),
    # B6 grouped g=2, 4→8, 32×32 k3
    BenchShape("B6", "grouped", 1, 4, 8, 32, 32, 3, 1, 1, 2, True, 1),
)


def shapes_for_ids(ids: Optional[Iterable[str]] = None) -> tuple[BenchShape, ...]:
    """Filter BENCHMARK_SHAPES by shape id (e.g. 'B1'). None → full suite."""
    if ids is None:
        return BENCHMARK_SHAPES
    wanted = {i.strip().upper() for i in ids}
    return tuple(s for s in BENCHMARK_SHAPES if s.id in wanted)


def conv2d_flops(
    batch: int,
    in_channels: int,
    out_channels: int,
    out_h: int,
    out_w: int,
    kernel_h: int,
    kernel_w: int,
    groups: int,
) -> int:
    """MAC count × 2 (mul+add) for one forward.

    FLOPs = 2 * N * Cout * OH * OW * (Cin/G) * KH * KW
    """
    if groups <= 0 or in_channels % groups != 0:
        raise ValueError(f"invalid groups={groups} for in_channels={in_channels}")
    cin_per_g = in_channels // groups
    return 2 * batch * out_channels * out_h * out_w * cin_per_g * kernel_h * kernel_w


def shape_flops(shape: BenchShape) -> int:
    return conv2d_flops(
        shape.batch,
        shape.in_channels,
        shape.out_channels,
        shape.out_h,
        shape.out_w,
        shape.kernel,
        shape.kernel,
        shape.groups,
    )


def gflops(flops: int, latency_us: float) -> float:
    """Throughput in GFLOP/s from FLOP count and latency in microseconds."""
    if latency_us <= 0:
        return float("nan")
    return flops / (latency_us * 1e-6) / 1e9


def bandwidth_gbps(total_bytes: int, latency_us: float) -> float:
    """Effective bandwidth: BO-byte sum / latency (same definition as run_test)."""
    if latency_us <= 0:
        return float("nan")
    return total_bytes / (latency_us * 1e-6) / 1e9


def percentile_nearest(sorted_samples: Sequence[float], p: float) -> float:
    """Nearest-rank percentile; ``p`` in [0, 100]. Empty → nan."""
    if not sorted_samples:
        return float("nan")
    if p <= 0:
        return float(sorted_samples[0])
    if p >= 100:
        return float(sorted_samples[-1])
    # Nearest-rank: ceil(p/100 * n) with 1-based rank, clamped.
    rank = max(1, min(len(sorted_samples), math.ceil(p / 100.0 * len(sorted_samples))))
    return float(sorted_samples[rank - 1])


def latency_stats_us(npu_time_ns_samples: Sequence[float]) -> dict[str, float]:
    """Convert per-iter NPU times (ns) to µs mean / median / p99."""
    if not npu_time_ns_samples:
        return {
            "mean_us": float("nan"),
            "median_us": float("nan"),
            "p99_us": float("nan"),
        }
    us = [float(t) / 1e3 for t in npu_time_ns_samples]
    ordered = sorted(us)
    return {
        "mean_us": float(statistics.fmean(us)),
        "median_us": float(statistics.median(us)),
        "p99_us": percentile_nearest(ordered, 99),
    }


def estimate_arg_bytes(
    in_channels: int,
    in_h: int,
    in_w: int,
    out_channels: int,
    out_h: int,
    out_w: int,
    kernel: int,
    groups: int,
    use_bias: bool,
    bytes_per_elem: int = 2,
) -> int:
    """Host-visible BO byte estimate (input + weight + optional bias + output).

    Matches the buffers registered in get_arg_spec / run_test for bf16.
    Host bias is still counted when use_bias (same as Effective BW today).
    """
    in_elems = in_channels * in_h * in_w
    w_elems = out_channels * (in_channels // groups) * kernel * kernel
    out_elems = out_channels * out_h * out_w
    bias_elems = out_channels if use_bias else 0
    return (in_elems + w_elems + out_elems + bias_elems) * bytes_per_elem


@dataclass
class BenchResult:
    shape: BenchShape
    flops: int
    warmup_iters: int
    timed_iters: int
    latency_mean_us: float
    latency_median_us: float
    latency_p99_us: float
    gflops_median: float
    bandwidth_gbps_median: float
    correctness: str  # "pass" | "fail" | "skip"
    device: str = ""
    commit: str = ""
    detail: str = ""

    def to_csv_row(self) -> dict[str, Any]:
        s = self.shape
        return {
            "commit": self.commit,
            "device": self.device,
            "shape_id": s.id,
            "kind": s.kind,
            "batch": s.batch,
            "in_channels": s.in_channels,
            "out_channels": s.out_channels,
            "in_h": s.in_h,
            "in_w": s.in_w,
            "kernel": s.kernel,
            "stride": s.stride,
            "padding": s.padding,
            "groups": s.groups,
            "use_bias": int(s.use_bias),
            "num_aie_columns": s.num_aie_columns,
            "flops": self.flops,
            "warmup_iters": self.warmup_iters,
            "timed_iters": self.timed_iters,
            "latency_mean_us": f"{self.latency_mean_us:.4f}",
            "latency_median_us": f"{self.latency_median_us:.4f}",
            "latency_p99_us": f"{self.latency_p99_us:.4f}",
            "gflops_median": f"{self.gflops_median:.6e}",
            "bandwidth_gbps_median": f"{self.bandwidth_gbps_median:.6e}",
            "correctness": self.correctness,
        }


def write_csv(
    path: Path | str,
    results: Sequence[BenchResult],
    *,
    append: bool = False,
) -> None:
    """Write or append BenchResult rows. Creates parent dirs. No header-only invent."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    write_header = not append or not path.exists() or path.stat().st_size == 0
    mode = "a" if append else "w"
    with path.open(mode, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDNAMES)
        if write_header:
            writer.writeheader()
        for r in results:
            writer.writerow(r.to_csv_row())


def format_metrics_lines(result: BenchResult) -> str:
    """Human-readable lines (includes GFLOPS; CI @metrics may ignore extras)."""
    return (
        f"\n[bench {result.shape.id}/{result.shape.kind} "
        f"{result.shape.num_aie_columns}c bias={result.shape.use_bias}]\n"
        f"Latency mean (us): {result.latency_mean_us:.1f}\n"
        f"Latency median (us): {result.latency_median_us:.1f}\n"
        f"Latency p99 (us): {result.latency_p99_us:.1f}\n"
        f"Throughput: {result.gflops_median:.6e} GFLOP/s\n"
        f"Effective Bandwidth: {result.bandwidth_gbps_median:.6e} GB/s\n"
        f"Correctness: {result.correctness}\n"
    )


def run_shape_on_npu(
    shape: BenchShape,
    aie_context,
    *,
    warmup_iters: int = DEFAULT_WARMUP_ITERS,
    timed_iters: int = DEFAULT_TIMED_ITERS,
    rel_tol: float = 0.1,
    abs_tol: float = 1.0,
    max_error_rate: float = 0.02,
    commit: str = "",
    device_name: str = "",
) -> BenchResult:
    """Compile + multi-iter timed run for one frozen shape.

    Uses NPU ``result.npu_time`` samples for median/p99 (not host wall clock).
    Raises import/runtime errors to the caller; L1/column rejects return skip.
    """
    from ml_dtypes import bfloat16

    from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor

    from iron.common import AIEOperatorConstraintError
    from iron.common.test_utils import verify_buffer
    from iron.operators.conv2d.op import AIEConv2d
    from iron.operators.conv2d.reference import generate_golden_reference

    flops = shape_flops(shape)
    total_bytes = estimate_arg_bytes(
        shape.in_channels,
        shape.in_h,
        shape.in_w,
        shape.out_channels,
        shape.out_h,
        shape.out_w,
        shape.kernel,
        shape.groups,
        shape.use_bias,
    )

    try:
        operator = AIEConv2d(
            in_channels=shape.in_channels,
            out_channels=shape.out_channels,
            kernel_size=shape.kernel,
            stride=shape.stride,
            padding=shape.padding,
            groups=shape.groups,
            use_bias=shape.use_bias,
            in_height=shape.in_h,
            in_width=shape.in_w,
            num_aie_columns=shape.num_aie_columns,
            context=aie_context,
        )
    except AIEOperatorConstraintError as e:
        return BenchResult(
            shape=shape,
            flops=flops,
            warmup_iters=warmup_iters,
            timed_iters=0,
            latency_mean_us=float("nan"),
            latency_median_us=float("nan"),
            latency_p99_us=float("nan"),
            gflops_median=float("nan"),
            bandwidth_gbps_median=float("nan"),
            correctness="skip",
            device=device_name,
            commit=commit,
            detail=str(e),
        )

    golden = generate_golden_reference(
        batch_size=shape.batch,
        in_channels=shape.in_channels,
        in_height=shape.in_h,
        in_width=shape.in_w,
        out_channels=shape.out_channels,
        kernel_size=shape.kernel,
        stride=shape.stride,
        padding=shape.padding,
        groups=shape.groups,
        use_bias=shape.use_bias,
        seed=42,
    )

    operator.compile()
    op_func = operator.get_callable()

    # Flatten N=1 tensors to match get_arg_spec (batch looped outside for N>1).
    x = golden["input"][0].reshape(-1).contiguous()
    w = golden["weight"].reshape(-1).contiguous()
    y_ref = golden["output"][0].reshape(-1).contiguous()

    in_b = XRTTensor.from_torch(x)
    w_b = XRTTensor.from_torch(w)
    out_b = XRTTensor((operator.output_size,), dtype=bfloat16)

    if shape.use_bias and golden["bias"] is not None:
        bias_b = XRTTensor.from_torch(golden["bias"].reshape(-1).contiguous())
        call_args = (in_b, w_b, bias_b, out_b)
    else:
        call_args = (in_b, w_b, out_b)

    for _ in range(warmup_iters):
        op_func(*call_args)

    samples_ns: list[float] = []
    for _ in range(timed_iters):
        result = op_func(*call_args)
        samples_ns.append(float(result.npu_time))

    stats = latency_stats_us(samples_ns)
    med = stats["median_us"]
    thr = gflops(flops, med)
    bw = bandwidth_gbps(total_bytes, med)

    # Correctness on last output vs golden.
    out_torch = out_b.to_torch()
    errs = verify_buffer(
        out_torch,
        "output",
        y_ref,
        rel_tol=rel_tol,
        abs_tol=abs_tol,
        max_error_rate=max_error_rate,
    )
    correctness = "pass" if not errs else "fail"

    return BenchResult(
        shape=shape,
        flops=flops,
        warmup_iters=warmup_iters,
        timed_iters=timed_iters,
        latency_mean_us=stats["mean_us"],
        latency_median_us=med,
        latency_p99_us=stats["p99_us"],
        gflops_median=thr,
        bandwidth_gbps_median=bw,
        correctness=correctness,
        device=device_name,
        commit=commit,
        detail="" if correctness == "pass" else f"{len(errs)} mismatches",
    )


def resolve_device_name() -> str:
    try:
        import aie.utils as aie_utils

        dev = aie_utils.get_current_device()
        cols = getattr(dev, "cols", "?")
        name = type(dev).__name__
        return f"{name}_cols{cols}"
    except Exception:
        return "unknown"


def resolve_git_commit(cwd: Optional[Path] = None) -> str:
    import subprocess

    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=cwd or Path.cwd(),
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except Exception:
        return ""
