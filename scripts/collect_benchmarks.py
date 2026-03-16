#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Benchmark Data Collection Script

Automated data collection for IRON benchmarks with:
- Scheduled/iterative collection
- System state capture at collection time
- Result aggregation and history tracking
- Anomaly flagging during collection
- Export to multiple formats

Usage:
    # Single collection run
    python scripts/collect_benchmarks.py

    # Collect with multiple iterations for stability
    python scripts/collect_benchmarks.py --runs 5

    # Collect and update baseline
    python scripts/collect_benchmarks.py --update-baseline

    # Continuous collection (for thermal/stability testing)
    python scripts/collect_benchmarks.py --continuous --interval 60
"""

import argparse
import json
import logging
import os
import platform
import shutil
import subprocess
import sys
import time
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


# =============================================================================
# Configuration
# =============================================================================

BENCHMARKS_DIR = project_root / "iron" / "benchmarks"
RESULTS_DIR = project_root / "iron" / "benchmarks" / "results"
SCRIPTS_DIR = project_root / "scripts"
BASELINE_FILE = SCRIPTS_DIR / "baseline.json"
HISTORY_FILE = RESULTS_DIR / "benchmark_history.json"

# Default benchmark configuration
DEFAULT_ITERATIONS = 50
DEFAULT_WARMUP = 10
DEFAULT_OPERATORS = ["rope", "rmsnorm", "silu", "softmax"]


# =============================================================================
# System Information Collection
# =============================================================================

def get_system_info() -> dict:
    """Collect comprehensive system information"""
    info = {
        "timestamp": datetime.now().isoformat(),
        "platform": {
            "system": platform.system(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
        },
        "hardware": {
            "cpu_count": os.cpu_count() or 0,
        },
        "software": {},
    }

    # Windows-specific info
    if platform.system() == "Windows":
        try:
            import winreg
            with winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SOFTWARE\Microsoft\Windows NT\CurrentVersion"
            ) as key:
                info["platform"]["windows_edition"] = winreg.QueryValueEx(key, "EditionId")[0]
                info["platform"]["windows_build"] = winreg.QueryValueEx(key, "CurrentBuild")[0]
        except Exception as e:
            logger.debug(f"Could not get Windows edition: {e}")

        # Get memory info
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            c_ulonglong = ctypes.c_ulonglong

            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [
                    ('dwLength', ctypes.c_ulong),
                    ('dwMemoryLoad', ctypes.c_ulong),
                    ('ullTotalPhys', c_ulonglong),
                    ('ullAvailPhys', c_ulonglong),
                ]

            memoryStatus = MEMORYSTATUSEX()
            memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            if kernel32.GlobalMemoryStatusEx(ctypes.byref(memoryStatus)):
                info["hardware"]["total_memory_gb"] = round(
                    memoryStatus.ullTotalPhys / (1024 ** 3), 2
                )
                info["hardware"]["available_memory_gb"] = round(
                    memoryStatus.ullAvailPhys / (1024 ** 3), 2
                )
        except Exception as e:
            logger.debug(f"Could not get memory info: {e}")

        # Detect NPU
        try:
            result = subprocess.run(
                ["powershell", "-Command",
                 "Get-PnpDevice -Class 'System' -Status 'OK' | "
                 "Where-Object {$_.FriendlyName -like '*Ryzen*AI*' -or "
                 "$_.FriendlyName -like '*NPU*'} | "
                 "Select-Object -First 1 -ExpandProperty FriendlyName"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.stdout.strip():
                info["hardware"]["npu"] = result.stdout.strip()
            else:
                # Try alternative method
                result = subprocess.run(
                    ["powershell", "-Command",
                     "Get-ChildItem Win32_PnPEntity | "
                     "Where-Object {$_.Name -like '*AMD*'} | "
                     "Select-Object -First 1 -ExpandProperty Name"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.stdout.strip():
                    info["hardware"]["amd_device"] = result.stdout.strip()
        except Exception as e:
            logger.debug(f"NPU detection failed: {e}")

    # PyTorch info
    try:
        import torch
        info["software"]["torch"] = {
            "version": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
        }
        if torch.cuda.is_available():
            info["software"]["torch"]["cuda_version"] = torch.version.cuda
            info["software"]["torch"]["gpu_name"] = torch.cuda.get_device_name(0)
    except ImportError:
        info["software"]["torch"] = {"error": "not installed"}

    # NumPy info
    try:
        import numpy
        info["software"]["numpy"] = {"version": numpy.__version__}
    except ImportError:
        info["software"]["numpy"] = {"error": "not installed"}

    # ML dtypes info
    try:
        import ml_dtypes
        info["software"]["ml_dtypes"] = {"version": ml_dtypes.__version__}
    except ImportError:
        info["software"]["ml_dtypes"] = {"error": "not installed"}

    return info


def get_process_info() -> dict:
    """Get current process information"""
    import os
    process = os.getpid()

    info = {
        "pid": process,
        "cpu_percent": 0.0,
        "memory_mb": 0.0,
    }

    try:
        import psutil
        p = psutil.Process(process)
        info["cpu_percent"] = p.cpu_percent()
        info["memory_mb"] = p.memory_info().rss / (1024 * 1024)
    except ImportError:
        pass

    return info


# =============================================================================
# Benchmark Execution
# =============================================================================

def run_benchmark(
    operators: Optional[List[str]] = None,
    iterations: int = DEFAULT_ITERATIONS,
    warmup: int = DEFAULT_WARMUP,
    verbose: bool = False,
) -> dict:
    """
    Run benchmark and collect results.

    Args:
        operators: List of operators to benchmark (None = all)
        iterations: Number of timed iterations
        warmup: Number of warmup iterations
        verbose: Enable verbose output

    Returns:
        Benchmark results dictionary
    """
    operators = operators or DEFAULT_OPERATORS

    logger.info(f"Running benchmarks: {operators}")
    logger.info(f"Iterations: {iterations}, Warmup: {warmup}")

    # Build command
    cmd = [
        sys.executable,
        "-m",
        "iron.benchmarks.baseline_bench",
        "--iterations", str(iterations),
        "--warmup", str(warmup),
        "--output", "json",
    ]

    if len(operators) == 1:
        cmd.extend(["--operator", operators[0]])

    if verbose:
        cmd.append("--verbose")

    # Run benchmark
    start_time = time.perf_counter()

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(project_root),
            timeout=300,  # 5 minute timeout
        )

        duration = time.perf_counter() - start_time

        # Parse JSON output
        if result.stdout:
            # Find JSON in output
            json_start = result.stdout.find('{')
            json_end = result.stdout.rfind('}') + 1
            if json_start >= 0 and json_end > json_start:
                json_str = result.stdout[json_start:json_end]
                benchmark_data = json.loads(json_str)
            else:
                benchmark_data = {"error": "Could not parse JSON output", "raw_output": result.stdout}
        else:
            benchmark_data = {"error": "No output from benchmark", "stderr": result.stderr}

        # Add metadata
        benchmark_data["collection_metadata"] = {
            "duration_sec": duration,
            "exit_code": result.returncode,
            "operators_requested": operators,
        }

        return benchmark_data

    except subprocess.TimeoutExpired:
        logger.error("Benchmark timed out")
        return {"error": "Benchmark timed out after 300 seconds"}
    except Exception as e:
        logger.error(f"Benchmark execution failed: {e}")
        return {"error": str(e)}


# =============================================================================
# Result Management
# =============================================================================

def save_results(results: dict, output_path: Optional[Path] = None) -> Path:
    """Save benchmark results to file"""
    if output_path is None:
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = RESULTS_DIR / f"benchmark_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)

    logger.info(f"Results saved to: {output_path}")
    return output_path


def load_history() -> List[dict]:
    """Load benchmark history"""
    if not HISTORY_FILE.exists():
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_to_history(results: dict, system_info: dict):
    """Add results to history file"""
    history = load_history()

    entry = {
        "timestamp": datetime.now().isoformat(),
        "system_info": system_info,
        "results": results.get("results", []),
        "summary": {
            "total_operators": len(results.get("results", [])),
            "errors": sum(1 for r in results.get("results", []) if r.get("error")),
        },
    }

    history.append(entry)

    # Keep last 100 entries
    if len(history) > 100:
        history = history[-100:]

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, default=str)

    logger.info(f"History updated ({len(history)} entries)")


def update_baseline(results: dict):
    """Update baseline file with current results"""
    baseline = {
        "description": "Performance baseline for IRON operators",
        "created_date": datetime.now().strftime("%Y-%m-%d"),
        "created_from": results.get("collection_metadata", {}),
        "results": [],
        "targets": {}
    }

    for result in results.get("results", []):
        if not result.get("error"):
            baseline["results"].append({
                "operator_name": result["operator_name"],
                "input_shape": result.get("input_shape", []),
                "metrics": result.get("metrics", {}),
            })

            # Add targets
            op_name = result["operator_name"]
            if "targets" in result:
                baseline["targets"][op_name] = {
                    "target_latency_ms": result["targets"].get("linux_npu_ms", 0),
                    "description": result.get("description", ""),
                }

    SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    with open(BASELINE_FILE, "w", encoding="utf-8") as f:
        json.dump(baseline, f, indent=2)

    logger.info(f"Baseline updated: {BASELINE_FILE}")


def export_results(
    results: dict,
    system_info: dict,
    format: str = "all",
    output_dir: Optional[Path] = None,
) -> List[Path]:
    """Export results in various formats"""
    output_dir = output_dir or RESULTS_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    paths = []

    if format in ("all", "json"):
        json_path = output_dir / f"export_{timestamp}.json"
        export_data = {
            "system_info": system_info,
            "benchmark_results": results,
            "export_timestamp": datetime.now().isoformat(),
        }
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, default=str)
        paths.append(json_path)

    if format in ("all", "csv"):
        csv_path = output_dir / f"export_{timestamp}.csv"
        with open(csv_path, "w", encoding="utf-8") as f:
            # Header
            f.write("Operator,Mean_ms,Median_ms,P99_ms,Throughput_ops,Bandwidth_Gbps,Target_met\n")

            # Data rows
            for result in results.get("results", []):
                if result.get("error"):
                    continue
                metrics = result.get("metrics", {})
                f.write(
                    f"{result['operator_name']},"
                    f"{metrics.get('mean_ms', 0):.4f},"
                    f"{metrics.get('median_ms', 0):.4f},"
                    f"{metrics.get('p99_ms', 0):.4f},"
                    f"{metrics.get('throughput_ops_sec', 0):.2f},"
                    f"{metrics.get('memory_bandwidth_gbps', 0):.4f},"
                    f"{result.get('target_met', 'N/A')}\n"
                )
        paths.append(csv_path)

    if format in ("all", "markdown"):
        md_path = output_dir / f"export_{timestamp}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# IRON Benchmark Results\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # System info
            f.write("## System Information\n\n")
            plat = system_info.get("platform", {})
            f.write(f"- **Platform:** {plat.get('system', 'Unknown')} ")
            f.write(f"{plat.get('windows_edition', '')}\n")
            f.write(f"- **Processor:** {plat.get('processor', 'Unknown')}\n")
            f.write(f"- **Python:** {plat.get('python_version', 'Unknown')}\n\n")

            # Results table
            f.write("## Results\n\n")
            f.write("| Operator | Mean (ms) | Median (ms) | P99 (ms) | Throughput (ops/s) | Target |\n")
            f.write("|----------|-----------|-------------|----------|-------------------|--------|\n")

            for result in results.get("results", []):
                if result.get("error"):
                    f.write(f"| {result['operator_name']} | ERROR: {result['error']} | | | | |\n")
                    continue

                metrics = result.get("metrics", {})
                target_status = "PASS" if result.get("target_met") else "FAIL"
                f.write(
                    f"| {result['operator_name'].upper()} | "
                    f"{metrics.get('mean_ms', 0):.4f} | "
                    f"{metrics.get('median_ms', 0):.4f} | "
                    f"{metrics.get('p99_ms', 0):.4f} | "
                    f"{metrics.get('throughput_ops_sec', 0):.2f} | "
                    f"{target_status} |\n"
                )
        paths.append(md_path)

    logger.info(f"Exported results to {len(paths)} files")
    return paths


# =============================================================================
# Main Collection Functions
# =============================================================================

def collect_single(
    operators: Optional[List[str]] = None,
    iterations: int = DEFAULT_ITERATIONS,
    warmup: int = DEFAULT_WARMUP,
    save: bool = True,
    update_history: bool = True,
    verbose: bool = False,
) -> Tuple[dict, dict]:
    """
    Perform single benchmark collection.

    Returns:
        Tuple of (results, system_info)
    """
    # Capture system info
    logger.info("Collecting system information...")
    system_info = get_system_info()
    process_info = get_process_info()
    system_info["process"] = process_info

    logger.info(f"Platform: {system_info['platform']['system']}")
    logger.info(f"Processor: {system_info['platform']['processor']}")
    logger.info(f"Python: {system_info['platform']['python_version']}")

    if "npu" in system_info.get("hardware", {}):
        logger.info(f"NPU: {system_info['hardware']['npu']}")

    # Run benchmarks
    logger.info("")
    results = run_benchmark(
        operators=operators,
        iterations=iterations,
        warmup=warmup,
        verbose=verbose,
    )

    # Save results
    if save:
        save_results(results)
        save_to_history(results, system_info)

    return results, system_info


def collect_multiple(
    runs: int = 5,
    operators: Optional[List[str]] = None,
    iterations: int = DEFAULT_ITERATIONS,
    warmup: int = DEFAULT_WARMUP,
    delay_between_runs: int = 5,
    verbose: bool = False,
) -> List[dict]:
    """
    Perform multiple benchmark runs for stability analysis.

    Args:
        runs: Number of runs to perform
        operators: Operators to benchmark
        iterations: Iterations per run
        warmup: Warmup iterations per run
        delay_between_runs: Seconds to wait between runs
        verbose: Enable verbose output

    Returns:
        List of result dictionaries
    """
    all_results = []

    for i in range(runs):
        logger.info(f"\n{'='*50}")
        logger.info(f"RUN {i+1}/{runs}")
        logger.info(f"{'='*50}")

        results, _ = collect_single(
            operators=operators,
            iterations=iterations,
            warmup=warmup,
            save=True,
            update_history=False,  # Don't update history for intermediate runs
            verbose=verbose,
        )

        all_results.append(results)

        if i < runs - 1 and delay_between_runs > 0:
            logger.info(f"Waiting {delay_between_runs}s before next run...")
            time.sleep(delay_between_runs)

    # Save aggregated results
    aggregated = {
        "timestamp": datetime.now().isoformat(),
        "runs": runs,
        "results_per_run": all_results,
        "aggregated": aggregate_results(all_results),
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    agg_path = RESULTS_DIR / f"benchmark_aggregated_{timestamp}.json"
    with open(agg_path, "w", encoding="utf-8") as f:
        json.dump(aggregated, f, indent=2, default=str)

    logger.info(f"Aggregated results saved to: {agg_path}")

    # Update history once with aggregated data
    save_to_history(aggregated["aggregated"], get_system_info())

    return all_results


def aggregate_results(results_list: List[dict]) -> dict:
    """Aggregate multiple benchmark runs"""
    if not results_list:
        return {}

    # Collect all results per operator
    operator_results: Dict[str, List[dict]] = {}

    for run_data in results_list:
        for result in run_data.get("results", []):
            op_name = result.get("operator_name")
            if not op_name or result.get("error"):
                continue

            if op_name not in operator_results:
                operator_results[op_name] = []
            operator_results[op_name].append(result)

    # Calculate aggregated statistics
    aggregated = {"results": []}

    for op_name, op_results in operator_results.items():
        if not op_results:
            continue

        # Collect metrics across runs
        metrics_collection: Dict[str, List[float]] = {}

        for result in op_results:
            metrics = result.get("metrics", {})
            for key, value in metrics.items():
                if isinstance(value, (int, float)) and value > 0:
                    if key not in metrics_collection:
                        metrics_collection[key] = []
                    metrics_collection[key].append(value)

        # Calculate aggregated metrics
        agg_result = {
            "operator_name": op_name,
            "input_shape": op_results[0].get("input_shape", []),
            "runs": len(op_results),
            "metrics": {},
            "statistics": {},
        }

        for metric_name, values in metrics_collection.items():
            agg_result["metrics"][f"{metric_name}_mean"] = sum(values) / len(values)
            agg_result["statistics"][metric_name] = {
                "min": min(values),
                "max": max(values),
                "mean": sum(values) / len(values),
                "range": max(values) - min(values),
            }

        aggregated["results"].append(agg_result)

    aggregated["timestamp"] = datetime.now().isoformat()
    aggregated["total_runs"] = len(results_list)

    return aggregated


# =============================================================================
# CLI
# =============================================================================

def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="IRON Benchmark Data Collection",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single collection run
  python scripts/collect_benchmarks.py

  # Multiple runs for stability
  python scripts/collect_benchmarks.py --runs 5

  # Update baseline with current results
  python scripts/collect_benchmarks.py --update-baseline

  # Export in all formats
  python scripts/collect_benchmarks.py --export all

  # Specific operators only
  python scripts/collect_benchmarks.py --operator rope --operator rmsnorm
""",
    )

    parser.add_argument(
        "--runs",
        type=int,
        default=1,
        help="Number of benchmark runs (default: 1)",
    )

    parser.add_argument(
        "--iterations",
        type=int,
        default=DEFAULT_ITERATIONS,
        help=f"Number of iterations per run (default: {DEFAULT_ITERATIONS})",
    )

    parser.add_argument(
        "--warmup",
        type=int,
        default=DEFAULT_WARMUP,
        help=f"Warmup iterations (default: {DEFAULT_WARMUP})",
    )

    parser.add_argument(
        "--operator",
        type=str,
        action="append",
        dest="operators",
        choices=["rope", "rmsnorm", "silu", "softmax"],
        help="Specific operator(s) to benchmark",
    )

    parser.add_argument(
        "--delay",
        type=int,
        default=5,
        help="Seconds between runs (default: 5)",
    )

    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="Update baseline file with current results",
    )

    parser.add_argument(
        "--export",
        type=str,
        choices=["json", "csv", "markdown", "all"],
        help="Export results in specified format",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        help="Output directory (default: iron/benchmarks/results)",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    return parser.parse_args()


def main():
    """Main entry point"""
    args = parse_args()

    logger.info("=" * 60)
    logger.info("IRON Benchmark Data Collection")
    logger.info("=" * 60)

    output_dir = Path(args.output_dir) if args.output_dir else None

    if args.runs > 1:
        # Multiple runs
        all_results = collect_multiple(
            runs=args.runs,
            operators=args.operators,
            iterations=args.iterations,
            warmup=args.warmup,
            delay_between_runs=args.delay,
            verbose=args.verbose,
        )
        final_results = all_results[-1]  # Use last run for baseline
    else:
        # Single run
        final_results, _ = collect_single(
            operators=args.operators,
            iterations=args.iterations,
            warmup=args.warmup,
            save=True,
            update_history=True,
            verbose=args.verbose,
        )

    # Update baseline if requested
    if args.update_baseline:
        logger.info("")
        logger.info("Updating baseline...")
        update_baseline(final_results)

    # Export if requested
    if args.export:
        logger.info("")
        logger.info(f"Exporting results as {args.export}...")
        system_info = get_system_info()
        export_results(
            final_results,
            system_info,
            format=args.export,
            output_dir=output_dir,
        )

    # Print summary
    logger.info("")
    logger.info("=" * 60)
    logger.info("COLLECTION COMPLETE")
    logger.info("=" * 60)

    errors = sum(1 for r in final_results.get("results", []) if r.get("error"))
    total = len(final_results.get("results", []))
    logger.info(f"Operators: {total}, Errors: {errors}")

    if args.export:
        logger.info(f"Results exported to: {output_dir or RESULTS_DIR}")

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
