// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file test_model_loader.cpp
 * @brief Unit tests for ThreadSafeModelLoader class
 *
 * This test suite validates the model loader implementation:
 * - Thread-safe loading with queuing
 * - Duplicate detection and caching
 * - Reference counting
 * - Memory budget validation
 * - Concurrent load requests
 *
 * @note Uses Google Test framework
 */

#include <atomic>
#include <chrono>
#include <filesystem>
#include <gtest/gtest.h>
#include <iron/memory_budget.hpp>
#include <iron/model_loader.hpp>
#include <thread>
#include <vector>

using namespace iron::runtime;

namespace
{

//==============================================================================
// Test Fixtures
//==============================================================================

/**
 * @brief Test fixture for ThreadSafeModelLoader tests
 */
class ModelLoaderTest : public ::testing::Test
{
  protected:
    /**
     * @brief Create a simple load callback for testing
     */
    ThreadSafeModelLoader::LoadCallback createMockLoadCallback()
    {
        return [](const std::string &path) -> std::shared_ptr<ThreadSafeModelLoader::LoadedModel> {
            auto model = std::make_shared<ThreadSafeModelLoader::LoadedModel>();
            model->path = path;
            // Create a dummy session (just a non-null pointer)
            model->session =
                std::shared_ptr<void>(static_cast<void *>(new int(42)), [](void *p) { delete static_cast<int *>(p); });
            model->memoryUsage = 1024;
            return model;
        };
    }

    /**
     * @brief Create a slow load callback for testing concurrency
     */
    ThreadSafeModelLoader::LoadCallback createSlowLoadCallback(int delayMs = 100)
    {
        return [delayMs](const std::string &path) -> std::shared_ptr<ThreadSafeModelLoader::LoadedModel> {
            std::this_thread::sleep_for(std::chrono::milliseconds(delayMs));
            auto model = std::make_shared<ThreadSafeModelLoader::LoadedModel>();
            model->path = path;
            model->session =
                std::shared_ptr<void>(static_cast<void *>(new int(42)), [](void *p) { delete static_cast<int *>(p); });
            return model;
        };
    }

    /**
     * @brief Create a failing load callback
     */
    ThreadSafeModelLoader::LoadCallback createFailingLoadCallback()
    {
        return [](const std::string &path) -> std::shared_ptr<ThreadSafeModelLoader::LoadedModel> {
            throw std::runtime_error("Simulated load failure");
        };
    }
};

//==============================================================================
// Construction Tests
//==============================================================================

TEST_F(ModelLoaderTest, Construction)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());
    EXPECT_EQ(loader.getPendingLoadCount(), 0);
    EXPECT_FALSE(loader.isProcessing());
}

TEST_F(ModelLoaderTest, ConstructionWithMemoryBudget)
{
    auto budget = std::make_shared<MemoryBudget>();
    ThreadSafeModelLoader loader(budget, createMockLoadCallback());
    EXPECT_NE(loader.getPendingLoadCount(), 0); // Will be 0 after construction
}

//==============================================================================
// Basic Loading Tests
//==============================================================================

TEST_F(ModelLoaderTest, LoadModel)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    auto result = loader.load("/path/to/model");
    EXPECT_TRUE(result.success);
    EXPECT_NE(result.model, nullptr);
    EXPECT_FALSE(result.wasCached);
    EXPECT_TRUE(result.errorMessage.empty());
}

TEST_F(ModelLoaderTest, LoadModelWithEmptyPath)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    auto result = loader.load("");
    EXPECT_FALSE(result.success);
    EXPECT_FALSE(result.errorMessage.empty());
}

TEST_F(ModelLoaderTest, LoadModelNoCallback)
{
    ThreadSafeModelLoader loader(nullptr, nullptr);

    auto result = loader.load("/path/to/model");
    EXPECT_FALSE(result.success);
    EXPECT_EQ(result.errorMessage, "No load callback configured");
}

//==============================================================================
// Caching Tests
//==============================================================================

TEST_F(ModelLoaderTest, LoadCachedModel)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    // First load
    auto result1 = loader.load("/path/to/model");
    EXPECT_TRUE(result1.success);
    EXPECT_FALSE(result1.wasCached);

    // Second load (should be cached)
    auto result2 = loader.load("/path/to/model");
    EXPECT_TRUE(result2.success);
    EXPECT_TRUE(result2.wasCached);

    // Should be the same model instance
    EXPECT_EQ(result1.model, result2.model);
}

TEST_F(ModelLoaderTest, IsLoaded)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    EXPECT_FALSE(loader.isLoaded("/path/to/model"));

    loader.load("/path/to/model");

    EXPECT_TRUE(loader.isLoaded("/path/to/model"));
}

TEST_F(ModelLoaderTest, GetLoadedModel)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    EXPECT_EQ(loader.getLoadedModel("/path/to/model"), nullptr);

    loader.load("/path/to/model");

    auto model = loader.getLoadedModel("/path/to/model");
    EXPECT_NE(model, nullptr);
    EXPECT_EQ(model->path, "/path/to/model");
}

TEST_F(ModelLoaderTest, GetLoadedModels)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    loader.load("/path/to/model1");
    loader.load("/path/to/model2");
    loader.load("/path/to/model3");

    auto models = loader.getLoadedModels();
    EXPECT_EQ(models.size(), 3);
    EXPECT_TRUE(std::find(models.begin(), models.end(), "/path/to/model1") != models.end());
    EXPECT_TRUE(std::find(models.begin(), models.end(), "/path/to/model2") != models.end());
    EXPECT_TRUE(std::find(models.begin(), models.end(), "/path/to/model3") != models.end());
}

//==============================================================================
// Unloading Tests
//==============================================================================

TEST_F(ModelLoaderTest, UnloadModel)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    loader.load("/path/to/model");
    EXPECT_TRUE(loader.isLoaded("/path/to/model"));

    // Need to decrement reference count to 0 before unloading
    loader.decrementReference("/path/to/model");
    loader.decrementReference("/path/to/model"); // Initial load adds 1, get adds 1

    EXPECT_TRUE(loader.unload("/path/to/model"));
    EXPECT_FALSE(loader.isLoaded("/path/to/model"));
}

TEST_F(ModelLoaderTest, UnloadModelStillInUse)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    loader.load("/path/to/model");

    // Still in use (reference count > 0)
    EXPECT_FALSE(loader.unload("/path/to/model"));
}

TEST_F(ModelLoaderTest, UnloadNotLoadedModel)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    EXPECT_FALSE(loader.unload("/path/to/nonexistent"));
}

//==============================================================================
// Reference Counting Tests
//==============================================================================

TEST_F(ModelLoaderTest, IncrementReference)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    loader.load("/path/to/model");
    int initialRef = loader.getReferenceCount("/path/to/model");

    loader.incrementReference("/path/to/model");
    EXPECT_EQ(loader.getReferenceCount("/path/to/model"), initialRef + 1);
}

TEST_F(ModelLoaderTest, DecrementReference)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    loader.load("/path/to/model");
    int initialRef = loader.getReferenceCount("/path/to/model");

    loader.decrementReference("/path/to/model");
    EXPECT_EQ(loader.getReferenceCount("/path/to/model"), initialRef - 1);
}

TEST_F(ModelLoaderTest, GetReferenceCountForNonExistentModel)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    EXPECT_EQ(loader.getReferenceCount("/path/to/nonexistent"), 0);
}

//==============================================================================
// Concurrent Loading Tests
//==============================================================================

TEST_F(ModelLoaderTest, ConcurrentLoadsSameModel)
{
    ThreadSafeModelLoader loader(nullptr, createSlowLoadCallback(50));

    std::atomic<int> successCount{0};
    std::vector<std::thread> threads;

    auto loadTask = [&]() {
        auto result = loader.load("/path/to/model");
        if (result.success) {
            successCount.fetch_add(1, std::memory_order_relaxed);
        }
    };

    // Start multiple concurrent loads for the same model
    for (int i = 0; i < 4; ++i) {
        threads.emplace_back(loadTask);
    }

    for (auto &t : threads) {
        t.join();
    }

    // All should succeed and get the same cached model
    EXPECT_EQ(successCount.load(), 4);
    EXPECT_EQ(loader.getReferenceCount("/path/to/model"), 4);
}

TEST_F(ModelLoaderTest, ConcurrentLoadsDifferentModels)
{
    ThreadSafeModelLoader loader(nullptr, createSlowLoadCallback(20));

    std::atomic<int> successCount{0};
    std::vector<std::thread> threads;
    const std::vector<std::string> modelPaths = {
        "/path/to/model1", "/path/to/model2", "/path/to/model3", "/path/to/model4"};

    auto loadTask = [&](const std::string &path) {
        auto result = loader.load(path);
        if (result.success) {
            successCount.fetch_add(1, std::memory_order_relaxed);
        }
    };

    for (const auto &path : modelPaths) {
        threads.emplace_back(loadTask, path);
    }

    for (auto &t : threads) {
        t.join();
    }

    // All should succeed
    EXPECT_EQ(successCount.load(), 4);
    EXPECT_EQ(loader.getLoadedModels().size(), 4);
}

TEST_F(ModelLoaderTest, LoadQueueOrder)
{
    ThreadSafeModelLoader loader(nullptr, createSlowLoadCallback(10));

    // Queue multiple loads
    std::vector<std::thread> threads;
    std::atomic<int> completed{0};

    auto loadTask = [&](int id) {
        loader.load("/path/to/model" + std::to_string(id));
        completed.fetch_add(1, std::memory_order_relaxed);
    };

    // Start loads in order
    for (int i = 0; i < 4; ++i) {
        threads.emplace_back(loadTask, i);
    }

    for (auto &t : threads) {
        t.join();
    }

    // All should complete
    EXPECT_EQ(completed.load(), 4);
}

//==============================================================================
// Memory Budget Validation Tests
//==============================================================================

TEST_F(ModelLoaderTest, LoadWithMemoryBudgetValidation)
{
    auto budget = std::make_shared<MemoryBudget>();
    ThreadSafeModelLoader loader(budget, createMockLoadCallback());

    // Mock callback uses 1024 bytes, which should fit in budget
    auto result = loader.load("/path/to/model");
    EXPECT_TRUE(result.success);
}

TEST_F(ModelLoaderTest, LoadFailsWithInsufficientBudget)
{
    // Create very restrictive budget
    MemoryBudget::Limits limits;
    limits.totalBudget = 100; // 100 bytes total
    limits.weightBudget = 50;
    limits.kvCacheBudget = 20;
    limits.activationBudget = 20;
    limits.headroom = 10;

    auto budget = std::make_shared<MemoryBudget>(limits);
    ThreadSafeModelLoader loader(budget, createMockLoadCallback());

    // Mock callback reports 1024 bytes, which exceeds budget
    auto result = loader.load("/path/to/large_model");
    EXPECT_FALSE(result.success);
    EXPECT_FALSE(result.errorMessage.empty());
}

//==============================================================================
// Error Handling Tests
//==============================================================================

TEST_F(ModelLoaderTest, LoadWithFailingCallback)
{
    ThreadSafeModelLoader loader(nullptr, createFailingLoadCallback());

    auto result = loader.load("/path/to/model");
    EXPECT_FALSE(result.success);
    EXPECT_EQ(result.errorMessage, "Simulated load failure");
}

TEST_F(ModelLoaderTest, LoadResultGetOrThrow)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    auto result = loader.load("/path/to/model");
    EXPECT_NO_THROW(result.getOrThrow());
}

TEST_F(ModelLoaderTest, LoadResultGetOrThrowFails)
{
    ThreadSafeModelLoader loader(nullptr, createFailingLoadCallback());

    auto result = loader.load("/path/to/model");
    EXPECT_THROW(result.getOrThrow(), std::runtime_error);
}

//==============================================================================
// Stress Tests
//==============================================================================

TEST_F(ModelLoaderTest, StressManyLoads)
{
    ThreadSafeModelLoader loader(nullptr, createMockLoadCallback());

    const int numLoads = 50;
    std::vector<std::thread> threads;

    auto loadTask = [&](int id) {
        loader.load("/path/to/model" + std::to_string(id % 10)); // Reuse 10 models
    };

    for (int i = 0; i < numLoads; ++i) {
        threads.emplace_back(loadTask, i);
    }

    for (auto &t : threads) {
        t.join();
    }

    // Should have 10 unique models loaded
    EXPECT_EQ(loader.getLoadedModels().size(), 10);
}

} // anonymous namespace
