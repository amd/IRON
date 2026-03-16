// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file kv_cache.hpp
 * @brief Paged KV Cache for efficient autoregressive inference
 *
 * This header defines the PagedKVCache class for block-based KV cache
 * management inspired by vLLM architecture.
 *
 * ARCHITECTURE:
 * - Block-based allocation (configurable: 16, 32, 64 tokens per block)
 * - Per-layer, per-head key and value storage
 * - Thread-safe operations with mutex protection
 * - Pure C++17 implementation (no PyTorch/torchtune dependency)
 *
 * MEMORY LAYOUT:
 * Each block stores: [numHeads][blockSize][headDim] for keys and values
 * Total block size: 2 * numHeads * blockSize * headDim * sizeof(float)
 *
 * THREAD SAFETY:
 * - All public methods are thread-safe
 * - Block allocation/deallocation is serialized
 * - KV read/write operations acquire locks
 */

#pragma once

#include <vector>
#include <memory>
#include <mutex>
#include <cstdint>
#include <cstddef>
#include <atomic>

namespace iron {
namespace runtime {

/**
 * @brief Paged KV Cache for efficient autoregressive inference
 *
 * Implements block-based KV cache management. Memory is allocated in
 * fixed-size blocks to reduce fragmentation and enable efficient
 * memory reuse across sequences.
 */
class PagedKVCache {
public:
    /**
     * @brief Configuration for KV cache
     *
     * Default values target Llama3.2-1B model:
     * - 16 transformer layers
     * - 32 attention heads (or GQA groups)
     * - 64-dimensional head size
     */
    struct Config {
        size_t blockSize = 32;        ///< Tokens per block
        size_t maxBlocks = 1024;      ///< Max blocks per sequence
        size_t numLayers = 16;        ///< Llama3.2-1B layers
        size_t numHeads = 32;         ///< Attention heads (GQA groups)
        size_t headDim = 64;          ///< Head dimension
        size_t maxSequences = 16;     ///< Max concurrent sequences

        /**
         * @brief Calculate bytes per block
         * @return Size in bytes for a single block (keys + values)
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
     * @throws std::invalid_argument if config is invalid
     * @throws std::bad_alloc if memory allocation fails
     */
    explicit PagedKVCache(const Config& config);

    /**
     * @brief Destructor
     */
    ~PagedKVCache();

    // Prevent copying (large object)
    PagedKVCache(const PagedKVCache&) = delete;
    PagedKVCache& operator=(const PagedKVCache&) = delete;

    // Allow moving
    PagedKVCache(PagedKVCache&& other) noexcept;
    PagedKVCache& operator=(PagedKVCache&& other) noexcept;

    //==========================================================================
    // Block Allocation
    //==========================================================================

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

    //==========================================================================
    // KV Operations
    //==========================================================================

    /**
     * @brief Write key vector to cache
     * @param layer Layer index (0 to numLayers-1)
     * @param blockId Block containing the token
     * @param tokenOffset Offset within block (0 to blockSize-1)
     * @param head Head index (0 to numHeads-1)
     * @param key Key vector data [headDim]
     * @throws std::out_of_range if indices are invalid
     * @throws std::runtime_error if writing to unallocated block
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
     * @throws std::out_of_range if indices are invalid
     * @throws std::runtime_error if writing to unallocated block
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
     * @throws std::out_of_range if indices are invalid
     */
    void readKeyValue(
        size_t layer,
        BlockId blockId,
        size_t tokenOffset,
        size_t head,
        float* key,
        float* value) const;

    //==========================================================================
    // Contiguous Block Access
    //==========================================================================

    /**
     * @brief Get contiguous memory for attention computation
     *
     * Reads multiple consecutive blocks for efficient attention computation.
     *
     * @param layer Layer index
     * @param startBlock First block to read
     * @param numBlocks Number of blocks to read
     * @param head Head index
     * @param outKeys Output buffer [numBlocks * blockSize * headDim]
     * @param outValues Output buffer [numBlocks * blockSize * headDim]
     * @throws std::out_of_range if block range is invalid
     * @throws std::runtime_error if reading from unallocated block
     */
    void getContiguousBlocks(
        size_t layer,
        BlockId startBlock,
        size_t numBlocks,
        size_t head,
        float* outKeys,
        float* outValues) const;

    //==========================================================================
    // Query Methods
    //==========================================================================

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
     * @return Total memory allocated (pre-allocated blocks)
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
     *
     * Each block contains flattened key and value caches:
     * - keyCache: [numHeads * blockSize * headDim] floats
     * - valueCache: [numHeads * blockSize * headDim] floats
     */
    struct Block {
        // Key cache: [numHeads, blockSize, headDim] - flattened
        std::unique_ptr<float[]> keyCache;
        // Value cache: [numHeads, blockSize, headDim] - flattened
        std::unique_ptr<float[]> valueCache;
        bool inUse = false;

        Block() = default;

        /**
         * @brief Construct block with specified dimensions
         * @param numHeads Number of attention heads
         * @param blockSize Tokens per block
         * @param headDim Head dimension
         */
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

    // Internal helper methods
    BlockId allocateBlockInternal();
    void freeBlockInternal(BlockId blockId);
    size_t getBlockOffset(BlockId blockId, size_t tokenOffset, size_t head) const;

    // Bounds checking helpers
    void validateLayer(size_t layer) const;
    void validateHead(size_t head) const;
    void validateBlockId(BlockId blockId) const;
    void validateTokenOffset(size_t offset) const;
};

} // namespace runtime
} // namespace iron
