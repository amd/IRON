#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Benchmark Validation Framework

Comprehensive empirical benchmark validation for Windows 11 with AMD Ryzen AI NPU.
This module provides automated benchmark execution with system diagnostics,
anomaly detection, and result logging.

Features:
- Automated benchmark execution with one-command running
- Automatic system information capture (hardware, drivers, OS)
- JSON result logging with historical tracking
- Anomaly detection for unusual results
- Comparison against both Linux and Windows NPU targets
- Visual output generation (charts, graphs)

Usage:
    # Run full validation suite
    python -m iron.benchmarks.validate

    # Run with specific options
    python -m iron.benchmarks.validate --operator rope --iterations 100

    # Generate charts after validation
    python -m iron.benchmarks.validate --generate-charts

    # Compare against baseline
    python -m iron.benchmarks.validate --compare-baseline
"""

import argparse
import json
import logging
import os
import platform
import subprocess
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import statistics

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import torch
    import numpy as np
except ImportError as e:
    print(f"Warning: Could not import torch/numpy: {e}")
    print("Some features may be limited.")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# =============================================================================
# System Diagnostics
# =============================================================================

@dataclass
class SystemInfo:
    """System information for benchmark context"""
    platform: str = ""
    platform_version: str = ""
    architecture: str = ""
    processor: str = ""
    python_version: str = ""
    cpu_count: int = 0
    total_memory_gb: float = 0.0
    torch_version: str = ""
    torch_cuda_available: bool = False
    numpy_version: str = ""
    timestamp: str = ""

    # Windows-specific
    windows_edition: str = ""
    windows_build: str = ""

    # NPU-specific (if available)
    npu_detected: bool = False
    npu_driver_version: str = ""

    def capture(self):
        """Capture current system information"""
        self.timestamp = datetime.now().isoformat()
        self.platform = platform.system()
        self.platform_version = platform.version()
        self.architecture = platform.machine()
        self.processor = platform.processor()
        self.python_version = platform.python_version()
        self.cpu_count = os.cpu_count() or 0

        # Memory detection
        try:
            if self.platform == "Windows":
                import ctypes
                kernel32 = ctypes.windll.kernel32
                c_ulonglong = ctypes.c_ulonglong

                class MEMORYSTATUSEX(ctypes.Structure):
                    _fields_ = [
                        ('dwLength', ctypes.c_ulong),
                        ('dwMemoryLoad', ctypes.c_ulong),
                        ('ullTotalPhys', c_ulonglong),
                        ('ullAvailPhys', c_ulonglong),
                        ('ullTotalPageFile', c_ulonglong),
                        ('ullAvailPageFile', c_ulonglong),
                        ('ullTotalVirtual', c_ulonglong),
                        ('ullAvailVirtual', c_ulonglong),
                        ('ullAvailExtendedVirtual', c_ulonglong),
                    ]

                memoryStatus = MEMORYSTATUSEX()
                memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
                if kernel32.GlobalMemoryStatusEx(ctypes.byref(memoryStatus)):
                    self.total_memory_gb = memoryStatus.ullTotalPhys / (1024 ** 3)
        except Exception as e:
            logger.debug(f"Could not detect total memory: {e}")
            self.total_memory_gb = 0.0

        # PyTorch info
        try:
            import torch
            self.torch_version = torch.__version__
            self.torch_cuda_available = torch.cuda.is_available()
        except ImportError:
            self.torch_version = "not installed"
            self.torch_cuda_available = False

        # NumPy info
        try:
            import numpy
            self.numpy_version = numpy.__version__
        except ImportError:
            self.numpy_version = "not installed"

        # Windows-specific info
        if self.platform == "Windows":
            try:
                # Get Windows edition
                import winreg
                with winreg.OpenKey(
                    winreg.HKEY_LOCAL_MACHINE,
                    r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
                ) as key:
                    self.windows_edition, _ = winreg.QueryValueEx(key, "EditionId")
                    self.windows_build, _ = winreg.QueryValueEx(key, "CurrentBuild")
            except Exception as e:
                logger.debug(f"Could not get Windows edition: {e}")

        # NPU detection (Windows)
        if self.platform == "Windows":
            self._detect_npu_windows()

        return self

    def _detect_npu_windows(self):
        """Detect NPU on Windows system"""
        try:
            # Try to detect AMD Ryzen AI NPU via PnP
            result = subprocess.run(
                ["powershell", "-Command",
                 "Get-PnpDevice -Class 'System' -Status 'OK' | "
                 "Where-Object {$_.FriendlyName -like '*Ryzen*AI*' -or "
                 "$_.FriendlyName -like '*NPU*' -or "
                 "$_.FriendlyName -like '*AMD*AI*'} | "
                 "Select-Object -First 1 -ExpandProperty FriendlyName"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.stdout.strip():
                self.npu_detected = True
                logger.info(f"NPU detected: {result.stdout.strip()}")
        except Exception as e:
            logger.debug(f"NPU detection failed: {e}")
            self.npu_detected = False

    def to_dict(self) -> dict:
        return asdict(self)


# =============================================================================
# Performance Targets
# =============================================================================

@dataclass
class PerformanceTarget:
    """Performance target specification"""
    operator_name: str
    input_shape: Tuple[int, ...]
    linux_target_ms: float
    windows_target_ms: float
    cpu_baseline_ms: float
    description: str


# Performance targets for Phase 1 operators (Llama3.2-1B configuration)
PERFORMANCE_TARGETS = {
    "rope": PerformanceTarget(
        operator_name="rope",
        input_shape=(1, 12, 128, 64),
        linux_target_ms=0.5,
        windows_target_ms=0.55,  # ~10% overhead for ONNX Runtime
        cpu_baseline_ms=5.0,     # 10x slower than NPU
        description="RoPE (Rotary Positional Embedding)",
    ),
    "rmsnorm": PerformanceTarget(
        operator_name="rmsnorm",
        input_shape=(1, 128, 2048),
        linux_target_ms=1.0,
        windows_target_ms=1.1,
        cpu_baseline_ms=10.0,
        description="RMSNorm (Root Mean Square Normalization)",
    ),
    "silu": PerformanceTarget(
        operator_name="silu",
        input_shape=(1, 128, 8192),
        linux_target_ms=0.3,
        windows_target_ms=0.33,
        cpu_baseline_ms=3.0,
        description="SiLU (Sigmoid Linear Unit)",
    ),
    "softmax": PerformanceTarget(
        operator_name="softmax",
        input_shape=(1, 12, 128, 128),
        linux_target_ms=2.0,
        windows_target_ms=2.2,
        cpu_baseline_ms=20.0,
        description="Softmax",
    ),
}


# =============================================================================
# Anomaly Detection
# =============================================================================

@dataclass
class AnomalyReport:
    """Report of detected anomalies in benchmark results"""
    operator_name: str
    anomaly_type: str  # "high_latency", "high_variance", "target_miss", "regression"
    severity: str  # "LOW", "MEDIUM", "HIGH", "CRITICAL"
    description: str
    actual_value: float
    expected_value: float
    deviation_percent: float
    recommendation: str


class AnomalyDetector:
    """Detects anomalies in benchmark results"""

    # Thresholds for anomaly detection
    HIGH_VARIANCE_THRESHOLD = 0.15  # 15% coefficient of variation
    CRITICAL_VARIANCE_THRESHOLD = 0.30  # 30% CV
    HIGH_LATENCY_FACTOR = 2.0  # 2x expected latency
    CRITICAL_LATENCY_FACTOR = 5.0  # 5x expected latency
    REGRESSION_THRESHOLD = 0.10  # 10% regression from baseline

    def __init__(self, targets: Dict[str, PerformanceTarget]):
        self.targets = targets

    def detect(self, result: dict, baseline: Optional[dict] = None) -> List[AnomalyReport]:
        """Detect anomalies in a benchmark result"""
        anomalies = []

        operator_name = result.get("operator_name", "unknown")
        metrics = result.get("metrics", {})
        error = result.get("error")

        if error:
            anomalies.append(AnomalyReport(
                operator_name=operator_name,
                anomaly_type="execution_error",
                severity="CRITICAL",
                description=f"Benchmark execution failed: {error}",
                actual_value=0.0,
                expected_value=self.targets.get(operator_name, PerformanceTarget(
                    operator_name, (), 0, 0, 0, ""
                )).windows_target_ms,
                deviation_percent=100.0,
                recommendation="Check operator implementation and system configuration",
            ))
            return anomalies

        mean_ms = metrics.get("mean_ms", 0)
        std_dev_ms = metrics.get("std_dev_ms", 0)
        p99_ms = metrics.get("p99_ms", 0)

        # Get target for this operator
        target = self.targets.get(operator_name)
        if not target:
            return anomalies

        # Check for high variance (coefficient of variation)
        if mean_ms > 0:
            cv = std_dev_ms / mean_ms
            if cv >= self.CRITICAL_VARIANCE_THRESHOLD:
                anomalies.append(AnomalyReport(
                    operator_name=operator_name,
                    anomaly_type="high_variance",
                    severity="CRITICAL",
                    description=f"Critical variance detected: CV={cv*100:.1f}%",
                    actual_value=cv,
                    expected_value=self.HIGH_VARIANCE_THRESHOLD,
                    deviation_percent=(cv - self.HIGH_VARIANCE_THRESHOLD) / self.HIGH_VARIANCE_THRESHOLD * 100,
                    recommendation="System may be under load or thermal throttling. Re-run benchmarks.",
                ))
            elif cv >= self.HIGH_VARIANCE_THRESHOLD:
                anomalies.append(AnomalyReport(
                    operator_name=operator_name,
                    anomaly_type="high_variance",
                    severity="MEDIUM",
                    description=f"High variance detected: CV={cv*100:.1f}%",
                    actual_value=cv,
                    expected_value=self.HIGH_VARIANCE_THRESHOLD,
                    deviation_percent=(cv - self.HIGH_VARIANCE_THRESHOLD) / self.HIGH_VARIANCE_THRESHOLD * 100,
                    recommendation="Consider running more iterations for stable results.",
                ))

        # Check for high latency vs target
        if mean_ms > 0 and target.windows_target_ms > 0:
            latency_ratio = mean_ms / target.windows_target_ms
            if latency_ratio >= self.CRITICAL_LATENCY_FACTOR:
                anomalies.append(AnomalyReport(
                    operator_name=operator_name,
                    anomaly_type="high_latency",
                    severity="CRITICAL",
                    description=f"Critical: Latency {latency_ratio:.1f}x above Windows NPU target",
                    actual_value=mean_ms,
                    expected_value=target.windows_target_ms,
                    deviation_percent=(latency_ratio - 1) * 100,
                    recommendation="Verify NPU runtime is being used, not CPU fallback.",
                ))
            elif latency_ratio >= self.HIGH_LATENCY_FACTOR:
                anomalies.append(AnomalyReport(
                    operator_name=operator_name,
                    anomaly_type="high_latency",
                    severity="HIGH",
                    description=f"Latency {latency_ratio:.1f}x above Windows NPU target",
                    actual_value=mean_ms,
                    expected_value=target.windows_target_ms,
                    deviation_percent=(latency_ratio - 1) * 100,
                    recommendation="Check if NPU execution provider is properly configured.",
                ))

        # Check against baseline (regression detection)
        if baseline:
            baseline_results = {r["operator_name"]: r for r in baseline.get("results", [])}
            if operator_name in baseline_results:
                baseline_mean = baseline_results[operator_name].get("metrics", {}).get("mean_ms")
                if baseline_mean is not None and baseline_mean > 0 and mean_ms > 0:
                    regression = (mean_ms - baseline_mean) / baseline_mean
                    if regression >= self.REGRESSION_THRESHOLD:
                        anomalies.append(AnomalyReport(
                            operator_name=operator_name,
                            anomaly_type="regression",
                            severity="HIGH" if regression > 0.20 else "MEDIUM",
                            description=f"Performance regression: {regression*100:.1f}% slower than baseline",
                            actual_value=mean_ms,
                            expected_value=baseline_mean,
                            deviation_percent=regression * 100,
                            recommendation="Investigate recent changes or system configuration.",
                        ))

        return anomalies


# =============================================================================
# Benchmark Validation Runner
# =============================================================================

@dataclass
class ValidationResult:
    """Result of a validation run"""
    success: bool
    system_info: SystemInfo
    benchmark_results: List[dict]
    anomaly_reports: List[AnomalyReport]
    targets_summary: dict
    timestamp: str = ""
    duration_sec: float = 0.0

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "system_info": self.system_info.to_dict(),
            "benchmark_results": self.benchmark_results,
            "anomaly_reports": [asdict(a) for a in self.anomaly_reports],
            "targets_summary": self.targets_summary,
            "timestamp": self.timestamp,
            "duration_sec": self.duration_sec,
        }


class BenchmarkValidator:
    """Main validation runner for IRON benchmarks"""

    def __init__(
        self,
        iterations: int = 50,
        warmup: int = 10,
        operators: Optional[List[str]] = None,
        output_dir: Optional[str] = None,
        compare_baseline: bool = True,
        generate_charts: bool = False,
    ):
        self.iterations = iterations
        self.warmup = warmup
        self.operators = operators or list(PERFORMANCE_TARGETS.keys())
        self.output_dir = Path(output_dir) if output_dir else Path(__file__).parent / "results"
        self.compare_baseline = compare_baseline
        self.generate_charts = generate_charts
        self.anomaly_detector = AnomalyDetector(PERFORMANCE_TARGETS)

        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run_validation(self) -> ValidationResult:
        """Run the complete validation suite"""
        start_time = time.perf_counter()
        timestamp = datetime.now().isoformat()

        logger.info("=" * 60)
        logger.info("IRON Benchmark Validation Framework")
        logger.info("=" * 60)

        # Capture system info
        logger.info("Capturing system information...")
        system_info = SystemInfo().capture()
        logger.info(f"Platform: {system_info.platform} {system_info.windows_edition}")
        logger.info(f"Processor: {system_info.processor}")
        logger.info(f"Python: {system_info.python_version}")
        logger.info(f"Torch: {system_info.torch_version}")
        if system_info.npu_detected:
            logger.info(f"NPU: Detected")
        else:
            logger.info(f"NPU: Not detected (using CPU reference)")

        # Run benchmarks
        logger.info("")
        logger.info(f"Running benchmarks: {self.operators}")
        logger.info(f"Iterations: {self.iterations}, Warmup: {self.warmup}")

        benchmark_results = []
        for operator in self.operators:
            result = self._run_operator_benchmark(operator)
            benchmark_results.append(result)

        # Load baseline for comparison
        baseline = None
        if self.compare_baseline:
            baseline = self._load_baseline()

        # Detect anomalies
        logger.info("")
        logger.info("Analyzing results for anomalies...")
        all_anomalies = []
        for result in benchmark_results:
            anomalies = self.anomaly_detector.detect(result, baseline)
            all_anomalies.extend(anomalies)

        # Generate targets summary
        targets_summary = self._generate_targets_summary(benchmark_results)

        # Generate charts if requested
        if self.generate_charts:
            logger.info("Generating charts...")
            self._generate_charts(benchmark_results, system_info)

        # Save results
        duration_sec = time.perf_counter() - start_time
        validation_result = ValidationResult(
            success=len(all_anomalies) == 0 or all(a.severity != "CRITICAL" for a in all_anomalies),
            system_info=system_info,
            benchmark_results=benchmark_results,
            anomaly_reports=all_anomalies,
            targets_summary=targets_summary,
            timestamp=timestamp,
            duration_sec=duration_sec,
        )

        self._save_results(validation_result)

        # Print summary
        self._print_summary(validation_result)

        return validation_result

    def _run_operator_benchmark(self, operator: str) -> dict:
        """Run benchmark for a single operator"""
        logger.info(f"\n--- Benchmarking {operator.upper()} ---")

        target = PERFORMANCE_TARGETS.get(operator)
        if not target:
            logger.warning(f"Unknown operator: {operator}")
            return {
                "operator_name": operator,
                "error": f"Unknown operator: {operator}",
                "metrics": {},
            }

        try:
            # Import and run baseline benchmark (CPU reference)
            from iron.benchmarks.baseline_bench import (
                BenchmarkRunner,
                BenchmarkConfig,
                OPERATOR_MAP,
            )

            config = BenchmarkConfig(
                iterations=self.iterations,
                warmup=self.warmup,
                output_format="json",
                operator=operator,
                verbose=False,
            )

            runner = BenchmarkRunner(config)
            results = runner.run_all_benchmarks()

            if results.results and len(results.results) > 0:
                result = results.results[0]
                metrics = result.metrics

                benchmark_result = {
                    "operator_name": operator,
                    "input_shape": list(result.input_shape),
                    "metrics": {
                        "mean_ms": metrics.mean_ms,
                        "median_ms": metrics.median_ms,
                        "std_dev_ms": metrics.std_dev_ms,
                        "p95_ms": metrics.p95_ms,
                        "p99_ms": metrics.p99_ms,
                        "min_ms": metrics.min_ms,
                        "max_ms": metrics.max_ms,
                        "throughput_ops_sec": metrics.throughput_ops_sec,
                        "memory_bandwidth_gbps": metrics.memory_bandwidth_gbps,
                    },
                    "targets": {
                        "linux_npu_ms": target.linux_target_ms,
                        "windows_npu_ms": target.windows_target_ms,
                        "cpu_baseline_ms": target.cpu_baseline_ms,
                    },
                    "target_met": result.target_met,
                    "device_info": results.device_info,
                    "timestamp": datetime.now().isoformat(),
                }

                # Log result
                status = "PASS" if result.target_met else "FAIL"
                logger.info(
                    f"{operator}: mean={metrics.mean_ms:.4f}ms, "
                    f"target={target.cpu_baseline_ms:.2f}ms (CPU baseline), "
                    f"status={status}"
                )

                return benchmark_result

            return {
                "operator_name": operator,
                "error": "No results from benchmark",
                "metrics": {},
            }

        except ImportError as e:
            logger.error(f"Could not import benchmark module: {e}")
            return {
                "operator_name": operator,
                "error": f"Import error: {e}",
                "metrics": {},
            }
        except Exception as e:
            logger.error(f"Benchmark failed for {operator}: {e}")
            return {
                "operator_name": operator,
                "error": str(e),
                "metrics": {},
            }

    def _load_baseline(self) -> Optional[dict]:
        """Load baseline results for comparison"""
        baseline_paths = [
            Path(__file__).parent.parent.parent / "scripts" / "baseline.json",
            self.output_dir / "baseline.json",
        ]

        for path in baseline_paths:
            if path.exists():
                try:
                    with open(path, "r") as f:
                        baseline = json.load(f)
                    logger.info(f"Loaded baseline from: {path}")
                    return baseline
                except Exception as e:
                    logger.warning(f"Could not load baseline: {e}")

        logger.info("No baseline found for comparison")
        return None

    def _generate_targets_summary(self, results: List[dict]) -> dict:
        """Generate summary of target achievements"""
        summary = {
            "total_operators": len(results),
            "targets_met": 0,
            "targets_missed": 0,
            "errors": 0,
            "operators": [],
        }

        for result in results:
            op_name = result.get("operator_name", "unknown")
            error = result.get("error")
            target_met = result.get("target_met")

            op_summary = {
                "name": op_name,
                "status": "ERROR" if error else ("PASS" if target_met else "MISS"),
                "mean_ms": result.get("metrics", {}).get("mean_ms"),
                "target_ms": result.get("targets", {}).get("cpu_baseline_ms"),
            }
            summary["operators"].append(op_summary)

            if error:
                summary["errors"] += 1
            elif target_met:
                summary["targets_met"] += 1
            else:
                summary["targets_missed"] += 1

        return summary

    def _generate_charts(self, results: List[dict], system_info: SystemInfo):
        """Generate visualization charts"""
        try:
            import matplotlib
            matplotlib.use('Agg')  # Non-interactive backend
            import matplotlib.pyplot as plt

            # Filter out errored results
            valid_results = [r for r in results if not r.get("error")]

            if not valid_results:
                logger.warning("No valid results to chart")
                return

            operators = [r["operator_name"] for r in valid_results]
            means = [r["metrics"]["mean_ms"] for r in valid_results]
            p99s = [r["metrics"]["p99_ms"] for r in valid_results]
            targets = [r["targets"]["cpu_baseline_ms"] for r in valid_results]
            windows_targets = [r["targets"]["windows_npu_ms"] for r in valid_results]

            # Create figure with subplots
            fig, axes = plt.subplots(2, 2, figsize=(14, 10))
            fig.suptitle(
                f"IRON Benchmark Validation Results\n"
                f"{system_info.platform} - {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                fontsize=14
            )

            # Plot 1: Mean latency comparison
            ax1 = axes[0, 0]
            x = range(len(operators))
            width = 0.25

            ax1.bar([i - width for i in x], means, width, label='Mean Latency', color='steelblue')
            ax1.bar(x, p99s, width, label='P99 Latency', color='coral')
            ax1.bar([i + width for i in x], targets, width, label='CPU Target', color='lightgreen', linestyle='--')

            ax1.set_ylabel('Latency (ms)')
            ax1.set_title('Latency Comparison')
            ax1.set_xticks(x)
            ax1.set_xticklabels([op.upper() for op in operators], rotation=45)
            ax1.legend()
            ax1.grid(axis='y', alpha=0.3)

            # Plot 2: Target achievement
            ax2 = axes[0, 1]
            colors = ['green' if r.get('target_met') else 'red' for r in valid_results]
            ax2.bar(operators, means, color=colors, alpha=0.7)
            ax2.axhline(y=1, color='gray', linestyle='--', alpha=0.5)
            ax2.set_ylabel('Mean Latency (ms)')
            ax2.set_title('Target Achievement (Green=PASS, Red=FAIL)')
            ax2.set_xticklabels([op.upper() for op in operators], rotation=45)
            ax2.grid(axis='y', alpha=0.3)

            # Plot 3: Throughput
            ax3 = axes[1, 0]
            throughputs = [r["metrics"]["throughput_ops_sec"] for r in valid_results]
            bars = ax3.bar(operators, throughputs, color='mediumpurple', alpha=0.7)
            ax3.set_ylabel('Throughput (ops/sec)')
            ax3.set_title('Operator Throughput')
            ax3.set_xticklabels([op.upper() for op in operators], rotation=45)
            ax3.grid(axis='y', alpha=0.3)

            # Add value labels
            for bar, val in zip(bars, throughputs):
                ax3.text(
                    bar.get_x() + bar.get_width()/2, bar.get_height(),
                    f'{val:.0f}', ha='center', va='bottom', fontsize=9
                )

            # Plot 4: Variance (std dev / mean)
            ax4 = axes[1, 1]
            std_devs = [r["metrics"]["std_dev_ms"] for r in valid_results]
            variance_pct = [(s/m)*100 if m > 0 else 0 for s, m in zip(std_devs, means)]

            colors = []
            for v in variance_pct:
                if v < 5:
                    colors.append('green')
                elif v < 15:
                    colors.append('yellow')
                else:
                    colors.append('red')

            ax4.bar(operators, variance_pct, color=colors, alpha=0.7)
            ax4.axhline(y=15, color='red', linestyle='--', alpha=0.7, label='High variance threshold')
            ax4.set_ylabel('Coefficient of Variation (%)')
            ax4.set_title('Result Variance (Lower is Better)')
            ax4.set_xticklabels([op.upper() for op in operators], rotation=45)
            ax4.legend()
            ax4.grid(axis='y', alpha=0.3)

            plt.tight_layout()

            # Save chart
            chart_path = self.output_dir / f"validation_chart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            plt.savefig(chart_path, dpi=150, bbox_inches='tight')
            logger.info(f"Chart saved to: {chart_path}")

            plt.close()

        except ImportError:
            logger.warning("matplotlib not available, skipping chart generation")
        except Exception as e:
            logger.warning(f"Could not generate charts: {e}")

    def _save_results(self, result: ValidationResult):
        """Save validation results to file"""
        # Save JSON results
        json_path = self.output_dir / f"validation_{result.timestamp.replace(':', '-')}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result.to_dict(), f, indent=2, default=str)
        logger.info(f"Results saved to: {json_path}")

        # Save Markdown summary
        md_path = self.output_dir / f"validation_{result.timestamp.replace(':', '-')}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(self._format_markdown(result))
        logger.info(f"Markdown summary saved to: {md_path}")

        # Also save as latest for easy access
        latest_json = self.output_dir / "validation_latest.json"
        with open(latest_json, "w", encoding="utf-8") as f:
            json.dump(result.to_dict(), f, indent=2, default=str)

        latest_md = self.output_dir / "validation_latest.md"
        with open(latest_md, "w", encoding="utf-8") as f:
            f.write(self._format_markdown(result))

    def _format_markdown(self, result: ValidationResult) -> str:
        """Format results as Markdown"""
        lines = []
        lines.append("# IRON Benchmark Validation Report")
        lines.append("")
        lines.append(f"**Generated:** {result.timestamp}")
        lines.append(f"**Duration:** {result.duration_sec:.2f}s")
        lines.append("")

        # System Info
        lines.append("## System Information")
        lines.append("")
        si = result.system_info
        lines.append(f"- **Platform:** {si.platform} {si.windows_edition} (Build {si.windows_build})")
        lines.append(f"- **Processor:** {si.processor}")
        lines.append(f"- **Memory:** {si.total_memory_gb:.1f} GB")
        lines.append(f"- **Python:** {si.python_version}")
        lines.append(f"- **PyTorch:** {si.torch_version}")
        lines.append(f"- **NPU Detected:** {'Yes' if si.npu_detected else 'No'}")
        lines.append("")

        # Summary
        lines.append("## Validation Summary")
        lines.append("")
        ts = result.targets_summary
        status = "PASS" if result.success else "FAIL"
        lines.append(f"**Overall Status:** {status}")
        lines.append(f"- Operators tested: {ts['total_operators']}")
        lines.append(f"- Targets met: {ts['targets_met']}")
        lines.append(f"- Targets missed: {ts['targets_missed']}")
        lines.append(f"- Errors: {ts['errors']}")
        lines.append("")

        # Results Table
        lines.append("## Results by Operator")
        lines.append("")
        lines.append("| Operator | Mean (ms) | Target (ms) | Status |")
        lines.append("|----------|-----------|-------------|--------|")
        for op in ts["operators"]:
            status_icon = "OK" if op["status"] == "PASS" else ("FAIL" if op["status"] == "MISS" else "ERR")
            mean_str = f"{op['mean_ms']:.4f}" if op['mean_ms'] else 'N/A'
            target_str = f"{op['target_ms']:.2f}" if op['target_ms'] else 'N/A'
            lines.append(
                f"| {op['name'].upper()} | {mean_str} | {target_str} | {status_icon} |"
            )
        lines.append("")

        # Anomalies
        if result.anomaly_reports:
            lines.append("## Anomalies Detected")
            lines.append("")
            for anomaly in result.anomaly_reports:
                severity_icon = {
                    "LOW": "",
                    "MEDIUM": "!",
                    "HIGH": "!!",
                    "CRITICAL": "!!!",
                }.get(anomaly.severity, "")
                lines.append(f"### {severity_icon} {anomaly.operator_name}: {anomaly.anomaly_type}")
                lines.append(f"- **Severity:** {anomaly.severity}")
                lines.append(f"- **Description:** {anomaly.description}")
                lines.append(f"- **Actual:** {anomaly.actual_value:.4f}")
                lines.append(f"- **Expected:** {anomaly.expected_value:.4f}")
                lines.append(f"- **Deviation:** {anomaly.deviation_percent:.1f}%")
                lines.append(f"- **Recommendation:** {anomaly.recommendation}")
                lines.append("")
        else:
            lines.append("## Anomalies")
            lines.append("")
            lines.append("No anomalies detected.")
            lines.append("")

        # Detailed Results
        lines.append("## Detailed Results")
        lines.append("")
        for br in result.benchmark_results:
            op_name = br.get("operator_name", "unknown")
            lines.append(f"### {op_name.upper()}")
            lines.append("")
            if br.get("error"):
                lines.append(f"**Error:** {br['error']}")
            else:
                metrics = br.get("metrics", {})
                lines.append("| Metric | Value |")
                lines.append("|--------|-------|")
                lines.append(f"| Mean | {metrics.get('mean_ms', 0):.4f} ms |")
                lines.append(f"| Median | {metrics.get('median_ms', 0):.4f} ms |")
                lines.append(f"| Std Dev | {metrics.get('std_dev_ms', 0):.4f} ms |")
                lines.append(f"| P95 | {metrics.get('p95_ms', 0):.4f} ms |")
                lines.append(f"| P99 | {metrics.get('p99_ms', 0):.4f} ms |")
                lines.append(f"| Throughput | {metrics.get('throughput_ops_sec', 0):.2f} ops/sec |")
                lines.append(f"| Bandwidth | {metrics.get('memory_bandwidth_gbps', 0):.4f} GB/s |")
            lines.append("")

        lines.append("---")
        lines.append("*Generated by IRON Benchmark Validation Framework*")

        return "\n".join(lines)

    def _print_summary(self, result: ValidationResult):
        """Print summary to console"""
        print("\n" + "=" * 60)
        print("VALIDATION COMPLETE")
        print("=" * 60)

        ts = result.targets_summary
        status = "PASS" if result.success else "FAIL"
        print(f"Overall Status: {status}")
        print(f"Operators: {ts['total_operators']} | Met: {ts['targets_met']} | Missed: {ts['targets_missed']} | Errors: {ts['errors']}")

        if result.anomaly_reports:
            print(f"\nAnomalies: {len(result.anomaly_reports)}")
            for a in result.anomaly_reports:
                print(f"  [{a.severity}] {a.operator_name}: {a.anomaly_type}")

        print(f"\nResults saved to: {self.output_dir}")
        print("=" * 60)


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="IRON Benchmark Validation Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full validation
  python -m iron.benchmarks.validate

  # Run specific operator
  python -m iron.benchmarks.validate --operator rope

  # Run with more iterations
  python -m iron.benchmarks.validate --iterations 100

  # Generate charts
  python -m iron.benchmarks.validate --generate-charts

  # Compare against baseline
  python -m iron.benchmarks.validate --compare-baseline
""",
    )

    parser.add_argument(
        "--operator",
        type=str,
        choices=["rope", "rmsnorm", "silu", "softmax"],
        help="Run specific operator (default: all)",
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
        default=10,
        help="Number of warmup runs (default: 10)",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        help="Output directory for results (default: benchmarks/results)",
    )

    parser.add_argument(
        "--compare-baseline",
        action="store_true",
        default=True,
        help="Compare against baseline (default: True)",
    )

    parser.add_argument(
        "--no-compare-baseline",
        action="store_true",
        help="Skip baseline comparison",
    )

    parser.add_argument(
        "--generate-charts",
        action="store_true",
        help="Generate visualization charts",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    return parser.parse_args()


def run_validation(
    operators: Optional[List[str]] = None,
    iterations: int = 50,
    warmup: int = 10,
    output_dir: Optional[str] = None,
    compare_baseline: bool = True,
    generate_charts: bool = False,
    verbose: bool = False,
) -> ValidationResult:
    """
    Convenience function to run benchmark validation.

    Args:
        operators: List of operators to benchmark (None = all)
        iterations: Number of timed iterations
        warmup: Number of warmup runs
        output_dir: Output directory for results
        compare_baseline: Compare against baseline
        generate_charts: Generate visualization charts
        verbose: Enable verbose logging

    Returns:
        ValidationResult with all benchmark data

    Example:
        >>> from iron.benchmarks.validate import run_validation
        >>> result = run_validation(iterations=100, generate_charts=True)
        >>> print(f"Targets met: {result.targets_summary['targets_met']}")
    """
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    validator = BenchmarkValidator(
        iterations=iterations,
        warmup=warmup,
        operators=operators,
        output_dir=output_dir,
        compare_baseline=compare_baseline,
        generate_charts=generate_charts,
    )

    return validator.run_validation()


def main():
    """Main entry point"""
    args = parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    operators = [args.operator] if args.operator else None

    validator = BenchmarkValidator(
        iterations=args.iterations,
        warmup=args.warmup,
        operators=operators,
        output_dir=args.output_dir,
        compare_baseline=not args.no_compare_baseline,
        generate_charts=args.generate_charts,
    )

    result = validator.run_validation()

    # Exit code based on success
    sys.exit(0 if result.success else 1)


if __name__ == "__main__":
    main()
