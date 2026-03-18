#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Operator Benchmark Suite

A comprehensive benchmark framework for measuring performance of IRON operators
on AMD Ryzen AI NPUs. Supports RoPE, RMSNorm, SiLU, and Softmax operators.

Features:
- Accurate timing using time.perf_counter()
- Statistical analysis (mean, median, std dev, p95, p99)
- Multiple output formats (console, JSON, Markdown)
- CI/CD integration support
- Target performance comparison

Usage:
    # Run all benchmarks
    python -m iron.benchmarks.run

    # Run specific operator
    python -m iron.benchmarks.run --operator rope

    # Custom iterations
    python -m iron.benchmarks.run --iterations 100 --warmup 10

    # Output to JSON
    python -m iron.benchmarks.run --output json --output-file results.json
"""

import argparse
import json
import logging
import os
import sys
import time
import statistics
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime
import torch
import numpy as np
from ml_dtypes import bfloat16

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from iron.operators.rope.op import AIERope
from iron.operators.rms_norm.op import AIERMSNorm
from iron.operators.silu.op import AIESiLU
from iron.operators.softmax.op import AIESoftmax
from iron.common.aie_context import AIEContext
from iron.common.aie_device_manager import AIEDeviceManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# =============================================================================
# Target Performance Specifications
# =============================================================================


@dataclass
class PerformanceTarget:
    """Target performance specification for an operator"""

    operator_name: str
    input_shape: tuple
    target_latency_ms: float
    description: str


PERFORMANCE_TARGETS = {
    "rope": PerformanceTarget(
        operator_name="rope",
        input_shape=(1, 12, 128, 64),
        target_latency_ms=0.5,
        description="RoPE (Rotary Positional Embedding) for [1, 12, 128, 64]",
    ),
    "rmsnorm": PerformanceTarget(
        operator_name="rmsnorm",
        input_shape=(1, 128, 2048),
        target_latency_ms=1.0,
        description="RMSNorm for [1, 128, 2048]",
    ),
    "silu": PerformanceTarget(
        operator_name="silu",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.3,
        description="SiLU (Sigmoid Linear Unit) for [1, 128, 8192]",
    ),
    "softmax": PerformanceTarget(
        operator_name="softmax",
        input_shape=(1, 12, 128, 128),
        target_latency_ms=2.0,
        description="Softmax for [1, 12, 128, 128]",
    ),
}


# =============================================================================
# Data Classes
# =============================================================================


@dataclass
class BenchmarkConfig:
    """Configuration for benchmark execution"""

    iterations: int = 50
    warmup: int = 10  # Increased for NPU thermal stabilization
    output_format: str = "console"  # console, json, markdown
    output_file: Optional[str] = None
    verbose: bool = False
    operator: Optional[str] = None  # None means run all
    device_id: int = 0

    def __post_init__(self):
        """Validate configuration parameters"""
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
    cpu_utilization_percent: float = 0.0

    # Statistical metrics
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
        # Proper percentile calculation for small sample sizes
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
    timestamp: str = ""
    error: Optional[str] = None

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
                "cpu_utilization_percent": self.metrics.cpu_utilization_percent,
            },
            "target_latency_ms": self.target_latency_ms,
            "target_met": self.target_met,
            "timestamp": self.timestamp,
            "error": self.error,
        }


@dataclass
class BenchmarkResults:
    """Complete benchmark results"""

    results: List[OperatorBenchmarkResult] = field(default_factory=list)
    start_time: str = ""
    end_time: str = ""
    total_duration_sec: float = 0.0
    config: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "results": [r.to_dict() for r in self.results],
            "start_time": self.start_time,
            "end_time": self.end_time,
            "total_duration_sec": self.total_duration_sec,
            "config": self.config,
        }


# =============================================================================
# Operator Benchmark Implementations
# =============================================================================


class OperatorBenchmark:
    """Base class for operator benchmarks"""

    def __init__(self, context: AIEContext, config: BenchmarkConfig):
        self.context = context
        self.config = config
        self.operator = None
        self.input_tensor = None
        self.additional_inputs = {}

    def setup(self):
        """Set up the operator and input tensors"""
        raise NotImplementedError

    def run(self) -> tuple:
        """Run the operator and return (latency_us, input_bytes, output_bytes)"""
        raise NotImplementedError

    def get_input_shape(self) -> tuple:
        """Return the input tensor shape"""
        raise NotImplementedError

    def get_memory_footprint(self) -> tuple:
        """Return (input_bytes, output_bytes)"""
        raise NotImplementedError


class RoPEBenchmark(OperatorBenchmark):
    """Benchmark for RoPE (Rotary Positional Embedding) operator"""

    # Target: <0.5ms for [1, 12, 128, 64]
    # RoPE config: rows=seq_len, cols=head_dim, angle_rows=context_len

    def setup(self):
        # Shape: (batch, heads, seq_len, head_dim) = (1, 12, 128, 64)
        self.batch_size = 1
        self.num_heads = 12
        self.seq_len = 128
        self.head_dim = 64

        # RoPE operates on (seq_len, num_heads, head_dim) internally
        # For the AIE operator: rows=seq_len, cols=num_heads * head_dim
        self.rows = self.seq_len
        self.cols = self.num_heads * self.head_dim
        self.angle_rows = self.seq_len  # Context length

        # AIE configuration
        self.num_aie_columns = 8
        self.method_type = 0  # Two-halves method

        # Create operator
        self.operator = AIERope(
            rows=self.rows,
            cols=self.cols,
            angle_rows=self.angle_rows,
            num_aie_columns=self.num_aie_columns,
            method_type=self.method_type,
            context=self.context,
        )

        # Create input tensor: (batch, seq_len, num_heads * head_dim)
        self.input_tensor = torch.randn(
            self.batch_size, self.rows, self.cols, dtype=torch.bfloat16
        )

        # Create angles tensor
        self.angles = torch.randn(self.angle_rows, self.cols, dtype=torch.bfloat16)

    def run(self) -> tuple:
        """Run RoPE operator and return timing"""
        self.operator.write_buffer("in", self.input_tensor)
        self.operator.write_buffer("angles", self.angles)
        self.operator.run_runlist()
        result = self.operator.read_buffer_as_torch(
            "output", self.input_tensor.shape, dtype=bfloat16
        )
        return result

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.num_heads, self.seq_len, self.head_dim)

    def get_memory_footprint(self) -> tuple:
        # Input: in buffer + angles buffer
        # Output: output buffer
        input_bytes = self.rows * self.cols * 2  # bfloat16 = 2 bytes
        input_bytes += self.angle_rows * self.cols * 2  # angles
        output_bytes = self.rows * self.cols * 2
        return input_bytes, output_bytes


class RMSNormBenchmark(OperatorBenchmark):
    """Benchmark for RMSNorm (Root Mean Square Normalization) operator"""

    # Target: <1ms for [1, 128, 2048]

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 2048)
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 2048
        self.size = self.hidden_dim

        # AIE configuration
        self.num_aie_columns = 8
        self.num_channels = 2
        self.tile_size = 256  # Must be multiple of 16

        # Calculate padded size
        max_multiple = self.num_aie_columns * self.tile_size
        self.padded_size = (
            (self.size + max_multiple - 1) // max_multiple
        ) * max_multiple

        # Create operator
        self.operator = AIERMSNorm(
            size=self.size,
            eps=1e-6,
            num_aie_columns=self.num_aie_columns,
            num_channels=self.num_channels,
            tile_size=self.tile_size,
            weighted=True,
            context=self.context,
        )

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size, self.seq_len, self.hidden_dim, dtype=torch.bfloat16
        )

    def run(self) -> tuple:
        """Run RMSNorm operator and return timing"""
        # Flatten for AIE processing
        x_flat = self.input_tensor.view(-1)
        result = self.operator(x_flat)
        return result

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        # Input: input1 buffer (padded)
        # Output: output buffer (padded)
        input_bytes = self.padded_size * 2  # bfloat16 = 2 bytes
        output_bytes = self.padded_size * 2
        return input_bytes, output_bytes


class SiLUBenchmark(OperatorBenchmark):
    """Benchmark for SiLU (Sigmoid Linear Unit) operator"""

    # Target: <0.3ms for [1, 128, 8192]

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 8192)
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 8192
        self.size = self.hidden_dim

        # AIE configuration
        self.num_aie_columns = 8
        self.num_channels = 2
        self.tile_size = 256  # Must be multiple of 16

        # Calculate padded size
        max_multiple = self.num_aie_columns * self.tile_size
        self.padded_size = (
            (self.size + max_multiple - 1) // max_multiple
        ) * max_multiple

        # Create operator
        self.operator = AIESiLU(
            size=self.size,
            num_aie_columns=self.num_aie_columns,
            num_channels=self.num_channels,
            tile_size=self.tile_size,
            context=self.context,
        )

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size, self.seq_len, self.hidden_dim, dtype=torch.bfloat16
        )

    def run(self) -> tuple:
        """Run SiLU operator and return timing"""
        # Flatten for AIE processing
        x_flat = self.input_tensor.view(-1)
        result = self.operator(x_flat)
        return result

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        input_bytes = self.padded_size * 2  # bfloat16 = 2 bytes
        output_bytes = self.padded_size * 2
        return input_bytes, output_bytes


class SoftmaxBenchmark(OperatorBenchmark):
    """Benchmark for Softmax operator"""

    # Target: <2ms for [1, 12, 128, 128]

    def setup(self):
        # Shape: (batch, heads, seq_len, key_len) = (1, 12, 128, 128)
        self.batch_size = 1
        self.num_heads = 12
        self.seq_len = 128
        self.key_len = 128

        # AIE configuration
        self.num_aie_columns = 8
        self.num_channels = 2
        self.rows = self.seq_len
        self.cols = self.key_len
        self.size = self.rows * self.cols

        # Create operator
        self.operator = AIESoftmax(
            rows=self.rows,
            cols=self.cols,
            num_aie_columns=self.num_aie_columns,
            num_channels=self.num_channels,
            context=self.context,
        )

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size,
            self.num_heads,
            self.seq_len,
            self.key_len,
            dtype=torch.bfloat16,
        )

    def run(self) -> tuple:
        """Run Softmax operator and return timing"""
        # Process each head
        results = []
        for h in range(self.num_heads):
            head_tensor = self.input_tensor[0, h, :, :]
            result = self.operator(head_tensor)
            results.append(result)
        return torch.stack(results, dim=0).unsqueeze(0)

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.num_heads, self.seq_len, self.key_len)

    def get_memory_footprint(self) -> tuple:
        # Input and output per head, multiplied by num_heads
        input_bytes = self.rows * self.cols * 2 * self.num_heads
        output_bytes = self.rows * self.cols * 2 * self.num_heads
        return input_bytes, output_bytes


# =============================================================================
# Benchmark Runner
# =============================================================================


class BenchmarkRunner:
    """Main benchmark runner that orchestrates all benchmarks"""

    OPERATOR_MAP = {
        "rope": RoPEBenchmark,
        "rmsnorm": RMSNormBenchmark,
        "silu": SiLUBenchmark,
        "softmax": SoftmaxBenchmark,
    }

    def __init__(self, config: BenchmarkConfig):
        self.config = config
        self.context = None
        self.results = BenchmarkResults()
        self.device_manager = None

    def setup(self):
        """Initialize AIE context and device"""
        logger.info("Initializing AIE context and device manager...")

        self.device_manager = AIEDeviceManager()
        self.context = AIEContext(device_manager=self.device_manager)

        logger.info(f"AIE context initialized with device ID: {self.config.device_id}")

    def teardown(self):
        """Clean up resources"""
        if self.context:
            logger.info("Cleaning up AIE context...")
            del self.context

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
        )

        try:
            # Create benchmark instance
            benchmark = benchmark_class(self.context, self.config)

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

            # Warmup runs
            logger.info(f"Running {self.config.warmup} warmup iterations...")
            for _ in range(self.config.warmup):
                benchmark.run()

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
                        f"  Iteration {i + 1}/{self.config.iterations}: "
                        f"{latency_ms:.4f} ms"
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

            # Check target
            if result.target_latency_ms is not None:
                result.target_met = result.metrics.mean_ms <= result.target_latency_ms

            # Log results
            status = (
                "PASS"
                if result.target_met
                else "FAIL" if result.target_latency_ms else "N/A"
            )
            logger.info(
                f"{operator_name} benchmark complete: "
                f"mean={result.metrics.mean_ms:.4f}ms, "
                f"target={result.target_latency_ms}ms, "
                f"status={status}"
            )

        except Exception as e:
            logger.error(f"Benchmark failed for {operator_name}: {str(e)}")
            result.error = str(e)
            result.target_met = None  # Explicitly set to None on error
            if self.config.verbose:
                import traceback

                logger.error(traceback.format_exc())

        return result

    def run_all_benchmarks(self) -> BenchmarkResults:
        """Run all operator benchmarks"""
        self.results.start_time = datetime.now().isoformat()
        self.results.config = asdict(self.config)
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
        lines.append("IRON OPERATOR BENCHMARK RESULTS")
        lines.append("=" * 80)
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
                status = "PASS" if result.target_met else "FAIL"
                status_icon = "[OK]" if result.target_met else "[!!]"
                lines.append(
                    f"Target: {result.target_latency_ms:.2f}ms | "
                    f"Actual: {m.mean_ms:.4f}ms | {status_icon} {status}"
                )

            lines.append("")

        lines.append("=" * 80)

        return "\n".join(lines)

    def format_json_output(self) -> str:
        """Format results as JSON"""
        return json.dumps(self.results.to_dict(), indent=2)

    def format_markdown_output(self) -> str:
        """Format results as Markdown table"""
        lines = []
        lines.append("# IRON Operator Benchmark Results")
        lines.append("")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        lines.append("## Configuration")
        lines.append("")
        lines.append(f"- **Iterations:** {self.config.iterations}")
        lines.append(f"- **Warmup:** {self.config.warmup}")
        lines.append(f"- **Total Duration:** {self.results.total_duration_sec:.2f}s")
        lines.append("")
        lines.append("## Results Summary")
        lines.append("")
        lines.append(
            "| Operator | Input Shape | Mean (ms) | Median (ms) | "
            "P95 (ms) | P99 (ms) | Throughput (ops/s) | Bandwidth (GB/s) | Target |"
        )
        lines.append(
            "|----------|-------------|-----------|-------------|"
            "---------|---------|--------------------|------------------|--------|"
        )

        for result in self.results.results:
            if result.error:
                continue

            m = result.metrics
            target_str = (
                f"{result.target_latency_ms:.2f}ms"
                if result.target_latency_ms
                else "N/A"
            )
            if result.target_met is not None:
                target_str += " [OK]" if result.target_met else " [FAIL]"

            shape_str = "x".join(map(str, result.input_shape))

            lines.append(
                f"| {result.operator_name} | {shape_str} | "
                f"{m.mean_ms:.4f} | {m.median_ms:.4f} | "
                f"{m.p95_ms:.4f} | {m.p99_ms:.4f} | "
                f"{m.throughput_ops_sec:.2f} | {m.memory_bandwidth_gbps:.4f} | "
                f"{target_str} |"
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
                lines.append(
                    f"| Target | {result.target_latency_ms:.2f}ms - {status} |"
                )

            lines.append("")

        lines.append("## Legend")
        lines.append("")
        lines.append("- **Mean**: Average latency across all iterations")
        lines.append("- **Median**: Middle value when latencies are sorted")
        lines.append("- **Std Dev**: Standard deviation of latencies")
        lines.append("- **P95**: 95th percentile latency")
        lines.append("- **P99**: 99th percentile latency")
        lines.append("- **Target**: Performance target (if available)")
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

        with open(output_file, "w") as f:
            f.write(content)

        logger.info(f"Results saved to {output_file}")


def run_benchmark(config: Optional[BenchmarkConfig] = None) -> BenchmarkResults:
    """Convenience function to run benchmarks"""
    if config is None:
        config = BenchmarkConfig()

    runner = BenchmarkRunner(config)
    runner.setup()

    try:
        results = runner.run_all_benchmarks()
        return results
    finally:
        runner.teardown()


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="IRON Operator Benchmark Suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all benchmarks
  python -m iron.benchmarks.run

  # Run specific operator
  python -m iron.benchmarks.run --operator rope

  # Custom iterations and warmup
  python -m iron.benchmarks.run --iterations 100 --warmup 10

  # Output to JSON file
  python -m iron.benchmarks.run --output json --output-file results.json

  # Output to Markdown file
  python -m iron.benchmarks.run --output markdown --output-file results.md

  # Verbose output
  python -m iron.benchmarks.run --verbose
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
        "--device-id",
        type=int,
        default=0,
        help="AIE device ID (default: 0)",
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
        device_id=args.device_id,
    )

    print("=" * 60)
    print("IRON Operator Benchmark Suite")
    print("=" * 60)
    print(f"Configuration: {args.iterations} iterations, {args.warmup} warmup")
    print(f"Output format: {args.output}")
    if args.operator:
        print(f"Operator: {args.operator}")
    else:
        print("Operators: rope, rmsnorm, silu, softmax")
    print("=" * 60)
    print()

    runner = BenchmarkRunner(config)
    runner.setup()

    try:
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

        # Check targets
        targets_met = sum(1 for r in results.results if r.target_met is True)
        targets_total = sum(
            1 for r in results.results if r.target_latency_ms is not None
        )

        if targets_total > 0:
            print(f"Targets met: {targets_met}/{targets_total}")

        print("=" * 60)

    except Exception as e:
        logger.error(f"Benchmark failed: {str(e)}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)
    finally:
        runner.teardown()


if __name__ == "__main__":
    main()
