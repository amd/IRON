// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file xdna_runtime.hpp
 * @brief Windows xDNA backend implementation for IRON NPU runtime
 *
 * This header defines the Windows-specific runtime implementation
 * using AMD's xDNA runtime API for Ryzen AI NPUs.
 *
 * ARCHITECTURE:
 * - Wraps xDNA runtime C/C++ APIs
 * - Implements INpuRuntime interface
 * - Handles Windows-specific memory management
 * - Supports FastFlowLM kernel format
 *
 * DEPENDENCIES:
 * - AMD xDNA Runtime SDK
 * - Windows Driver Model (WDM) for NPU access
 *
 * @note This is a stub implementation. Full implementation requires
 *       the AMD xDNA runtime SDK to be installed.
 */

#pragma once

#include <iron/runtime/npu_runtime.hpp>

#include <string>
#include <vector>
#include <memory>
#include <mutex>
#include <atomic>
#include <unordered_map>

namespace iron {
namespace runtime {

//==============================================================================
// Forward Declarations
//==============================================================================

class XdnaBuffer;
class XdnaKernelHandle;
class XdnaBufferManager;

// Forward declare xDNA types (actual types depend on xDNA SDK)
namespace xdna_detail {
    // Opaque handles - actual types defined by xDNA SDK
    using DeviceHandle = void*;
    using BufferHandle = void*;
    using KernelHandle = void*;
    using ContextHandle = void*;
}

//==============================================================================
// XDNA Buffer Implementation
//==============================================================================

/**
 * @brief Windows xDNA buffer implementation
 *
 * Wraps xDNA buffer handles for device memory operations.
 */
class XdnaBuffer : public IBuffer {
public:
    /**
     * @brief Construct from xDNA buffer handle
     * @param handle Native xDNA buffer handle
     * @param size Buffer size in bytes
     */
    explicit XdnaBuffer(xdna_detail::BufferHandle handle, size_t size);

    ~XdnaBuffer() override;

    // Prevent copying
    XdnaBuffer(const XdnaBuffer&) = delete;
    XdnaBuffer& operator=(const XdnaBuffer&) = delete;

    // Allow moving
    XdnaBuffer(XdnaBuffer&& other) noexcept;
    XdnaBuffer& operator=(XdnaBuffer&& other) noexcept;

    // IBuffer interface
    [[nodiscard]] size_t size() const override;
    void write(const void* data, size_t size, size_t offset = 0) override;
    void read(void* data, size_t size, size_t offset = 0) const override;
    void sync(bool to_device) override;
    [[nodiscard]] void* nativeHandle() const override;
    [[nodiscard]] uint64_t address() const override;
    [[nodiscard]] bool isValid() const override;

private:
    xdna_detail::BufferHandle handle_;
    size_t size_;
    std::atomic<bool> valid_;
    mutable std::mutex mutex_;
};

//==============================================================================
// XDNA Kernel Handle Implementation
//==============================================================================

/**
 * @brief Windows xDNA kernel handle implementation
 */
class XdnaKernelHandle : public IKernelHandle {
public:
    /**
     * @brief Construct from xDNA kernel handle
     * @param handle Native xDNA kernel handle
     * @param name Kernel name
     * @param numArgs Number of kernel arguments
     */
    XdnaKernelHandle(
        xdna_detail::KernelHandle handle,
        const std::string& name,
        size_t numArgs);

    ~XdnaKernelHandle() override;

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
    xdna_detail::KernelHandle handle_;
    std::string name_;
    size_t numArgs_;
    std::vector<std::optional<KernelArgument>> setArgs_;
    std::vector<std::pair<std::string, std::string>> argInfo_;
    mutable std::mutex mutex_;
};

//==============================================================================
// XDNA Buffer Manager Implementation
//==============================================================================

/**
 * @brief Windows xDNA buffer manager with pooling
 */
class XdnaBufferManager : public IBufferManager {
public:
    /**
     * @brief Construct buffer manager
     * @param maxPoolSize Maximum pool size in bytes
     */
    explicit XdnaBufferManager(size_t maxPoolSize = 256 * 1024 * 1024);

    ~XdnaBufferManager() override;

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
    struct PoolEntry {
        std::shared_ptr<XdnaBuffer> buffer;
        size_t size;
    };

    size_t maxPoolSize_;
    std::atomic<size_t> totalMemoryInUse_;
    std::atomic<size_t> activeCount_;

    // Pool organized by size buckets
    std::unordered_map<size_t, std::vector<PoolEntry>> pool_;
    mutable std::mutex poolMutex_;
};

//==============================================================================
// XDNA Runtime Implementation
//==============================================================================

/**
 * @brief Windows xDNA runtime implementation
 *
 * Implements the INpuRuntime interface using AMD's xDNA runtime
 * for Windows platforms.
 *
 * FEATURES:
 * - xDNA kernel loading and execution
 * - Buffer management with pooling
 * - Thread-safe kernel execution
 * - Error handling with descriptive messages
 *
 * @note Requires AMD xDNA Runtime SDK to be installed
 */
class XdnaRuntime : public INpuRuntime {
public:
    /**
     * @brief Construct xDNA runtime
     * @param deviceId Device ID (default: 0)
     *
     * @throws DeviceNotAvailableError if device not found
     * @throws RuntimeError if initialization fails
     */
    explicit XdnaRuntime(int deviceId = 0);

    ~XdnaRuntime() override;

    // Prevent copying
    XdnaRuntime(const XdnaRuntime&) = delete;
    XdnaRuntime& operator=(const XdnaRuntime&) = delete;

    //--------------------------------------------------------------------------
    // INpuRuntime Interface - Xclbin Loading
    //--------------------------------------------------------------------------

    bool loadXclbin(const std::string& path) override;
    bool loadXclbinFromMemory(const void* data, size_t size) override;
    bool unloadXclbin(const std::string& path) override;
    [[nodiscard]] std::vector<std::string> getKernelNames() const override;
    [[nodiscard]] std::vector<std::string> getKernelsFromXclbin(
        const std::string& xclbinPath) const override;
    [[nodiscard]] bool hasKernel(const std::string& kernelName) const override;

    //--------------------------------------------------------------------------
    // INpuRuntime Interface - Kernel Execution
    //--------------------------------------------------------------------------

    ExecutionResult execute(
        const std::string& kernelName,
        const std::vector<KernelArgument>& arguments,
        const ExecutionOptions& options = ExecutionOptions()) override;

    std::shared_ptr<IKernelHandle> getKernel(const std::string& kernelName) override;

    //--------------------------------------------------------------------------
    // INpuRuntime Interface - Buffer Management
    //--------------------------------------------------------------------------

    std::shared_ptr<IBuffer> allocateBuffer(
        size_t size,
        bool hostAccessible = true) override;

    std::shared_ptr<IBuffer> allocateBufferFromData(
        const void* data,
        size_t size) override;

    std::shared_ptr<IBufferManager> getBufferManager() override;

    //--------------------------------------------------------------------------
    // INpuRuntime Interface - Runtime Management
    //--------------------------------------------------------------------------

    void unload() override;
    [[nodiscard]] bool isLoaded() const override;
    [[nodiscard]] std::string getPlatformName() const override;
    [[nodiscard]] std::string getVersion() const override;
    [[nodiscard]] std::string getPlatformVersion() const override;
    [[nodiscard]] std::string getDeviceInfo() const override;

    //--------------------------------------------------------------------------
    // Static Methods
    //--------------------------------------------------------------------------

    /**
     * @brief Check if xDNA runtime is available
     * @return true if xDNA SDK is installed and NPU is accessible
     */
    [[nodiscard]] static bool isAvailable();

    /**
     * @brief Get xDNA driver version
     * @return Version string
     */
    [[nodiscard]] static std::string getDriverVersion();

private:
    // Internal structure for loaded xclbin
    struct LoadedXclbin {
        std::string path;
        std::vector<std::string> kernelNames;
        xdna_detail::ContextHandle context;
    };

    int deviceId_;
    xdna_detail::DeviceHandle device_;
    std::vector<LoadedXclbin> loadedXclbins_;
    std::shared_ptr<XdnaBufferManager> bufferManager_;
    mutable std::mutex mutex_;
    std::atomic<bool> initialized_;

    // Helper methods
    void initializeDevice();
    LoadedXclbin loadXclbinInternal(const void* data, size_t size, const std::string& path);
    XdnaKernelHandle* getKernelHandleInternal(const std::string& kernelName);
};

//==============================================================================
// Inline Implementations
//==============================================================================

inline bool XdnaRuntime::isAvailable() {
    // Stub: In real implementation, check for xDNA SDK and device
    return true;
}

inline std::string XdnaRuntime::getDriverVersion() {
    // Stub: In real implementation, query xDNA driver
    return "1.0.0-stub";
}

} // namespace runtime
} // namespace iron
