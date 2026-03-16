// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file test_memory_budget.cpp
 * @brief Unit tests for MemoryBudget class
 *
 * This test suite validates the MemoryBudget implementation:
 * - Construction and validation
 * - Budget allocation and tracking
 * - Model load validation
 * - KV cache allocation checks
 * - Thread safety under concurrent access
 *
 * @note Uses Google Test framework
 */

#include <iron/memory_budget.hpp>
#include <gtest/gtest.h>
#include <thread>
#include <vector>
#include <atomic>

using namespace iron::runtime;

namespace {

//==============================================================================
// Test Fixtures
//==============================================================================

/**
 * @brief Test fixture for MemoryBudget tests
 */
class MemoryBudgetTest : public ::testing::Test {
protected:
    MemoryBudget::Limits createTestLimits() {
        MemoryBudget::Limits limits;
        limits.totalBudget = 256 * 1024 * 1024;      // 256 MB total
        limits.weightBudget = 128 * 1024 * 1024;     // 128 MB weights
        limits.kvCacheBudget = 64 * 1024 * 1024;     // 64 MB KV cache
        limits.activationBudget = 32 * 1024 * 1024;  // 32 MB activations
        limits.headroom = 32 * 1024 * 1024;          // 32 MB headroom
        return limits;
    }
};

//==============================================================================
// Construction Tests
//==============================================================================

TEST_F(MemoryBudgetTest, ConstructionWithDefaults) {
    MemoryBudget budget;
    EXPECT_EQ(budget.getTotalBudget(), 4ULL * 1024 * 1024 * 1024);  // 4 GB
    EXPECT_EQ(budget.getTotalUsage(), 0);
    EXPECT_NEAR(budget.getUtilizationPercentage(), 0.0, 0.001);
}

TEST_F(MemoryBudgetTest, ConstructionWithCustomLimits) {
    auto limits = createTestLimits();
    MemoryBudget budget(limits);
    EXPECT_EQ(budget.getTotalBudget(), limits.totalBudget);
}

TEST_F(MemoryBudgetTest, ConstructionWithInvalidLimits) {
    MemoryBudget::Limits limits;
    limits.totalBudget = 100;  // Too small
    limits.weightBudget = 1000;  // Exceeds total
    EXPECT_THROW(MemoryBudget(limits), std::invalid_argument);
}

//==============================================================================
// Budget Query Tests
//==============================================================================

TEST_F(MemoryBudgetTest, GetRemainingBudget) {
    auto limits = createTestLimits();
    MemoryBudget budget(limits);

    EXPECT_EQ(budget.getRemainingBudget(MemoryBudget::Component::WEIGHTS),
              limits.weightBudget);
    EXPECT_EQ(budget.getRemainingBudget(MemoryBudget::Component::KV_CACHE),
              limits.kvCacheBudget);
    EXPECT_EQ(budget.getRemainingBudget(MemoryBudget::Component::ACTIVATIONS),
              limits.activationBudget);
}

TEST_F(MemoryBudgetTest, GetUtilizationPercentage) {
    MemoryBudget budget;

    // Initial utilization should be 0
    EXPECT_NEAR(budget.getUtilizationPercentage(), 0.0, 0.001);

    // Allocate some memory
    void* ptr = budget.allocateWithBudget(1024, MemoryBudget::Component::MISC);
    ASSERT_NE(ptr, nullptr);

    double expected = (1024.0 / static_cast<double>(budget.getTotalBudget())) * 100.0;
    EXPECT_NEAR(budget.getUtilizationPercentage(), expected, 0.001);

    budget.freeWithBudget(ptr, 1024, MemoryBudget::Component::MISC);
}

//==============================================================================
// Allocation Tests
//==============================================================================

TEST_F(MemoryBudgetTest, AllocateWithBudget) {
    MemoryBudget budget;

    void* ptr = budget.allocateWithBudget(1024, MemoryBudget::Component::MISC);
    ASSERT_NE(ptr, nullptr);
    EXPECT_EQ(budget.getCurrentUsage(MemoryBudget::Component::MISC), 1024);

    budget.freeWithBudget(ptr, 1024, MemoryBudget::Component::MISC);
    EXPECT_EQ(budget.getCurrentUsage(MemoryBudget::Component::MISC), 0);
}

TEST_F(MemoryBudgetTest, AllocateExceedsBudget) {
    auto limits = createTestLimits();
    MemoryBudget budget(limits);

    // Try to allocate more than available
    void* ptr = budget.allocateWithBudget(limits.weightBudget + 1,
                                           MemoryBudget::Component::WEIGHTS);
    EXPECT_EQ(ptr, nullptr);
}

TEST_F(MemoryBudgetTest, AllocateZeroBytes) {
    MemoryBudget budget;
    void* ptr = budget.allocateWithBudget(0, MemoryBudget::Component::MISC);
    EXPECT_EQ(ptr, nullptr);  // Null for zero allocation
}

TEST_F(MemoryBudgetTest, AllocateFreeCycle) {
    MemoryBudget budget;
    const size_t allocSize = 4096;
    const int numCycles = 100;

    for (int i = 0; i < numCycles; ++i) {
        void* ptr = budget.allocateWithBudget(allocSize,
                                               MemoryBudget::Component::MISC);
        ASSERT_NE(ptr, nullptr);
        budget.freeWithBudget(ptr, allocSize, MemoryBudget::Component::MISC);
    }

    // Usage should be back to zero
    EXPECT_EQ(budget.getTotalUsage(), 0);
}

//==============================================================================
// Model Load Validation Tests
//==============================================================================

TEST_F(MemoryBudgetTest, ValidateModelLoadSuccess) {
    MemoryBudget budget;

    auto result = budget.validateModelLoad(
        1024 * 1024 * 1024,  // 1 GB weights
        512 * 1024 * 1024,   // 512 MB KV cache
        256 * 1024 * 1024    // 256 MB activations
    );

    EXPECT_TRUE(result.success);
    EXPECT_TRUE(result.errorMessage.empty());
}

TEST_F(MemoryBudgetTest, ValidateModelLoadExceedsWeightBudget) {
    MemoryBudget budget;

    auto result = budget.validateModelLoad(
        3 * 1024 * 1024 * 1024,  // 3 GB weights (exceeds 2 GB budget)
        512 * 1024 * 1024,
        256 * 1024 * 1024
    );

    EXPECT_FALSE(result.success);
    EXPECT_FALSE(result.errorMessage.empty());
    EXPECT_EQ(result.requestedSize, 3ULL * 1024 * 1024 * 1024);
}

TEST_F(MemoryBudgetTest, ValidateModelLoadExceedsKVCacheBudget) {
    MemoryBudget budget;

    auto result = budget.validateModelLoad(
        1024 * 1024 * 1024,
        2 * 1024 * 1024 * 1024,  // 2 GB KV cache (exceeds 1 GB budget)
        256 * 1024 * 1024
    );

    EXPECT_FALSE(result.success);
    EXPECT_NE(result.errorMessage.find("KV cache"), std::string::npos);
}

TEST_F(MemoryBudgetTest, ValidateModelLoadExceedsTotalBudget) {
    MemoryBudget budget;

    // Individual budgets OK, but total exceeds
    auto result = budget.validateModelLoad(
        2 * 1024 * 1024 * 1024,   // 2 GB weights (at limit)
        1024 * 1024 * 1024,       // 1 GB KV cache
        512 * 1024 * 1024 + 1     // Just over remaining
    );

    EXPECT_FALSE(result.success);
}

//==============================================================================
// KV Cache Allocation Tests
//==============================================================================

TEST_F(MemoryBudgetTest, CanAllocateKV) {
    MemoryBudget budget;

    // Llama3.2-1B config: 16 layers, 32 heads, 64 dim, 2048 seq len
    bool canAlloc = budget.canAllocateKV(
        2048,  // sequence length
        1,     // batch size
        16,    // num layers
        32,    // num heads
        64     // head dim
    );

    EXPECT_TRUE(canAlloc);
}

TEST_F(MemoryBudgetTest, CanAllocateKVLargeBatch) {
    MemoryBudget budget;

    // Large batch should fail
    bool canAlloc = budget.canAllocateKV(
        2048,  // sequence length
        32,    // large batch size
        16,
        32,
        64
    );

    EXPECT_FALSE(canAlloc);
}

TEST_F(MemoryBudgetTest, CalculateKVCacheMemory) {
    // Verify the helper function
    size_t memory = calculateKVCacheMemory(
        32,    // 1 block
        1,
        1,
        1,
        64,
        32     // block size
    );

    // 2 (k+v) * 1 layer * 1 head * 32 tokens * 64 dim * 4 bytes
    size_t expected = 2 * 1 * 1 * 32 * 64 * sizeof(float);
    EXPECT_EQ(memory, expected);
}

//==============================================================================
// Budget Reservation Tests
//==============================================================================

TEST_F(MemoryBudgetTest, ReserveBudget) {
    MemoryBudget budget;

    bool reserved = budget.reserveBudget(1024, MemoryBudget::Component::MISC);
    EXPECT_TRUE(reserved);
}

TEST_F(MemoryBudgetTest, ReserveBudgetExceedsLimit) {
    auto limits = createTestLimits();
    MemoryBudget budget(limits);

    bool reserved = budget.reserveBudget(limits.weightBudget + 1,
                                          MemoryBudget::Component::WEIGHTS);
    EXPECT_FALSE(reserved);
}

TEST_F(MemoryBudgetTest, ReleaseBudget) {
    MemoryBudget budget;

    budget.reserveBudget(1024, MemoryBudget::Component::MISC);
    budget.releaseBudget(1024, MemoryBudget::Component::MISC);
    // No crash = success for now
}

//==============================================================================
// Reset Tests
//==============================================================================

TEST_F(MemoryBudgetTest, Reset) {
    MemoryBudget budget;

    // Allocate some memory
    void* ptr1 = budget.allocateWithBudget(1024, MemoryBudget::Component::WEIGHTS);
    void* ptr2 = budget.allocateWithBudget(2048, MemoryBudget::Component::KV_CACHE);

    EXPECT_EQ(budget.getTotalUsage(), 3072);

    budget.reset();
    EXPECT_EQ(budget.getTotalUsage(), 0);

    // Note: We don't free the pointers - they leak but that's OK for this test
}

//==============================================================================
// Thread Safety Tests
//==============================================================================

TEST_F(MemoryBudgetTest, ConcurrentAllocations) {
    MemoryBudget budget;
    const int numThreads = 8;
    const size_t allocSize = 1024;
    std::atomic<int> successCount{0};
    std::atomic<int> failCount{0};

    auto allocateTask = [&]() {
        for (int i = 0; i < 100; ++i) {
            void* ptr = budget.allocateWithBudget(allocSize,
                                                   MemoryBudget::Component::MISC);
            if (ptr) {
                successCount.fetch_add(1, std::memory_order_relaxed);
                budget.freeWithBudget(ptr, allocSize,
                                       MemoryBudget::Component::MISC);
            } else {
                failCount.fetch_add(1, std::memory_order_relaxed);
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

    // All allocations should be freed
    EXPECT_EQ(budget.getCurrentUsage(MemoryBudget::Component::MISC), 0);

    // Some may have failed due to budget limits, which is OK
    EXPECT_GT(successCount.load(), 0);
}

TEST_F(MemoryBudgetTest, ConcurrentValidation) {
    MemoryBudget budget;
    const int numThreads = 8;
    std::atomic<int> validationCount{0};

    auto validateTask = [&]() {
        for (int i = 0; i < 100; ++i) {
            auto result = budget.validateModelLoad(
                100 * 1024 * 1024,
                50 * 1024 * 1024,
                25 * 1024 * 1024
            );
            (void)result;
            validationCount.fetch_add(1, std::memory_order_relaxed);
        }
    };

    std::vector<std::thread> threads;
    for (int i = 0; i < numThreads; ++i) {
        threads.emplace_back(validateTask);
    }

    for (auto& t : threads) {
        t.join();
    }

    EXPECT_EQ(validationCount.load(), numThreads * 100);
}

} // anonymous namespace
