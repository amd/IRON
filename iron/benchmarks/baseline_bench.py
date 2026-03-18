#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Baseline Benchmark Suite - CPU Reference Implementations

This benchmark suite provides baseline performance measurements using
optimized PyTorch CPU implementations. These serve as reference points
until AIE NPU hardware benchmarks can be collected.

Usage:
    # Run all benchmarks
    python -m iron.benchmarks.baseline_bench --iterations 100 --warmup 10

    # Output to JSON
    python -m iron.benchmarks.baseline_bench --output json --output-file results.json
"""

import argparse
import json
import logging
import sys
import time
import statistics
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime
import torch
import numpy as np
from ml_dtypes import bfloat16

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# =============================================================================
# Target Performance Specifications (NPU Targets)
# =============================================================================


@dataclass
class PerformanceTarget:
    """Target performance specification for an operator"""

    operator_name: str
    input_shape: tuple
    target_latency_ms: float
    description: str
    cpu_baseline_factor: float = 10.0  # CPU expected to be ~10x slower than NPU


PERFORMANCE_TARGETS = {
    "rope": PerformanceTarget(
        operator_name="rope",
        input_shape=(1, 12, 128, 64),
        target_latency_ms=0.5,
        description="RoPE (Rotary Positional Embedding) for [1, 12, 128, 64]",
        cpu_baseline_factor=10.0,
    ),
    "rmsnorm": PerformanceTarget(
        operator_name="rmsnorm",
        input_shape=(1, 128, 2048),
        target_latency_ms=1.0,
        description="RMSNorm for [1, 128, 2048]",
        cpu_baseline_factor=10.0,
    ),
    "silu": PerformanceTarget(
        operator_name="silu",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.3,
        description="SiLU (Sigmoid Linear Unit) for [1, 128, 8192]",
        cpu_baseline_factor=10.0,
    ),
    "softmax": PerformanceTarget(
        operator_name="softmax",
        input_shape=(1, 12, 128, 128),
        target_latency_ms=2.0,
        description="Softmax for [1, 12, 128, 128]",
        cpu_baseline_factor=10.0,
    ),
}


# =============================================================================
# Data Classes
# =============================================================================


@dataclass
class BenchmarkConfig:
    """Configuration for benchmark execution"""

    iterations: int = 50
    warmup: int = 10
    output_format: str = "console"
    output_file: Optional[str] = None
    verbose: bool = False
    operator: Optional[str] = None
    device: str = "cpu"
    dtype: str = "bfloat16"

    def __post_init__(self):
        if self.iterations < 1:
            raise ValueError("iterations must be >= 1")
        if self.warmup < 0:
            raise ValueError("warmup must be >= 0")
        if self.output_format not in ("console", "json", "markdown"):
            raise ValueError("output_format must be 'console', 'json', or 'markdown'")


@dataclass
class BenchmarkMetrics:
    """Performance metrics for a single benchmark run"""

    latencies_ms: List[float] = field(default_factory=list)
    throughput_ops_sec: float = 0.0
    memory_bandwidth_gbps: float = 0.0

    mean_ms: float = 0.0
    median_ms: float = 0.0
    std_dev_ms: float = 0.0
    p95_ms: float = 0.0
    p99_ms: float = 0.0
    min_ms: float = 0.0
    max_ms: float = 0.0

    def compute_statistics(self):
        """Compute statistical metrics from raw latencies"""
        if not self.latencies_ms:
            return

        sorted_latencies = sorted(self.latencies_ms)
        n = len(sorted_latencies)

        self.mean_ms = statistics.mean(sorted_latencies)
        self.median_ms = statistics.median(sorted_latencies)
        self.std_dev_ms = statistics.stdev(sorted_latencies) if n > 1 else 0.0
        self.p95_ms = (
            sorted_latencies[min(int((n - 1) * 0.95), n - 1)]
            if n > 1
            else sorted_latencies[-1]
        )
        self.p99_ms = (
            sorted_latencies[min(int((n - 1) * 0.99), n - 1)]
            if n > 1
            else sorted_latencies[-1]
        )
        self.min_ms = min(sorted_latencies)
        self.max_ms = max(sorted_latencies)


@dataclass
class OperatorBenchmarkResult:
    """Results for a single operator benchmark"""

    operator_name: str
    input_shape: tuple
    config: dict
    metrics: BenchmarkMetrics
    target_latency_ms: Optional[float] = None
    target_met: Optional[bool] = None
    cpu_baseline_latency_ms: Optional[float] = None
    timestamp: str = ""
    error: Optional[str] = None
    device_info: str = ""

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "operator_name": self.operator_name,
            "input_shape": list(self.input_shape),
            "config": self.config,
            "metrics": {
                "mean_ms": self.metrics.mean_ms,
                "median_ms": self.metrics.median_ms,
                "std_dev_ms": self.metrics.std_dev_ms,
                "p95_ms": self.metrics.p95_ms,
                "p99_ms": self.metrics.p99_ms,
                "min_ms": self.metrics.min_ms,
                "max_ms": self.metrics.max_ms,
                "throughput_ops_sec": self.metrics.throughput_ops_sec,
                "memory_bandwidth_gbps": self.metrics.memory_bandwidth_gbps,
            },
            "target_latency_ms": self.target_latency_ms,
            "target_met": self.target_met,
            "cpu_baseline_latency_ms": self.cpu_baseline_latency_ms,
            "timestamp": self.timestamp,
            "error": self.error,
            "device_info": self.device_info,
        }


@dataclass
class BenchmarkResults:
    """Complete benchmark results"""

    results: List[OperatorBenchmarkResult] = field(default_factory=list)
    start_time: str = ""
    end_time: str = ""
    total_duration_sec: float = 0.0
    config: dict = field(default_factory=dict)
    device_info: str = ""

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "device_info": self.device_info,
            "results": [r.to_dict() for r in self.results],
            "start_time": self.start_time,
            "end_time": self.end_time,
            "total_duration_sec": self.total_duration_sec,
            "config": self.config,
        }


# =============================================================================
# Reference Operator Implementations (Optimized CPU/PyTorch)
# =============================================================================


class OperatorBenchmark:
    """Base class for operator benchmarks"""

    def __init__(self, config: BenchmarkConfig):
        self.config = config
        self.device = torch.device(config.device)
        self.input_tensor = None
        self.dtype = torch.bfloat16 if config.dtype == "bfloat16" else torch.float32

    def setup(self):
        raise NotImplementedError

    def run(self) -> torch.Tensor:
        raise NotImplementedError

    def get_input_shape(self) -> tuple:
        raise NotImplementedError

    def get_memory_footprint(self) -> tuple:
        raise NotImplementedError


class RoPEBenchmark(OperatorBenchmark):
    """Benchmark for RoPE (Rotary Positional Embedding) operator"""

    def setup(self):
        # Shape: (batch, heads, seq_len, head_dim) = (1, 12, 128, 64)
        self.batch_size = 1
        self.num_heads = 12
        self.seq_len = 128
        self.head_dim = 64

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size,
            self.num_heads,
            self.seq_len,
            self.head_dim,
            dtype=self.dtype,
            device=self.device,
        )

        # Precompute RoPE parameters
        self.cos, self.sin = self._compute_rope_params()

    def _compute_rope_params(self):
        """Precompute cosine and sine tables for RoPE"""
        head_dim = self.head_dim
        context_length = self.seq_len
        theta_base = 10_000

        inv_freq = 1.0 / (
            theta_base
            ** (
                torch.arange(0, head_dim, 2, dtype=torch.float32)[: (head_dim // 2)]
                / head_dim
            )
        )

        positions = torch.arange(context_length, dtype=torch.float32)
        angles = positions.unsqueeze(1) * inv_freq.unsqueeze(0)

        cos = torch.cos(angles).to(self.dtype).to(self.device)
        sin = torch.sin(angles).to(self.dtype).to(self.device)

        return cos, sin

    def run(self) -> torch.Tensor:
        """Apply RoPE using optimized PyTorch operations"""
        x = self.input_tensor
        cos = self.cos
        sin = self.sin

        # Split x into first half and second half
        x1 = x[..., : self.head_dim // 2]
        x2 = x[..., self.head_dim // 2 :]

        # Apply rotary transformation
        x_rotated = torch.empty_like(x)
        x_rotated[..., : self.head_dim // 2] = (x1 * cos) + (-x2 * sin)
        x_rotated[..., self.head_dim // 2 :] = (x2 * cos) + (x1 * sin)

        return x_rotated

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.num_heads, self.seq_len, self.head_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.num_heads * self.seq_len * self.head_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class RMSNormBenchmark(OperatorBenchmark):
    """Benchmark for RMSNorm (Root Mean Square Normalization) operator"""

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 2048)
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 2048
        self.eps = 1e-6

        # Create input tensor and weight
        self.input_tensor = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )
        self.weight = torch.ones(self.hidden_dim, dtype=self.dtype, device=self.device)

    def run(self) -> torch.Tensor:
        """Apply RMSNorm"""
        x = self.input_tensor
        # Compute RMS
        rms = torch.sqrt(torch.mean(x * x, dim=-1, keepdim=True) + self.eps)
        # Normalize and scale
        return x / rms * self.weight

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class SiLUBenchmark(OperatorBenchmark):
    """Benchmark for SiLU (Sigmoid Linear Unit) operator"""

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 8192)
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 8192

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply SiLU activation"""
        return torch.nn.functional.silu(self.input_tensor)

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class SoftmaxBenchmark(OperatorBenchmark):
    """Benchmark for Softmax operator"""

    def setup(self):
        # Shape: (batch, heads, seq_len, key_len) = (1, 12, 128, 128)
        self.batch_size = 1
        self.num_heads = 12
        self.seq_len = 128
        self.key_len = 128

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size,
            self.num_heads,
            self.seq_len,
            self.key_len,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply Softmax"""
        return torch.softmax(self.input_tensor, dim=-1)

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.num_heads, self.seq_len, self.key_len)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.num_heads * self.seq_len * self.key_len
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


# =============================================================================
# Operator Map (Module-level export for external imports)
# =============================================================================

OPERATOR_MAP = {
    "rope": RoPEBenchmark,
    "rmsnorm": RMSNormBenchmark,
    "silu": SiLUBenchmark,
    "softmax": SoftmaxBenchmark,
}


# =============================================================================
# Benchmark Runner
# =============================================================================


class BenchmarkRunner:
    """Main benchmark runner that orchestrates all benchmarks"""

    # Reference to module-level OPERATOR_MAP for backward compatibility
    OPERATOR_MAP = OPERATOR_MAP

    def __init__(self, config: BenchmarkConfig):
        self.config = config
        self.results = BenchmarkResults()

    def get_device_info(self) -> str:
        """Get device information string"""
        if self.config.device == "cuda" and torch.cuda.is_available():
            return f"CUDA: {torch.cuda.get_device_name(0)}"
        elif self.config.device == "cpu":
            return (
                f"CPU: {torch.get_cpu_name()}"
                if hasattr(torch, "get_cpu_name")
                else "CPU"
            )
        return "Unknown device"

    def run_operator_benchmark(
        self, operator_name: str, benchmark_class: type
    ) -> OperatorBenchmarkResult:
        """Run benchmark for a single operator"""
        logger.info(f"Starting benchmark for {operator_name}...")

        result = OperatorBenchmarkResult(
            operator_name=operator_name,
            input_shape=(),
            config=asdict(self.config),
            metrics=BenchmarkMetrics(),
            timestamp=datetime.now().isoformat(),
            device_info=self.results.device_info,
        )

        try:
            # Create benchmark instance
            benchmark = benchmark_class(self.config)

            # Setup operator and tensors
            benchmark.setup()
            result.input_shape = benchmark.get_input_shape()

            # Get memory footprint
            input_bytes, output_bytes = benchmark.get_memory_footprint()
            total_bytes = input_bytes + output_bytes

            # Get target latency
            if operator_name in PERFORMANCE_TARGETS:
                result.target_latency_ms = PERFORMANCE_TARGETS[
                    operator_name
                ].target_latency_ms
                result.cpu_baseline_latency_ms = (
                    result.target_latency_ms
                    * PERFORMANCE_TARGETS[operator_name].cpu_baseline_factor
                )

            # Warmup runs
            logger.info(f"Running {self.config.warmup} warmup iterations...")
            for _ in range(self.config.warmup):
                benchmark.run()

            # Clear CUDA cache if using GPU
            if self.config.device == "cuda" and torch.cuda.is_available():
                torch.cuda.empty_cache()

            # Timed runs
            logger.info(f"Running {self.config.iterations} timed iterations...")
            latencies_ms = []

            for i in range(self.config.iterations):
                start_time = time.perf_counter()
                benchmark.run()
                end_time = time.perf_counter()

                latency_ms = (end_time - start_time) * 1000
                latencies_ms.append(latency_ms)

                if self.config.verbose and (i + 1) % 10 == 0:
                    logger.info(
                        f"  Iteration {i + 1}/{self.config.iterations}: {latency_ms:.4f} ms"
                    )

            # Compute metrics
            result.metrics.latencies_ms = latencies_ms
            result.metrics.compute_statistics()

            # Calculate throughput
            if result.metrics.mean_ms > 0:
                result.metrics.throughput_ops_sec = 1000.0 / result.metrics.mean_ms

            # Calculate memory bandwidth
            if result.metrics.mean_ms > 0:
                mean_sec = result.metrics.mean_ms / 1000.0
                result.metrics.memory_bandwidth_gbps = total_bytes / mean_sec / 1e9

            # Check target (using CPU baseline target, not NPU target)
            if result.cpu_baseline_latency_ms is not None:
                result.target_met = (
                    result.metrics.mean_ms <= result.cpu_baseline_latency_ms
                )

            # Log results
            status = "PASS" if result.target_met else "FAIL"
            logger.info(
                f"{operator_name} benchmark complete: "
                f"mean={result.metrics.mean_ms:.4f}ms, "
                f"cpu_baseline={result.cpu_baseline_latency_ms:.2f}ms, "
                f"status={status}"
            )

        except Exception as e:
            logger.error(f"Benchmark failed for {operator_name}: {str(e)}")
            result.error = str(e)
            result.target_met = None
            if self.config.verbose:
                import traceback

                logger.error(traceback.format_exc())

        return result

    def run_all_benchmarks(self) -> BenchmarkResults:
        """Run all operator benchmarks"""
        self.results.start_time = datetime.now().isoformat()
        self.results.config = asdict(self.config)
        self.results.device_info = self.get_device_info()
        overall_start = time.perf_counter()

        # Determine which operators to run
        if self.config.operator:
            operators = [self.config.operator]
        else:
            operators = list(self.OPERATOR_MAP.keys())

        for op_name in operators:
            if op_name not in self.OPERATOR_MAP:
                logger.warning(f"Unknown operator: {op_name}, skipping...")
                continue

            benchmark_class = self.OPERATOR_MAP[op_name]
            result = self.run_operator_benchmark(op_name, benchmark_class)
            self.results.results.append(result)

        overall_end = time.perf_counter()
        self.results.end_time = datetime.now().isoformat()
        self.results.total_duration_sec = overall_end - overall_start

        return self.results

    def format_console_output(self) -> str:
        """Format results for console output"""
        lines = []
        lines.append("=" * 80)
        lines.append("IRON BASELINE BENCHMARK RESULTS (CPU Reference)")
        lines.append("=" * 80)
        lines.append(f"Device: {self.results.device_info}")
        lines.append(f"Start Time: {self.results.start_time}")
        lines.append(f"Total Duration: {self.results.total_duration_sec:.2f}s")
        lines.append(f"Iterations: {self.config.iterations}")
        lines.append(f"Warmup: {self.config.warmup}")
        lines.append("")

        for result in self.results.results:
            lines.append("-" * 80)
            lines.append(f"Operator: {result.operator_name.upper()}")
            lines.append(f"Input Shape: {result.input_shape}")

            if result.error:
                lines.append(f"ERROR: {result.error}")
                lines.append("")
                continue

            m = result.metrics
            lines.append("")
            lines.append("Latency Statistics (ms):")
            lines.append(f"  Mean:     {m.mean_ms:8.4f}")
            lines.append(f"  Median:   {m.median_ms:8.4f}")
            lines.append(f"  Std Dev:  {m.std_dev_ms:8.4f}")
            lines.append(f"  P95:      {m.p95_ms:8.4f}")
            lines.append(f"  P99:      {m.p99_ms:8.4f}")
            lines.append(f"  Min:      {m.min_ms:8.4f}")
            lines.append(f"  Max:      {m.max_ms:8.4f}")
            lines.append("")
            lines.append(f"Throughput:      {m.throughput_ops_sec:12.2f} ops/sec")
            lines.append(f"Memory Bandwidth: {m.memory_bandwidth_gbps:12.4f} GB/s")
            lines.append("")

            if result.target_latency_ms is not None:
                lines.append("Performance Targets:")
                lines.append(f"  NPU Target:       {result.target_latency_ms:.2f}ms")
                lines.append(
                    f"  CPU Baseline:     {result.cpu_baseline_latency_ms:.2f}ms (expected)"
                )
                status = "PASS" if result.target_met else "FAIL"
                status_icon = "[OK]" if result.target_met else "[!!]"
                lines.append(
                    f"  CPU Result:       {m.mean_ms:.4f}ms | {status_icon} {status} (vs CPU baseline)"
                )

            lines.append("")

        lines.append("=" * 80)
        lines.append("")
        lines.append("NOTE: These are CPU reference benchmarks.")
        lines.append("NPU hardware benchmarks will be significantly faster.")
        lines.append("Expected NPU speedup: ~10x over CPU baseline.")
        lines.append("=" * 80)

        return "\n".join(lines)

    def format_json_output(self) -> str:
        """Format results as JSON"""
        return json.dumps(self.results.to_dict(), indent=2)

    def format_markdown_output(self) -> str:
        """Format results as Markdown table"""
        lines = []
        lines.append("# IRON Baseline Benchmark Results (CPU Reference)")
        lines.append("")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"**Device:** {self.results.device_info}")
        lines.append("")
        lines.append("## Configuration")
        lines.append("")
        lines.append(f"- **Iterations:** {self.config.iterations}")
        lines.append(f"- **Warmup:** {self.config.warmup}")
        lines.append(f"- **Data Type:** {self.config.dtype}")
        lines.append(f"- **Total Duration:** {self.results.total_duration_sec:.2f}s")
        lines.append("")
        lines.append("## Results Summary")
        lines.append("")
        lines.append(
            "| Operator | Input Shape | Mean (ms) | Median (ms) | "
            "P95 (ms) | P99 (ms) | Throughput (ops/s) | Target |"
        )
        lines.append(
            "|----------|-------------|-----------|-------------|"
            "---------|---------|--------------------|--------|"
        )

        for result in self.results.results:
            if result.error:
                continue

            m = result.metrics
            target_str = (
                f"{result.target_latency_ms:.2f}ms (NPU)"
                if result.target_latency_ms
                else "N/A"
            )
            status = (
                "[OK]"
                if result.target_met
                else "[FAIL]" if result.target_met is not None else ""
            )
            target_str += f" {status}" if status else ""

            shape_str = "x".join(map(str, result.input_shape))

            lines.append(
                f"| {result.operator_name} | {shape_str} | "
                f"{m.mean_ms:.4f} | {m.median_ms:.4f} | "
                f"{m.p95_ms:.4f} | {m.p99_ms:.4f} | "
                f"{m.throughput_ops_sec:.2f} | {target_str} |"
            )

        lines.append("")
        lines.append("## Detailed Statistics")
        lines.append("")

        for result in self.results.results:
            if result.error:
                lines.append(f"### {result.operator_name.upper()}")
                lines.append("")
                lines.append(f"**Error:** {result.error}")
                lines.append("")
                continue

            m = result.metrics
            lines.append(f"### {result.operator_name.upper()}")
            lines.append("")
            lines.append(f"**Input Shape:** {result.input_shape}")
            lines.append("")
            lines.append("| Metric | Value |")
            lines.append("|--------|-------|")
            lines.append(f"| Mean | {m.mean_ms:.4f} ms |")
            lines.append(f"| Median | {m.median_ms:.4f} ms |")
            lines.append(f"| Std Dev | {m.std_dev_ms:.4f} ms |")
            lines.append(f"| P95 | {m.p95_ms:.4f} ms |")
            lines.append(f"| P99 | {m.p99_ms:.4f} ms |")
            lines.append(f"| Min | {m.min_ms:.4f} ms |")
            lines.append(f"| Max | {m.max_ms:.4f} ms |")
            lines.append(f"| Throughput | {m.throughput_ops_sec:.2f} ops/sec |")
            lines.append(f"| Memory Bandwidth | {m.memory_bandwidth_gbps:.4f} GB/s |")

            if result.target_latency_ms is not None:
                status = "PASS" if result.target_met else "FAIL"
                lines.append(f"| NPU Target | {result.target_latency_ms:.2f}ms |")
                lines.append(
                    f"| CPU Baseline | {result.cpu_baseline_latency_ms:.2f}ms |"
                )
                lines.append(f"| CPU Result | {m.mean_ms:.4f}ms - {status} |")

            lines.append("")

        lines.append("")
        lines.append("## Notes")
        lines.append("")
        lines.append(
            "- These benchmarks use **CPU reference implementations** in PyTorch"
        )
        lines.append("- NPU hardware benchmarks are expected to be ~10x faster")
        lines.append("- NPU Target = hardware performance goal")
        lines.append("- CPU Baseline = expected CPU performance (10x NPU target)")
        lines.append("")

        return "\n".join(lines)

    def save_results(self, output_file: str, format: str):
        """Save results to file"""
        if format == "json":
            content = self.format_json_output()
        elif format == "markdown":
            content = self.format_markdown_output()
        else:
            content = self.format_console_output()

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        logger.info(f"Results saved to {output_file}")


def run_benchmark(config: Optional[BenchmarkConfig] = None) -> BenchmarkResults:
    """Convenience function to run benchmarks"""
    if config is None:
        config = BenchmarkConfig()

    runner = BenchmarkRunner(config)
    return runner.run_all_benchmarks()


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="IRON Baseline Benchmark Suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all benchmarks
  python -m iron.benchmarks.baseline_bench

  # Run specific operator
  python -m iron.benchmarks.baseline_bench --operator rope

  # Custom iterations and warmup
  python -m iron.benchmarks.baseline_bench --iterations 100 --warmup 10

  # Output to JSON file
  python -m iron.benchmarks.baseline_bench --output json --output-file results.json

  # Output to Markdown file
  python -m iron.benchmarks.baseline_bench --output markdown --output-file results.md

  # Verbose output
  python -m iron.benchmarks.baseline_bench --verbose
""",
    )

    parser.add_argument(
        "--operator",
        type=str,
        choices=["rope", "rmsnorm", "silu", "softmax"],
        help="Run specific operator (default: run all)",
    )

    parser.add_argument(
        "--iterations",
        type=int,
        default=50,
        help="Number of benchmark iterations (default: 50)",
    )

    parser.add_argument(
        "--warmup",
        type=int,
        default=5,
        help="Number of warmup runs (default: 5)",
    )

    parser.add_argument(
        "--output",
        type=str,
        choices=["console", "json", "markdown"],
        default="console",
        help="Output format (default: console)",
    )

    parser.add_argument(
        "--output-file",
        type=str,
        help="Output file path (default: print to console)",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    parser.add_argument(
        "--device",
        type=str,
        choices=["cpu", "cuda"],
        default="cpu",
        help="Device to run benchmarks on (default: cpu)",
    )

    parser.add_argument(
        "--dtype",
        type=str,
        choices=["bfloat16", "float32"],
        default="bfloat16",
        help="Data type for benchmarks (default: bfloat16)",
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    config = BenchmarkConfig(
        iterations=args.iterations,
        warmup=args.warmup,
        output_format=args.output,
        output_file=args.output_file,
        verbose=args.verbose,
        operator=args.operator,
        device=args.device,
        dtype=args.dtype,
    )

    print("=" * 60)
    print("IRON Baseline Benchmark Suite (CPU Reference)")
    print("=" * 60)
    print(f"Configuration: {args.iterations} iterations, {args.warmup} warmup")
    print(f"Device: {args.device}")
    print(f"Data Type: {args.dtype}")
    print(f"Output format: {args.output}")
    if args.operator:
        print(f"Operator: {args.operator}")
    else:
        print("Operators: rope, rmsnorm, silu, softmax")
    print("=" * 60)
    print()

    runner = BenchmarkRunner(config)
    results = runner.run_all_benchmarks()

    # Output results
    if args.output == "json":
        output = runner.format_json_output()
    elif args.output == "markdown":
        output = runner.format_markdown_output()
    else:
        output = runner.format_console_output()

    if args.output_file:
        runner.save_results(args.output_file, args.output)
        print(f"\nResults saved to: {args.output_file}")
    else:
        print(output)

    # Summary
    print("\n" + "=" * 60)
    print("BENCHMARK COMPLETE")
    print(f"Total duration: {results.total_duration_sec:.2f}s")
    print(f"Device: {results.device_info}")

    # Check targets
    targets_met = sum(1 for r in results.results if r.target_met is True)
    targets_total = sum(1 for r in results.results if r.target_met is not None)

    if targets_total > 0:
        print(f"CPU Baseline targets met: {targets_met}/{targets_total}")

    print("=" * 60)


if __name__ == "__main__":
    main()
