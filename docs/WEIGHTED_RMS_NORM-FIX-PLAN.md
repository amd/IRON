# WEIGHTED_RMS_NORM Fix Plan

**Document Type:** Technical Fix Plan
**Priority:** P1-HIGH
**Date:** 2026-03-21
**Author:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead

---

## Executive Summary

This document outlines the fix plan for WEIGHTED_RMS_NORM benchmark regressions affecting 2 of 4 configurations. The root cause is an incomplete adaptive ObjectFifo depth formula that fails to account for edge cases in column/channel combinations.

---

## 1. Benchmark Analysis

### 1.1 Configuration Overview

WEIGHTED_RMS_NORM operates with 4 benchmark configurations varying in column count and channel configuration:

| Config ID | Columns | Channels | Weight Length | Status |
|-----------|---------|----------|---------------|--------|
| weighted_rms_norm_1_cols_2_channels_2048_weights_2048 | 1 | 2 | 2048 | **P1-HIGH REGRESSION** |
| weighted_rms_norm_2_cols_2_channels_2048_weights_1024 | 2 | 2 | 1024 | STABLE/IMPROVED |
| weighted_rms_norm_4_cols_2_channels_2048_weights_512 | 4 | 2 | 512 | STABLE/IMPROVED |
| weighted_rms_norm_8_cols_2_channels_2048_weights_256 | 8 | 2 | 256 | **P1-HIGH REGRESSION** |

### 1.2 Regression Details

#### Configuration 1: 1-Col, 2-Ch, 2048-weights
```
Metric          | Regression    | Impact
----------------|---------------|------------------
Bandwidth       | -22.59% to -31.19% | Severe performance degradation
Latency         | +45.30%       | Significant slowdown
```

**Root Issue:** FIFO depth=2 assigned, but depth=4 required for stable 2-channel operation with single column.

#### Configuration 4: 8-Col, 2-Ch, 256-weights
```
Metric          | Regression    | Impact
----------------|---------------|------------------
Latency StdDev  | +67.90%       | Performance instability/explosion
```

**Root Issue:** FIFO depth=4 assigned, but depth=5 required for high-parallelism 8-column configuration.

### 1.3 Stable Configurations

| Configuration | Current Depth | Performance |
|---------------|---------------|-------------|
| 2-col, 2-ch   | depth=2       | STABLE      |
| 4-col, 2-ch   | depth=3       | IMPROVED    |

---

## 2. Root Cause Analysis

### 2.1 Current Formula (INCOMPLETE)

Located in: `C:\Users\antmi\IRON\iron\operators\rms_norm\design_weighted.py` (lines 41-45)

```python
fifodepth = (
    4 if num_columns >= 8 else
    (3 if num_columns >= 4 and num_channels == 2 else
     (2 if num_channels == 2 or weight_length >= 1024 else 1))
)
```

### 2.2 Formula Breakdown

| Condition | Depth Assigned | Problem |
|-----------|----------------|---------|
| `num_columns >= 8` | 4 | Under-provisioned for 8-col/2-ch (needs 5) |
| `num_columns >= 4 and num_channels == 2` | 3 | Correct for 4-col |
| `num_channels == 2 or weight_length >= 1024` | 2 | **FAILS 1-col/2-ch** (needs 4) |
| Default | 1 | Baseline for single-channel, small weights |

### 2.3 Failure Modes

**1-Col/2-Channel Failure:**
- Single column must handle full 2-channel throughput
- Depth=2 creates backpressure, causing -22.59% to -31.19% bandwidth loss
- Required depth=4 to absorb 2-channel DMA bursts

**8-Column Failure:**
- 8 columns × 2 channels = 16 ShimDMA channels at saturation
- Depth=4 insufficient for concurrent channel arbitration
- Results in +67.90% latency stddev explosion
- Required depth=5 for stable high-parallelism operation

---

## 3. Proposed Fix

### 3.1 Enhanced FIFO Depth Formula

```python
fifodepth = (
    5 if num_columns >= 8 else
    (4 if num_channels == 2 and num_columns == 1 else
     (3 if num_columns >= 4 and num_channels == 2 else
      (2 if num_channels == 2 or weight_length >= 1024 else 1))))
```

### 3.2 Depth Assignment Matrix

| Columns | Channels | Current Depth | Proposed Depth | Change |
|---------|----------|---------------|----------------|--------|
| 1 | 2 | 2 | **4** | +2 (fix bandwidth) |
| 2 | 2 | 2 | 2 | No change (stable) |
| 4 | 2 | 3 | 3 | No change (stable) |
| 8 | 2 | 4 | **5** | +1 (fix stddev) |

### 3.3 Implementation Location

**File:** `C:\Users\antmi\IRON\iron\operators\rms_norm\design_weighted.py`
**Lines:** 36-45 (comment block + formula)

---

## 4. Expected Impact

### 4.1 Performance Recovery

| Configuration | Current | Expected Post-Fix | Improvement |
|---------------|---------|-------------------|-------------|
| 1-col, 2-ch | -31.19% BW | 0% to +5% BW | +31-36% |
| 1-col, 2-ch | +45.30% latency | 0% to +10% | -35-45% |
| 8-col, 2-ch | +67.90% stddev | <15% stddev | -53% |

### 4.2 Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Over-provisioning FIFO | Low | Memory usage | Depth increase is minimal (1-2 slots) |
| Other configs affected | Very Low | Regressions | 2-col and 4-col unchanged |
| ShimDMA channel limits | Low | Configuration errors | Already validated in op.py (line 52-53) |

### 4.3 Resource Impact

- **Memory:** +2 FIFO slots × 1-col config = negligible (tile_ty buffer)
- **8-col config:** +1 FIFO slot × 8 columns = minimal overhead
- **Trade-off:** Small memory increase for significant performance recovery

---

## 5. Implementation Plan

### 5.1 Code Changes

**Step 1:** Update `design_weighted.py` (lines 36-45)

```python
# P1-HIGH FIX: Enhanced adaptive ObjectFifo depth for WEIGHTED_RMS_NORM regressions
# Issue 1: -22.59% to -31.19% bandwidth (weighted_rms_norm_1_cols_2_channels_2048_weights_2048)
# Issue 2: +67.90% latency stddev (weighted_rms_norm_8_cols_2_channels_2048_weights_256)
# Source: weightrmsnorm.txt benchmark analysis
# Depth=5 for 8+ columns (high parallelism)
# Depth=4 for 1-column/2-channel (single column throughput)
# Depth=3 for 4+ columns with 2-channel
# Depth=2 for 2-channel or large tiles (>=1024)
# Depth=1 otherwise (baseline)
fifodepth = (
    5 if num_columns >= 8 else
    (4 if num_channels == 2 and num_columns == 1 else
     (3 if num_columns >= 4 and num_channels == 2 else
      (2 if num_channels == 2 or weight_length >= 1024 else 1)))
)
```

### 5.2 Validation Steps

1. **Unit Test:** Verify formula produces correct depth for all 4 configs
2. **Benchmark Run:** Execute full weighted_rms_norm benchmark suite
3. **Regression Check:** Confirm 2-col and 4-col remain stable
4. **Performance Validation:** Verify 1-col and 8-col regressions eliminated

### 5.3 Success Criteria

| Metric | Target | Pass Condition |
|--------|--------|----------------|
| 1-col bandwidth | > -5% | Recovery from -31.19% |
| 1-col latency | < +10% | Recovery from +45.30% |
| 8-col stddev | < 15% | Recovery from +67.90% |
| 2-col, 4-col | No change | Maintain stable/improved |

---

## 6. Verification Checklist

- [ ] Code change applied to `design_weighted.py`
- [ ] Unit test confirms depth values for all 4 configs
- [ ] Benchmark suite executed (100 iterations recommended)
- [ ] 1-col bandwidth regression eliminated (< -5%)
- [ ] 1-col latency regression eliminated (< +10%)
- [ ] 8-col stddev explosion resolved (< 15%)
- [ ] 2-col and 4-col remain stable
- [ ] Documentation updated in TASK-TRACKING-BENCHMARK-ANALYSIS.md

---

## 7. Related Files

| File | Purpose |
|------|---------|
| `iron/operators/rms_norm/design_weighted.py` | FIFO depth formula (PRIMARY FIX) |
| `iron/operators/rms_norm/op.py` | Operator runtime configuration |
| `iron/benchmarks/run.py` | Benchmark execution |
| `iron/benchmarks/results/validation_latest.md` | Results validation |
| `docs/TASK-TRACKING-BENCHMARK-ANALYSIS.md` | Tracking documentation |

---

## 8. Timeline Estimate

| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Implementation | 0.5 hour | None |
| Unit Testing | 0.5 hour | Implementation complete |
| Benchmark Validation | 2-3 hours | Test environment available |
| Documentation | 0.5 hour | Results validated |
| **Total** | **3.5-4.5 hours** | |

---

## Appendix A: Formula Derivation

### A.1 Depth Requirements Analysis

The ObjectFifo depth determines buffer slots for DMA<->AIE data flow:

- **Depth=1:** Minimum (single buffer, high contention)
- **Depth=2:** Basic 2-channel support
- **Depth=3:** 4+ column with 2-channel parallelism
- **Depth=4:** Single-column full throughput OR high column count
- **Depth=5:** Maximum parallelism (8-col × 2-ch = 16 channels)

### A.2 Decision Tree

```
num_columns >= 8?
  Yes -> depth=5 (max parallelism)
  No -> num_channels==2 AND num_columns==1?
    Yes -> depth=4 (single column, full throughput)
    No -> num_columns>=4 AND num_channels==2?
      Yes -> depth=3 (moderate parallelism)
      No -> num_channels==2 OR weight_length>=1024?
        Yes -> depth=2 (basic 2-channel or large tile)
        No -> depth=1 (baseline)
```

---

**Document Status:** READY FOR IMPLEMENTATION
**Approved By:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
