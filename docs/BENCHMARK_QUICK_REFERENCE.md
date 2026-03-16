# Benchmark Validation Framework - Quick Reference

**Created:** 2026-03-15
**Version:** 1.0.0

---

## Files Created

### Core Modules

| File | Purpose | Entry Point |
|------|---------|-------------|
| `iron/benchmarks/validate.py` | Main validation runner | `python -m iron.benchmarks.validate` |
| `iron/benchmarks/verify.py` | Verification & comparison | `python -m iron.benchmarks.verify` |
| `scripts/collect_benchmarks.py` | Data collection | `python scripts/collect_benchmarks.py` |
| `scripts/analyze_results.py` | Analysis & charts | `python scripts/analyze_results.py` |
| `docs/BENCHMARK_VALIDATION_GUIDE.md` | Full documentation | - |

### Updated Files

| File | Changes |
|------|---------|
| `iron/benchmarks/__init__.py` | Added validation/verification exports, version bumped to 1.1.0 |

---

## Quick Start Commands

### Run Full Validation

```bash
# From project root (c:\Users\antmi\IRON)
python -m iron.benchmarks.validate --generate-charts
```

### Collect Data

```bash
# Single run
python scripts/collect_benchmarks.py

# Multiple runs for stability
python scripts/collect_benchmarks.py --runs 5

# Update baseline
python scripts/collect_benchmarks.py --update-baseline --export all
```

### Verify Results

```bash
# Compare against baseline
python -m iron.benchmarks.verify compare --current results.json --baseline scripts/baseline.json

# Verify against targets
python -m iron.benchmarks.verify verify-targets results.json --target-type windows_npu

# Quick summary
python -m iron.benchmarks.verify summary results.json
```

### Analyze Results

```bash
# Generate full report with charts
python scripts/analyze_results.py --report full --charts all

# Trend analysis
python scripts/analyze_results.py --trend-analysis
```

---

## Command Reference

### validate.py Options

| Option | Description | Default |
|--------|-------------|---------|
| `--operator` | rope, rmsnorm, silu, softmax | All |
| `--iterations` | Timed iterations | 50 |
| `--warmup` | Warmup runs | 10 |
| `--generate-charts` | Create visualizations | False |
| `--compare-baseline` | Compare vs baseline | True |
| `--verbose` | Debug output | False |

### verify.py Commands

| Command | Description |
|---------|-------------|
| `compare` | Compare two result files |
| `verify-targets` | Check against performance targets |
| `trend-analysis` | Analyze historical trends |
| `summary` | Quick results overview |

### collect_benchmarks.py Options

| Option | Description | Default |
|--------|-------------|---------|
| `--runs` | Number of runs | 1 |
| `--iterations` | Iterations per run | 50 |
| `--update-baseline` | Update baseline file | False |
| `--export` | Export format | None |

### analyze_results.py Options

| Option | Description | Default |
|--------|-------------|---------|
| `--input` | Input results file | Latest |
| `--charts` | Chart type | None |
| `--report` | Report format | text |
| `--trend-analysis` | Analyze trends | False |

---

## Performance Targets (Llama3.2-1B)

| Operator | CPU Baseline | Windows NPU | Linux NPU |
|----------|-------------|-------------|-----------|
| RoPE | < 5.0ms | < 0.55ms | < 0.5ms |
| RMSNorm | < 10.0ms | < 1.1ms | < 1.0ms |
| SiLU | < 3.0ms | < 0.33ms | < 0.3ms |
| Softmax | < 20.0ms | < 2.2ms | < 2.0ms |

---

## Output Files

Results are saved to `iron/benchmarks/results/`:

| File | Description |
|------|-------------|
| `validation_latest.json` | Latest validation results |
| `validation_latest.md` | Markdown summary |
| `benchmark_*.json` | Raw benchmark data |
| `charts/*.png` | Generated charts |
| `benchmark_history.json` | Historical data |

---

## Python API

```python
# Run validation programmatically
from iron.benchmarks.validate import run_validation

result = run_validation(
    iterations=100,
    generate_charts=True
)

print(f"Targets met: {result.targets_summary['targets_met']}")
print(f"Anomalies: {len(result.anomaly_reports)}")

# Compare results
from iron.benchmarks.verify import compare_results, verify_targets

comparisons = compare_results(current, baseline)
verifications = verify_targets(results, "windows_npu")
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | `pip install torch numpy ml_dtypes matplotlib psutil` |
| NPU not detected | Expected for CPU reference benchmarks |
| High variance (>20% CV) | Close other apps, run more iterations |
| Charts not generating | `pip install matplotlib` |

---

## Workflow Example

```bash
# 1. Run validation with charts
python -m iron.benchmarks.validate --generate-charts --iterations 100

# 2. Collect multiple runs
python scripts/collect_benchmarks.py --runs 3 --export all

# 3. Analyze and generate report
python scripts/analyze_results.py --report full --charts all

# 4. If results are good, update baseline
python scripts/collect_benchmarks.py --update-baseline

# 5. Verify against new baseline
python -m iron.benchmarks.verify verify-targets \
    iron/benchmarks/results/validation_latest.json \
    --target-type windows_npu
```

---

*For detailed documentation, see `docs/BENCHMARK_VALIDATION_GUIDE.md`*
