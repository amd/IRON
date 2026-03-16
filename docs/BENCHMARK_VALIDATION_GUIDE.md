# IRON Benchmark Validation Guide

**Document Type:** Technical Guide
**Version:** 1.0.0
**Date:** 2026-03-15
**Platform:** Windows 11 with AMD Ryzen AI NPU

---

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Benchmark Framework Components](#benchmark-framework-components)
4. [Running Benchmarks](#running-benchmarks)
5. [Understanding Results](#understanding-results)
6. [Verification and Comparison](#verification-and-comparison)
7. [Data Collection](#data-collection)
8. [Analysis and Visualization](#analysis-and-visualization)
9. [Performance Targets](#performance-targets)
10. [Troubleshooting](#troubleshooting)

---

## Overview

The IRON Benchmark Validation Framework provides comprehensive empirical performance testing for the IRON NPU runtime framework on Windows 11 with AMD Ryzen AI NPU.

### Key Features

- **Automated Benchmark Execution**: One-command running with automatic system diagnostics
- **Result Verification**: Compare against Linux and Windows NPU targets
- **Anomaly Detection**: Automatic flagging of unusual results
- **Historical Tracking**: JSON result logging with trend analysis
- **Visual Outputs**: Charts and graphs showing performance distribution
- **System Diagnostics**: Capture hardware info, driver versions, OS details

### Framework Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Validation Runner | `iron/benchmarks/validate.py` | Main benchmark execution |
| Verification Tool | `iron/benchmarks/verify.py` | Result comparison and analysis |
| Data Collector | `scripts/collect_benchmarks.py` | Automated data collection |
| Analysis Tool | `scripts/analyze_results.py` | Charts and report generation |

---

## Quick Start

### Prerequisites

Ensure you have the required dependencies installed:

```bash
pip install torch numpy ml_dtypes matplotlib psutil
```

### Run Full Validation Suite

Execute the complete validation framework with one command:

```bash
# From project root (c:\Users\antmi\IRON)
python -m iron.benchmarks.validate
```

This will:
1. Capture system information (CPU, NPU, OS, drivers)
2. Run benchmarks for all operators (RoPE, RMSNorm, SiLU, Softmax)
3. Detect anomalies and flag issues
4. Save results to `iron/benchmarks/results/`
5. Generate summary report

### Generate Charts

```bash
python -m iron.benchmarks.validate --generate-charts
```

### Compare Against Baseline

```bash
python -m iron.benchmarks.verify compare --current results.json --baseline scripts/baseline.json
```

---

## Benchmark Framework Components

### 1. Validation Runner (`iron/benchmarks/validate.py`)

The main entry point for benchmark execution.

**Features:**
- Automatic system information capture
- Benchmark execution with configurable iterations
- Anomaly detection (high variance, regressions, target misses)
- Result saving in JSON and Markdown formats
- Optional chart generation

**Usage:**

```bash
# Run all benchmarks
python -m iron.benchmarks.validate

# Run specific operator
python -m iron.benchmarks.validate --operator rope

# More iterations for stability
python -m iron.benchmarks.validate --iterations 100

# Generate visualization charts
python -m iron.benchmarks.validate --generate-charts

# Skip baseline comparison
python -m iron.benchmarks.validate --no-compare-baseline

# Verbose output
python -m iron.benchmarks.validate --verbose
```

**Command-line Options:**

| Option | Description | Default |
|--------|-------------|---------|
| `--operator` | Specific operator (rope, rmsnorm, silu, softmax) | All operators |
| `--iterations` | Number of timed iterations | 50 |
| `--warmup` | Number of warmup runs | 10 |
| `--output-dir` | Results output directory | `iron/benchmarks/results` |
| `--compare-baseline` | Compare against baseline | True |
| `--no-compare-baseline` | Skip baseline comparison | False |
| `--generate-charts` | Generate visualization charts | False |
| `--verbose` | Enable debug logging | False |

### 2. Verification Tool (`iron/benchmarks/verify.py`)

Tool for comparing and verifying benchmark results.

**Commands:**

```bash
# Compare two result files
python -m iron.benchmarks.verify compare --current current.json --baseline baseline.json

# Verify against performance targets
python -m iron.benchmarks.verify verify-targets results.json --target-type windows_npu

# Analyze trends from history
python -m iron.benchmarks.verify trend-analysis iron/benchmarks/results/

# Quick summary
python -m iron.benchmarks.verify summary results.json
```

**Subcommands:**

| Command | Description |
|---------|-------------|
| `compare` | Compare current vs baseline results |
| `verify-targets` | Verify results against performance targets |
| `trend-analysis` | Analyze performance trends over time |
| `summary` | Quick results summary |

### 3. Data Collector (`scripts/collect_benchmarks.py`)

Automated data collection with history tracking.

**Usage:**

```bash
# Single collection run
python scripts/collect_benchmarks.py

# Multiple runs for stability analysis
python scripts/collect_benchmarks.py --runs 5

# Update baseline with current results
python scripts/collect_benchmarks.py --update-baseline

# Export in multiple formats
python scripts/collect_benchmarks.py --export all

# Specific operators only
python scripts/collect_benchmarks.py --operator rope --operator rmsnorm
```

**Options:**

| Option | Description | Default |
|--------|-------------|---------|
| `--runs` | Number of benchmark runs | 1 |
| `--iterations` | Iterations per run | 50 |
| `--warmup` | Warmup iterations | 10 |
| `--operator` | Specific operator(s) to benchmark | All |
| `--delay` | Seconds between runs | 5 |
| `--update-baseline` | Update baseline file | False |
| `--export` | Export format (json, csv, markdown, all) | None |
| `--verbose` | Verbose output | False |

### 4. Analysis Tool (`scripts/analyze_results.py`)

Comprehensive analysis and chart generation.

**Usage:**

```bash
# Analyze latest results
python scripts/analyze_results.py

# Analyze specific result file
python scripts/analyze_results.py --input results.json

# Generate all charts
python scripts/analyze_results.py --charts all

# Generate full report
python scripts/analyze_results.py --report full

# Trend analysis only
python scripts/analyze_results.py --trend-analysis
```

**Options:**

| Option | Description | Default |
|--------|-------------|---------|
| `--input` | Input results file | Latest file |
| `--charts` | Chart type to generate | None |
| `--report` | Report format (text, markdown, full) | text |
| `--trend-analysis` | Analyze historical trends | False |
| `--output` | Output file path | Auto-generated |

---

## Running Benchmarks

### Step-by-Step Execution

#### Step 1: Prepare Environment

```bash
# Navigate to project root
cd c:\Users\antmi\IRON

# Verify Python environment
python --version

# Check dependencies
python -c "import torch; print(torch.__version__)"
```

#### Step 2: Run Initial Validation

```bash
# Run full validation suite
python -m iron.benchmarks.validate --generate-charts
```

#### Step 3: Review Results

Results are saved to `iron/benchmarks/results/`:
- `validation_latest.json` - Latest JSON results
- `validation_latest.md` - Markdown summary
- `charts/` - Generated visualization charts

#### Step 4: Collect Multiple Runs (Optional)

For stability analysis:

```bash
python scripts/collect_benchmarks.py --runs 5 --delay 10
```

#### Step 5: Update Baseline (Optional)

After verifying results are correct:

```bash
python scripts/collect_benchmarks.py --update-baseline
```

### Batch Execution Script

Create a batch file for automated testing:

```batch
@echo off
echo IRON Benchmark Validation Batch
echo ================================

REM Run validation with charts
python -m iron.benchmarks.validate --generate-charts --iterations 100

REM Collect multiple runs
python scripts/collect_benchmarks.py --runs 3 --export all

REM Analyze results
python scripts/analyze_results.py --report full

echo.
echo Batch complete. Results in iron/benchmarks/results/
```

---

## Understanding Results

### Result Structure

Benchmark results are stored in JSON format:

```json
{
  "timestamp": "2026-03-15T10:30:00.000000",
  "system_info": {
    "platform": "Windows",
    "processor": "AMD Ryzen AI",
    "python_version": "3.11.0",
    "torch_version": "2.1.0"
  },
  "results": [
    {
      "operator_name": "rope",
      "input_shape": [1, 12, 128, 64],
      "metrics": {
        "mean_ms": 0.0871,
        "median_ms": 0.0863,
        "std_dev_ms": 0.0026,
        "p95_ms": 0.0921,
        "p99_ms": 0.0966,
        "throughput_ops_sec": 11481.0,
        "memory_bandwidth_gbps": 4.51
      },
      "targets": {
        "linux_npu_ms": 0.5,
        "windows_npu_ms": 0.55,
        "cpu_baseline_ms": 5.0
      },
      "target_met": true
    }
  ],
  "anomaly_reports": [],
  "targets_summary": {
    "total_operators": 4,
    "targets_met": 4,
    "targets_missed": 0,
    "errors": 0
  }
}
```

### Key Metrics Explained

| Metric | Description | What It Tells You |
|--------|-------------|-------------------|
| **Mean Latency** | Average execution time | Overall performance |
| **Median Latency** | Middle value of sorted latencies | Typical case performance |
| **Std Dev** | Standard deviation | Consistency/stability |
| **P95 Latency** | 95th percentile | Near-worst case |
| **P99 Latency** | 99th percentile | Worst case (excluding outliers) |
| **Throughput** | Operations per second | Processing capacity |
| **Memory Bandwidth** | GB/s of memory transfer | Memory subsystem efficiency |

### Interpreting Target Status

| Status | Meaning | Action |
|--------|---------|--------|
| **PASS** | Measured <= Target | No action needed |
| **FAIL** | Measured > Target | Investigate cause |
| **ERROR** | Benchmark execution failed | Check implementation |

### Coefficient of Variation (CV)

CV = (Std Dev / Mean) * 100%

| CV Range | Stability Rating | Interpretation |
|----------|-----------------|----------------|
| < 5% | EXCELLENT | Very consistent results |
| 5-10% | GOOD | Acceptable variance |
| 10-20% | ACCEPTABLE | Some instability |
| > 20% | POOR | High variance, investigate |

---

## Verification and Comparison

### Comparing Against Baseline

```bash
python -m iron.benchmarks.verify compare \
    --current iron/benchmarks/results/validation_latest.json \
    --baseline scripts/baseline.json \
    --threshold 0.10
```

**Output Interpretation:**

```
SUMMARY
----------------------------------------------------------------------
Total operators compared: 4
Regressions detected: 0
Improvements: 1

DETAILED COMPARISON
----------------------------------------------------------------------

Operator: ROPE
  Baseline: 0.0875 ms
  Current:  0.0871 ms
  Change:   -0.5% (No significant change)
```

### Verifying Against Targets

```bash
# Verify against Windows NPU targets
python -m iron.benchmarks.verify verify-targets \
    iron/benchmarks/results/validation_latest.json \
    --target-type windows_npu

# Verify against CPU baseline
python -m iron.benchmarks.verify verify-targets \
    iron/benchmarks/results/validation_latest.json \
    --target-type cpu_baseline
```

### Trend Analysis

```bash
python -m iron.benchmarks.verify trend-analysis \
    iron/benchmarks/results/ \
    --metric mean_ms
```

**Trend Interpretation:**

| Direction | Meaning |
|-----------|---------|
| IMPROVING | Latency decreasing over time |
| STABLE | No significant change |
| DEGRADING | Latency increasing, investigate |

---

## Data Collection

### Collection Workflow

1. **Single Collection**: One-time benchmark run
2. **Multiple Runs**: Several runs for statistical stability
3. **History Tracking**: Results appended to history file
4. **Baseline Update**: Promote current results to baseline

### Automated Collection Script

```bash
# Full collection workflow
python scripts/collect_benchmarks.py \
    --runs 3 \
    --iterations 100 \
    --update-baseline \
    --export all
```

### Result Files

| File | Location | Purpose |
|------|----------|---------|
| `benchmark_YYYYMMDD_HHMMSS.json` | `iron/benchmarks/results/` | Raw benchmark data |
| `benchmark_aggregated_*.json` | `iron/benchmarks/results/` | Aggregated multi-run data |
| `benchmark_history.json` | `iron/benchmarks/results/` | Historical trend data |
| `export_*.json/csv/md` | `iron/benchmarks/results/` | Exported results |

---

## Analysis and Visualization

### Chart Types

| Chart | Description | Use Case |
|-------|-------------|----------|
| **Latency Comparison** | Mean vs P99 vs Target | Quick performance overview |
| **Target Achievement** | Pass/Fail visualization | Target compliance check |
| **Throughput** | Operations per second | Capacity analysis |
| **Variance** | Coefficient of variation | Stability assessment |
| **Trend** | Performance over time | Regression detection |

### Generating Reports

```bash
# Full analysis report with all charts
python scripts/analyze_results.py --report full --charts all
```

### Report Components

1. **System Information**: Platform, processor, Python version
2. **Summary**: Total operators, pass/fail counts
3. **Distribution Analysis**: Statistical metrics per operator
4. **Target Comparison**: Measured vs target for each target type
5. **Trend Analysis**: Historical performance changes
6. **Charts**: Visual representations

---

## Performance Targets

### Target Specifications

All targets are for Llama3.2-1B configuration with bfloat16 precision.

| Operator | Input Shape | Linux NPU | Windows NPU | CPU Baseline |
|----------|-------------|-----------|-------------|--------------|
| **RoPE** | [1, 12, 128, 64] | < 0.5ms | < 0.55ms | < 5.0ms |
| **RMSNorm** | [1, 128, 2048] | < 1.0ms | < 1.1ms | < 10.0ms |
| **SiLU** | [1, 128, 8192] | < 0.3ms | < 0.33ms | < 3.0ms |
| **Softmax** | [1, 12, 128, 128] | < 2.0ms | < 2.2ms | < 20.0ms |

### Target Derivation

- **Linux NPU**: Raw XRT/mlir-aie hardware performance target
- **Windows NPU**: Linux target + ~10% for ONNX Runtime GenAI overhead
- **CPU Baseline**: Linux NPU target * 10 (expected NPU speedup)

### Platform Notes

- Windows targets include overhead for ONNX Runtime abstraction
- Linux targets represent direct hardware access performance
- Both platforms use identical C++ operator implementations
- CPU baseline applies equally to both platforms

---

## Troubleshooting

### Common Issues

#### Issue: "Module not found: ml_dtypes"

**Solution:**
```bash
pip install ml_dtypes
```

#### Issue: "NPU not detected"

This is expected if running CPU reference benchmarks. The framework will automatically use CPU fallback.

To verify NPU detection:
```bash
python -c "from iron.benchmarks.validate import SystemInfo; print(SystemInfo().capture().npu_detected)"
```

#### Issue: High variance (>20% CV)

**Possible causes:**
- System under load from other processes
- Thermal throttling
- Power management interference

**Solutions:**
1. Close other applications
2. Run more iterations: `--iterations 100`
3. Run multiple times: `--runs 5`
4. Check system thermals

#### Issue: Results don't meet targets

**Investigation steps:**

1. Verify running correct benchmark type:
   - CPU reference should meet CPU baseline targets
   - NPU benchmarks should meet NPU targets

2. Check for anomalies:
   ```bash
   python -m iron.benchmarks.validate --verbose
   ```

3. Compare against baseline:
   ```bash
   python -m iron.benchmarks.verify compare --current latest.json --baseline baseline.json
   ```

#### Issue: Charts not generating

**Check matplotlib installation:**
```bash
pip install matplotlib
```

**Verify non-interactive backend:**
The framework uses 'Agg' backend for headless chart generation.

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, no critical issues |
| 1 | Failure or critical anomalies detected |

### Getting Help

```bash
# Help for any command
python -m iron.benchmarks.validate --help
python scripts/collect_benchmarks.py --help
python scripts/analyze_results.py --help
```

---

## Appendix: File Reference

### Directory Structure

```
IRON/
├── iron/
│   ├── benchmarks/
│   │   ├── validate.py       # Main validation runner
│   │   ├── verify.py         # Verification tool
│   │   ├── baseline_bench.py # CPU baseline benchmarks
│   │   ├── run.py            # Original benchmark runner
│   │   └── results/          # Generated results
│   │       ├── charts/       # Generated charts
│   │       └── latest/       # Symlinks to latest
│   └── operators/            # Operator implementations
├── scripts/
│   ├── collect_benchmarks.py # Data collection
│   ├── analyze_results.py    # Analysis tool
│   ├── check_regression.py   # CI regression check
│   └── baseline.json         # Baseline targets
└── docs/
    └── BENCHMARK_VALIDATION_GUIDE.md  # This document
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `IRON_BENCHMARK_RESULTS` | Custom results directory | `iron/benchmarks/results` |
| `IRON_LOG_LEVEL` | Logging level | `INFO` |

---

*Copyright © 2026 IRON Project. All rights reserved.*
