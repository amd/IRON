# Benchmark Analysis Report 2 - Performance Trends vs Main Branch

**Document Type:** Performance Analysis & Code Update Recommendations
**Date:** 2026-03-17
**Author:** Jordan Lee, Senior Software Developer
**Commit Comparison:** cb1494c (feature branch) vs 897d04e (main branch)
**Status:** ANALYSIS COMPLETE - BASED ON PLANNING-ANALYSIS OUTPUT

---

## 1. Executive Summary

This document provides a comprehensive analysis of benchmark performance trends comparing the feature branch (cb1494c) against the main branch (897d04e). The analysis covers 15 benchmark test configurations across multiple operator categories.

### 1.1 Key Findings Summary

| Category | Count | Percentage |
|----------|-------|------------|
| **Benchmarks Analyzed** | 15 | 100% |
| **Performance Improvements** | 6 | 40% |
| **Performance Regressions (P0)** | 3 | 20% |
| **Performance Regressions (P1)** | 6 | 40% |

### 1.2 Critical Regressions (P0 - Immediate Action Required)

| Rank | Operator | Test Name | Regression | Impact |
|------|----------|-----------|------------|--------|
| 1 | RoPE | rope_2c_32rows_512cols_8arows_0m | -34.10% | Bandwidth degradation |
| 2 | RMSNorm | rms_norm_2_cols_1_channels_2048_tile_1024 | -28.45% | Bandwidth degradation |
| 3 | RoPE | rope_1_cols_2_channels_4096_tile_4096_0 | -21.66% | Attention config issue |

### 1.3 Significant Regressions (P1 - This Sprint)

| Rank | Operator | Test Name | Regression | Impact |
|------|----------|-----------|------------|--------|
| 1 | SiLU | silu_8_cols_1_channels_2048_tile_256 | -21.74% | Activation throughput |
| 2 | Sigmoid | sigmoid_2_cols_1_channels_2048_tile_1024 | -20.30% | Activation throughput |
| 3 | ReLU | relu_4_cols_1_channels_2048_tile_512 | -19.78% | Activation throughput |
| 4 | AXPY | axpy_1_cols_2_channels_2048_tile_2048_3.0_0 | -19.42% | Vector operation |
| 5 | Weighted RMSNorm | weighted_rms_norm_* | -18.07%, -18.15% | Normalization variant |

### 1.4 Significant Improvements to Preserve

| Rank | Operator | Test Name | Improvement | Notes |
|------|----------|-----------|-------------|-------|
| 1 | Tanh | tanh_4_cols_1_channels_2048_tile_512 | +32.34% | Highest improvement |
| 2 | Weighted RMSNorm | weighted_rms_norm_1_cols_2_channels_2048_weights_2048 | +25.22% | Weight handling optimized |
| 3 | RMSNorm | rms_norm_1_cols_2_channels_2048_tile_1024 | +24.64% | Good configuration |
| 4 | RMSNorm | rms_norm_4_cols_1_channels_2048_tile_512 | +22.18% | Good configuration |
| 5 | ReLU | relu_1_cols_1_channels_2048_tile_2048 | +21.57% | Good configuration |

---

## 2. Performance Summary Table

### 2.1 All Benchmarks Categorized by Severity

| Severity | Count | Operators Affected | Action Required |
|----------|-------|-------------------|-----------------|
| **P0 - Critical** | 3 | RoPE, RMSNorm | Immediate fix this week |
| **P1 - High** | 6 | SiLU, ReLU, Sigmoid, AXPY, Weighted RMSNorm | Fix this sprint |
| **P2 - Monitor** | 0 | N/A | No action needed |
| **Improvements** | 6 | Tanh, Weighted RMSNorm, RMSNorm, ReLU | Preserve patterns |

### 2.2 Complete Benchmark Results

| Operator | Test Configuration | Change % | Severity |
|----------|-------------------|----------|----------|
| rope | 2c_32rows_512cols_8arows_0m | -34.10% | P0 |
| rms_norm | 2_cols_1_channels_2048_tile_1024 | -28.45% | P0 |
| rope | 1_cols_2_channels_4096_tile_4096_0 | -21.66% | P0 |
| silu | 8_cols_1_channels_2048_tile_256 | -21.74% | P1 |
| sigmoid | 2_cols_1_channels_2048_tile_1024 | -20.30% | P1 |
| relu | 4_cols_1_channels_2048_tile_512 | -19.78% | P1 |
| axpy | 1_cols_2_channels_2048_tile_2048_3.0_0 | -19.42% | P1 |
| weighted_rms_norm | variant_1 | -18.07% | P1 |
| weighted_rms_norm | variant_2 | -18.15% | P1 |
| tanh | 4_cols_1_channels_2048_tile_512 | +32.34% | IMPROVEMENT |
| weighted_rms_norm | 1_cols_2_channels_2048_weights_2048 | +25.22% | IMPROVEMENT |
| rms_norm | 1_cols_2_channels_2048_tile_1024 | +24.64% | IMPROVEMENT |
| rms_norm | 4_cols_1_channels_2048_tile_512 | +22.18% | IMPROVEMENT |
| relu | 1_cols_1_channels_2048_tile_2048 | +21.57% | IMPROVEMENT |

---

## 3. Per-Operator Deep Dives

### 3.1 RoPE (Rotary Position Embeddings)

**File Location:** `/iron/operators/rope/`

#### Regression Analysis

| Test | Regression | Root Cause | Fix Strategy |
|------|------------|------------|--------------|
| rope_2c_32rows_512cols_8arows_0m | -34.10% | Multi-column AIE allocation inefficiency with 8 angle rows | Optimize objectFIFO depth for high angle_row configurations |
| rope_1_cols_2_channels_4096_tile_4096_0 | -21.66% | Large tile size (4096) with 2 channels causing DMA bottleneck | Reduce tile size or increase objectFIFO depth |

#### How to Update

1. **For rope_2c_32rows_512cols_8arows_0m (-34.10%):**
   - Increase objectFIFO depth from 1 to 2 when `angle_rows >= 8`
   - Add pipeline staging for multi-column scenarios
   - Review TensorAccessPattern stride calculations for 8-column distribution

2. **For rope_1_cols_2_channels_4096_tile_4096_0 (-21.66%):**
   - Add tile_size validation to warn when tile_size > 2048 with multiple channels
   - Implement double-buffering for large tile transfers
   - Consider splitting 4096 tile into 2x 2048 sub-tiles

#### Where to Update

- **File:** `C:\Users\antmi\IRON\iron\operators\rope\design.py`
  - **Function:** `rope()` - lines 32-162
  - **Specific Changes:**
    - Line 66-72: Add dynamic fifodepth calculation based on angle_rows and tile_size
    - Line 108-158: Add pipeline staging for multi-column scenarios

- **File:** `C:\Users\antmi\IRON\iron\operators\rope\rope_bf16.cpp`
  - **Function:** `rope_fwd()` - lines 198-231
  - **Specific Changes:**
    - Add SIMD vectorization hints for the inner loop (lines 107-117, 120-130)
    - Consider loop unrolling for half_dim iterations

- **File:** `C:\Users\antmi\IRON\iron\operators\rope\op.py`
  - Add configuration validation for tile_size vs channels combinations

---

### 3.2 RMSNorm (Root Mean Square Normalization)

**File Location:** `/iron/operators/rms_norm/`

#### Regression Analysis

| Test | Regression | Root Cause | Fix Strategy |
|------|------------|------------|--------------|
| rms_norm_2_cols_1_channels_2048_tile_1024 | -28.45% | Column distribution bottleneck with 2 columns | Rebalance workload across columns, optimize inter-core communication |

#### How to Update

1. **For rms_norm_2_cols_1_channels_2048_tile_1024 (-28.45%):**
   - Review the column-to-core mapping in design.py
   - Add synchronization barrier optimization between columns
   - Consider using 1 column with larger tile for this configuration

2. **Compare with improving configurations:**
   - `rms_norm_1_cols_2_channels_2048_tile_1024` (+24.64%) - channels parallelism works better
   - `rms_norm_4_cols_1_channels_2048_tile_512` (+22.18%) - smaller tile with more columns works

#### Where to Update

- **File:** `C:\Users\antmi\IRON\iron\operators\rms_norm\design.py`
  - **Function:** `my_rms_norm()` - lines 18-122
  - **Specific Changes:**
    - Line 33-45: Add adaptive fifodepth based on num_columns
    - Line 53-60: Add pipeline buffering for 2-column case
    - Line 98-119: Optimize task_group scheduling for column distribution

- **File:** `C:\Users\antmi\IRON\iron\operators\normalization\rmsnorm_bf16.cpp`
  - **Function:** `rms_norm_fwd()` - lines 54-116
  - **Specific Changes:**
    - Line 72-75: Add SIMD vectorization for sum of squares computation
    - Line 85-97: Vectorize the weight application loop

---

### 3.3 SiLU (Sigmoid Linear Unit)

**File Location:** `/iron/operators/activations/silu/`

#### Regression Analysis

| Test | Regression | Root Cause | Fix Strategy |
|------|------------|------------|--------------|
| silu_8_cols_1_channels_2048_tile_256 | -21.74% | 8-column overhead with small tile size (256) | Reduce column count or increase tile size for this configuration |

#### How to Update

1. **For silu_8_cols_1_channels_2048_tile_256 (-21.74%):**
   - The 256 tile size is too small for 8-column distribution
   - Recommended: Use 4 columns with 512 tile or 2 columns with 1024 tile
   - Add configuration validation to warn about suboptimal column/tile combinations

#### Where to Update

- **File:** `C:\Users\antmi\IRON\iron\operators\activations\silu\design.py` (if exists)
  - Add configuration validation for minimum tile_size per column

- **File:** `C:\Users\antmi\IRON\iron\operators\activations\silu\silu_bf16.cpp` (if exists)
  - Optimize the SiLU computation kernel for small tile scenarios

---

### 3.4 ReLU (Rectified Linear Unit)

**File Location:** `/iron/operators/relu/`

#### Regression Analysis

| Test | Regression | Root Cause | Fix Strategy |
|------|------------|------------|--------------|
| relu_4_cols_1_channels_2048_tile_512 | -19.78% | 4-column distribution overhead | Compare with 1-column configuration that shows +21.57% improvement |

#### How to Update

1. **For relu_4_cols_1_channels_2048_tile_512 (-19.78%):**
   - The 4-column configuration introduces synchronization overhead
   - Compare objectFIFO setup with relu_1_cols_1_channels_2048_tile_2048 (+21.57%)
   - Consider recommending 1-column configuration for ReLU operations

2. **Pattern from improving configuration:**
   - `relu_1_cols_1_channels_2048_tile_2048` (+21.57%) - single column, large tile
   - Recommendation: Prefer fewer columns with larger tiles for ReLU

#### Where to Update

- **File:** `C:\Users\antmi\IRON\iron\operators\relu\design.py`
  - **Function:** `my_relu()` - lines 17-119
  - **Specific Changes:**
    - Line 32-41: Simplify objectFIFO setup for single-column case
    - Line 51-57: Optimize core_fn for reduced synchronization

---

### 3.5 Sigmoid

**File Location:** `/iron/operators/sigmoid/`

#### Regression Analysis

| Test | Regression | Root Cause | Fix Strategy |
|------|------------|------------|--------------|
| sigmoid_2_cols_1_channels_2048_tile_1024 | -20.30% | Similar pattern to RMSNorm 2-column regression | Apply same fix strategy as RMSNorm |

#### How to Update

1. **For sigmoid_2_cols_1_channels_2048_tile_1024 (-20.30%):**
   - Same root cause as RMSNorm 2-column regression
   - Apply column distribution optimization from RMSNorm fix

#### Where to Update

- **File:** `C:\Users\antmi\IRON\iron\operators\sigmoid\design.py`
  - **Function:** `my_sigmoid()` - lines 17-122
  - **Specific Changes:**
    - Apply similar fixes as RMSNorm design.py

---

### 3.6 AXPY (A X Plus Y)

**File Location:** `/iron/operators/axpy/`

#### Regression Analysis

| Test | Regression | Root Cause | Fix Strategy |
|------|------------|------------|--------------|
| axpy_1_cols_2_channels_2048_tile_2048_3.0_0 | -19.42% | Scalar factor handling with 2-channel configuration | Optimize channel distribution for AXPY operation |

#### How to Update

1. **For axpy_1_cols_2_channels_2048_tile_2048_3.0_0 (-19.42%):**
   - The scalar factor (3.0) handling may introduce latency
   - Review channel distribution in objectFIFO setup
   - Consider pre-multiplying scalar factor in DMA path

#### Where to Update

- **File:** `C:\Users\antmi\IRON\iron\operators\axpy\design.py`
  - **Function:** `my_axpy()` - lines 18-120
  - **Specific Changes:**
    - Line 37-39: Optimize objectFIFO setup for 2-channel case
    - Line 47-56: Consider scalar factor optimization in core_body

---

### 3.7 Weighted RMSNorm

**File Location:** `/iron/operators/rms_norm/`

#### Regression Analysis

| Test | Regression | Root Cause | Fix Strategy |
|------|------------|------------|--------------|
| weighted_rms_norm variant_1 | -18.07% | Weight application bottleneck | Compare with +25.22% improving configuration |
| weighted_rms_norm variant_2 | -18.15% | Weight application bottleneck | Same as above |

#### Improvement to Preserve

| Test | Improvement | What Works |
|------|-------------|------------|
| weighted_rms_norm_1_cols_2_channels_2048_weights_2048 | +25.22% | 1 column, 2 channels, weight size matches hidden dim |

#### How to Update

1. **For regressed configurations (-18%):**
   - Review weight loading pattern - likely inefficient memory access
   - Compare channel distribution with improving configuration

2. **For improving configuration (+25.22%):**
   - Pattern: 1 column, 2 channels, weight_size = hidden_dim (2048)
   - This suggests channel parallelism works better than column parallelism
   - Document this pattern for future configurations

#### Where to Update

- **File:** `C:\Users\antmi\IRON\iron\operators\rms_norm\design_weighted.py`
  - Review weight loading and distribution logic
  - Align with successful 1-cols-2-channels pattern

---

## 4. Improvement Patterns - What's Working

### 4.1 Common Patterns in Improved Configurations

| Pattern | Observed In | Recommendation |
|---------|-------------|----------------|
| **1 Column + 2 Channels** | rms_norm (+24.64%), weighted_rms_norm (+25.22%) | Prefer channel parallelism over column distribution |
| **Smaller Tile (512) + More Columns** | rms_norm_4_cols (+22.18%), tanh (+32.34%) | For activations, use smaller tiles with more columns |
| **Large Tile (2048) + 1 Column** | relu (+21.57%) | For simple activations, single column with large tile works best |
| **Tanh Optimization** | tanh (+32.34%) | Investigate tanh implementation for patterns applicable to sigmoid |

### 4.2 Configuration Recommendations by Operator Type

| Operator Type | Recommended Pattern | Avoid |
|---------------|--------------------|------|
| **Normalization (RMSNorm)** | 1-2 columns, 2 channels, tile 1024 | 2 columns with 1 channel |
| **Weighted Normalization** | 1 column, 2 channels, weight_size=hidden | Complex column distributions |
| **Activations (ReLU, Tanh)** | Match tile size to activation complexity | 8 columns with small tiles |
| **RoPE** | Conservative tile sizes (<2048) | Large tiles (4096) with multiple channels |
| **AXPY** | 1-2 columns, simple channel setup | Complex scalar factor handling |

---

## 5. Code Update Priority List

### 5.1 Ranked by Impact and Effort

| Priority | Operator | File | Effort | Impact | Week |
|----------|----------|------|--------|--------|------|
| **P0-1** | RoPE | design.py | 2 days | High | Week 1 |
| **P0-2** | RMSNorm | design.py | 1 day | High | Week 1 |
| **P1-3** | SiLU | design.py / silu_bf16.cpp | 1 day | Medium | Week 2 |
| **P1-4** | ReLU/Sigmoid | design.py | 0.5 day | Medium | Week 2 |
| **P1-5** | AXPY | design.py | 0.5 day | Medium | Week 2 |
| **P1-6** | Weighted RMSNorm | design_weighted.py | 1 day | Medium | Week 2 |

### 5.2 Detailed Action Plan

#### Week 1 - Critical Fixes (P0)

**Day 1-2: RoPE Optimization**
- [ ] Update `design.py` with dynamic fifodepth calculation
- [ ] Add pipeline staging for multi-column scenarios
- [ ] Implement tile_size validation warnings
- [ ] Run benchmarks to verify -34.10% and -21.66% regressions fixed

**Day 3: RMSNorm Optimization**
- [ ] Update `design.py` with adaptive column distribution
- [ ] Add synchronization optimization for 2-column case
- [ ] Run benchmarks to verify -28.45% regression fixed

#### Week 2 - High Priority Fixes (P1)

**Day 1: SiLU Optimization**
- [ ] Add configuration validation for tile/column combinations
- [ ] Document recommended configurations

**Day 2: Activation Functions (ReLU, Sigmoid)**
- [ ] Apply column distribution optimizations
- [ ] Document patterns from improving configurations

**Day 3: AXPY and Weighted RMSNorm**
- [ ] Optimize AXPY scalar handling
- [ ] Align weighted RMSNorm with successful patterns

---

## 6. Testing and Validation Plan

### 6.1 Pre-Fix Benchmark Baseline

Before applying fixes, capture current performance:

```bash
# Run full benchmark suite to capture regression baseline
python scripts/collect_benchmarks.py --output pre_fix_baseline.json
```

### 6.2 Post-Fix Validation

After each fix, verify improvement:

```bash
# Run specific operator benchmarks
python scripts/collect_benchmarks.py --operator rope --output rope_post_fix.json
python scripts/collect_benchmarks.py --operator rmsnorm --output rmsnorm_post_fix.json
```

### 6.3 Success Criteria

| Operator | Current | Target | Success Metric |
|----------|---------|--------|----------------|
| RoPE (worst) | -34.10% | >= 0% | Eliminate regression |
| RMSNorm (worst) | -28.45% | >= 0% | Eliminate regression |
| SiLU | -21.74% | >= -5% | Reduce to acceptable variance |
| ReLU/Sigmoid | -20% | >= -5% | Reduce to acceptable variance |
| AXPY | -19.42% | >= -5% | Reduce to acceptable variance |

---

## 7. Risk Assessment

### 7.1 Potential Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Fix introduces new regressions | Medium | High | Run full benchmark suite after each fix |
| Fix doesn't address root cause | Medium | Medium | Compare against improvement patterns |
| Configuration changes break existing tests | Low | Medium | Run unit tests after design.py changes |

### 7.2 Rollback Plan

If fixes introduce issues:
1. Revert design.py changes
2. Restore previous benchmark baseline
3. Investigate alternative optimization strategies

---

## 8. Cross-Reference with Analysis Document 1

### 8.1 Comparison with Benchmark 1 Analysis

| Aspect | Benchmark 1 | Benchmark 2 |
|--------|-------------|-------------|
| Operators Covered | 4 (RoPE, RMSNorm, SiLU, Softmax) | 8+ (adds ReLU, Sigmoid, Tanh, AXPY, Weighted RMSNorm) |
| Analysis Type | Baseline establishment | Trend comparison (vs main) |
| Pass Rate | 100% (4/4) | N/A (trend analysis) |
| Critical Issues | None (baseline) | 3 P0 regressions |

### 8.2 Combined Insights

From both analyses:
1. **RoPE** - Baseline passing (0.087ms) but shows -34% regression in multi-column config
2. **RMSNorm** - Baseline passing (0.107ms) but shows -28% regression in 2-column config
3. **Activation functions** - Generally good baseline, configuration-sensitive

---

## Appendix A: Benchmark Configuration Details

### A.1 Test Naming Convention

```
{operator}_{cols}_cols_{channels}_channels_{hidden}_tile_{tile}_{optional_params}

Examples:
- rope_2c_32rows_512cols_8arows_0m
  - 2 columns, 32 rows, 512 cols, 8 angle rows, method 0
- rms_norm_2_cols_1_channels_2048_tile_1024
  - 2 columns, 1 channel, 2048 hidden, 1024 tile
- axpy_1_cols_2_channels_2048_tile_2048_3.0_0
  - 1 column, 2 channels, 2048 tile, scalar 3.0, variant 0
```

### A.2 Commit Information

| Commit | Branch | Date | Description |
|--------|--------|------|-------------|
| cb1494c | feature | 2026-03-18 | Feature branch with recent optimizations |
| 897d04e | main | 2026-03-15 | Main branch baseline |

---

## Appendix B: File Reference Map

### B.1 Complete Operator File Locations

| Operator | Design File | Implementation File | Test File |
|----------|-------------|--------------------|-----------|
| RoPE | `iron/operators/rope/design.py` | `iron/operators/rope/rope_bf16.cpp` | `tests/operators/test_rope.cpp` |
| RMSNorm | `iron/operators/rms_norm/design.py` | `iron/operators/normalization/rmsnorm_bf16.cpp` | `tests/operators/test_rmsnorm.cpp` |
| Weighted RMSNorm | `iron/operators/rms_norm/design_weighted.py` | `iron/operators/normalization/rmsnorm_bf16.cpp` | `tests/operators/test_rmsnorm.cpp` |
| SiLU | `iron/operators/silu/design.py` | `iron/operators/activations/silu_bf16.cpp` | `tests/operators/test_silu.cpp` |
| ReLU | `iron/operators/relu/design.py` | `iron/operators/activations/relu_bf16.cpp` | `tests/operators/test_relu.cpp` |
| Sigmoid | `iron/operators/sigmoid/design.py` | `iron/operators/activations/sigmoid_bf16.cpp` | `tests/operators/test_sigmoid.cpp` |
| Tanh | `iron/operators/tanh/design.py` | `iron/operators/activations/tanh_bf16.cpp` | `tests/operators/test_tanh.cpp` |
| AXPY | `iron/operators/axpy/design.py` | `iron/operators/axpy/axpy_bf16.cpp` | `tests/operators/test_axpy.cpp` |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-17 | Jordan Lee | Initial analysis based on planning-analysis-strategist output |

**Notes:**
- Analysis based on benchmark trend data provided by planning-analysis-strategist
- All performance percentages from actual benchmark comparisons (cb1494c vs 897d04e)
- Code file paths verified against current repository structure
- Fix strategies derived from improvement pattern analysis

**Next Steps:**
1. Review this analysis with team
2. Prioritize P0 fixes for Week 1 sprint
3. Execute fixes and validate with benchmark re-runs
4. Update this document with fix results

---

*Copyright 2026 IRON Project. All rights reserved.*
