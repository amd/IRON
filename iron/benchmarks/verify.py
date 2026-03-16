#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Benchmark Verification and Comparison Tool

This module provides verification capabilities for benchmark results:
- Compare current results against baseline
- Compare against Linux and Windows NPU targets
- Statistical analysis and anomaly flagging
- Trend analysis across multiple runs
- Report generation

Usage:
    # Compare two result files
    python -m iron.benchmarks.verify --current results.json --baseline baseline.json

    # Verify against targets
    python -m iron.benchmarks.verify --verify-targets results.json

    # Analyze trends across multiple runs
    python -m iron.benchmarks.verify --trend-analysis results_dir/

    # Generate comparison report
    python -m iron.benchmarks.verify --compare results1.json results2.json
"""

import argparse
import json
import logging
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import statistics

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# =============================================================================
# Performance Targets
# =============================================================================

@dataclass
class TargetSpec:
    """Performance target specification"""
    operator_name: str
    linux_npu_ms: float
    windows_npu_ms: float
    cpu_baseline_ms: float
    description: str


TARGETS = {
    "rope": TargetSpec(
        operator_name="rope",
        linux_npu_ms=0.5,
        windows_npu_ms=0.55,
        cpu_baseline_ms=5.0,
        description="RoPE (Rotary Positional Embedding)",
    ),
    "rmsnorm": TargetSpec(
        operator_name="rmsnorm",
        linux_npu_ms=1.0,
        windows_npu_ms=1.1,
        cpu_baseline_ms=10.0,
        description="RMSNorm",
    ),
    "silu": TargetSpec(
        operator_name="silu",
        linux_npu_ms=0.3,
        windows_npu_ms=0.33,
        cpu_baseline_ms=3.0,
        description="SiLU",
    ),
    "softmax": TargetSpec(
        operator_name="softmax",
        linux_npu_ms=2.0,
        windows_npu_ms=2.2,
        cpu_baseline_ms=20.0,
        description="Softmax",
    ),
}


# =============================================================================
# Data Classes
# =============================================================================

@dataclass
class ComparisonResult:
    """Result of comparing two benchmark runs"""
    operator_name: str
    baseline_mean_ms: float
    current_mean_ms: float
    change_ms: float
    change_percent: float
    regression: bool
    severity: str  # "NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class TargetVerificationResult:
    """Result of target verification"""
    operator_name: str
    measured_mean_ms: float
    target_type: str  # "linux_npu", "windows_npu", "cpu_baseline"
    target_value_ms: float
    passed: bool
    margin_ms: float
    margin_percent: float

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class TrendAnalysis:
    """Trend analysis across multiple runs"""
    operator_name: str
    metric_name: str
    values: List[float]
    trend_direction: str  # "IMPROVING", "DEGRADING", "STABLE"
    trend_slope: float
    min_value: float
    max_value: float
    mean_value: float
    std_dev: float
    outlier_count: int

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class VerificationReport:
    """Complete verification report"""
    timestamp: str
    current_file: str
    baseline_file: Optional[str]
    comparisons: List[ComparisonResult]
    target_verifications: List[TargetVerificationResult]
    trends: Optional[List[TrendAnalysis]]
    summary: dict

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "current_file": self.current_file,
            "baseline_file": self.baseline_file,
            "comparisons": [c.to_dict() for c in self.comparisons],
            "target_verifications": [t.to_dict() for t in self.target_verifications],
            "trends": [t.to_dict() for t in self.trends] if self.trends else None,
            "summary": self.summary,
        }


# =============================================================================
# Verification Functions
# =============================================================================

def load_results(file_path: str) -> dict:
    """Load benchmark results from JSON file"""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Results file not found: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def compare_results(
    current: dict,
    baseline: dict,
    threshold: float = 0.10
) -> List[ComparisonResult]:
    """
    Compare current results against baseline.

    Args:
        current: Current benchmark results
        baseline: Baseline benchmark results
        threshold: Regression threshold (default 10%)

    Returns:
        List of comparison results
    """
    comparisons = []

    current_results = {r["operator_name"]: r for r in current.get("results", [])}
    baseline_results = {r["operator_name"]: r for r in baseline.get("results", [])}

    for op_name, current_data in current_results.items():
        if op_name not in baseline_results:
            logger.debug(f"Operator {op_name} not in baseline, skipping comparison")
            continue

        baseline_data = baseline_results[op_name]

        # Skip if either has errors
        if current_data.get("error") or baseline_data.get("error"):
            comparisons.append(ComparisonResult(
                operator_name=op_name,
                baseline_mean_ms=0.0,
                current_mean_ms=0.0,
                change_ms=0.0,
                change_percent=0.0,
                regression=False,
                severity="NONE",
            ))
            continue

        current_mean = current_data.get("metrics", {}).get("mean_ms", 0)
        baseline_mean = baseline_data.get("metrics", {}).get("mean_ms", 0)

        if baseline_mean <= 0 or current_mean <= 0:
            continue

        change_ms = current_mean - baseline_mean
        change_percent = (change_ms / baseline_mean) * 100

        # Determine regression and severity
        regression = change_percent > (threshold * 100)
        if change_percent <= 5:
            severity = "NONE"
        elif change_percent <= 10:
            severity = "LOW"
        elif change_percent <= 20:
            severity = "MEDIUM"
        elif change_percent <= 50:
            severity = "HIGH"
        else:
            severity = "CRITICAL"

        comparisons.append(ComparisonResult(
            operator_name=op_name,
            baseline_mean_ms=baseline_mean,
            current_mean_ms=current_mean,
            change_ms=change_ms,
            change_percent=change_percent,
            regression=regression,
            severity=severity,
        ))

    return comparisons


def verify_targets(
    results: dict,
    target_type: str = "windows_npu"
) -> List[TargetVerificationResult]:
    """
    Verify results against performance targets.

    Args:
        results: Benchmark results
        target_type: Type of target ("linux_npu", "windows_npu", "cpu_baseline")

    Returns:
        List of verification results
    """
    verifications = []

    for result in results.get("results", []):
        op_name = result.get("operator_name")
        if op_name not in TARGETS:
            logger.debug(f"No target for operator: {op_name}")
            continue

        target = TARGETS[op_name]
        target_value = getattr(target, f"{target_type}_ms")

        mean_ms = result.get("metrics", {}).get("mean_ms", 0)
        if mean_ms <= 0:
            continue

        passed = mean_ms <= target_value
        margin_ms = target_value - mean_ms
        margin_percent = (margin_ms / target_value) * 100 if target_value > 0 else 0

        verifications.append(TargetVerificationResult(
            operator_name=op_name,
            measured_mean_ms=mean_ms,
            target_type=target_type,
            target_value_ms=target_value,
            passed=passed,
            margin_ms=margin_ms,
            margin_percent=margin_percent,
        ))

    return verifications


def analyze_trends(
    results_dir: str,
    metric_name: str = "mean_ms"
) -> List[TrendAnalysis]:
    """
    Analyze trends across multiple result files.

    Args:
        results_dir: Directory containing result JSON files
        metric_name: Metric to analyze

    Returns:
        List of trend analyses per operator
    """
    dir_path = Path(results_dir)
    if not dir_path.exists():
        raise FileNotFoundError(f"Results directory not found: {results_dir}")

    # Collect all result files sorted by timestamp
    result_files = sorted(
        dir_path.glob("validation_*.json"),
        key=lambda p: p.stat().st_mtime
    )

    if not result_files:
        raise ValueError(f"No result files found in {results_dir}")

    logger.info(f"Found {len(result_files)} result files for trend analysis")

    # Collect values per operator
    operator_values: Dict[str, List[Tuple[datetime, float]]] = {}

    for file_path in result_files:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)

            timestamp_str = data.get("timestamp", "")
            try:
                timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
            except:
                timestamp = datetime.fromtimestamp(file_path.stat().st_mtime)

            for result in data.get("results", []):
                op_name = result.get("operator_name")
                if not op_name:
                    continue

                value = result.get("metrics", {}).get(metric_name, 0)
                if value > 0:
                    if op_name not in operator_values:
                        operator_values[op_name] = []
                    operator_values[op_name].append((timestamp, value))
        except Exception as e:
            logger.warning(f"Could not process {file_path}: {e}")

    # Analyze trends
    trends = []
    for op_name, values in operator_values.items():
        if len(values) < 2:
            continue

        # Sort by timestamp
        values.sort(key=lambda x: x[0])
        numeric_values = [v[1] for v in values]

        # Calculate statistics
        mean_val = statistics.mean(numeric_values)
        std_val = statistics.stdev(numeric_values) if len(numeric_values) > 1 else 0
        min_val = min(numeric_values)
        max_val = max(numeric_values)

        # Calculate trend slope (simple linear regression)
        n = len(values)
        x_mean = n / 2
        y_mean = mean_val

        numerator = sum((i - x_mean) * (v - y_mean) for i, v in enumerate(numeric_values))
        denominator = sum((i - x_mean) ** 2 for i in range(n))

        slope = numerator / denominator if denominator != 0 else 0

        # Determine trend direction
        if abs(slope) < 0.01 * mean_val:
            direction = "STABLE"
        elif slope < 0:
            direction = "IMPROVING"  # Lower latency is better
        else:
            direction = "DEGRADING"

        # Detect outliers (values > 2 std dev from mean)
        outlier_count = sum(1 for v in numeric_values if abs(v - mean_val) > 2 * std_val)

        trends.append(TrendAnalysis(
            operator_name=op_name,
            metric_name=metric_name,
            values=numeric_values,
            trend_direction=direction,
            trend_slope=slope,
            min_value=min_val,
            max_value=max_val,
            mean_value=mean_val,
            std_dev=std_val,
            outlier_count=outlier_count,
        ))

    return trends


# =============================================================================
# Report Generation
# =============================================================================

def format_comparison_report(
    comparisons: List[ComparisonResult],
    current: dict,
    baseline: dict
) -> str:
    """Format comparison results as text report"""
    lines = []
    lines.append("=" * 70)
    lines.append("BENCHMARK COMPARISON REPORT")
    lines.append("=" * 70)
    lines.append("")

    # Summary
    regressions = [c for c in comparisons if c.regression]
    improvements = [c for c in comparisons if c.change_percent < -5]

    lines.append("SUMMARY")
    lines.append("-" * 70)
    lines.append(f"Total operators compared: {len(comparisons)}")
    lines.append(f"Regressions detected: {len(regressions)}")
    lines.append(f"Improvements: {len(improvements)}")
    lines.append("")

    # Detailed comparisons
    lines.append("DETAILED COMPARISON")
    lines.append("-" * 70)
    lines.append("")

    for comp in comparisons:
        lines.append(f"Operator: {comp.operator_name.upper()}")
        if comp.severity == "NONE":
            lines.append(f"  Baseline: {comp.baseline_mean_ms:.4f} ms")
            lines.append(f"  Current:  {comp.current_mean_ms:.4f} ms")
            lines.append(f"  Change:   {comp.change_percent:+.1f}% (No significant change)")
        elif comp.regression:
            lines.append(f"  Baseline: {comp.baseline_mean_ms:.4f} ms")
            lines.append(f"  Current:  {comp.current_mean_ms:.4f} ms")
            lines.append(f"  Change:   {comp.change_percent:+.1f}% [{comp.severity}] REGRESSION")
        else:
            lines.append(f"  Baseline: {comp.baseline_mean_ms:.4f} ms")
            lines.append(f"  Current:  {comp.current_mean_ms:.4f} ms")
            lines.append(f"  Change:   {comp.change_percent:+.1f}% [{comp.severity}]")
        lines.append("")

    lines.append("=" * 70)
    return "\n".join(lines)


def format_target_report(
    verifications: List[TargetVerificationResult],
    target_type: str
) -> str:
    """Format target verification as text report"""
    lines = []
    lines.append("=" * 70)
    lines.append(f"TARGET VERIFICATION REPORT ({target_type.upper()})")
    lines.append("=" * 70)
    lines.append("")

    # Summary
    passed = [v for v in verifications if v.passed]
    failed = [v for v in verifications if not v.passed]

    lines.append("SUMMARY")
    lines.append("-" * 70)
    lines.append(f"Total operators: {len(verifications)}")
    lines.append(f"Targets met: {len(passed)}")
    lines.append(f"Targets missed: {len(failed)}")
    lines.append(f"Pass rate: {len(passed)/len(verifications)*100:.1f}%" if verifications else "N/A")
    lines.append("")

    # Detailed results
    lines.append("DETAILED RESULTS")
    lines.append("-" * 70)
    lines.append("")

    for v in verifications:
        status = "PASS" if v.passed else "FAIL"
        lines.append(f"Operator: {v.operator_name.upper()}")
        lines.append(f"  Target:     {v.target_value_ms:.2f} ms ({v.target_type})")
        lines.append(f"  Measured:   {v.measured_mean_ms:.4f} ms")
        lines.append(f"  Margin:     {v.margin_ms:+.4f} ms ({v.margin_percent:+.1f}%)")
        lines.append(f"  Status:     [{status}]")
        lines.append("")

    lines.append("=" * 70)
    return "\n".join(lines)


def format_trend_report(trends: List[TrendAnalysis]) -> str:
    """Format trend analysis as text report"""
    lines = []
    lines.append("=" * 70)
    lines.append("TREND ANALYSIS REPORT")
    lines.append("=" * 70)
    lines.append("")

    for trend in trends:
        lines.append(f"Operator: {trend.operator_name.upper()}")
        lines.append(f"  Metric:     {trend.metric_name}")
        lines.append(f"  Trend:      {trend.trend_direction}")
        lines.append(f"  Slope:      {trend.trend_slope:.6f}")
        lines.append(f"  Mean:       {trend.mean_value:.4f}")
        lines.append(f"  Std Dev:    {trend.std_dev:.4f}")
        lines.append(f"  Min/Max:    {trend.min_value:.4f} / {trend.max_value:.4f}")
        lines.append(f"  Outliers:   {trend.outlier_count}")

        if trend.values:
            lines.append(f"  Values:     {' -> '.join(f'{v:.4f}' for v in trend.values)}")
        lines.append("")

    lines.append("=" * 70)
    return "\n".join(lines)


# =============================================================================
# CLI Functions
# =============================================================================

def cmd_compare(args):
    """Handle compare command"""
    try:
        current = load_results(args.current)
        baseline = load_results(args.baseline)
    except FileNotFoundError as e:
        logger.error(str(e))
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {e}")
        sys.exit(1)

    comparisons = compare_results(current, baseline, args.threshold)
    report = format_comparison_report(comparisons, current, baseline)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        logger.info(f"Report saved to: {args.output}")
    else:
        print(report)

    # Exit with error if regressions found
    regressions = [c for c in comparisons if c.regression and c.severity in ("HIGH", "CRITICAL")]
    if args.exit_on_regression and regressions:
        logger.error(f"Found {len(regressions)} significant regressions")
        sys.exit(1)

    sys.exit(0)


def cmd_verify_targets(args):
    """Handle verify-targets command"""
    try:
        results = load_results(args.results_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(str(e))
        sys.exit(1)

    verifications = verify_targets(results, args.target_type)
    report = format_target_report(verifications, args.target_type)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        logger.info(f"Report saved to: {args.output}")
    else:
        print(report)

    # Exit with error if any targets missed
    missed = [v for v in verifications if not v.passed]
    if args.exit_on_failure and missed:
        logger.error(f"Missed {len(missed)} targets")
        sys.exit(1)

    sys.exit(0)


def cmd_trend_analysis(args):
    """Handle trend-analysis command"""
    try:
        trends = analyze_trends(args.results_dir, args.metric)
    except (FileNotFoundError, ValueError) as e:
        logger.error(str(e))
        sys.exit(1)

    report = format_trend_report(trends)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        logger.info(f"Report saved to: {args.output}")
    else:
        print(report)

    sys.exit(0)


def cmd_summary(args):
    """Handle summary command - quick overview of results"""
    try:
        results = load_results(args.results_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(str(e))
        sys.exit(1)

    print("=" * 50)
    print("BENCHMARK RESULTS SUMMARY")
    print("=" * 50)

    # System info if available
    if "system_info" in results:
        si = results["system_info"]
        print(f"Platform: {si.get('platform', 'Unknown')}")
        print(f"Processor: {si.get('processor', 'Unknown')}")
        print(f"Timestamp: {results.get('timestamp', 'Unknown')}")
        print("")

    # Results summary
    print("RESULTS")
    print("-" * 50)

    for result in results.get("results", []):
        op_name = result.get("operator_name", "unknown")
        error = result.get("error")

        if error:
            print(f"{op_name.upper()}: ERROR - {error}")
        else:
            metrics = result.get("metrics", {})
            mean_ms = metrics.get("mean_ms", 0)
            p99_ms = metrics.get("p99_ms", 0)
            throughput = metrics.get("throughput_ops_sec", 0)

            print(f"{op_name.upper()}:")
            print(f"  Mean: {mean_ms:.4f} ms | P99: {p99_ms:.4f} ms | Throughput: {throughput:.0f} ops/s")

    print("=" * 50)
    sys.exit(0)


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="IRON Benchmark Verification and Comparison Tool"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Compare command
    compare_parser = subparsers.add_parser("compare", help="Compare two result files")
    compare_parser.add_argument("--current", required=True, help="Current results file")
    compare_parser.add_argument("--baseline", required=True, help="Baseline results file")
    compare_parser.add_argument("--threshold", type=float, default=0.10, help="Regression threshold")
    compare_parser.add_argument("--output", help="Output file for report")
    compare_parser.add_argument("--exit-on-regression", action="store_true", help="Exit 1 on regression")

    # Verify-targets command
    verify_parser = subparsers.add_parser("verify-targets", help="Verify against targets")
    verify_parser.add_argument("results_file", help="Results file to verify")
    verify_parser.add_argument(
        "--target-type",
        choices=["linux_npu", "windows_npu", "cpu_baseline"],
        default="windows_npu",
        help="Target type to verify against"
    )
    verify_parser.add_argument("--output", help="Output file for report")
    verify_parser.add_argument("--exit-on-failure", action="store_true", help="Exit 1 on failure")

    # Trend-analysis command
    trend_parser = subparsers.add_parser("trend-analysis", help="Analyze trends")
    trend_parser.add_argument("results_dir", help="Directory with result files")
    trend_parser.add_argument(
        "--metric",
        default="mean_ms",
        help="Metric to analyze (default: mean_ms)"
    )
    trend_parser.add_argument("--output", help="Output file for report")

    # Summary command
    summary_parser = subparsers.add_parser("summary", help="Quick results summary")
    summary_parser.add_argument("results_file", help="Results file to summarize")

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_args()

    if args.command == "compare":
        cmd_compare(args)
    elif args.command == "verify-targets":
        cmd_verify_targets(args)
    elif args.command == "trend-analysis":
        cmd_trend_analysis(args)
    elif args.command == "summary":
        cmd_summary(args)
    else:
        print("Usage: python -m iron.benchmarks.verify <command>")
        print("")
        print("Commands:")
        print("  compare         Compare two result files")
        print("  verify-targets  Verify results against performance targets")
        print("  trend-analysis  Analyze trends across multiple runs")
        print("  summary         Quick results summary")
        print("")
        print("Use 'python -m iron.benchmarks.verify <command> --help' for more info.")
        sys.exit(1)


if __name__ == "__main__":
    main()
