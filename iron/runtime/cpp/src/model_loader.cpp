// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file model_loader.cpp
 * @brief Implementation of thread-safe model loader with queuing
 *
 * This file implements the ThreadSafeModelLoader class for managing
 * concurrent model load requests. Key features:
 *
 * - Worker thread processes load requests sequentially from FIFO queue
 * - Duplicate detection prevents loading same model multiple times
 * - Reference counting tracks model usage for safe unloading
 * - Memory budget validation prevents OOM conditions
 * - Condition variables for efficient waiting
 *
 * THREAD SAFETY:
 * - All public methods are thread-safe
 * - Queue operations protected by mutex
 * - Condition variables signal load completion
 * - Atomic counters for lock-free status checks
 */

#include <algorithm>
#include <filesystem>
#include <iron/memory_budget.hpp>
#include <iron/model_loader.hpp>
#include <stdexcept>

namespace iron
{
namespace runtime
{

//==============================================================================
// Construction/Destruction
//==============================================================================

ThreadSafeModelLoader::ThreadSafeModelLoader(std::shared_ptr<MemoryBudget> memoryBudget, LoadCallback loadCallback)
    : memoryBudget_(std::move(memoryBudget)), loadCallback_(std::move(loadCallback))
{
    startWorker();
}

ThreadSafeModelLoader::~ThreadSafeModelLoader()
{
    stopWorker();
}

//==============================================================================
// Worker Thread Management
//==============================================================================

void ThreadSafeModelLoader::startWorker()
{
    stopping_ = false;
    workerThread_ = std::thread(&ThreadSafeModelLoader::processQueue, this);
}

void ThreadSafeModelLoader::stopWorker()
{
    {
        std::lock_guard<std::mutex> lock(queueMutex_);
        stopping_ = true;
    }
    loadComplete_.notify_one();

    if (workerThread_.joinable()) {
        workerThread_.join();
    }
}

void ThreadSafeModelLoader::processQueue()
{
    while (true) {
        std::string pathToLoad;

        // Wait for work
        {
            std::unique_lock<std::mutex> lock(queueMutex_);
            loadComplete_.wait(lock, [this] { return stopping_ || !loadQueue_.empty(); });

            if (stopping_ && loadQueue_.empty()) {
                return; // Shutdown requested and no more work
            }

            if (!loadQueue_.empty()) {
                pathToLoad = loadQueue_.front();
                loadQueue_.pop();
                processing_.store(true, std::memory_order_relaxed);
            }
        }

        // Load outside the lock (may take time)
        if (!pathToLoad.empty()) {
            loadInternal(pathToLoad);

            // Notify waiters that load completed
            {
                std::lock_guard<std::mutex> lock(queueMutex_);
                processing_.store(false, std::memory_order_relaxed);
            }
            loadComplete_.notify_all();
        }
    }
}

//==============================================================================
// Public API - Model Loading
//==============================================================================

ThreadSafeModelLoader::LoadResult ThreadSafeModelLoader::load(const std::string &path)
{
    if (path.empty()) {
        return LoadResult{false, nullptr, "Empty model path", false};
    }

    // Fast path: check if already loaded and ready
    {
        std::lock_guard<std::mutex> lock(queueMutex_);
        auto it = loadedModels_.find(path);
        if (it != loadedModels_.end() && it->second->isReady()) {
            it->second->referenceCount.fetch_add(1, std::memory_order_relaxed);
            return LoadResult{true, it->second, "", true};
        }

        // Check if already loading - wait for it
        if (it != loadedModels_.end() && it->second->isLoading) {
            // Release lock before waiting
        }
    }

    // Check if we need to queue the load
    bool needToQueue = false;
    {
        std::lock_guard<std::mutex> lock(queueMutex_);
        auto it = loadedModels_.find(path);
        if (it == loadedModels_.end() || !it->second->isLoading) {
            // Not currently loading, add to queue
            loadQueue_.push(path);
            pendingLoads_.fetch_add(1, std::memory_order_relaxed);
            needToQueue = true;

            // Create placeholder entry
            if (it == loadedModels_.end()) {
                auto model = std::make_shared<LoadedModel>();
                model->path = path;
                model->isLoading = true;
                loadedModels_[path] = model;
            } else {
                it->second->isLoading = true;
            }
        }
    }

    if (needToQueue) {
        loadComplete_.notify_one();
    }

    // Wait for loading to complete
    return waitForLoading(path);
}

ThreadSafeModelLoader::LoadResult ThreadSafeModelLoader::waitForLoading(const std::string &path)
{
    // Poll for completion
    while (true) {
        std::this_thread::sleep_for(std::chrono::milliseconds(10));

        std::lock_guard<std::mutex> lock(queueMutex_);
        auto it = loadedModels_.find(path);

        if (it == loadedModels_.end()) {
            // Model was removed while waiting
            return LoadResult{false, nullptr, "Model removed during load", false};
        }

        if (it->second->isReady()) {
            it->second->referenceCount.fetch_add(1, std::memory_order_relaxed);
            return LoadResult{true, it->second, "", false};
        }

        if (!it->second->errorMessage.empty()) {
            return LoadResult{false, nullptr, it->second->errorMessage, false};
        }

        // Check if still in queue (not yet being processed)
        // Note: std::queue doesn't support iteration in C++17, so we use a simple heuristic
        bool stillInQueue = !processing_.load(std::memory_order_relaxed);

        // If not in queue and not processing, something went wrong
        if (!stillInQueue && !processing_.load(std::memory_order_relaxed)) {
            if (it->second->errorMessage.empty() && !it->second->isReady()) {
                // Edge case: load was skipped somehow
                return LoadResult{false, nullptr, "Load was skipped", false};
            }
        }
    }
}

std::shared_ptr<ThreadSafeModelLoader::LoadedModel> ThreadSafeModelLoader::getLoadedModel(const std::string &path) const
{
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it != loadedModels_.end() && it->second->isReady()) {
        return it->second;
    }
    return nullptr;
}

bool ThreadSafeModelLoader::isLoaded(const std::string &path) const
{
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    return it != loadedModels_.end() && it->second->isReady();
}

bool ThreadSafeModelLoader::unload(const std::string &path)
{
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it == loadedModels_.end()) {
        return false;
    }

    if (it->second->referenceCount.load(std::memory_order_relaxed) > 0) {
        return false; // Still in use
    }

    loadedModels_.erase(it);
    return true;
}

std::vector<std::string> ThreadSafeModelLoader::getLoadedModels() const
{
    std::lock_guard<std::mutex> lock(queueMutex_);
    std::vector<std::string> models;
    models.reserve(loadedModels_.size());
    for (const auto &[path, model] : loadedModels_) {
        if (model->isReady()) {
            models.push_back(path);
        }
    }
    return models;
}

size_t ThreadSafeModelLoader::getPendingLoadCount() const
{
    return pendingLoads_.load(std::memory_order_relaxed);
}

//==============================================================================
// Reference Counting
//==============================================================================

void ThreadSafeModelLoader::incrementReference(const std::string &path)
{
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it != loadedModels_.end()) {
        it->second->referenceCount.fetch_add(1, std::memory_order_relaxed);
    }
}

void ThreadSafeModelLoader::decrementReference(const std::string &path)
{
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it != loadedModels_.end()) {
        it->second->referenceCount.fetch_sub(1, std::memory_order_relaxed);
    }
}

int ThreadSafeModelLoader::getReferenceCount(const std::string &path) const
{
    std::lock_guard<std::mutex> lock(queueMutex_);
    auto it = loadedModels_.find(path);
    if (it != loadedModels_.end()) {
        return it->second->referenceCount.load(std::memory_order_relaxed);
    }
    return 0;
}

//==============================================================================
// Internal Methods
//==============================================================================

ThreadSafeModelLoader::LoadResult ThreadSafeModelLoader::loadInternal(const std::string &path)
{
    // Double-check if already loaded (could have been loaded while queued)
    {
        std::lock_guard<std::mutex> lock(queueMutex_);
        auto it = loadedModels_.find(path);
        if (it != loadedModels_.end() && it->second->isReady()) {
            pendingLoads_.fetch_sub(1, std::memory_order_relaxed);
            return LoadResult{true, it->second, "", true};
        }
    }

    // Validate memory budget if available
    if (memoryBudget_) {
        // Estimate model size from file
        size_t estimatedSize = 0;
        try {
            estimatedSize = std::filesystem::file_size(path);
        } catch (const std::filesystem::filesystem_error &e) {
            std::lock_guard<std::mutex> lock(queueMutex_);
            loadedModels_[path]->errorMessage = std::string("Cannot access model file: ") + e.what();
            loadedModels_[path]->isLoading = false;
            pendingLoads_.fetch_sub(1, std::memory_order_relaxed);
            return LoadResult{false, nullptr, loadedModels_[path]->errorMessage, false};
        }

        // Validate with rough estimates for KV cache and activations
        auto result = memoryBudget_->validateModelLoad(estimatedSize,
                                                       estimatedSize / 4, // Rough estimate for KV cache
                                                       estimatedSize / 8  // Rough estimate for activations
        );

        if (!result.success) {
            std::lock_guard<std::mutex> lock(queueMutex_);
            loadedModels_[path]->errorMessage = result.errorMessage;
            loadedModels_[path]->isLoading = false;
            pendingLoads_.fetch_sub(1, std::memory_order_relaxed);
            return LoadResult{false, nullptr, result.errorMessage, false};
        }
    }

    // Load the model via callback
    if (!loadCallback_) {
        std::lock_guard<std::mutex> lock(queueMutex_);
        loadedModels_[path]->errorMessage = "No load callback configured";
        loadedModels_[path]->isLoading = false;
        pendingLoads_.fetch_sub(1, std::memory_order_relaxed);
        return LoadResult{false, nullptr, "No load callback configured", false};
    }

    try {
        auto loadedModel = loadCallback_(path);
        {
            std::lock_guard<std::mutex> lock(queueMutex_);
            // Copy individual fields (LoadedModel is not copyable due to atomic)
            loadedModels_[path]->session = loadedModel->session;
            loadedModels_[path]->memoryUsage = loadedModel->memoryUsage;
            loadedModels_[path]->errorMessage = loadedModel->errorMessage;
            loadedModels_[path]->isLoading = false;
        }
        pendingLoads_.fetch_sub(1, std::memory_order_relaxed);
        return LoadResult{true, loadedModels_[path], "", false};
    } catch (const std::exception &e) {
        std::lock_guard<std::mutex> lock(queueMutex_);
        loadedModels_[path]->errorMessage = e.what();
        loadedModels_[path]->isLoading = false;
        pendingLoads_.fetch_sub(1, std::memory_order_relaxed);
        return LoadResult{false, nullptr, e.what(), false};
    }
}

} // namespace runtime
} // namespace iron
