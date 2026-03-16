# Phase 3 Implementation Plan: End-to-End Llama3.2 Integration

**Document Type:** Implementation Roadmap (Revised)
**Date:** 2026-03-15
**Author:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**Version:** 2.0.0 (Revised with Quality Review Feedback)
**Status:** APPROVED FOR EXECUTION

---

## Executive Summary

This revised Phase 3 implementation plan addresses the **4 Critical + 5 High priority issues** identified by the quality reviewer (Taylor Kim, Review Report dated 2026-03-15). The original plan was superseded by architectural gaps in KV cache management, tokenizer handling, and generation infrastructure.

**Quality Review Status:** CONDITIONAL PASS

**Key Changes from Original Plan:**
1. **KV Cache:** Internal implementation required (no torchytpe dependency)
2. **KV Cache Persistence:** Design for context retention across tokens
3. **RoPE Angle Cache:** Pre-computed sinusoidal cache implementation
4. **Memory Budget Validation:** Hard limits and enforcement
5. **Tokenizer Robustness:** Proper fallback chain with validation
6. **Concurrent Load Protection:** Thread-safe model loading
7. **Streaming Generation:** Token-by-token efficient pipeline
8. **EOS Token Handling:** Explicit end-of-sequence detection
9. **Auto-Converter Retry:** Resilient model conversion with fallbacks

**Timeline:** 6 weeks (Weeks 1-6)
**Risk Level:** MEDIUM (mitigated by pre-implementation prerequisites)

---

## 1. Critical Issue Resolutions

### C-01: KV Cache External Dependency (torchtune)

**Issue:** Original design depended on torchytpe for KV cache management, creating external dependency and licensing concerns.

**Resolution:**
- Implement internal `PagedKVCache` class in C++
- Use block-based memory allocation (inspired by vLLM but original implementation)
- Support block sizes: 16, 32, 64 tokens
- API matches requirements without external dependencies

**Implementation:**
```cpp
// File: iron/runtime/cpp/include/iron/kv_cache.hpp
class PagedKVCache {
public:
    struct Config {
        size_t blockSize = 32;        // Tokens per block
        size_t maxBlocks = 1024;      // Max blocks per sequence
        size_t numLayers = 16;        // Llama3.2-1B layers
        size_t numHeads = 32;         // Attention heads
        size_t headDim = 64;          // Head dimension
    };

    // Allocate blocks for sequence
    std::vector<BlockId> allocateBlocks(size_t numBlocks);

    // Read/Write KV vectors
    void writeKey(size_t layer, size_t tokenPos, const float* key);
    void writeValue(size_t layer, size_t tokenPos, const float* value);
    void readKeyValue(size_t layer, size_t tokenPos, float* key, float* value);

private:
    struct Block {
        std::unique_ptr<float[]> keyCache;   // [numHeads, headDim]
        std::unique_ptr<float[]> valueCache; // [numHeads, headDim]
    };
    std::vector<Block> blocks_;
};
```

**Acceptance Criteria:**
- [ ] No torchytpe or PyTorch dependencies
- [ ] Unit tests for block allocation/deallocation
- [ ] Memory layout optimized for NPU access patterns

---

### C-02: Missing KV Cache Persistence Design

**Issue:** No design for retaining KV cache across token generation (required for autoregressive inference).

**Resolution:**
- Add `SequenceState` class to track KV blocks per sequence
- Implement cache serialization for long contexts
- Support pause/resume for multi-turn conversations

**Implementation:**
```cpp
// File: iron/runtime/cpp/include/iron/sequence_state.hpp
class SequenceState {
public:
    struct State {
        uint64_t sequenceId;
        size_t currentLength = 0;
        std::vector<BlockId> kvBlocks;  // Allocated KV blocks
        std::vector<float> promptEmbeddings; // For long prompt resumption
        bool isComplete = false;
    };

    // Start new sequence
    uint64_t startSequence(const std::vector<int32_t>& promptTokens);

    // Append generated token
    void appendToken(uint64_t sequenceId, int32_t tokenId);

    // Serialize state for persistence
    std::vector<uint8_t> serialize(uint64_t sequenceId) const;

    // Deserialize to resume
    static SequenceState deserialize(const std::vector<uint8_t>& data);

private:
    std::map<uint64_t, State> sequences_;
    std::mt19937 rng_;
};
```

**Acceptance Criteria:**
- [ ] Can persist/resume sequences up to 128K tokens
- [ ] Serialization size < 100MB for 32K context
- [ ] Resume latency < 50ms

---

### C-03: RoPE Angle Cache Not Implemented

**Issue:** RoPE requires pre-computed sin/cos tables; runtime computation is inefficient.

**Resolution:**
- Pre-compute RoPE angle cache at model load time
- Support multiple sequence lengths dynamically
- Cache stored in CPU memory, copied to NPU as needed

**Implementation:**
```cpp
// File: iron/operators/rope/rope_cache.hpp
class RoPECache {
public:
    struct Config {
        size_t maxSeqLen = 131072;  // Llama3.2 max context
        size_t headDim = 64;
        float theta = 10000.0f;     // RoPE theta
    };

    void initialize(const Config& config);

    // Get pre-computed sin/cos for sequence length
    const float* getCosTable(size_t seqLen) const;
    const float* getSinTable(size_t seqLen) const;

    // Get cache in NPU-accessible format
    const void* getDeviceBuffer() const { return deviceBuffer_.get(); }
    size_t getDeviceBufferSize() const { return deviceBufferSize_; }

private:
    std::vector<float> cosCache_;  // [maxSeqLen, headDim/2]
    std::vector<float> sinCache_;  // [maxSeqLen, headDim/2]
    std::unique_ptr<uint8_t[]> deviceBuffer_;
    size_t deviceBufferSize_ = 0;
};
```

**Acceptance Criteria:**
- [ ] Pre-computation completes in < 100ms
- [ ] Cache size < 64MB for max context
- [ ] Table lookup O(1) complexity

---

### C-04: No Memory Budget Validation

**Issue:** No hard limits on memory usage; risk of OOM on resource-constrained devices.

**Resolution:**
- Implement `MemoryBudget` class with hard limits
- Validate before model load, fail gracefully if exceeded
- Per-component budgets (weights, KV cache, activations)

**Implementation:**
```cpp
// File: iron/runtime/cpp/include/iron/memory_budget.hpp
class MemoryBudget {
public:
    struct Limits {
        size_t totalBudget = 4_GB;      // Total NPU+CPU budget
        size_t weightBudget = 2_GB;     // Model weights
        size_t kvCacheBudget = 1_GB;    // KV cache
        size_t activationBudget = 512_MB; // Temporary activations
        size_t headroom = 512_MB;       // Safety margin
    };

    // Validate before load
    bool validateModelLoad(const ModelSpec& spec) const;

    // Check before KV allocation
    bool canAllocateKV(size_t seqLen, size_t batchSize) const;

    // Get remaining budget
    size_t getRemainingBudget(Component component) const;

    // Enforce limits (throw if exceeded)
    void* allocateWithBudget(size_t size, Component component);

private:
    Limits limits_;
    std::atomic<size_t> usedWeights_{0};
    std::atomic<size_t> usedKVCache_{0};
    std::atomic<size_t> usedActivations_{0};
};
```

**Acceptance Criteria:**
- [ ] Model load fails gracefully if budget exceeded
- [ ] Clear error message with required vs. available memory
- [ ] Runtime enforcement with atomic counters

---

## 2. High Priority Issue Resolutions

### H-01: Tokenizer Fallback Inadequate

**Resolution:** Implement robust fallback chain with validation:
```
Primary: HuggingFace tokenizers (installed)
  ↓ (if unavailable)
Secondary: HuggingFace tokenizers (auto-install via pip)
  ↓ (if fails)
Tertiary: Local cached tokenizer.json
  ↓ (if fails)
Fallback: Character-level tokenizer (graceful degradation)
```

**Implementation:**
```python
# File: iron/api/tokenizers.py
class RobustTokenizer:
    FALLBACK_CHAIN = [
        HFTokenizerBackend,
        CachedTokenizerBackend,
        CharacterLevelBackend
    ]

    def __init__(self, modelPath):
        for backendClass in self.FALLBACK_CHAIN:
            try:
                self.backend = backendClass(modelPath)
                self.backend.validate()  # Ensure it works
                return
            except Exception as e:
                logging.warning(f"{backendClass.__name__} failed: {e}")
        raise TokenizerError("All tokenizer backends failed")
```

---

### H-02: No Concurrent Load Protection

**Resolution:** Add thread-safe model loading with queue:
```cpp
// File: iron/runtime/cpp/src/model_loader.cpp
class ThreadSafeModelLoader {
public:
    std::shared_ptr<LoadedModel> load(const std::string& path) {
        std::lock_guard<std::mutex> lock(queueMutex_);
        loadQueue_.push(path);

        // Process queue sequentially
        if (!processing_.load()) {
            processQueue();
        }

        return getLoadedModel(path);
    }

private:
    std::mutex queueMutex_;
    std::queue<std::string> loadQueue_;
    std::atomic<bool> processing_{false};
    std::map<std::string, std::shared_ptr<LoadedModel>> loadedModels_;
};
```

---

### H-03: Streaming Generation Inefficient

**Resolution:** Implement token-by-token pipeline with minimal latency:
```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│   Prompt    │ -> │  Prefill     │ -> │   Decode    │ -> │   Output    │
│ Tokenization│    │  (parallel)  │    │ (token-by-  │    │  Streaming  │
│             │    │              │    │  token)     │    │             │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
                          │                    │
                          v                    v
                   ┌──────────────┐    ┌─────────────┐
                   │  KV Cache    │    │  EOS Check  │
                   │  Population  │    │  & Yield    │
                   └──────────────┘    └─────────────┘
```

---

### H-04: Missing EOS Token Handling

**Resolution:** Explicit EOS detection with configurable tokens:
```python
# File: iron/api/generation_config.py
@dataclass
class GenerationConfig:
    """Configuration for text generation"""
    # Stopping criteria
    eos_tokens: List[int] = None  # Model-specific EOS token IDs
    max_new_tokens: int = 2048
    stop_strings: List[str] = None

    # Sampling
    temperature: float = 0.7
    top_p: float = 0.9
    top_k: int = 50

    def __post_init__(self):
        if self.eos_tokens is None:
            # Llama3.2 default EOS
            self.eos_tokens = [128001, 128009]
```

---

### H-05: Auto-Converter No Retry Logic

**Resolution:** Add exponential backoff retry for HuggingFace downloads:
```python
# File: iron/api/auto_converter.py
from tenacity import retry, stop_after_attempt, wait_exponential

class HuggingFaceConverter:
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def download_model(self, model_id: str) -> Path:
        """Download model with retry logic"""
        try:
            return hf_hub_download(repo_id=model_id, filename="model.safetensors")
        except Exception as e:
            # Cleanup partial downloads
            self._cleanup_partial_downloads()
            raise
```

---

## 3. Pre-Implementation Prerequisites

**Must complete before Phase 3 coding begins:**

| ID | Task | Owner | Effort | Status |
|----|------|-------|--------|--------|
| PR-01 | Implement internal `KVCache` class | Runtime Team | 2 days | TODO |
| PR-02 | Create `RoPECache` with precomputation | Runtime Team | 1 day | TODO |
| PR-03 | Add `GenerationConfig` class | API Team | 1 day | TODO |
| PR-04 | Implement `MemoryBudget` class | Runtime Team | 2 days | TODO |
| PR-05 | Add concurrent load protection | API Team | 1 day | TODO |

**Total Prerequisite Effort:** 7 days

---

## 4. Sprint Timeline (Weeks 1-6)

### Week 1: Foundation

| Task | Files | Deliverable |
|------|-------|-------------|
| KV Cache implementation | `iron/runtime/kv_cache.{hpp,cpp}` | Paged KV cache |
| RoPE Cache implementation | `iron/operators/rope/rope_cache.{hpp,cpp}` | Precomputed angles |
| Memory Budget implementation | `iron/runtime/memory_budget.{hpp,cpp}` | Validation |

**Week 1 Exit Criteria:**
- [ ] All critical infrastructure classes implemented
- [ ] Unit tests passing for new classes
- [ ] No external dependencies (torchtune removed)

### Week 2: Model Loader

| Task | Files | Deliverable |
|------|-------|-------------|
| Config adapter | `iron/models/llama32/config.py` | Config loading |
| Weight loader | `iron/models/llama32/loader.py` | HF weight loading |
| Model class | `iron/models/llama32/model.py` | Forward pass |

**Week 2 Exit Criteria:**
- [ ] Can load Llama3.2-1B from HuggingFace
- [ ] Forward pass produces valid output
- [ ] Memory validation working

### Week 3: Generation

| Task | Files | Deliverable |
|------|-------|-------------|
| Generation loop | `iron/api/generation.py` | Autoregressive |
| KV cache integration | `iron/runtime/sequence_state.{hpp,cpp}` | Context retention |
| EOS handling | `iron/api/generation_config.py` | Proper termination |

**Week 3 Exit Criteria:**
- [ ] Can generate 128+ coherent tokens
- [ ] KV cache persists across tokens
- [ ] EOS properly detected

### Week 4: API Integration

| Task | Files | Deliverable |
|------|-------|-------------|
| OpenAI endpoint | `iron/api/server.py` | `/v1/chat/completions` |
| Streaming support | `iron/api/server.py` | SSE streaming |
| Tokenizer enhancement | `iron/api/tokenizers.py` | Robust fallback |

**Week 4 Exit Criteria:**
- [ ] API returns valid completions
- [ ] Streaming works end-to-end
- [ ] Tokenizer handles all cases

### Week 5: Testing & Validation

| Task | Files | Deliverable |
|------|-------|-------------|
| Unit tests | `iron/api/test/`, `iron/runtime/test/` | Test coverage |
| Integration tests | `tests/integration/` | End-to-end tests |
| Load tests | `tests/load/` | Concurrent requests |

**Week 5 Exit Criteria:**
- [ ] Test coverage >90%
- [ ] All integration tests pass
- [ ] 24-hour stability test passes

### Week 6: Hardening & Documentation

| Task | Files | Deliverable |
|------|-------|-------------|
| Error handling | All files | Graceful failures |
| Documentation | `docs/USER_GUIDE.md` | User documentation |
| CI/CD integration | `.github/workflows/` | Automated testing |

**Week 6 Exit Criteria:**
- [ ] All quality gates met
- [ ] Documentation complete
- [ ] CI/CD pipeline green

---

## 5. Updated Task List for PROJECT_STATUS_TRACKER.md

### Phase 3 Tasks (NEW)

| Task ID | Subject | Description | Priority | Status |
|---------|---------|-------------|----------|--------|
| P3-00 | Pre-implementation prerequisites | Complete all Critical issue fixes | CRITICAL | TODO |
| P3-01 | KV Cache internal implementation | Remove torchytpe dependency | CRITICAL | TODO |
| P3-02 | RoPE Cache implementation | Precomputed angle tables | CRITICAL | TODO |
| P3-03 | Memory Budget implementation | Hard limits with validation | CRITICAL | TODO |
| P3-04 | Generation Config class | EOS handling, sampling params | HIGH | TODO |
| P3-05 | Concurrent load protection | Thread-safe model loading | HIGH | TODO |
| P3-06 | Model loader implementation | Load Llama3.2-1B from HF | CRITICAL | TODO |
| P3-07 | Tokenizer enhancement | Robust fallback chain | HIGH | TODO |
| P3-08 | Generation loop | Autoregressive generation | CRITICAL | TODO |
| P3-09 | KV cache persistence | Context retention across tokens | CRITICAL | TODO |
| P3-10 | Streaming optimization | Token-by-token pipeline | HIGH | TODO |
| P3-11 | OpenAI API endpoint | `/v1/chat/completions` | CRITICAL | TODO |
| P3-12 | Auto-converter retry | Resilient HF downloads | HIGH | TODO |
| P3-13 | Unit tests | Test coverage >90% | CRITICAL | TODO |
| P3-14 | Integration tests | End-to-end validation | CRITICAL | TODO |
| P3-15 | Documentation | User guide, API reference | HIGH | TODO |

### Task Status Updates

| Task ID | Current Status | New Status | Notes |
|---------|----------------|------------|-------|
| P2-06 (Benchmark Results) | IN PROGRESS | COMPLETE | CPU reference complete |
| P3-01 through P3-15 | N/A | TODO | New Phase 3 tasks |

---

## 6. Risk Mitigation Plan

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| **R1: NPU benchmarks unavailable** | HIGH | CRITICAL | Continue with CPU reference; plan Linux VM setup | DevOps |
| **R2: Memory limits exceeded** | MEDIUM | HIGH | MemoryBudget validation; graceful failures | Runtime |
| **R3: KV cache performance** | MEDIUM | MEDIUM | Paged attention; early profiling | Runtime |
| **R4: Tokenizer failures** | LOW | MEDIUM | Robust fallback chain | API |
| **R5: HF download failures** | MEDIUM | LOW | Retry logic with exponential backoff | API |
| **R6: Concurrent request issues** | MEDIUM | MEDIUM | Thread-safe loader with queue | API |

---

## 7. Quality Gates

### Before Merge to Main

- [ ] All CRITICAL issues resolved
- [ ] All HIGH issues resolved or documented as known issues
- [ ] Unit test coverage >90% for new code
- [ ] Integration test with end-to-end generation
- [ ] Memory leak test (24-hour stability)
- [ ] Concurrent request test (10 simultaneous requests)

### Phase 3 Exit Criteria

- [ ] End-to-end Llama3.2-1B inference working
- [ ] Can generate 128+ coherent tokens
- [ ] TTFT <200ms (initial target)
- [ ] OpenAI API endpoint functional
- [ ] All quality gates passed

---

## 8. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **TTFT (Time to First Token)** | <200ms | End-to-end measurement |
| **Token Generation Speed** | >10 tok/s | tokens/second average |
| **Memory Usage** | <2GB | Peak memory for Llama3.2-1B |
| **Context Length** | 128+ tokens | Max coherent generation |
| **Test Coverage** | >90% | Code coverage percentage |
| **API Compatibility** | 100% | OpenAI spec compliance |

---

## 9. Files to Create

### Week 1-2 (Foundation)

| File | Type | Description |
|------|------|-------------|
| `iron/runtime/cpp/include/iron/kv_cache.hpp` | Header | Paged KV cache interface |
| `iron/runtime/cpp/src/kv_cache.cpp` | Source | KV cache implementation |
| `iron/runtime/cpp/include/iron/sequence_state.hpp` | Header | Sequence state tracking |
| `iron/runtime/cpp/src/sequence_state.cpp` | Source | Sequence state implementation |
| `iron/runtime/cpp/include/iron/rope_cache.hpp` | Header | RoPE angle cache |
| `iron/runtime/cpp/src/rope_cache.cpp` | Source | RoPE cache implementation |
| `iron/runtime/cpp/include/iron/memory_budget.hpp` | Header | Memory budget validation |
| `iron/runtime/cpp/src/memory_budget.cpp` | Source | Memory budget implementation |

### Week 2-3 (Model)

| File | Type | Description |
|------|------|-------------|
| `iron/models/__init__.py` | Package | Model package init |
| `iron/models/base.py` | Source | Base model interface |
| `iron/models/llama32/__init__.py` | Package | Llama32 package init |
| `iron/models/llama32/config.py` | Source | Model configuration |
| `iron/models/llama32/loader.py` | Source | Weight loading |
| `iron/models/llama32/model.py` | Source | Model class |
| `iron/models/llama32/kv_cache.py` | Source | Python KV cache wrapper |
| `iron/models/registry.py` | Source | Model registry |

### Week 3-4 (API)

| File | Type | Description |
|------|------|-------------|
| `iron/api/generation_config.py` | Source | Generation configuration |
| `iron/api/generation.py` | Source | Generation loop |
| `iron/api/server.py` | Source | FastAPI server (enhanced) |
| `iron/api/tokenizers.py` | Source | Enhanced tokenizer |
| `iron/api/auto_converter.py` | Source | Model conversion with retry |

### Week 5 (Tests)

| File | Type | Description |
|------|------|-------------|
| `iron/api/test/test_server.py` | Test | Server endpoint tests |
| `iron/api/test/test_tokenizers.py` | Test | Tokenizer tests |
| `iron/api/test/test_generation.py` | Test | Generation tests |
| `iron/runtime/test/test_kv_cache.py` | Test | KV cache tests |
| `iron/runtime/test/test_memory_budget.py` | Test | Memory budget tests |

---

## 10. Dependencies

### Required (pyproject.toml)

| Dependency | Version | Purpose |
|------------|---------|---------|
| `safetensors` | >=0.3.0 | Weight loading |
| `huggingface_hub` | >=0.17.0 | Model download |
| `transformers` | >=4.30.0 | Tokenizer |
| `torch` | Latest CPU | Tensor operations |
| `numpy` | Latest | Array operations |
| `ml_dtypes` | Latest | bfloat16 support |
| `tenacity` | Latest | Retry logic |

### Optional

| Dependency | Version | Purpose |
|------------|---------|---------|
| `onnxruntime-genai` | Latest | Windows NPU backend |
| `pyxrt` | Latest | Linux NPU backend |

---

## 11. Summary

This revised Phase 3 implementation plan provides:

1. **Issue Resolution:** All 4 Critical + 5 High priority issues from quality review addressed
2. **Clean Architecture:** Internal implementations without external dependencies
3. **Production Ready:** Robust error handling, retry logic, concurrent safety
4. **Testable:** Clear unit test structure for quality validation
5. **Measurable:** Success metrics defined for performance validation

**Next Steps:**

1. Complete pre-implementation prerequisites (7 days effort)
2. Begin Week 1 implementation (KV cache, RoPE cache, memory budget)
3. Schedule weekly review checkpoints

---

**Prepared by:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**Date:** 2026-03-15
**Next Review:** Week 1 Implementation Review (scheduled for 2026-03-22)

*Copyright © 2026 IRON Project. All rights reserved.*
