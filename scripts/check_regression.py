#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Performance Regression Checker for IRON Benchmarks

This script compares current benchmark results against a baseline to detect
performance regressions. It is designed for CI/CD integration.

Usage:
    python scripts/check_regression.py \
        --current benchmark_results.json \
        --baseline scripts/baseline.json \
        --threshold 0.10

Returns exit code 0 if no regressions, 1 if regressions detected.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def load_results(file_path: str) -> dict:
    """Load benchmark results from JSON file"""
    with open(file_path, "r") as f:
        return json.load(f)


def compare_metrics(
    current: dict,
    baseline: dict,
    threshold: float
) -> List[Dict]:
    """
    Compare current metrics against baseline.

    Args:
        current: Current benchmark results
        baseline: Baseline benchmark results
        threshold: Maximum acceptable regression (e.g., 0.10 = 10%)

    Returns:
        List of regression findings
    """
    regressions = []

    current_results = {r["operator_name"]: r for r in current.get("results", [])}
    baseline_results = {r["operator_name"]: r for r in baseline.get("results", [])}

    for op_name, current_data in current_results.items():
        if op_name not in baseline_results:
            continue

        baseline_data = baseline_results[op_name]

        # Skip if either has errors
        if current_data.get("error") or baseline_data.get("error"):
            continue

        current_metrics = current_data.get("metrics", {})
        baseline_metrics = baseline_data.get("metrics", {})

        # Compare mean latency
        current_mean = current_metrics.get("mean_ms", 0)
        baseline_mean = baseline_metrics.get("mean_ms", 0)

        if current_mean > 0 and baseline_mean > 0:
            change = (current_mean - baseline_mean) / baseline_mean
            if change > threshold:
                regressions.append({
                    "operator": op_name,
                    "metric": "mean_ms",
                    "current": current_mean,
                    "baseline": baseline_mean,
                    "change_percent": change * 100,
                    "severity": "HIGH" if change > 0.20 else "MEDIUM",
                })

        # Compare P99 latency (important for tail latency)
        current_p99 = current_metrics.get("p99_ms", 0)
        baseline_p99 = baseline_metrics.get("p99_ms", 0)

        if current_p99 > 0 and baseline_p99 > 0:
            change = (current_p99 - baseline_p99) / baseline_p99
            if change > threshold:
                regressions.append({
                    "operator": op_name,
                    "metric": "p99_ms",
                    "current": current_p99,
                    "baseline": baseline_p99,
                    "change_percent": change * 100,
                    "severity": "HIGH" if change > 0.20 else "MEDIUM",
                })

        # Compare throughput (inverse - lower is worse)
        current_throughput = current_metrics.get("throughput_ops_sec", 0)
        baseline_throughput = baseline_metrics.get("throughput_ops_sec", 0)

        if current_throughput > 0 and baseline_throughput > 0:
            change = (baseline_throughput - current_throughput) / baseline_throughput
            if change > threshold:
                regressions.append({
                    "operator": op_name,
                    "metric": "throughput_ops_sec",
                    "current": current_throughput,
                    "baseline": baseline_throughput,
                    "change_percent": change * 100,
                    "severity": "HIGH" if change > 0.20 else "MEDIUM",
                })

    return regressions


def check_targets(results: dict) -> List[Dict]:
    """
    Check if results meet performance targets.

    Args:
        results: Benchmark results

    Returns:
        List of target failures
    """
    failures = []

    for result in results.get("results", []):
        if result.get("error"):
            failures.append({
                "operator": result["operator_name"],
                "reason": f"Benchmark failed: {result['error']}",
            })
            continue

        if result.get("target_latency_ms") is not None:
            if not result.get("target_met", False):
                failures.append({
                    "operator": result["operator_name"],
                    "reason": (
                        f"Target not met: {result['metrics']['mean_ms']:.4f}ms > "
                        f"{result['target_latency_ms']:.2f}ms"
                    ),
                })

    return failures


def format_report(
    regressions: List[Dict],
    target_failures: List[Dict],
    current: dict,
    baseline: dict
) -> str:
    """Format a human-readable report"""
    lines = []
    lines.append("=" * 70)
    lines.append("PERFORMANCE REGRESSION CHECK REPORT")
    lines.append("=" * 70)
    lines.append("")

    # Summary
    lines.append("SUMMARY")
    lines.append("-" * 70)

    if not regressions and not target_failures:
        lines.append("Status: PASS - No regressions detected")
        lines.append("")
        lines.append(f"Current benchmark: {current.get('start_time', 'N/A')}")
        lines.append(f"Baseline: {baseline.get('start_time', 'N/A')}")
        lines.append(f"Total operators tested: {len(current.get('results', []))}")
    else:
        lines.append("Status: FAIL - Issues detected")
        lines.append("")
        lines.append(f"Regressions found: {len(regressions)}")
        lines.append(f"Target failures: {len(target_failures)}")

    lines.append("")

    # Regressions
    if regressions:
        lines.append("REGRESSIONS DETECTED")
        lines.append("-" * 70)

        for reg in regressions:
            severity_icon = "[!!]" if reg["severity"] == "HIGH" else "[!]"
            lines.append(
                f"{severity_icon} {reg['operator']}.{reg['metric']}: "
                f"{reg['current']:.4f} vs {reg['baseline']:.4f} "
                f"({reg['change_percent']:+.1f}%)"
            )

        lines.append("")

    # Target failures
    if target_failures:
        lines.append("TARGET FAILURES")
        lines.append("-" * 70)

        for failure in target_failures:
            lines.append(f"[!!] {failure['operator']}: {failure['reason']}")

        lines.append("")

    # Detailed results
    lines.append("DETAILED RESULTS")
    lines.append("-" * 70)
    lines.append("")

    for result in current.get("results", []):
        op_name = result["operator_name"].upper()
        lines.append(f"{op_name}:")

        if result.get("error"):
            lines.append(f"  ERROR: {result['error']}")
        else:
            metrics = result.get("metrics", {})
            lines.append(f"  Mean:    {metrics.get('mean_ms', 0):.4f} ms")
            lines.append(f"  Median:  {metrics.get('median_ms', 0):.4f} ms")
            lines.append(f"  P99:     {metrics.get('p99_ms', 0):.4f} ms")
            lines.append(
                f"  Throughput: {metrics.get('throughput_ops_sec', 0):.2f} ops/sec"
            )

            if result.get("target_latency_ms"):
                status = "PASS" if result.get("target_met") else "FAIL"
                lines.append(f"  Target: {result['target_latency_ms']:.2f}ms - {status}")

        lines.append("")

    lines.append("=" * 70)

    return "\n".join(lines)


def create_baseline(results: dict, output_path: str):
    """Create a baseline file from current results"""
    baseline = {
        "description": "Performance baseline for IRON operators",
        "created_from": results.get("config", {}),
        "results": []
    }

    for result in results.get("results", []):
        if not result.get("error"):
            baseline["results"].append({
                "operator_name": result["operator_name"],
                "metrics": result["metrics"],
            })

    with open(output_path, "w") as f:
        json.dump(baseline, f, indent=2)

    print(f"Baseline created: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Check for performance regressions in benchmark results"
    )

    parser.add_argument(
        "--current",
        type=str,
        required=True,
        help="Path to current benchmark results JSON"
    )

    parser.add_argument(
        "--baseline",
        type=str,
        required=True,
        help="Path to baseline results JSON"
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=0.10,
        help="Maximum acceptable regression (default: 0.10 = 10%%)"
    )

    parser.add_argument(
        "--create-baseline",
        type=str,
        help="Create baseline from current results"
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Write report to file instead of stdout"
    )

    parser.add_argument(
        "--exit-on-regression",
        action="store_true",
        help="Exit with code 1 if any regressions detected"
    )

    args = parser.parse_args()

    # Load results
    try:
        current = load_results(args.current)
    except FileNotFoundError:
        print(f"Error: Current results file not found: {args.current}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in current results: {e}")
        sys.exit(1)

    try:
        baseline = load_results(args.baseline)
    except FileNotFoundError:
        print(f"Error: Baseline file not found: {args.baseline}")
        if args.create_baseline:
            create_baseline(current, args.create_baseline)
            sys.exit(0)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in baseline: {e}")
        sys.exit(1)

    # Handle baseline creation
    if args.create_baseline:
        create_baseline(current, args.create_baseline)
        sys.exit(0)

    # Compare metrics
    regressions = compare_metrics(current, baseline, args.threshold)

    # Check targets
    target_failures = check_targets(current)

    # Generate report
    report = format_report(regressions, target_failures, current, baseline)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report written to: {args.output}")
    else:
        print(report)

    # Exit code
    if regressions or target_failures:
        if args.exit_on_regression:
            sys.exit(1)
        else:
            print("\nNote: Regressions detected but --exit-on-regression not set")
            sys.exit(0)
    else:
        print("\nAll checks passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()
