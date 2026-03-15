// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file xrt_runtime_wrapper.hpp
 * @brief Linux XRT backend implementation for IRON NPU runtime
 *
 * This header defines the Linux-specific runtime implementation
 * using AMD/Xilinx XRT (Xilinx Runtime) for Ryzen AI NPUs.
 *
 * ARCHITECTURE:
 * - Wraps XRT C++ APIs (or pyxrt for Python interop)
 * - Implements INpuRuntime interface
 * - Handles XRT-specific memory management
 * - Supports MLIR-compiled kernels via aiecc.py
 *
 * DEPENDENCIES:
 * - AMD XRT (Xilinx Runtime) >= 2.15.0
 * - libxrt_coreutils
 * - Ryzen AI device drivers
 *
 * BUILD REQUIREMENTS:
 * - CMake option IRON_USE_XRT=ON
 * - XRT_INCLUDE_DIRS and XRT_LIBRARIES configured
 *
 * @see https://github.com/Xilinx/XRT for XRT documentation
 */

#pragma once

#include <iron/runtime/npu_runtime.hpp>

#include <string>
#include <vector>
#include <memory>
#include <mutex>
#include <atomic>
#include <unordered_map>

// Forward declare XRT types to avoid heavy include dependency
// Actual XRT headers included in implementation file
namespace xrt {
    class device;
    class kernel;
    class buffer;
    class hw_context;
}

namespace iron {
namespace runtime {

//==============================================================================
// Forward Declarations
//==============================================================================

class XrtBuffer;
class XrtKernelHandle;
class XrtBufferManager;

//==============================================================================
// XRT Buffer Implementation
//==============================================================================

/**
 * @brief Linux XRT buffer implementation
 *
 * Wraps XRT buffer objects for device memory operations.
 * Provides host-to-device and device-to-host transfers.
 */
class XrtBuffer : public IBuffer {
public:
    /**
     * @brief Construct from XRT buffer
     * @param buffer XRT buffer object
     */
    explicit XrtBuffer(xrt::buffer buffer);

    /**
     * @brief Construct new buffer on device
     * @param device XRT device
     * @param size Buffer size in bytes
     * @param hostAccessible If true, buffer is host-accessible
     */
    XrtBuffer(const xrt::device& device, size_t size, bool hostAccessible = true);

    ~XrtBuffer() override;

    // Prevent copying (XRT buffers are move-only)
    XrtBuffer(const XrtBuffer&) = delete;
    XrtBuffer& operator=(const XrtBuffer&) = delete;

    // Allow moving
    XrtBuffer(XrtBuffer&& other) noexcept;
    XrtBuffer& operator=(XrtBuffer&& other) noexcept;

    // IBuffer interface
    [[nodiscard]] size_t size() const override;
    void write(const void* data, size_t size, size_t offset = 0) override;
    void read(void* data, size_t size, size_t offset = 0) const override;
    void sync(bool to_device) override;
    [[nodiscard]] void* nativeHandle() const override;
    [[nodiscard]] uint64_t address() const override;
    [[nodiscard]] bool isValid() const override;

    /**
     * @brief Get underlying XRT buffer
     * @return Reference to XRT buffer
     */
    [[nodiscard]] xrt::buffer& xrtBuffer();
    [[nodiscard]] const xrt::buffer& xrtBuffer() const;

private:
    xrt::buffer buffer_;
    size_t size_;
    std::atomic<bool> valid_;
    mutable std::mutex mutex_;
};

//==============================================================================
// XRT Kernel Handle Implementation
//==============================================================================

/**
 * @brief Linux XRT kernel handle implementation
 *
 * Wraps XRT kernel objects for repeated execution.
 */
class XrtKernelHandle : public IKernelHandle {
public:
    /**
     * @brief Construct from XRT kernel
     * @param kernel XRT kernel object
     * @param name Kernel name
     */
    XrtKernelHandle(xrt::kernel kernel, const std::string& name);

    ~XrtKernelHandle() override;

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

    /**
     * @brief Get underlying XRT kernel
     * @return Reference to XRT kernel
     */
    [[nodiscard]] xrt::kernel& xrtKernel();
    [[nodiscard]] const xrt::kernel& xrtKernel() const;

private:
    xrt::kernel kernel_;
    std::string name_;
    std::vector<std::optional<KernelArgument>> setArgs_;
    std::vector<std::pair<std::string, std::string>> argInfo_;
    mutable std::mutex mutex_;

    // Helper to convert KernelArgument to XRT format
    void applyArgument(size_t index, const KernelArgument& arg);
};

//==============================================================================
// XRT Buffer Manager Implementation
//==============================================================================

/**
 * @brief Linux XRT buffer manager with pooling
 *
 * Manages a pool of XRT buffers to reduce allocation overhead.
 */
class XrtBufferManager : public IBufferManager {
public:
    /**
     * @brief Construct buffer manager
     * @param device XRT device for buffer allocation
     * @param maxPoolSize Maximum pool size in bytes
     */
    XrtBufferManager(const xrt::device& device, size_t maxPoolSize = 256 * 1024 * 1024);

    ~XrtBufferManager() override;

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
        std::shared_ptr<XrtBuffer> buffer;
        size_t size;
    };

    xrt::device device_;
    size_t maxPoolSize_;
    std::atomic<size_t> totalMemoryInUse_;
    std::atomic<size_t> activeCount_;

    // Pool organized by size buckets (rounded to page size)
    std::unordered_map<size_t, std::vector<PoolEntry>> pool_;
    mutable std::mutex poolMutex_;

    // Helper to round size to pool bucket
    static size_t roundToBucket(size_t size);
};

//==============================================================================
// XRT Runtime Wrapper Implementation
//==============================================================================

/**
 * @brief Linux XRT runtime wrapper implementation
 *
 * Implements the INpuRuntime interface using AMD/Xilinx XRT
 * for Linux platforms.
 *
 * FEATURES:
 * - XRT kernel loading and execution
 * - Support for MLIR-compiled kernels (aiecc.py output)
 * - Buffer management with pooling
 * - Thread-safe kernel execution
 * - Hardware context management
 *
 * EXAMPLE:
 * @code
 * auto runtime = XrtRuntimeWrapper::create(0);
 * runtime->loadXclbin("/path/to/kernel.xclbin");
 *
 * auto kernel = runtime->getKernel("my_kernel");
 * // ... set arguments and execute
 * @endcode
 */
class XrtRuntimeWrapper : public INpuRuntime {
public:
    /**
     * @brief Construct XRT runtime wrapper
     * @param deviceId Device ID (default: 0)
     *
     * @throws DeviceNotAvailableError if device not found
     * @throws RuntimeError if initialization fails
     */
    explicit XrtRuntimeWrapper(int deviceId = 0);

    ~XrtRuntimeWrapper() override;

    // Prevent copying
    XrtRuntimeWrapper(const XrtRuntimeWrapper&) = delete;
    XrtRuntimeWrapper& operator=(const XrtRuntimeWrapper&) = delete;

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
     * @brief Check if XRT runtime is available
     * @return true if XRT is installed and NPU is accessible
     */
    [[nodiscard]] static bool isAvailable();

    /**
     * @brief Get XRT version string
     * @return Version in format "major.minor.patch"
     */
    [[nodiscard]] static std::string getXrtVersion();

    /**
     * @brief Create XRT runtime (convenience factory)
     * @param deviceId Device ID
     * @return Unique pointer to runtime
     */
    [[nodiscard]] static std::unique_ptr<XrtRuntimeWrapper> create(int deviceId = 0);

private:
    // Internal structure for loaded xclbin
    struct LoadedXclbin {
        std::string path;
        std::vector<std::string> kernelNames;
        std::unordered_map<std::string, xrt::kernel> kernels;
        std::unique_ptr<xrt::hw_context> hwContext;
    };

    int deviceId_;
    std::unique_ptr<xrt::device> device_;
    std::vector<LoadedXclbin> loadedXclbins_;
    std::shared_ptr<XrtBufferManager> bufferManager_;
    mutable std::mutex mutex_;
    std::atomic<bool> initialized_;

    // Helper methods
    void initializeDevice();
    LoadedXclbin loadXclbinInternal(const void* data, size_t size, const std::string& path);
    XrtKernelHandle* getKernelHandleInternal(const std::string& kernelName);
};

//==============================================================================
// Inline Implementations
//==============================================================================

inline bool XrtRuntimeWrapper::isAvailable() {
    // Stub: In real implementation, check for XRT library and device
    return true;
}

inline std::string XrtRuntimeWrapper::getXrtVersion() {
    // Stub: In real implementation, query XRT version
    return "2.15.0-stub";
}

inline std::unique_ptr<XrtRuntimeWrapper> XrtRuntimeWrapper::create(int deviceId) {
    return std::make_unique<XrtRuntimeWrapper>(deviceId);
}

} // namespace runtime
} // namespace iron
