// SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
// SPDX-License-Identifier: Apache-2.0

/**
 * @file pybind11_bindings.cpp
 * @brief Python bindings for IRON NPU Runtime using pybind11
 *
 * This file provides Python bindings for the IRON NPU C++ runtime,
 * allowing Python code to load and execute NPU kernels.
 *
 * BUILD REQUIREMENTS:
 * - pybind11 >= 2.10.0
 * - C++17 compatible compiler
 * - IRON NPU Runtime library (iron::runtime)
 *
 * USAGE:
 * @code
 * import iron.runtime
 *
 * runtime = iron.runtime.NpuRuntime.create()
 * runtime.load_xclbin("/path/to/kernel.xclbin")
 *
 * buffer = runtime.allocate_buffer(1024 * 1024)
 * kernel = runtime.get_kernel("my_kernel")
 * result = kernel.execute()
 * @endcode
 *
 * EXCEPTIONS:
 * C++ exceptions are translated to Python exceptions:
 * - RuntimeError -> iron.runtime.RuntimeError
 * - KernelNotFoundError -> iron.runtime.KernelNotFoundError
 * - BufferError -> iron.runtime.BufferError
 * - XclbinError -> iron.runtime.XclbinError
 * - DeviceNotAvailableError -> iron.runtime.DeviceNotAvailableError
 */

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>
#include <pybind11/operators.h>

#include <iron/runtime/npu_runtime.hpp>

namespace py = pybind11;
using namespace iron::runtime;

/**
 * @brief Translate C++ exceptions to Python exceptions
 *
 * Registers exception translators for all IRON runtime exception types.
 * Each C++ exception is re-raised as a corresponding Python exception.
 */
void register_exception_translators(py::module_& m) {
    // Base RuntimeError
    py::register_exception<RuntimeError>(m, "RuntimeError");

    // KernelNotFoundError
    py::register_exception<KernelNotFoundError>(m, "KernelNotFoundError");

    // ArgumentError
    py::register_exception<ArgumentError>(m, "ArgumentError");

    // BufferError
    py::register_exception<BufferError>(m, "BufferError");

    // XclbinError
    py::register_exception<XclbinError>(m, "XclbinError");

    // DeviceNotAvailableError
    py::register_exception<DeviceNotAvailableError>(m, "DeviceNotAvailableError");
}

/**
 * @brief Create buffer weak reference proxy
 *
 * Allows Python code to write/read buffer data as bytes
 */
py::bytes buffer_to_bytes(IBuffer& buffer) {
    auto size = buffer.size();
    std::vector<char> data(size);
    buffer.read(data.data(), size);
    return py::bytes(data.data(), size);
}

PYBIND11_MODULE(iron_runtime, m) {
    // Module documentation
    m.doc() = R"pbdoc(
        IRON NPU Runtime Python Bindings

        This module provides Python access to the IRON NPU runtime,
        enabling kernel loading and execution on AMD/Xilinx NPUs.

        Example:
            >>> import iron_runtime
            >>> runtime = iron_runtime.NpuRuntime.create()
            >>> runtime.load_xclbin("/path/to/kernel.xclbin")
            >>> kernel = runtime.get_kernel("my_kernel")
            >>> result = kernel.execute()

        Exceptions:
            RuntimeError: Base exception for runtime errors
            KernelNotFoundError: Raised when kernel is not found
            ArgumentError: Raised for invalid kernel arguments
            BufferError: Raised for buffer operation failures
            XclbinError: Raised for xclbin loading errors
            DeviceNotAvailableError: Raised when NPU device is unavailable
    )pbdoc";

    // Register exception translators
    register_exception_translators(m);

    // ==========================================================================
    // ExecutionOptions struct
    // ==========================================================================
    py::class_<ExecutionOptions>(m, "ExecutionOptions",
        R"pbdoc(
            Kernel execution options.

            Attributes:
                timeout_ms (int): Timeout in milliseconds (0 = default)
                profile (bool): Enable profiling to collect execution time
                synchronous (bool): Wait for completion if True
                priority (int): Priority level (0 = normal, higher = more priority)
                platform_options (Optional[str]): Platform-specific JSON options
                stream (Optional[int]): Execution stream for async operations

            Example:
                >>> opts = ExecutionOptions()
                >>> opts.timeout_ms = 5000
                >>> opts.profile = True
                >>> opts.synchronous = True
        )pbdoc")
        .def(py::init<>())
        .def_readwrite("timeout_ms", &ExecutionOptions::timeoutMs,
            "Timeout in milliseconds (0 = use default)")
        .def_readwrite("profile", &ExecutionOptions::profile,
            "Enable profiling to collect execution time")
        .def_readwrite("synchronous", &ExecutionOptions::synchronous,
            "Wait for completion if True")
        .def_readwrite("priority", &ExecutionOptions::priority,
            "Priority level (0 = normal, higher = more priority)")
        .def_readwrite("platform_options", &ExecutionOptions::platformOptions,
            "Platform-specific JSON options")
        // Fluent interface methods
        .def("with_timeout", &ExecutionOptions::withTimeout,
            py::arg("ms"),
            "Set timeout and return self for chaining")
        .def("with_profiling", &ExecutionOptions::withProfiling,
            py::arg("enable") = true,
            "Enable profiling and return self for chaining")
        .def("with_synchronous", &ExecutionOptions::withSynchronous,
            py::arg("sync") = true,
            "Set execution mode and return self for chaining");

    // ==========================================================================
    // ExecutionResult struct
    // ==========================================================================
    py::class_<ExecutionResult>(m, "ExecutionResult",
        R"pbdoc(
            Result of kernel execution.

            Attributes:
                status (int): Execution status code (0 = success)
                execution_time_us (Optional[int]): Execution time in microseconds
                error_message (Optional[str]): Error message if failed
                outputs (List[Buffer]): Output buffers if any
                platform_data (Optional[str]): Platform-specific data
                execution_id (Optional[int]): Execution ID for tracing

            Example:
                >>> result = kernel.execute()
                >>> if result.success:
                ...     print(f"Executed in {result.execution_time_us} us")
                ...     data = result.outputs[0].read()
        )pbdoc")
        .def(py::init<>())
        .def_readwrite("status", &ExecutionResult::status,
            "Execution status code (0 = success, non-zero = error)")
        .def_readwrite("execution_time_us", &ExecutionResult::executionTimeUs,
            "Execution time in microseconds")
        .def_readwrite("error_message", &ExecutionResult::errorMessage,
            "Error message if execution failed")
        .def_readwrite("outputs", &ExecutionResult::outputs,
            "Output buffers if any")
        .def_readwrite("platform_data", &ExecutionResult::platformData,
            "Platform-specific data")
        .def_readwrite("execution_id", &ExecutionResult::executionId,
            "Execution ID for tracing")
        .def_property_readonly("success", &ExecutionResult::success,
            "Check if execution was successful (status == 0)")
        .def("get_error_message", &ExecutionResult::getErrorMessage,
            "Get error message or empty string")
        .def("get_execution_time_us", &ExecutionResult::getExecutionTimeUs,
            "Get execution time in microseconds (0 if not profiled)");

    // ==========================================================================
    // IBuffer class
    // ==========================================================================
    py::class_<IBuffer, std::shared_ptr<IBuffer>>(m, "Buffer",
        R"pbdoc(
            Device memory buffer for NPU operations.

            Represents a buffer object (BO) in the NPU's memory space.
            Provides host-to-device and device-to-host data transfer.

            Example:
                >>> buffer = runtime.allocate_buffer(1024 * 1024)  # 1MB
                >>> buffer.write(b"\\x00\\x01\\x02\\x03")  # Write data
                >>> buffer.sync(True)  # Sync to device
                >>> data = buffer.read(4)  # Read 4 bytes
                >>> buffer.sync(False)  # Sync from device
        )pbdoc")
        .def("size", &IBuffer::size,
            "Get buffer size in bytes")
        .def("write", &IBuffer::write,
            py::arg("data"), py::arg("size"), py::arg("offset") = 0,
            R"pbdoc(
                Write data to buffer (host-to-device).

                Args:
                    data: Bytes-like object to write
                    size: Number of bytes to write
                    offset: Offset in destination buffer (default: 0)

                Raises:
                    BufferError: If write fails
            )pbdoc")
        .def("read",
            [](IBuffer& self, size_t size, size_t offset) -> py::bytes {
                std::vector<char> data(size);
                self.read(data.data(), size, offset);
                return py::bytes(data.data(), size);
            },
            py::arg("size"), py::arg("offset") = 0,
            R"pbdoc(
                Read data from buffer (device-to-host).

                Args:
                    size: Number of bytes to read
                    offset: Offset in source buffer (default: 0)

                Returns:
                    bytes: The read data

                Raises:
                    BufferError: If read fails
            )pbdoc")
        .def("sync", &IBuffer::sync,
            py::arg("to_device"),
            R"pbdoc(
                Sync buffer with device.

                Args:
                    to_device: If True, sync host-to-device; otherwise device-to-host

                Raises:
                    BufferError: If sync fails
            )pbdoc")
        .def("native_handle", &IBuffer::nativeHandle,
            R"pbdoc(
                Get native buffer handle (platform-specific).

                Returns:
                    int: Opaque handle for platform-specific operations

                Note:
                    Use this only for platform-specific operations
                    not covered by this interface.
            )pbdoc")
        .def("address", &IBuffer::address,
            "Get buffer address for kernel argument")
        .def("is_valid", &IBuffer::isValid,
            "Check if buffer is allocated and accessible")
        .def("__len__", &IBuffer::size,
            "Get buffer size in bytes")
        .def("__repr__", [](const IBuffer& self) {
            return "<Buffer size=" + std::to_string(self.size()) +
                   " valid=" + std::string(self.isValid() ? "True" : "False") + ">";
        });

    // ==========================================================================
    // IKernelHandle class
    // ==========================================================================
    py::class_<IKernelHandle, std::shared_ptr<IKernelHandle>>(m, "KernelHandle",
        R"pbdoc(
            Handle for repeated kernel execution.

            Provides an efficient interface for kernels that need to be executed
            multiple times with different arguments. Avoids repeated kernel
            lookup and validation overhead.

            Example:
                >>> kernel = runtime.get_kernel("gemm_kernel")
                >>> kernel.set_arg(0, buffer_a)
                >>> kernel.set_arg(1, buffer_b)
                >>> kernel.set_arg(2, buffer_c)
                >>> result = kernel.execute()
                >>> kernel.reset()  # Clear arguments for reuse
        )pbdoc")
        .def("name", &IKernelHandle::name,
            "Get kernel name")
        .def("set_arg", &IKernelHandle::setArg,
            py::arg("index"), py::arg("arg"),
            R"pbdoc(
                Set kernel argument.

                Args:
                    index: Argument index (0-based)
                    arg: Argument value (Buffer, int, or float)

                Raises:
                    ArgumentError: If index is invalid or type mismatch
            )pbdoc")
        .def("execute", &IKernelHandle::execute,
            py::arg("options") = ExecutionOptions(),
            R"pbdoc(
                Execute kernel with set arguments.

                Args:
                    options: Execution options (optional)

                Returns:
                    ExecutionResult: Status and metadata

                Raises:
                    RuntimeError: If execution fails
            )pbdoc")
        .def("executeAndWait", &IKernelHandle::executeAndWait,
            py::arg("timeout_ms") = 0,
            R"pbdoc(
                Execute and wait for completion.

                Args:
                    timeout_ms: Timeout in milliseconds

                Returns:
                    ExecutionResult: Status and metadata
            )pbdoc")
        .def("reset", &IKernelHandle::reset,
            "Reset all arguments to default state")
        .def("num_arguments", &IKernelHandle::numArguments,
            "Get number of kernel arguments")
        .def("is_ready", &IKernelHandle::isReady,
            "Check if all required arguments are set")
        .def("get_argument_info", &IKernelHandle::getArgumentInfo,
            py::arg("index"),
            "Get argument info (name, type) for debugging")
        .def("get_argument_names", &IKernelHandle::getArgumentNames,
            "Get all argument names")
        .def("is_argument_set", &IKernelHandle::isArgumentSet,
            py::arg("index"),
            "Check if specific argument is set")
        .def("__repr__", [](const IKernelHandle& self) {
            return "<KernelHandle name='" + self.name() +
                   "' ready=" + std::string(self.isReady() ? "True" : "False") + ">";
        });

    // ==========================================================================
    // IBufferManager class
    // ==========================================================================
    py::class_<IBufferManager, std::shared_ptr<IBufferManager>>(m, "BufferManager",
        R"pbdoc(
            Buffer manager for efficient memory allocation.

            Manages a pool of buffers to avoid repeated allocation/deallocation
            overhead. Useful for repeated kernel invocations with similar
            buffer size requirements.

            Example:
                >>> manager = runtime.get_buffer_manager()
                >>> buf1 = manager.allocate(1024 * 1024)  # 1MB
                >>> manager.deallocate(buf1)  # Return to pool
                >>> buf2 = manager.allocate(1024 * 1024)  # Reuses pooled buffer
        )pbdoc")
        .def("allocate", &IBufferManager::allocate,
            py::arg("size"),
            R"pbdoc(
                Allocate buffer from pool.

                Args:
                    size: Minimum buffer size needed (bytes)

                Returns:
                    Buffer: Shared pointer to buffer
            )pbdoc")
        .def("deallocate", &IBufferManager::deallocate,
            py::arg("buffer"),
            R"pbdoc(
                Return buffer to pool for reuse.

                Args:
                    buffer: Buffer to return
            )pbdoc")
        .def("get_pool_stats", &IBufferManager::getPoolStats,
            R"pbdoc(
                Get pool statistics.

                Returns:
                    Dict[int, int]: Map of buffer size to count of available buffers
            )pbdoc")
        .def("clear", &IBufferManager::clear,
            "Clear all buffers from pool")
        .def("total_memory_in_use", &IBufferManager::totalMemoryInUse,
            "Get total memory in use (pooled + allocated)")
        .def("active_buffer_count", &IBufferManager::activeBufferCount,
            "Get number of active (non-pooled) buffers")
        .def("pooled_buffer_count", &IBufferManager::pooledBufferCount,
            "Get number of pooled (available) buffers")
        .def("set_max_pool_size", &IBufferManager::setMaxPoolSize,
            py::arg("max_bytes"),
            "Set maximum pool size in bytes");

    // ==========================================================================
    // INpuRuntime class
    // ==========================================================================
    py::class_<INpuRuntime, std::unique_ptr<INpuRuntime>>(m, "NpuRuntime",
        R"pbdoc(
            Main NPU runtime interface.

            This class provides platform-agnostic kernel loading and execution.
            Use create() to get the appropriate implementation for your platform.

            Platform Detection:
                - Linux: Uses XRT (Xilinx Runtime)
                - Windows: Uses xDNA runtime

            Example:
                >>> import iron_runtime
                >>> runtime = iron_runtime.NpuRuntime.create()
                >>> runtime.load_xclbin("/path/to/kernel.xclbin")
                >>> print(runtime.kernel_names)
                ['kernel_1', 'kernel_2']
        )pbdoc")
        // Xclbin loading methods
        .def("load_xclbin", &INpuRuntime::loadXclbin,
            py::arg("path"),
            R"pbdoc(
                Load .xclbin kernel package.

                Loads all kernels contained in the .xclbin file.

                Args:
                    path: Path to .xclbin file

                Returns:
                    bool: True if loaded successfully

                Raises:
                    XclbinError: If file is invalid or loading fails
            )pbdoc")
        .def("load_xclbin_from_memory", &INpuRuntime::loadXclbinFromMemory,
            py::arg("data"), py::arg("size"),
            R"pbdoc(
                Load .xclbin from memory buffer.

                Args:
                    data: Bytes containing .xclbin data
                    size: Size of data in bytes

                Returns:
                    bool: True if loaded successfully

                Raises:
                    XclbinError: If data is invalid or loading fails
            )pbdoc")
        .def("unload_xclbin", &INpuRuntime::unloadXclbin,
            py::arg("path"),
            R"pbdoc(
                Unload specific .xclbin package.

                Args:
                    path: Path to .xclbin (must match load path)

                Returns:
                    bool: True if unloaded successfully
            )pbdoc")
        .def_property_readonly("kernel_names", &INpuRuntime::getKernelNames,
            "Get list of available kernel names")
        .def("get_kernels_from_xclbin", &INpuRuntime::getKernelsFromXclbin,
            py::arg("xclbin_path"),
            "Get kernels from a specific .xclbin")
        .def("has_kernel", &INpuRuntime::hasKernel,
            py::arg("kernel_name"),
            "Check if a specific kernel is available")
        // Kernel execution methods
        .def("execute",
            [](INpuRuntime& self, const std::string& kernel_name,
               const std::vector<KernelArgument>& args,
               const ExecutionOptions& options) {
                return self.execute(kernel_name, args, options);
            },
            py::arg("kernel_name"), py::arg("arguments"),
            py::arg("options") = ExecutionOptions(),
            R"pbdoc(
                Execute kernel with provided arguments.

                Convenience method for one-off kernel execution.
                For repeated execution, use get_kernel() for better performance.

                Args:
                    kernel_name: Name of kernel to execute
                    arguments: Kernel arguments (Buffers and scalars)
                    options: Execution options

                Returns:
                    ExecutionResult: Status and outputs

                Raises:
                    KernelNotFoundError: If kernel not found
                    RuntimeError: If execution fails
            )pbdoc")
        .def("get_kernel", &INpuRuntime::getKernel,
            py::arg("kernel_name"),
            R"pbdoc(
                Create a kernel execution handle.

                Returns a handle for repeated kernel execution with
                different arguments. More efficient than execute() for
                repeated calls.

                Args:
                    kernel_name: Name of kernel

                Returns:
                    KernelHandle: Kernel handle for execution

                Note:
                    Returned handle is NOT thread-safe.
            )pbdoc")
        // Buffer management methods
        .def("allocate_buffer", &INpuRuntime::allocateBuffer,
            py::arg("size"), py::arg("host_accessible") = true,
            R"pbdoc(
                Allocate buffer for kernel I/O.

                Args:
                    size: Size in bytes
                    host_accessible: If True, buffer is accessible from host

                Returns:
                    Buffer: Shared pointer to buffer

                Raises:
                    BufferError: If allocation fails
            )pbdoc")
        .def("allocate_buffer_from_data",
            [](INpuRuntime& self, const py::bytes& data) {
                auto buffer_info = py::buffer::ensure_object(data).request();
                return self.allocateBufferFromData(buffer_info.ptr, buffer_info.size);
            },
            py::arg("data"),
            R"pbdoc(
                Allocate buffer from existing host data.

                Creates a device buffer and copies initial data from host.

                Args:
                    data: Bytes-like object

                Returns:
                    Buffer: Shared pointer to buffer

                Raises:
                    BufferError: If allocation fails
            )pbdoc")
        .def("get_buffer_manager", &INpuRuntime::getBufferManager,
            R"pbdoc(
                Get buffer manager for efficient allocation.

                Returns:
                    BufferManager: Shared pointer to buffer manager
            )pbdoc")
        // Runtime management methods
        .def("unload", &INpuRuntime::unload,
            "Unload all kernels and free resources")
        .def_property_readonly("is_loaded", &INpuRuntime::isLoaded,
            "Check if runtime has loaded kernels")
        .def("get_platform_name", &INpuRuntime::getPlatformName,
            "Get platform name (XRT for Linux, xDNA for Windows)")
        .def("get_version", &INpuRuntime::getVersion,
            "Get IRON runtime version string")
        .def("get_platform_version", &INpuRuntime::getPlatformVersion,
            "Get underlying runtime version (XRT/xDNA)")
        .def("get_device_info", &INpuRuntime::getDeviceInfo,
            "Get device information as JSON string")
        // Static factory methods
        .def_static("create", &INpuRuntime::create,
            py::arg("device_id") = 0,
            R"pbdoc(
                Create platform-appropriate runtime implementation.

                Factory method that returns XrtRuntimeWrapper on Linux
                or XdnaRuntime on Windows.

                Args:
                    device_id: Device ID (default: 0)

                Returns:
                    NpuRuntime: Runtime instance

                Raises:
                    DeviceNotAvailableError: If no NPU device available
            )pbdoc")
        .def_static("create_for_platform", &INpuRuntime::createForPlatform,
            py::arg("platform"), py::arg("device_id") = 0,
            R"pbdoc(
                Create runtime with explicit platform selection.

                Force a specific platform implementation (for testing).

                Args:
                    platform: "XRT", "xDNA", or "mock"
                    device_id: Device ID (default: 0)

                Returns:
                    NpuRuntime: Runtime instance

                Raises:
                    RuntimeError: If platform not supported
            )pbdoc")
        .def_static_property_readonly("current_platform", &INpuRuntime::getCurrentPlatform,
            "Get current platform string ('linux', 'windows', or 'unknown')")
        .def_static_property_readonly("is_linux", &INpuRuntime::isLinux,
            "Check if running on Linux")
        .def_static_property_readonly("is_windows", &INpuRuntime::isWindows,
            "Check if running on Windows")
        .def_static("is_device_available", &INpuRuntime::isDeviceAvailable,
            "Check if NPU device is available")
        .def_static("get_available_devices", &INpuRuntime::getAvailableDevices,
            "Get list of available NPU devices")
        .def("__repr__", [](const INpuRuntime& self) {
            return "<NpuRuntime platform='" + self.getPlatformName() +
                   "' version='" + self.getVersion() +
                   "' loaded=" + std::string(self.isLoaded() ? "True" : "False") + ">";
        });

    // ==========================================================================
    // Module-level functions
    // ==========================================================================
    m.def("get_version", &getIronRuntimeVersion,
        R"pbdoc(
            Get IRON runtime version.

            Returns:
                str: Version string (e.g., "1.0.0")
        )pbdoc");

    m.def("get_version_tuple",
        [](int& major, int& minor, int& patch) {
            getIronRuntimeVersion(major, minor, patch);
            return std::make_tuple(major, minor, patch);
        },
        R"pbdoc(
            Get IRON runtime version as tuple.

            Returns:
                tuple: (major, minor, patch) version numbers
        )pbdoc");

    // Version info
#ifdef PYBIND11_VERSION_MAJOR
    m.attr("__version__") = "1.0.0";
#endif

    // Platform info
#if defined(IRON_PLATFORM_WINDOWS) && IRON_PLATFORM_WINDOWS
    m.attr("PLATFORM") = "windows";
#else
    m.attr("PLATFORM") = "linux";
#endif

#if defined(IRON_HAS_XRT) && IRON_HAS_XRT
    m.attr("HAS_XRT") = 1;
#else
    m.attr("HAS_XRT") = 0;
#endif

#if defined(IRON_HAS_XDNA) && IRON_HAS_XDNA
    m.attr("HAS_XDNA") = 1;
#else
    m.attr("HAS_XDNA") = 0;
#endif
}
