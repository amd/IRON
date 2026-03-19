#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Benchmark Visualization Tools

This module provides visualization utilities for IRON benchmark results,
including tile size scaling charts, column configuration charts, and
heatmap visualizations for performance analysis.

Features:
- Tile size scaling line charts with dual y-axis (latency + bandwidth)
- Column configuration bar charts with error bars and speedup lines
- Heatmap visualizations for configuration space exploration
- CLI interface for easy chart generation
- Output in PNG and SVG formats at 150 DPI

Usage:
    # Generate all charts from a benchmark JSON file
    python -m iron.benchmarks.visualize -i results/benchmark.json -o results/charts -t all

    # Generate only tile size chart
    python -m iron.benchmarks.visualize -i results/benchmark.json -t tile_size

    # Generate heatmap with specific format
    python -m iron.benchmarks.visualize -i results/benchmark.json -t heatmap -f svg
"""

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import matplotlib

    matplotlib.use("Agg")  # Non-interactive backend for Windows compatibility
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError as e:
    print(f"Warning: Could not import matplotlib/numpy: {e}")
    print("Install with: pip install matplotlib numpy")
    sys.exit(1)


# =============================================================================
# Data Classes for Report Structures
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


@dataclass
class TileSizeScalingReport:
    """Complete tile size scaling study report"""

    operator_name: str
    input_shape: tuple
    tile_size_results: List[TileSizeScalingResult]
    optimal_tile_size: Optional[int] = None
    optimal_latency_ms: Optional[float] = None
    worst_tile_size: Optional[int] = None
    worst_latency_ms: Optional[float] = None
    scaling_efficiency: float = 0.0
    recommendation: Optional[str] = None
    start_time: str = ""
    end_time: str = ""
    total_duration_sec: float = 0.0


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


@dataclass
class ColumnScalingReport:
    """Complete column scaling study report"""

    operator_name: str
    input_shape: tuple
    column_results: List[ColumnScalingResult]
    optimal_num_columns: Optional[int] = None
    optimal_latency_ms: Optional[float] = None
    worst_num_columns: Optional[int] = None
    worst_latency_ms: Optional[float] = None
    scaling_efficiency: float = 0.0
    column_efficiency: float = 0.0
    recommendation: Optional[str] = None
    start_time: str = ""
    end_time: str = ""
    total_duration_sec: float = 0.0


# =============================================================================
# Output Directory Utilities
# =============================================================================


def create_output_dir(output_dir: str) -> Path:
    """
    Create output directory if it doesn't exist.

    Args:
        output_dir: Path to the output directory

    Returns:
        Path object for the output directory
    """
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_timestamp() -> str:
    """
    Get current timestamp string for file naming.

    Returns:
        Timestamp string in YYYYMMDD_HHMMSS format
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def load_results_from_json(json_path: str) -> Dict[str, Any]:
    """
    Load benchmark results from a JSON file.

    Args:
        json_path: Path to the JSON file containing benchmark results

    Returns:
        Dictionary containing the benchmark data

    Raises:
        FileNotFoundError: If the JSON file doesn't exist
        json.JSONDecodeError: If the JSON is invalid
    """
    path = Path(json_path)
    if not path.exists():
        raise FileNotFoundError(f"Benchmark results file not found: {json_path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def _dict_to_tile_report(data: Dict[str, Any]) -> TileSizeScalingReport:
    """
    Convert a dictionary to a TileSizeScalingReport.

    Args:
        data: Dictionary containing tile size scaling data

    Returns:
        TileSizeScalingReport object
    """
    tile_size_results = []
    for result_data in data.get("tile_size_results", []):
        result = TileSizeScalingResult(
            tile_size=result_data.get("tile_size", 0),
            mean_latency_ms=result_data.get("mean_latency_ms", 0.0),
            median_latency_ms=result_data.get("median_latency_ms", 0.0),
            std_dev_ms=result_data.get("std_dev_ms", 0.0),
            p95_ms=result_data.get("p95_ms", 0.0),
            p99_ms=result_data.get("p99_ms", 0.0),
            min_ms=result_data.get("min_ms", 0.0),
            max_ms=result_data.get("max_ms", 0.0),
            throughput_ops_sec=result_data.get("throughput_ops_sec", 0.0),
            memory_bandwidth_gbps=result_data.get("memory_bandwidth_gbps", 0.0),
            iterations=result_data.get("iterations", 0),
            timestamp=result_data.get("timestamp", ""),
        )
        tile_size_results.append(result)

    input_shape = data.get("input_shape", ())
    if isinstance(input_shape, list):
        input_shape = tuple(input_shape)

    return TileSizeScalingReport(
        operator_name=data.get("operator_name", "unknown"),
        input_shape=input_shape,
        tile_size_results=tile_size_results,
        optimal_tile_size=data.get("optimal_tile_size"),
        optimal_latency_ms=data.get("optimal_latency_ms"),
        worst_tile_size=data.get("worst_tile_size"),
        worst_latency_ms=data.get("worst_latency_ms"),
        scaling_efficiency=data.get("scaling_efficiency", 0.0),
        recommendation=data.get("recommendation"),
        start_time=data.get("start_time", ""),
        end_time=data.get("end_time", ""),
        total_duration_sec=data.get("total_duration_sec", 0.0),
    )


def _dict_to_column_report(data: Dict[str, Any]) -> ColumnScalingReport:
    """
    Convert a dictionary to a ColumnScalingReport.

    Args:
        data: Dictionary containing column scaling data

    Returns:
        ColumnScalingReport object
    """
    column_results = []
    for result_data in data.get("column_results", []):
        result = ColumnScalingResult(
            num_columns=result_data.get("num_columns", 0),
            mean_latency_ms=result_data.get("mean_latency_ms", 0.0),
            median_latency_ms=result_data.get("median_latency_ms", 0.0),
            std_dev_ms=result_data.get("std_dev_ms", 0.0),
            p95_ms=result_data.get("p95_ms", 0.0),
            p99_ms=result_data.get("p99_ms", 0.0),
            min_ms=result_data.get("min_ms", 0.0),
            max_ms=result_data.get("max_ms", 0.0),
            throughput_ops_sec=result_data.get("throughput_ops_sec", 0.0),
            memory_bandwidth_gbps=result_data.get("memory_bandwidth_gbps", 0.0),
            iterations=result_data.get("iterations", 0),
            timestamp=result_data.get("timestamp", ""),
        )
        column_results.append(result)

    input_shape = data.get("input_shape", ())
    if isinstance(input_shape, list):
        input_shape = tuple(input_shape)

    return ColumnScalingReport(
        operator_name=data.get("operator_name", "unknown"),
        input_shape=input_shape,
        column_results=column_results,
        optimal_num_columns=data.get("optimal_num_columns"),
        optimal_latency_ms=data.get("optimal_latency_ms"),
        worst_num_columns=data.get("worst_num_columns"),
        worst_latency_ms=data.get("worst_latency_ms"),
        scaling_efficiency=data.get("scaling_efficiency", 0.0),
        column_efficiency=data.get("column_efficiency", 0.0),
        recommendation=data.get("recommendation"),
        start_time=data.get("start_time", ""),
        end_time=data.get("end_time", ""),
        total_duration_sec=data.get("total_duration_sec", 0.0),
    )


# =============================================================================
# Phase 1 - Core Visualizations
# =============================================================================


class TileSizePlotter:
    """
    Generates tile size scaling visualization charts.

    Creates line charts showing latency and memory bandwidth
    as a function of tile size, with optimal configuration marked.
    """

    def __init__(self):
        """Initialize the TileSizePlotter"""
        self.dpi = 150
        self.figsize = (12, 7)
        self.colors = {
            "latency": "#2E86AB",
            "bandwidth": "#A23B72",
            "optimal": "#28A745",
            "grid": "#E0E0E0",
        }

    def generate_chart(self, report: TileSizeScalingReport, output_path: str) -> str:
        """
        Generate a tile size scaling chart.

        Creates a line chart with:
        - Tile size on x-axis (log scale)
        - Primary y-axis: Mean latency (ms)
        - Secondary y-axis: Memory bandwidth (GB/s)
        - Vertical green line marking optimal tile size

        Args:
            report: TileSizeScalingReport containing benchmark data
            output_path: Path where the chart will be saved

        Returns:
            The file path where the chart was saved
        """
        # Extract data
        tile_sizes = [r.tile_size for r in report.tile_size_results]
        latencies = [r.mean_latency_ms for r in report.tile_size_results]
        bandwidths = [r.memory_bandwidth_gbps for r in report.tile_size_results]
        std_devs = [r.std_dev_ms for r in report.tile_size_results]

        if not tile_sizes:
            raise ValueError("No tile size results to plot")

        # Create figure and primary axis
        fig, ax1 = plt.subplots(figsize=self.figsize)
        fig.suptitle(
            f"Tile Size Scaling Analysis - {report.operator_name.upper()}\n"
            f"Input Shape: {report.input_shape}",
            fontsize=14,
            fontweight="bold",
        )

        # Plot latency on primary y-axis (left)
        ax1.plot(
            tile_sizes,
            latencies,
            marker="o",
            linewidth=2,
            markersize=8,
            color=self.colors["latency"],
            label="Mean Latency",
        )

        # Add error bars for standard deviation
        ax1.errorbar(
            tile_sizes,
            latencies,
            yerr=std_devs,
            fmt="none",
            ecolor=self.colors["latency"],
            capsize=4,
            alpha=0.7,
        )

        # Configure primary axis
        ax1.set_xlabel("Tile Size", fontsize=12, fontweight="bold")
        ax1.set_ylabel(
            "Mean Latency (ms)",
            fontsize=12,
            fontweight="bold",
            color=self.colors["latency"],
        )
        ax1.tick_params(axis="y", labelcolor=self.colors["latency"])
        ax1.set_xscale("log")
        ax1.grid(True, alpha=0.3, color=self.colors["grid"])
        ax1.set_xticks(tile_sizes)
        ax1.get_xaxis().set_major_formatter(
            plt.FuncFormatter(lambda x, p: format(int(x), ","))
        )

        # Create secondary y-axis for bandwidth
        ax2 = ax1.twinx()
        ax2.plot(
            tile_sizes,
            bandwidths,
            marker="s",
            linewidth=2,
            markersize=8,
            color=self.colors["bandwidth"],
            label="Memory Bandwidth",
        )

        # Configure secondary axis
        ax2.set_ylabel(
            "Memory Bandwidth (GB/s)",
            fontsize=12,
            fontweight="bold",
            color=self.colors["bandwidth"],
        )
        ax2.tick_params(axis="y", labelcolor=self.colors["bandwidth"])
        ax2.grid(False)

        # Mark optimal tile size with vertical line
        if report.optimal_tile_size is not None:
            ax1.axvline(
                x=report.optimal_tile_size,
                color=self.colors["optimal"],
                linestyle="--",
                linewidth=2,
                label=f"Optimal Tile Size ({report.optimal_tile_size})",
            )

        # Combine legends from both axes
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="best", fontsize=10)

        # Add annotation for optimal latency if available
        if (
            report.optimal_tile_size is not None
            and report.optimal_latency_ms is not None
        ):
            ax1.annotate(
                f"Optimal: {report.optimal_latency_ms:.4f} ms",
                xy=(report.optimal_tile_size, report.optimal_latency_ms),
                xytext=(10, 10),
                textcoords="offset points",
                bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
                fontsize=10,
                fontweight="bold",
            )

        plt.tight_layout()

        # Ensure output directory exists
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        # Save the chart
        plt.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)

        return str(output_path)


class ColumnConfigPlotter:
    """
    Generates column configuration visualization charts.

    Creates bar charts showing latency as a function of column count,
    with error bars and speedup comparison.
    """

    def __init__(self):
        """Initialize the ColumnConfigPlotter"""
        self.dpi = 150
        self.figsize = (12, 7)
        self.colors = {
            "latency": "#2E86AB",
            "speedup": "#28A745",
            "optimal": "#FF8C00",
            "grid": "#E0E0E0",
        }

    def generate_chart(self, report: ColumnScalingReport, output_path: str) -> str:
        """
        Generate a column configuration chart.

        Creates a bar chart with:
        - Column count on x-axis
        - Primary y-axis: Mean latency (ms) with error bars
        - Secondary y-axis: Speedup vs 1-column configuration
        - Marked optimal column count

        Args:
            report: ColumnScalingReport containing benchmark data
            output_path: Path where the chart will be saved

        Returns:
            The file path where the chart was saved
        """
        # Extract data
        columns = [r.num_columns for r in report.column_results]
        latencies = [r.mean_latency_ms for r in report.column_results]
        std_devs = [r.std_dev_ms for r in report.column_results]

        if not columns:
            raise ValueError("No column results to plot")

        # Calculate speedup vs 1-column configuration
        baseline_latency = latencies[0] if columns[0] == 1 else latencies[0]
        speedups = [baseline_latency / lat if lat > 0 else 1.0 for lat in latencies]

        # Create figure and primary axis
        fig, ax1 = plt.subplots(figsize=self.figsize)
        fig.suptitle(
            f"Column Configuration Scaling - {report.operator_name.upper()}\n"
            f"Input Shape: {report.input_shape}",
            fontsize=14,
            fontweight="bold",
        )

        # Set up x-axis positions
        x_pos = np.arange(len(columns))
        bar_width = 0.6

        # Plot latency bars on primary y-axis
        bars = ax1.bar(
            x_pos,
            latencies,
            width=bar_width,
            color=self.colors["latency"],
            alpha=0.8,
            label="Mean Latency",
            yerr=std_devs,
            error_kw={"capsize": 4, "ecolor": "black", "alpha": 0.7},
        )

        # Configure primary axis
        ax1.set_xlabel("Number of Columns", fontsize=12, fontweight="bold")
        ax1.set_ylabel(
            "Mean Latency (ms)",
            fontsize=12,
            fontweight="bold",
            color=self.colors["latency"],
        )
        ax1.tick_params(axis="y", labelcolor=self.colors["latency"])
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels([str(c) for c in columns])
        ax1.grid(True, alpha=0.3, color=self.colors["grid"], axis="y")

        # Create secondary y-axis for speedup
        ax2 = ax1.twinx()
        ax2.plot(
            x_pos,
            speedups,
            marker="D",
            linewidth=2,
            markersize=10,
            color=self.colors["speedup"],
            label="Speedup vs 1-Col",
        )

        # Add reference line at speedup = 1.0
        ax2.axhline(y=1.0, color="gray", linestyle="-.", alpha=0.5)

        # Configure secondary axis
        ax2.set_ylabel(
            "Speedup (vs 1-Column)",
            fontsize=12,
            fontweight="bold",
            color=self.colors["speedup"],
        )
        ax2.tick_params(axis="y", labelcolor=self.colors["speedup"])
        ax2.grid(False)

        # Mark optimal column count
        if report.optimal_num_columns is not None:
            optimal_idx = (
                columns.index(report.optimal_num_columns)
                if report.optimal_num_columns in columns
                else None
            )
            if optimal_idx is not None:
                # Highlight optimal bar
                bars[optimal_idx].set_color(self.colors["optimal"])
                bars[optimal_idx].set_alpha(1.0)

                # Add vertical line at optimal position
                ax1.axvline(
                    x=optimal_idx,
                    color=self.colors["optimal"],
                    linestyle="--",
                    linewidth=2,
                    label=f"Optimal Columns ({report.optimal_num_columns})",
                )

        # Combine legends
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="best", fontsize=10)

        # Add value labels on bars
        for i, (bar, lat) in enumerate(zip(bars, latencies)):
            height = bar.get_height()
            ax1.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{lat:.3f}",
                ha="center",
                va="bottom",
                fontsize=9,
                fontweight="bold",
            )

        # Add annotation for optimal configuration
        if (
            report.optimal_num_columns is not None
            and report.optimal_latency_ms is not None
        ):
            if report.optimal_num_columns in columns:
                optimal_idx = columns.index(report.optimal_num_columns)
                ax1.annotate(
                    f"Optimal: {report.optimal_latency_ms:.4f} ms",
                    xy=(optimal_idx, report.optimal_latency_ms),
                    xytext=(10, -20),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
                    fontsize=10,
                    fontweight="bold",
                )

        plt.tight_layout()

        # Ensure output directory exists
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        # Save the chart
        plt.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)

        return str(output_path)


# =============================================================================
# Phase 2 - Additional Visualizations
# =============================================================================


class HeatmapPlotter:
    """
    Generates heatmap visualizations for configuration space exploration.

    Creates heatmaps showing performance across tile size and column
    configuration combinations.
    """

    def __init__(self):
        """Initialize the HeatmapPlotter"""
        self.dpi = 150
        self.figsize = (10, 8)
        self.cmap = "RdYlGn_r"  # Red (slow) to Green (fast)

    def generate_heatmap(
        self,
        data: List[Dict[str, Any]],
        output_path: str,
        optimal_config: Optional[Dict[str, int]] = None,
    ) -> str:
        """
        Generate a heatmap visualization.

        Creates a heatmap with:
        - Tile size on y-axis
        - Column count on x-axis
        - Color scale: Green (fast) to Red (slow)
        - Optional: Highlight optimal configuration cell

        Args:
            data: List of dictionaries containing configuration results.
                  Each dict should have: tile_size, num_columns, mean_latency_ms
            output_path: Path where the chart will be saved
            optimal_config: Optional dict with optimal_tile_size and optimal_num_columns

        Returns:
            The file path where the chart was saved
        """
        if not data:
            raise ValueError("No data provided for heatmap")

        # Extract unique tile sizes and column counts
        tile_sizes = sorted(set(d.get("tile_size", 0) for d in data))
        columns = sorted(set(d.get("num_columns", 0) for d in data))

        if not tile_sizes or not columns:
            raise ValueError("Invalid data format: missing tile_size or num_columns")

        # Create latency matrix
        latency_matrix = np.zeros((len(tile_sizes), len(columns)))

        # Build lookup for data
        data_lookup = {}
        for d in data:
            key = (d.get("tile_size", 0), d.get("num_columns", 0))
            data_lookup[key] = d.get("mean_latency_ms", float("inf"))

        # Fill matrix
        for i, ts in enumerate(tile_sizes):
            for j, col in enumerate(columns):
                latency_matrix[i, j] = data_lookup.get((ts, col), np.nan)

        # Create figure
        fig, ax = plt.subplots(figsize=self.figsize)

        # Generate heatmap
        im = ax.imshow(
            latency_matrix,
            cmap=self.cmap,
            aspect="auto",
            origin="lower",
        )

        # Add colorbar
        plt.colorbar(im, ax=ax, label="Mean Latency (ms)")

        # Set tick labels
        ax.set_xticks(np.arange(len(columns)))
        ax.set_yticks(np.arange(len(tile_sizes)))
        ax.set_xticklabels([str(c) for c in columns])
        ax.set_yticklabels([str(ts) for ts in tile_sizes])

        # Set labels
        ax.set_xlabel("Number of Columns", fontsize=12, fontweight="bold")
        ax.set_ylabel("Tile Size", fontsize=12, fontweight="bold")
        ax.set_title("Configuration Space Heatmap", fontsize=14, fontweight="bold")

        # Highlight optimal configuration
        if optimal_config:
            opt_tile = optimal_config.get("optimal_tile_size")
            opt_col = optimal_config.get("optimal_num_columns")

            if opt_tile in tile_sizes and opt_col in columns:
                opt_y = tile_sizes.index(opt_tile)
                opt_x = columns.index(opt_col)

                # Draw rectangle around optimal cell
                rect = plt.Rectangle(
                    (opt_x - 0.5, opt_y - 0.5),
                    1,
                    1,
                    fill=False,
                    color="blue",
                    linewidth=3,
                    label="Optimal Config",
                )
                ax.add_patch(rect)

                # Add annotation
                if not np.isnan(latency_matrix[opt_y, opt_x]):
                    ax.annotate(
                        f"Optimal\n{latency_matrix[opt_y, opt_x]:.3f} ms",
                        xy=(opt_x, opt_y),
                        ha="center",
                        va="center",
                        fontsize=9,
                        fontweight="bold",
                        color="white",
                        bbox=dict(boxstyle="round", facecolor="blue", alpha=0.8),
                    )

        # Add value annotations to cells
        for i in range(len(tile_sizes)):
            for j in range(len(columns)):
                if not np.isnan(latency_matrix[i, j]):
                    ax.text(
                        j,
                        i,
                        f"{latency_matrix[i, j]:.3f}",
                        ha="center",
                        va="center",
                        fontsize=8,
                        color=(
                            "white"
                            if latency_matrix[i, j] > np.nanmean(latency_matrix) / 2
                            else "black"
                        ),
                    )

        # Add legend for optimal config
        if optimal_config:
            ax.plot([], [], color="blue", linewidth=3, label="Optimal Config")
            ax.legend(loc="upper right", fontsize=10)

        plt.tight_layout()

        # Ensure output directory exists
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        # Save the chart
        plt.savefig(output_path, dpi=self.dpi, bbox_inches="tight")
        plt.close(fig)

        return str(output_path)


# =============================================================================
# CLI Interface and Main Function
# =============================================================================


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(
        description="IRON Benchmark Visualization Tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all charts from a benchmark JSON file
  python -m iron.benchmarks.visualize -i results/benchmark.json -o results/charts -t all

  # Generate only tile size chart (PNG format)
  python -m iron.benchmarks.visualize -i results/results.json -t tile_size -f png

  # Generate heatmap (SVG format)
  python -m iron.benchmarks.visualize -i results/results.json -t heatmap -f svg

  # Generate column config chart with custom output directory
  python -m iron.benchmarks.visualize -i results/results.json -t column -o custom/charts
""",
    )

    parser.add_argument(
        "--input",
        "-i",
        type=str,
        required=True,
        help="Input JSON file containing benchmark results (required)",
    )

    parser.add_argument(
        "--output-dir",
        "-o",
        type=str,
        default="results/charts",
        help="Output directory for charts (default: results/charts)",
    )

    parser.add_argument(
        "--chart-type",
        "-t",
        type=str,
        choices=["tile_size", "column", "heatmap", "dashboard", "all"],
        default="all",
        help="Type of chart to generate (default: all)",
    )

    parser.add_argument(
        "--format",
        "-f",
        type=str,
        choices=["png", "svg"],
        default="png",
        help="Output format for charts (default: png)",
    )

    parser.add_argument(
        "--operator",
        type=str,
        help="Specific operator to visualize (default: all operators in file)",
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose output",
    )

    return parser.parse_args()


def _generate_dashboard(
    tile_report: Optional[TileSizeScalingReport],
    column_report: Optional[ColumnScalingReport],
    output_path: str,
    dpi: int = 150,
) -> str:
    """
    Generate a combined dashboard visualization.

    Args:
        tile_report: Tile size scaling report (optional)
        column_report: Column scaling report (optional)
        output_path: Path where the dashboard will be saved
        dpi: Output DPI

    Returns:
        The file path where the dashboard was saved
    """
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle("IRON Benchmark Dashboard", fontsize=16, fontweight="bold")

    plot_idx = 1
    total_plots = (1 if tile_report else 0) + (1 if column_report else 0)

    if tile_report and tile_report.tile_size_results:
        if total_plots == 1:
            ax = fig.add_subplot(111)
        else:
            ax = fig.add_subplot(1, 2, plot_idx)

        tile_sizes = [r.tile_size for r in tile_report.tile_size_results]
        latencies = [r.mean_latency_ms for r in tile_report.tile_size_results]
        bandwidths = [r.memory_bandwidth_gbps for r in tile_report.tile_size_results]

        ax.plot(tile_sizes, latencies, marker="o", color="#2E86AB", label="Latency")
        ax.set_xlabel("Tile Size")
        ax.set_ylabel("Mean Latency (ms)", color="#2E86AB")
        ax.set_title(f"Tile Size Scaling - {tile_report.operator_name.upper()}")
        ax.set_xscale("log")
        ax.grid(True, alpha=0.3)

        # Secondary axis for bandwidth
        ax2 = ax.twinx()
        ax2.plot(tile_sizes, bandwidths, marker="s", color="#A23B72", label="Bandwidth")
        ax2.set_ylabel("Memory Bandwidth (GB/s)", color="#A23B72")

        if tile_report.optimal_tile_size:
            ax.axvline(x=tile_report.optimal_tile_size, color="green", linestyle="--")

        plot_idx += 1

    if column_report and column_report.column_results:
        if total_plots == 1:
            ax = fig.add_subplot(111)
        else:
            ax = fig.add_subplot(1, 2, plot_idx)

        columns = [r.num_columns for r in column_report.column_results]
        latencies = [r.mean_latency_ms for r in column_report.column_results]

        x_pos = np.arange(len(columns))
        ax.bar(x_pos, latencies, color="#2E86AB", alpha=0.8)
        ax.set_xlabel("Number of Columns")
        ax.set_ylabel("Mean Latency (ms)")
        ax.set_title(f"Column Scaling - {column_report.operator_name.upper()}")
        ax.set_xticks(x_pos)
        ax.set_xticklabels([str(c) for c in columns])
        ax.grid(True, alpha=0.3, axis="y")

        if (
            column_report.optimal_num_columns
            and column_report.optimal_num_columns in columns
        ):
            opt_idx = columns.index(column_report.optimal_num_columns)
            ax.bar(opt_idx, latencies[opt_idx], color="orange", alpha=1.0)

        plot_idx += 1

    plt.tight_layout()

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)

    return str(output_path)


def main():
    """
    Main entry point for the visualization CLI.

    Parses arguments, loads benchmark data, and generates
    the requested charts.
    """
    args = parse_args()

    # Create output directory
    output_dir = create_output_dir(args.output_dir)
    timestamp = get_timestamp()

    print("IRON Benchmark Visualization Tools")
    print("=" * 40)
    print(f"Input file: {args.input}")
    print(f"Output directory: {output_dir}")
    print(f"Chart type: {args.chart_type}")
    print(f"Output format: {args.format}")
    print()

    # Load benchmark data
    try:
        data = load_results_from_json(args.input)
        print(f"Loaded benchmark data from: {args.input}")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading benchmark data: {e}")
        sys.exit(1)

    # Track generated charts
    generated_charts = []

    # Determine which reports are available
    tile_report = None
    column_report = None

    # Check if data contains tile_size_results (direct report or nested)
    if "tile_size_results" in data:
        tile_report = _dict_to_tile_report(data)
    elif "column_results" in data:
        column_report = _dict_to_column_report(data)
    elif "results" in data:
        # Handle nested results (e.g., from full benchmark suite)
        for result in data.get("results", []):
            if args.operator and result.get("operator_name") != args.operator:
                continue

            if "tile_size_results" in result:
                tile_report = _dict_to_tile_report(result)
            if "column_results" in result:
                column_report = _dict_to_column_report(result)

    # Generate requested charts
    chart_types = []
    if args.chart_type == "all":
        chart_types = ["tile_size", "column", "dashboard"]
    else:
        chart_types = [args.chart_type]

    for chart_type in chart_types:
        if chart_type == "tile_size":
            if tile_report and tile_report.tile_size_results:
                output_path = str(
                    output_dir
                    / f"tile_size_{tile_report.operator_name}_{timestamp}.{args.format}"
                )
                plotter = TileSizePlotter()
                chart_path = plotter.generate_chart(tile_report, output_path)
                generated_charts.append(chart_path)
                print(f"Generated tile size chart: {chart_path}")
            else:
                print("Warning: No tile size data available for chart generation")

        elif chart_type == "column":
            if column_report and column_report.column_results:
                output_path = str(
                    output_dir
                    / f"column_{column_report.operator_name}_{timestamp}.{args.format}"
                )
                plotter = ColumnConfigPlotter()
                chart_path = plotter.generate_chart(column_report, output_path)
                generated_charts.append(chart_path)
                print(f"Generated column config chart: {chart_path}")
            else:
                print("Warning: No column config data available for chart generation")

        elif chart_type == "heatmap":
            # For heatmap, we need combined data
            heatmap_data = []
            if tile_report and column_report:
                # Generate synthetic combined data
                for ts_result in tile_report.tile_size_results:
                    for col_result in column_report.column_results:
                        combined = {
                            "tile_size": ts_result.tile_size,
                            "num_columns": col_result.num_columns,
                            "mean_latency_ms": (
                                ts_result.mean_latency_ms + col_result.mean_latency_ms
                            )
                            / 2,
                        }
                        heatmap_data.append(combined)

            if heatmap_data:
                optimal_config = {}
                if tile_report.optimal_tile_size:
                    optimal_config["optimal_tile_size"] = tile_report.optimal_tile_size
                if column_report.optimal_num_columns:
                    optimal_config["optimal_num_columns"] = (
                        column_report.optimal_num_columns
                    )

                output_path = str(output_dir / f"heatmap_{timestamp}.{args.format}")
                plotter = HeatmapPlotter()
                chart_path = plotter.generate_heatmap(
                    heatmap_data, output_path, optimal_config
                )
                generated_charts.append(chart_path)
                print(f"Generated heatmap: {chart_path}")
            else:
                print("Warning: Insufficient data for heatmap generation")

        elif chart_type == "dashboard":
            if tile_report or column_report:
                output_path = str(output_dir / f"dashboard_{timestamp}.{args.format}")
                chart_path = _generate_dashboard(
                    tile_report, column_report, output_path
                )
                generated_charts.append(chart_path)
                print(f"Generated dashboard: {chart_path}")
            else:
                print("Warning: No data available for dashboard generation")

    # Print summary
    print()
    print("=" * 40)
    print("Visualization complete!")
    print(f"Generated {len(generated_charts)} chart(s):")
    for chart in generated_charts:
        print(f"  - {chart}")


if __name__ == "__main__":
    main()
