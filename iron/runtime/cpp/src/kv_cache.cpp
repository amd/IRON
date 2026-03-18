// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file kv_cache.cpp
 * @brief Implementation of paged KV cache for autoregressive inference
 *
 * This file implements the PagedKVCache class for block-based KV cache
 * management. Key features:
 *
 * - Block-based allocation reduces memory fragmentation
 * - Thread-safe operations via mutex protection
 * - Bounds checking for all operations
 * - Pre-allocated memory pools for performance
 *
 * MEMORY LAYOUT:
 * Each block stores keys and values for all heads:
 * - keyCache: flattened [numHeads * blockSize * headDim]
 * - valueCache: flattened [numHeads * blockSize * headDim]
 *
 * OFFSET CALCULATION:
 * For a given head and token offset within a block:
 *   offset = head * (blockSize * headDim) + tokenOffset * headDim
 */

#include <algorithm>
#include <cstring>
#include <iron/kv_cache.hpp>
#include <sstream>
#include <stdexcept>
#include <string>

namespace iron
{
namespace runtime
{

//==============================================================================
// Construction/Destruction
//==============================================================================

PagedKVCache::PagedKVCache(const Config &config) : config_(config)
{
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

PagedKVCache::PagedKVCache(PagedKVCache &&other) noexcept
    : config_(std::move(other.config_)),
      blocks_(std::move(other.blocks_)),
      allocatedBlocks_(other.allocatedBlocks_.load())
{
    other.allocatedBlocks_ = 0;
}

PagedKVCache &PagedKVCache::operator=(PagedKVCache &&other) noexcept
{
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

std::vector<PagedKVCache::BlockId> PagedKVCache::allocateBlocks(size_t numBlocks)
{
    std::vector<BlockId> allocated;
    allocated.reserve(numBlocks);

    std::lock_guard<std::mutex> lock(mutex_);

    for (size_t i = 0; i < numBlocks; ++i) {
        if (getAvailableBlocks() == 0) {
            // Not enough blocks - free what we allocated
            for (BlockId id : allocated) {
                freeBlockInternal(id);
            }
            return {}; // Return empty to indicate failure
        }

        BlockId id = allocateBlockInternal();
        allocated.push_back(id);
    }

    return allocated;
}

void PagedKVCache::freeBlocks(const std::vector<BlockId> &blocks)
{
    std::lock_guard<std::mutex> lock(mutex_);
    for (BlockId blockId : blocks) {
        freeBlockInternal(blockId);
    }
}

PagedKVCache::BlockId PagedKVCache::allocateBlockInternal()
{
    // Find first free block (simple first-fit strategy)
    for (BlockId i = 0; i < static_cast<BlockId>(blocks_.size()); ++i) {
        if (!blocks_[i].inUse) {
            blocks_[i].inUse = true;
            allocatedBlocks_.fetch_add(1, std::memory_order_relaxed);
            return i;
        }
    }
    return static_cast<BlockId>(-1); // No free blocks
}

void PagedKVCache::freeBlockInternal(BlockId blockId)
{
    if (blockId < blocks_.size() && blocks_[blockId].inUse) {
        blocks_[blockId].inUse = false;
        // Note: We don't zero out the cache data for performance
        // It will be overwritten on next allocation
        allocatedBlocks_.fetch_sub(1, std::memory_order_relaxed);
    }
}

//==============================================================================
// KV Operations
//==============================================================================

void PagedKVCache::writeKey(size_t layer, BlockId blockId, size_t tokenOffset, size_t head, const float *key)
{

    // Validate all indices
    validateLayer(layer);
    validateBlockId(blockId);
    validateTokenOffset(tokenOffset);
    validateHead(head);

    // Check block is allocated
    if (!blocks_[blockId].inUse) {
        throw std::runtime_error("Writing to unallocated block");
    }

    std::lock_guard<std::mutex> lock(mutex_);

    size_t offset = getBlockOffset(blockId, tokenOffset, head);
    std::memcpy(blocks_[blockId].keyCache.get() + offset, key, config_.headDim * sizeof(float));
}

void PagedKVCache::writeValue(size_t layer, BlockId blockId, size_t tokenOffset, size_t head, const float *value)
{

    // Validate all indices
    validateLayer(layer);
    validateBlockId(blockId);
    validateTokenOffset(tokenOffset);
    validateHead(head);

    // Check block is allocated
    if (!blocks_[blockId].inUse) {
        throw std::runtime_error("Writing to unallocated block");
    }

    std::lock_guard<std::mutex> lock(mutex_);

    size_t offset = getBlockOffset(blockId, tokenOffset, head);
    std::memcpy(blocks_[blockId].valueCache.get() + offset, value, config_.headDim * sizeof(float));
}

void PagedKVCache::readKeyValue(size_t layer,
                                BlockId blockId,
                                size_t tokenOffset,
                                size_t head,
                                float *key,
                                float *value) const
{

    // Validate all indices
    validateLayer(layer);
    validateBlockId(blockId);
    validateTokenOffset(tokenOffset);
    validateHead(head);

    std::lock_guard<std::mutex> lock(mutex_);

    size_t offset = getBlockOffset(blockId, tokenOffset, head);
    std::memcpy(key, blocks_[blockId].keyCache.get() + offset, config_.headDim * sizeof(float));
    std::memcpy(value, blocks_[blockId].valueCache.get() + offset, config_.headDim * sizeof(float));
}

//==============================================================================
// Contiguous Block Access
//==============================================================================

void PagedKVCache::getContiguousBlocks(size_t layer,
                                       BlockId startBlock,
                                       size_t numBlocks,
                                       size_t head,
                                       float *outKeys,
                                       float *outValues) const
{

    validateLayer(layer);
    validateHead(head);

    if (startBlock + numBlocks > blocks_.size()) {
        throw std::out_of_range("Block range out of bounds");
    }

    std::lock_guard<std::mutex> lock(mutex_);

    const size_t elementsPerBlock = config_.blockSize * config_.headDim;
    const size_t offsetInHead = head * config_.blockSize * config_.headDim;

    for (size_t i = 0; i < numBlocks; ++i) {
        BlockId blockId = static_cast<BlockId>(startBlock + i);
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

size_t PagedKVCache::getAvailableBlocks() const
{
    return config_.maxBlocks - allocatedBlocks_.load(std::memory_order_relaxed);
}

size_t PagedKVCache::getTotalBlocks() const
{
    return config_.maxBlocks;
}

bool PagedKVCache::canAllocate(size_t requiredBlocks) const
{
    return getAvailableBlocks() >= requiredBlocks;
}

size_t PagedKVCache::getMemoryUsage() const
{
    // All blocks are pre-allocated, so return total
    return config_.totalBytes();
}

//==============================================================================
// Helper Methods
//==============================================================================

size_t PagedKVCache::getBlockOffset(BlockId /* blockId */, size_t tokenOffset, size_t head) const
{
    // Layout: [head0_block0, head0_block1, ..., head1_block0, ...]
    // Within a head: [token0, token1, ..., tokenN] where each token is headDim floats
    // Note: blockId is not used in offset calculation since each block has the same layout
    return head * config_.blockSize * config_.headDim + tokenOffset * config_.headDim;
}

void PagedKVCache::validateLayer(size_t layer) const
{
    if (layer >= config_.numLayers) {
        throw std::out_of_range("Layer index " + std::to_string(layer) + " >= numLayers " +
                                std::to_string(config_.numLayers));
    }
}

void PagedKVCache::validateHead(size_t head) const
{
    if (head >= config_.numHeads) {
        throw std::out_of_range("Head index " + std::to_string(head) + " >= numHeads " +
                                std::to_string(config_.numHeads));
    }
}

void PagedKVCache::validateBlockId(BlockId blockId) const
{
    if (blockId >= blocks_.size()) {
        throw std::out_of_range("Block ID " + std::to_string(blockId) + " >= total blocks " +
                                std::to_string(blocks_.size()));
    }
}

void PagedKVCache::validateTokenOffset(size_t offset) const
{
    if (offset >= config_.blockSize) {
        throw std::out_of_range("Token offset " + std::to_string(offset) + " >= blockSize " +
                                std::to_string(config_.blockSize));
    }
}

} // namespace runtime
} // namespace iron
