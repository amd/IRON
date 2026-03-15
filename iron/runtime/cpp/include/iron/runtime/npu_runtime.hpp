// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file npu_runtime.hpp
 * @brief Main C++ interface for NPU runtime abstraction layer
 *
 * This header defines the modern C++17 interface for the IRON NPU runtime.
 * It provides a clean abstraction over platform-specific backends:
 * - Linux: XRT (Xilinx Runtime) via pyxrt wrapper
 * - Windows: xDNA runtime for Ryzen AI NPUs
 *
 * DESIGN PRINCIPLES:
 * - Clean separation between interface and implementation
 * - Modern C++17 with RAII resource management
 * - Exception-based error handling
 * - Thread-safe operations where applicable
 * - Platform detection at compile-time and runtime
 *
 * @see xrt_runtime_wrapper.hpp for Linux XRT implementation
 * @see xdna_runtime.hpp for Windows xDNA implementation
 *
 * @example
 * @code
 * #include <iron/runtime/npu_runtime.hpp>
 *
 * using namespace iron::runtime;
 *
 * int main() {
 *     // Create runtime (auto-detects platform)
 *     auto runtime = NpuRuntime::create();
 *
 *     // Load kernel package
 *     runtime->loadXclbin("/path/to/kernel.xclbin");
 *
 *     // Allocate buffers
 *     auto buffer_a = runtime->allocateBuffer(1024 * 1024);
 *     auto buffer_b = runtime->allocateBuffer(1024 * 1024);
 *     auto buffer_c = runtime->allocateBuffer(1024 * 1024);
 *
 *     // Get kernel handle and set arguments
 *     auto kernel = runtime->getKernel("gemm_kernel");
 *     kernel->setArg(0, buffer_a);
 *     kernel->setArg(1, buffer_b);
 *     kernel->setArg(2, buffer_c);
 *     kernel->setArg(3, static_cast<int32_t>(64));
 *
 *     // Execute
 *     auto result = kernel->execute();
 *     if (result.success()) {
 *         // Process results...
 *     }
 *
 *     return 0;
 * }
 * @endcode
 */

#pragma once

#include <string>
#include <vector>
#include <memory>
#include <cstdint>
#include <optional>
#include <variant>
#include <map>
#include <stdexcept>
#include <functional>
#include <mutex>
#include <atomic>

namespace iron {
namespace runtime {

// Forward declarations
class IBuffer;
class IKernelHandle;
class IBufferManager;

//==============================================================================
// Buffer Interface
//==============================================================================

/**
 * @brief Abstract interface for device memory buffer
 *
 * Represents a buffer object (BO) in the NPU's memory space.
 * Provides host-to-device and device-to-host data transfer.
 *
 * THREAD SAFETY:
 * - read()/write() operations are thread-safe
 * - Multiple threads can read simultaneously
 * - Write operations are serialized internally
 */
class IBuffer {
public:
    virtual ~IBuffer() = default;

    /**
     * @brief Get buffer size in bytes
     * @return Size in bytes
     */
    [[nodiscard]] virtual size_t size() const = 0;

    /**
     * @brief Write data to buffer (host-to-device)
     *
     * @param data Pointer to source data
     * @param size Number of bytes to write
     * @param offset Offset in destination buffer (default: 0)
     *
     * @throws BufferError if write fails
     */
    virtual void write(const void* data, size_t size, size_t offset = 0) = 0;

    /**
     * @brief Read data from buffer (device-to-host)
     *
     * @param data Pointer to destination buffer (must be pre-allocated)
     * @param size Number of bytes to read
     * @param offset Offset in source buffer (default: 0)
     *
     * @throws BufferError if read fails
     */
    virtual void read(void* data, size_t size, size_t offset = 0) const = 0;

    /**
     * @brief Sync buffer with device
     *
     * @param to_device If true, sync host-to-device; otherwise device-to-host
     *
     * @throws BufferError if sync fails
     */
    virtual void sync(bool to_device) = 0;

    /**
     * @brief Get native buffer handle (platform-specific)
     *
     * @return Opaque handle for platform-specific code
     *
     * @note Use this only for platform-specific operations
     *       not covered by this interface.
     */
    [[nodiscard]] virtual void* nativeHandle() const = 0;

    /**
     * @brief Get buffer address for kernel argument
     *
     * @return Platform-specific address/identifier
     */
    [[nodiscard]] virtual uint64_t address() const = 0;

    /**
     * @brief Check if buffer is valid
     * @return true if buffer is allocated and accessible
     */
    [[nodiscard]] virtual bool isValid() const = 0;
};

//==============================================================================
// Execution Result
//==============================================================================

/**
 * @brief Result of kernel execution
 *
 * Contains execution status, timing information, and optional outputs.
 */
struct ExecutionResult {
    /// Execution status code (0 = success, non-zero = error code)
    int status = 0;

    /// Execution time in microseconds (optional, if profiling enabled)
    std::optional<uint64_t> executionTimeUs;

    /// Error message if execution failed (optional)
    std::optional<std::string> errorMessage;

    /// Output buffers (optional, if kernel produces indirect outputs)
    std::vector<std::shared_ptr<IBuffer>> outputs;

    /// Additional platform-specific data (optional)
    std::optional<std::string> platformData;

    /// Kernel execution ID for tracing (optional)
    std::optional<uint64_t> executionId;

    /**
     * @brief Check if execution was successful
     * @return true if status == 0
     */
    [[nodiscard]] bool success() const { return status == 0; }

    /**
     * @brief Get error message or empty string
     * @return Error message if available
     */
    [[nodiscard]] std::string getErrorMessage() const {
        return errorMessage.value_or("");
    }

    /**
     * @brief Get execution time or 0
     * @return Execution time in microseconds
     */
    [[nodiscard]] uint64_t getExecutionTimeUs() const {
        return executionTimeUs.value_or(0);
    }
};

//==============================================================================
// Kernel Arguments
//==============================================================================

/**
 * @brief Kernel argument variant types
 *
 * Kernel arguments can be:
 * - Buffer references (most common for tensor data)
 * - Scalar integers (sizes, counts, indices)
 * - Scalar floats (parameters like epsilon, scale, alpha)
 */
using KernelArgument = std::variant<
    std::shared_ptr<IBuffer>,  // Buffer argument
    int32_t,                    // Scalar signed integer
    float,                      // Scalar float
    uint32_t,                   // Scalar unsigned integer
    int64_t,                    // Scalar 64-bit signed integer
    uint64_t,                   // Scalar 64-bit unsigned integer
    double                      // Scalar double precision
>;

/**
 * @brief Helper to check KernelArgument type at runtime
 */
struct KernelArgumentVisitor {
    [[nodiscard]] const char* operator()(const std::shared_ptr<IBuffer>&) const { return "buffer"; }
    [[nodiscard]] const char* operator()(int32_t) const { return "int32"; }
    [[nodiscard]] const char* operator()(uint32_t) const { return "uint32"; }
    [[nodiscard]] const char* operator()(int64_t) const { return "int64"; }
    [[nodiscard]] const char* operator()(uint64_t) const { return "uint64"; }
    [[nodiscard]] const char* operator()(float) const { return "float"; }
    [[nodiscard]] const char* operator()(double) const { return "double"; }
};

/**
 * @brief Kernel execution options
 */
struct ExecutionOptions {
    /// Timeout in milliseconds (0 = use default timeout)
    uint32_t timeoutMs = 0;

    /// Enable profiling (collect execution time)
    bool profile = false;

    /// Synchronous execution (wait for completion)
    /// If false, execute() returns immediately and caller must wait()
    bool synchronous = true;

    /// Priority level (0 = normal, higher = higher priority)
    uint32_t priority = 0;

    /// Custom platform-specific options (JSON string)
    std::optional<std::string> platformOptions;

    /// Execution stream for async operations (platform-specific, nullable)
    std::optional<void*> stream;

    /**
     * @brief Set timeout and return self for chaining
     */
    ExecutionOptions& withTimeout(uint32_t ms) {
        timeoutMs = ms;
        return *this;
    }

    /**
     * @brief Enable profiling and return self for chaining
     */
    ExecutionOptions& withProfiling(bool enable = true) {
        profile = enable;
        return *this;
    }

    /**
     * @brief Set execution mode and return self for chaining
     */
    ExecutionOptions& withSynchronous(bool sync = true) {
        synchronous = sync;
        return *this;
    }
};

//==============================================================================
// Kernel Handle Interface
//==============================================================================

/**
 * @brief Handle for repeated kernel execution
 *
 * Provides an efficient interface for kernels that need to be executed
 * multiple times with different arguments. Avoids repeated kernel
 * lookup and validation overhead.
 *
 * THREAD SAFETY:
 * - Not thread-safe by design for performance
 * - Create separate handles for concurrent execution
 * - Use NpuRuntime::execute() for thread-safe one-off execution
 *
 * @example
 * @code
 * auto kernel = runtime->getKernel("gemm_kernel");
 *
 * // Execute multiple times with different inputs
 * for (int i = 0; i < iterations; ++i) {
 *     kernel->setArg(0, input_buffers[i]);
 *     kernel->setArg(1, weight_buffer);
 *     kernel->setArg(2, output_buffers[i]);
 *     auto result = kernel->execute();
 * }
 * @endcode
 */
class IKernelHandle {
public:
    virtual ~IKernelHandle() = default;

    /**
     * @brief Get kernel name
     * @return Kernel identifier
     */
    [[nodiscard]] virtual std::string name() const = 0;

    /**
     * @brief Set kernel argument
     *
     * @param index Argument index (0-based, must match kernel definition)
     * @param arg Argument value (buffer or scalar)
     *
     * @throws ArgumentError if index is invalid or type mismatch
     */
    virtual void setArg(size_t index, const KernelArgument& arg) = 0;

    /**
     * @brief Execute kernel with set arguments
     *
     * @param options Execution options
     * @return ExecutionResult with status and metadata
     *
     * @throws RuntimeError if execution fails
     */
    virtual ExecutionResult execute(const ExecutionOptions& options = ExecutionOptions()) = 0;

    /**
     * @brief Execute and wait for completion (convenience method)
     *
     * @param timeoutMs Timeout in milliseconds
     * @return ExecutionResult
     */
    [[nodiscard]] ExecutionResult executeAndWait(uint32_t timeoutMs = 0) {
        ExecutionOptions opts;
        opts.timeoutMs = timeoutMs;
        opts.synchronous = true;
        return execute(opts);
    }

    /**
     * @brief Reset all arguments to default state
     *
     * Clears all previously set arguments.
     */
    virtual void reset() = 0;

    /**
     * @brief Get number of kernel arguments
     * @return Argument count from kernel metadata
     */
    [[nodiscard]] virtual size_t numArguments() const = 0;

    /**
     * @brief Check if all required arguments are set
     * @return true if kernel is ready for execution
     */
    [[nodiscard]] virtual bool isReady() const = 0;

    /**
     * @brief Get argument info (name, type) for debugging
     * @param index Argument index
     * @return Tuple of (name, type_name) or ("", "") if unknown
     */
    [[nodiscard]] virtual std::pair<std::string, std::string> getArgumentInfo(size_t index) const = 0;

    /**
     * @brief Get all argument names
     * @return Vector of argument names in order
     */
    [[nodiscard]] virtual std::vector<std::string> getArgumentNames() const = 0;

    /**
     * @brief Check if specific argument is set
     * @param index Argument index
     * @return true if argument has been set
     */
    [[nodiscard]] virtual bool isArgumentSet(size_t index) const = 0;
};

//==============================================================================
// Buffer Manager Interface
//==============================================================================

/**
 * @brief Buffer manager for efficient memory allocation
 *
 * Manages a pool of buffers to avoid repeated allocation/deallocation
 * overhead. Useful for repeated kernel invocations with similar
 * buffer size requirements.
 *
 * FEATURES:
 * - Automatic buffer reuse for same-size allocations
 * - Configurable pool size limits
 * - Statistics tracking for memory profiling
 * - Thread-safe allocation
 *
 * EXAMPLE:
 * @code
 * auto manager = runtime->getBufferManager();
 *
 * // First allocation (creates new buffer)
 * auto buf1 = manager->allocate(1024 * 1024);  // 1MB
 *
 * // Use buffer...
 *
 * // Return to pool
 * manager->deallocate(buf1);
 *
 * // Second allocation (reuses pooled buffer)
 * auto buf2 = manager->allocate(1024 * 1024);  // Gets same buffer
 * @endcode
 */
class IBufferManager {
public:
    virtual ~IBufferManager() = default;

    /**
     * @brief Allocate buffer from pool
     *
     * @param size Minimum buffer size needed (bytes)
     * @return Shared pointer to buffer
     */
    virtual std::shared_ptr<IBuffer> allocate(size_t size) = 0;

    /**
     * @brief Return buffer to pool for reuse
     *
     * @param buffer Buffer to return
     */
    virtual void deallocate(std::shared_ptr<IBuffer> buffer) = 0;

    /**
     * @brief Get pool statistics
     *
     * @return Map of buffer size to count of available buffers
     */
    [[nodiscard]] virtual std::map<size_t, size_t> getPoolStats() const = 0;

    /**
     * @brief Clear all buffers from pool
     *
     * Frees all pooled memory. Use before shutdown or
     * when memory needs to be reclaimed.
     */
    virtual void clear() = 0;

    /**
     * @brief Get total memory in use (pooled + allocated)
     * @return Bytes
     */
    [[nodiscard]] virtual size_t totalMemoryInUse() const = 0;

    /**
     * @brief Get number of active (non-pooled) buffers
     * @return Buffer count
     */
    [[nodiscard]] virtual size_t activeBufferCount() const = 0;

    /**
     * @brief Get number of pooled (available) buffers
     * @return Buffer count
     */
    [[nodiscard]] virtual size_t pooledBufferCount() const = 0;

    /**
     * @brief Set maximum pool size
     *
     * @param max_bytes Maximum bytes to keep in pool
     */
    virtual void setMaxPoolSize(size_t max_bytes) = 0;
};

//==============================================================================
// Main Runtime Interface
//==============================================================================

/**
 * @brief Abstract interface for NPU runtime
 *
 * This interface provides platform-agnostic kernel loading and execution.
 * Implementations exist for:
 * - Linux: XrtRuntimeWrapper (uses XRT/pyxrt)
 * - Windows: XdnaRuntime (uses xDNA runtime)
 *
 * PLATFORM DETECTION:
 * Use NpuRuntime::create() to get the appropriate implementation
 * for the current platform.
 *
 * @see NpuRuntime::create() for factory method
 * @see NpuRuntime::createForPlatform() for explicit platform selection
 */
class INpuRuntime {
public:
    virtual ~INpuRuntime() = default;

    //--------------------------------------------------------------------------
    // Xclbin Loading
    //--------------------------------------------------------------------------

    /**
     * @brief Load .xclbin kernel package
     *
     * Loads all kernels contained in the .xclbin file.
     * The file must exist and be a valid .xclbin format.
     *
     * @param path Path to .xclbin file (absolute or relative)
     * @return true if loaded successfully
     *
     * @throws XclbinError if file is invalid or loading fails
     */
    virtual bool loadXclbin(const std::string& path) = 0;

    /**
     * @brief Load .xclbin from memory buffer
     *
     * Allows loading .xclbin from a memory buffer instead of file.
     * Useful for embedded scenarios or custom loading logic.
     *
     * @param data Pointer to .xclbin data
     * @param size Size of data in bytes
     * @return true if loaded successfully
     *
     * @throws XclbinError if data is invalid or loading fails
     */
    virtual bool loadXclbinFromMemory(const void* data, size_t size) = 0;

    /**
     * @brief Unload specific .xclbin package
     *
     * Unloads kernels from a previously loaded .xclbin.
     * Use when you need to free memory but keep the runtime.
     *
     * @param path Path to .xclbin (must match load path)
     * @return true if unloaded successfully
     */
    virtual bool unloadXclbin(const std::string& path) = 0;

    /**
     * @brief Get list of available kernel names
     * @return Vector of kernel names (may be empty if nothing loaded)
     */
    [[nodiscard]] virtual std::vector<std::string> getKernelNames() const = 0;

    /**
     * @brief Get kernels from a specific .xclbin
     *
     * @param xclbinPath Path to .xclbin file
     * @return Vector of kernel names from that file
     */
    [[nodiscard]] virtual std::vector<std::string> getKernelsFromXclbin(
        const std::string& xclbinPath) const = 0;

    /**
     * @brief Check if a specific kernel is available
     * @param kernelName Name of kernel to check
     * @return true if kernel is loaded and available
     */
    [[nodiscard]] virtual bool hasKernel(const std::string& kernelName) const = 0;

    //--------------------------------------------------------------------------
    // Kernel Execution
    //--------------------------------------------------------------------------

    /**
     * @brief Execute kernel with provided arguments
     *
     * Convenience method for one-off kernel execution.
     * For repeated execution, use getKernel() for better performance.
     *
     * THREAD SAFETY: This method is thread-safe.
     *
     * @param kernelName Name of kernel to execute
     * @param arguments Kernel arguments (buffers and scalars)
     * @param options Execution options
     * @return ExecutionResult with status and outputs
     *
     * @throws KernelNotFoundError if kernel not found
     * @throws RuntimeError if execution fails
     */
    virtual ExecutionResult execute(
        const std::string& kernelName,
        const std::vector<KernelArgument>& arguments,
        const ExecutionOptions& options = ExecutionOptions()) = 0;

    /**
     * @brief Create a kernel execution handle
     *
     * Returns a handle for repeated kernel execution with
     * different arguments. More efficient than execute() for
     * repeated calls.
     *
     * THREAD SAFETY: This method is thread-safe.
     * Returned handle is NOT thread-safe.
     *
     * @param kernelName Name of kernel
     * @return Kernel handle, or nullptr if kernel not found
     */
    virtual std::shared_ptr<IKernelHandle> getKernel(const std::string& kernelName) = 0;

    //--------------------------------------------------------------------------
    // Buffer Management
    //--------------------------------------------------------------------------

    /**
     * @brief Allocate buffer for kernel I/O
     *
     * THREAD SAFETY: This method is thread-safe.
     *
     * @param size Size in bytes
     * @param hostAccessible If true, buffer is accessible from host
     * @return Shared pointer to buffer
     *
     * @throws BufferError if allocation fails
     */
    virtual std::shared_ptr<IBuffer> allocateBuffer(
        size_t size,
        bool hostAccessible = true) = 0;

    /**
     * @brief Allocate buffer from existing host data
     *
     * Creates a device buffer and copies initial data from host.
     *
     * THREAD SAFETY: This method is thread-safe.
     *
     * @param data Pointer to host data
     * @param size Size in bytes
     * @return Shared pointer to buffer
     *
     * @throws BufferError if allocation fails
     */
    virtual std::shared_ptr<IBuffer> allocateBufferFromData(
        const void* data,
        size_t size) = 0;

    /**
     * @brief Get buffer manager for efficient allocation
     * @return Shared pointer to buffer manager
     */
    virtual std::shared_ptr<IBufferManager> getBufferManager() = 0;

    //--------------------------------------------------------------------------
    // Runtime Management
    //--------------------------------------------------------------------------

    /**
     * @brief Unload all kernels and free resources
     */
    virtual void unload() = 0;

    /**
     * @brief Check if runtime has loaded kernels
     * @return true if any kernels are loaded
     */
    [[nodiscard]] virtual bool isLoaded() const = 0;

    /**
     * @brief Get platform name
     * @return "XRT" for Linux, "xDNA" for Windows
     */
    [[nodiscard]] virtual std::string getPlatformName() const = 0;

    /**
     * @brief Get IRON runtime version string
     * @return Version information (e.g., "1.0.0")
     */
    [[nodiscard]] virtual std::string getVersion() const = 0;

    /**
     * @brief Get underlying runtime version (XRT/xDNA)
     * @return Platform-specific version string
     */
    [[nodiscard]] virtual std::string getPlatformVersion() const = 0;

    /**
     * @brief Get device information as JSON string
     * @return Device info JSON
     */
    [[nodiscard]] virtual std::string getDeviceInfo() const = 0;

    //--------------------------------------------------------------------------
    // Static Factory Methods
    //--------------------------------------------------------------------------

    /**
     * @brief Check if NPU device is available
     * @return true if NPU is present and accessible
     */
    [[nodiscard]] static bool isDeviceAvailable();

    /**
     * @brief Get list of available NPU devices
     * @return Vector of device IDs (usually [0] for single NPU)
     */
    [[nodiscard]] static std::vector<int> getAvailableDevices();

    /**
     * @brief Create platform-appropriate runtime implementation
     *
     * Factory method that returns XrtRuntimeWrapper on Linux
     * or XdnaRuntime on Windows.
     *
     * @param deviceId Device ID (default: 0)
     * @return Unique pointer to runtime instance
     *
     * @throws RuntimeError if no NPU device available
     */
    [[nodiscard]] static std::unique_ptr<INpuRuntime> create(int deviceId = 0);

    /**
     * @brief Create runtime with explicit platform selection
     *
     * Force a specific platform implementation (for testing).
     *
     * @param platform "XRT", "xDNA", or "mock"
     * @param deviceId Device ID
     * @return Unique pointer to runtime instance
     *
     * @throws RuntimeError if platform not supported
     */
    [[nodiscard]] static std::unique_ptr<INpuRuntime> createForPlatform(
        const std::string& platform,
        int deviceId = 0);

    /**
     * @brief Get current platform string
     * @return "linux", "windows", or "unknown"
     */
    [[nodiscard]] static std::string getCurrentPlatform();

    /**
     * @brief Check if running on Linux
     * @return true if Linux platform
     */
    [[nodiscard]] static bool isLinux();

    /**
     * @brief Check if running on Windows
     * @return true if Windows platform
     */
    [[nodiscard]] static bool isWindows();
};

//==============================================================================
// Exception Classes
//==============================================================================

/**
 * @brief Base exception for runtime errors
 */
class RuntimeError : public std::runtime_error {
public:
    explicit RuntimeError(const std::string& msg)
        : std::runtime_error(msg) {}

    RuntimeError(const std::string& msg, int errorCode)
        : std::runtime_error(msg), errorCode_(errorCode) {}

    [[nodiscard]] int errorCode() const { return errorCode_.value_or(-1); }

private:
    std::optional<int> errorCode_;
};

/**
 * @brief Exception for kernel not found
 */
class KernelNotFoundError : public RuntimeError {
public:
    explicit KernelNotFoundError(const std::string& kernelName)
        : RuntimeError("Kernel not found: " + kernelName),
          kernelName_(kernelName) {}

    [[nodiscard]] const std::string& kernelName() const { return kernelName_; }

private:
    std::string kernelName_;
};

/**
 * @brief Exception for argument type mismatch
 */
class ArgumentError : public RuntimeError {
public:
    ArgumentError(const std::string& msg, size_t argIndex)
        : RuntimeError(msg), argIndex_(argIndex) {}

    [[nodiscard]] size_t argumentIndex() const { return argIndex_.value_or(0); }

private:
    std::optional<size_t> argIndex_;
};

/**
 * @brief Exception for buffer operations
 */
class BufferError : public RuntimeError {
public:
    explicit BufferError(const std::string& msg)
        : RuntimeError(msg) {}

    BufferError(const std::string& msg, int errorCode)
        : RuntimeError(msg, errorCode) {}
};

/**
 * @brief Exception for Xclbin loading errors
 */
class XclbinError : public RuntimeError {
public:
    explicit XclbinError(const std::string& msg)
        : RuntimeError(msg) {}

    XclbinError(const std::string& msg, int errorCode)
        : RuntimeError(msg, errorCode) {}
};

/**
 * @brief Exception for device not available
 */
class DeviceNotAvailableError : public RuntimeError {
public:
    explicit DeviceNotAvailableError(int deviceId)
        : RuntimeError("NPU device " + std::to_string(deviceId) + " not available"),
          deviceId_(deviceId) {}

    [[nodiscard]] int deviceId() const { return deviceId_; }

private:
    int deviceId_;
};

//==============================================================================
// Type Aliases for Convenience
//==============================================================================

/**
 * @brief Type alias for the main runtime interface
 * @deprecated Use INpuRuntime directly
 */
using NpuRuntime = INpuRuntime;

/**
 * @brief Type alias for runtime pointer
 */
using NpuRuntimePtr = std::unique_ptr<INpuRuntime>;

/**
 * @brief Type alias for buffer pointer
 */
using BufferPtr = std::shared_ptr<IBuffer>;

/**
 * @brief Type alias for kernel handle pointer
 */
using KernelHandlePtr = std::shared_ptr<IKernelHandle>;

/**
 * @brief Type alias for buffer manager pointer
 */
using BufferManagerPtr = std::shared_ptr<IBufferManager>;

} // namespace runtime
} // namespace iron

// NOTE: Platform-specific implementations (xdna_runtime.hpp, xrt_runtime_wrapper.hpp)
// are included by the implementation file (npu_runtime.cpp), not here.
// This prevents circular includes and reduces compilation dependencies.
