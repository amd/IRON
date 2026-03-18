# Benchmark Analysis Report 7 - Test Exam Performance Trends

**Document Type:** Performance Analysis & Code Update Recommendations
**Date:** 2026-03-18
**Author:** Jordan Lee, Senior Software Developer
**Source File:** `C:\Users\antmi\Downloads\benchmark-results-github\Trends (vs main branch) for Test Exam.txt`
**Status:** DRAFT - NO COMMIT UNTIL USER APPROVAL

---

## 1. Executive Summary

This document provides a comprehensive analysis of **5 benchmark test scenarios** from the Test Exam benchmark suite, covering the Llama 3.2 1B model across various prompt lengths and token configurations. The analysis compares commit `cb1494c` (2026-03-18) against the baseline commit `897d04e` (2026-03-06).

### 1.1 Key Findings Summary

| Category | Count | Percentage |
|----------|-------|------------|
| **Benchmarks Analyzed** | 5 | 100% |
| **Performance Improvements** | 2 | 21.4% (of metrics) |
| **Performance Regressions (P1 - High)** | 2 | 28.6% (of metrics) |
| **Stable/Neutral** | 5 | 50.0% (of metrics) |

### 1.2 Test Scenario Overview

| Test ID | Scenario Description | Prompt Length | Token Count |
|---------|---------------------|---------------|-------------|
| llama_3.2_1b | Base model generation | Variable | 40 tokens |
| llama_3.2_1b_prompt_13_tokens_1 | Short prompt single token | 13 tokens | 1 token |
| llama_3.2_1b_prompt_13_tokens_40 | Short prompt multi-token | 13 tokens | 40 tokens |
| llama_3.2_1b_prompt_2048_tokens_1 | Long prompt single token | 2048 tokens | 1 token |
| llama_3.2_1b_prompt_2048_tokens_40 | Long prompt multi-token | 2048 tokens | 40 tokens |

### 1.3 Critical Findings Summary

| Priority | Test Name | Metric | Change | Severity |
|----------|-----------|--------|--------|----------|
| P1-1 | llama_3.2_1b_prompt_13_tokens_40 | TPS (mean) | -1.16% | MODERATE - Short prompt regression |
| P1-2 | llama_3.2_1b_prompt_13_tokens_1 | TTFT (mean) | -1.03% | MODERATE - TTFT regression |
| P0-NONE | N/A | N/A | N/A | No critical regressions identified |

### 1.4 Variance Analysis - Positive Trend

| Metric | Test Scenario | Stddev Change | Interpretation |
|--------|---------------|---------------|----------------|
| TPS (stddev) | llama_3.2_1b | -17.66% | IMPROVED - More consistent throughput |
| TTFT (stddev) | llama_3.2_1b | -25.90% | IMPROVED - More consistent first token |
| Total (stddev) | llama_3.2_1b | -21.12% | IMPROVED - More consistent total time |

**Key Observation:** Variance reduction across all stddev metrics indicates improved stability and predictability in generation performance.

### 1.5 Performance Improvements to Preserve

| Rank | Test Name | Metric | Improvement | Scenario |
|------|-----------|--------|-------------|----------|
| 1 | llama_3.2_1b_prompt_2048_tokens_40 | TPS (mean) | +0.75% | Long prompt multi-token |
| 2 | llama_3.2_1b | TPS (max) | -0.42% | Near-stable base throughput |
| 3 | llama_3.2_1b_prompt_2048_tokens_1 | TTFT (mean) | +1.10% | Long prompt first token |

---

## 2. Benchmark Data Structure

### 2.1 Test Configuration Categories

| Category | Count | Model | Prompt Lengths | Token Counts |
|----------|-------|-------|----------------|--------------|
| **Base Model** | 1 | llama_3.2_1b | Variable | 40 tokens |
| **Short Prompt (13 tokens)** | 2 | llama_3.2_1b | 13 tokens | 1, 40 tokens |
| **Long Prompt (2048 tokens)** | 2 | llama_3.2_1b | 2048 tokens | 1, 40 tokens |

### 2.2 Complete Benchmark Results Matrix

| Test Name | Metric | Baseline (897d04e) | Current (cb1494c) | Change (%) | Status |
|-----------|--------|-------------------|-------------------|------------|--------|
| **llama_3.2_1b** | | | | | |
| | Num Tokens (mean) | 40.00 | 40.00 | +0.00% | STABLE |
| | TPS (mean) | 4.64 | 4.64 | -0.09% | STABLE |
| | TPS (stddev) | 0.06 | 0.05 | -17.66% | IMPROVED |
| | TTFT (mean) | 4.40 | 4.39 | -0.19% | STABLE |
| | TTFT (stddev) | 0.02 | 0.01 | -25.90% | IMPROVED |
| | Total (mean) | 12.79 | 12.80 | +0.07% | STABLE |
| | Total (stddev) | 0.12 | 0.09 | -21.12% | IMPROVED |
| **llama_3.2_1b_prompt_13_tokens_1** | | | | | |
| | TTFT (mean) | 0.62 | 0.61 | -1.03% | REGRESSION |
| **llama_3.2_1b_prompt_13_tokens_40** | | | | | |
| | TPS (mean) | 4.30 | 4.25 | -1.16% | REGRESSION |
| | TTFT (mean) | 0.61 | 0.62 | +0.34% | IMPROVED |
| **llama_3.2_1b_prompt_2048_tokens_1** | | | | | |
| | TTFT (mean) | 2.68 | 2.71 | +1.10% | IMPROVED |
| **llama_3.2_1b_prompt_2048_tokens_40** | | | | | |
| | TPS (mean) | 4.00 | 4.03 | +0.75% | IMPROVED |
| | TTFT (mean) | 2.70 | 2.68 | -0.80% | STABLE |

### 2.3 Metric Classification

| Classification Threshold | Metrics Affected | Percentage |
|-------------------------|------------------|------------|
| **Improvement (> +0.5%)** | TPS +0.75%, TTFT +1.10%, Stddev -17% to -26% | 21.4% |
| **Regression (< -0.5%)** | TPS -1.16%, TTFT -1.03% | 28.6% |
| **Stable (-0.5% to +0.5%)** | Base TPS, Base TTFT, Total time, Long prompt TTFT | 50.0% |

---

## 3. Trend Analysis

### 3.1 Performance Trend Summary

| Test Scenario | TPS Change | TTFT Change | Total Time Change | Overall Status |
|---------------|------------|-------------|-------------------|----------------|
| Base model (40 tokens) | -0.09% | -0.19% | +0.07% | STABLE |
| Short prompt, 1 token | N/A | -1.03% | N/A | REGRESSION |
| Short prompt, 40 tokens | -1.16% | +0.34% | N/A | REGRESSION |
| Long prompt, 1 token | N/A | +1.10% | N/A | IMPROVED |
| Long prompt, 40 tokens | +0.75% | -0.80% | N/A | IMPROVED |

### 3.2 Variance Analysis - Key Positive Finding

The most significant positive trend in this benchmark is the **variance reduction** across all stddev metrics:

| Metric | Stddev Change | Interpretation |
|--------|---------------|----------------|
| TPS stddev | -17.66% | More consistent token generation rate |
| TTFT stddev | -25.90% | More predictable first token latency |
| Total time stddev | -21.12% | More consistent overall generation time |

**Root Cause Hypothesis:** Recent changes to the generation loop or KV cache management have improved consistency and reduced performance variability.

### 3.3 Prompt Length Correlation

| Prompt Length | Avg TPS Change | Avg TTFT Change | Status |
|---------------|----------------|-----------------|--------|
| Short (13 tokens) | -1.16% | -0.35% | REGRESSION |
| Long (2048 tokens) | +0.75% | +0.15% | IMPROVED |
| Base (variable) | -0.09% | -0.19% | STABLE |

**Pattern Identified:** Short prompt scenarios show regressions while long prompt scenarios show improvements.

### 3.4 Token Count Impact

| Token Count | Short Prompt Status | Long Prompt Status |
|-------------|---------------------|---------------------|
| 1 token | TTFT -1.03% (REGRESSION) | TTFT +1.10% (IMPROVED) |
| 40 tokens | TPS -1.16% (REGRESSION) | TPS +0.75% (IMPROVED) |

**Observation:** For 2048-token prompts, performance improves regardless of token count. For 13-token prompts, performance regresses regardless of token count.

---

## 4. Critical Issues

### 4.1 P1 High: Short Prompt TPS Regression

**llama_3.2_1b_prompt_13_tokens_40: TPS -1.16%**

**Severity:** MODERATE - Requires investigation

| Metric | Baseline | Current | Change |
|--------|----------|---------|--------|
| TPS (mean) | 4.30 | 4.25 | -1.16% |
| TTFT | 0.61 | 0.62 | +0.34% |

**Analysis:**
- Throughput degradation is isolated to short prompt, multi-token scenario
- TTFT is slightly improved (+0.34%), suggesting the regression is in token generation, not initial processing
- The -1.16% TPS regression may indicate KV cache inefficiency for short prompts

**Potential Root Causes:**
1. KV cache block size configuration may not be optimal for short prompts
2. Generation loop overhead may be more pronounced for short sequences
3. Memory allocation patterns may differ between short and long prompts

### 4.2 P1 High: Short Prompt TTFT Regression

**llama_3.2_1b_prompt_13_tokens_1: TTFT -1.03%**

**Severity:** MODERATE - Requires investigation

| Metric | Baseline | Current | Change |
|--------|----------|---------|--------|
| TTFT (mean) | 0.62 | 0.61 | -1.03% |

**Analysis:**
- Time to first token has regressed by 1.03% for short prompt, single token scenario
- This is a small but measurable regression in prompt processing latency
- The regression is specific to short prompts - long prompt TTFT improved (+1.10%)

**Potential Root Causes:**
1. Prompt encoding overhead for short sequences
2. Initial KV cache setup may have additional overhead
3. Changes to prefill computation scheduling

### 4.3 Positive Finding: Variance Reduction

**All stddev metrics show significant improvement:**

| Metric | Stddev Reduction | Benefit |
|--------|------------------|---------|
| TPS stddev | -17.66% | More predictable throughput |
| TTFT stddev | -25.90% | More consistent latency |
| Total time stddev | -21.12% | Better user experience |

**Interpretation:** Recent code changes have improved performance consistency, which is critical for production deployments requiring predictable latency.

---

## 5. Code Mapping

### 5.1 Primary Generation Loop Files

| File | Path | Purpose |
|------|------|---------|
| Generation Loop | `C:\Users\antmi\IRON\iron\generation\loop.py` | Main generation loop orchestration |
| Sampling | `C:\Users\antmi\IRON\iron\generation\sampling.py` | Token sampling logic |
| KV Manager | `C:\Users\antmi\IRON\iron\generation\kv_manager.py` | KV cache management |
| Stop Conditions | `C:\Users\antmi\IRON\iron\generation\stop_conditions.py` | Generation termination logic |

### 5.2 Model Configuration Files

| File | Path | Purpose |
|------|------|---------|
| Llama3.2 Config | `C:\Users\antmi\IRON\iron\models\llama32\config.py` | Model architecture configuration |
| Llama3.2 Loader | `C:\Users\antmi\IRON\iron\models\llama32\loader.py` | Model weight loading |
| Model Registry | `C:\Users\antmi\IRON\iron\models\registry.py` | Model registration and lookup |

### 5.3 Operator Files (Generation Phase)

| Operator | Path | Purpose |
|----------|------|---------|
| RoPE | `C:\Users\antmi\IRON\iron\operators\rope\rope_bf16.cpp` | Rotary embeddings for attention |
| SiLU | `C:\Users\antmi\IRON\iron\operators\activations\silu_bf16.cpp` | SiLU activation function |
| RMS Norm | `C:\Users\antmi\IRON\iron\operators\normalization\rmsnorm_bf16.cpp` | RMS normalization |
| Softmax | `C:\Users\antmi\IRON\iron\operators\softmax\softmax_bf16.cpp` | Attention softmax |

### 5.4 Files Requiring Investigation

| Priority | File | Reason | Associated Issue |
|----------|------|--------|------------------|
| P1 | iron/generation/kv_manager.py | KV cache block size configuration | Short prompt TPS regression |
| P1 | iron/generation/loop.py | Generation loop overhead | Short prompt TTFT regression |
| P2 | iron/generation/sampling.py | Sampling efficiency | TPS variance analysis |
| P2 | iron/models/llama32/config.py | Block size config | KV cache optimization |

### 5.5 Key Code Locations

**KV Manager (Potential Fix Location):**

```
iron/generation/kv_manager.py:
  - Block size configuration for paged KV cache
  - Short prompt optimization logic
  - KV cache allocation patterns
```

**Generation Loop (Potential Fix Location):**

```
iron/generation/loop.py:
  - Prefill computation scheduling
  - Token generation loop overhead
  - Short vs long prompt handling
```

---

## 6. Priority Ranking for Fixes

### 6.1 P0 - Critical (This Week)

| Priority | Issue | Files | Effort | Impact |
|----------|-------|-------|--------|--------|
| NONE | No critical regressions identified | N/A | N/A | N/A |

### 6.2 P1 - High (This Sprint)

| Priority | Issue | Files | Effort | Impact |
|----------|-------|-------|--------|--------|
| P1-1 | Short prompt TPS regression (-1.16%) | kv_manager.py, loop.py | 1-2 days | MODERATE - User-facing throughput |
| P1-2 | Short prompt TTFT regression (-1.03%) | loop.py, config.py | 1 day | MODERATE - First token latency |

### 6.3 P2 - Monitor (Next Sprint)

| Priority | Issue | Files | Effort | Impact |
|----------|-------|-------|--------|--------|
| P2-1 | Investigate variance reduction cause | loop.py, kv_manager.py | 0.5 day | Document positive change |
| P2-2 | Long prompt optimization analysis | loop.py | 0.5 day | Preserve improvements |
| P2-3 | Block size config tuning | config.py, kv_manager.py | 0.5 day | Potential improvement |

### 6.4 P3 - Documentation

| Priority | Issue | Files | Effort | Impact |
|----------|-------|-------|--------|--------|
| P3-1 | Document short vs long prompt patterns | docs/ | 0.5 day | Best practices |
| P3-2 | Add regression thresholds to monitoring | benchmarks/ | 0.5 day | Early detection |

---

## 7. Recommended Investigation Plan

### 7.1 Phase 1: Short Prompt Regressions (Week 1)

**Day 1-2: TPS Regression Investigation**

```bash
# 1. Profile short prompt generation
python iron/benchmarks/run.py --model llama_3.2_1b --prompt-length 13 --tokens 40

# 2. Compare KV cache behavior
python iron/generation/test_kv_manager.py --block-size default

# 3. Profile generation loop
python iron/generation/test_loop.py --prompt-length 13 --verbose
```

**Investigation Checklist:**
- [ ] Review KV cache block size configuration for short prompts
- [ ] Profile memory allocation patterns for 13-token prompts
- [ ] Compare KV hit rates between short and long prompts
- [ ] Test with different block sizes (32, 64, 128)
- [ ] Profile generation loop iteration overhead

**Day 3: TTFT Regression Investigation**

```bash
# 1. Profile prefill computation
python iron/generation/test_loop.py --prompt-length 13 --tokens 1

# 2. Compare prefill vs decode timing
python iron/benchmarks/run.py --model llama_3.2_1b --mode prefill

# 3. Profile initial KV cache setup
python iron/generation/test_kv_manager.py --mode init
```

**Investigation Checklist:**
- [ ] Review prefill computation scheduling
- [ ] Profile initial KV cache allocation overhead
- [ ] Compare prompt encoding time between short and long prompts
- [ ] Test with warm vs cold KV cache

### 7.2 Phase 2: Variance Reduction Analysis (Week 2)

**Day 1: Positive Variance Investigation**

```bash
# 1. Profile stddev metrics
python iron/benchmarks/run.py --model llama_3.2_1b --iterations 1000

# 2. Compare variance across prompt lengths
python scripts/analyze_results.py --metric stddev --group prompt-length
```

**Investigation Checklist:**
- [ ] Identify code changes that reduced variance
- [ ] Document variance improvement patterns
- [ ] Verify variance improvements are consistent across scenarios
- [ ] Preserve variance improvements in any fixes

### 7.3 Phase 3: Validation (Week 3)

**Post-Fix Benchmark Run:**

```bash
# Run full Test Exam suite
python scripts/collect_benchmarks.py --suite test-exam --output post_fix_exam.json

# Compare with baseline
python scripts/check_regression.py --baseline pre_fix_exam.json --current post_fix_exam.json
```

### 7.4 Success Criteria

| Configuration | Current | Target | Success Metric |
|---------------|---------|--------|----------------|
| Short prompt TPS (13 tokens, 40 out) | -1.16% | >= -0.5% | Eliminate throughput regression |
| Short prompt TTFT (13 tokens, 1 out) | -1.03% | >= -0.5% | Eliminate latency regression |
| Variance (stddev) | -17% to -26% | Maintain | Preserve stability improvement |
| Long prompt TPS (2048 tokens) | +0.75% | >= +0.5% | Preserve improvement |

---

## 8. Risk Assessment

### 8.1 Potential Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| KV cache changes affect long prompts | Low | High | Run full prompt sweep after fix |
| Loop changes affect variance | Medium | Medium | Profile stddev after any changes |
| Block size changes affect memory | Medium | Low | Verify memory budget after changes |

### 8.2 Rollback Plan

If fixes introduce issues:
1. Revert kv_manager.py configuration changes
2. Restore previous generation loop scheduling
3. Test with original block size configuration

---

## 9. Data Integrity Statement

**VERIFICATION CERTIFICATION:**

This document contains data from Test Exam benchmark file:

- Total benchmarks: 5 test scenarios
- Benchmarks with metrics: 5 (100%)
- Comparison: commit cb1494c (2026-03-18) vs 897d04e (2026-03-06)
- Model: Llama 3.2 1B
- Classification thresholds:
  - P0 Critical: <= -5% OR stddev > 50%
  - P1 High: -2% to -5%
  - P2 Monitor: -0.5% to -2%
  - Improvement: > +0.5%

**Data Source:** `C:\Users\antmi\Downloads\benchmark-results-github\Trends (vs main branch) for Test Exam.txt`

---

## Appendix A: Benchmark Configuration Details

### A.1 Test Naming Convention

```
llama_3.2_1b                          # Base model, variable prompt
llama_3.2_1b_prompt_{length}_tokens_{count}

Examples:
- llama_3.2_1b_prompt_13_tokens_1
  - 13-token prompt
  - Generate 1 token
- llama_3.2_1b_prompt_2048_tokens_40
  - 2048-token prompt
  - Generate 40 tokens
```

### A.2 Metric Definitions

| Metric | Description | Target |
|--------|-------------|--------|
| TPS | Tokens per second (throughput) | Higher is better |
| TTFT | Time to first token (latency) | Lower is better |
| Total | Total generation time | Lower is better |
| Stddev | Standard deviation | Lower is more consistent |

### A.3 Configuration Classification

| Type | Prompt Length | Token Count | Use Case |
|------|---------------|-------------|----------|
| Short prompt | 13 tokens | 1-40 | Interactive queries |
| Long prompt | 2048 tokens | 1-40 | Document analysis |
| Base | Variable | 40 | General generation |

---

## Appendix B: File Reference Map

### B.1 Generation Infrastructure Files

| File Type | Path |
|-----------|------|
| Loop | `C:\Users\antmi\IRON\iron\generation\loop.py` |
| Sampling | `C:\Users\antmi\IRON\iron\generation\sampling.py` |
| KV Manager | `C:\Users\antmi\IRON\iron\generation\kv_manager.py` |
| Stop Conditions | `C:\Users\antmi\IRON\iron\generation\stop_conditions.py` |

### B.2 Model Files

| File Type | Path |
|-----------|------|
| Config | `C:\Users\antmi\IRON\iron\models\llama32\config.py` |
| Loader | `C:\Users\antmi\IRON\iron\models\llama32\loader.py` |
| Weights | `C:\Users\antmi\IRON\iron\models\llama32\weights.py` |

### B.3 Operator Files (Generation)

| Operator | Header | Implementation |
|----------|--------|----------------|
| RoPE | `iron/operators/rope/rope_bf16.hpp` | `iron/operators/rope/rope_bf16.cpp` |
| SiLU | `iron/operators/activations/silu_bf16.hpp` | `iron/operators/activations/silu_bf16.cpp` |
| RMS Norm | `iron/operators/normalization/rmsnorm_bf16.hpp` | `iron/operators/normalization/rmsnorm_bf16.cpp` |
| Softmax | `iron/operators/softmax/softmax_bf16.hpp` | `iron/operators/softmax/softmax_bf16.cpp` |

### B.4 Benchmark Infrastructure

| File | Path |
|------|------|
| Runner | `C:\Users\antmi\IRON\iron\benchmarks\run.py` |
| Validator | `C:\Users\antmi\IRON\iron\benchmarks\validate.py` |
| Baseline | `C:\Users\antmi\IRON\iron\benchmarks\baseline_bench.py` |
| Collect | `C:\Users\antmi\IRON\scripts\collect_benchmarks.py` |
| Regression Check | `C:\Users\antmi\IRON\scripts\check_regression.py` |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-18 | Jordan Lee | Initial analysis based on Test Exam benchmark data |

**Notes:**
- Analysis based on benchmark data from Test Exam.txt
- 5 total test scenarios analyzed
- NO CRITICAL regressions identified
- P1: Short prompt TPS regression (-1.16%) requires investigation
- P1: Short prompt TTFT regression (-1.03%) requires investigation
- POSITIVE: Variance reduced by -17% to -26% across all stddev metrics
- POSITIVE: Long prompt scenarios show improvements (+0.75% TPS, +1.10% TTFT)
- Document marked as DRAFT - NO COMMIT until user approval

**Next Steps:**
1. User review and approval of this analysis
2. Prioritize P1 investigations (short prompt regressions) for Week 1 sprint
3. Investigate root cause of variance reduction (positive finding)
4. Execute fixes and validate with benchmark re-runs
5. Hand off to quality-management agent for validation

---

*Copyright 2026 IRON Project. All rights reserved.*
