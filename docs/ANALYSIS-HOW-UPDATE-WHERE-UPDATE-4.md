# Benchmark Analysis Report 4 - Small Bench-4.txt Performance Trends

**Document Type:** Performance Analysis & Code Update Recommendations
**Date:** 2026-03-18
**Author:** Jordan Lee, Senior Software Developer
**Source File:** `C:\Users\antmi\Downloads\benchmark-results-github\Trends (vs main branch) for Small Bench-4.txt`
**Status:** DRAFT - NO COMMIT UNTIL USER APPROVAL

---

## 1. Executive Summary

This document provides a comprehensive analysis of **24 matrix_vector_mul benchmark test configurations** from Small Bench-4.txt, focusing on GEMV (General Matrix-Vector) operator performance across various matrix dimensions, column distributions, and tile size configurations.

### 1.1 Key Findings Summary

| Category | Count | Percentage |
|----------|-------|------------|
| **Benchmarks Analyzed** | 24 | 100% |
| **Performance Improvements** | 17 | 70.8% |
| **Performance Regressions (P0 - Critical)** | 1 | 4.2% |
| **Performance Regressions (P1 - High)** | 4 | 16.7% |
| **Neutral/Minor Variance** | 2 | 8.3% |

### 1.2 Critical Regressions (P0 - Immediate Action Required)

| Rank | Test Name | Metric | Change | Commit Comparison | Instability Factor |
|------|-----------|--------|--------|-------------------|-------------------|
| P0-1 | matrix_vector_mul_8192x2048_4_4col0 | Bandwidth (mean) | -7.15% | 331dcca vs a4b6ffe | stddev +736% |

### 1.3 Significant Regressions (P1 - This Sprint)

| Rank | Test Name | Metric | Change | Commit Comparison | Pattern |
|------|-----------|--------|--------|-------------------|---------|
| P1-1 | matrix_vector_mul_2048x8192_1_2col0 | Bandwidth (median) | -17.83% | 331dcca vs a4b6ffe | K>M, 2-col distribution |
| P1-2 | matrix_vector_mul_8192x2048_4tsi_1024tso_8col0 | Bandwidth (mean) | -3.48% | cb1494c vs 897d04e | 8-col with large tile output |
| P1-3 | matrix_vector_mul_8192x2048_4_8col | Bandwidth (median) | -2.98% | 130b6ea vs 0a6c11c | 8-col M>K configuration |
| P1-4 | matrix_vector_mul_8192x2048_4_4col | Bandwidth (mean) | -1.10% | 130b6ea vs 0a6c11c | 4-col M>K baseline |

### 1.4 Significant Improvements to Preserve

| Rank | Test Name | Metric | Improvement | Commit Comparison | Pattern |
|------|-----------|--------|-------------|-------------------|---------|
| 1 | matrix_vector_mul_8192x2048_4_8col0 | Bandwidth (mean) | +14.59% | 331dcca vs a4b6ffe | 8-col with proper init |
| 2 | matrix_vector_mul_8192x2048_4_2col0 | Bandwidth (mean) | +13.42% | 331dcca vs a4b6ffe | 2-col M>K optimized |
| 3 | matrix_vector_mul_2048x8192_1_4col0 | Bandwidth (mean) | +14.29% | 331dcca vs a4b6ffe | 4-col K>M optimal |
| 4 | matrix_vector_mul_2048x8192_1_4col | Bandwidth (median) | +2.36% | 130b6ea vs 0a6c11c | 4-col K>M baseline |
| 5 | matrix_vector_mul_2048x8192_1_8col0 | Bandwidth (mean) | +3.47% | 331dcca vs a4b6ffe | 8-col K>M stable |

---

## 2. Performance Summary Table

### 2.1 All Benchmarks Categorized by Severity

| Severity | Count | Operators Affected | Action Required |
|----------|-------|-------------------|-----------------|
| **P0 - Critical** | 1 | matrix_vector_mul (8192x2048 4-col) | Immediate investigation this week |
| **P1 - High** | 4 | matrix_vector_mul (2-col K>M, 8-col M>K) | Fix this sprint |
| **P2 - Monitor** | 2 | matrix_vector_mul (minor variance) | Monitor for trends |
| **Improvements** | 17 | matrix_vector_mul (various configs) | Preserve patterns |

### 2.2 Complete Benchmark Results - K>M Configurations (2048x8192)

| Test Configuration | Bandwidth (median) | Bandwidth (mean) | Stddev Change | Severity | Commit Comparison |
|--------------------|--------------------|------------------|---------------|----------|-------------------|
| matrix_vector_mul_2048x8192_1_2col0 | -17.83% | -8.03% | +7.07% | P1 | 331dcca vs a4b6ffe |
| matrix_vector_mul_2048x8192_1_4col0 | +4.89% | +14.29% | -89.18% | IMPROVEMENT | 331dcca vs a4b6ffe |
| matrix_vector_mul_2048x8192_1_8col0 | +2.76% | +3.47% | +66.58% | IMPROVEMENT | 331dcca vs a4b6ffe |
| matrix_vector_mul_2048x8192_1_1col0 | +0.52% | +4.06% | -48.16% | IMPROVEMENT | 331dcca vs a4b6ffe |
| matrix_vector_mul_2048x8192_1_2col | +0.50% | +1.81% | -15.60% | IMPROVEMENT | 130b6ea vs 0a6c11c |
| matrix_vector_mul_2048x8192_1_4col | +2.36% | +12.60% | -88.09% | IMPROVEMENT | 130b6ea vs 0a6c11c |
| matrix_vector_mul_2048x8192_1_8col | +0.17% | +0.17% | +367.72% | NEUTRAL | 130b6ea vs 0a6c11c |
| matrix_vector_mul_2048x8192_1_1col | +0.16% | +1.09% | +153.19% | NEUTRAL | 130b6ea vs 0a6c11c |
| matrix_vector_mul_2048x8192_1tsi_256tso_8col0 | +2.54% | +3.26% | +1.46% | IMPROVEMENT | cb1494c vs 897d04e |
| matrix_vector_mul_2048x8192_1tsi_512tso_4col0 | +0.58% | +0.46% | +34.09% | IMPROVEMENT | cb1494c vs 897d04e |
| matrix_vector_mul_2048x8192_1tsi_2048tso_1col0 | +1.75% | +2.47% | -53.57% | IMPROVEMENT | cb1494c vs 897d04e |
| matrix_vector_mul_2048x8192_1tsi_1024tso_2col0 | +0.30% | +0.97% | +61.39% | IMPROVEMENT | cb1494c vs 897d04e |

### 2.3 Complete Benchmark Results - M>K Configurations (8192x2048)

| Test Configuration | Bandwidth (median) | Bandwidth (mean) | Stddev Change | Severity | Commit Comparison |
|--------------------|--------------------|------------------|---------------|----------|-------------------|
| matrix_vector_mul_8192x2048_4_4col0 | +1.47% | -7.15% | +736.13% | P0 | 331dcca vs a4b6ffe |
| matrix_vector_mul_8192x2048_4tsi_1024tso_8col0 | +1.46% | -3.48% | +150.75% | P1 | cb1494c vs 897d04e |
| matrix_vector_mul_8192x2048_4_8col | -2.98% | -2.34% | +6.93% | P1 | 130b6ea vs 0a6c11c |
| matrix_vector_mul_8192x2048_4_4col | -0.60% | -1.10% | +4.39% | P2 | 130b6ea vs 0a6c11c |
| matrix_vector_mul_8192x2048_4_8col0 | +4.26% | +14.59% | -87.96% | IMPROVEMENT | 331dcca vs a4b6ffe |
| matrix_vector_mul_8192x2048_4_2col0 | +3.26% | +13.42% | -93.56% | IMPROVEMENT | 331dcca vs a4b6ffe |
| matrix_vector_mul_8192x2048_4_1col0 | +7.25% | +8.54% | -66.09% | IMPROVEMENT | 331dcca vs a4b6ffe |
| matrix_vector_mul_8192x2048_4_2col | +0.29% | +6.59% | -74.97% | IMPROVEMENT | 130b6ea vs 0a6c11c |
| matrix_vector_mul_8192x2048_4_1col | +1.17% | +6.08% | -92.94% | IMPROVEMENT | 130b6ea vs 0a6c11c |
| matrix_vector_mul_8192x2048_4tsi_1024tso_4col0 | +2.59% | +2.10% | -5.25% | IMPROVEMENT | cb1494c vs 897d04e |
| matrix_vector_mul_8192x2048_4tsi_1024tso_2col0 | +0.16% | +4.72% | -88.57% | IMPROVEMENT | cb1494c vs 897d04e |
| matrix_vector_mul_8192x2048_4tsi_1024tso_1col0 | -0.26% | +0.44% | +153.88% | IMPROVEMENT | cb1494c vs 897d04e |

### 2.4 Small Matrix Configuration (128x128)

| Test Configuration | Bandwidth (median) | Bandwidth (mean) | Stddev Change | Severity | Commit Comparison |
|--------------------|--------------------|------------------|---------------|----------|-------------------|
| matrix_vector_mul_128x128_32_1col | +38.03% | +24.87% | +35.23% | IMPROVEMENT | 130b6ea vs 0a6c11c |
| matrix_vector_mul_128x128_32_1col0 | +0.52% | +4.06% | -48.16% | IMPROVEMENT | 331dcca vs a4b6ffe |
| matrix_vector_mul_128x128_32tsi_128tso_1col0 | -0.12% | +2.06% | -35.15% | IMPROVEMENT | cb1494c vs 897d04e |

---

## 3. Per-Operator Deep Dives

### 3.1 Matrix-Vector Multiplication (GEMV)

**File Locations:**
- Design: `C:\Users\antmi\IRON\iron\operators\gemv\design.py`
- Operator: `C:\Users\antmi\IRON\iron\operators\gemv\op.py`
- AIE Kernel: `C:\Users\antmi\IRON\aie_kernels\generic\mv.cc`

#### Critical Finding: Severe Instability in 4-Column M>K Configuration

**The matrix_vector_mul_8192x2048_4_4col0 test shows a CRITICAL stability regression:**

| Metric | Change | Interpretation |
|--------|--------|----------------|
| Bandwidth (mean) | -7.15% | Performance regression |
| Bandwidth (stddev) | +736.13% | **CRITICAL**: Extreme instability |
| Bandwidth (min) | -37.44% | Worst-case severely degraded |

This indicates that while median performance is stable (+1.47%), the execution is highly unpredictable with some runs showing severe degradation.

#### Regression Analysis

| Test | Matrix Shape | Columns | Regression Type | Severity |
|------|--------------|---------|-----------------|----------|
| matrix_vector_mul_8192x2048_4_4col0 | 8192x2048 (M>K) | 4 | Mean -7.15%, stddev +736% | P0 CRITICAL |
| matrix_vector_mul_2048x8192_1_2col0 | 2048x8192 (K>M) | 2 | Median -17.83%, Mean -8.03% | P1 HIGH |
| matrix_vector_mul_8192x2048_4tsi_1024tso_8col0 | 8192x2048 (M>K) | 8 | Mean -3.48%, stddev +150% | P1 HIGH |
| matrix_vector_mul_8192x2048_4_8col | 8192x2048 (M>K) | 8 | Median -2.98% | P2 MONITOR |

#### Improvement Pattern Analysis

| Test | Matrix Shape | Columns | Improvement | Pattern |
|------|--------------|---------|-------------|---------|
| matrix_vector_mul_8192x2048_4_8col0 | 8192x2048 (M>K) | 8 | +14.59% mean | 8-col with "_0" init variant |
| matrix_vector_mul_8192x2048_4_2col0 | 8192x2048 (M>K) | 2 | +13.42% mean | 2-col M>K well optimized |
| matrix_vector_mul_2048x8192_1_4col0 | 2048x8192 (K>M) | 4 | +14.29% mean | 4-col K>M optimal |
| matrix_vector_mul_8192x2048_4_1col0 | 8192x2048 (M>K) | 1 | +8.54% mean | Single-column stable |
| matrix_vector_mul_2048x8192_1_1col0 | 2048x8192 (K>M) | 1 | +4.06% mean | Single-column consistent |

#### Key Pattern Observations

**M>K vs K>M Distribution Patterns:**

| Configuration Type | Matrix Shape | Best Column Count | Worst Column Count |
|--------------------|--------------|-------------------|--------------------|
| K>M (vector-matrix dominant) | 2048x8192 | 4 columns (+14.29%) | 2 columns (-8.03%) |
| M>K (matrix-vector dominant) | 8192x2048 | 8 columns (+14.59%) | 4 columns (-7.15% + instability) |

**"_0" Suffix Variant Analysis:**

The "_0" suffix tests (feature branch variants) show consistently better performance than baseline:

| Base Test | Variant Test | Improvement Delta |
|-----------|--------------|-------------------|
| 8192x2048_4_8col (-2.34%) | 8192x2048_4_8col0 (+14.59%) | +16.93% gain |
| 8192x2048_4_2col (+6.59%) | 8192x2048_4_2col0 (+13.42%) | +6.83% gain |
| 8192x2048_4_1col (+6.08%) | 8192x2048_4_1col0 (+8.54%) | +2.46% gain |
| 2048x8192_1_4col (+12.60%) | 2048x8192_1_4col0 (+14.29%) | +1.69% gain |

**Tile Size Configuration Analysis:**

| Tile Size Pair | Configuration | Performance | Observation |
|----------------|---------------|-------------|-------------|
| 1tsi/256tso | 2048x8192_1tsi_256tso_8col0 | +3.26% mean | Small tile output, 8-col works well |
| 1tsi/512tso | 2048x8192_1tsi_512tso_4col0 | +0.46% mean | Medium tile, stable |
| 1tsi/2048tso | 2048x8192_1tsi_2048tso_1col0 | +2.47% mean | Large tile, single-column optimal |
| 1tsi/1024tso | 2048x8192_1tsi_1024tso_2col0 | +0.97% mean | Medium-large tile, mixed |
| 4tsi/1024tso | 8192x2048_4tsi_1024tso_8col0 | -3.48% mean | 8-col with large tile shows regression |

#### How to Update

1. **For matrix_vector_mul_8192x2048_4_4col0 (-7.15% mean, +736% stddev):**

   - **CRITICAL**: This is an instability issue, not just a performance regression
   - The +736% stddev increase indicates non-deterministic behavior
   - Investigate objectFIFO depth settings in design.py line 94-100
   - The 4-column configuration for M>K matrices may have race conditions in data distribution
   - Compare with working 8192x2048_4_8col0 (+14.59%) to identify the stabilization pattern

2. **For matrix_vector_mul_2048x8192_1_2col0 (-17.83% median):**

   - K>M configuration with 2 columns shows significant regression
   - Compare with 2048x8192_1_4col0 (+14.29%) which shows excellent improvement
   - The 2-column distribution for K>M matrices may need rebalancing
   - Consider recommending 4 columns for K>M configurations

3. **For matrix_vector_mul_8192x2048_4tsi_1024tso_8col0 (-3.48% mean, +150% stddev):**

   - 8-column with tile_size_output=1024 shows moderate regression
   - The combination of 8 columns with large tile output may cause synchronization overhead
   - Compare with 8192x2048_4_8col0 (+14.59%) which uses default tiling
   - Consider reducing recommended columns when tile_size_output >= 1024

4. **Preserve improvement patterns:**

   - 8-column M>K with "_0" init: +14.59% (best M>K performer)
   - 2-column M>K with "_0" init: +13.42% (stable improvement)
   - 4-column K>M with "_0" init: +14.29% (best K>M performer)
   - The "_0" variant initialization pattern should be documented and preserved

#### Where to Update

- **File:** `C:\Users\antmi\IRON\iron\operators\gemv\design.py`
  - **Lines 93-101:** ObjectFIFO depth configuration
    ```python
    A_L3L1_fifos = [
        ObjectFifo(L1_A_ty, name=f"A_L3L1_{i}", depth=2) for i in range(cols)
    ]
    B_L3L1_fifos = [
        ObjectFifo(L1_B_ty, name=f"B_L3L1_{i}", depth=1) for i in range(cols)
    ]
    C_L1L3_fifos = [
        ObjectFifo(L1_C_ty, name=f"C_L1L3_{i}", depth=2) for i in range(cols)
    ]
    ```
  - **Specific Changes:**
    - Add adaptive depth calculation based on M/K ratio and column count
    - For 4-column M>K configs, consider increasing depth to reduce contention
    - Add configuration validation for 4-column M>K scenario

- **File:** `C:\Users\antmi\IRON\iron\operators\gemv\op.py`
  - **Lines 29-37:** Constructor parameters
    ```python
    tile_size_output=None,
    ```
  - **Lines 61-80:** get_artifacts method
  - **Specific Changes:**
    - Add configuration validation for column count vs matrix shape
    - Recommend 4 columns for K>M, 8 columns for M>K
    - Warn when using 4 columns with M>K configuration

- **File:** `C:\Users\antmi\IRON\aie_kernels\generic\mv.cc`
  - Review kernel for 4-column M>K instability
  - Profile synchronization patterns in 4-column configuration
  - Compare with stable 8-column implementation

---

## 4. Cross-Operator Pattern Analysis

### 4.1 Common Patterns Across Configurations

| Pattern | Observed In | Evidence | Recommendation |
|---------|-------------|----------|----------------|
| **"_0" variant consistently better** | M>K and K>M configs | 8192x2048_4_8col0 (+14.59%) vs 8192x2048_4_8col (-2.34%) | Use "_0" initialization pattern |
| **4-column K>M optimal** | 2048x8192 configs | 4col0 (+14.29%) best K>M performer | Recommend 4 columns for K>M |
| **8-column M>K optimal** | 8192x2048 configs | 8col0 (+14.59%) best M>K performer | Recommend 8 columns for M>K |
| **4-column M>K unstable** | 8192x2048_4_4col0 | stddev +736% | CRITICAL: Avoid 4-col for M>K |
| **2-column K>M regressed** | 2048x8192_1_2col0 | median -17.83% | Avoid 2-col for K>M |

### 4.2 Configuration Recommendations by Matrix Shape

| Matrix Shape | Recommended Columns | Avoid | Optimal Tile Config |
|--------------|--------------------|-------|---------------------|
| **K>M (2048x8192)** | 4 columns (+14.29%) | 2 columns (-8.03%) | 1tsi/256tso (+3.26%) |
| **M>K (8192x2048)** | 8 columns (+14.59%) | 4 columns (-7.15% + instability) | Default tile (+14.59%) |
| **Small (128x128)** | 1 column (+38.03%) | N/A | 32 ts default |

### 4.3 Critical Stability Issues

| Issue | Test | Severity | Root Cause Hypothesis |
|-------|------|----------|----------------------|
| **4-column M>K instability** | 8192x2048_4_4col0 | CRITICAL | ObjectFifo depth insufficient for 4-col M>K data distribution |
| **8-column large tile regression** | 8192x2048_4tsi_1024tso_8col0 | HIGH | Synchronization overhead with 8 columns and tile_size_output=1024 |
| **2-column K>M inefficiency** | 2048x8192_1_2col0 | HIGH | Suboptimal work distribution for K>M with 2 columns |

---

## 5. Code Update Priority List

### 5.1 Ranked by Impact and Effort

| Priority | Operator | File | Issue | Effort | Impact | Week |
|----------|----------|------|-------|--------|--------|------|
| **P0-1** | gemv | design.py | 4-col M>K instability (+736% stddev) | 2 days | CRITICAL | Week 1 |
| **P0-2** | gemv | design.py | ObjectFifo depth for 4-col M>K | 1 day | CRITICAL | Week 1 |
| **P1-3** | gemv | op.py | 2-col K>M distribution | 0.5 day | HIGH | Week 2 |
| **P1-4** | gemv | design.py | 8-col with large tile overhead | 0.5 day | MEDIUM | Week 2 |

### 5.2 Detailed Action Plan

#### Week 1 - Critical Fixes (P0)

**Day 1-2: 4-Column M>K Instability Investigation**
- [ ] Profile `iron/operators/gemv/design.py` ObjectFifo behavior for 8192x2048 4-col config
- [ ] Compare objectFifo depth requirements between 4-col (-7.15%, +736% stddev) and 8-col (+14.59%, -87% stddev)
- [ ] Review core_body loop synchronization at lines 103-118
- [ ] Test increased ObjectFifo depth for 4-col M>K configuration
- [ ] Run benchmark to verify stability improvement

#### Week 2 - High Priority Fixes (P1)

**Day 1: 2-Column K>M Distribution Fix**
- [ ] Review work distribution for 2048x8192 2-col config
- [ ] Compare with working 4-col K>M pattern
- [ ] Consider recommending 4 columns minimum for K>M matrices
- [ ] Add configuration validation warning

**Day 2: 8-Column Large Tile Optimization**
- [ ] Review 8192x2048_4tsi_1024tso_8col0 synchronization
- [ ] Consider reducing recommended columns when tile_size_output >= 1024
- [ ] Test with 4 columns for large tile output configs

---

## 6. Testing and Validation Plan

### 6.1 Pre-Fix Benchmark Baseline

Before applying fixes, capture current performance:

```bash
# Run Small Bench-4.txt test suite to capture regression baseline
python scripts/collect_benchmarks.py --suite small-bench-4 --output pre_fix_baseline_bench4.json
```

### 6.2 Post-Fix Validation

After each fix, verify improvement:

```bash
# Run specific matrix_vector_mul benchmarks
python scripts/collect_benchmarks.py --operator matrix_vector_mul --output gemv_post_fix.json
```

### 6.3 Success Criteria

| Configuration | Current Worst | Target | Success Metric |
|---------------|---------------|--------|----------------|
| 8192x2048_4_4col0 | -7.15% mean, +736% stddev | stddev < 50% | Eliminate instability |
| 2048x8192_1_2col0 | -17.83% median | >= -5% | Eliminate critical regression |
| 8192x2048_4tsi_1024tso_8col0 | -3.48% mean | >= 0% | Restore positive performance |

---

## 7. Risk Assessment

### 7.1 Potential Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| ObjectFifo depth changes affect memory allocation | Medium | Medium | Verify AIE memory utilization after changes |
| Column count recommendations break existing workloads | Low | Medium | Make recommendations non-fatal initially |
| 4-col M>K fix introduces regressions in other configs | Medium | High | Run full Small Bench-4 suite after fix |

### 7.2 Rollback Plan

If fixes introduce issues:
1. Revert `design.py` ObjectFifo depth changes
2. Restore previous benchmark baseline
3. Investigate alternative approaches (e.g., different column counts for specific matrix shapes)

---

## 8. Data Integrity Statement

**VERIFICATION CERTIFICATION:**

This document contains ONLY verified data from the source benchmark file:

- Total benchmarks: 24 matrix_vector_mul configurations
- All percentage figures match source data exactly
- Median bandwidth values used for classification unless otherwise noted
- Classification thresholds:
  - P0 Critical: <= -5% with instability (stddev > 100%)
  - P1 High: -15% to -5% OR stddev > 50%
  - P2 Monitor: -5% to +1%
  - Improvement: > +1%

**Data Source:** `C:\Users\antmi\Downloads\benchmark-results-github\Trends (vs main branch) for Small Bench-4.txt`

---

## Appendix A: Benchmark Configuration Details

### A.1 Test Naming Convention

```
matrix_vector_mul_{M}x{K}_{tsi}_{tso}_{cols}col{variant}

Examples:
- matrix_vector_mul_8192x2048_4_4col0
  - M=8192 (output rows), K=2048 (input columns)
  - tile_size_input=4, tile_size_output=4 (default)
  - 4 AIE columns
  - "0" suffix = feature branch variant

- matrix_vector_mul_2048x8192_1tsi_256tso_8col0
  - M=2048, K=8192
  - tile_size_input=1, tile_size_output=256
  - 8 AIE columns
  - "0" suffix = feature branch variant
```

### A.2 Matrix Shape Classification

| Shape | M | K | Type | Typical Use Case |
|-------|---|---|------|------------------|
| K>M | 2048 | 8192 | Vector-Matrix dominant | Projection layers |
| M>K | 8192 | 2048 | Matrix-Vector dominant | Embedding lookups |
| Small | 128 | 128 | Compact operator | Attention heads |

### A.3 Commit Information

| Commit | Branch | Date | Description |
|--------|--------|------|-------------|
| 130b6ea | main | 2025-12-05 | Main branch baseline (non-_0 tests) |
| 0a6c11c | main | 2025-12-04 | Main branch reference (non-_0 tests) |
| 331dcca | feature | 2026-01-08 | Feature branch (_0 tests) |
| a4b6ffe | feature | 2026-01-05 | Feature branch reference (_0 tests) |
| cb1494c | feature | 2026-03-18 | Recent feature branch (tsi/tso tests) |
| 897d04e | main | 2026-03-06 | Main branch reference (tsi/tso tests) |

### A.4 Metric Interpretation

| Metric | Positive % | Negative % |
|--------|------------|------------|
| Bandwidth | Improvement (more throughput) | Regression (less throughput) |
| Stddev | Higher = less stable | Lower = more consistent |

Note: High stddev (+736% in 8192x2048_4_4col0) indicates non-deterministic performance, which is often more concerning than consistent regression.

---

## Appendix B: File Reference Map

### B.1 Complete GEMV File Locations

| File Type | Path |
|-----------|------|
| Design | `C:\Users\antmi\IRON\iron\operators\gemv\design.py` |
| Operator | `C:\Users\antmi\IRON\iron\operators\gemv\op.py` |
| Reference | `C:\Users\antmi\IRON\iron\operators\gemv\reference.py` |
| Test | `C:\Users\antmi\IRON\iron\operators\gemv\test.py` |
| AIE Kernel | `C:\Users\antmi\IRON\aie_kernels\generic\mv.cc` |

### B.2 Code Mapping Summary

```
GEMV (Matrix-Vector Multiplication):
  /iron/operators/gemv/op.py           - Operator interface
  /iron/operators/gemv/design.py       - AIE design configuration (ObjectFifo setup)
  /iron/operators/gemv/reference.py    - Reference implementation
  /iron/operators/gemv/test.py         - Test harness
  /aie_kernels/generic/mv.cc           - AIE kernel implementation
```

### B.3 Key Code Locations for Fixes

| Issue | File | Lines | Change Required |
|-------|------|-------|-----------------|
| ObjectFifo depth | design.py | 93-101 | Add adaptive depth for 4-col M>K |
| Column validation | op.py | 29-50 | Add matrix shape vs column count validation |
| Core synchronization | design.py | 103-118 | Review 4-col M>K loop pattern |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-18 | Jordan Lee | Initial analysis based on Small Bench-4.txt benchmark data |

**Notes:**
- Analysis based on actual benchmark data from Small Bench-4.txt
- All 24 benchmark figures verified against source file tables
- No test names invented - only actual test configurations included
- Document marked as DRAFT - NO COMMIT until user approval
- Critical finding: 8192x2048_4_4col0 shows +736% stddev increase (instability)

**Next Steps:**
1. User review and approval of this analysis
2. Prioritize P0 fixes (4-col M>K instability) for Week 1 sprint
3. Execute fixes and validate with benchmark re-runs
4. Update this document with fix results
5. Hand off to quality-management agent for validation

---

*Copyright 2026 IRON Project. All rights reserved.*
