// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file test_kv_cache.cpp
 * @brief Unit tests for PagedKVCache and SequenceState classes
 *
 * This test suite validates the KV cache implementation:
 * - Block allocation and deallocation
 * - Key/value read/write operations
 * - Contiguous block access
 * - Thread safety under concurrent access
 * - Sequence state management
 *
 * @note Uses Google Test framework
 */

#include <iron/kv_cache.hpp>
#include <iron/sequence_state.hpp>
#include <gtest/gtest.h>
#include <thread>
#include <vector>
#include <cstring>
#include <random>

using namespace iron::runtime;

namespace {

//==============================================================================
// PagedKVCache Test Fixture
//==============================================================================

/**
 * @brief Test fixture for PagedKVCache tests
 */
class PagedKVCacheTest : public ::testing::Test {
protected:
    PagedKVCache::Config createTestConfig() {
        PagedKVCache::Config config;
        config.blockSize = 32;
        config.maxBlocks = 64;
        config.numLayers = 2;   // Small for testing
        config.numHeads = 4;    // Small for testing
        config.headDim = 64;
        return config;
    }

    void fillVector(std::vector<float>& vec, float value) {
        std::fill(vec.begin(), vec.end(), value);
    }
};

//==============================================================================
// PagedKVCache Construction Tests
//==============================================================================

TEST_F(PagedKVCacheTest, Construction) {
    auto config = createTestConfig();
    PagedKVCache cache(config);

    EXPECT_EQ(cache.getTotalBlocks(), config.maxBlocks);
    EXPECT_EQ(cache.getAvailableBlocks(), config.maxBlocks);
    EXPECT_EQ(cache.getMemoryUsage(), config.totalBytes());
}

TEST_F(PagedKVCacheTest, ConstructionWithInvalidConfig) {
    PagedKVCache::Config config;
    config.blockSize = 0;  // Invalid
    EXPECT_THROW(PagedKVCache cache(config), std::invalid_argument);
}

TEST_F(PagedKVCacheTest, MoveConstruction) {
    auto config = createTestConfig();
    PagedKVCache cache1(config);
    cache1.allocateBlocks(10);

    PagedKVCache cache2(std::move(cache1));
    EXPECT_EQ(cache2.getTotalBlocks(), config.maxBlocks);
    EXPECT_EQ(cache2.getAvailableBlocks(), config.maxBlocks - 10);
}

TEST_F(PagedKVCacheTest, MoveAssignment) {
    auto config = createTestConfig();
    PagedKVCache cache1(config);
    cache1.allocateBlocks(10);

    PagedKVCache cache2(createTestConfig());
    cache2 = std::move(cache1);
    EXPECT_EQ(cache2.getAvailableBlocks(), config.maxBlocks - 10);
}

//==============================================================================
// PagedKVCache Block Allocation Tests
//==============================================================================

TEST_F(PagedKVCacheTest, BlockAllocation) {
    PagedKVCache cache(createTestConfig());

    auto blocks = cache.allocateBlocks(4);
    EXPECT_EQ(blocks.size(), 4);
    EXPECT_EQ(cache.getAvailableBlocks(), 60);

    cache.freeBlocks(blocks);
    EXPECT_EQ(cache.getAvailableBlocks(), 64);
}

TEST_F(PagedKVCacheTest, BlockAllocationExhaustion) {
    PagedKVCache cache(createTestConfig());

    // Allocate all blocks
    auto blocks = cache.allocateBlocks(64);
    EXPECT_EQ(blocks.size(), 64);
    EXPECT_EQ(cache.getAvailableBlocks(), 0);

    // Try to allocate more
    auto moreBlocks = cache.allocateBlocks(1);
    EXPECT_TRUE(moreBlocks.empty());

    cache.freeBlocks(blocks);
    EXPECT_EQ(cache.getAvailableBlocks(), 64);
}

TEST_F(PagedKVCacheTest, BlockAllocationPartialFailure) {
    PagedKVCache cache(createTestConfig());

    // Allocate most blocks
    auto blocks1 = cache.allocateBlocks(60);
    EXPECT_EQ(blocks1.size(), 60);

    // Try to allocate more than available
    auto blocks2 = cache.allocateBlocks(10);
    EXPECT_TRUE(blocks2.empty());  // Should fail and not allocate any

    // Original allocation should still be there
    EXPECT_EQ(cache.getAvailableBlocks(), 4);

    cache.freeBlocks(blocks1);
}

TEST_F(PagedKVCacheTest, CanAllocate) {
    PagedKVCache cache(createTestConfig());

    EXPECT_TRUE(cache.canAllocate(10));
    EXPECT_TRUE(cache.canAllocate(64));
    EXPECT_FALSE(cache.canAllocate(65));

    auto blocks = cache.allocateBlocks(50);
    EXPECT_TRUE(cache.canAllocate(14));
    EXPECT_FALSE(cache.canAllocate(15));

    cache.freeBlocks(blocks);
    EXPECT_TRUE(cache.canAllocate(64));
}

//==============================================================================
// PagedKVCache KV Operations Tests
//==============================================================================

TEST_F(PagedKVCacheTest, KVReadWrite) {
    PagedKVCache cache(createTestConfig());

    auto blocks = cache.allocateBlocks(1);
    ASSERT_EQ(blocks.size(), 1);

    // Write key
    std::vector<float> key(64, 1.5f);
    cache.writeKey(0, blocks[0], 0, 0, key.data());

    // Read key
    std::vector<float> readKey(64);
    std::vector<float> readValue(64);
    cache.readKeyValue(0, blocks[0], 0, 0, readKey.data(), readValue.data());

    EXPECT_EQ(key, readKey);
}

TEST_F(PagedKVCacheTest, KVWriteToUnallocatedBlock) {
    PagedKVCache cache(createTestConfig());

    std::vector<float> key(64, 1.0f);
    EXPECT_THROW(cache.writeKey(0, 0, 0, 0, key.data()), std::runtime_error);
}

TEST_F(PagedKVCacheTest, KVReadInvalidLayer) {
    PagedKVCache cache(createTestConfig());

    auto blocks = cache.allocateBlocks(1);
    std::vector<float> key(64), value(64);

    EXPECT_THROW(cache.readKeyValue(10, blocks[0], 0, 0, key.data(), value.data()),
                 std::out_of_range);
}

TEST_F(PagedKVCacheTest, KVWriteInvalidHead) {
    PagedKVCache cache(createTestConfig());

    auto blocks = cache.allocateBlocks(1);
    std::vector<float> key(64, 1.0f);

    EXPECT_THROW(cache.writeKey(0, blocks[0], 0, 10, key.data()),
                 std::out_of_range);
}

TEST_F(PagedKVCacheTest, KVWriteInvalidOffset) {
    PagedKVCache cache(createTestConfig());

    auto blocks = cache.allocateBlocks(1);
    std::vector<float> key(64, 1.0f);

    // Offset >= blockSize is invalid
    EXPECT_THROW(cache.writeKey(0, blocks[0], 32, 0, key.data()),
                 std::out_of_range);
}

//==============================================================================
// PagedKVCache Contiguous Block Tests
//==============================================================================

TEST_F(PagedKVCacheTest, GetContiguousBlocks) {
    PagedKVCache cache(createTestConfig());

    auto blocks = cache.allocateBlocks(4);
    ASSERT_EQ(blocks.size(), 4);

    // Write different values to each block
    for (size_t i = 0; i < 4; ++i) {
        std::vector<float> key(64, static_cast<float>(i + 1));
        cache.writeKey(0, blocks[i], 0, 0, key.data());
    }

    // Read contiguous blocks
    const size_t elementsPerBlock = 32 * 64;  // blockSize * headDim
    std::vector<float> outKeys(4 * elementsPerBlock);
    std::vector<float> outValues(4 * elementsPerBlock);

    cache.getContiguousBlocks(0, blocks[0], 4, 0,
                               outKeys.data(), outValues.data());

    // Verify first block's keys
    for (size_t i = 0; i < 64; ++i) {
        EXPECT_FLOAT_EQ(outKeys[i], 1.0f);
    }

    // Verify second block's keys (after first blockSize tokens)
    for (size_t i = 0; i < 64; ++i) {
        EXPECT_FLOAT_EQ(outKeys[elementsPerBlock + i], 2.0f);
    }
}

TEST_F(PagedKVCacheTest, GetContiguousBlocksOutOfRange) {
    PagedKVCache cache(createTestConfig());

    std::vector<float> keys(100), values(100);
    EXPECT_THROW(cache.getContiguousBlocks(0, 0, 100, 0, keys.data(), values.data()),
                 std::out_of_range);
}

//==============================================================================
// PagedKVCache Thread Safety Tests
//==============================================================================

TEST_F(PagedKVCacheTest, ConcurrentAllocations) {
    PagedKVCache cache(createTestConfig());
    const int numThreads = 8;
    std::atomic<int> successCount{0};
    std::atomic<int> totalAllocated{0};

    auto allocateTask = [&]() {
        for (int i = 0; i < 10; ++i) {
            auto blocks = cache.allocateBlocks(1);
            if (!blocks.empty()) {
                successCount.fetch_add(1, std::memory_order_relaxed);
                totalAllocated.fetch_add(blocks.size(), std::memory_order_relaxed);
                cache.freeBlocks(blocks);
            }
        }
    };

    std::vector<std::thread> threads;
    for (int i = 0; i < numThreads; ++i) {
        threads.emplace_back(allocateTask);
    }

    for (auto& t : threads) {
        t.join();
    }

    // All blocks should be freed
    EXPECT_EQ(cache.getAvailableBlocks(), 64);
    EXPECT_GT(successCount.load(), 0);
}

TEST_F(PagedKVCacheTest, ConcurrentReadWrite) {
    PagedKVCache cache(createTestConfig());
    auto blocks = cache.allocateBlocks(10);
    const int numThreads = 4;

    auto writeTask = [&](int threadId) {
        for (int i = 0; i < 10; ++i) {
            std::vector<float> key(64, static_cast<float>(threadId * 100 + i));
            cache.writeKey(0, blocks[i % 10], 0, 0, key.data());
        }
    };

    std::vector<std::thread> threads;
    for (int i = 0; i < numThreads; ++i) {
        threads.emplace_back(writeTask, i);
    }

    for (auto& t : threads) {
        t.join();
    }

    // No crashes = thread safety maintained
    cache.freeBlocks(blocks);
}

//==============================================================================
// SequenceState Tests
//==============================================================================

/**
 * @brief Test fixture for SequenceState tests
 */
class SequenceStateTest : public ::testing::Test {
protected:
    std::shared_ptr<PagedKVCache> createTestKVCache() {
        PagedKVCache::Config config;
        config.blockSize = 32;
        config.maxBlocks = 100;
        config.numLayers = 2;
        config.numHeads = 4;
        config.headDim = 64;
        return std::make_shared<PagedKVCache>(config);
    }
};

TEST_F(SequenceStateTest, Construction) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);
    EXPECT_TRUE(state.getActiveSequences().empty());
}

TEST_F(SequenceStateTest, ConstructionWithNullCache) {
    EXPECT_THROW(SequenceState state(nullptr), std::invalid_argument);
}

TEST_F(SequenceStateTest, StartSequence) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    std::vector<int32_t> prompt = {1, 2, 3, 4, 5};
    uint64_t seqId = state.startSequence(prompt, 10);

    EXPECT_NE(seqId, 0);
    EXPECT_TRUE(state.hasSequence(seqId));
    EXPECT_EQ(state.getNextTokenPosition(seqId), 5);

    auto tokens = state.getGeneratedTokens(seqId);
    EXPECT_EQ(tokens.size(), 5);
    EXPECT_EQ(tokens, prompt);
}

TEST_F(SequenceStateTest, AppendToken) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    std::vector<int32_t> prompt = {1, 2, 3};
    uint64_t seqId = state.startSequence(prompt, 10);

    state.appendToken(seqId, 100);
    state.appendToken(seqId, 101);

    auto tokens = state.getGeneratedTokens(seqId);
    EXPECT_EQ(tokens.size(), 5);
    EXPECT_EQ(tokens[3], 100);
    EXPECT_EQ(tokens[4], 101);
}

TEST_F(SequenceStateTest, CompleteSequence) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    std::vector<int32_t> prompt = {1, 2, 3};
    uint64_t seqId = state.startSequence(prompt, 10);

    state.completeSequence(seqId, "eos_token");

    auto stateInfo = state.getState(seqId);
    EXPECT_TRUE(stateInfo.isComplete);
    EXPECT_EQ(stateInfo.stopReason, "eos_token");
}

TEST_F(SequenceStateTest, RemoveSequence) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    std::vector<int32_t> prompt = {1, 2, 3};
    uint64_t seqId = state.startSequence(prompt, 10);

    const size_t availableBefore = kvCache->getAvailableBlocks();
    state.removeSequence(seqId);

    EXPECT_FALSE(state.hasSequence(seqId));
    // Blocks should be freed
    EXPECT_EQ(kvCache->getAvailableBlocks(), availableBefore);
}

TEST_F(SequenceStateTest, AppendTokenToCompletedSequence) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    std::vector<int32_t> prompt = {1, 2, 3};
    uint64_t seqId = state.startSequence(prompt, 10);
    state.completeSequence(seqId, "eos_token");

    EXPECT_THROW(state.appendToken(seqId, 100), std::runtime_error);
}

TEST_F(SequenceStateTest, GetActiveSequences) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    uint64_t seq1 = state.startSequence({1, 2, 3}, 10);
    uint64_t seq2 = state.startSequence({4, 5}, 10);
    uint64_t seq3 = state.startSequence({6}, 10);

    state.completeSequence(seq2, "eos_token");

    auto active = state.getActiveSequences();
    EXPECT_EQ(active.size(), 2);
    EXPECT_TRUE(std::find(active.begin(), active.end(), seq1) != active.end());
    EXPECT_TRUE(std::find(active.begin(), active.end(), seq3) != active.end());
}

TEST_F(SequenceStateTest, SequenceStateInvalidSequenceId) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    EXPECT_THROW(state.getState(999), std::out_of_range);
    EXPECT_THROW(state.appendToken(999, 100), std::out_of_range);
    EXPECT_THROW(state.completeSequence(999, "test"), std::out_of_range);
    EXPECT_THROW(state.removeSequence(999), std::out_of_range);
}

TEST_F(SequenceStateTest, StartSequenceWithEmptyPrompt) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    EXPECT_THROW(state.startSequence({}, 10), std::invalid_argument);
}

TEST_F(SequenceStateTest, StartSequenceWithZeroMaxTokens) {
    auto kvCache = createTestKVCache();
    SequenceState state(kvCache);

    EXPECT_THROW(state.startSequence({1, 2, 3}, 0), std::invalid_argument);
}

} // anonymous namespace
