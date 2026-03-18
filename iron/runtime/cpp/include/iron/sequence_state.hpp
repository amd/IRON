// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file sequence_state.hpp
 * @brief Sequence state tracking for autoregressive generation
 *
 * This header defines the SequenceState class for tracking the state
 * of individual generation sequences during autoregressive inference.
 *
 * FEATURES:
 * - Unique sequence ID generation
 * - KV cache block tracking per sequence
 * - Generated token history
 * - Stop condition tracking (EOS, max_length, stop_string)
 * - Thread-safe operations
 *
 * USAGE PATTERN:
 * 1. Create SequenceState with shared PagedKVCache
 * 2. Call startSequence() to begin generation
 * 3. Call appendToken() for each generated token
 * 4. Call completeSequence() when done
 * 5. Call removeSequence() to free resources
 */

#pragma once

#include <atomic>
#include <cstdint>
#include <iron/kv_cache.hpp>
#include <map>
#include <memory>
#include <mutex>
#include <random>
#include <string>
#include <vector>

namespace iron
{
namespace runtime
{

/**
 * @brief Tracks state for an autoregressive generation sequence
 *
 * Manages the lifecycle of a generation sequence from start to completion,
 * tracking allocated KV cache blocks, generated tokens, and stop conditions.
 */
class SequenceState
{
  public:
    /**
     * @brief Sequence state information
     */
    struct State {
        uint64_t sequenceId;                         ///< Unique sequence identifier
        size_t currentLength = 0;                    ///< Current sequence length
        size_t promptLength = 0;                     ///< Original prompt length
        std::vector<PagedKVCache::BlockId> kvBlocks; ///< Allocated KV blocks
        std::vector<int32_t> generatedTokens;        ///< Generated token IDs
        bool isComplete = false;                     ///< Generation finished
        std::string stopReason;                      ///< Why generation stopped

        // For long-context resumption
        std::vector<float> cachedPromptEmbeddings; ///< Optional: cache embeddings
    };

    /**
     * @brief Construct sequence state manager
     * @param kvCache Reference to shared KV cache
     * @throws std::invalid_argument if kvCache is null
     */
    explicit SequenceState(std::shared_ptr<PagedKVCache> kvCache);

    /**
     * @brief Destructor
     */
    ~SequenceState();

    // Prevent copying
    SequenceState(const SequenceState &) = delete;
    SequenceState &operator=(const SequenceState &) = delete;

    // Allow moving
    SequenceState(SequenceState &&other) noexcept = default;
    SequenceState &operator=(SequenceState &&other) noexcept = default;

    //==========================================================================
    // Sequence Lifecycle
    //==========================================================================

    /**
     * @brief Start a new sequence
     * @param promptTokens Input prompt token IDs
     * @param maxNewTokens Maximum tokens to generate
     * @return Sequence ID for tracking
     * @throws std::bad_alloc if KV blocks cannot be allocated
     */
    uint64_t startSequence(const std::vector<int32_t> &promptTokens, size_t maxNewTokens);

    /**
     * @brief Append a generated token to sequence
     * @param sequenceId Sequence to update
     * @param tokenId Generated token ID
     * @throws std::out_of_range if sequence not found
     */
    void appendToken(uint64_t sequenceId, int32_t tokenId);

    /**
     * @brief Mark sequence as complete
     * @param sequenceId Sequence to complete
     * @param reason Stop reason (eos, max_length, stop_string)
     * @throws std::out_of_range if sequence not found
     */
    void completeSequence(uint64_t sequenceId, const std::string &reason);

    /**
     * @brief Remove sequence and free resources
     * @param sequenceId Sequence to remove
     * @throws std::out_of_range if sequence not found
     */
    void removeSequence(uint64_t sequenceId);

    //==========================================================================
    // State Queries
    //==========================================================================

    /**
     * @brief Get current sequence state
     * @param sequenceId Sequence to query
     * @return Current state
     * @throws std::out_of_range if sequence not found
     */
    State getState(uint64_t sequenceId) const;

    /**
     * @brief Check if sequence exists
     * @param sequenceId Sequence to check
     * @return true if sequence is active
     */
    bool hasSequence(uint64_t sequenceId) const;

    /**
     * @brief Get all active sequence IDs
     * @return Vector of active sequence IDs
     */
    std::vector<uint64_t> getActiveSequences() const;

    /**
     * @brief Get number of tokens to generate next
     * @param sequenceId Sequence to query
     * @return Current length for next token computation
     * @throws std::out_of_range if sequence not found
     */
    size_t getNextTokenPosition(uint64_t sequenceId) const;

    /**
     * @brief Get generated tokens for a sequence
     * @param sequenceId Sequence to query
     * @return Vector of generated token IDs
     * @throws std::out_of_range if sequence not found
     */
    std::vector<int32_t> getGeneratedTokens(uint64_t sequenceId) const;

    /**
     * @brief Get KV cache blocks for a sequence
     * @param sequenceId Sequence to query
     * @return Vector of block IDs
     * @throws std::out_of_range if sequence not found
     */
    std::vector<PagedKVCache::BlockId> getKVBlocks(uint64_t sequenceId) const;

    //==========================================================================
    // Serialization (for long-context resumption)
    //==========================================================================

    /**
     * @brief Serialize sequence state for persistence
     * @param sequenceId Sequence to serialize
     * @return Serialized data
     * @throws std::out_of_range if sequence not found
     */
    std::vector<uint8_t> serialize(uint64_t sequenceId) const;

    /**
     * @brief Deserialize sequence state
     * @param data Serialized data
     * @param kvCache KV cache for restoration
     * @return Restored SequenceState
     * @throws std::runtime_error if deserialization fails
     */
    static std::unique_ptr<SequenceState> deserialize(const std::vector<uint8_t> &data,
                                                      std::shared_ptr<PagedKVCache> kvCache);

  private:
    std::shared_ptr<PagedKVCache> kvCache_;
    std::map<uint64_t, State> sequences_;
    mutable std::mutex mutex_;
    std::mt19937_64 rng_;
    std::atomic<uint64_t> nextSequenceId_{1};

    /**
     * @brief Generate unique sequence ID
     * @return New sequence ID
     */
    uint64_t generateSequenceId();

    /**
     * @brief Calculate blocks needed for sequence
     * @param tokenCount Number of tokens
     * @return Number of blocks required
     */
    size_t calculateBlocksNeeded(size_t tokenCount) const;
};

} // namespace runtime
} // namespace iron
