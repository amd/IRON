# IRON NPU Runtime C++ Library

## Overview

The IRON NPU Runtime C++ library provides a unified, modern C++17 interface for executing kernels on AMD Ryzen AI NPUs. It abstracts the platform-specific backends:

- **Linux**: XRT (Xilinx Runtime) backend
- **Windows**: xDNA runtime backend

## Directory Structure

```
cpp/
├── CMakeLists.txt              # Build configuration
├── cmake/
│   └── iron_runtime_config.cmake.in  # CMake package config
├── include/
│   └── iron/
│       └── runtime/
│           ├── npu_runtime.hpp       # Main interface (required)
│           ├── platform_utils.hpp    # Platform utilities
│           ├── xdna_runtime.hpp      # Windows backend header
│           └── xrt_runtime_wrapper.hpp # Linux backend header
└── src/
    ├── npu_runtime.cpp         # Base implementation
    ├── platform_utils.cpp      # Platform utilities
    ├── xdna_runtime_impl.cpp   # Windows backend implementation
    └── xrt_runtime_impl.cpp    # Linux backend implementation
```

## Quick Start

### Basic Usage

```cpp
#include <iron/runtime/npu_runtime.hpp>

using namespace iron::runtime;

int main() {
    // Create runtime (auto-detects platform)
    auto runtime = NpuRuntime::create();

    // Load kernel package
    runtime->loadXclbin("/path/to/kernel.xclbin");

    // Allocate buffers
    auto buffer_a = runtime->allocateBuffer(1024 * 1024);
    auto buffer_b = runtime->allocateBuffer(1024 * 1024);
    auto buffer_c = runtime->allocateBuffer(1024 * 1024);

    // Write input data
    buffer_a->write(host_data_a, size_a);
    buffer_b->write(host_data_b, size_b);

    // Get kernel handle and set arguments
    auto kernel = runtime->getKernel("gemm_kernel");
    kernel->setArg(0, buffer_a);
    kernel->setArg(1, buffer_b);
    kernel->setArg(2, buffer_c);
    kernel->setArg(3, static_cast<int32_t>(M));
    kernel->setArg(4, static_cast<int32_t>(K));
    kernel->setArg(5, static_cast<int32_t>(N));

    // Execute
    auto result = kernel->execute();
    if (result.success()) {
        // Read output
        buffer_c->read(host_data_c, size_c);
    }

    return 0;
}
```

### Building

```bash
# Create build directory
mkdir build && cd build

# Configure
cmake .. -DCMAKE_BUILD_TYPE=Release

# Build
cmake --build . --config Release

# Install
cmake --install . --prefix /usr/local
```

### Using in Your Project

```cmake
find_package(iron_runtime REQUIRED)
target_link_libraries(your_target PRIVATE iron::runtime)
```

## Key Components

### INpuRuntime (Main Interface)

The primary interface for NPU operations:

- `loadXclbin(path)` - Load kernel package
- `allocateBuffer(size)` - Allocate device memory
- `getKernel(name)` - Get kernel execution handle
- `execute(name, args)` - One-off kernel execution
- `getBufferManager()` - Get buffer pool manager

### IBuffer

Device memory buffer interface:

- `write(data, size, offset)` - Host-to-device transfer
- `read(data, size, offset)` - Device-to-host transfer
- `sync(to_device)` - Sync buffer with device
- `address()` - Get device address for kernel args

### IKernelHandle

Kernel execution handle:

- `setArg(index, value)` - Set kernel argument
- `execute(options)` - Execute kernel
- `isReady()` - Check if all args are set
- `reset()` - Clear all arguments

### IBufferManager

Buffer pooling for efficient allocation:

- `allocate(size)` - Get buffer from pool
- `deallocate(buffer)` - Return buffer to pool
- `getPoolStats()` - Get pool statistics

## Build Options

| Option | Default | Description |
|--------|---------|-------------|
| `IRON_BUILD_SHARED` | ON | Build shared library |
| `IRON_BUILD_TESTS` | OFF | Build test suite |
| `IRON_BUILD_EXAMPLES` | OFF | Build example programs |
| `IRON_USE_XRT` | ON (Linux) | Enable XRT backend |
| `IRON_USE_XDNA` | ON (Windows) | Enable xDNA backend |
| `IRON_ENABLE_COVERAGE` | OFF | Enable code coverage |
| `IRON_ENABLE_SANITIZER` | OFF | Enable sanitizers |

## Error Handling

The library uses exceptions for error handling:

- `RuntimeError` - Base exception for all runtime errors
- `KernelNotFoundError` - Kernel not found
- `ArgumentError` - Invalid argument type or index
- `BufferError` - Buffer operation failed
- `XclbinError` - Xclbin loading failed
- `DeviceNotAvailableError` - NPU device not available

```cpp
try {
    auto runtime = NpuRuntime::create();
    runtime->loadXclbin("kernel.xclbin");
} catch (const KernelNotFoundError& e) {
    std::cerr << "Kernel not found: " << e.kernelName() << std::endl;
} catch (const DeviceNotAvailableError& e) {
    std::cerr << "Device " << e.deviceId() << " not available" << std::endl;
} catch (const RuntimeError& e) {
    std::cerr << "Runtime error: " << e.what() << std::endl;
}
```

## Thread Safety

- **Runtime instance**: NOT thread-safe by default. Use external synchronization.
- **Buffer**: Thread-safe for concurrent reads; writes are serialized.
- **Kernel Handle**: NOT thread-safe. Create separate handles for concurrent use.
- **Buffer Manager**: Thread-safe allocation/deallocation.
- **Static methods**: All thread-safe.

## Platform Detection

```cpp
// Compile-time detection
if constexpr (iron::runtime::INpuRuntime::isLinux()) {
    // Linux-specific code
}

// Runtime detection
if (NpuRuntime::isDeviceAvailable()) {
    auto runtime = NpuRuntime::create();
}
```

## License

Apache 2.0 License
