# Phase 3 Week 1 Implementation Scope: Foundation Components

**Document Type:** Technical Implementation Specification
**Date:** 2026-03-15
**Author:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**Version:** 1.0.0
**Status:** READY FOR EXECUTION

---

## 1. Executive Summary

### 1.1 Purpose

This document defines the implementation scope for **Phase 3 Week 1: Foundation Components**. These components form the critical infrastructure required for Llama3.2 end-to-end inference on AMD Ryzen AI NPUs.

### 1.2 Week 1 Goals

Implement five foundational components that enable:
- Efficient KV cache management for autoregressive generation
- Pre-computed RoPE angle tables for fast inference
- Memory budget validation to prevent OOM conditions
- Configurable generation parameters
- Thread-safe model loading for concurrent requests

### 1.3 Success Criteria

| Criterion | Measurement | Target |
|-----------|-------------|--------|
| **KV Cache** | No torchytpe dependencies | 100% internal implementation |
| **RoPE Cache** | Pre-computation time | <100ms for 128K context |
| **Memory Budget** | Validation accuracy | 100% of allocations checked |
| **Generation Config** | Parameter coverage | All sampling parameters supported |
| **Concurrent Load** | Thread safety | No race conditions in testing |

---

## 2. Task Overview

### 2.1 Week 1 Task List

| Task ID | Subject | Priority | Effort | Dependencies |
|---------|---------|----------|--------|--------------|
| **#63** | Implement internal KV Cache infrastructure | CRITICAL | 2 days | None |
| **#64** | Implement RoPE Cache precomputation | CRITICAL | 1 day | None |
| **#65** | Implement Memory Budget validation | CRITICAL | 2 days | None |
| **#66** | Create Generation Configuration system | HIGH | 1 day | None |
| **#67** | Add concurrent model load protection | HIGH | 1 day | Task #65 |

**Total Effort:** 7 developer-days

### 2.2 Implementation Order

```
Day 1-2: Memory Budget (Task #65)
         └── No dependencies, provides allocation validation

Day 2-3: RoPE Cache (Task #64)
         └── No dependencies, standalone component

Day 3-4: KV Cache (Task #63)
         └── Uses Memory Budget for validation

Day 5:   Sequence State (part of Task #63)
         └── Depends on KV Cache

Day 5:   Generation Config (Task #66)
         └── Python-only, independent

Day 6-7: Concurrent Load Protection (Task #67)
         └── Uses Memory Budget validation
```

---

## 3. Technical Specifications

### 3.1 Task #63: Internal KV Cache Infrastructure

#### 3.1.1 Problem Statement

**Original Design Issue:** Phase 3 plan initially proposed using `torchtune` for KV cache management, creating:
- External PyTorch dependency
- Licensing concerns
- Limited control over memory layout
- No paged attention support

**Resolution:** Implement internal `PagedKVCache` class inspired by vLLM architecture but with original implementation.

#### 3.1.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **No External Dependencies** | Pure C++ implementation | CRITICAL |
| **Paged Allocation** | Block-based memory management | CRITICAL |
| **Configurable Block Size** | Support 16, 32, 64 token blocks | HIGH |
| **Multi-Layer Support** | Handle all transformer layers | CRITICAL |
| **Multi-Head Support** | Handle all attention heads | CRITICAL |
| **Thread-Safe** | Safe concurrent access | HIGH |
| **Memory Efficient** | Minimal fragmentation | MEDIUM |

#### 3.1.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/runtime/cpp/include/iron/kv_cache.hpp` | Header | Paged KV cache interface |
| `iron/runtime/cpp/src/kv_cache.cpp` | Source | KV cache implementation |
| `iron/runtime/cpp/include/iron/sequence_state.hpp` | Header | Sequence state tracking |
| `iron/runtime/cpp/src/sequence_state.cpp` | Source | Sequence state implementation |

#### 3.1.4 Class Specifications

**PagedKVCache Class:**

```cpp
// File: iron/runtime/cpp/include/iron/kv_cache.hpp
#pragma once

#include <vector>
#include <memory>
#include <mutex>
#include <cstdint>
#include <optional>

namespace iron {
namespace runtime {

/**
 * @brief Paged KV Cache for efficient autoregressive inference
 *
 * Implements block-based KV cache management inspired by vLLM.
 * Memory is allocated in fixed-size blocks to reduce fragmentation
 * and enable efficient memory reuse across sequences.
 */
class PagedKVCache {
public:
    /**
     * @brief Configuration for KV cache
     */
    struct Config {
        size_t blockSize = 32;        // Tokens per block
        size_t maxBlocks = 1024;      // Max blocks per sequence
        size_t numLayers = 16;        // Llama3.2-1B layers
        size_t numHeads = 32;         // Attention heads (GQA groups)
        size_t headDim = 64;          // Head dimension
        size_t maxSequences = 16;     // Max concurrent sequences

        // Derived values (computed)
        size_t bytesPerBlock() const;
        size_t totalBytes() const;
    };

    /**
     * @brief Block identifier type
     */
    using BlockId = uint32_t;

    /**
     * @brief Sequence identifier type
     */
    using SequenceId = uint64_t;

    /**
     * @brief Construct KV cache with configuration
     * @param config Cache configuration
     * @throws std::bad_alloc if memory allocation fails
     */
    explicit PagedKVCache(const Config& config);

    ~PagedKVCache();

    // Prevent copying (large object)
    PagedKVCache(const PagedKVCache&) = delete;
    PagedKVCache& operator=(const PagedKVCache&) = delete;

    // Allow moving
    PagedKVCache(PagedKVCache&& other) noexcept;
    PagedKVCache& operator=(PagedKVCache&& other) noexcept;

    /**
     * @brief Allocate blocks for a new sequence
     * @param numBlocks Number of blocks to allocate
     * @return Vector of allocated block IDs, or empty if insufficient memory
     */
    std::vector<BlockId> allocateBlocks(size_t numBlocks);

    /**
     * @brief Free blocks for a sequence
     * @param blocks Block IDs to free
     */
    void freeBlocks(const std::vector<BlockId>& blocks);

    /**
     * @brief Write key vector to cache
     * @param layer Layer index
     * @param blockId Block containing the token
     * @param tokenOffset Offset within block (0 to blockSize-1)
     * @param head Head index
     * @param key Key vector data [headDim]
     */
    void writeKey(
        size_t layer,
        BlockId blockId,
        size_t tokenOffset,
        size_t head,
        const float* key);

    /**
     * @brief Write value vector to cache
     * @param layer Layer index
     * @param blockId Block containing the token
     * @param tokenOffset Offset within block
     * @param head Head index
     * @param value Value vector data [headDim]
     */
    void writeValue(
        size_t layer,
        BlockId blockId,
        size_t tokenOffset,
        size_t head,
        const float* value);

    /**
     * @brief Read key and value vectors from cache
     * @param layer Layer index
     * @param blockId Block containing the token
     * @param tokenOffset Offset within block
     * @param head Head index
     * @param key Output key vector [headDim]
     * @param value Output value vector [headDim]
     */
    void readKeyValue(
        size_t layer,
        BlockId blockId,
        size_t tokenOffset,
        size_t head,
        float* key,
        float* value) const;

    /**
     * @brief Get contiguous memory for attention computation
     * @param layer Layer index
     * @param startBlock First block to read
     * @param numBlocks Number of blocks to read
     * @param head Head index
     * @param outKeys Output buffer [numBlocks * blockSize * headDim]
     * @param outValues Output buffer [numBlocks * blockSize * headDim]
     */
    void getContiguousBlocks(
        size_t layer,
        BlockId startBlock,
        size_t numBlocks,
        size_t head,
        float* outKeys,
        float* outValues) const;

    /**
     * @brief Get number of available blocks
     * @return Number of free blocks
     */
    size_t getAvailableBlocks() const;

    /**
     * @brief Get total number of blocks
     * @return Total block count
     */
    size_t getTotalBlocks() const;

    /**
     * @brief Check if cache can accommodate additional tokens
     * @param requiredBlocks Number of blocks needed
     * @return true if allocation would succeed
     */
    bool canAllocate(size_t requiredBlocks) const;

    /**
     * @brief Get memory usage in bytes
     * @return Total memory allocated
     */
    size_t getMemoryUsage() const;

private:
    /**
     * @brief Internal block structure
     */
    struct Block {
        // Key cache: [numHeads, blockSize, headDim]
        std::unique_ptr<float[]> keyCache;
        // Value cache: [numHeads, blockSize, headDim]
        std::unique_ptr<float[]> valueCache;
        bool inUse = false;

        Block(size_t numHeads, size_t blockSize, size_t headDim)
            : keyCache(std::make_unique<float[]>(numHeads * blockSize * headDim)),
              valueCache(std::make_unique<float[]>(numHeads * blockSize * headDim)) {}
    };

    Config config_;
    std::vector<Block> blocks_;
    mutable std::mutex mutex_;
    std::atomic<size_t> allocatedBlocks_{0};

    // Helper methods
    BlockId allocateBlockInternal();
    void freeBlockInternal(BlockId blockId);
    size_t getBlockOffset(BlockId blockId, size_t tokenOffset, size_t head) const;
};

} // namespace runtime
} // namespace iron
```

**SequenceState Class:**

```cpp
// File: iron/runtime/cpp/include/iron/sequence_state.hpp
#pragma once

#include <iron/kv_cache.hpp>
#include <vector>
#include <map>
#include <mutex>
#include <cstdint>
#include <random>

namespace iron {
namespace runtime {

/**
 * @brief Tracks state for an autoregressive generation sequence
 */
class SequenceState {
public:
    /**
     * @brief Sequence state information
     */
    struct State {
        uint64_t sequenceId;
        size_t currentLength = 0;          // Current sequence length
        size_t promptLength = 0;           // Original prompt length
        std::vector<PagedKVCache::BlockId> kvBlocks;  // Allocated KV blocks
        std::vector<int32_t> generatedTokens;         // Generated token IDs
        bool isComplete = false;           // Generation finished
        std::string stopReason;            // Why generation stopped

        // For long-context resumption
        std::vector<float> cachedPromptEmbeddings;  // Optional: cache embeddings
    };

    /**
     * @brief Construct sequence state manager
     * @param kvCache Reference to shared KV cache
     */
    explicit SequenceState(std::shared_ptr<PagedKVCache> kvCache);

    ~SequenceState();

    /**
     * @brief Start a new sequence
     * @param promptTokens Input prompt token IDs
     * @param maxNewTokens Maximum tokens to generate
     * @return Sequence ID for tracking
     */
    uint64_t startSequence(
        const std::vector<int32_t>& promptTokens,
        size_t maxNewTokens);

    /**
     * @brief Append a generated token to sequence
     * @param sequenceId Sequence to update
     * @param tokenId Generated token ID
     */
    void appendToken(uint64_t sequenceId, int32_t tokenId);

    /**
     * @brief Mark sequence as complete
     * @param sequenceId Sequence to complete
     * @param reason Stop reason (eos, max_length, stop_string)
     */
    void completeSequence(uint64_t sequenceId, const std::string& reason);

    /**
     * @brief Get current sequence state
     * @param sequenceId Sequence to query
     * @return Current state (throws if not found)
     */
    State getState(uint64_t sequenceId) const;

    /**
     * @brief Check if sequence exists
     * @param sequenceId Sequence to check
     * @return true if sequence is active
     */
    bool hasSequence(uint64_t sequenceId) const;

    /**
     * @brief Remove sequence and free resources
     * @param sequenceId Sequence to remove
     */
    void removeSequence(uint64_t sequenceId);

    /**
     * @brief Get all active sequence IDs
     * @return Vector of active sequence IDs
     */
    std::vector<uint64_t> getActiveSequences() const;

    /**
     * @brief Get number of tokens to generate next
     * @param sequenceId Sequence to query
     * @return Current length for next token computation
     */
    size_t getNextTokenPosition(uint64_t sequenceId) const;

    /**
     * @brief Serialize sequence state for persistence
     * @param sequenceId Sequence to serialize
     * @return Serialized data
     */
    std::vector<uint8_t> serialize(uint64_t sequenceId) const;

    /**
     * @brief Deserialize sequence state
     * @param data Serialized data
     * @param kvCache KV cache for restoration
     * @return Restored SequenceState
     */
    static SequenceState deserialize(
        const std::vector<uint8_t>& data,
        std::shared_ptr<PagedKVCache> kvCache);

private:
    std::shared_ptr<PagedKVCache> kvCache_;
    std::map<uint64_t, State> sequences_;
    mutable std::mutex mutex_;
    std::mt19937_64 rng_;
    std::atomic<uint64_t> nextSequenceId_{1};

    uint64_t generateSequenceId();
};

} // namespace runtime
} // namespace iron
```

#### 3.1.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-63.1 | No torchytpe/PyTorch dependencies | Code review, dependency scan |
| AC-63.2 | Block allocation works correctly | Unit test: allocate/free cycles |
| AC-63.3 | KV read/write preserves data | Unit test: write then read |
| AC-63.4 | Thread-safe concurrent access | Stress test with multiple threads |
| AC-63.5 | Memory usage tracked accurately | Unit test: verify getMemoryUsage() |
| AC-63.6 | Can handle Llama3.2-1B config | Integration test: 16 layers, 32 heads |

---

### 3.2 Task #64: RoPE Cache Precomputation

#### 3.2.1 Problem Statement

RoPE (Rotary Positional Embedding) requires sinusoidal angle tables for computation. Runtime computation of sin/cos for every token is inefficient. Pre-computation at model load time provides O(1) table lookup.

#### 3.2.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **Pre-computation** | Compute sin/cos tables at load time | CRITICAL |
| **O(1) Lookup** | Constant-time table access | CRITICAL |
| **Max Context Support** | Support up to 131K tokens (Llama3.2) | HIGH |
| **Memory Efficient** | Cache size <64MB for max context | MEDIUM |
| **NPU-Accessible Format** | Contiguous memory for DMA transfer | HIGH |

#### 3.2.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/runtime/cpp/include/iron/rope_cache.hpp` | Header | RoPE angle cache interface |
| `iron/runtime/cpp/src/rope_cache.cpp` | Source | RoPE cache implementation |

#### 3.2.4 Class Specifications

**RoPECache Class:**

```cpp
// File: iron/runtime/cpp/include/iron/rope_cache.hpp
#pragma once

#include <vector>
#include <memory>
#include <cstdint>

namespace iron {
namespace runtime {

/**
 * @brief Pre-computed RoPE angle cache for fast inference
 *
 * Stores sin/cos angle tables pre-computed at model load time.
 * Supports multiple sequence lengths and head dimensions.
 */
class RoPECache {
public:
    /**
     * @brief Configuration for RoPE cache
     */
    struct Config {
        size_t maxSeqLen = 131072;   // Llama3.2 max context (128K)
        size_t headDim = 64;         // Head dimension
        float theta = 10000.0f;      // RoPE theta parameter

        // Derived: cache size = maxSeqLen * (headDim/2) * 2 (sin+cos)
        size_t cacheSize() const {
            return maxSeqLen * (headDim / 2) * 2;  // sin + cos
        }
    };

    /**
     * @brief Construct and initialize RoPE cache
     * @param config Cache configuration
     */
    explicit RoPECache(const Config& config = Config());

    ~RoPECache();

    /**
     * @brief Get pre-computed cos table for sequence length
     * @param seqLen Sequence length (must be <= maxSeqLen)
     * @return Pointer to cos values [seqLen, headDim/2]
     */
    const float* getCosTable(size_t seqLen) const;

    /**
     * @brief Get pre-computed sin table for sequence length
     * @param seqLen Sequence length (must be <= maxSeqLen)
     * @return Pointer to sin values [seqLen, headDim/2]
     */
    const float* getSinTable(size_t seqLen) const;

    /**
     * @brief Get combined cache in NPU-accessible format
     * @return Pointer to interleaved [cos, sin] buffer
     */
    const void* getDeviceBuffer() const;

    /**
     * @brief Get device buffer size in bytes
     * @return Size in bytes
     */
    size_t getDeviceBufferSize() const;

    /**
     * @brief Get configuration
     * @return Current configuration
     */
    const Config& getConfig() const { return config_; }

    /**
     * @brief Check if cache is initialized
     * @return true if initialization complete
     */
    bool isInitialized() const { return initialized_; }

    /**
     * @brief Get pre-computation time (for profiling)
     * @return Initialization time in milliseconds
     */
    double getInitializationTimeMs() const { return initializationTimeMs_; }

private:
    Config config_;
    std::vector<float> cosCache_;  // [maxSeqLen, headDim/2]
    std::vector<float> sinCache_;  // [maxSeqLen, headDim/2]
    std::unique_ptr<uint8_t[]> deviceBuffer_;  // Interleaved for NPU
    size_t deviceBufferSize_ = 0;
    bool initialized_ = false;
    double initializationTimeMs_ = 0.0;

    void initialize();
    void computeAngles();
    float getInverseFrequency(size_t i, size_t headDim, float theta) const;
};

} // namespace runtime
} // namespace iron
```

#### 3.2.5 Implementation Notes

**Pre-computation Formula:**
```cpp
// For position p and dimension i:
// angle = p * inverse_freq[i]
// cos[p, i] = cos(angle)
// sin[p, i] = sin(angle)
// where inverse_freq[i] = 1 / (theta ^ (2*i/headDim))
```

**Memory Layout:**
```
cosCache_: [pos0_dim0, pos0_dim1, ..., pos0_dimN,
            pos1_dim0, pos1_dim1, ..., pos1_dimN,
            ...]

deviceBuffer_: [cos_data..., sin_data...]  // Contiguous for DMA
```

#### 3.2.6 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-64.1 | Pre-computation completes <100ms | Profile initialization |
| AC-64.2 | Cache size <64MB for 128K context | Verify getDeviceBufferSize() |
| AC-64.3 | Table lookup returns correct values | Unit test: spot-check angles |
| AC-64.4 | Device buffer is contiguous | Memory layout verification |
| AC-64.5 | Works with RoPE operator | Integration test with rope_bf16.cpp |

---

### 3.3 Task #65: Memory Budget Validation

#### 3.3.1 Problem Statement

Without hard memory limits, the system risks OOM (Out of Memory) conditions on resource-constrained devices. Need to validate memory requirements before allocation and fail gracefully.

#### 3.3.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **Hard Limits** | Enforce maximum memory per component | CRITICAL |
| **Pre-Allocation Validation** | Check before every allocation | CRITICAL |
| **Per-Component Budgets** | Separate budgets for weights, KV, activations | HIGH |
| **Atomic Tracking** | Thread-safe usage counters | HIGH |
| **Graceful Failures** | Clear error messages with required vs available | HIGH |

#### 3.3.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/runtime/cpp/include/iron/memory_budget.hpp` | Header | Memory budget interface |
| `iron/runtime/cpp/src/memory_budget.cpp` | Source | Memory budget implementation |

#### 3.3.4 Class Specifications

**MemoryBudget Class:**

```cpp
// File: iron/runtime/cpp/include/iron/memory_budget.hpp
#pragma once

#include <string>
#include <atomic>
#include <cstdint>
#include <optional>

namespace iron {
namespace runtime {

/**
 * @brief Memory budget enforcement and validation
 *
 * Tracks memory usage across components and enforces hard limits
 * to prevent OOM conditions on resource-constrained devices.
 */
class MemoryBudget {
public:
    /**
     * @brief Component types for budget tracking
     */
    enum class Component {
        WEIGHTS,      // Model weights
        KV_CACHE,     // KV cache for attention
        ACTIVATIONS,  // Temporary activations
        MISC          // Miscellaneous allocations
    };

    /**
     * @brief Memory limits configuration
     */
    struct Limits {
        size_t totalBudget = 4ULL * 1024 * 1024 * 1024;    // 4 GB total
        size_t weightBudget = 2ULL * 1024 * 1024 * 1024;   // 2 GB weights
        size_t kvCacheBudget = 1ULL * 1024 * 1024 * 1024;  // 1 GB KV cache
        size_t activationBudget = 512ULL * 1024 * 1024;    // 512 MB activations
        size_t headroom = 512ULL * 1024 * 1024;            // 512 MB safety

        // Validation
        bool isValid() const {
            return weightBudget + kvCacheBudget + activationBudget + headroom <= totalBudget;
        }
    };

    /**
     * @brief Memory allocation result
     */
    struct AllocationResult {
        bool success;
        std::string errorMessage;
        size_t requestedSize;
        size_t availableSize;
    };

    /**
     * @brief Construct memory budget with limits
     * @param limits Memory limits (uses defaults if not provided)
     */
    explicit MemoryBudget(const Limits& limits = Limits());

    ~MemoryBudget() = default;

    /**
     * @brief Validate memory before model load
     * @param requiredWeights Memory needed for weights
     * @param requiredKV Memory needed for KV cache (max context)
     * @param requiredActivations Memory needed for activations
     * @return AllocationResult with success/failure
     */
    AllocationResult validateModelLoad(
        size_t requiredWeights,
        size_t requiredKV,
        size_t requiredActivations) const;

    /**
     * @brief Check if KV allocation is possible
     * @param sequenceLength Sequence length
     * @param batchSize Batch size
     * @param numLayers Number of transformer layers
     * @param numHeads Number of attention heads
     * @param headDim Head dimension
     * @param blockSize KV cache block size
     * @return true if allocation would succeed
     */
    bool canAllocateKV(
        size_t sequenceLength,
        size_t batchSize,
        size_t numLayers,
        size_t numHeads,
        size_t headDim,
        size_t blockSize) const;

    /**
     * @brief Get remaining budget for component
     * @param component Component to query
     * @return Available bytes
     */
    size_t getRemainingBudget(Component component) const;

    /**
     * @brief Get current usage for component
     * @param component Component to query
     * @return Used bytes
     */
    size_t getCurrentUsage(Component component) const;

    /**
     * @brief Allocate memory with budget enforcement
     * @param size Bytes to allocate
     * @param component Component requesting allocation
     * @return Pointer to allocated memory, or nullptr if budget exceeded
     */
    void* allocateWithBudget(size_t size, Component component);

    /**
     * @brief Free memory and update budget
     * @param ptr Pointer to free
     * @param size Size of allocation
     * @param component Component that allocated
     */
    void freeWithBudget(void* ptr, size_t size, Component component);

    /**
     * @brief Reserve budget for upcoming allocation
     * @param size Bytes to reserve
     * @param component Component reserving
     * @return true if reservation succeeded
     */
    bool reserveBudget(size_t size, Component component);

    /**
     * @brief Release reserved budget
     * @param size Bytes to release
     * @param component Component releasing
     */
    void releaseBudget(size_t size, Component component);

    /**
     * @brief Get total memory usage
     * @return Sum of all component usage
     */
    size_t getTotalUsage() const;

    /**
     * @brief Get total budget
     * @return Total configured budget
     */
    size_t getTotalBudget() const { return limits_.totalBudget; }

    /**
     * @brief Get budget utilization percentage
     * @return Percentage (0-100)
     */
    double getUtilizationPercentage() const;

    /**
     * @brief Reset all usage counters (for testing)
     */
    void reset();

private:
    Limits limits_;
    std::atomic<size_t> usedWeights_{0};
    std::atomic<size_t> usedKVCache_{0};
    std::atomic<size_t> usedActivations_{0};
    std::atomic<size_t> usedMisc_{0};

    size_t getBudgetForComponent(Component component) const;
    size_t getUsageForComponent(Component component) const;
    void addUsage(Component component, size_t size);
    void removeUsage(Component component, size_t size);
};

// Helper function to calculate KV cache memory requirements
inline size_t calculateKVCacheMemory(
    size_t sequenceLength,
    size_t batchSize,
    size_t numLayers,
    size_t numHeads,
    size_t headDim,
    size_t blockSize = 32) {

    // Round up to block size
    size_t blocksPerSequence = (sequenceLength + blockSize - 1) / blockSize;
    size_t totalBlocks = blocksPerSequence * batchSize;

    // 2 (key + value) * numLayers * numHeads * blockSize * headDim * sizeof(float)
    size_t bytesPerBlock = 2 * numLayers * numHeads * blockSize * headDim * sizeof(float);

    return totalBlocks * bytesPerBlock;
}

} // namespace runtime
} // namespace iron
```

#### 3.3.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-65.1 | Model load validation works | Unit test: validate oversized model fails |
| AC-65.2 | KV allocation check accurate | Unit test: boundary conditions |
| AC-65.3 | Atomic counters thread-safe | Stress test with concurrent allocations |
| AC-65.4 | Clear error messages | Verify errorMessage content |
| AC-65.5 | Budget tracking accurate | Unit test: allocate/free cycles |

---

### 3.4 Task #66: Generation Configuration System

#### 3.4.1 Problem Statement

Generation parameters (temperature, top_p, max_tokens, EOS tokens) need to be configurable per-request with sensible defaults for Llama3.2.

#### 3.4.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **Sampling Parameters** | Temperature, top_p, top_k | CRITICAL |
| **Stopping Criteria** | EOS tokens, max_length, stop_strings | CRITICAL |
| **Model-Specific Defaults** | Llama3.2 EOS token IDs | HIGH |
| **Validation** | Parameter range checking | MEDIUM |
| **JSON Serialization** | API request/response support | HIGH |

#### 3.4.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/api/generation_config.py` | Source | Generation configuration (Python) |

#### 3.4.4 Class Specifications

**GenerationConfig Class:**

```python
# File: iron/api/generation_config.py
"""Generation configuration for autoregressive inference."""

from dataclasses import dataclass, field
from typing import List, Optional
import json


@dataclass
class GenerationConfig:
    """Configuration for text generation.

    Attributes:
        # Stopping criteria
        eos_tokens: List of EOS token IDs (model-specific)
        max_new_tokens: Maximum tokens to generate
        max_length: Maximum total sequence length
        stop_strings: Strings that trigger stopping

        # Sampling parameters
        temperature: Sampling temperature (0.0 = greedy)
        top_p: Nucleus sampling threshold
        top_k: Top-k sampling
        repetition_penalty: Penalty for repetition (>1.0 discourages)

        # Performance
        use_cache: Use KV cache for generation
        pad_token_id: Padding token ID
    """

    # Stopping criteria
    eos_tokens: List[int] = None
    max_new_tokens: int = 2048
    max_length: Optional[int] = None
    stop_strings: List[str] = None

    # Sampling parameters
    temperature: float = 0.7
    top_p: float = 0.9
    top_k: int = 50
    repetition_penalty: float = 1.0

    # Performance
    use_cache: bool = True
    pad_token_id: int = 128001  # Llama3.2 default

    # Model-specific configuration
    model_type: str = "llama3"

    def __post_init__(self):
        """Initialize defaults and validate."""
        # Set model-specific EOS tokens
        if self.eos_tokens is None:
            if self.model_type == "llama3":
                # Llama3.2 EOS: 128001 (<|end_of_text|>), 128009 (<|eot_id|>)
                self.eos_tokens = [128001, 128009]
            else:
                self.eos_tokens = [128001]

        # Validate parameters
        self._validate()

    def _validate(self):
        """Validate configuration parameters."""
        if self.temperature < 0:
            raise ValueError("temperature must be >= 0")
        if self.top_p < 0 or self.top_p > 1:
            raise ValueError("top_p must be in [0, 1]")
        if self.top_k < 1:
            raise ValueError("top_k must be >= 1")
        if self.repetition_penalty < 0:
            raise ValueError("repetition_penalty must be >= 0")
        if self.max_new_tokens < 1:
            raise ValueError("max_new_tokens must be >= 1")

    def is_eos_token(self, token_id: int) -> bool:
        """Check if token is an EOS token."""
        return token_id in self.eos_tokens

    def should_stop(
        self,
        token_id: int,
        current_length: int,
        generated_text: str = ""
    ) -> tuple[bool, str]:
        """Check if generation should stop.

        Returns:
            Tuple of (should_stop, reason)
        """
        # Check EOS tokens
        if self.is_eos_token(token_id):
            return True, "eos_token"

        # Check max length
        if current_length >= self.max_length:
            return True, "max_length"

        # Check stop strings
        if self.stop_strings:
            for stop_str in self.stop_strings:
                if stop_str in generated_text:
                    return True, "stop_string"

        return False, ""

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "eos_tokens": self.eos_tokens,
            "max_new_tokens": self.max_new_tokens,
            "max_length": self.max_length,
            "stop_strings": self.stop_strings,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "repetition_penalty": self.repetition_penalty,
            "use_cache": self.use_cache,
            "pad_token_id": self.pad_token_id,
            "model_type": self.model_type,
        }

    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, data: dict) -> "GenerationConfig":
        """Create from dictionary."""
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> "GenerationConfig":
        """Create from JSON string."""
        return cls.from_dict(json.loads(json_str))


# Preset configurations for common models
LLAMA3_CONFIG = GenerationConfig(
    model_type="llama3",
    eos_tokens=[128001, 128009],
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    max_new_tokens=2048,
)

LLAMA3_GREEDY_CONFIG = GenerationConfig(
    model_type="llama3",
    eos_tokens=[128001, 128009],
    temperature=0.0,  # Greedy decoding
    max_new_tokens=2048,
)
```

#### 3.4.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-66.1 | All sampling parameters supported | Unit test: parameter coverage |
| AC-66.2 | EOS detection works | Unit test: is_eos_token() |
| AC-66.3 | Stop string detection works | Unit test: should_stop() |
| AC-66.4 | JSON serialization works | Unit test: to_json/from_json |
| AC-66.5 | Parameter validation works | Unit test: invalid parameters |

---

### 3.5 Task #67: Concurrent Model Load Protection

#### 3.5.1 Problem Statement

Multiple concurrent requests to load models can cause race conditions, duplicate loading, and memory issues. Need thread-safe model loading with request queuing.

#### 3.5.2 Design Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| **Thread-Safe Loading** | Sequential model loading | CRITICAL |
| **Request Queue** | Queue concurrent load requests | HIGH |
| **Duplicate Detection** | Prevent loading same model twice | HIGH |
| **Reference Counting** | Track model usage | MEDIUM |
| **Graceful Waiting** | Wait for in-progress loads | HIGH |

#### 3.5.3 File Locations

| File | Type | Purpose |
|------|------|---------|
| `iron/runtime/cpp/include/iron/model_loader.hpp` | Header | Model loader interface |
| `iron/runtime/cpp/src/model_loader.cpp` | Source | Model loader implementation |

#### 3.5.4 Class Specifications

**ThreadSafeModelLoader Class:**

```cpp
// File: iron/runtime/cpp/include/iron/model_loader.hpp
#pragma once

#include <string>
#include <queue>
#include <map>
#include <mutex>
#include <condition_variable>
#include <memory>
#include <atomic>

namespace iron {
namespace runtime {

// Forward declaration
class MemoryBudget;

/**
 * @brief Thread-safe model loader with queuing
 *
 * Ensures models are loaded sequentially to prevent
 * race conditions and memory issues.
 */
class ThreadSafeModelLoader {
public:
    /**
     * @brief Loaded model information
     */
    struct LoadedModel {
        std::string path;
        std::shared_ptr<void> session;  // Type-erased session
        size_t memoryUsage = 0;
        std::atomic<int> referenceCount{1};
        bool isLoading = false;
    };

    /**
     * @brief Load result
     */
    struct LoadResult {
        bool success;
        std::shared_ptr<LoadedModel> model;
        std::string errorMessage;
        bool wasCached;  // true if model was already loaded
    };

    /**
     * @brief Construct model loader
     * @param memoryBudget Memory budget for validation
     */
    explicit ThreadSafeModelLoader(
        std::shared_ptr<MemoryBudget> memoryBudget = nullptr);

    ~ThreadSafeModelLoader();

    /**
     * @brief Load model (thread-safe)
     * @param path Path to model
     * @return LoadResult with model or error
     */
    LoadResult load(const std::string& path);

    /**
     * @brief Get loaded model
     * @param path Path to model
     * @return Loaded model or nullptr
     */
    std::shared_ptr<LoadedModel> getLoadedModel(const std::string& path) const;

    /**
     * @brief Check if model is loaded
     * @param path Path to model
     * @return true if model is loaded
     */
    bool isLoaded(const std::string& path) const;

    /**
     * @brief Unload model
     * @param path Path to model
     * @return true if unloaded successfully
     */
    bool unload(const std::string& path);

    /**
     * @brief Get all loaded model paths
     * @return Vector of paths
     */
    std::vector<std::string> getLoadedModels() const;

    /**
     * @brief Get number of models being loaded
     * @return Pending load count
     */
    size_t getPendingLoadCount() const;

    /**
     * @brief Increment reference count
     * @param path Path to model
     */
    void incrementReference(const std::string& path);

    /**
     * @brief Decrement reference count and unload if zero
     * @param path Path to model
     */
    void decrementReference(const std::string& path);

private:
    std::shared_ptr<MemoryBudget> memoryBudget_;

    mutable std::mutex queueMutex_;
    std::condition_variable loadComplete_;

    std::queue<std::string> loadQueue_;
    std::map<std::string, std::shared_ptr<LoadedModel>> loadedModels_;

    std::atomic<bool> processing_{false};
    std::atomic<size_t> pendingLoads_{0};

    // Worker thread
    void processQueue();
    LoadResult loadInternal(const std::string& path);
};

} // namespace runtime
} // namespace iron
```

#### 3.5.5 Acceptance Criteria

| ID | Criterion | Verification Method |
|----|-----------|---------------------|
| AC-67.1 | Concurrent loads are serialized | Stress test with parallel loads |
| AC-67.2 | Duplicate loads are detected | Unit test: load same model twice |
| AC-67.3 | Reference counting works | Unit test: increment/decrement |
| AC-67.4 | Queue processing is fair | Test: FIFO ordering |
| AC-67.5 | Memory budget is validated | Integration with MemoryBudget |

---

## 4. Dependencies Analysis

### 4.1 Internal Dependencies

```
                    ┌─────────────────┐
                    │  MemoryBudget   │
                    │   (Task #65)    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
     ┌────────────┐  ┌────────────┐  ┌────────────┐
     │  KV Cache  │  │   RoPE     │  │  Model     │
     │ (Task #63) │  │  Cache     │  │  Loader    │
     │            │  │ (Task #64) │  │ (Task #67) │
     └─────┬──────┘  └────────────┘  └─────┬──────┘
           │                               │
           ▼                               │
     ┌────────────┐                        │
     │ Sequence   │                        │
     │   State    │                        │
     │ (Task #63) │                        │
     └────────────┘                        │
                                         │
                    ┌────────────────────┘
                    │
                    ▼
           ┌────────────────┐
           │  Generation    │
           │    Config      │
           │  (Task #66)    │
           └────────────────┘
```

### 4.2 External Dependencies

| Dependency | Version | Purpose | Used By |
|------------|---------|---------|---------|
| Standard C++17 | - | Core language features | All components |
| CMake | 3.20+ | Build system | All C++ components |

---

## 5. File Creation Summary

### 5.1 C++ Headers

| File | Task | Lines (est.) |
|------|------|--------------|
| `iron/runtime/cpp/include/iron/kv_cache.hpp` | #63 | 200 |
| `iron/runtime/cpp/include/iron/sequence_state.hpp` | #63 | 150 |
| `iron/runtime/cpp/include/iron/rope_cache.hpp` | #64 | 100 |
| `iron/runtime/cpp/include/iron/memory_budget.hpp` | #65 | 180 |
| `iron/runtime/cpp/include/iron/model_loader.hpp` | #67 | 120 |

**Total Header Lines:** ~750

### 5.2 C++ Sources

| File | Task | Lines (est.) |
|------|------|--------------|
| `iron/runtime/cpp/src/kv_cache.cpp` | #63 | 250 |
| `iron/runtime/cpp/src/sequence_state.cpp` | #63 | 150 |
| `iron/runtime/cpp/src/rope_cache.cpp` | #64 | 100 |
| `iron/runtime/cpp/src/memory_budget.cpp` | #65 | 200 |
| `iron/runtime/cpp/src/model_loader.cpp` | #67 | 150 |

**Total Source Lines:** ~850

### 5.3 Python Files

| File | Task | Lines (est.) |
|------|------|--------------|
| `iron/api/generation_config.py` | #66 | 150 |

### 5.4 Build Configuration Updates

| File | Changes |
|------|---------|
| `iron/runtime/cpp/CMakeLists.txt` | Add new source files |
| `iron/runtime/cpp/include/iron/CMakeLists.txt` | Add new headers |

---

## 6. Testing Strategy

### 6.1 Unit Tests

| Component | Test File | Key Tests |
|-----------|-----------|-----------|
| PagedKVCache | `test_kv_cache.cpp` | Allocate/free, read/write, concurrent access |
| SequenceState | `test_sequence_state.cpp` | Start/complete/remove sequences |
| RoPECache | `test_rope_cache.cpp` | Pre-computation, lookup, device buffer |
| MemoryBudget | `test_memory_budget.cpp` | Validation, allocation, budget tracking |
| ModelLoader | `test_model_loader.cpp` | Concurrent loads, reference counting |
| GenerationConfig | `test_generation_config.py` | Parameters, EOS detection, serialization |

### 6.2 Integration Tests

| Test | Components | Purpose |
|------|------------|---------|
| KV + Memory Budget | PagedKVCache, MemoryBudget | Validate KV allocation respects budget |
| RoPE + Model | RoPECache, model forward | Validate RoPE angles work with model |
| Generation Loop | All components | End-to-end token generation |

### 6.3 Performance Benchmarks

| Component | Metric | Target |
|-----------|--------|--------|
| KV Cache | Block allocation time | <1ms per block |
| RoPE Cache | Initialization time | <100ms |
| Memory Budget | Validation overhead | <10ms per check |

---

## 7. Quality Gates

### 7.1 Code Quality

| Gate | Requirement |
|------|-------------|
| Compiles without warnings | -Wall -Wextra -Werror |
| No memory leaks | Valgrind/sanitizers clean |
| Thread safety verified | No data races in stress tests |
| Documentation complete | Doxygen comments for all public APIs |

### 7.2 Test Coverage

| Metric | Target |
|--------|--------|
| Line coverage | >90% |
| Branch coverage | >85% |
| All acceptance criteria | 100% verified |

### 7.3 Performance

| Metric | Target |
|--------|--------|
| KV cache overhead | <5% of attention latency |
| RoPE lookup | O(1) complexity verified |
| Memory validation | <10ms per check |

---

## 8. Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| R1: KV cache memory layout inefficient | Medium | Medium | Profile early, iterate on design |
| R2: RoPE pre-computation too slow | Low | Medium | Optimize angle computation loop |
| R3: Memory budget too restrictive | Medium | High | Provide configuration override |
| R4: Thread-safe loader causes deadlocks | Low | High | Extensive stress testing |
| R5: Generation config missing parameters | Low | Low | Design for extensibility |

---

## 9. Handoff Package for Senior Developer

### 9.1 Implementation Checklist

**For Senior Developer executing Week 1 tasks:**

- [ ] Read this specification thoroughly
- [ ] Review PHASE3_IMPLEMENTATION_PLAN.md for context
- [ ] Create all files listed in Section 5
- [ ] Implement classes per specifications in Section 3
- [ ] Write unit tests per Section 6
- [ ] Verify all acceptance criteria are met
- [ ] Run sanitizers to check for memory issues
- [ ] Document any deviations from specification

### 9.2 Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Pure C++ KV cache | No PyTorch dependency, full control |
| Block-based allocation | Inspired by vLLM, reduces fragmentation |
| Pre-computed RoPE | O(1) lookup vs O(n) computation |
| Hard memory limits | Prevent OOM on constrained devices |
| Thread-safe loader queue | Prevent race conditions in model loading |

### 9.3 Points of Contact

| Role | Responsibility |
|------|----------------|
| Dr. Sarah Kim | Technical specifications, requirements |
| Senior Developer | Implementation, testing |
| Quality Reviewer | Code review, acceptance verification |

---

## 10. Next Steps After Week 1

Upon successful completion of Week 1:

1. **Week 2: Model Loader** - Implement Llama3.2 model loading from HuggingFace
2. **Week 3: Generation Loop** - Implement autoregressive generation with KV cache
3. **Week 4: API Integration** - OpenAI-compatible `/v1/chat/completions` endpoint
4. **Week 5: Testing** - Comprehensive unit and integration tests
5. **Week 6: Hardening** - Error handling, documentation, CI/CD

---

**Document Approval:**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Technical Product Strategist | Dr. Sarah Kim | 2026-03-15 | /s/ Dr. Sarah Kim |

---

*Copyright © 2026 IRON Project. All rights reserved.*
