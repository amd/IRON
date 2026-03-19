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


# =============================================================================
# Tile Size Scaling Study Configuration
# =============================================================================


TILE_SIZE_PRESETS = {
    "standard": [128, 256, 512, 1024, 2048],
    "fine_grained": [64, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048],
    "coarse": [256, 512, 1024, 2048],
    "memory_bounded": [512, 1024, 2048, 4096],
    "compute_bounded": [64, 128, 256, 512],
}


# =============================================================================
# Column Configuration Study Configuration (P3-7)
# =============================================================================


COLUMN_CONFIG_PRESETS = {
    "standard": [1, 2, 4, 8],
    "fine_grained": [1, 2, 3, 4, 6, 8],
    "coarse": [1, 4, 8],
    "power_of_two": [1, 2, 4, 8, 16],
    "scaling_study": [1, 2, 4, 8],
}


OPERATOR_COLUMN_RECOMMENDATIONS = {
    # GEMM operators - benefit from column parallelism
    "gemm": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Standard GEMM - 4 columns optimal for most shapes",
    },
    "gemm_km_large": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "K>>M pattern - 4 columns for load balancing",
    },
    "gemm_mk_large": {
        "recommended": 8,
        "min": 1,
        "max": 16,
        "note": "M>>K pattern - 8 columns for row parallelism",
    },
    "gemm_square": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Square matrices - 4 columns balanced",
    },
    "gemm_small": {
        "recommended": 2,
        "min": 1,
        "max": 4,
        "note": "Small matrices - fewer columns reduce overhead",
    },
    # GEMV operators - vector-matrix multiplication
    "gemv": {
        "recommended": 2,
        "min": 1,
        "max": 4,
        "note": "GEMV - limited parallelism, 2 columns typical",
    },
    "gemv_m_large": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "M>>K GEMV - more columns for row parallelism",
    },
    "gemv_k_large": {
        "recommended": 2,
        "min": 1,
        "max": 4,
        "note": "K>>M GEMV - fewer columns, reduction-heavy",
    },
    # Normalization operators - memory-bound
    "rmsnorm": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "RMSNorm - 4 columns for memory parallelism",
    },
    "layer_norm": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "LayerNorm - similar to RMSNorm",
    },
    "batch_norm": {
        "recommended": 2,
        "min": 1,
        "max": 4,
        "note": "BatchNorm - channel-wise, fewer columns",
    },
    # Elementwise operators - highly memory-bound
    "elementwise_add": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Simple addition - 4 columns efficient",
    },
    "elementwise_mul": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Simple multiplication - 4 columns efficient",
    },
    "axpy": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Fused multiply-add - 4 columns for streaming",
    },
    # Activation functions - memory-bound with compute
    "silu": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "SiLU - moderate compute, 4 columns",
    },
    "gelu": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "GELU - moderate compute, 4 columns",
    },
    "relu": {
        "recommended": 8,
        "min": 1,
        "max": 16,
        "note": "ReLU - simple, more columns for throughput",
    },
    "sigmoid": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Sigmoid - transcendental, 4 columns",
    },
    "tanh": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Tanh - transcendental, 4 columns",
    },
    "leaky_relu": {
        "recommended": 8,
        "min": 1,
        "max": 16,
        "note": "Leaky ReLU - simple, more columns",
    },
    "softmax": {
        "recommended": 2,
        "min": 1,
        "max": 4,
        "note": "Softmax - reduction operation, fewer columns",
    },
    # Attention operators
    "rope": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "RoPE - element-wise rotation, 4 columns",
    },
    "attention": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Self-attention - compute + memory, 4 columns",
    },
    # Convolution operators
    "conv2d": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "2D Conv - spatial + channel parallelism",
    },
    "conv3d": {
        "recommended": 2,
        "min": 1,
        "max": 4,
        "note": "3D Conv - memory intensive, fewer columns",
    },
    "conv1d": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "1D Conv - simpler, 4 columns",
    },
    # Pooling operators
    "maxpool": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "MaxPool - window reduction, 4 columns",
    },
    "avgpool": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "AvgPool - window reduction, 4 columns",
    },
    # Other operators
    "reduction": {
        "recommended": 2,
        "min": 1,
        "max": 4,
        "note": "Reduction - sequential, fewer columns",
    },
    "transpose": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Transpose - memory reordering, 4 columns",
    },
    "concat": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Concatenation - 4 columns for bandwidth",
    },
    "split": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Split - inverse of concat, 4 columns",
    },
    # Default for unknown operators
    "default": {
        "recommended": 4,
        "min": 1,
        "max": 8,
        "note": "Default column configuration",
    },
}


OPERATOR_TILE_SIZE_RECOMMENDATIONS = {
    # GEMM operators - compute-bound, benefit from larger tiles
    "gemm": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Balance compute utilization and memory",
    },
    "gemm_km_large": {
        "recommended": 256,
        "min": 64,
        "max": 512,
        "note": "K>>M pattern favors smaller tiles",
    },
    "gemm_mk_large": {
        "recommended": 1024,
        "min": 256,
        "max": 2048,
        "note": "M>>K pattern benefits from larger tiles",
    },
    "gemm_square": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Square matrices optimal at mid-range tiles",
    },
    "gemm_small": {
        "recommended": 64,
        "min": 32,
        "max": 128,
        "note": "Small matrices need smaller tiles",
    },
    # Normalization operators - memory-bound
    "rmsnorm": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Memory-bound, smaller tiles reduce cache pressure",
    },
    "layer_norm": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Similar to RMSNorm, memory-bound",
    },
    # Elementwise operators - highly memory-bound
    "elementwise_add": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Simple ops benefit from larger contiguous access",
    },
    "elementwise_mul": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Simple ops benefit from larger contiguous access",
    },
    "axpy": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Fused multiply-add, larger tiles efficient",
    },
    # Activation functions - memory-bound with compute
    "silu": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Moderate compute, larger tiles OK",
    },
    "gelu": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Moderate compute, larger tiles OK",
    },
    "relu": {
        "recommended": 1024,
        "min": 256,
        "max": 2048,
        "note": "Simple activation, maximize throughput",
    },
    "sigmoid": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Transcendental, balance compute/memory",
    },
    "tanh": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Transcendental, balance compute/memory",
    },
    "leaky_relu": {
        "recommended": 1024,
        "min": 256,
        "max": 2048,
        "note": "Simple activation, maximize throughput",
    },
    # Attention operators
    "rope": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Complex indexing, moderate tile sizes",
    },
    "softmax": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Reduction operation, cache-sensitive",
    },
    # Convolution operators - compute-bound with spatial locality
    "conv2d": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Spatial locality important",
    },
    "conv3d": {
        "recommended": 128,
        "min": 64,
        "max": 256,
        "note": "3D convolutions need smaller tiles for cache",
    },
    # Pooling operators
    "maxpool": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Window-based, moderate tiles",
    },
    "avgpool": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Window-based, moderate tiles",
    },
    # Other operators
    "reduction": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Reduction patterns favor moderate tiles",
    },
    "transpose": {
        "recommended": 512,
        "min": 128,
        "max": 1024,
        "note": "Memory reordering, larger tiles help",
    },
    # Default for unknown operators
    "default": {
        "recommended": 256,
        "min": 128,
        "max": 512,
        "note": "Default tile size recommendation",
    },
}


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
    # P1 Group G - Maxpool/Reduction Metrics Infrastructure
    "maxpool": PerformanceTarget(
        operator_name="maxpool",
        input_shape=(1, 16, 32, 32),
        target_latency_ms=0.8,
        description="MaxPool2d 2x2 kernel for [1, 16, 32, 32]",
        cpu_baseline_factor=10.0,
    ),
    "reduction": PerformanceTarget(
        operator_name="reduction",
        input_shape=(64, 64),
        target_latency_ms=0.4,
        description="Reduction (sum/max/min) for [64, 64] along last dim",
        cpu_baseline_factor=10.0,
    ),
    # P3-1 Benchmark Expansion - Priority 1 Operators
    "gelu": PerformanceTarget(
        operator_name="gelu",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.3,
        description="GELU (Gaussian Error Linear Unit) for [1, 128, 8192]",
        cpu_baseline_factor=10.0,
    ),
    "layer_norm": PerformanceTarget(
        operator_name="layer_norm",
        input_shape=(1, 128, 2048),
        target_latency_ms=1.0,
        description="LayerNorm for [1, 128, 2048]",
        cpu_baseline_factor=10.0,
    ),
    "gemm": PerformanceTarget(
        operator_name="gemm",
        input_shape=((64, 128), (128, 256)),
        target_latency_ms=0.5,
        description="GEMM (64,128) x (128,256) matrix multiplication",
        cpu_baseline_factor=10.0,
    ),
    "gemm_km_large": PerformanceTarget(
        operator_name="gemm_km_large",
        input_shape=((32, 4096), (4096, 256)),
        target_latency_ms=0.8,
        description="GEMM K>>M (32,4096) x (4096,256) matrix multiplication - optimal 4 columns",
        cpu_baseline_factor=10.0,
    ),
    "gemm_mk_large": PerformanceTarget(
        operator_name="gemm_mk_large",
        input_shape=((4096, 32), (32, 256)),
        target_latency_ms=0.8,
        description="GEMM M>>K (4096,32) x (32,256) matrix multiplication - optimal 8 columns",
        cpu_baseline_factor=10.0,
    ),
    "gemm_square": PerformanceTarget(
        operator_name="gemm_square",
        input_shape=((512, 512), (512, 512)),
        target_latency_ms=0.6,
        description="GEMM square (512,512) x (512,512) matrix multiplication",
        cpu_baseline_factor=10.0,
    ),
    "gemm_small": PerformanceTarget(
        operator_name="gemm_small",
        input_shape=((16, 16), (16, 16)),
        target_latency_ms=0.2,
        description="GEMM small (16,16) x (16,16) matrix multiplication",
        cpu_baseline_factor=10.0,
    ),
    "transpose": PerformanceTarget(
        operator_name="transpose",
        input_shape=(1, 128, 2048),
        target_latency_ms=0.2,
        description="Tensor transpose for [1, 128, 2048]",
        cpu_baseline_factor=10.0,
    ),
    "avgpool": PerformanceTarget(
        operator_name="avgpool",
        input_shape=(1, 16, 32, 32),
        target_latency_ms=0.8,
        description="AvgPool2d 2x2 kernel for [1, 16, 32, 32]",
        cpu_baseline_factor=10.0,
    ),
    # P3-3 Convolution Operator Benchmarks
    "conv2d": PerformanceTarget(
        operator_name="conv2d",
        input_shape=(1, 3, 32, 32),
        target_latency_ms=1.0,
        description="Conv2d (16,3,3,3) kernel for [1, 3, 32, 32]",
        cpu_baseline_factor=10.0,
    ),
    "conv3d": PerformanceTarget(
        operator_name="conv3d",
        input_shape=(1, 3, 16, 16, 16),
        target_latency_ms=1.5,
        description="Conv3d (8,3,3,3,3) kernel for [1, 3, 16, 16, 16]",
        cpu_baseline_factor=10.0,
    ),
    # P3-4 Activation Function Benchmarks
    "relu": PerformanceTarget(
        operator_name="relu",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.3,
        description="ReLU (Rectified Linear Unit) for [1, 128, 8192]",
        cpu_baseline_factor=10.0,
    ),
    "sigmoid": PerformanceTarget(
        operator_name="sigmoid",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.3,
        description="Sigmoid activation for [1, 128, 8192]",
        cpu_baseline_factor=10.0,
    ),
    "tanh": PerformanceTarget(
        operator_name="tanh",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.3,
        description="Tanh (Hyperbolic Tangent) activation for [1, 128, 8192]",
        cpu_baseline_factor=10.0,
    ),
    "leaky_relu": PerformanceTarget(
        operator_name="leaky_relu",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.3,
        description="Leaky ReLU (negative_slope=0.01) for [1, 128, 8192]",
        cpu_baseline_factor=10.0,
    ),
    # P3-5 Elementwise Operations Benchmarks
    "elementwise_add": PerformanceTarget(
        operator_name="elementwise_add",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.2,
        description="Elementwise tensor addition (A + B) for [1, 128, 8192]",
        cpu_baseline_factor=10.0,
    ),
    "elementwise_mul": PerformanceTarget(
        operator_name="elementwise_mul",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.2,
        description="Elementwise tensor multiplication (A * B) for [1, 128, 8192]",
        cpu_baseline_factor=10.0,
    ),
    "axpy": PerformanceTarget(
        operator_name="axpy",
        input_shape=(1, 128, 8192),
        target_latency_ms=0.2,
        description="AXPY operation (Y = a*X + Y) for [1, 128, 8192]",
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
    # Tile Size Scaling Study configuration
    tile_sizes: Optional[List[int]] = None
    enable_tile_size_study: bool = False
    # Column Configuration Study configuration (P3-7)
    num_columns: Optional[int] = None
    column_preset: Optional[str] = None
    enable_column_study: bool = False

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
# Tile Size Scaling Study Data Classes
# =============================================================================


@dataclass
class TileSizeScalingResult:
    """Results for a single tile size configuration"""

    tile_size: int
    mean_latency_ms: float
    median_latency_ms: float
    std_dev_ms: float
    p95_ms: float
    p99_ms: float
    min_ms: float
    max_ms: float
    throughput_ops_sec: float
    memory_bandwidth_gbps: float
    iterations: int
    timestamp: str = ""

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "tile_size": self.tile_size,
            "mean_latency_ms": self.mean_latency_ms,
            "median_latency_ms": self.median_latency_ms,
            "std_dev_ms": self.std_dev_ms,
            "p95_ms": self.p95_ms,
            "p99_ms": self.p99_ms,
            "min_ms": self.min_ms,
            "max_ms": self.max_ms,
            "throughput_ops_sec": self.throughput_ops_sec,
            "memory_bandwidth_gbps": self.memory_bandwidth_gbps,
            "iterations": self.iterations,
            "timestamp": self.timestamp,
        }


@dataclass
class TileSizeScalingReport:
    """Complete tile size scaling study report"""

    operator_name: str
    input_shape: tuple
    tile_size_results: List[TileSizeScalingResult] = field(default_factory=list)
    optimal_tile_size: Optional[int] = None
    optimal_latency_ms: Optional[float] = None
    worst_tile_size: Optional[int] = None
    worst_latency_ms: Optional[float] = None
    scaling_efficiency: float = 0.0  # Ratio of best to worst performance
    recommendation: Optional[str] = None
    start_time: str = ""
    end_time: str = ""
    total_duration_sec: float = 0.0

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "operator_name": self.operator_name,
            "input_shape": list(self.input_shape) if self.input_shape else [],
            "tile_size_results": [r.to_dict() for r in self.tile_size_results],
            "optimal_tile_size": self.optimal_tile_size,
            "optimal_latency_ms": self.optimal_latency_ms,
            "worst_tile_size": self.worst_tile_size,
            "worst_latency_ms": self.worst_latency_ms,
            "scaling_efficiency": self.scaling_efficiency,
            "recommendation": self.recommendation,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "total_duration_sec": self.total_duration_sec,
        }


# =============================================================================
# Column Configuration Study Data Classes (P3-7)
# =============================================================================


@dataclass
class ColumnScalingResult:
    """Results for a single column configuration"""

    num_columns: int
    mean_latency_ms: float
    median_latency_ms: float
    std_dev_ms: float
    p95_ms: float
    p99_ms: float
    min_ms: float
    max_ms: float
    throughput_ops_sec: float
    memory_bandwidth_gbps: float
    iterations: int
    timestamp: str = ""

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "num_columns": self.num_columns,
            "mean_latency_ms": self.mean_latency_ms,
            "median_latency_ms": self.median_latency_ms,
            "std_dev_ms": self.std_dev_ms,
            "p95_ms": self.p95_ms,
            "p99_ms": self.p99_ms,
            "min_ms": self.min_ms,
            "max_ms": self.max_ms,
            "throughput_ops_sec": self.throughput_ops_sec,
            "memory_bandwidth_gbps": self.memory_bandwidth_gbps,
            "iterations": self.iterations,
            "timestamp": self.timestamp,
        }


@dataclass
class ColumnScalingReport:
    """Complete column scaling study report"""

    operator_name: str
    input_shape: tuple
    column_results: List[ColumnScalingResult] = field(default_factory=list)
    optimal_num_columns: Optional[int] = None
    optimal_latency_ms: Optional[float] = None
    worst_num_columns: Optional[int] = None
    worst_latency_ms: Optional[float] = None
    scaling_efficiency: float = 0.0  # Ratio of best to worst performance
    column_efficiency: float = 0.0  # How well columns scale (1.0 = linear)
    recommendation: Optional[str] = None
    start_time: str = ""
    end_time: str = ""
    total_duration_sec: float = 0.0

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "operator_name": self.operator_name,
            "input_shape": list(self.input_shape) if self.input_shape else [],
            "column_results": [r.to_dict() for r in self.column_results],
            "optimal_num_columns": self.optimal_num_columns,
            "optimal_latency_ms": self.optimal_latency_ms,
            "worst_num_columns": self.worst_num_columns,
            "worst_latency_ms": self.worst_latency_ms,
            "scaling_efficiency": self.scaling_efficiency,
            "column_efficiency": self.column_efficiency,
            "recommendation": self.recommendation,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "total_duration_sec": self.total_duration_sec,
        }


# =============================================================================
# Tile Size Scaling Study Analyzer
# =============================================================================


class TileSizeScalingAnalyzer:
    """Analyzer for tile size scaling study results"""

    def __init__(self, operator_name: str, input_shape: tuple):
        self.operator_name = operator_name
        self.input_shape = input_shape
        self.results: List[TileSizeScalingResult] = []

    def compute_optimal_tile_size(
        self, metric: str = "mean_latency_ms", lower_is_better: bool = True
    ) -> tuple:
        """
        Compute the optimal tile size based on the specified metric.

        Args:
            metric: The metric to optimize (default: mean_latency_ms)
            lower_is_better: If True, find minimum; if False, find maximum

        Returns:
            Tuple of (tile_size, metric_value) or (None, None) if no results
        """
        if not self.results:
            return None, None

        def get_value(r: TileSizeScalingResult) -> float:
            return getattr(r, metric, r.mean_latency_ms)

        if lower_is_better:
            best_result = min(self.results, key=get_value)
        else:
            best_result = max(self.results, key=get_value)

        return best_result.tile_size, get_value(best_result)

    def compute_scaling_efficiency(self) -> float:
        """
        Compute scaling efficiency as ratio of best to worst performance.

        Returns:
            Efficiency ratio (values > 1.0 indicate scaling benefit)
        """
        if len(self.results) < 2:
            return 1.0

        latencies = [r.mean_latency_ms for r in self.results]
        min_latency = min(latencies)
        max_latency = max(latencies)

        if max_latency == 0:
            return 1.0

        # Efficiency = how much faster is the best vs worst
        return max_latency / min_latency if min_latency > 0 else 1.0

    def generate_recommendations(self) -> str:
        """
        Generate tile size recommendations based on analysis.

        Returns:
            Recommendation string
        """
        if not self.results:
            return "No data available for recommendations"

        # Get operator-specific recommendation if available
        op_recommendation = OPERATOR_TILE_SIZE_RECOMMENDATIONS.get(
            self.operator_name, OPERATOR_TILE_SIZE_RECOMMENDATIONS.get("default", {})
        )

        optimal_tile, optimal_latency = self.compute_optimal_tile_size()
        worst_tile, worst_latency = self.compute_optimal_tile_size(
            lower_is_better=False
        )
        efficiency = self.compute_scaling_efficiency()

        if len(self.results) < 2:
            return f"Insufficient data. Use recommended tile size: {op_recommendation.get('recommended', 256)}"

        recommendations = []
        recommendations.append(
            f"Optimal tile size: {optimal_tile} ({optimal_latency:.4f} ms)"
        )
        recommendations.append(
            f"Worst tile size: {worst_tile} ({worst_latency:.4f} ms)"
        )
        recommendations.append(f"Scaling efficiency: {efficiency:.2f}x")

        if efficiency > 1.5:
            recommendations.append(
                f"NOTE: Significant performance variation ({efficiency:.2f}x) across tile sizes."
            )
            recommendations.append(
                f"Recommended to use tile size {optimal_tile} for this operator."
            )
        elif efficiency > 1.1:
            recommendations.append(
                f"NOTE: Moderate performance variation ({efficiency:.2f}x) across tile sizes."
            )
        else:
            recommendations.append(
                f"NOTE: Minimal performance variation ({efficiency:.2f}x). Tile size has limited impact."
            )

        if op_recommendation.get("note"):
            recommendations.append(
                f"Operator-specific note: {op_recommendation['note']}"
            )

        return "; ".join(recommendations)

    def generate_report(self) -> TileSizeScalingReport:
        """
        Generate a complete tile size scaling report.

        Returns:
            TileSizeScalingReport with analysis results
        """
        optimal_tile, optimal_latency = self.compute_optimal_tile_size()
        worst_tile, worst_latency = self.compute_optimal_tile_size(
            lower_is_better=False
        )

        return TileSizeScalingReport(
            operator_name=self.operator_name,
            input_shape=self.input_shape,
            tile_size_results=self.results.copy(),
            optimal_tile_size=optimal_tile,
            optimal_latency_ms=optimal_latency,
            worst_tile_size=worst_tile,
            worst_latency_ms=worst_latency,
            scaling_efficiency=self.compute_scaling_efficiency(),
            recommendation=self.generate_recommendations(),
        )

    def add_result(self, result: TileSizeScalingResult):
        """Add a tile size scaling result to the analyzer"""
        self.results.append(result)


# =============================================================================
# Column Configuration Study Analyzer (P3-7)
# =============================================================================


class ColumnScalingAnalyzer:
    """Analyzer for column scaling study results"""

    def __init__(self, operator_name: str, input_shape: tuple):
        self.operator_name = operator_name
        self.input_shape = input_shape
        self.results: List[ColumnScalingResult] = []

    def compute_optimal_num_columns(
        self, metric: str = "mean_latency_ms", lower_is_better: bool = True
    ) -> tuple:
        """
        Compute the optimal number of columns based on the specified metric.

        Args:
            metric: The metric to optimize (default: mean_latency_ms)
            lower_is_better: If True, find minimum; if False, find maximum

        Returns:
            Tuple of (num_columns, metric_value) or (None, None) if no results
        """
        if not self.results:
            return None, None

        def get_value(r: ColumnScalingResult) -> float:
            return getattr(r, metric, r.mean_latency_ms)

        if lower_is_better:
            best_result = min(self.results, key=get_value)
        else:
            best_result = max(self.results, key=get_value)

        return best_result.num_columns, get_value(best_result)

    def compute_scaling_efficiency(self) -> float:
        """
        Compute scaling efficiency as ratio of best to worst performance.

        Returns:
            Efficiency ratio (values > 1.0 indicate scaling benefit)
        """
        if len(self.results) < 2:
            return 1.0

        latencies = [r.mean_latency_ms for r in self.results]
        min_latency = min(latencies)
        max_latency = max(latencies)

        if max_latency == 0:
            return 1.0

        # Efficiency = how much faster is the best vs worst
        return max_latency / min_latency if min_latency > 0 else 1.0

    def compute_column_efficiency(self) -> float:
        """
        Compute column efficiency as how well performance scales with columns.

        Returns:
            Column efficiency ratio (1.0 = perfect linear scaling)
        """
        if len(self.results) < 2:
            return 1.0

        # Get results sorted by num_columns
        sorted_results = sorted(self.results, key=lambda r: r.num_columns)
        min_cols = sorted_results[0].num_columns
        max_cols = sorted_results[-1].num_columns
        min_latency = sorted_results[0].mean_latency_ms
        max_latency = sorted_results[-1].mean_latency_ms

        if min_cols == max_cols or min_latency == 0:
            return 1.0

        # Ideal: latency should decrease linearly with more columns
        # column_efficiency = (latency_improvement) / (column_increase)
        latency_improvement = (max_latency - min_latency) / max_latency
        column_increase = (max_cols - min_cols) / max_cols

        if column_increase == 0:
            return 1.0

        return (
            min(latency_improvement / column_increase, 1.0)
            if column_increase > 0
            else 1.0
        )

    def generate_recommendations(self) -> str:
        """
        Generate column configuration recommendations based on analysis.

        Returns:
            Recommendation string
        """
        if not self.results:
            return "No data available for recommendations"

        # Get operator-specific recommendation if available
        op_recommendation = OPERATOR_COLUMN_RECOMMENDATIONS.get(
            self.operator_name, OPERATOR_COLUMN_RECOMMENDATIONS.get("default", {})
        )

        optimal_cols, optimal_latency = self.compute_optimal_num_columns()
        worst_cols, worst_latency = self.compute_optimal_num_columns(
            lower_is_better=False
        )
        scaling_eff = self.compute_scaling_efficiency()
        column_eff = self.compute_column_efficiency()

        if len(self.results) < 2:
            return f"Insufficient data. Use recommended columns: {op_recommendation.get('recommended', 4)}"

        recommendations = []
        recommendations.append(
            f"Optimal columns: {optimal_cols} ({optimal_latency:.4f} ms)"
        )
        recommendations.append(f"Worst columns: {worst_cols} ({worst_latency:.4f} ms)")
        recommendations.append(f"Scaling efficiency: {scaling_eff:.2f}x")
        recommendations.append(f"Column efficiency: {column_eff:.2f}")

        if scaling_eff > 1.5:
            recommendations.append(
                f"NOTE: Significant performance variation ({scaling_eff:.2f}x) across column configs."
            )
            recommendations.append(
                f"Recommended to use {optimal_cols} columns for this operator."
            )
        elif scaling_eff > 1.1:
            recommendations.append(
                f"NOTE: Moderate performance variation ({scaling_eff:.2f}x) across column configs."
            )
        else:
            recommendations.append(
                f"NOTE: Minimal performance variation ({scaling_eff:.2f}x). Column count has limited impact."
            )

        if column_eff > 0.8:
            recommendations.append(
                "Good column scaling - parallelization is effective."
            )
        elif column_eff > 0.5:
            recommendations.append(
                "Moderate column scaling - some overhead from parallelization."
            )
        else:
            recommendations.append(
                "Poor column scaling - parallelization overhead dominates."
            )

        if op_recommendation.get("note"):
            recommendations.append(
                f"Operator-specific note: {op_recommendation['note']}"
            )

        return "; ".join(recommendations)

    def generate_report(self) -> ColumnScalingReport:
        """
        Generate a complete column scaling study report.

        Returns:
            ColumnScalingReport with analysis results
        """
        optimal_cols, optimal_latency = self.compute_optimal_num_columns()
        worst_cols, worst_latency = self.compute_optimal_num_columns(
            lower_is_better=False
        )

        return ColumnScalingReport(
            operator_name=self.operator_name,
            input_shape=self.input_shape,
            column_results=self.results.copy(),
            optimal_num_columns=optimal_cols,
            optimal_latency_ms=optimal_latency,
            worst_num_columns=worst_cols,
            worst_latency_ms=worst_latency,
            scaling_efficiency=self.compute_scaling_efficiency(),
            column_efficiency=self.compute_column_efficiency(),
            recommendation=self.generate_recommendations(),
        )

    def add_result(self, result: ColumnScalingResult):
        """Add a column scaling result to the analyzer"""
        self.results.append(result)


def parse_tile_sizes_argument(arg: str) -> List[int]:
    """
    Parse tile sizes argument from command line.

    Supports two formats:
    1. Preset name: "standard", "fine_grained", "coarse", "memory_bounded", "compute_bounded"
    2. Comma-separated values: "128,256,512" or "128, 256, 512"

    Args:
        arg: String argument specifying tile sizes

    Returns:
        List of tile sizes as integers

    Raises:
        ValueError: If the argument is invalid
    """
    arg = arg.strip()

    # Check if it's a preset name
    if arg in TILE_SIZE_PRESETS:
        return TILE_SIZE_PRESETS[arg].copy()

    # Try to parse as comma-separated values
    try:
        tile_sizes = [int(x.strip()) for x in arg.split(",")]
        if not tile_sizes:
            raise ValueError("Empty tile sizes list")
        if any(ts <= 0 for ts in tile_sizes):
            raise ValueError("Tile sizes must be positive integers")
        return tile_sizes
    except ValueError as e:
        raise ValueError(
            f"Invalid tile sizes argument: '{arg}'. "
            f"Must be a preset name ({', '.join(TILE_SIZE_PRESETS.keys())}) "
            f"or comma-separated positive integers."
        ) from e


def parse_column_count_argument(arg: str) -> List[int]:
    """
    Parse column count argument from command line.

    Supports two formats:
    1. Preset name: "standard", "fine_grained", "coarse", "power_of_two", "scaling_study"
    2. Comma-separated values: "1,2,4,8" or "1, 2, 4, 8"

    Args:
        arg: String argument specifying column counts

    Returns:
        List of column counts as integers

    Raises:
        ValueError: If the argument is invalid
    """
    arg = arg.strip()

    # Check if it's a preset name
    if arg in COLUMN_CONFIG_PRESETS:
        return COLUMN_CONFIG_PRESETS[arg].copy()

    # Try to parse as comma-separated values
    try:
        column_counts = [int(x.strip()) for x in arg.split(",")]
        if not column_counts:
            raise ValueError("Empty column counts list")
        if any(cc <= 0 for cc in column_counts):
            raise ValueError("Column counts must be positive integers")
        return column_counts
    except ValueError as e:
        raise ValueError(
            f"Invalid column count argument: '{arg}'. "
            f"Must be a preset name ({', '.join(COLUMN_CONFIG_PRESETS.keys())}) "
            f"or comma-separated positive integers."
        ) from e


# =============================================================================
# Reference Operator Implementations (Optimized CPU/PyTorch)
# =============================================================================


class OperatorBenchmark:
    """Base class for operator benchmarks"""

    COLUMN_PRESETS = COLUMN_CONFIG_PRESETS

    def __init__(
        self,
        config: BenchmarkConfig,
        tile_size: Optional[int] = None,
        num_columns: Optional[int] = None,
    ):
        self.config = config
        self.device = torch.device(config.device)
        self.input_tensor = None
        self.dtype = torch.bfloat16 if config.dtype == "bfloat16" else torch.float32
        self._tile_size = tile_size
        self._num_columns = num_columns

    @property
    def effective_tile_size(self) -> Optional[int]:
        """Get the effective tile size (explicit or default)"""
        return (
            self._tile_size if self._tile_size is not None else self._default_tile_size
        )

    @property
    def effective_num_columns(self) -> Optional[int]:
        """Get the effective number of columns (explicit or default)"""
        return (
            self._num_columns
            if self._num_columns is not None
            else self._default_num_columns
        )

    @property
    def _default_tile_size(self) -> int:
        """Default tile size for operators without specific recommendations"""
        return 256

    @property
    def _default_num_columns(self) -> int:
        """Default number of columns for operators without specific recommendations"""
        return 4

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

    @property
    def _default_tile_size(self) -> int:
        """RMSNorm is memory-bound, smaller tiles reduce cache pressure"""
        return 256

    @property
    def _default_num_columns(self) -> int:
        """RMSNorm - 4 columns for memory parallelism"""
        return 4

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


class MaxPoolBenchmark(OperatorBenchmark):
    """Benchmark for MaxPool2d operator"""

    def setup(self):
        self.batch_size = 1
        self.channels = 16
        self.height = 32
        self.width = 32
        self.kernel_size = 2
        self.stride = 2
        self.padding = 0

        self.input_tensor = torch.randn(
            self.batch_size,
            self.channels,
            self.height,
            self.width,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        return torch.nn.functional.max_pool2d(
            self.input_tensor,
            kernel_size=self.kernel_size,
            stride=self.stride,
            padding=self.padding,
        )

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.channels, self.height, self.width)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_elements = self.batch_size * self.channels * self.height * self.width
        output_elements = input_elements // 4  # 2x2 kernel reduces to 1/4
        return input_elements * bytes_per_element, output_elements * bytes_per_element


class ReductionBenchmark(OperatorBenchmark):
    """Benchmark for Reduction operator"""

    def setup(self):
        self.output_dim = 64
        self.reduction_dim = 64
        self.input_tensor = torch.randn(
            self.output_dim,
            self.reduction_dim,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        return torch.sum(self.input_tensor, dim=-1)

    def get_input_shape(self) -> tuple:
        return (self.output_dim, self.reduction_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_elements = self.output_dim * self.reduction_dim
        output_elements = self.output_dim
        return input_elements * bytes_per_element, output_elements * bytes_per_element


class GELUBenchmark(OperatorBenchmark):
    """Benchmark for GELU (Gaussian Error Linear Unit) operator"""

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
        """Apply GELU activation"""
        return torch.nn.functional.gelu(self.input_tensor)

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class LayerNormBenchmark(OperatorBenchmark):
    """Benchmark for LayerNorm (Layer Normalization) operator"""

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 2048)
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 2048
        self.eps = 1e-6

        # Create input tensor and weight/bias
        self.input_tensor = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )
        self.weight = torch.ones(self.hidden_dim, dtype=self.dtype, device=self.device)
        self.bias = torch.zeros(self.hidden_dim, dtype=self.dtype, device=self.device)

    def run(self) -> torch.Tensor:
        """Apply LayerNorm"""
        x = self.input_tensor
        return torch.nn.functional.layer_norm(
            x,
            normalized_shape=(self.hidden_dim,),
            weight=self.weight,
            bias=self.bias,
            eps=self.eps,
        )

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class GEMMBenchmark(OperatorBenchmark):
    """Benchmark for GEMM (General Matrix Multiply) operator"""

    @property
    def _default_tile_size(self) -> int:
        """GEMM is compute-bound, balance compute utilization and memory"""
        return 512

    @property
    def _default_num_columns(self) -> int:
        """GEMM - 4 columns optimal for most shapes"""
        return 4

    def setup(self):
        # Shape: Matrix multiplication (M, K) x (K, N) = (M, N)
        self.M = 64  # rows of input A
        self.K = 128  # cols of A, rows of B
        self.N = 256  # cols of B

        # Create input tensors
        self.input_a = torch.randn(
            self.M,
            self.K,
            dtype=self.dtype,
            device=self.device,
        )
        self.input_b = torch.randn(
            self.K,
            self.N,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply GEMM (matrix multiplication)"""
        return torch.matmul(self.input_a, self.input_b)

    def get_input_shape(self) -> tuple:
        return ((self.M, self.K), (self.K, self.N))

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_a_elements = self.M * self.K
        input_b_elements = self.K * self.N
        output_elements = self.M * self.N
        input_bytes = (input_a_elements + input_b_elements) * bytes_per_element
        output_bytes = output_elements * bytes_per_element
        return input_bytes, output_bytes


class GEMM_KM_Large_Benchmark(OperatorBenchmark):
    """Benchmark for GEMM with K >> M (K much larger than M, optimal 4 columns)"""

    @property
    def _default_num_columns(self) -> int:
        """GEMM K>>M pattern - 4 columns for load balancing"""
        return 4

    def setup(self):
        # Shape: Matrix multiplication (M, K) x (K, N) = (M, N) where K >> M
        self.M = 32  # rows of input A (small)
        self.K = 4096  # cols of A, rows of B (very large - K >> M)
        self.N = 256  # cols of B

        # Create input tensors
        self.input_a = torch.randn(
            self.M,
            self.K,
            dtype=self.dtype,
            device=self.device,
        )
        self.input_b = torch.randn(
            self.K,
            self.N,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply GEMM (matrix multiplication) with K >> M"""
        return torch.matmul(self.input_a, self.input_b)

    def get_input_shape(self) -> tuple:
        return ((self.M, self.K), (self.K, self.N))

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_a_elements = self.M * self.K
        input_b_elements = self.K * self.N
        output_elements = self.M * self.N
        input_bytes = (input_a_elements + input_b_elements) * bytes_per_element
        output_bytes = output_elements * bytes_per_element
        return input_bytes, output_bytes


class GEMM_MK_Large_Benchmark(OperatorBenchmark):
    """Benchmark for GEMM with M >> K (M much larger than K, optimal 8 columns)"""

    @property
    def _default_num_columns(self) -> int:
        """GEMM M>>K pattern - 8 columns for row parallelism"""
        return 8

    def setup(self):
        # Shape: Matrix multiplication (M, K) x (K, N) = (M, N) where M >> K
        self.M = 4096  # rows of input A (very large - M >> K)
        self.K = 32  # cols of A, rows of B (small)
        self.N = 256  # cols of B

        # Create input tensors
        self.input_a = torch.randn(
            self.M,
            self.K,
            dtype=self.dtype,
            device=self.device,
        )
        self.input_b = torch.randn(
            self.K,
            self.N,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply GEMM (matrix multiplication) with M >> K"""
        return torch.matmul(self.input_a, self.input_b)

    def get_input_shape(self) -> tuple:
        return ((self.M, self.K), (self.K, self.N))

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_a_elements = self.M * self.K
        input_b_elements = self.K * self.N
        output_elements = self.M * self.N
        input_bytes = (input_a_elements + input_b_elements) * bytes_per_element
        output_bytes = output_elements * bytes_per_element
        return input_bytes, output_bytes


class GEMM_Square_Benchmark(OperatorBenchmark):
    """Benchmark for GEMM with square matrices (M = K = N)"""

    def setup(self):
        # Shape: Matrix multiplication (M, K) x (K, N) = (M, N) where M = K = N
        self.M = 512  # rows of input A (square)
        self.K = 512  # cols of A, rows of B (square)
        self.N = 512  # cols of B (square)

        # Create input tensors
        self.input_a = torch.randn(
            self.M,
            self.K,
            dtype=self.dtype,
            device=self.device,
        )
        self.input_b = torch.randn(
            self.K,
            self.N,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply GEMM (matrix multiplication) with square matrices"""
        return torch.matmul(self.input_a, self.input_b)

    def get_input_shape(self) -> tuple:
        return ((self.M, self.K), (self.K, self.N))

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_a_elements = self.M * self.K
        input_b_elements = self.K * self.N
        output_elements = self.M * self.N
        input_bytes = (input_a_elements + input_b_elements) * bytes_per_element
        output_bytes = output_elements * bytes_per_element
        return input_bytes, output_bytes


class GEMM_Small_Benchmark(OperatorBenchmark):
    """Benchmark for GEMM with small matrices"""

    def setup(self):
        # Shape: Matrix multiplication (M, K) x (K, N) = (M, N) with small dimensions
        self.M = 16  # rows of input A (small)
        self.K = 16  # cols of A, rows of B (small)
        self.N = 16  # cols of B (small)

        # Create input tensors
        self.input_a = torch.randn(
            self.M,
            self.K,
            dtype=self.dtype,
            device=self.device,
        )
        self.input_b = torch.randn(
            self.K,
            self.N,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply GEMM (matrix multiplication) with small matrices"""
        return torch.matmul(self.input_a, self.input_b)

    def get_input_shape(self) -> tuple:
        return ((self.M, self.K), (self.K, self.N))

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_a_elements = self.M * self.K
        input_b_elements = self.K * self.N
        output_elements = self.M * self.N
        input_bytes = (input_a_elements + input_b_elements) * bytes_per_element
        output_bytes = output_elements * bytes_per_element
        return input_bytes, output_bytes


class TransposeBenchmark(OperatorBenchmark):
    """Benchmark for Tensor Transpose operator"""

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 2048)
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 2048

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply tensor transpose (swap last two dimensions)"""
        return self.input_tensor.transpose(-2, -1)

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class AvgPoolBenchmark(OperatorBenchmark):
    """Benchmark for AvgPool2d operator"""

    def setup(self):
        self.batch_size = 1
        self.channels = 16
        self.height = 32
        self.width = 32
        self.kernel_size = 2
        self.stride = 2
        self.padding = 0

        self.input_tensor = torch.randn(
            self.batch_size,
            self.channels,
            self.height,
            self.width,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        return torch.nn.functional.avg_pool2d(
            self.input_tensor,
            kernel_size=self.kernel_size,
            stride=self.stride,
            padding=self.padding,
        )

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.channels, self.height, self.width)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_elements = self.batch_size * self.channels * self.height * self.width
        output_elements = input_elements // 4  # 2x2 kernel reduces to 1/4
        return input_elements * bytes_per_element, output_elements * bytes_per_element


class Conv2dBenchmark(OperatorBenchmark):
    """Benchmark for Conv2d (2D Convolution) operator"""

    def setup(self):
        # Input shape: (batch, channels, height, width) = (1, 3, 32, 32)
        self.batch_size = 1
        self.in_channels = 3
        self.out_channels = 16
        self.height = 32
        self.width = 32
        self.kernel_size = (3, 3)  # (kernel_h, kernel_w)
        self.stride = 1
        self.padding = 1  # Preserve spatial dimensions

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size,
            self.in_channels,
            self.height,
            self.width,
            dtype=self.dtype,
            device=self.device,
        )

        # Create weight tensor: (out_channels, in_channels, kernel_h, kernel_w)
        self.weight = torch.randn(
            self.out_channels,
            self.in_channels,
            *self.kernel_size,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply 2D convolution"""
        return torch.nn.functional.conv2d(
            self.input_tensor,
            self.weight,
            stride=self.stride,
            padding=self.padding,
        )

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.in_channels, self.height, self.width)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_elements = self.batch_size * self.in_channels * self.height * self.width
        weight_elements = (
            self.out_channels
            * self.in_channels
            * self.kernel_size[0]
            * self.kernel_size[1]
        )
        output_elements = (
            self.batch_size * self.out_channels * self.height * self.width
        )  # padding=1 preserves dims
        input_bytes = (input_elements + weight_elements) * bytes_per_element
        output_bytes = output_elements * bytes_per_element
        return input_bytes, output_bytes


class Conv3dBenchmark(OperatorBenchmark):
    """Benchmark for Conv3d (3D Convolution) operator"""

    def setup(self):
        # Input shape: (batch, channels, depth, height, width) = (1, 3, 16, 16, 16)
        self.batch_size = 1
        self.in_channels = 3
        self.out_channels = 8
        self.depth = 16
        self.height = 16
        self.width = 16
        self.kernel_size = (3, 3, 3)  # (kernel_d, kernel_h, kernel_w)
        self.stride = 1
        self.padding = 1  # Preserve spatial dimensions

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size,
            self.in_channels,
            self.depth,
            self.height,
            self.width,
            dtype=self.dtype,
            device=self.device,
        )

        # Create weight tensor: (out_channels, in_channels, kernel_d, kernel_h, kernel_w)
        self.weight = torch.randn(
            self.out_channels,
            self.in_channels,
            *self.kernel_size,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply 3D convolution"""
        return torch.nn.functional.conv3d(
            self.input_tensor,
            self.weight,
            stride=self.stride,
            padding=self.padding,
        )

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.in_channels, self.depth, self.height, self.width)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        input_elements = (
            self.batch_size * self.in_channels * self.depth * self.height * self.width
        )
        weight_elements = (
            self.out_channels
            * self.in_channels
            * self.kernel_size[0]
            * self.kernel_size[1]
            * self.kernel_size[2]
        )
        output_elements = (
            self.batch_size * self.out_channels * self.depth * self.height * self.width
        )  # padding=1 preserves dims
        input_bytes = (input_elements + weight_elements) * bytes_per_element
        output_bytes = output_elements * bytes_per_element
        return input_bytes, output_bytes


class ReLUBenchmark(OperatorBenchmark):
    """Benchmark for ReLU (Rectified Linear Unit) operator"""

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 8192) - match silu dimensions
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
        """Apply ReLU activation"""
        return torch.nn.functional.relu(self.input_tensor)

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class SigmoidBenchmark(OperatorBenchmark):
    """Benchmark for Sigmoid activation operator"""

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 8192) - match silu dimensions
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
        """Apply Sigmoid activation"""
        return torch.sigmoid(self.input_tensor)

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class TanhBenchmark(OperatorBenchmark):
    """Benchmark for Tanh (Hyperbolic Tangent) activation operator"""

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 8192) - match silu dimensions
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
        """Apply Tanh activation"""
        return torch.tanh(self.input_tensor)

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class LeakyReLUBenchmark(OperatorBenchmark):
    """Benchmark for Leaky ReLU activation operator"""

    def setup(self):
        # Shape: (batch, seq_len, hidden_dim) = (1, 128, 8192) - match silu dimensions
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 8192
        self.negative_slope = 0.01

        # Create input tensor
        self.input_tensor = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        """Apply Leaky ReLU activation"""
        return torch.nn.functional.leaky_relu(
            self.input_tensor, negative_slope=self.negative_slope
        )

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = total_elements * bytes_per_element
        output_bytes = input_bytes
        return input_bytes, output_bytes


class ElementwiseAddBenchmark(OperatorBenchmark):
    """Benchmark for Elementwise Addition operator (A + B)"""

    @property
    def _default_tile_size(self) -> int:
        """Elementwise add is memory-bound, larger contiguous access is beneficial"""
        return 512

    @property
    def _default_num_columns(self) -> int:
        """Elementwise add - 4 columns efficient for memory parallelism"""
        return 4

    def setup(self):
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 8192
        self.input_tensor_a = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )
        self.input_tensor_b = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        return self.input_tensor_a + self.input_tensor_b

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = 2 * total_elements * bytes_per_element
        output_bytes = total_elements * bytes_per_element
        return input_bytes, output_bytes


class ElementwiseMulBenchmark(OperatorBenchmark):
    """Benchmark for Elementwise Multiplication operator (A * B)"""

    def setup(self):
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 8192
        self.input_tensor_a = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )
        self.input_tensor_b = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        return self.input_tensor_a * self.input_tensor_b

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = 2 * total_elements * bytes_per_element
        output_bytes = total_elements * bytes_per_element
        return input_bytes, output_bytes


class AXPYBenchmark(OperatorBenchmark):
    """Benchmark for AXPY operator (Y = a*X + Y - scaled addition)"""

    def setup(self):
        self.batch_size = 1
        self.seq_len = 128
        self.hidden_dim = 8192
        self.scaler = 2.0
        self.input_tensor_x = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )
        self.input_tensor_y = torch.randn(
            self.batch_size,
            self.seq_len,
            self.hidden_dim,
            dtype=self.dtype,
            device=self.device,
        )

    def run(self) -> torch.Tensor:
        return self.input_tensor_x * self.scaler + self.input_tensor_y

    def get_input_shape(self) -> tuple:
        return (self.batch_size, self.seq_len, self.hidden_dim)

    def get_memory_footprint(self) -> tuple:
        bytes_per_element = 2 if self.dtype == torch.bfloat16 else 4
        total_elements = self.batch_size * self.seq_len * self.hidden_dim
        input_bytes = 2 * total_elements * bytes_per_element
        output_bytes = total_elements * bytes_per_element
        return input_bytes, output_bytes


# =============================================================================
# Operator Map (Module-level export for external imports)
# =============================================================================

OPERATOR_MAP = {
    "rope": RoPEBenchmark,
    "rmsnorm": RMSNormBenchmark,
    "silu": SiLUBenchmark,
    "softmax": SoftmaxBenchmark,
    "maxpool": MaxPoolBenchmark,  # P1 Group G - Maxpool/Reduction Infrastructure
    "reduction": ReductionBenchmark,  # P1 Group G - Maxpool/Reduction Infrastructure
    "gelu": GELUBenchmark,  # P3-1 Benchmark Expansion
    "layer_norm": LayerNormBenchmark,  # P3-1 Benchmark Expansion
    "gemm": GEMMBenchmark,  # P3-1 Benchmark Expansion
    "gemm_km_large": GEMM_KM_Large_Benchmark,  # P3-2 GEMM Benchmark Expansion
    "gemm_mk_large": GEMM_MK_Large_Benchmark,  # P3-2 GEMM Benchmark Expansion
    "gemm_square": GEMM_Square_Benchmark,  # P3-2 GEMM Benchmark Expansion
    "gemm_small": GEMM_Small_Benchmark,  # P3-2 GEMM Benchmark Expansion
    "transpose": TransposeBenchmark,  # P3-1 Benchmark Expansion
    "avgpool": AvgPoolBenchmark,  # P3-1 Benchmark Expansion
    "conv2d": Conv2dBenchmark,  # P3-3 Convolution Operator Benchmarks
    "conv3d": Conv3dBenchmark,  # P3-3 Convolution Operator Benchmarks
    "relu": ReLUBenchmark,  # P3-4 Activation Function Benchmarks
    "sigmoid": SigmoidBenchmark,  # P3-4 Activation Function Benchmarks
    "tanh": TanhBenchmark,  # P3-4 Activation Function Benchmarks
    "leaky_relu": LeakyReLUBenchmark,  # P3-4 Activation Function Benchmarks
    "elementwise_add": ElementwiseAddBenchmark,  # P3-5 Elementwise Operations
    "elementwise_mul": ElementwiseMulBenchmark,  # P3-5 Elementwise Operations
    "axpy": AXPYBenchmark,  # P3-5 Elementwise Operations
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
        choices=[
            "rope",
            "rmsnorm",
            "silu",
            "softmax",
            "maxpool",
            "reduction",
            "gelu",
            "layer_norm",
            "gemm",
            "gemm_km_large",
            "gemm_mk_large",
            "gemm_square",
            "gemm_small",
            "transpose",
            "avgpool",
            "conv2d",
            "conv3d",
            "relu",
            "sigmoid",
            "tanh",
            "leaky_relu",
            "elementwise_add",
            "elementwise_mul",
            "axpy",
        ],
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

    parser.add_argument(
        "--column-count",
        type=str,
        help="Column count or preset name for column scaling study (presets: standard, fine_grained, coarse, power_of_two, scaling_study; or comma-separated values like '1,2,4,8')",
    )

    parser.add_argument(
        "--enable-column-study",
        action="store_true",
        help="Enable column scaling study (tests multiple column configurations)",
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Parse column count if provided
    num_columns = None
    column_preset = None
    if args.column_count:
        try:
            parsed_columns = parse_column_count_argument(args.column_count)
            if len(parsed_columns) == 1:
                num_columns = parsed_columns[0]
            else:
                # Multiple column counts - use as column study
                column_preset = args.column_count
                args.enable_column_study = True
        except ValueError as e:
            logger.error(f"Invalid column count: {e}")
            sys.exit(1)

    config = BenchmarkConfig(
        iterations=args.iterations,
        warmup=args.warmup,
        output_format=args.output,
        output_file=args.output_file,
        verbose=args.verbose,
        operator=args.operator,
        device=args.device,
        dtype=args.dtype,
        num_columns=num_columns,
        column_preset=column_preset,
        enable_column_study=args.enable_column_study,
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
        print(
            "Operators: rope, rmsnorm, silu, softmax, maxpool, reduction, gelu, layer_norm, gemm, gemm_km_large, gemm_mk_large, gemm_square, gemm_small, transpose, avgpool, conv2d, conv3d, relu, sigmoid, tanh, leaky_relu, elementwise_add, elementwise_mul, axpy"
        )
    if num_columns is not None:
        print(f"Column count: {num_columns}")
    if column_preset:
        print(f"Column preset: {column_preset}")
    if args.enable_column_study:
        print("Column scaling study: ENABLED")
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
