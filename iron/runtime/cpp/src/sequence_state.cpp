// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file sequence_state.cpp
 * @brief Implementation of sequence state tracking for autoregressive generation
 *
 * This file implements the SequenceState class for managing generation
 * sequence lifecycles. Key responsibilities:
 *
 * - Unique sequence ID generation using atomic counters
 * - KV cache block allocation and tracking per sequence
 * - Token history management
 * - Stop condition tracking
 * - Thread-safe state access
 *
 * THREAD SAFETY:
 * - All public methods are thread-safe
 * - State modifications are protected by mutex
 * - Reads can proceed concurrently when not modifying state
 */

#include <iron/sequence_state.hpp>
#include <stdexcept>
#include <cstring>
#include <algorithm>

namespace iron {
namespace runtime {

//==============================================================================
// Construction/Destruction
//==============================================================================

SequenceState::SequenceState(std::shared_ptr<PagedKVCache> kvCache)
    : kvCache_(std::move(kvCache)),
      rng_(std::random_device{}()) {
    if (!kvCache_) {
        throw std::invalid_argument("SequenceState requires a valid KV cache");
    }
}

SequenceState::~SequenceState() = default;

//==============================================================================
// Sequence Lifecycle
//==============================================================================

uint64_t SequenceState::startSequence(
    const std::vector<int32_t>& promptTokens,
    size_t maxNewTokens) {
    if (promptTokens.empty()) {
        throw std::invalid_argument("Prompt tokens cannot be empty");
    }
    if (maxNewTokens == 0) {
        throw std::invalid_argument("maxNewTokens must be > 0");
    }

    // Calculate blocks needed for full sequence (prompt + max new tokens)
    const size_t totalTokens = promptTokens.size() + maxNewTokens;
    const size_t blocksNeeded = calculateBlocksNeeded(totalTokens);

    // Allocate KV blocks
    auto blocks = kvCache_->allocateBlocks(blocksNeeded);
    if (blocks.empty() && blocksNeeded > 0) {
        throw std::bad_alloc();
    }

    // Create sequence state
    const uint64_t seqId = generateSequenceId();

    std::lock_guard<std::mutex> lock(mutex_);
    State& state = sequences_[seqId];
    state.sequenceId = seqId;
    state.promptLength = promptTokens.size();
    state.currentLength = promptTokens.size();
    state.kvBlocks = std::move(blocks);
    state.generatedTokens.reserve(totalTokens);
    state.generatedTokens.insert(state.generatedTokens.end(),
                                  promptTokens.begin(),
                                  promptTokens.end());
    state.isComplete = false;

    return seqId;
}

void SequenceState::appendToken(uint64_t sequenceId, int32_t tokenId) {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = sequences_.find(sequenceId);
    if (it == sequences_.end()) {
        throw std::out_of_range("Sequence " + std::to_string(sequenceId) + " not found");
    }

    State& state = it->second;
    if (state.isComplete) {
        throw std::runtime_error("Cannot append token to completed sequence");
    }

    state.generatedTokens.push_back(tokenId);
    state.currentLength++;

    // Check if we need more KV blocks (should be pre-allocated, but check anyway)
    const size_t blocksNeeded = calculateBlocksNeeded(state.currentLength);
    if (blocksNeeded > state.kvBlocks.size()) {
        // Try to allocate more blocks
        const size_t additionalBlocks = blocksNeeded - state.kvBlocks.size();
        auto newBlocks = kvCache_->allocateBlocks(additionalBlocks);
        if (!newBlocks.empty()) {
            state.kvBlocks.insert(state.kvBlocks.end(),
                                   newBlocks.begin(),
                                   newBlocks.end());
        }
        // If allocation fails, we continue anyway - the KV cache will handle it
    }
}

void SequenceState::completeSequence(uint64_t sequenceId, const std::string& reason) {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = sequences_.find(sequenceId);
    if (it == sequences_.end()) {
        throw std::out_of_range("Sequence " + std::to_string(sequenceId) + " not found");
    }

    it->second.isComplete = true;
    it->second.stopReason = reason;
}

void SequenceState::removeSequence(uint64_t sequenceId) {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = sequences_.find(sequenceId);
    if (it == sequences_.end()) {
        throw std::out_of_range("Sequence " + std::to_string(sequenceId) + " not found");
    }

    // Free KV blocks
    kvCache_->freeBlocks(it->second.kvBlocks);

    // Remove from map
    sequences_.erase(it);
}

//==============================================================================
// State Queries
//==============================================================================

SequenceState::State SequenceState::getState(uint64_t sequenceId) const {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = sequences_.find(sequenceId);
    if (it == sequences_.end()) {
        throw std::out_of_range("Sequence " + std::to_string(sequenceId) + " not found");
    }

    return it->second;
}

bool SequenceState::hasSequence(uint64_t sequenceId) const {
    std::lock_guard<std::mutex> lock(mutex_);
    return sequences_.find(sequenceId) != sequences_.end();
}

std::vector<uint64_t> SequenceState::getActiveSequences() const {
    std::lock_guard<std::mutex> lock(mutex_);

    std::vector<uint64_t> active;
    active.reserve(sequences_.size());
    for (const auto& [id, state] : sequences_) {
        if (!state.isComplete) {
            active.push_back(id);
        }
    }
    return active;
}

size_t SequenceState::getNextTokenPosition(uint64_t sequenceId) const {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = sequences_.find(sequenceId);
    if (it == sequences_.end()) {
        throw std::out_of_range("Sequence " + std::to_string(sequenceId) + " not found");
    }

    return it->second.currentLength;
}

std::vector<int32_t> SequenceState::getGeneratedTokens(uint64_t sequenceId) const {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = sequences_.find(sequenceId);
    if (it == sequences_.end()) {
        throw std::out_of_range("Sequence " + std::to_string(sequenceId) + " not found");
    }

    return it->second.generatedTokens;
}

std::vector<PagedKVCache::BlockId> SequenceState::getKVBlocks(uint64_t sequenceId) const {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = sequences_.find(sequenceId);
    if (it == sequences_.end()) {
        throw std::out_of_range("Sequence " + std::to_string(sequenceId) + " not found");
    }

    return it->second.kvBlocks;
}

//==============================================================================
// Serialization
//==============================================================================

std::vector<uint8_t> SequenceState::serialize(uint64_t sequenceId) const {
    std::lock_guard<std::mutex> lock(mutex_);

    auto it = sequences_.find(sequenceId);
    if (it == sequences_.end()) {
        throw std::out_of_range("Sequence " + std::to_string(sequenceId) + " not found");
    }

    const State& state = it->second;

    // Simple binary serialization format:
    // [sequenceId:8][currentLength:8][promptLength:8][isComplete:1]
    // [stopReasonLen:4][stopReason:N][numBlocks:4][blockIds:4*N]
    // [numTokens:4][tokens:4*N][numEmbeds:4][embeddings:4*N]

    std::vector<uint8_t> data;

    // Helper to append data
    auto append = [&data](const void* ptr, size_t len) {
        const size_t offset = data.size();
        data.resize(offset + len);
        std::memcpy(data.data() + offset, ptr, len);
    };

    // Header
    append(&state.sequenceId, sizeof(state.sequenceId));
    append(&state.currentLength, sizeof(state.currentLength));
    append(&state.promptLength, sizeof(state.promptLength));

    uint8_t completeFlag = state.isComplete ? 1 : 0;
    append(&completeFlag, sizeof(completeFlag));

    // Stop reason
    uint32_t reasonLen = static_cast<uint32_t>(state.stopReason.size());
    append(&reasonLen, sizeof(reasonLen));
    append(state.stopReason.data(), state.stopReason.size());

    // KV blocks
    uint32_t numBlocks = static_cast<uint32_t>(state.kvBlocks.size());
    append(&numBlocks, sizeof(numBlocks));
    for (auto blockId : state.kvBlocks) {
        append(&blockId, sizeof(blockId));
    }

    // Generated tokens
    uint32_t numTokens = static_cast<uint32_t>(state.generatedTokens.size());
    append(&numTokens, sizeof(numTokens));
    for (auto token : state.generatedTokens) {
        append(&token, sizeof(token));
    }

    // Prompt embeddings (if cached)
    uint32_t numEmbeds = static_cast<uint32_t>(state.cachedPromptEmbeddings.size());
    append(&numEmbeds, sizeof(numEmbeds));
    if (numEmbeds > 0) {
        append(state.cachedPromptEmbeddings.data(),
               numEmbeds * sizeof(float));
    }

    return data;
}

std::unique_ptr<SequenceState> SequenceState::deserialize(
    const std::vector<uint8_t>& data,
    std::shared_ptr<PagedKVCache> kvCache) {

    if (data.size() < 25) {  // Minimum size for header
        throw std::runtime_error("Invalid serialized data: too short");
    }

    auto state = std::make_unique<SequenceState>(std::move(kvCache));

    size_t offset = 0;

    // Helper to read data
    auto read = [&data, &offset](void* dest, size_t len) {
        if (offset + len > data.size()) {
            throw std::runtime_error("Invalid serialized data: read past end");
        }
        std::memcpy(dest, data.data() + offset, len);
        offset += len;
    };

    // Header
    State reconstructed;
    read(&reconstructed.sequenceId, sizeof(reconstructed.sequenceId));
    read(&reconstructed.currentLength, sizeof(reconstructed.currentLength));
    read(&reconstructed.promptLength, sizeof(reconstructed.promptLength));

    uint8_t completeFlag;
    read(&completeFlag, sizeof(completeFlag));
    reconstructed.isComplete = (completeFlag != 0);

    // Stop reason
    uint32_t reasonLen;
    read(&reasonLen, sizeof(reasonLen));
    if (reasonLen > 0) {
        if (offset + reasonLen > data.size()) {
            throw std::runtime_error("Invalid serialized data: invalid stop reason length");
        }
        reconstructed.stopReason.resize(reasonLen);
        read(reconstructed.stopReason.data(), reasonLen);
    }

    // KV blocks
    uint32_t numBlocks;
    read(&numBlocks, sizeof(numBlocks));
    reconstructed.kvBlocks.resize(numBlocks);
    for (uint32_t i = 0; i < numBlocks; ++i) {
        read(&reconstructed.kvBlocks[i], sizeof(PagedKVCache::BlockId));
    }

    // Generated tokens
    uint32_t numTokens;
    read(&numTokens, sizeof(numTokens));
    reconstructed.generatedTokens.resize(numTokens);
    for (uint32_t i = 0; i < numTokens; ++i) {
        read(&reconstructed.generatedTokens[i], sizeof(int32_t));
    }

    // Prompt embeddings
    uint32_t numEmbeds;
    read(&numEmbeds, sizeof(numEmbeds));
    if (numEmbeds > 0) {
        if (offset + numEmbeds * sizeof(float) > data.size()) {
            throw std::runtime_error("Invalid serialized data: invalid embeddings length");
        }
        reconstructed.cachedPromptEmbeddings.resize(numEmbeds);
        read(reconstructed.cachedPromptEmbeddings.data(),
             numEmbeds * sizeof(float));
    }

    // Insert into state map
    std::lock_guard<std::mutex> lock(state->mutex_);
    state->sequences_[reconstructed.sequenceId] = std::move(reconstructed);

    return state;
}

//==============================================================================
// Private Helpers
//==============================================================================

uint64_t SequenceState::generateSequenceId() {
    // Use atomic increment for unique IDs
    // Add randomness to prevent predictable IDs across restarts
    const uint64_t base = nextSequenceId_.fetch_add(1, std::memory_order_relaxed);
    const uint64_t random = rng_() & 0xFFFF;  // 16 bits of randomness
    return (base << 16) | random;
}

size_t SequenceState::calculateBlocksNeeded(size_t tokenCount) const {
    const size_t blockSize = kvCache_->getConfig().blockSize;
    return (tokenCount + blockSize - 1) / blockSize;
}

} // namespace runtime
} // namespace iron
