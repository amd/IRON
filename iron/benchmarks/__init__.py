# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Benchmark Framework

A production-ready benchmark suite for measuring performance of IRON operators
on AMD Ryzen AI NPUs.

This package provides:
- Operator latency and throughput measurements
- Memory bandwidth utilization analysis
- Statistical metrics (mean, median, std dev, p95, p99)
- Multiple output formats (console, JSON, Markdown)
- CI/CD integration capabilities
- Benchmark validation and verification tools
"""

__version__ = "1.1.0"


# Lazy imports to avoid requiring AIE stack for baseline benchmarks
def __getattr__(name):
    if name in (
        "BenchmarkRunner",
        "OperatorBenchmark",
        "BenchmarkConfig",
        "BenchmarkResults",
        "run_benchmark",
    ):
        try:
            from .run import (
                BenchmarkRunner,
                OperatorBenchmark,
                BenchmarkConfig,
                BenchmarkResults,
                run_benchmark,
            )

            return globals().get(name) or locals().get(name)
        except ImportError as e:
            raise ImportError(
                f"Cannot import {name}: AIE stack (mlir_aie) not available. "
                "Use baseline_bench module for CPU reference benchmarks instead."
            ) from e
    elif name in ("BenchmarkValidator", "ValidationResult", "run_validation"):
        from .validate import (
            BenchmarkValidator,
            ValidationResult,
            run_validation,
        )

        return globals().get(name) or locals().get(name)
    elif name in ("VerificationReport", "compare_results", "verify_targets"):
        from .verify import (
            VerificationReport,
            compare_results,
            verify_targets,
        )

        return globals().get(name) or locals().get(name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    # Core benchmark runners
    "BenchmarkRunner",
    "OperatorBenchmark",
    "BenchmarkConfig",
    "BenchmarkResults",
    "run_benchmark",
    # Validation framework
    "BenchmarkValidator",
    "ValidationResult",
    "run_validation",
    # Verification tools
    "VerificationReport",
    "compare_results",
    "verify_targets",
]
