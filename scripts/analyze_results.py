#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Benchmark Results Analysis and Visualization

Comprehensive analysis tool for IRON benchmark results with:
- Statistical analysis and distribution charts
- Performance comparison visualizations
- Trend analysis over time
- Anomaly detection visualization
- Report generation in multiple formats

Usage:
    # Analyze latest results
    python scripts/analyze_results.py

    # Analyze specific result file
    python scripts/analyze_results.py --input results.json

    # Generate all charts
    python scripts/analyze_results.py --charts all

    # Analyze trends from history
    python scripts/analyze_results.py --trend-analysis

    # Generate full report
    python scripts/analyze_results.py --report full
"""

import argparse
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Optional imports
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    logger.warning("NumPy not available, some features limited")

try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    logger.warning("Matplotlib not available, charts disabled")


# =============================================================================
# Configuration
# =============================================================================

RESULTS_DIR = project_root / "iron" / "benchmarks" / "results"
HISTORY_FILE = RESULTS_DIR / "benchmark_history.json"
CHARTS_DIR = RESULTS_DIR / "charts"

# Performance targets for reference
TARGETS = {
    "rope": {"linux_npu": 0.5, "windows_npu": 0.55, "cpu_baseline": 5.0},
    "rmsnorm": {"linux_npu": 1.0, "windows_npu": 1.1, "cpu_baseline": 10.0},
    "silu": {"linux_npu": 0.3, "windows_npu": 0.33, "cpu_baseline": 3.0},
    "softmax": {"linux_npu": 2.0, "windows_npu": 2.2, "cpu_baseline": 20.0},
}


# =============================================================================
# Data Loading
# =============================================================================

def load_results(file_path: str) -> dict:
    """Load benchmark results from JSON file"""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Results file not found: {file_path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_history() -> List[dict]:
    """Load benchmark history"""
    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def load_latest_results() -> Optional[dict]:
    """Load latest benchmark results"""
    latest_file = RESULTS_DIR / "validation_latest.json"
    if latest_file.exists():
        return load_results(str(latest_file))

    # Try to find most recent benchmark file
    benchmark_files = sorted(
        RESULTS_DIR.glob("benchmark_*.json"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if benchmark_files:
        return load_results(str(benchmark_files[0]))

    return None


# =============================================================================
# Statistical Analysis
# =============================================================================

def analyze_distribution(results: dict) -> dict:
    """Analyze latency distribution for each operator"""
    analysis = {}

    for result in results.get("results", []):
        op_name = result.get("operator_name")
        if not op_name or result.get("error"):
            continue

        metrics = result.get("metrics", {})
        latencies = result.get("raw_latencies", [])

        op_analysis = {
            "mean": metrics.get("mean_ms", 0),
            "median": metrics.get("median_ms", 0),
            "std_dev": metrics.get("std_dev_ms", 0),
            "p95": metrics.get("p95_ms", 0),
            "p99": metrics.get("p99_ms", 0),
            "min": metrics.get("min_ms", 0),
            "max": metrics.get("max_ms", 0),
        }

        # Calculate coefficient of variation
        if op_analysis["mean"] > 0:
            op_analysis["cv_percent"] = (op_analysis["std_dev"] / op_analysis["mean"]) * 100
        else:
            op_analysis["cv_percent"] = 0

        # Determine stability rating
        cv = op_analysis["cv_percent"]
        if cv < 5:
            op_analysis["stability"] = "EXCELLENT"
        elif cv < 10:
            op_analysis["stability"] = "GOOD"
        elif cv < 20:
            op_analysis["stability"] = "ACCEPTABLE"
        else:
            op_analysis["stability"] = "POOR"

        analysis[op_name] = op_analysis

    return analysis


def compare_against_targets(results: dict) -> dict:
    """Compare results against performance targets"""
    comparison = {}

    for result in results.get("results", []):
        op_name = result.get("operator_name")
        if not op_name or op_name not in TARGETS:
            continue

        if result.get("error"):
            comparison[op_name] = {
                "status": "ERROR",
                "error": result.get("error"),
            }
            continue

        mean_ms = result.get("metrics", {}).get("mean_ms", 0)
        targets = TARGETS[op_name]

        comparison[op_name] = {
            "measured": mean_ms,
            "linux_npu": {
                "target": targets["linux_npu"],
                "ratio": mean_ms / targets["linux_npu"] if targets["linux_npu"] > 0 else 0,
                "passed": mean_ms <= targets["linux_npu"],
            },
            "windows_npu": {
                "target": targets["windows_npu"],
                "ratio": mean_ms / targets["windows_npu"] if targets["windows_npu"] > 0 else 0,
                "passed": mean_ms <= targets["windows_npu"],
            },
            "cpu_baseline": {
                "target": targets["cpu_baseline"],
                "ratio": mean_ms / targets["cpu_baseline"] if targets["cpu_baseline"] > 0 else 0,
                "passed": mean_ms <= targets["cpu_baseline"],
            },
        }

    return comparison


def analyze_trends(history: List[dict]) -> dict:
    """Analyze performance trends over time"""
    if not history:
        return {}

    # Collect data points per operator
    operator_data: Dict[str, List[dict]] = {}

    for entry in history:
        timestamp = entry.get("timestamp", "")
        results = entry.get("results", [])

        for result in results:
            op_name = result.get("operator_name")
            if not op_name or result.get("error"):
                continue

            mean_ms = result.get("metrics", {}).get("mean_ms", 0)
            if mean_ms <= 0:
                continue

            if op_name not in operator_data:
                operator_data[op_name] = []

            operator_data[op_name].append({
                "timestamp": timestamp,
                "mean_ms": mean_ms,
            })

    # Analyze each operator
    trends = {}
    for op_name, data_points in operator_data.items():
        if len(data_points) < 2:
            continue

        values = [dp["mean_ms"] for dp in data_points]

        # Calculate trend (simple linear regression)
        n = len(values)
        x_mean = n / 2
        y_mean = sum(values) / n

        numerator = sum((i - x_mean) * (v - y_mean) for i, v in enumerate(values))
        denominator = sum((i - x_mean) ** 2 for i in range(n))

        slope = numerator / denominator if denominator != 0 else 0

        # Determine trend direction
        if abs(slope) < 0.01 * y_mean:
            direction = "STABLE"
        elif slope < 0:
            direction = "IMPROVING"
        else:
            direction = "DEGRADING"

        trends[op_name] = {
            "data_points": len(data_points),
            "mean": y_mean,
            "min": min(values),
            "max": max(values),
            "slope": slope,
            "direction": direction,
            "first_value": values[0],
            "last_value": values[-1],
            "change_percent": ((values[-1] - values[0]) / values[0]) * 100 if values[0] > 0 else 0,
        }

    return trends


# =============================================================================
# Chart Generation
# =============================================================================

def generate_latency_comparison_chart(results: dict, output_path: Path):
    """Generate latency comparison bar chart"""
    if not HAS_MATPLOTLIB:
        logger.warning("Matplotlib not available, skipping chart generation")
        return None

    # Filter valid results
    valid_results = [r for r in results.get("results", []) if not r.get("error")]
    if not valid_results:
        logger.warning("No valid results for chart")
        return None

    operators = [r["operator_name"] for r in valid_results]
    means = [r["metrics"]["mean_ms"] for r in valid_results]
    p99s = [r["metrics"]["p99_ms"] for r in valid_results]

    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(operators))
    width = 0.35

    # Bars for mean and p99
    bars1 = ax.bar([i - width/2 for i in x], means, width, label='Mean', color='steelblue')
    bars2 = ax.bar([i + width/2 for i in x], p99s, width, label='P99', color='coral')

    # Target lines
    for i, op in enumerate(operators):
        if op in TARGETS:
            ax.axvline(x=i - 0.5, color='gray', linestyle='--', alpha=0.3)
            ax.text(i, max(means[i], p99s[i]) * 1.05,
                   f'Target: {TARGETS[op]["cpu_baseline"]:.1f}ms',
                   ha='center', fontsize=8, rotation=45)

    ax.set_ylabel('Latency (ms)')
    ax.set_title('Operator Latency Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels([op.upper() for op in operators])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}', ha='center', va='bottom', fontsize=9)

    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    logger.info(f"Chart saved: {output_path}")
    return output_path


def generate_target_achievement_chart(results: dict, output_path: Path):
    """Generate target achievement chart"""
    if not HAS_MATPLOTLIB:
        return None

    valid_results = [r for r in results.get("results", []) if not r.get("error")]
    if not valid_results:
        return None

    operators = [r["operator_name"] for r in valid_results]
    means = [r["metrics"]["mean_ms"] for r in valid_results]
    targets = [TARGETS.get(op, {}).get("cpu_baseline", 0) for op in operators]

    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(operators))

    # Color based on pass/fail
    colors = ['green' if m <= t else 'red' for m, t in zip(means, targets)]

    bars = ax.bar(x, means, color=colors, alpha=0.7, label='Measured')

    # Target line
    ax.plot(x, targets, 'r--', linewidth=2, label='Target')

    ax.set_ylabel('Latency (ms)')
    ax.set_title('Target Achievement (Green=PASS, Red=FAIL)')
    ax.set_xticks(x)
    ax.set_xticklabels([op.upper() for op in operators])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar, target in zip(bars, targets):
        height = bar.get_height()
        status = 'PASS' if height <= target else 'FAIL'
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}\n{status}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    logger.info(f"Chart saved: {output_path}")
    return output_path


def generate_throughput_chart(results: dict, output_path: Path):
    """Generate throughput comparison chart"""
    if not HAS_MATPLOTLIB:
        return None

    valid_results = [r for r in results.get("results", []) if not r.get("error")]
    if not valid_results:
        return None

    operators = [r["operator_name"] for r in valid_results]
    throughputs = [r["metrics"]["throughput_ops_sec"] for r in valid_results]

    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(operators))

    bars = ax.bar(x, throughputs, color='mediumpurple', alpha=0.7)

    ax.set_ylabel('Throughput (ops/sec)')
    ax.set_title('Operator Throughput')
    ax.set_xticks(x)
    ax.set_xticklabels([op.upper() for op in operators])
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar, val in zip(bars, throughputs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.0f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    logger.info(f"Chart saved: {output_path}")
    return output_path


def generate_variance_chart(results: dict, output_path: Path):
    """Generate variance/coefficient of variation chart"""
    if not HAS_MATPLOTLIB:
        return None

    valid_results = [r for r in results.get("results", []) if not r.get("error")]
    if not valid_results:
        return None

    operators = [r["operator_name"] for r in valid_results]
    means = [r["metrics"]["mean_ms"] for r in valid_results]
    std_devs = [r["metrics"]["std_dev_ms"] for r in valid_results]

    # Calculate CV percentage
    cv_percent = [(s/m)*100 if m > 0 else 0 for s, m in zip(std_devs, means)]

    # Color based on CV
    colors = []
    for cv in cv_percent:
        if cv < 5:
            colors.append('green')
        elif cv < 10:
            colors.append('yellowgreen')
        elif cv < 20:
            colors.append('orange')
        else:
            colors.append('red')

    fig, ax = plt.subplots(figsize=(10, 6))
    x = range(len(operators))

    bars = ax.bar(x, cv_percent, color=colors, alpha=0.7)

    # Threshold lines
    ax.axhline(y=5, color='green', linestyle='--', alpha=0.5, label='Excellent (<5%)')
    ax.axhline(y=10, color='orange', linestyle='--', alpha=0.5, label='Acceptable (<10%)')
    ax.axhline(y=20, color='red', linestyle='--', alpha=0.5, label='Poor (>20%)')

    ax.set_ylabel('Coefficient of Variation (%)')
    ax.set_title('Result Variance by Operator (Lower is Better)')
    ax.set_xticks(x)
    ax.set_xticklabels([op.upper() for op in operators])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar, val in zip(bars, cv_percent):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.1f}%', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    logger.info(f"Chart saved: {output_path}")
    return output_path


def generate_trend_chart(history: List[dict], output_path: Path):
    """Generate trend analysis chart"""
    if not HAS_MATPLOTLIB or not history:
        return None

    # Collect data per operator
    operator_data: Dict[str, List[Tuple[str, float]]] = {}

    for entry in history:
        timestamp = entry.get("timestamp", "")
        for result in entry.get("results", []):
            op_name = result.get("operator_name")
            if not op_name or result.get("error"):
                continue

            mean_ms = result.get("metrics", {}).get("mean_ms", 0)
            if mean_ms <= 0:
                continue

            if op_name not in operator_data:
                operator_data[op_name] = []
            operator_data[op_name].append((timestamp, mean_ms))

    if not operator_data:
        logger.warning("No trend data available")
        return None

    fig, ax = plt.subplots(figsize=(12, 6))

    colors = {'rope': 'blue', 'rmsnorm': 'green', 'silu': 'red', 'softmax': 'purple'}

    for op_name, data_points in operator_data.items():
        if len(data_points) < 2:
            continue

        # Parse timestamps
        timestamps = []
        values = []
        for ts, val in data_points:
            try:
                dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                timestamps.append(dt)
                values.append(val)
            except:
                continue

        if len(timestamps) < 2:
            continue

        color = colors.get(op_name, 'gray')
        ax.plot(timestamps, values, 'o-', color=color, label=op_name.upper(), markersize=6)

    ax.set_xlabel('Time')
    ax.set_ylabel('Mean Latency (ms)')
    ax.set_title('Performance Trend Over Time')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Format x-axis dates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    logger.info(f"Chart saved: {output_path}")
    return output_path


def generate_all_charts(results: dict, history: List[dict]) -> List[Path]:
    """Generate all available charts"""
    if not HAS_MATPLOTLIB:
        logger.warning("Matplotlib not available")
        return []

    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    charts = []

    # Individual charts
    chart_configs = [
        ("latency_comparison", generate_latency_comparison_chart, [results]),
        ("target_achievement", generate_target_achievement_chart, [results]),
        ("throughput", generate_throughput_chart, [results]),
        ("variance", generate_variance_chart, [results]),
        ("trend", generate_trend_chart, [history]),
    ]

    for name, generator, args in chart_configs:
        try:
            output_path = CHARTS_DIR / f"{name}_{timestamp}.png"
            result = generator(*args, output_path)
            if result:
                charts.append(result)
        except Exception as e:
            logger.warning(f"Could not generate {name} chart: {e}")

    # Create symlink to latest
    if charts:
        latest_dir = CHARTS_DIR / "latest"
        latest_dir.mkdir(exist_ok=True)

        for chart in charts:
            chart_name = chart.stem.split('_')[0]
            latest_path = latest_dir / f"{chart_name}.png"
            try:
                if latest_path.exists():
                    latest_path.unlink()
                latest_path.symlink_to(chart.name)
            except Exception as e:
                logger.debug(f"Could not create symlink: {e}")

    return charts


# =============================================================================
# Report Generation
# =============================================================================

def generate_text_report(
    results: dict,
    distribution: dict,
    target_comparison: dict,
    trends: Optional[dict] = None,
) -> str:
    """Generate text analysis report"""
    lines = []
    lines.append("=" * 70)
    lines.append("IRON BENCHMARK ANALYSIS REPORT")
    lines.append("=" * 70)
    lines.append("")

    # Timestamp
    timestamp = results.get("timestamp", "Unknown")
    lines.append(f"Generated: {timestamp}")
    lines.append("")

    # Distribution Analysis
    lines.append("DISTRIBUTION ANALYSIS")
    lines.append("-" * 70)

    for op_name, analysis in distribution.items():
        lines.append(f"\n{op_name.upper()}:")
        lines.append(f"  Mean: {analysis['mean']:.4f} ms")
        lines.append(f"  Std Dev: {analysis['std_dev']:.4f} ms")
        lines.append(f"  CV: {analysis['cv_percent']:.1f}%")
        lines.append(f"  Stability: {analysis['stability']}")

    lines.append("")

    # Target Comparison
    lines.append("\nTARGET COMPARISON")
    lines.append("-" * 70)

    for op_name, comparison in target_comparison.items():
        if comparison.get("status") == "ERROR":
            lines.append(f"\n{op_name.upper()}: ERROR - {comparison.get('error')}")
            continue

        lines.append(f"\n{op_name.upper()}:")
        lines.append(f"  Measured: {comparison['measured']:.4f} ms")

        for target_type in ["linux_npu", "windows_npu", "cpu_baseline"]:
            if target_type in comparison:
                tc = comparison[target_type]
                status = "PASS" if tc["passed"] else "FAIL"
                lines.append(
                    f"  {target_type.replace('_', ' ').title()}: "
                    f"{tc['target']:.2f}ms -> Ratio: {tc['ratio']:.2f}x [{status}]"
                )

    lines.append("")

    # Trend Analysis
    if trends:
        lines.append("\nTREND ANALYSIS")
        lines.append("-" * 70)

        for op_name, trend in trends.items():
            lines.append(f"\n{op_name.upper()}:")
            lines.append(f"  Data points: {trend['data_points']}")
            lines.append(f"  Trend: {trend['direction']}")
            lines.append(f"  Change: {trend['change_percent']:+.1f}%")
            lines.append(f"  Range: {trend['min']:.4f} - {trend['max']:.4f} ms")

    lines.append("")
    lines.append("=" * 70)

    return "\n".join(lines)


def generate_markdown_report(
    results: dict,
    system_info: dict,
    distribution: dict,
    target_comparison: dict,
    trends: Optional[dict] = None,
    charts: Optional[List[Path]] = None,
) -> str:
    """Generate Markdown analysis report"""
    lines = []
    lines.append("# IRON Benchmark Analysis Report")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    # System Info
    lines.append("## System Information")
    lines.append("")
    if system_info:
        plat = system_info.get("platform", {})
        hw = system_info.get("hardware", {})
        lines.append(f"- **Platform:** {plat.get('system', 'Unknown')} {plat.get('windows_edition', '')}")
        lines.append(f"- **Processor:** {plat.get('processor', 'Unknown')}")
        lines.append(f"- **Python:** {plat.get('python_version', 'Unknown')}")
        lines.append(f"- **NPU:** {hw.get('npu', hw.get('amd_device', 'Not detected'))}")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    total = len(results.get("results", []))
    errors = sum(1 for r in results.get("results", []) if r.get("error"))
    passed = sum(1 for r in results.get("results", []) if r.get("target_met"))

    lines.append(f"- **Total operators:** {total}")
    lines.append(f"- **Errors:** {errors}")
    lines.append(f"- **Targets passed:** {passed}/{total - errors}")
    lines.append("")

    # Charts
    if charts:
        lines.append("## Charts")
        lines.append("")
        for chart in charts:
            lines.append(f"![{chart.stem}]({chart.name})")
        lines.append("")

    # Distribution Analysis
    lines.append("## Distribution Analysis")
    lines.append("")
    lines.append("| Operator | Mean (ms) | Std Dev (ms) | CV (%) | Stability |")
    lines.append("|----------|-----------|--------------|--------|-----------|")

    for op_name, analysis in distribution.items():
        lines.append(
            f"| {op_name.upper()} | {analysis['mean']:.4f} | "
            f"{analysis['std_dev']:.4f} | {analysis['cv_percent']:.1f} | "
            f"{analysis['stability']} |"
        )
    lines.append("")

    # Target Comparison
    lines.append("## Target Comparison")
    lines.append("")
    lines.append("| Operator | Measured | CPU Target | Windows NPU | Linux NPU |")
    lines.append("|----------|----------|------------|-------------|-----------|")

    for op_name, comparison in target_comparison.items():
        if comparison.get("status") == "ERROR":
            lines.append(f"| {op_name.upper()} | ERROR | - | - | - |")
            continue

        measured = comparison.get("measured", 0)

        def fmt_target(tc):
            if tc.get("passed"):
                return f"{tc['target']:.2f}ms OK"
            return f"{tc['target']:.2f}ms FAIL"

        cpu = fmt_target(comparison.get("cpu_baseline", {}))
        win = fmt_target(comparison.get("windows_npu", {}))
        linux = fmt_target(comparison.get("linux_npu", {}))

        lines.append(
            f"| {op_name.upper()} | {measured:.4f}ms | {cpu} | {win} | {linux} |"
        )
    lines.append("")

    # Trend Analysis
    if trends:
        lines.append("## Trend Analysis")
        lines.append("")
        lines.append("| Operator | Trend | Change | Range |")
        lines.append("|----------|-------|--------|-------|")

        for op_name, trend in trends.items():
            lines.append(
                f"| {op_name.upper()} | {trend['direction']} | "
                f"{trend['change_percent']:+.1f}% | "
                f"{trend['min']:.4f}-{trend['max']:.4f}ms |"
            )
        lines.append("")

    lines.append("---")
    lines.append("*Generated by IRON Benchmark Analysis Tool*")

    return "\n".join(lines)


# =============================================================================
# CLI
# =============================================================================

def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="IRON Benchmark Results Analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze latest results
  python scripts/analyze_results.py

  # Analyze specific file
  python scripts/analyze_results.py --input results.json

  # Generate all charts
  python scripts/analyze_results.py --charts all

  # Generate full report
  python scripts/analyze_results.py --report full

  # Trend analysis only
  python scripts/analyze_results.py --trend-analysis
""",
    )

    parser.add_argument(
        "--input",
        type=str,
        help="Input results file (default: latest)",
    )

    parser.add_argument(
        "--charts",
        type=str,
        choices=["all", "latency", "target", "throughput", "variance", "trend"],
        help="Generate specific charts",
    )

    parser.add_argument(
        "--report",
        type=str,
        choices=["text", "markdown", "full"],
        help="Generate report in specified format",
    )

    parser.add_argument(
        "--trend-analysis",
        action="store_true",
        help="Perform trend analysis from history",
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Output file path",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        help="Output directory (default: results dir)",
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_args()

    logger.info("=" * 60)
    logger.info("IRON Benchmark Analysis")
    logger.info("=" * 60)

    # Determine output directory
    output_dir = Path(args.output_dir) if args.output_dir else RESULTS_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load results
    if args.input:
        logger.info(f"Loading results from: {args.input}")
        results = load_results(args.input)
    else:
        logger.info("Loading latest results...")
        results = load_latest_results()
        if not results:
            logger.error("No results found")
            sys.exit(1)

    # Load history
    history = load_history()

    # Perform analysis
    logger.info("Performing distribution analysis...")
    distribution = analyze_distribution(results)

    logger.info("Comparing against targets...")
    target_comparison = compare_against_targets(results)

    trends = None
    if args.trend_analysis or history:
        logger.info("Analyzing trends...")
        trends = analyze_trends(history)

    # Generate charts
    charts = []
    if args.charts:
        logger.info(f"Generating charts: {args.charts}")
        if args.charts == "all":
            charts = generate_all_charts(results, history)
        else:
            # Generate specific chart
            chart_generators = {
                "latency": generate_latency_comparison_chart,
                "target": generate_target_achievement_chart,
                "throughput": generate_throughput_chart,
                "variance": generate_variance_chart,
                "trend": generate_trend_chart,
            }
            if args.charts in chart_generators:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = output_dir / f"{args.charts}_{timestamp}.png"
                if args.charts == "trend":
                    result = chart_generators[args.charts](history, output_path)
                else:
                    result = chart_generators[args.charts](results, output_path)
                if result:
                    charts.append(result)

    # Generate report
    if args.report or not args.charts:
        logger.info("Generating report...")
        system_info = results.get("system_info", {})

        if args.report == "markdown" or args.report == "full":
            md_report = generate_markdown_report(
                results, system_info, distribution, target_comparison, trends, charts
            )
            if args.output:
                output_path = Path(args.output)
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = output_dir / f"analysis_{timestamp}.md"

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(md_report)
            logger.info(f"Markdown report saved: {output_path}")

        if args.report == "text" or args.report == "full":
            text_report = generate_text_report(
                results, distribution, target_comparison, trends
            )
            if args.output:
                output_path = Path(args.output)
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = output_dir / f"analysis_{timestamp}.txt"

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text_report)
            logger.info(f"Text report saved: {output_path}")

        if not args.report:
            # Default: print text report to console
            text_report = generate_text_report(
                results, distribution, target_comparison, trends
            )
            print(text_report)

    # Print summary
    logger.info("")
    logger.info("=" * 60)
    logger.info("ANALYSIS COMPLETE")
    logger.info("=" * 60)

    if charts:
        logger.info(f"Charts generated: {len(charts)}")
        for c in charts:
            logger.info(f"  - {c}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
