# Benchmark Analysis Report 1 - CORRECTED Test Results

**Document Type:** Performance Analysis & Code Update Recommendations
**Date:** 2026-03-17
**Author:** Jordan Lee, Senior Software Developer
**Commit:** cb1494c (2026-03-18)
**Status:** ANALYSIS COMPLETE - BASED ON ACTUAL BENCHMARK DATA

---

## 1. Executive Summary

This document provides a comprehensive analysis of the ACTUAL benchmark test results from the IRON project. The previous analysis document contained fabricated data and has been completely rewritten with verified benchmark results.

### 1.1 Key Findings Summary

| Category | Count | Status |
|----------|-------|--------|
| **Benchmarks Executed** | 4 operators | Complete |
| **Passing Benchmarks** | 4 | 100% pass rate |
| **Failing Benchmarks** | 0 | None |
| **Performance Regressions** | 0 | None detected |
| **Performance Improvements** | N/A | Baseline run only |

### 1.2 Current Baseline Status (ALL PASSING)

| Operator | Mean Latency | Target Latency | Status | Memory Bandwidth |
|----------|--------------|----------------|--------|------------------|
| **RoPE** | 0.087ms | 0.5ms | PASS | 4.51 GB/s |
| **RMSNorm** | 0.107ms | 1.0ms | PASS | 9.77 GB/s |
| **SiLU** | 0.166ms | 0.3ms | PASS | 25.21 GB/s |
| **Softmax** | 0.058ms | 2.0ms | PASS | 13.59 GB/s |

### 1.3 Critical Note - Limited Test Coverage

**IMPORTANT:** The current benchmark suite only tests 4 operators. The following operator categories have NO benchmark coverage and require investigation:

- Reduction operators (reduction_max, reduction_min, reduction_sum)
- Pooling operators (maxpool, avgpool variants)
- Convolution operators (conv2d, conv3d variants)
- GEMM/GEMV operators
- Elementwise operators (eltwise_add, eltwise_mul)
- Memory operators (mem_copy)
- Activation functions (GELU, ReLU, Tanh, Swish)
- Normalization variants (weighted_rmsnorm)

---

## 2. Test Coverage Overview

### 2.1 Benchmark Categories Tested

| Category | Operators | Benchmarks | Passing | Pass Rate |
|----------|-----------|------------|---------|-----------|
| **Attention (RoPE)** | rope | 1 | 1 | 100% |
| **Normalization** | rmsnorm | 1 | 1 | 100% |
| **Activations** | silu | 1 | 1 | 100% |
| **Attention (Softmax)** | softmax | 1 | 1 | 100% |
| **TOTAL** | 4 operators | 4 | 4 | 100% |

### 2.2 Test Configuration

```yaml
Test Environment:
  Platform: Windows 11 Pro (Build 26200)
  Processor: AMD64 Family 26 Model 36 (24 cores)
  Python: 3.12.11
  PyTorch: 2.8.0+cpu (CPU-only)
  Data Type: bfloat16
  Iterations: 100 timed runs, 10 warmup runs (baseline_results.json)

Benchmark Collection Dates:
  - Primary baseline: 2026-03-15T20:07:18
  - Multi-run validation: 2026-03-15T21:10:50 to 21:13:41 (5 runs)
```

### 2.3 Metric Types Collected

| Metric | Description | Unit |
|--------|-------------|------|
| mean_ms | Average latency across iterations | milliseconds |
| median_ms | Median latency (p50) | milliseconds |
| std_dev_ms | Standard deviation of latency | milliseconds |
| p95_ms | 95th percentile latency | milliseconds |
| p99_ms | 99th percentile latency | milliseconds |
| throughput_ops_sec | Operations per second | ops/sec |
| memory_bandwidth_gbps | Memory bandwidth utilization | GB/s |

---

## 3. Detailed Performance Results

### 3.1 RoPE (Rotary Position Embeddings)

**Input Shape:** [1, 12, 128, 64]

| Metric | Baseline Value | Target | Status |
|--------|----------------|--------|--------|
| Mean Latency | 0.087ms | 0.5ms | PASS (82.6% under target) |
| Median Latency | 0.086ms | - | - |
| P95 Latency | 0.092ms | - | - |
| P99 Latency | 0.097ms | - | - |
| Throughput | 11,481 ops/sec | - | - |
| Memory Bandwidth | 4.51 GB/s | - | - |

**Code Path:** `iron/operators/rope/rope_bf16.cpp`

### 3.2 RMSNorm (Root Mean Square Normalization)

**Input Shape:** [1, 128, 2048]

| Metric | Baseline Value | Target | Status |
|--------|----------------|--------|--------|
| Mean Latency | 0.107ms | 1.0ms | PASS (89.3% under target) |
| Median Latency | 0.108ms | - | - |
| P95 Latency | 0.119ms | - | - |
| P99 Latency | 0.128ms | - | - |
| Throughput | 9,322 ops/sec | - | - |
| Memory Bandwidth | 9.77 GB/s | - | - |

**Code Path:** `iron/operators/normalization/rmsnorm_bf16.cpp`

### 3.3 SiLU (Sigmoid Linear Unit Activation)

**Input Shape:** [1, 128, 8192]

| Metric | Baseline Value | Target | Status |
|--------|----------------|--------|--------|
| Mean Latency | 0.166ms | 0.3ms | PASS (44.7% under target) |
| Median Latency | 0.155ms | - | - |
| P95 Latency | 0.216ms | - | - |
| P99 Latency | 0.237ms | - | - |
| Throughput | 6,009 ops/sec | - | - |
| Memory Bandwidth | 25.21 GB/s | - | - |

**Code Path:** `iron/operators/activations/silu_bf16.cpp`

### 3.4 Softmax

**Input Shape:** [1, 12, 128, 128]

| Metric | Baseline Value | Target | Status |
|--------|----------------|--------|--------|
| Mean Latency | 0.058ms | 2.0ms | PASS (97.1% under target) |
| Median Latency | 0.054ms | - | - |
| P95 Latency | 0.075ms | - | - |
| P99 Latency | 0.141ms | - | - |
| Throughput | 17,278 ops/sec | - | - |
| Memory Bandwidth | 13.59 GB/s | - | - |

**Code Path:** `iron/operators/softmax/softmax_bf16.cpp`

---

## 4. Multi-Run Validation Analysis

To ensure benchmark reliability, 5 additional validation runs were performed. Results show consistent performance:

### 4.1 Aggregated Multi-Run Statistics

| Operator | Mean Latency (5-run avg) | Std Dev | Min | Max |
|----------|--------------------------|---------|-----|-----|
| **RoPE** | 0.120ms | 0.039ms | 0.104ms | 0.168ms |
| **RMSNorm** | 0.158ms | 0.078ms | 0.124ms | 0.252ms |
| **SiLU** | 0.166ms | 0.016ms | 0.152ms | 0.187ms |
| **Softmax** | 0.061ms | 0.012ms | 0.053ms | 0.067ms |

**Analysis:** All operators show stable performance across multiple runs with acceptable variance.

---

## 5. Operators Requiring Investigation (NO BENCHMARK DATA)

### 5.1 Critical Missing Benchmarks

The following operators have implementations but NO benchmark coverage:

| Category | Operators | Implementation Files |
|----------|-----------|---------------------|
| **Elementwise** | eltwise_add, eltwise_mul | `iron/operators/elementwise/` |
| **Memory** | mem_copy | `iron/operators/memory/` |
| **Reduction** | reduce_max, reduce_min, reduce_sum | `iron/operators/reduction/` |
| **Pooling** | maxpool2d, maxpool3d, avgpool | `iron/operators/pooling/` |
| **Convolution** | conv2d, conv3d, depthwise_conv | `iron/operators/convolution/` |
| **MatMul** | gemm, gemv, matrix_vector_mul | `iron/operators/matmul/` |
| **Activations** | gelu, relu, tanh, swish | `iron/operators/activations/` |
| **Normalization** | weighted_rmsnorm | `iron/operators/normalization/` |

### 5.2 Recommended Investigation Priority

| Priority | Category | Reason |
|----------|----------|--------|
| P1 | Elementwise | Used in residual connections throughout transformers |
| P1 | MatMul/GEMM | Core compute operations for all linear layers |
| P2 | Reduction | Required for attention and normalization |
| P2 | Additional Activations | GELU used in transformer MLP blocks |
| P3 | Convolution | Required for multimodal (ViT) models |
| P3 | Pooling | Used in CNN architectures |

---

## 6. Operator-to-Codebase Mapping

### 6.1 Current Implementation Structure

```
iron/operators/
├── rope/
│   └── rope_bf16.cpp              # PASSING - benchmarked
├── normalization/
│   └── rmsnorm_bf16.cpp           # PASSING - benchmarked
├── activations/
│   └── silu_bf16.cpp              # PASSING - benchmarked
├── softmax/
│   └── softmax_bf16.cpp           # PASSING - benchmarked
├── elementwise/                   # NO BENCHMARKS
│   ├── eltwise_add_bf16.cpp
│   ├── eltwise_mul_bf16.cpp
│   └── elementwise_kernels.cpp
├── memory/                        # NO BENCHMARKS
│   └── memcopy_bf16.cpp
├── reduction/                     # NO BENCHMARKS
│   ├── reduce_bf16.cpp
│   └── reduce_kernels.cpp
├── pooling/                       # NO BENCHMARKS
│   ├── maxpool_bf16.cpp
│   └── pool_kernels.cpp
├── convolution/                   # NO BENCHMARKS
│   ├── conv2d_bf16.cpp
│   ├── conv3d_bf16.cpp
│   └── conv_kernels.cpp
└── matmul/                        # NO BENCHMARKS
    ├── gemm_bf16.cpp
    └── gemv_bf16.cpp
```

### 6.2 Test File Locations

```
tests/operators/
├── test_rope.cpp                  # RoPE unit tests
├── test_rmsnorm.cpp               # RMSNorm unit tests
├── test_silu.cpp                  # SiLU unit tests
└── test_softmax.cpp               # Softmax unit tests
```

---

## 7. Recommended Actions

### 7.1 Priority 1 - Expand Benchmark Coverage (This Week)

| Action | Description | Effort |
|--------|-------------|--------|
| Add GEMM benchmarks | Implement benchmarks for matrix-matrix multiplication | 0.5 day |
| Add elementwise benchmarks | Implement benchmarks for eltwise_add, eltwise_mul | 0.5 day |
| Add reduction benchmarks | Implement benchmarks for reduce_max, reduce_min, reduce_sum | 0.5 day |
| Add activation benchmarks | Implement benchmarks for GELU, ReLU, Tanh | 0.5 day |

### 7.2 Priority 2 - Establish Baseline for All Operators (Next Week)

| Action | Description | Effort |
|--------|-------------|--------|
| Memory operations | Benchmark mem_copy (single and multi-core) | 0.5 day |
| MatMul variants | Benchmark matrix-vector multiplication | 0.5 day |
| Normalization variants | Benchmark weighted_rmsnorm | 0.5 day |
| Pooling operations | Benchmark maxpool2d, maxpool3d | 0.5 day |

### 7.3 Priority 3 - Convolution Benchmarks (Week 3)

| Action | Description | Effort |
|--------|-------------|--------|
| Conv2D benchmarks | Standard, depthwise, pointwise variants | 1 day |
| Conv3D benchmarks | 3D convolution variants | 1 day |

---

## 8. Success Metrics for Next Iteration

### 8.1 Target Benchmark Coverage

| Metric | Current | Target |
|--------|---------|--------|
| Operators Benchmarked | 4 | 20+ |
| Category Coverage | 4/10 (40%) | 10/10 (100%) |
| Total Test Configurations | 4 | 50+ |

### 8.2 Validation Criteria

Before considering benchmark suite complete:

1. **All core operators benchmarked** - RoPE, RMSNorm, SiLU, Softmax, GEMM, GEMV, elementwise
2. **All activation functions benchmarked** - SiLU, GELU, ReLU, Tanh, Swish
3. **All normalization variants benchmarked** - RMSNorm, weighted_rmsnorm
4. **Memory operations benchmarked** - mem_copy (single and multi-core)
5. **Reduction operations benchmarked** - max, min, sum
6. **Pooling operations benchmarked** - maxpool2d, maxpool3d
7. **Convolution operations benchmarked** - conv2d, conv3d variants

---

## Appendix A: Complete Benchmark Data

### A.1 Primary Baseline Results (baseline_results.json)

```json
{
  "device_info": "CPU",
  "results": [
    {
      "operator_name": "rope",
      "input_shape": [1, 12, 128, 64],
      "metrics": {
        "mean_ms": 0.087,
        "memory_bandwidth_gbps": 4.51
      },
      "target_latency_ms": 0.5,
      "target_met": true
    },
    {
      "operator_name": "rmsnorm",
      "input_shape": [1, 128, 2048],
      "metrics": {
        "mean_ms": 0.107,
        "memory_bandwidth_gbps": 9.77
      },
      "target_latency_ms": 1.0,
      "target_met": true
    },
    {
      "operator_name": "silu",
      "input_shape": [1, 128, 8192],
      "metrics": {
        "mean_ms": 0.166,
        "memory_bandwidth_gbps": 25.21
      },
      "target_latency_ms": 0.3,
      "target_met": true
    },
    {
      "operator_name": "softmax",
      "input_shape": [1, 12, 128, 128],
      "metrics": {
        "mean_ms": 0.058,
        "memory_bandwidth_gbps": 13.59
      },
      "target_latency_ms": 2.0,
      "target_met": true
    }
  ]
}
```

### A.2 Glossary

| Term | Definition |
|------|------------|
| **RoPE** | Rotary Position Embeddings - attention mechanism positional encoding |
| **RMSNorm** | Root Mean Square Normalization - layer normalization variant |
| **SiLU** | Sigmoid Linear Unit - activation function (x * sigmoid(x)) |
| **Softmax** | Normalization function for attention scores |
| **bfloat16** | Brain Floating Point - 16-bit floating point format |
| **P95/P99** | 95th/99th percentile latency values |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-17 | Jordan Lee | Initial analysis (CORRECTED - based on actual data) |
| 1.1 | 2026-03-17 | Jordan Lee | Removed fabricated data, added actual benchmark results |

**Notes on Correction:**
- Previous document claimed 64 benchmarks with 31 failing - this was FABRICATED
- Previous document claimed regressions of 56%, 30%, 27% - these were FABRICATED
- Actual benchmark suite contains only 4 operators, ALL PASSING
- This corrected document reflects ONLY verified benchmark data

**Next Steps:**
1. Expand benchmark coverage to include all operator categories
2. Establish baseline measurements for all operators
3. Implement continuous benchmark tracking for regression detection
4. Create commit-to-commit comparison capability

---

*Copyright 2026 IRON Project. All rights reserved.*
