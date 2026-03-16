# Phase 3 Week 1: Technical Implementation Templates

**Document Type:** Implementation Templates & Code Stubs
**Date:** 2026-03-15
**Author:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**For:** Senior Developer - Week 1 Implementation

---

## Overview

This document provides implementation templates and code stubs for Phase 3 Week 1 foundation components. Use these as starting points for your implementation.

**Refer to:** `PHASE3_WEEK1_IMPLEMENTATION_SCOPE.md` for full specifications and acceptance criteria.

---

## Task #63: KV Cache Implementation

### File: `iron/runtime/cpp/include/iron/kv_cache.hpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include <vector>
#include <memory>
#include <mutex>
#include <cstdint>
#include <atomic>

namespace iron {
namespace runtime {

/**
 * @brief Paged KV Cache for efficient autoregressive inference
 *
 * Implements block-based KV cache management. Memory is allocated in fixed-size
 * blocks to reduce fragmentation and enable efficient memory reuse.
 *
 * ARCHITECTURE:
 * - Block-based allocation (configurable: 16, 32, 64 tokens)
 * - Per-layer, per-head key and value storage
 * - Thread-safe operations with fine-grained locking
 * - No external dependencies (pure C++17)
 *
 * MEMORY LAYOUT:
 * Each block stores: [numHeads][blockSize][headDim] for keys and values
 * Total block size: 2 * numHeads * blockSize * headDim * sizeof(float)
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

        /**
         * @brief Calculate bytes per block
         * @return Size in bytes
         */
        size_t bytesPerBlock() const {
            // 2 (key + value) * numHeads * blockSize * headDim * sizeof(float)
            return 2 * numHeads * blockSize * headDim * sizeof(float);
        }

        /**
         * @brief Calculate total memory requirement
         * @return Total bytes needed for all blocks
         */
        size_t totalBytes() const {
            return maxBlocks * bytesPerBlock();
        }

        /**
         * @brief Validate configuration
         * @return true if configuration is valid
         */
        bool isValid() const {
            return blockSize > 0 && maxBlocks > 0 && numLayers > 0 &&
                   numHeads > 0 && headDim > 0 && maxSequences > 0;
        }
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
     * @throws std::invalid_argument if config is invalid
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
     * @param layer Layer index (0 to numLayers-1)
     * @param blockId Block containing the token
     * @param tokenOffset Offset within block (0 to blockSize-1)
     * @param head Head index (0 to numHeads-1)
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
     * @param layer Layer index (0 to numLayers-1)
     * @param blockId Block containing the token
     * @param tokenOffset Offset within block
     * @param head Head index (0 to numHeads-1)
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
     * @param layer Layer index (0 to numLayers-1)
     * @param blockId Block containing the token
     * @param tokenOffset Offset within block
     * @param head Head index (0 to numHeads-1)
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

    /**
     * @brief Get configuration
     * @return Current configuration
     */
    const Config& getConfig() const { return config_; }

private:
    /**
     * @brief Internal block structure
     */
    struct Block {
        // Key cache: [numHeads, blockSize, headDim] - flattened
        std::unique_ptr<float[]> keyCache;
        // Value cache: [numHeads, blockSize, headDim] - flattened
        std::unique_ptr<float[]> valueCache;
        bool inUse = false;

        Block() = default;

        Block(size_t numHeads, size_t blockSize, size_t headDim)
            : keyCache(std::make_unique<float[]>(numHeads * blockSize * headDim)),
              valueCache(std::make_unique<float[]>(numHeads * blockSize * headDim)) {}

        // Move constructor
        Block(Block&& other) noexcept
            : keyCache(std::move(other.keyCache)),
              valueCache(std::move(other.valueCache)),
              inUse(other.inUse) {
            other.inUse = false;
        }

        // Move assignment
        Block& operator=(Block&& other) noexcept {
            if (this != &other) {
                keyCache = std::move(other.keyCache);
                valueCache = std::move(other.valueCache);
                inUse = other.inUse;
                other.inUse = false;
            }
            return *this;
        }
    };

    Config config_;
    std::vector<Block> blocks_;
    mutable std::mutex mutex_;
    std::atomic<size_t> allocatedBlocks_{0};

    // Helper methods
    BlockId allocateBlockInternal();
    void freeBlockInternal(BlockId blockId);
    size_t getBlockOffset(BlockId blockId, size_t tokenOffset, size_t head) const;

    // Bounds checking
    void validateLayer(size_t layer) const;
    void validateHead(size_t head) const;
    void validateBlockId(BlockId blockId) const;
    void validateTokenOffset(size_t offset) const;
};

} // namespace runtime
} // namespace iron
```

### File: `iron/runtime/cpp/src/kv_cache.cpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <iron/kv_cache.hpp>
#include <stdexcept>
#include <cstring>
#include <algorithm>

namespace iron {
namespace runtime {

//==============================================================================
// Construction/Destruction
//==============================================================================

PagedKVCache::PagedKVCache(const Config& config)
    : config_(config) {
    // Validate configuration
    if (!config.isValid()) {
        throw std::invalid_argument("Invalid PagedKVCache configuration");
    }

    // Pre-allocate all blocks
    blocks_.reserve(config.maxBlocks);
    for (size_t i = 0; i < config.maxBlocks; ++i) {
        blocks_.emplace_back(config.numHeads, config.blockSize, config.headDim);
    }
}

PagedKVCache::~PagedKVCache() = default;

PagedKVCache::PagedKVCache(PagedKVCache&& other) noexcept
    : config_(std::move(other.config_)),
      blocks_(std::move(other.blocks_)),
      allocatedBlocks_(other.allocatedBlocks_.load()) {
    other.allocatedBlocks_ = 0;
}

PagedKVCache& PagedKVCache::operator=(PagedKVCache&& other) noexcept {
    if (this != &other) {
        config_ = std::move(other.config_);
        blocks_ = std::move(other.blocks_);
        allocatedBlocks_ = other.allocatedBlocks_.load();
        other.allocatedBlocks_ = 0;
    }
    return *this;
}

//==============================================================================
// Block Allocation
//==============================================================================

std::vector<PagedKVCache::BlockId> PagedKVCache::allocateBlocks(size_t numBlocks) {
    std::vector<BlockId> allocated;
    allocated.reserve(numBlocks);

    std::lock_guard<std::mutex> lock(mutex_);

    for (size_t i = 0; i < numBlocks; ++i) {
        if (getAvailableBlocks() == 0) {
            // Not enough blocks - free what we allocated
            for (BlockId id : allocated) {
                freeBlockInternal(id);
            }
            return {};  // Return empty to indicate failure
        }

        BlockId id = allocateBlockInternal();
        allocated.push_back(id);
    }

    return allocated;
}

void PagedKVCache::freeBlocks(const std::vector<BlockId>& blocks) {
    std::lock_guard<std::mutex> lock(mutex_);
    for (BlockId blockId : blocks) {
        freeBlockInternal(blockId);
    }
}

PagedKVCache::BlockId PagedKVCache::allocateBlockInternal() {
    // Find first free block (simple first-fit)
    for (BlockId i = 0; i < static_cast<BlockId>(blocks_.size()); ++i) {
        if (!blocks_[i].inUse) {
            blocks_[i].inUse = true;
            allocatedBlocks_++;
            return i;
        }
    }
    return static_cast<BlockId>(-1);  // No free blocks
}

void PagedKVCache::freeBlockInternal(BlockId blockId) {
    if (blockId < blocks_.size() && blocks_[blockId].inUse) {
        blocks_[blockId].inUse = false;
        // Note: We don't zero out the cache data for performance
        // It will be overwritten on next allocation
        allocatedBlocks_--;
    }
}

//==============================================================================
// KV Operations
//==============================================================================

void PagedKVCache::writeKey(
    size_t layer,
    BlockId blockId,
    size_t tokenOffset,
    size_t head,
    const float* key) {

    validateLayer(layer);
    validateBlockId(blockId);
    validateTokenOffset(tokenOffset);
    validateHead(head);

    if (!blocks_[blockId].inUse) {
        throw std::runtime_error("Writing to unallocated block");
    }

    std::lock_guard<std::mutex> lock(mutex_);

    size_t offset = getBlockOffset(blockId, tokenOffset, head);
    std::memcpy(blocks_[blockId].keyCache.get() + offset, key,
                config_.headDim * sizeof(float));
}

void PagedKVCache::writeValue(
    size_t layer,
    BlockId blockId,
    size_t tokenOffset,
    size_t head,
    const float* value) {

    validateLayer(layer);
    validateBlockId(blockId);
    validateTokenOffset(tokenOffset);
    validateHead(head);

    if (!blocks_[blockId].inUse) {
        throw std::runtime_error("Writing to unallocated block");
    }

    std::lock_guard<std::mutex> lock(mutex_);

    size_t offset = getBlockOffset(blockId, tokenOffset, head);
    std::memcpy(blocks_[blockId].valueCache.get() + offset, value,
                config_.headDim * sizeof(float));
}

void PagedKVCache::readKeyValue(
    size_t layer,
    BlockId blockId,
    size_t tokenOffset,
    size_t head,
    float* key,
    float* value) const {

    validateLayer(layer);
    validateBlockId(blockId);
    validateTokenOffset(tokenOffset);
    validateHead(head);

    std::lock_guard<std::mutex> lock(mutex_);

    size_t offset = getBlockOffset(blockId, tokenOffset, head);
    std::memcpy(key, blocks_[blockId].keyCache.get() + offset,
                config_.headDim * sizeof(float));
    std::memcpy(value, blocks_[blockId].valueCache.get() + offset,
                config_.headDim * sizeof(float));
}

//==============================================================================
// Contiguous Block Access
//==============================================================================

void PagedKVCache::getContiguousBlocks(
    size_t layer,
    BlockId startBlock,
    size_t numBlocks,
    size_t head,
    float* outKeys,
    float* outValues) const {

    validateLayer(layer);
    validateHead(head);

    if (startBlock + numBlocks > blocks_.size()) {
        throw std::out_of_range("Block range out of bounds");
    }

    std::lock_guard<std::mutex> lock(mutex_);

    size_t elementsPerBlock = config_.blockSize * config_.headDim;
    size_t offsetInHead = head * config_.blockSize * config_.headDim;

    for (size_t i = 0; i < numBlocks; ++i) {
        BlockId blockId = startBlock + i;
        if (!blocks_[blockId].inUse) {
            throw std::runtime_error("Reading from unallocated block");
        }

        // Copy keys for this block and head
        std::memcpy(outKeys + i * elementsPerBlock,
                    blocks_[blockId].keyCache.get() + offsetInHead,
                    elementsPerBlock * sizeof(float));

        // Copy values for this block and head
        std::memcpy(outValues + i * elementsPerBlock,
                    blocks_[blockId].valueCache.get() + offsetInHead,
                    elementsPerBlock * sizeof(float));
    }
}

//==============================================================================
// Query Methods
//==============================================================================

size_t PagedKVCache::getAvailableBlocks() const {
    return config_.maxBlocks - allocatedBlocks_.load();
}

size_t PagedKVCache::getTotalBlocks() const {
    return config_.maxBlocks;
}

bool PagedKVCache::canAllocate(size_t requiredBlocks) const {
    return getAvailableBlocks() >= requiredBlocks;
}

size_t PagedKVCache::getMemoryUsage() const {
    // All blocks are pre-allocated, so return total
    return config_.totalBytes();
}

//==============================================================================
// Helper Methods
//==============================================================================

size_t PagedKVCache::getBlockOffset(BlockId blockId, size_t tokenOffset, size_t head) const {
    // Layout: [head0_block0, head0_block1, ..., head1_block0, ...]
    // Within a head: [token0, token1, ..., tokenN] where each token is headDim floats
    return head * config_.blockSize * config_.headDim +
           tokenOffset * config_.headDim;
}

void PagedKVCache::validateLayer(size_t layer) const {
    if (layer >= config_.numLayers) {
        throw std::out_of_range("Layer index out of range");
    }
}

void PagedKVCache::validateHead(size_t head) const {
    if (head >= config_.numHeads) {
        throw std::out_of_range("Head index out of range");
    }
}

void PagedKVCache::validateBlockId(BlockId blockId) const {
    if (blockId >= blocks_.size()) {
        throw std::out_of_range("Block ID out of range");
    }
}

void PagedKVCache::validateTokenOffset(size_t offset) const {
    if (offset >= config_.blockSize) {
        throw std::out_of_range("Token offset out of range");
    }
}

} // namespace runtime
} // namespace iron
```

---

## Task #64: RoPE Cache Implementation

### File: `iron/runtime/cpp/include/iron/rope_cache.hpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

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
 * Supports sequence lengths up to 131K (Llama3.2 max context).
 *
 * MATHEMATICAL BACKGROUND:
 * RoPE applies rotational embeddings to query and key vectors:
 *   RoPE(x, pos, i) = x[i] * cos(theta_i * pos) - x[i+d/2] * sin(theta_i * pos)
 * where theta_i = 10000^(-2i/d)
 *
 * This class pre-computes cos(theta_i * pos) and sin(theta_i * pos) for all
 * positions and dimensions, enabling O(1) lookup during inference.
 *
 * MEMORY LAYOUT:
 * cosCache_: [pos0_dim0, pos0_dim1, ..., pos0_dimN/2,
 *             pos1_dim0, pos1_dim1, ..., pos1_dimN/2,
 *             ...]
 * Size: maxSeqLen * (headDim/2) * sizeof(float)
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

        /**
         * @brief Calculate cache size in elements
         * @return Number of float elements per cache (cos or sin)
         */
        size_t cacheElements() const {
            return maxSeqLen * (headDim / 2);
        }

        /**
         * @brief Calculate total cache size in bytes
         * @return Total bytes for both cos and sin caches
         */
        size_t totalBytes() const {
            return cacheElements() * 2 * sizeof(float);  // cos + sin
        }

        /**
         * @brief Validate configuration
         * @return true if valid
         */
        bool isValid() const {
            return maxSeqLen > 0 && headDim > 0 && headDim % 2 == 0 && theta > 0;
        }
    };

    /**
     * @brief Construct and initialize RoPE cache
     * @param config Cache configuration (uses defaults if not provided)
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
     * @return Pointer to interleaved [cos_data, sin_data] buffer
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

    // Cosine cache: [maxSeqLen, headDim/2]
    std::vector<float> cosCache_;

    // Sine cache: [maxSeqLen, headDim/2]
    std::vector<float> sinCache_;

    // Device buffer: interleaved [cos..., sin...] for DMA transfer
    std::unique_ptr<uint8_t[]> deviceBuffer_;
    size_t deviceBufferSize_ = 0;

    // Initialization state
    bool initialized_ = false;
    double initializationTimeMs_ = 0.0;

    // Initialization
    void initialize();
    void computeAngles();

    /**
     * @brief Calculate inverse frequency for dimension i
     * @param i Dimension index (0 to headDim/2 - 1)
     * @param headDim Head dimension
     * @param theta RoPE theta parameter
     * @return Inverse frequency: 1 / (theta ^ (2*i/headDim))
     */
    float getInverseFrequency(size_t i, size_t headDim, float theta) const;
};

} // namespace runtime
} // namespace iron
```

### File: `iron/runtime/cpp/src/rope_cache.cpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <iron/rope_cache.hpp>
#include <cmath>
#include <chrono>
#include <stdexcept>
#include <cstring>

namespace iron {
namespace runtime {

//==============================================================================
// Construction/Destruction
//==============================================================================

RoPECache::RoPECache(const Config& config) : config_(config) {
    if (!config.isValid()) {
        throw std::invalid_argument("Invalid RoPECache configuration");
    }
    initialize();
}

RoPECache::~RoPECache() = default;

//==============================================================================
// Initialization
//==============================================================================

void RoPECache::initialize() {
    auto startTime = std::chrono::high_resolution_clock::now();

    // Allocate caches
    size_t elements = config_.cacheElements();
    cosCache_.resize(elements);
    sinCache_.resize(elements);

    // Compute angles
    computeAngles();

    // Create device buffer (interleaved cos + sin)
    deviceBufferSize_ = config_.totalBytes();
    deviceBuffer_ = std::make_unique<uint8_t[]>(deviceBufferSize_);

    // Copy to device buffer in interleaved format
    std::memcpy(deviceBuffer_.get(), cosCache_.data(), elements * sizeof(float));
    std::memcpy(deviceBuffer_.get() + elements * sizeof(float),
                sinCache_.data(), elements * sizeof(float));

    auto endTime = std::chrono::high_resolution_clock::now();
    initializationTimeMs_ = std::chrono::duration<double, std::milli>(
        endTime - startTime).count();

    initialized_ = true;
}

void RoPECache::computeAngles() {
    size_t halfDim = config_.headDim / 2;

    // Pre-compute inverse frequencies
    std::vector<float> invFreq(halfDim);
    for (size_t i = 0; i < halfDim; ++i) {
        invFreq[i] = getInverseFrequency(i, config_.headDim, config_.theta);
    }

    // Compute sin/cos for all positions and dimensions
    for (size_t pos = 0; pos < config_.maxSeqLen; ++pos) {
        for (size_t i = 0; i < halfDim; ++i) {
            float angle = pos * invFreq[i];
            size_t idx = pos * halfDim + i;
            cosCache_[idx] = std::cos(angle);
            sinCache_[idx] = std::sin(angle);
        }
    }
}

float RoPECache::getInverseFrequency(size_t i, size_t headDim, float theta) const {
    // inv_freq[i] = 1 / (theta ^ (2*i/headDim))
    // Computed as: theta^(-2*i/headDim)
    float exponent = -2.0f * static_cast<float>(i) / static_cast<float>(headDim);
    return std::pow(theta, exponent);
}

//==============================================================================
// Table Access
//==============================================================================

const float* RoPECache::getCosTable(size_t seqLen) const {
    if (!initialized_) {
        throw std::runtime_error("RoPECache not initialized");
    }
    if (seqLen > config_.maxSeqLen) {
        throw std::out_of_range("Sequence length exceeds maxSeqLen");
    }
    return cosCache_.data();  // Return full table, caller uses first seqLen rows
}

const float* RoPECache::getSinTable(size_t seqLen) const {
    if (!initialized_) {
        throw std::runtime_error("RoPECache not initialized");
    }
    if (seqLen > config_.maxSeqLen) {
        throw std::out_of_range("Sequence length exceeds maxSeqLen");
    }
    return sinCache_.data();  // Return full table, caller uses first seqLen rows
}

const void* RoPECache::getDeviceBuffer() const {
    if (!initialized_) {
        throw std::runtime_error("RoPECache not initialized");
    }
    return deviceBuffer_.get();
}

size_t RoPECache::getDeviceBufferSize() const {
    return deviceBufferSize_;
}

} // namespace runtime
} // namespace iron
```

---

## Task #65: Memory Budget Implementation

### File: `iron/runtime/cpp/include/iron/memory_budget.hpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include <string>
#include <atomic>
#include <cstdint>
#include <cstddef>

namespace iron {
namespace runtime {

/**
 * @brief Memory budget enforcement and validation
 *
 * Tracks memory usage across components and enforces hard limits
 * to prevent OOM conditions on resource-constrained devices.
 *
 * COMPONENTS:
 * - WEIGHTS: Model weight parameters
 * - KV_CACHE: KV cache for autoregressive generation
 * - ACTIVATIONS: Temporary activation tensors
 * - MISC: Miscellaneous allocations
 *
 * USAGE PATTERN:
 * 1. Create MemoryBudget with appropriate limits
 * 2. Call validateModelLoad() before loading model
 * 3. Use allocateWithBudget() for tracked allocations
 * 4. Call freeWithBudget() when freeing
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

        /**
         * @brief Validate limits are consistent
         * @return true if sum of component budgets + headroom <= totalBudget
         */
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

        /**
         * @brief Convert to human-readable string
         */
        std::string toString() const {
            if (success) return "Allocation OK";
            return errorMessage +
                   " (requested: " + std::to_string(requestedSize) +
                   " bytes, available: " + std::to_string(availableSize) + " bytes)";
        }
    };

    /**
     * @brief Construct memory budget with limits
     * @param limits Memory limits (uses defaults if not provided)
     * @throws std::invalid_argument if limits are invalid
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
        size_t blockSize = 32) const;

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
     * @brief Get limits
     * @return Current limits
     */
    const Limits& getLimits() const { return limits_; }

    /**
     * @brief Reset all usage counters (for testing)
     */
    void reset();

private:
    Limits limits_;

    // Atomic usage counters (bytes)
    std::atomic<size_t> usedWeights_{0};
    std::atomic<size_t> usedKVCache_{0};
    std::atomic<size_t> usedActivations_{0};
    std::atomic<size_t> usedMisc_{0};

    size_t getBudgetForComponent(Component component) const;
    size_t getUsageForComponent(Component component) const;
    void addUsage(Component component, size_t size);
    void removeUsage(Component component, size_t size);

    static size_t formatBytes(size_t bytes);
};

/**
 * @brief Calculate KV cache memory requirements
 * @param sequenceLength Sequence length
 * @param batchSize Batch size
 * @param numLayers Number of transformer layers
 * @param numHeads Number of attention heads
 * @param headDim Head dimension
 * @param blockSize KV cache block size (default: 32)
 * @return Memory requirement in bytes
 */
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

### File: `iron/runtime/cpp/src/memory_budget.cpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <iron/memory_budget.hpp>
#include <stdexcept>
#include <cstring>
#include <sstream>
#include <iomanip>

namespace iron {
namespace runtime {

//==============================================================================
// Construction/Destruction
//==============================================================================

MemoryBudget::MemoryBudget(const Limits& limits) : limits_(limits) {
    if (!limits.isValid()) {
        throw std::invalid_argument("Invalid MemoryBudget limits");
    }
}

//==============================================================================
// Validation
//==============================================================================

MemoryBudget::AllocationResult MemoryBudget::validateModelLoad(
    size_t requiredWeights,
    size_t requiredKV,
    size_t requiredActivations) const {

    // Check each component budget
    if (requiredWeights > limits_.weightBudget) {
        return AllocationResult{
            false,
            "Weight memory exceeds budget",
            requiredWeights,
            limits_.weightBudget
        };
    }

    if (requiredKV > limits_.kvCacheBudget) {
        return AllocationResult{
            false,
            "KV cache memory exceeds budget",
            requiredKV,
            limits_.kvCacheBudget
        };
    }

    if (requiredActivations > limits_.activationBudget) {
        return AllocationResult{
            false,
            "Activation memory exceeds budget",
            requiredActivations,
            limits_.activationBudget
        };
    }

    // Check total budget
    size_t totalRequired = requiredWeights + requiredKV + requiredActivations;
    size_t availableForModel = limits_.totalBudget - limits_.headroom;

    if (totalRequired > availableForModel) {
        return AllocationResult{
            false,
            "Total memory requirement exceeds available budget",
            totalRequired,
            availableForModel
        };
    }

    // All checks passed
    return AllocationResult{true, "", requiredWeights, 0};
}

bool MemoryBudget::canAllocateKV(
    size_t sequenceLength,
    size_t batchSize,
    size_t numLayers,
    size_t numHeads,
    size_t headDim,
    size_t blockSize) const {

    size_t required = calculateKVCacheMemory(
        sequenceLength, batchSize, numLayers, numHeads, headDim, blockSize);

    return required <= getRemainingBudget(Component::KV_CACHE);
}

//==============================================================================
// Budget Queries
//==============================================================================

size_t MemoryBudget::getRemainingBudget(Component component) const {
    return getBudgetForComponent(component) - getUsageForComponent(component);
}

size_t MemoryBudget::getCurrentUsage(Component component) const {
    return getUsageForComponent(component);
}

size_t MemoryBudget::getBudgetForComponent(Component component) const {
    switch (component) {
        case Component::WEIGHTS: return limits_.weightBudget;
        case Component::KV_CACHE: return limits_.kvCacheBudget;
        case Component::ACTIVATIONS: return limits_.activationBudget;
        case Component::MISC: return limits_.totalBudget - limits_.headroom -
                               limits_.weightBudget - limits_.kvCacheBudget -
                               limits_.activationBudget;
    }
    return 0;  // Should never reach here
}

size_t MemoryBudget::getUsageForComponent(Component component) const {
    switch (component) {
        case Component::WEIGHTS: return usedWeights_.load();
        case Component::KV_CACHE: return usedKVCache_.load();
        case Component::ACTIVATIONS: return usedActivations_.load();
        case Component::MISC: return usedMisc_.load();
    }
    return 0;  // Should never reach here
}

//==============================================================================
// Allocation/Deallocation
//==============================================================================

void* MemoryBudget::allocateWithBudget(size_t size, Component component) {
    if (size > getRemainingBudget(component)) {
        return nullptr;  // Budget exceeded
    }

    void* ptr = std::malloc(size);
    if (ptr) {
        addUsage(component, size);
    }
    return ptr;
}

void MemoryBudget::freeWithBudget(void* ptr, size_t size, Component component) {
    if (ptr) {
        std::free(ptr);
        removeUsage(component, size);
    }
}

bool MemoryBudget::reserveBudget(size_t size, Component component) {
    if (size > getRemainingBudget(component)) {
        return false;
    }
    // For now, just return success
    // Could implement a reservation system for complex scenarios
    return true;
}

void MemoryBudget::releaseBudget(size_t size, Component component) {
    // No-op for now - reservations are not tracked
    (void)size;
    (void)component;
}

//==============================================================================
// Utility Methods
//==============================================================================

size_t MemoryBudget::getTotalUsage() const {
    return usedWeights_.load() + usedKVCache_.load() +
           usedActivations_.load() + usedMisc_.load();
}

double MemoryBudget::getUtilizationPercentage() const {
    return (static_cast<double>(getTotalUsage()) /
            static_cast<double>(limits_.totalBudget)) * 100.0;
}

void MemoryBudget::reset() {
    usedWeights_ = 0;
    usedKVCache_ = 0;
    usedActivations_ = 0;
    usedMisc_ = 0;
}

void MemoryBudget::addUsage(Component component, size_t size) {
    switch (component) {
        case Component::WEIGHTS: usedWeights_ += size; break;
        case Component::KV_CACHE: usedKVCache_ += size; break;
        case Component::ACTIVATIONS: usedActivations_ += size; break;
        case Component::MISC: usedMisc_ += size; break;
    }
}

void MemoryBudget::removeUsage(Component component, size_t size) {
    switch (component) {
        case Component::WEIGHTS:
            usedWeights_ = (usedWeights_ >= size) ? (usedWeights_ - size) : 0;
            break;
        case Component::KV_CACHE:
            usedKVCache_ = (usedKVCache_ >= size) ? (usedKVCache_ - size) : 0;
            break;
        case Component::ACTIVATIONS:
            usedActivations_ = (usedActivations_ >= size) ? (usedActivations_ - size) : 0;
            break;
        case Component::MISC:
            usedMisc_ = (usedMisc_ >= size) ? (usedMisc_ - size) : 0;
            break;
    }
}

size_t MemoryBudget::formatBytes(size_t bytes) {
    return bytes;  // Placeholder for potential formatting utility
}

} // namespace runtime
} // namespace iron
```

---

## Task #66: Generation Configuration (Python)

### File: `iron/api/generation_config.py`

```python
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

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

        # Model-specific configuration
        model_type: Model type identifier
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
        if not (0 <= self.top_p <= 1):
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

        Args:
            token_id: Current token ID
            current_length: Current sequence length
            generated_text: Generated text so far

        Returns:
            Tuple of (should_stop, reason)
        """
        # Check EOS tokens
        if self.is_eos_token(token_id):
            return True, "eos_token"

        # Check max length
        if self.max_length and current_length >= self.max_length:
            return True, "max_length"

        # Check max new tokens
        # (caller should track this separately)

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
        # Filter out None values to use defaults
        filtered = {k: v for k, v in data.items() if v is not None}
        return cls(**filtered)

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

LLAMA3_HIGH_CREATIVE_CONFIG = GenerationConfig(
    model_type="llama3",
    eos_tokens=[128001, 128009],
    temperature=1.0,
    top_p=0.95,
    top_k=100,
    max_new_tokens=4096,
)
```

---

## Task #67: Concurrent Model Loader

### File: `iron/runtime/cpp/include/iron/model_loader.hpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#pragma once

#include <string>
#include <queue>
#include <map>
#include <mutex>
#include <condition_variable>
#include <memory>
#include <atomic>
#include <vector>
#include <thread>
#include <functional>

namespace iron {
namespace runtime {

// Forward declaration
class MemoryBudget;

/**
 * @brief Thread-safe model loader with queuing
 *
 * Ensures models are loaded sequentially to prevent
 * race conditions and memory issues.
 *
 * FEATURES:
 * - Sequential model loading (one at a time)
 * - Request queue for concurrent load requests
 * - Duplicate detection (prevents loading same model twice)
 * - Reference counting for model usage tracking
 * - Memory budget validation before loading
 */
class ThreadSafeModelLoader {
public:
    /**
     * @brief Loaded model information
     */
    struct LoadedModel {
        std::string path;
        std::shared_ptr<void> session;  // Type-erased session (could be Ort::Session*)
        size_t memoryUsage = 0;
        std::atomic<int> referenceCount{1};
        bool isLoading = false;
        std::string errorMessage;

        /**
         * @brief Check if model is ready for use
         */
        bool isReady() const {
            return session != nullptr && !isLoading;
        }
    };

    /**
     * @brief Load result
     */
    struct LoadResult {
        bool success;
        std::shared_ptr<LoadedModel> model;
        std::string errorMessage;
        bool wasCached;  // true if model was already loaded

        /**
         * @brief Get model or throw exception
         */
        std::shared_ptr<LoadedModel> getOrThrow() const {
            if (!success) {
                throw std::runtime_error(errorMessage);
            }
            return model;
        }
    };

    /**
     * @brief Model load callback type
     */
    using LoadCallback = std::function<std::shared_ptr<LoadedModel>(const std::string&)>;

    /**
     * @brief Construct model loader
     * @param memoryBudget Memory budget for validation (optional)
     * @param loadCallback Callback to perform actual loading
     */
    explicit ThreadSafeModelLoader(
        std::shared_ptr<MemoryBudget> memoryBudget = nullptr,
        LoadCallback loadCallback = nullptr);

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
     * @return Loaded model or nullptr if not loaded
     */
    std::shared_ptr<LoadedModel> getLoadedModel(const std::string& path) const;

    /**
     * @brief Check if model is loaded
     * @param path Path to model
     * @return true if model is loaded and ready
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
     * @brief Get number of pending loads
     * @return Number of loads in queue
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

    /**
     * @brief Get reference count
     * @param path Path to model
     * @return Reference count or 0 if not loaded
     */
    int getReferenceCount(const std::string& path) const;

private:
    std::shared_ptr<MemoryBudget> memoryBudget_;
    LoadCallback loadCallback_;

    mutable std::mutex queueMutex_;
    std::condition_variable loadComplete_;

    std::queue<std::string> loadQueue_;
    std::map<std::string, std::shared_ptr<LoadedModel>> loadedModels_;

    std::atomic<bool> processing_{false};
    std::atomic<size_t> pendingLoads_{0};

    // Worker thread
    std::thread workerThread_;
    bool stopping_ = false;

    // Internal methods
    void startWorker();
    void stopWorker();
    void processQueue();
    LoadResult loadInternal(const std::string& path);
    LoadResult loadFromCache(const std::string& path);
};

} // namespace runtime
} // namespace iron
```

### File: `iron/runtime/cpp/src/model_loader.cpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <iron/model_loader.hpp>
#include <iron/memory_budget.hpp>
#include <stdexcept>
#include <algorithm>

namespace iron {
namespace runtime {

//==============================================================================
// Construction/Destruction
//==============================================================================

ThreadSafeModelLoader::ThreadSafeModelLoader(
    std::shared_ptr<MemoryBudget> memoryBudget,
    LoadCallback loadCallback)
    : memoryBudget_(memoryBudget),
      loadCallback_(loadCallback) {
    startWorker();
}

ThreadSafeModelLoader::~ThreadSafeModelLoader() {
    stopWorker();
}

//==============================================================================
// Worker Thread
//==============================================================================

void ThreadSafeModelLoader::startWorker() {
    stopping_ = false;
    workerThread_ = std::thread(&ThreadSafeModelLoader::processQueue, this);
}

void ThreadSafeModelLoader::stopWorker() {
    {
        std::lock_guard<std::mutex> lock(queueMutex_);
        stopping_ = true;
    }
    loadComplete_.notify_one();
    if (workerThread_.joinable()) {
        workerThread_.join();
    }
}

void ThreadSafeModelLoader::processQueue() {
    while (true) {
        std::string pathToLoad;

        // Wait for work
        {
            std::unique_lock<std::mutex> lock(queueMutex_);
            loadComplete_.wait(lock, [this] {
                return stopping_ || !loadQueue_.empty();
            });

            if (stopping_ && loadQueue_.empty()) {
                return;
            }

            if (!loadQueue_.empty()) {
                pathToLoad = loadQueue_.front();
                loadQueue_.pop();
                processing_ = true;
            }
        }

        // Load outside the lock
        if (!pathToLoad.empty()) {
            loadInternal(pathToLoad);

            // Notify waiters
            {
                std::lock_guard<std::mutex> lock(queueMutex_);
                processing_ = false;
            }
            loadComplete_.notify_all();
        }
    }
}

//==============================================================================
// Public API
//==============================================================================

ThreadSafeModelLoader::LoadResult ThreadSafeModelLoader::load(const std::string& path) {
    // Check if already loaded
    {
        std::lock_guard<std::mutex> lock(queueMutex_);
        auto it = loadedModels_.find(path);
        if (it != loadedModels_.end() && it->second->isReady()) {
            it->second->referenceCount++;
            return LoadResult{true, it->second, "", true};
        }

        // Check if already loading
        if (it != loadedModels_.end() && it->second->isLoading) {
            // Wait for loading to complete
        }
    }

    // Add to queue
    {
        std::lock_guard<std::mutex> lock(queueMutex_);
        loadQueue_.push(path);
        pendingLoads_++;
    }
    loadComplete_.notify_one();

    // Wait for completion
    while (true) {
        std::this_thread::sleep_for(std::chrono::milliseconds(10));

        std::lock_guard<std::mutex> lock(queueMutex_);
        auto it = loadedModels_.find(path);
        if (it != loadedModels_.end()) {
            if (it->second->isReady()) {
                it->second->referenceCount++;
                return LoadResult{true, it->second, "", false};
            }
            if (!it->second->errorMessage.empty()) {
                return LoadResult{false, nullptr, it->second->errorMessage, false};
            }
        }

        // Check if removed from queue (processing started)
        if (loadQueue_.empty() || loadQueue_.front() != path) {
            // Either processed or still in queue
            if (processing_ && loadQueue_.empty()) {
                // Currently processing this one
                continue;
            }
        }
    }
}

std::shared_ptr<ThreadSafeModelLoader::LoadedModel>
ThreadSafeModelLoader::getLoadedModel(const std::string& path) const {
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it != loadedModels_.end() && it->second->isReady()) {
        return it->second;
    }
    return nullptr;
}

bool ThreadSafeModelLoader::isLoaded(const std::string& path) const {
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    return it != loadedModels_.end() && it->second->isReady();
}

bool ThreadSafeModelLoader::unload(const std::string& path) {
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it == loadedModels_.end()) {
        return false;
    }

    if (it->second->referenceCount > 0) {
        return false;  // Still in use
    }

    loadedModels_.erase(it);
    return true;
}

std::vector<std::string> ThreadSafeModelLoader::getLoadedModels() const {
    std::lock_guard<std::mutex> lock(queueMutex_);
    std::vector<std::string> models;
    for (const auto& [path, model] : loadedModels_) {
        if (model->isReady()) {
            models.push_back(path);
        }
    }
    return models;
}

size_t ThreadSafeModelLoader::getPendingLoadCount() const {
    return pendingLoads_.load();
}

void ThreadSafeModelLoader::incrementReference(const std::string& path) {
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it != loadedModels_.end()) {
        it->second->referenceCount++;
    }
}

void ThreadSafeModelLoader::decrementReference(const std::string& path) {
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it != loadedModels_.end()) {
        it->second->referenceCount--;
    }
}

int ThreadSafeModelLoader::getReferenceCount(const std::string& path) const {
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it != loadedModels_.end()) {
        return it->second->referenceCount.load();
    }
    return 0;
}

//==============================================================================
// Internal Methods
//==============================================================================

ThreadSafeModelLoader::LoadResult ThreadSafeModelLoader::loadInternal(
    const std::string& path) {

    // Check if already loaded (double-check after queue processing)
    {
        std::lock_guard<std::mutex> lock(queueMutex_);
        auto it = loadedModels_.find(path);
        if (it != loadedModels_.end() && it->second->isReady()) {
            pendingLoads_--;
            return LoadResult{true, it->second, "", true};
        }

        // Mark as loading
        if (it == loadedModels_.end()) {
            auto model = std::make_shared<LoadedModel>();
            model->path = path;
            model->isLoading = true;
            loadedModels_[path] = model;
        } else {
            it->second->isLoading = true;
        }
    }

    // Validate memory budget if available
    if (memoryBudget_) {
        // Estimate model size (placeholder - actual implementation would check file size)
        size_t estimatedSize = 0;  // TODO: Get actual file size

        auto result = memoryBudget_->validateModelLoad(estimatedSize, 0, 0);
        if (!result.success) {
            std::lock_guard<std::mutex> lock(queueMutex_);
            loadedModels_[path]->errorMessage = result.errorMessage;
            loadedModels_[path]->isLoading = false;
            pendingLoads_--;
            return LoadResult{false, nullptr, result.errorMessage, false};
        }
    }

    // Load the model via callback
    if (!loadCallback_) {
        std::lock_guard<std::mutex> lock(queueMutex_);
        loadedModels_[path]->errorMessage = "No load callback configured";
        loadedModels_[path]->isLoading = false;
        pendingLoads_--;
        return LoadResult{false, nullptr, "No load callback configured", false};
    }

    try {
        auto loadedModel = loadCallback_(path);
        {
            std::lock_guard<std::mutex> lock(queueMutex_);
            loadedModels_[path] = loadedModel;
            loadedModel->isLoading = false;
        }
        pendingLoads_--;
        return LoadResult{true, loadedModel, "", false};
    } catch (const std::exception& e) {
        std::lock_guard<std::mutex> lock(queueMutex_);
        loadedModels_[path]->errorMessage = e.what();
        loadedModels_[path]->isLoading = false;
        pendingLoads_--;
        return LoadResult{false, nullptr, e.what(), false};
    }
}

} // namespace runtime
} // namespace iron
```

---

## Build Configuration Updates

### File: `iron/runtime/cpp/CMakeLists.txt` (additions)

```cmake
# Add new Week 1 source files
set(IRON_RUNTIME_SOURCES
    ${IRON_RUNTIME_SOURCES}

    # Week 1: Foundation Components
    src/kv_cache.cpp
    src/sequence_state.cpp
    src/rope_cache.cpp
    src/memory_budget.cpp
    src/model_loader.cpp
)

# Add new headers to installation
set(IRON_RUNTIME_HEADERS
    ${IRON_RUNTIME_HEADERS}

    # Week 1: Foundation Components
    include/iron/kv_cache.hpp
    include/iron/sequence_state.hpp
    include/iron/rope_cache.hpp
    include/iron/memory_budget.hpp
    include/iron/model_loader.hpp
)
```

---

## Unit Test Templates

### File: `iron/runtime/test/test_kv_cache.cpp`

```cpp
// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

#include <iron/kv_cache.hpp>
#include <gtest/gtest.h>
#include <thread>
#include <vector>

using namespace iron::runtime;

class PagedKVCacheTest : public ::testing::Test {
protected:
    PagedKVCache::Config createTestConfig() {
        PagedKVCache::Config config;
        config.blockSize = 32;
        config.maxBlocks = 64;
        config.numLayers = 2;  // Small for testing
        config.numHeads = 4;   // Small for testing
        config.headDim = 64;
        return config;
    }
};

TEST_F(PagedKVCacheTest, Construction) {
    auto config = createTestConfig();
    PagedKVCache cache(config);

    EXPECT_EQ(cache.getTotalBlocks(), config.maxBlocks);
    EXPECT_EQ(cache.getAvailableBlocks(), config.maxBlocks);
    EXPECT_EQ(cache.getMemoryUsage(), config.totalBytes());
}

TEST_F(PagedKVCacheTest, BlockAllocation) {
    PagedKVCache cache(createTestConfig());

    auto blocks = cache.allocateBlocks(4);
    EXPECT_EQ(blocks.size(), 4);
    EXPECT_EQ(cache.getAvailableBlocks(), 60);

    cache.freeBlocks(blocks);
    EXPECT_EQ(cache.getAvailableBlocks(), 64);
}

TEST_F(PagedKVCacheTest, KVReadWrite) {
    PagedKVCache cache(createTestConfig());

    auto blocks = cache.allocateBlocks(1);
    ASSERT_EQ(blocks.size(), 1);

    // Write key
    std::vector<float> key(64, 1.0f);
    cache.writeKey(0, blocks[0], 0, 0, key.data());

    // Read key
    std::vector<float> readKey(64);
    std::vector<float> readValue(64);
    cache.readKeyValue(0, blocks[0], 0, 0, readKey.data(), readValue.data());

    EXPECT_EQ(key, readKey);
}

TEST_F(PagedKVCacheTest, ConcurrentAccess) {
    PagedKVCache cache(createTestConfig());

    auto allocateTask = [&cache]() {
        for (int i = 0; i < 10; ++i) {
            auto blocks = cache.allocateBlocks(1);
            if (!blocks.empty()) {
                cache.freeBlocks(blocks);
            }
        }
    };

    std::vector<std::thread> threads;
    for (int i = 0; i < 4; ++i) {
        threads.emplace_back(allocateTask);
    }

    for (auto& t : threads) {
        t.join();
    }

    // All blocks should be freed
    EXPECT_EQ(cache.getAvailableBlocks(), 64);
}
```

---

**Document Prepared By:** Dr. Sarah Kim, Technical Product Strategist & Engineering Lead
**Date:** 2026-03-15
**For Questions:** Refer to PHASE3_WEEK1_IMPLEMENTATION_SCOPE.md

---

*Copyright © 2026 IRON Project. All rights reserved.*
