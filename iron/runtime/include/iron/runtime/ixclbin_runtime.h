// SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc.
// SPDX-License-Identifier: Apache-2.0

/**
 * @file ixclbin_runtime.h
 * @brief Cross-platform runtime interface for .xclbin kernel execution
 *
 * This header defines the abstract interface for loading and executing
 * .xclbin kernels on AMD Ryzen AI NPUs. The implementation differs
 * between Linux (XRT) and Windows (xDNA), but the interface remains
 * consistent.
 *
 * DESIGN RATIONALE:
 * - Linux uses XRT with runtime MLIR compilation via aiecc.py
 * - Windows uses xDNA runtime with pre-compiled FastFlowLM kernels
 * - This interface abstracts both into a unified API
 *
 * USAGE EXAMPLE:
 * @code
 * // Create runtime (auto-selects platform implementation)
 * auto runtime = IXclbinRuntime::create();
 *
 * // Load kernel package
 * if (!runtime->load_xclbin("/path/to/gemm.xclbin")) {
 *     throw std::runtime_error("Failed to load xclbin");
 * }
 *
 * // Allocate buffers
 * auto buffer_a = runtime->allocate_buffer(M * K * sizeof(bfloat16));
 * auto buffer_b = runtime->allocate_buffer(K * N * sizeof(bfloat16));
 * auto buffer_c = runtime->allocate_buffer(M * N * sizeof(bfloat16));
 *
 * // Write input data
 * buffer_a->write(host_data_a, M * K * sizeof(bfloat16));
 * buffer_b->write(host_data_b, K * N * sizeof(bfloat16));
 *
 * // Get kernel handle
 * auto kernel = runtime->get_kernel("gemm_kernel");
 * kernel->set_arg(0, buffer_a);
 * kernel->set_arg(1, buffer_b);
 * kernel->set_arg(2, buffer_c);
 * kernel->set_arg(3, static_cast<int32_t>(M));
 * kernel->set_arg(4, static_cast<int32_t>(K));
 * kernel->set_arg(5, static_cast<int32_t>(N));
 *
 * // Execute
 * auto result = kernel->execute();
 * if (result.success()) {
 *     buffer_c->read(host_data_c, M * N * sizeof(bfloat16));
 * }
 * @endcode
 */

#pragma once

#include <cstdint>
#include <map>
#include <memory>
#include <optional>
#include <stdexcept>
#include <string>
#include <variant>
#include <vector>

namespace iron
{
namespace runtime
{

/**
 * @brief Forward declarations
 */
class IBuffer;
class IKernelHandle;

/**
 * @brief Buffer handle for device memory
 *
 * Represents a buffer object (BO) in the NPU's memory space.
 * Platform-specific implementations wrap XRT BOs (Linux) or
 * xDNA buffer handles (Windows).
 *
 * THREAD SAFETY: Implementations should be thread-safe for
 * concurrent read/write operations.
 */
class IBuffer
{
  public:
    virtual ~IBuffer() = default;

    /**
     * @brief Get buffer size in bytes
     * @return Size in bytes
     */
    virtual size_t size() const = 0;

    /**
     * @brief Write data to buffer (host-to-device)
     *
     * @param data Pointer to source data
     * @param size Number of bytes to write
     * @param offset Offset in destination buffer (default: 0)
     *
     * @throws std::runtime_error if write fails
     */
    virtual void write(const void *data, size_t size, size_t offset = 0) = 0;

    /**
     * @brief Read data from buffer (device-to-host)
     *
     * @param data Pointer to destination buffer (must be pre-allocated)
     * @param size Number of bytes to read
     * @param offset Offset in source buffer (default: 0)
     *
     * @throws std::runtime_error if read fails
     */
    virtual void read(void *data, size_t size, size_t offset = 0) const = 0;

    /**
     * @brief Sync buffer with device
     *
     * @param to_device If true, sync host-to-device; otherwise device-to-host
     *
     * @throws std::runtime_error if sync fails
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
    virtual void *native_handle() = 0;

    /**
     * @brief Get buffer address for kernel argument
     *
     * @return Platform-specific address/identifier
     */
    virtual uint64_t address() const = 0;
};

/**
 * @brief Result of kernel execution
 */
struct ExecutionResult {
    /// Execution status code (0 = success, non-zero = error)
    int status = 0;

    /// Execution time in microseconds (optional, if profiling enabled)
    std::optional<uint64_t> execution_time_us;

    /// Error message if execution failed (optional)
    std::optional<std::string> error_message;

    /// Output buffers (optional, if kernel produces indirect outputs)
    std::vector<std::shared_ptr<IBuffer>> outputs;

    /// Additional platform-specific data (optional)
    std::optional<std::string> platform_data;

    /**
     * @brief Check if execution was successful
     * @return true if status == 0
     */
    bool success() const
    {
        return status == 0;
    }

    /**
     * @brief Get error message or empty string
     * @return Error message if available
     */
    std::string get_error_message() const
    {
        return error_message.value_or("");
    }
};

/**
 * @brief Kernel argument variant types
 *
 * Kernel arguments can be:
 * - Buffer references (most common)
 * - Scalar integers (sizes, counts)
 * - Scalar floats (parameters like epsilon, scale)
 */
using KernelArgument = std::variant<std::shared_ptr<IBuffer>, // Buffer argument (address_qualifier=1)
                                    int32_t,                  // Scalar signed integer
                                    float,                    // Scalar float
                                    uint32_t,                 // Scalar unsigned integer
                                    int64_t,                  // Scalar 64-bit signed integer
                                    uint64_t                  // Scalar 64-bit unsigned integer
                                    >;

/**
 * @brief Kernel execution options
 */
struct ExecutionOptions {
    /// Timeout in milliseconds (0 = no timeout, use default)
    uint32_t timeout_ms = 0;

    /// Enable profiling (collect execution time)
    bool profile = false;

    /// Synchronous execution (wait for completion)
    /// If false, execute() returns immediately and caller must wait()
    bool synchronous = true;

    /// Priority level (0 = normal, higher = higher priority)
    uint32_t priority = 0;

    /// Custom platform-specific options (JSON string)
    std::optional<std::string> platform_options;
};

/**
 * @brief Handle for repeated kernel execution
 *
 * Provides a more efficient interface for kernels that
 * need to be executed multiple times with different arguments.
 * Avoids repeated kernel lookup and validation overhead.
 *
 * THREAD SAFETY: Not thread-safe. Create separate handles
 * for concurrent execution.
 */
class IKernelHandle
{
  public:
    virtual ~IKernelHandle() = default;

    /**
     * @brief Get kernel name
     * @return Kernel identifier
     */
    virtual std::string name() const = 0;

    /**
     * @brief Set kernel argument
     *
     * @param index Argument index (0-based, must match kernel definition)
     * @param arg Argument value (buffer or scalar)
     *
     * @throws std::out_of_range if index is invalid
     * @throws std::invalid_argument if argument type doesn't match
     */
    virtual void set_arg(size_t index, const KernelArgument &arg) = 0;

    /**
     * @brief Execute kernel with set arguments
     *
     * @param options Execution options
     * @return ExecutionResult with status and metadata
     *
     * @throws std::runtime_error if execution fails
     */
    virtual ExecutionResult execute(const ExecutionOptions &options = ExecutionOptions()) = 0;

    /**
     * @brief Execute and wait for completion (convenience method)
     *
     * @param timeout_ms Timeout in milliseconds
     * @return ExecutionResult
     */
    ExecutionResult executeAndWait(uint32_t timeout_ms = 0)
    {
        ExecutionOptions opts;
        opts.timeout_ms = timeout_ms;
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
    virtual size_t num_arguments() const = 0;

    /**
     * @brief Check if all required arguments are set
     * @return true if kernel is ready for execution
     */
    virtual bool is_ready() const = 0;

    /**
     * @brief Get argument info (name, type) for debugging
     * @param index Argument index
     * @return Tuple of (name, type_name) or ("", "") if unknown
     */
    virtual std::pair<std::string, std::string> get_argument_info(size_t index) const = 0;
};

/**
 * @brief Buffer manager for efficient memory allocation
 *
 * Manages a pool of buffers to avoid repeated allocation/deallocation
 * overhead. Useful for repeated kernel invocations with similar
 * buffer size requirements.
 *
 * EXAMPLE:
 * @code
 * auto manager = runtime->get_buffer_manager();
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
class IBufferManager
{
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
    virtual std::map<size_t, size_t> get_pool_stats() const = 0;

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
    virtual size_t total_memory_in_use() const = 0;
};

/**
 * @brief Abstract interface for .xclbin runtime
 *
 * This interface provides platform-agnostic kernel loading and execution.
 * Implementations exist for:
 * - Linux: XrtRuntime (uses XRT/pyxrt)
 * - Windows: XdnaRuntime (uses xDNA runtime)
 *
 * PLATFORM DETECTION:
 * Use IXclbinRuntime::create() to get the appropriate implementation
 * for the current platform.
 */
class IXclbinRuntime
{
  public:
    virtual ~IXclbinRuntime() = default;

    /**
     * @brief Load .xclbin kernel package
     *
     * Loads all kernels contained in the .xclbin file.
     * The file must exist and be a valid .xclbin format.
     *
     * @param path Path to .xclbin file (absolute or relative)
     * @return true if loaded successfully, false otherwise
     *
     * @throws std::runtime_error if file is invalid or loading fails
     */
    virtual bool load_xclbin(const std::string &path) = 0;

    /**
     * @brief Load .xclbin from memory buffer
     *
     * Allows loading .xclbin from a memory buffer instead of file.
     * Useful for embedded scenarios or custom loading logic.
     *
     * @param data Pointer to .xclbin data
     * @param size Size of data in bytes
     * @return true if loaded successfully, false otherwise
     *
     * @throws std::runtime_error if data is invalid or loading fails
     */
    virtual bool load_xclbin_from_memory(const void *data, size_t size) = 0;

    /**
     * @brief Unload specific .xclbin package
     *
     * Unloads kernels from a previously loaded .xclbin.
     * Use when you need to free memory but keep the runtime.
     *
     * @param path Path to .xclbin (must match load path)
     * @return true if unloaded successfully
     */
    virtual bool unload_xclbin(const std::string &path) = 0;

    /**
     * @brief Get list of available kernel names
     * @return Vector of kernel names (may be empty if nothing loaded)
     */
    virtual std::vector<std::string> get_kernel_names() const = 0;

    /**
     * @brief Get kernels from a specific .xclbin
     *
     * @param xclbin_path Path to .xclbin file
     * @return Vector of kernel names from that file
     */
    virtual std::vector<std::string> get_kernels_from_xclbin(const std::string &xclbin_path) const = 0;

    /**
     * @brief Check if a specific kernel is available
     * @param kernel_name Name of kernel to check
     * @return true if kernel is loaded and available
     */
    virtual bool has_kernel(const std::string &kernel_name) const = 0;

    /**
     * @brief Execute kernel with provided arguments
     *
     * Convenience method for one-off kernel execution.
     * For repeated execution, use get_kernel() for better performance.
     *
     * @param kernel_name Name of kernel to execute
     * @param arguments Kernel arguments (buffers and scalars)
     * @param options Execution options
     * @return ExecutionResult with status and outputs
     *
     * @throws std::runtime_error if kernel not found or execution fails
     */
    virtual ExecutionResult execute(const std::string &kernel_name,
                                    const std::vector<KernelArgument> &arguments,
                                    const ExecutionOptions &options = ExecutionOptions()) = 0;

    /**
     * @brief Create a kernel execution handle
     *
     * Returns a handle for repeated kernel execution with
     * different arguments. More efficient than execute() for
     * repeated calls.
     *
     * @param kernel_name Name of kernel
     * @return Kernel handle, or nullptr if kernel not found
     */
    virtual std::shared_ptr<IKernelHandle> get_kernel(const std::string &kernel_name) = 0;

    /**
     * @brief Allocate buffer for kernel I/O
     *
     * @param size Size in bytes
     * @param host_accessible If true, buffer is accessible from host
     * @return Shared pointer to buffer
     *
     * @throws std::runtime_error if allocation fails
     */
    virtual std::shared_ptr<IBuffer> allocate_buffer(size_t size, bool host_accessible = true) = 0;

    /**
     * @brief Allocate buffer from existing host data
     *
     * Creates a device buffer and copies initial data from host.
     *
     * @param data Pointer to host data
     * @param size Size in bytes
     * @return Shared pointer to buffer
     *
     * @throws std::runtime_error if allocation fails
     */
    virtual std::shared_ptr<IBuffer> allocate_buffer_from_data(const void *data, size_t size) = 0;

    /**
     * @brief Get buffer manager for efficient allocation
     * @return Shared pointer to buffer manager
     */
    virtual std::shared_ptr<IBufferManager> get_buffer_manager() = 0;

    /**
     * @brief Unload all kernels and free resources
     */
    virtual void unload() = 0;

    /**
     * @brief Check if runtime has loaded kernels
     * @return true if any kernels are loaded
     */
    virtual bool is_loaded() const = 0;

    /**
     * @brief Get platform name
     * @return "XRT" for Linux, "xDNA" for Windows
     */
    virtual std::string get_platform_name() const = 0;

    /**
     * @brief Get runtime version string
     * @return Version information (e.g., "2.15.0")
     */
    virtual std::string get_version() const = 0;

    /**
     * @brief Get underlying runtime version (XRT/xDNA)
     * @return Platform-specific version string
     */
    virtual std::string get_platform_version() const = 0;

    /**
     * @brief Check if NPU device is available
     * @return true if NPU is present and accessible
     */
    static bool is_device_available();

    /**
     * @brief Get list of available NPU devices
     * @return Vector of device IDs (usually [0] for single NPU)
     */
    static std::vector<int> get_available_devices();

    /**
     * @brief Create platform-appropriate runtime implementation
     *
     * Factory method that returns XrtRuntime on Linux
     * or XdnaRuntime on Windows.
     *
     * @param device_id Device ID (default: 0)
     * @return Unique pointer to runtime instance
     *
     * @throws std::runtime_error if no NPU device available
     */
    static std::unique_ptr<IXclbinRuntime> create(int device_id = 0);

    /**
     * @brief Create runtime with explicit platform selection
     *
     * Force a specific platform implementation (for testing).
     *
     * @param platform "XRT", "xDNA", or "mock"
     * @param device_id Device ID
     * @return Unique pointer to runtime instance
     */
    static std::unique_ptr<IXclbinRuntime> create_for_platform(const std::string &platform, int device_id = 0);
};

/**
 * @brief Exception for runtime errors
 */
class RuntimeError : public std::runtime_error
{
  public:
    explicit RuntimeError(const std::string &msg) : std::runtime_error(msg) {}

    RuntimeError(const std::string &msg, int error_code) : std::runtime_error(msg), error_code_(error_code) {}

    int error_code() const
    {
        return error_code_.value_or(-1);
    }

  private:
    std::optional<int> error_code_;
};

/**
 * @brief Exception for kernel not found
 */
class KernelNotFoundError : public RuntimeError
{
  public:
    explicit KernelNotFoundError(const std::string &kernel_name)
        : RuntimeError("Kernel not found: " + kernel_name), kernel_name_(kernel_name)
    {
    }

    const std::string &kernel_name() const
    {
        return kernel_name_;
    }

  private:
    std::string kernel_name_;
};

/**
 * @brief Exception for argument type mismatch
 */
class ArgumentError : public RuntimeError
{
  public:
    ArgumentError(const std::string &msg, size_t arg_index) : RuntimeError(msg), arg_index_(arg_index) {}

    size_t argument_index() const
    {
        return arg_index_.value_or(0);
    }

  private:
    std::optional<size_t> arg_index_;
};

} // namespace runtime
} // namespace iron
