// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file memory_budget.hpp
 * @brief Memory budget enforcement and validation for IRON runtime
 *
 * This header defines the MemoryBudget class for tracking and enforcing
 * memory limits across different components to prevent OOM conditions.
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
 *
 * THREAD SAFETY:
 * - All operations are thread-safe via atomic counters
 * - Suitable for concurrent allocations from multiple threads
 */

#pragma once

#include <string>
#include <atomic>
#include <cstdint>
#include <cstddef>
#include <string>

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
        WEIGHTS,      ///< Model weights
        KV_CACHE,     ///< KV cache for attention
        ACTIVATIONS,  ///< Temporary activations
        MISC          ///< Miscellaneous allocations
    };

    /**
     * @brief Memory limits configuration
     *
     * Default values target a 4GB total budget suitable for most NPU devices.
     */
    struct Limits {
        size_t totalBudget = 4ULL * 1024 * 1024 * 1024;    ///< 4 GB total
        size_t weightBudget = 2ULL * 1024 * 1024 * 1024;   ///< 2 GB weights
        size_t kvCacheBudget = 1ULL * 1024 * 1024 * 1024;  ///< 1 GB KV cache
        size_t activationBudget = 512ULL * 1024 * 1024;    ///< 512 MB activations
        size_t headroom = 512ULL * 1024 * 1024;            ///< 512 MB safety

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
        bool success;                  ///< Allocation succeeded
        std::string errorMessage;      ///< Error message if failed
        size_t requestedSize;          ///< Bytes requested
        size_t availableSize;          ///< Bytes available

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

    /**
     * @brief Destructor
     */
    ~MemoryBudget() = default;

    // Prevent copying
    MemoryBudget(const MemoryBudget&) = delete;
    MemoryBudget& operator=(const MemoryBudget&) = delete;

    // Allow moving
    MemoryBudget(MemoryBudget&& other) noexcept = default;
    MemoryBudget& operator=(MemoryBudget&& other) noexcept = default;

    //==========================================================================
    // Validation
    //==========================================================================

    /**
     * @brief Validate memory before model load
     * @param requiredWeights Memory needed for weights in bytes
     * @param requiredKV Memory needed for KV cache (max context) in bytes
     * @param requiredActivations Memory needed for activations in bytes
     * @return AllocationResult with success/failure details
     */
    AllocationResult validateModelLoad(
        size_t requiredWeights,
        size_t requiredKV,
        size_t requiredActivations) const;

    /**
     * @brief Check if KV allocation is possible
     * @param sequenceLength Sequence length in tokens
     * @param batchSize Batch size
     * @param numLayers Number of transformer layers
     * @param numHeads Number of attention heads (or GQA groups)
     * @param headDim Head dimension (e.g., 64)
     * @param blockSize KV cache block size in tokens (default: 32)
     * @return true if allocation would succeed
     */
    bool canAllocateKV(
        size_t sequenceLength,
        size_t batchSize,
        size_t numLayers,
        size_t numHeads,
        size_t headDim,
        size_t blockSize = 32) const;

    //==========================================================================
    // Budget Queries
    //==========================================================================

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
     * @brief Get total memory usage
     * @return Sum of all component usage in bytes
     */
    size_t getTotalUsage() const;

    /**
     * @brief Get total budget
     * @return Total configured budget in bytes
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

    //==========================================================================
    // Allocation/Deallocation
    //==========================================================================

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
     * @param size Size of allocation in bytes
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

    //==========================================================================
    // Utility
    //==========================================================================

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

    // Internal helpers
    size_t getBudgetForComponent(Component component) const;
    size_t getUsageForComponent(Component component) const;
    void addUsage(Component component, size_t size);
    void removeUsage(Component component, size_t size);

    /**
     * @brief Format bytes as human-readable string
     * @param bytes Size in bytes
     * @return Formatted string (e.g., "1.5 GB")
     */
    static std::string formatBytes(size_t bytes);
};

/**
 * @brief Calculate KV cache memory requirements
 * @param sequenceLength Sequence length in tokens
 * @param batchSize Batch size
 * @param numLayers Number of transformer layers
 * @param numHeads Number of attention heads (or GQA groups)
 * @param headDim Head dimension (e.g., 64)
 * @param blockSize KV cache block size in tokens (default: 32)
 * @return Memory requirement in bytes
 *
 * Formula: 2 (key + value) * numLayers * numHeads * totalTokens * sizeof(float)
 * Where totalTokens is rounded up to block boundaries
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
