// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file onnxruntime_genai.hpp
 * @brief Windows ONNX Runtime GenAI backend for IRON NPU runtime
 *
 * This header provides the Windows NPU backend using ONNX Runtime GenAI
 * with DirectML acceleration for AMD Ryzen AI NPUs.
 *
 * DESIGN PRINCIPLES:
 * - Wraps ONNX Runtime GenAI C++ API
 * - Implements INpuRuntime interface for cross-platform abstraction
 * - Supports ONNX model format with NPU Execution Provider
 * - Thread-safe operations with internal synchronization
 *
 * DEPENDENCIES:
 * - ONNX Runtime GenAI (v0.11.2 or later)
 * - DirectML (Windows 10/11)
 * - AMD Ryzen AI drivers
 *
 * @see npu_runtime.hpp for main interface definition
 *
 * @example
 * @code
 * #include <iron/runtime/onnxruntime_genai.hpp>
 *
 * using namespace iron::runtime;
 *
 * int main() {
 *     // Create ONNX Runtime GenAI backend
 *     auto runtime = std::make_unique<OnnxRuntimeGenAiWrapper>();
 *
 *     // Load ONNX model
 *     runtime->loadModel("model.onnx");
 *
 *     // Allocate buffers and execute
 *     auto buffer = runtime->allocateBuffer(1024 * 1024);
 *     // ... set up arguments and execute
 *
 *     return 0;
 * }
 * @endcode
 */

#pragma once

#include <iron/runtime/npu_runtime.hpp>

#ifdef _WIN32

// ONNX Runtime GenAI headers
#include <ort_genai.h>
#include <onnxruntime/core/session/onnxruntime_cxx_api.h>

namespace iron {
namespace runtime {

//==============================================================================
// Forward Declarations
//==============================================================================

class OnnxBuffer;
class OnnxKernelHandle;
class OnnxBufferManager;

//==============================================================================
// ONNX Buffer Implementation
//==============================================================================

/**
 * @brief Buffer implementation for ONNX Runtime GenAI
 *
 * Wraps ONNX Runtime memory buffers with IBuffer interface.
 * Supports both CPU and NPU memory through DirectML.
 */
class OnnxBuffer : public IBuffer {
public:
    /**
     * @brief Create buffer from ONNX tensor
     * @param tensor ONNX tensor value
     * @param size Buffer size in bytes
     */
    OnnxBuffer(Ort::Value tensor, size_t size);

    /**
     * @brief Create buffer with specified size
     * @param memoryInfo ONNX memory info
     * @param size Buffer size in bytes
     */
    OnnxBuffer(const Ort::MemoryInfo& memoryInfo, size_t size);

    ~OnnxBuffer() override;

    // Move semantics
    OnnxBuffer(OnnxBuffer&& other) noexcept;
    OnnxBuffer& operator=(OnnxBuffer&& other) noexcept;

    // Disable copy
    OnnxBuffer(const OnnxBuffer&) = delete;
    OnnxBuffer& operator=(const OnnxBuffer&) = delete;

    // IBuffer interface
    [[nodiscard]] size_t size() const override;
    void write(const void* data, size_t size, size_t offset = 0) override;
    void read(void* data, size_t size, size_t offset = 0) const override;
    void sync(bool to_device) override;
    [[nodiscard]] void* nativeHandle() const override;
    [[nodiscard]] uint64_t address() const override;
    [[nodiscard]] bool isValid() const override;

    // ONNX-specific access
    Ort::Value& tensor();
    const Ort::Value& tensor() const;

private:
    Ort::Value tensor_;
    size_t size_;
    bool valid_;
    mutable std::mutex mutex_;
};

//==============================================================================
// ONNX Kernel Handle Implementation
//==============================================================================

/**
 * @brief Kernel handle for ONNX Runtime GenAI
 *
 * Wraps ONNX Runtime session with IKernelHandle interface.
 * Supports incremental inference and streaming output.
 */
class OnnxKernelHandle : public IKernelHandle {
public:
    /**
     * @brief Create kernel handle from ONNX session
     * @param session ONNX session
     * @param name Kernel/model name
     */
    OnnxKernelHandle(std::unique_ptr<Ort::Session> session, const std::string& name);

    ~OnnxKernelHandle() override;

    // IKernelHandle interface
    [[nodiscard]] std::string name() const override;
    void setArg(size_t index, const KernelArgument& arg) override;
    ExecutionResult execute(const ExecutionOptions& options = ExecutionOptions()) override;
    void reset() override;
    [[nodiscard]] size_t numArguments() const override;
    [[nodiscard]] bool isReady() const override;
    [[nodiscard]] std::pair<std::string, std::string> getArgumentInfo(size_t index) const override;
    [[nodiscard]] std::vector<std::string> getArgumentNames() const override;
    [[nodiscard]] bool isArgumentSet(size_t index) const override;

private:
    std::unique_ptr<Ort::Session> session_;
    std::string name_;
    std::vector<std::optional<KernelArgument>> setArgs_;
    std::vector<std::pair<std::string, std::string>> argInfo_;
    mutable std::mutex mutex_;

    // Helper to validate arguments before execution
    bool validateArguments() const;
};

//==============================================================================
// ONNX Buffer Manager Implementation
//==============================================================================

/**
 * @brief Buffer manager for ONNX Runtime GenAI
 *
 * Manages a pool of ONNX tensors for efficient allocation.
 */
class OnnxBufferManager : public IBufferManager {
public:
    /**
     * @brief Create buffer manager
     * @param memoryInfo ONNX memory info
     * @param maxPoolSize Maximum pool size in bytes
     */
    OnnxBufferManager(const Ort::MemoryInfo& memoryInfo, size_t maxPoolSize = 1024 * 1024 * 1024);

    ~OnnxBufferManager() override;

    // IBufferManager interface
    std::shared_ptr<IBuffer> allocate(size_t size) override;
    void deallocate(std::shared_ptr<IBuffer> buffer) override;
    [[nodiscard]] std::map<size_t, size_t> getPoolStats() const override;
    void clear() override;
    [[nodiscard]] size_t totalMemoryInUse() const override;
    [[nodiscard]] size_t activeBufferCount() const override;
    [[nodiscard]] size_t pooledBufferCount() const override;
    void setMaxPoolSize(size_t max_bytes) override;

private:
    std::unique_ptr<Ort::MemoryInfo> memoryInfo_;
    size_t maxPoolSize_;
    std::atomic<size_t> totalMemoryInUse_;
    std::atomic<size_t> activeCount_;

    struct PoolEntry {
        std::shared_ptr<OnnxBuffer> buffer;
        size_t size;
    };

    std::map<size_t, std::vector<PoolEntry>> pool_;
    mutable std::mutex poolMutex_;

    size_t roundToBucket(size_t size);
};

//==============================================================================
// ONNX Runtime GenAI Wrapper
//==============================================================================

/**
 * @brief ONNX Runtime GenAI implementation of INpuRuntime
 *
 * Windows NPU backend using ONNX Runtime GenAI with DirectML.
 */
class OnnxRuntimeGenAiWrapper : public INpuRuntime {
public:
    /**
     * @brief Create ONNX Runtime GenAI wrapper
     * @param deviceId Device ID (reserved for future use)
     */
    explicit OnnxRuntimeGenAiWrapper(int deviceId = 0);

    ~OnnxRuntimeGenAiWrapper() override;

    // Xclbin loading (ONNX model loading instead)
    bool loadXclbin(const std::string& path) override;
    bool loadXclbinFromMemory(const void* data, size_t size) override;
    bool unloadXclbin(const std::string& path) override;

    [[nodiscard]] std::vector<std::string> getKernelNames() const override;
    [[nodiscard]] std::vector<std::string> getKernelsFromXclbin(
        const std::string& xclbinPath) const override;
    [[nodiscard]] bool hasKernel(const std::string& kernelName) const override;

    // Kernel execution
    ExecutionResult execute(
        const std::string& kernelName,
        const std::vector<KernelArgument>& arguments,
        const ExecutionOptions& options = ExecutionOptions()) override;

    std::shared_ptr<IKernelHandle> getKernel(const std::string& kernelName) override;

    // Buffer management
    std::shared_ptr<IBuffer> allocateBuffer(
        size_t size,
        bool hostAccessible = true) override;
    std::shared_ptr<IBuffer> allocateBufferFromData(
        const void* data,
        size_t size) override;
    std::shared_ptr<IBufferManager> getBufferManager() override;

    // Runtime management
    void unload() override;
    [[nodiscard]] bool isLoaded() const override;
    [[nodiscard]] std::string getPlatformName() const override;
    [[nodiscard]] std::string getVersion() const override;
    [[nodiscard]] std::string getPlatformVersion() const override;
    [[nodiscard]] std::string getDeviceInfo() const override;

    // Static availability check
    static bool isAvailable();

private:
    std::unique_ptr<Ort::Env> env_;
    std::unique_ptr<Ort::SessionOptions> sessionOptions_;
    std::unique_ptr<Ort::MemoryInfo> memoryInfo_;
    std::shared_ptr<OnnxBufferManager> bufferManager_;

    struct LoadedModel {
        std::string path;
        std::unique_ptr<Ort::Session> session;
        std::vector<std::string> inputNames;
        std::vector<std::string> outputNames;
    };

    std::vector<LoadedModel> loadedModels_;
    mutable std::mutex mutex_;

    bool initialized_;

    // Helper methods
    void initializeSessionOptions();
    LoadedModel* findModel(const std::string& path);
};

} // namespace runtime
} // namespace iron

#endif // _WIN32
