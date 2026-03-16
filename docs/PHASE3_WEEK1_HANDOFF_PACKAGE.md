# Phase 3 Week 1 Implementation: Senior Developer Handoff Package

**Document Type:** Implementation Handoff Package
**Date:** 2026-03-15
**Prepared By:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**For:** Senior Developer - Week 1 Foundation Implementation

---

## 1. Executive Summary

### 1.1 Mission

Implement **5 foundational components** for Phase 3 Llama3.2 end-to-end inference support. These components form the critical infrastructure for autoregressive generation on AMD Ryzen AI NPUs.

### 1.2 Week 1 Tasks Overview

| # | Task ID | Component | Priority | Effort | Status |
|---|---------|-----------|----------|--------|--------|
| 1 | #63 | Internal KV Cache Infrastructure | CRITICAL | 2 days | READY |
| 2 | #64 | RoPE Cache Precomputation | CRITICAL | 1 day | READY |
| 3 | #65 | Memory Budget Validation | CRITICAL | 2 days | READY |
| 4 | #66 | Generation Configuration System | HIGH | 1 day | READY |
| 5 | #67 | Concurrent Model Load Protection | HIGH | 1 day | READY |

**Total Effort:** 7 developer-days

### 1.3 Key Documents

| Document | Purpose | Location |
|----------|---------|----------|
| Implementation Scope | Full specifications & acceptance criteria | `docs/PHASE3_WEEK1_IMPLEMENTATION_SCOPE.md` |
| Technical Templates | Code stubs & implementation templates | `docs/PHASE3_WEEK1_TECHNICAL_TEMPLATES.md` |
| Phase 3 Plan | Overall Phase 3 roadmap | `docs/PHASE3_IMPLEMENTATION_PLAN.md` |
| Status Tracker | Project-wide status | `docs/PROJECT_STATUS_TRACKER.md` |

---

## 2. Implementation Checklist

### 2.1 Pre-Implementation

Before starting coding:

- [ ] Read `PHASE3_WEEK1_IMPLEMENTATION_SCOPE.md` thoroughly
- [ ] Review `PHASE3_IMPLEMENTATION_PLAN.md` for context
- [ ] Understand existing runtime architecture in `iron/runtime/cpp/`
- [ ] Review existing headers in `iron/runtime/cpp/include/iron/runtime/`
- [ ] Set up development environment (CMake, C++17 compiler)

### 2.2 File Creation Checklist

Create the following files:

#### C++ Headers (5 files)

- [ ] `iron/runtime/cpp/include/iron/kv_cache.hpp`
- [ ] `iron/runtime/cpp/include/iron/sequence_state.hpp`
- [ ] `iron/runtime/cpp/include/iron/rope_cache.hpp`
- [ ] `iron/runtime/cpp/include/iron/memory_budget.hpp`
- [ ] `iron/runtime/cpp/include/iron/model_loader.hpp`

#### C++ Sources (5 files)

- [ ] `iron/runtime/cpp/src/kv_cache.cpp`
- [ ] `iron/runtime/cpp/src/sequence_state.cpp`
- [ ] `iron/runtime/cpp/src/rope_cache.cpp`
- [ ] `iron/runtime/cpp/src/memory_budget.cpp`
- [ ] `iron/runtime/cpp/src/model_loader.cpp`

#### Python Files (1 file)

- [ ] `iron/api/generation_config.py`

#### Build Configuration

- [ ] Update `iron/runtime/cpp/CMakeLists.txt` with new sources
- [ ] Update `iron/runtime/cpp/include/iron/CMakeLists.txt` with new headers

### 2.3 Implementation Order

Recommended implementation sequence:

```
Day 1-2: Task #65 - Memory Budget
         └── No dependencies
         └── Provides allocation validation for other components

Day 2-3: Task #64 - RoPE Cache
         └── No dependencies
         └── Standalone component

Day 3-4: Task #63 - KV Cache
         └── Uses Memory Budget for validation
         └── Most complex component

Day 5:   Task #63 (cont.) - Sequence State
         └── Depends on KV Cache

Day 5:   Task #66 - Generation Config
         └── Python-only, independent

Day 6-7: Task #67 - Concurrent Load Protection
         └── Uses Memory Budget validation
         └── Thread-safe model loading
```

---

## 3. Technical Specifications Summary

### 3.1 Task #63: Internal KV Cache

**Purpose:** Block-based KV cache management for autoregressive generation

**Key Design Decisions:**
- Pure C++ implementation (no PyTorch/torchtune dependency)
- Paged allocation (inspired by vLLM, original implementation)
- Configurable block sizes: 16, 32, 64 tokens
- Thread-safe operations

**Files:**
- `iron/runtime/cpp/include/iron/kv_cache.hpp`
- `iron/runtime/cpp/src/kv_cache.cpp`
- `iron/runtime/cpp/include/iron/sequence_state.hpp`
- `iron/runtime/cpp/src/sequence_state.cpp`

**Acceptance Criteria:**
- [ ] No torchytpe/PyTorch dependencies
- [ ] Block allocation/deallocation works correctly
- [ ] KV read/write preserves data integrity
- [ ] Thread-safe concurrent access verified
- [ ] Memory usage tracked accurately
- [ ] Supports Llama3.2-1B config (16 layers, 32 heads, 64 dim)

---

### 3.2 Task #64: RoPE Cache

**Purpose:** Pre-computed RoPE angle tables for O(1) lookup during inference

**Key Design Decisions:**
- Pre-compute at model load time
- Support up to 131K sequence length
- Contiguous device buffer for DMA transfer
- Initialization time <100ms

**Files:**
- `iron/runtime/cpp/include/iron/rope_cache.hpp`
- `iron/runtime/cpp/src/rope_cache.cpp`

**Acceptance Criteria:**
- [ ] Pre-computation completes <100ms
- [ ] Cache size <64MB for 128K context
- [ ] Table lookup returns correct values
- [ ] Device buffer is contiguous
- [ ] Works with existing `rope_bf16.cpp` operator

---

### 3.3 Task #65: Memory Budget

**Purpose:** Hard memory limits with validation to prevent OOM conditions

**Key Design Decisions:**
- Per-component budgets (weights, KV cache, activations, misc)
- Pre-allocation validation
- Atomic tracking for thread safety
- Graceful failures with clear error messages

**Files:**
- `iron/runtime/cpp/include/iron/memory_budget.hpp`
- `iron/runtime/cpp/src/memory_budget.cpp`

**Acceptance Criteria:**
- [ ] Model load validation works (oversized model fails gracefully)
- [ ] KV allocation check accurate at boundary conditions
- [ ] Atomic counters thread-safe under stress
- [ ] Clear error messages with required vs. available
- [ ] Budget tracking accurate after allocate/free cycles

---

### 3.4 Task #66: Generation Config

**Purpose:** Configurable generation parameters with model-specific defaults

**Key Design Decisions:**
- Dataclass-based Python implementation
- Llama3.2-specific EOS token defaults
- JSON serialization for API integration
- Parameter validation

**Files:**
- `iron/api/generation_config.py`

**Acceptance Criteria:**
- [ ] All sampling parameters supported (temp, top_p, top_k)
- [ ] EOS detection works correctly
- [ ] Stop string detection works
- [ ] JSON serialization/deserialization works
- [ ] Parameter validation catches invalid inputs

---

### 3.5 Task #67: Concurrent Load Protection

**Purpose:** Thread-safe model loading with request queuing

**Key Design Decisions:**
- Sequential loading (one model at a time)
- Request queue for concurrent requests
- Duplicate detection (prevent loading same model twice)
- Reference counting for usage tracking

**Files:**
- `iron/runtime/cpp/include/iron/model_loader.hpp`
- `iron/runtime/cpp/src/model_loader.cpp`

**Acceptance Criteria:**
- [ ] Concurrent loads are serialized (no race conditions)
- [ ] Duplicate loads detected and cached result returned
- [ ] Reference counting works (increment/decrement)
- [ ] Queue processing is fair (FIFO ordering)
- [ ] Memory budget is validated before loading

---

## 4. Code Templates

### 4.1 Using the Templates

`PHASE3_WEEK1_TECHNICAL_TEMPLATES.md` provides:

- **Complete header stubs** with doxygen comments
- **Implementation skeletons** with key methods outlined
- **Unit test templates** for each component
- **Build configuration snippets** for CMake integration

### 4.2 Template Adaptation

The templates are starting points. Adapt as needed:

1. **Review existing code style** in `iron/runtime/cpp/include/iron/runtime/`
2. **Match naming conventions** used in the codebase
3. **Integrate with existing types** (e.g., `npu_runtime.hpp` interfaces)
4. **Add platform-specific handling** if needed for Windows NPU

---

## 5. Testing Requirements

### 5.1 Unit Tests

Create unit tests in `iron/runtime/test/`:

| Component | Test File | Key Tests |
|-----------|-----------|-----------|
| PagedKVCache | `test_kv_cache.cpp` | Allocate/free, read/write, concurrent access |
| SequenceState | `test_sequence_state.cpp` | Start/complete/remove sequences |
| RoPECache | `test_rope_cache.cpp` | Pre-computation, lookup, device buffer |
| MemoryBudget | `test_memory_budget.cpp` | Validation, allocation, budget tracking |
| ModelLoader | `test_model_loader.cpp` | Concurrent loads, reference counting |
| GenerationConfig | `test_generation_config.py` | Parameters, EOS detection, serialization |

### 5.2 Integration Tests

After unit tests pass:

| Test | Components | Purpose |
|------|------------|---------|
| KV + Memory Budget | PagedKVCache, MemoryBudget | Validate KV allocation respects budget |
| RoPE + Model | RoPECache, model forward | Validate RoPE angles work with model |
| Generation Loop | All components | End-to-end token generation |

### 5.3 Test Execution

```bash
# Build tests
cd iron/runtime/cpp/build
cmake .. -DBUILD_TESTING=ON
make -j

# Run unit tests
ctest --output-on-failure

# Run Python tests
cd iron/api
python -m pytest test_generation_config.py -v
```

---

## 6. Quality Gates

### 6.1 Code Quality

| Gate | Requirement | Verification |
|------|-------------|--------------|
| Compiles without warnings | `-Wall -Wextra -Werror` | Build output |
| No memory leaks | Valgrind/sanitizers clean | `valgrind --leak-check=full` |
| Thread safety verified | No data races in stress tests | ThreadSanitizer |
| Documentation complete | Doxygen comments for all public APIs | `doxygen` |

### 6.2 Test Coverage

| Metric | Target | Verification |
|--------|--------|--------------|
| Line coverage | >90% | `gcov` / `lcov` |
| Branch coverage | >85% | `gcov` / `lcov` |
| All acceptance criteria | 100% verified | Manual checklist |

### 6.3 Performance

| Component | Metric | Target | Verification |
|-----------|--------|--------|--------------|
| KV cache | Block allocation time | <1ms per block | Profile |
| RoPE cache | Initialization time | <100ms | Profile |
| Memory budget | Validation overhead | <10ms per check | Profile |

---

## 7. Integration Points

### 7.1 With Existing Runtime

```
iron/runtime/cpp/include/iron/runtime/
├── npu_runtime.hpp       # Base runtime interface
├── onnxruntime_genai.hpp # ONNX backend (Task #52-53)
└── xdna_runtime.hpp      # xDNA backend (future)

Week 1 additions:
├── kv_cache.hpp          # Task #63
├── rope_cache.hpp        # Task #64
├── memory_budget.hpp     # Task #65
└── model_loader.hpp      # Task #67
```

### 7.2 With Python API

```
iron/api/
├── generation_config.py  # Task #66
├── generation.py         # Future: Generation loop (Week 3)
└── server.py             # Future: OpenAI endpoint (Week 4)
```

### 7.3 With Operators

```
iron/operators/
├── rope/
│   ├── rope_bf16.cpp     # Existing RoPE kernel
│   └── op.py             # Python interface
└── ...                   # Other operators

Week 1 RoPE cache feeds into rope_bf16.cpp operator
```

---

## 8. Risk Mitigation

### 8.1 Known Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| R1: KV cache memory layout inefficient | Medium | Medium | Profile early, iterate on design |
| R2: RoPE pre-computation too slow | Low | Medium | Optimize angle computation loop |
| R3: Memory budget too restrictive | Medium | High | Provide configuration override |
| R4: Thread-safe loader causes deadlocks | Low | High | Extensive stress testing |
| R5: Generation config missing parameters | Low | Low | Design for extensibility |

### 8.2 Escalation Path

If you encounter blockers:

1. **Technical questions:** Review `PHASE3_WEEK1_IMPLEMENTATION_SCOPE.md`
2. **Design clarifications:** Consult with Dr. Sarah Kim
3. **Code review:** Schedule review with Quality Reviewer
4. **Integration issues:** Check existing runtime code patterns

---

## 9. Deliverables

### 9.1 Required Deliverables

| # | Deliverable | Format | Location |
|---|-------------|--------|----------|
| 1 | KV Cache implementation | C++ source + header | `iron/runtime/cpp/` |
| 2 | Sequence State implementation | C++ source + header | `iron/runtime/cpp/` |
| 3 | RoPE Cache implementation | C++ source + header | `iron/runtime/cpp/` |
| 4 | Memory Budget implementation | C++ source + header | `iron/runtime/cpp/` |
| 5 | Model Loader implementation | C++ source + header | `iron/runtime/cpp/` |
| 6 | Generation Config implementation | Python source | `iron/api/` |
| 7 | Unit tests | C++/Python tests | `iron/runtime/test/`, `iron/api/test/` |
| 8 | Build configuration updates | CMakeLists.txt | `iron/runtime/cpp/` |

### 9.2 Optional Deliverables

| # | Deliverable | Format | Notes |
|---|-------------|--------|-------|
| 9 | Integration tests | C++/Python tests | If time permits |
| 10 | Performance benchmarks | Benchmark scripts | If time permits |
| 11 | API documentation | Doxygen output | Auto-generated |

---

## 10. Acceptance Process

### 10.1 Self-Verification

Before submitting for review:

- [ ] All files compile without warnings
- [ ] All unit tests pass
- [ ] Code coverage meets targets (>90% line, >85% branch)
- [ ] No memory leaks (sanitizer clean)
- [ ] No thread safety issues (ThreadSanitizer clean)
- [ ] All acceptance criteria verified

### 10.2 Code Review

Submit for review:

1. Create pull request to `devel` branch
2. Request review from:
   - Dr. Sarah Kim (Technical specifications)
   - Quality Reviewer (Code quality)
3. Address review comments
4. Re-run tests after changes

### 10.3 Merge Criteria

- [ ] All review comments addressed
- [ ] CI/CD pipeline passes
- [ ] Test coverage verified
- [ ] Documentation complete

---

## 11. Post-Week 1: Next Steps

Upon successful completion of Week 1:

### Week 2: Model Loader
- Implement Llama3.2 model loading from HuggingFace
- Config adapter for model hyperparameters
- Weight loader with memory mapping

### Week 3: Generation Loop
- Implement autoregressive generation
- KV cache integration for context retention
- EOS handling and stop conditions

### Week 4: API Integration
- OpenAI-compatible `/v1/chat/completions` endpoint
- Streaming support (SSE)
- Tokenizer enhancement

### Week 5: Testing
- Comprehensive unit tests
- Integration tests
- Load tests (concurrent requests)

### Week 6: Hardening
- Error handling improvements
- Documentation completion
- CI/CD integration

---

## 12. Quick Reference

### 12.1 Command Summary

```bash
# Build C++ runtime
cd iron/runtime/cpp
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j

# Run C++ tests
ctest --output-on-failure

# Run Python tests
cd iron/api
python -m pytest test_generation_config.py -v

# Check memory leaks
valgrind --leak-check=full ./test_runner

# Check thread safety
TSAN_OPTIONS="halt_on_error=1" ./test_runner
```

### 12.2 Key Types

```cpp
// KV Cache
iron::runtime::PagedKVCache
iron::runtime::PagedKVCache::Config
iron::runtime::SequenceState

// RoPE Cache
iron::runtime::RoPECache
iron::runtime::RoPECache::Config

// Memory Budget
iron::runtime::MemoryBudget
iron::runtime::MemoryBudget::Component
iron::runtime::MemoryBudget::Limits

// Model Loader
iron::runtime::ThreadSafeModelLoader
iron::runtime::ThreadSafeModelLoader::LoadedModel
```

### 12.3 Key Functions

```cpp
// KV Cache
cache.allocateBlocks(numBlocks)
cache.writeKey(layer, blockId, tokenOffset, head, key)
cache.readValue(layer, blockId, tokenOffset, head, value)

// RoPE Cache
ropeCache.getCosTable(seqLen)
ropeCache.getSinTable(seqLen)
ropeCache.getDeviceBuffer()

// Memory Budget
budget.validateModelLoad(weights, kv, activations)
budget.allocateWithBudget(size, component)
budget.canAllocateKV(...)

// Generation Config (Python)
config.is_eos_token(token_id)
config.should_stop(token_id, length, text)
config.to_json()
```

---

## 13. Contact Information

| Role | Name | Responsibility |
|------|------|----------------|
| Technical Product Strategist | Dr. Sarah Kim | Specifications, requirements, design |
| Senior Developer | You | Implementation, testing |
| Quality Reviewer | TBD | Code review, acceptance verification |

---

## 14. Document History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-03-15 | Initial creation | Dr. Sarah Kim |

---

**Handoff Package Prepared By:**

Dr. Sarah Kim
Technical Product Strategist & Engineering Lead
Date: 2026-03-15

---

*Copyright © 2026 IRON Project. All rights reserved.*
