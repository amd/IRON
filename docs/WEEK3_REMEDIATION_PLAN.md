# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

# Week 3 Generation Loop Remediation Plan

**Document Type:** Technical Remediation Plan
**Date:** 2026-03-16
**Author:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**Priority:** CRITICAL (P0)
**Status:** REMEDIATION REQUIRED

---

## Executive Summary

Week 3's generation loop implementation has **complete infrastructure** but a **non-functional forward pass**. The `_forward_layer()` method in `iron/generation/loop.py` (lines 313-344) returns input unchanged, blocking all integration testing and actual token generation.

**Decision:** NO-GO with remediation path. Week 4 planning is **PAUSED** until Week 3 remediation is complete.

---

## 1. Problem Analysis

### 1.1 Current State

| Component | Status | Notes |
|-----------|--------|-------|
| GenerationLoop structure | COMPLETE | Prefill/decode phases defined |
| TokenSampler | COMPLETE | Full sampling strategies (temp, top_p, top_k) |
| KVCacheManager | COMPLETE | Paged KV cache management |
| StopConditionChecker | COMPLETE | EOS, max_tokens, stop_strings |
| Operators (RMSNorm, MHA, SwiGLU) | COMPLETE | Exist in iron/operators/ |
| **_forward_layer()** | **PLACEHOLDER** | **Returns input unchanged - NO operator calls** |
| Integration Testing | BLOCKED | Cannot test without functional forward pass |

### 1.2 The Blocker

From `iron/generation/loop.py` lines 313-344:

```python
def _forward_layer(
    self,
    hidden: np.ndarray,
    layer_weights: Any,
    layer_idx: int,
    positions: List[int],
    is_prefill: bool
) -> np.ndarray:
    """Forward pass through a single transformer layer.
    ...
    """
    # This is a simplified implementation
    # A full implementation would include:
    # 1. Input RMSNorm
    # 2. Attention with KV cache
    # 3. Output projection
    # 4. Residual connection
    # 5. MLP with SwiGLU
    # 6. Final residual connection

    # For now, return hidden as placeholder
    # The actual forward pass would use the operators from iron/operators/
    return hidden  # <<< PLACEHOLDER - NO ACTUAL COMPUTATION
```

### 1.3 Impact Assessment

| Impact Area | Severity | Description |
|-------------|----------|-------------|
| Token Generation | CRITICAL | Cannot generate meaningful tokens |
| Integration Testing | CRITICAL | 161 tests cannot validate functionality |
| Week 4 Planning | HIGH | API integration blocked |
| Project Timeline | MEDIUM | Remediation required before proceeding |

---

## 2. Remediation Tasks

### 2.1 P0 Tasks (CRITICAL - Blocks All Functionality)

#### P0-1: Implement `_forward_layer()` with Actual Operator Calls

**Owner:** Runtime Team
**Effort:** 2-3 days
**Dependencies:** Operator implementations in iron/operators/

**Required Operators:**
1. **RMSNorm** - `iron/operators/rms_norm/op.py` (AIERMSNorm)
2. **Multi-Head Attention** - `iron/operators/mha/op.py` (AIEMHA)
3. **SwiGLU** - `iron/operators/swiglu_prefill/op.py` (AIESwiGLUPrefill)
4. **RoPE** - `iron/operators/rope/op.py` (for positional embeddings)

**Implementation Steps:**

```python
def _forward_layer(
    self,
    hidden: np.ndarray,
    layer_weights: Any,
    layer_idx: int,
    positions: List[int],
    is_prefill: bool
) -> np.ndarray:
    """Forward pass through a single transformer layer."""

    # Store input for residual connection
    residual = hidden

    # 1. Input RMSNorm
    hidden = self._rms_norm(hidden, layer_weights.input_norm)

    # 2. Self-Attention with KV cache
    attn_out = self._attention_layer(
        hidden,
        layer_weights.attn_weights,
        layer_idx,
        positions,
        is_prefill
    )

    # 3. Attention residual connection
    hidden = residual + attn_out

    # Store for MLP residual
    residual = hidden

    # 4. MLP RMSNorm
    hidden = self._rms_norm(hidden, layer_weights.mlp_norm)

    # 5. SwiGLU MLP
    hidden = self._swiglu_layer(hidden, layer_weights.mlp_weights)

    # 6. MLP residual connection
    hidden = residual + hidden

    return hidden
```

**Acceptance Criteria:**
- [ ] `_forward_layer()` calls actual operator implementations
- [ ] Prefill phase processes full prompt through all layers
- [ ] Decode phase processes single token with KV cache read/write
- [ ] Output logits produce meaningful token predictions
- [ ] Numerical accuracy verified against PyTorch reference

---

#### P0-2: Resolve `aie` Module Dependency for Testing

**Owner:** Runtime Team
**Effort:** 1 day
**Dependencies:** None

**Issue:** The `iron.common.__init__.py` imports `aie_base.py` which requires external AMD AIE hardware module.

**Solution Options:**

**Option A: Mock Module (Recommended for Testing)**
```python
# iron/common/aie_mock.py
class MockAIEModule:
    """Mock AIE module for testing without hardware."""
    pass

# In iron/common/__init__.py
try:
    import aie
except ImportError:
    from .aie_mock import MockAIEModule as aie
```

**Option B: Optional Import with Fallback**
```python
# iron/common/__init__.py
try:
    from aie import AIEOperatorBase
    HAS_AIE = True
except ImportError:
    HAS_AIE = False
    AIEOperatorBase = object  # Fallback base class
```

**Acceptance Criteria:**
- [ ] Tests can run without AMD NPU hardware
- [ ] Mock provides same interface as real module
- [ ] Real hardware path still works when available
- [ ] No test failures due to import errors

---

### 2.2 P1 Tasks (HIGH - Required for Production)

#### P1-1: Create End-to-End Integration Test

**Owner:** QA Team
**Effort:** 1-2 days
**Dependencies:** P0-1, P0-2 complete

**Test Scope:**
```python
def test_end_to_end_generation():
    """Test full generation loop from prompt to output."""
    config = Llama32Config()
    weights = load_test_weights()
    gen_config = GenerationConfig(
        temperature=0.7,
        max_new_tokens=50,
        eos_tokens=[128001]
    )

    loop = GenerationLoop(config, weights, gen_config)
    prompt_tokens = [1, 2, 3, ...]  # Tokenized prompt

    generated = []
    for result in loop.generate(prompt_tokens):
        generated.append(result.token_id)
        if result.is_eos:
            break

    # Assertions
    assert len(generated) > 0
    assert len(generated) <= gen_config.max_new_tokens
    assert all(0 <= t < config.vocab_size for t in generated)
```

**Acceptance Criteria:**
- [ ] Test generates 50+ coherent tokens
- [ ] EOS token properly detected and stops generation
- [ ] KV cache correctly maintains context
- [ ] Output is deterministic with greedy sampling
- [ ] Performance meets initial targets (TTFT, token/s)

---

## 3. Implementation Timeline

```
Day 1-2: P0-1 Implementation
├── Analyze existing operator implementations
├── Design _forward_layer() operator integration
├── Implement attention path (RMSNorm → Attention → Residual)
├── Implement MLP path (RMSNorm → SwiGLU → Residual)
└── Unit test individual components

Day 3: P0-2 Mock Module
├── Create aie_mock.py
├── Update iron/common/__init__.py for optional import
├── Verify tests can run without hardware
└── Document mock limitations

Day 4: P1-1 Integration Test
├── Create end-to-end test framework
├── Test with sample weights
├── Verify output coherence
└── Performance baseline measurement

Day 5: Validation & Cleanup
├── Run full test suite (161 tests)
├── Fix any integration issues
├── Update documentation
└── Quality review for re-submission
```

---

## 4. Quality Gates

### 4.1 Code Quality Requirements

| Metric | Target | Verification |
|--------|--------|--------------|
| Type Hints | 100% | Static analysis |
| Docstrings | >90% | Manual review |
| Error Handling | All paths | Exception coverage |
| Logging | Debug/Info levels | Log output review |

### 4.2 Test Requirements

| Test Category | Target | Status |
|---------------|--------|--------|
| Unit Tests | >90% coverage | 161 tests designed |
| Integration Tests | End-to-end flow | BLOCKED (P0-1) |
| Performance Tests | Baseline metrics | BLOCKED (P0-1) |

### 4.3 Acceptance Criteria

**Week 3 Remediation Complete When:**
- [ ] P0-1: `_forward_layer()` calls actual operators
- [ ] P0-2: Tests run without hardware dependency
- [ ] P1-1: End-to-end test generates 50+ tokens
- [ ] All 161 tests pass
- [ ] Quality Review: GO decision

---

## 5. Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Operator API mismatch | MEDIUM | HIGH | Review operator interfaces before integration |
| Numerical accuracy issues | MEDIUM | MEDIUM | Compare against PyTorch reference implementation |
| Performance below targets | LOW | MEDIUM | Optimize after functional; profile hot paths |
| KV cache integration bugs | MEDIUM | HIGH | Unit test KV read/write separately |

---

## 6. Strategic Impact

### 6.1 Before Remediation

```
Infrastructure: ████████████████████ 100% COMPLETE
Forward Pass:   ░░░░░░░░░░░░░░░░░░░░   0% FUNCTIONAL
Testing:        ░░░░░░░░░░░░░░░░░░░░   0% BLOCKED
```

### 6.2 After Remediation

```
Infrastructure: ████████████████████ 100% COMPLETE
Forward Pass:   ████████████████████ 100% FUNCTIONAL
Testing:        ████████████████████ 100% ENABLED
```

### 6.3 Project Timeline Impact

| Scenario | Week 3 | Week 4 | Week 5 |
|----------|--------|--------|--------|
| **With Remediation** | Fix forward pass | API Integration | Testing |
| **Without Remediation** | BLOCKED | BLOCKED | BLOCKED |

**Recommendation:** Complete remediation before Week 4 planning.

---

## 7. Files Requiring Changes

| File | Change Type | Lines | Priority |
|------|-------------|-------|----------|
| `iron/generation/loop.py` | Implement `_forward_layer()` | ~50 | P0 |
| `iron/generation/loop.py` | Add `_attention_layer()` method | ~40 | P0 |
| `iron/generation/loop.py` | Add `_swiglu_layer()` method | ~30 | P0 |
| `iron/common/aie_mock.py` | Create mock module | ~100 | P0 |
| `iron/common/__init__.py` | Optional import handling | ~20 | P0 |
| `iron/generation/test_loop.py` | Add integration test | ~50 | P1 |

---

## 8. Git Commit Plan

### 8.1 Week 3 Commit (With Caveat)

```bash
git add iron/generation/
git commit -m "feat: Phase 3 Week 3 generation infrastructure - STRUCTURE COMPLETE

WHAT:
- GenerationLoop with prefill/decode structure (Task #70)
- KVCacheManager for KV persistence (Task #71)
- StopConditionChecker for EOS handling (Task #72)
- 161 unit tests designed

CAVEAT:
- _forward_layer() is placeholder - returns input unchanged
- Integration testing blocked until forward pass implemented
- Quality review: NO-GO with remediation path

REMEDIATION REQUIRED:
- Implement _forward_layer() with RMSNorm, Attention, SwiGLU calls
- Resolve aie module dependency for testing
- Create end-to-end integration test

References:
- docs/WEEK3_REMEDIATION_PLAN.md (this document)
- quality_review_week3_report.md (NO-GO decision)"
```

### 8.2 Remediation Follow-up Commit

```bash
git add iron/generation/loop.py iron/common/
git commit -m "fix: Implement _forward_layer() with actual operator calls

- Add RMSNorm, Attention, SwiGLU integration in _forward_layer()
- Create aie_mock.py for testing without hardware
- Enable 161 unit tests to execute
- Add end-to-end integration test

Unblocks: Week 4 API integration
References: docs/WEEK3_REMEDIATION_PLAN.md"
```

---

## 9. Recommendation

### 9.1 Immediate Actions

1. **PAUSE Week 4 Planning** - Do not proceed with API integration until forward pass works
2. **Assign Runtime Team** - Focus on P0-1 implementation
3. **Daily Check-ins** - Monitor remediation progress
4. **Quality Review Hold** - Schedule re-review after remediation

### 9.2 Success Criteria

**Week 3 is COMPLETE when:**
- Generation loop produces coherent token sequences
- All 161 tests execute and pass
- End-to-end test validates full generation flow
- Quality Review issues GO decision

---

## 10. Approval

| Role | Name | Date | Status |
|------|------|------|--------|
| Technical Product Strategist | Dr. Sarah Kim | 2026-03-16 | APPROVED |
| Engineering Lead | [Pending] | [Pending] | [Pending] |
| Quality Reviewer | Taylor Kim | [Pending] | [Pending] |

---

*Copyright © 2026 IRON Project. All rights reserved.*
