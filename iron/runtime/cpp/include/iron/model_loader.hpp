// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file model_loader.hpp
 * @brief Thread-safe model loader with request queuing
 *
 * This header defines the ThreadSafeModelLoader class for managing
 * concurrent model load requests safely.
 *
 * FEATURES:
 * - Sequential model loading (one model at a time)
 * - Request queue for concurrent load requests
 * - Duplicate detection (prevents loading same model twice)
 * - Reference counting for model usage tracking
 * - Memory budget validation before loading
 *
 * THREAD SAFETY:
 * - All public methods are thread-safe
 * - Load requests are queued and processed sequentially
 * - Duplicate requests return cached results
 *
 * USAGE PATTERN:
 * 1. Create ThreadSafeModelLoader with optional MemoryBudget
 * 2. Call load() from any thread to request model loading
 * 3. Use getLoadedModel() to retrieve loaded models
 * 4. Call incrementReference()/decrementReference() for usage tracking
 * 5. Call unload() when model is no longer needed
 */

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
#include <chrono>

namespace iron {
namespace runtime {

// Forward declaration
class MemoryBudget;

/**
 * @brief Thread-safe model loader with queuing
 *
 * Ensures models are loaded sequentially to prevent race conditions
 * and memory issues. Uses a worker thread to process load requests
 * from a FIFO queue.
 */
class ThreadSafeModelLoader {
public:
    /**
     * @brief Loaded model information
     */
    struct LoadedModel {
        std::string path;                          ///< Model path
        std::shared_ptr<void> session;             ///< Type-erased session
        size_t memoryUsage = 0;                    ///< Memory used by model
        std::atomic<int> referenceCount{1};        ///< Reference count
        bool isLoading = false;                    ///< Currently loading
        std::string errorMessage;                  ///< Error if load failed

        /**
         * @brief Check if model is ready for use
         * @return true if session is valid and not loading
         */
        bool isReady() const {
            return session != nullptr && !isLoading && errorMessage.empty();
        }
    };

    /**
     * @brief Load result
     */
    struct LoadResult {
        bool success;                              ///< Load succeeded
        std::shared_ptr<LoadedModel> model;        ///< Loaded model
        std::string errorMessage;                  ///< Error message if failed
        bool wasCached;                            ///< True if model was already loaded

        /**
         * @brief Get model or throw exception
         * @return Shared pointer to loaded model
         * @throws std::runtime_error if load failed
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
     *
     * The callback is responsible for actually loading the model
     * (e.g., using ONNX Runtime, xDNA, or other backend).
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

    /**
     * @brief Destructor - stops worker thread and cleans up
     */
    ~ThreadSafeModelLoader();

    // Prevent copying
    ThreadSafeModelLoader(const ThreadSafeModelLoader&) = delete;
    ThreadSafeModelLoader& operator=(const ThreadSafeModelLoader&) = delete;

    //==========================================================================
    // Model Loading
    //==========================================================================

    /**
     * @brief Load model (thread-safe)
     *
     * Queues the model for loading and waits for completion.
     * If the model is already loaded, returns the cached result.
     * If the model is currently loading, waits for completion.
     *
     * @param path Path to model
     * @return LoadResult with model or error
     */
    LoadResult load(const std::string& path);

    /**
     * @brief Get loaded model
     * @param path Path to model
     * @return Loaded model or nullptr if not loaded/ready
     */
    std::shared_ptr<LoadedModel> getLoadedModel(const std::string& path) const;

    /**
     * @brief Check if model is loaded and ready
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
     * @return Vector of paths for ready models
     */
    std::vector<std::string> getLoadedModels() const;

    //==========================================================================
    // Reference Counting
    //==========================================================================

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

    //==========================================================================
    // Status Queries
    //==========================================================================

    /**
     * @brief Get number of pending loads
     * @return Number of loads in queue
     */
    size_t getPendingLoadCount() const;

    /**
     * @brief Check if loader is processing a request
     * @return true if currently processing
     */
    bool isProcessing() const { return processing_.load(std::memory_order_relaxed); }

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
    LoadResult waitForLoading(const std::string& path);
};

} // namespace runtime
} // namespace iron
