# IRON NPU Runtime - Python Bindings

Python bindings for the IRON NPU Runtime using pybind11.

## Overview

This package provides Python access to the IRON NPU runtime, enabling kernel loading and execution on AMD/Xilinx NPUs from Python code.

### Platform Support

| Platform | Backend | Status |
|----------|---------|--------|
| Linux    | XRT (Xilinx Runtime) | Supported |
| Windows  | xDNA Runtime | Supported |

## Installation

### Prerequisites

- Python 3.8 or higher
- CMake 3.16 or higher
- C++17 compatible compiler (GCC 8+, Clang 7+, MSVC 2019+)
- pybind11 2.10 or higher
- IRON NPU Runtime C++ library

### Building from Source

```bash
# Clone the repository
git clone https://github.com/iron-project/iron.git
cd iron/runtime/python

# Create build directory
mkdir build && cd build

# Configure with CMake
cmake .. -DCMAKE_BUILD_TYPE=Release

# Build the module
cmake --build . --config Release

# Install (optional)
cmake --install . --prefix /path/to/install
```

### Building with Specific Python Version

```bash
cmake .. -DPYTHON_VERSION=3.9
```

### Building with Custom pybind11 Path

```bash
cmake .. -DIRON_PYBIND11_PATH=/path/to/pybind11
```

## Quick Start

```python
import iron.runtime

# Create runtime instance
runtime = iron.runtime.NpuRuntime.create()

# Load kernel package
runtime.load_xclbin("/path/to/kernel.xclbin")

# Get kernel handle
kernel = runtime.get_kernel("my_kernel")

# Allocate buffers
input_buffer = runtime.allocate_buffer(1024 * 1024)
output_buffer = runtime.allocate_buffer(1024 * 1024)

# Set arguments and execute
kernel.set_arg(0, input_buffer)
kernel.set_arg(1, output_buffer)
kernel.set_arg(2, 64)  # Scalar argument

result = kernel.execute()

if result.success:
    print(f"Execution completed in {result.execution_time_us} us")
    data = output_buffer.read(1024)
else:
    print(f"Execution failed: {result.error_message}")
```

## API Reference

### NpuRuntime

Main runtime interface for kernel loading and execution.

#### Class Methods

```python
# Create runtime for current platform
runtime = NpuRuntime.create(device_id=0)

# Create runtime for specific platform
runtime = NpuRuntime.create_for_platform("XRT", device_id=0)
runtime = NpuRuntime.create_for_platform("xDNA", device_id=0)

# Check platform
platform = NpuRuntime.current_platform  # "linux" or "windows"
is_linux = NpuRuntime.is_linux
is_windows = NpuRuntime.is_windows

# Check device availability
available = NpuRuntime.is_device_available()
devices = NpuRuntime.get_available_devices()
```

#### Instance Methods

```python
# Load xclbin
runtime.load_xclbin("/path/to/kernel.xclbin")
runtime.load_xclbin_from_memory(data, size)
runtime.unload_xclbin("/path/to/kernel.xclbin")

# Query kernels
names = runtime.kernel_names
names = runtime.get_kernels_from_xclbin("/path/to/kernel.xclbin")
has_kernel = runtime.has_kernel("my_kernel")

# Get kernel handle
kernel = runtime.get_kernel("my_kernel")

# Allocate buffers
buffer = runtime.allocate_buffer(size)
buffer = runtime.allocate_buffer_from_data(data)

# Get buffer manager
manager = runtime.get_buffer_manager()

# Execute kernel directly
result = runtime.execute("kernel_name", [arg1, arg2, arg3])

# Runtime info
runtime.unload()
loaded = runtime.is_loaded
platform = runtime.get_platform_name()
version = runtime.get_version()
platform_version = runtime.get_platform_version()
device_info = runtime.get_device_info()
```

### Buffer

Device memory buffer for NPU operations.

```python
# Get buffer info
size = buffer.size()
valid = buffer.is_valid()
address = buffer.address()
handle = buffer.native_handle()

# Write data
buffer.write(data, size, offset=0)

# Read data
data = buffer.read(size, offset=0)

# Sync buffer
buffer.sync(to_device=True)   # Host to device
buffer.sync(to_device=False)  # Device to host

# Python convenience
length = len(buffer)  # Same as size()
```

### KernelHandle

Handle for repeated kernel execution.

```python
# Get kernel info
name = kernel.name()
num_args = kernel.num_arguments()
arg_names = kernel.get_argument_names()
info = kernel.get_argument_info(index)

# Set arguments
kernel.set_arg(index, buffer)
kernel.set_arg(index, 42)       # int
kernel.set_arg(index, 3.14)     # float

# Check readiness
ready = kernel.is_ready()
is_set = kernel.is_argument_set(index)

# Execute
result = kernel.execute()
result = kernel.execute(options)
result = kernel.execute_and_wait(timeout_ms=5000)

# Reset for reuse
kernel.reset()
```

### ExecutionOptions

Kernel execution options.

```python
options = ExecutionOptions()
options.timeout_ms = 5000
options.profile = True
options.synchronous = True
options.priority = 0

# Fluent interface
options = (ExecutionOptions()
    .with_timeout(5000)
    .with_profiling(True)
    .with_synchronous(True))
```

### ExecutionResult

Result of kernel execution.

```python
# Check status
success = result.success
status = result.status

# Get timing
time_us = result.execution_time_us
time_us = result.get_execution_time_us()

# Get error info
error = result.error_message
error = result.get_error_message()

# Get outputs
outputs = result.outputs
```

### BufferManager

Buffer pool manager for efficient allocation.

```python
manager = runtime.get_buffer_manager()

# Allocate from pool
buffer = manager.allocate(size)

# Return to pool
manager.deallocate(buffer)

# Get statistics
stats = manager.get_pool_stats()
total = manager.total_memory_in_use()
active = manager.active_buffer_count()
pooled = manager.pooled_buffer_count()

# Clear pool
manager.clear()
manager.set_max_pool_size(256 * 1024 * 1024)
```

## Exception Handling

The Python bindings translate C++ exceptions to Python exceptions:

```python
import iron.runtime

try:
    runtime = iron.runtime.NpuRuntime.create()
    runtime.load_xclbin("/path/to/kernel.xclbin")
except iron.runtime.DeviceNotAvailableError as e:
    print(f"NPU device not available: {e}")
except iron.runtime.XclbinError as e:
    print(f"Failed to load xclbin: {e}")
except iron.runtime.KernelNotFoundError as e:
    print(f"Kernel not found: {e}")
except iron.runtime.BufferError as e:
    print(f"Buffer operation failed: {e}")
except iron.runtime.ArgumentError as e:
    print(f"Invalid argument: {e}")
except iron.runtime.RuntimeError as e:
    print(f"Runtime error: {e}")
```

## Advanced Usage

### Using Context Manager

```python
from iron.runtime import RuntimeContext

with RuntimeContext("/path/to/kernel.xclbin") as runtime:
    kernel = runtime.get_kernel("my_kernel")
    result = kernel.execute()
# Runtime automatically unloaded
```

### High-Level Execution Helper

```python
from iron.runtime import execute_kernel, create_runtime

runtime = create_runtime()
runtime.load_xclbin("/path/to/kernel.xclbin")

result = execute_kernel(
    runtime,
    "gemm_kernel",
    [buffer_a, buffer_b, buffer_c, 64],
    timeout_ms=5000,
    profile=True
)
```

### Quick Start Helper

```python
from iron.runtime import quick_start

runtime = quick_start("/path/to/kernel.xclbin")
kernel = runtime.get_kernel("my_kernel")
```

### Repeated Kernel Execution

```python
runtime = iron.runtime.NpuRuntime.create()
runtime.load_xclbin("/path/to/kernel.xclbin")

kernel = runtime.get_kernel("my_kernel")

# Execute multiple times with different inputs
for i in range(iterations):
    kernel.set_arg(0, input_buffers[i])
    kernel.set_arg(1, weight_buffer)
    kernel.set_arg(2, output_buffers[i])
    result = kernel.execute()
    kernel.reset()
```

### Buffer Pooling

```python
runtime = iron.runtime.NpuRuntime.create()
manager = runtime.get_buffer_manager()

# First allocation (creates new buffer)
buf1 = manager.allocate(1024 * 1024)

# Use buffer...
buf1.write(initial_data)

# Return to pool
manager.deallocate(buf1)

# Second allocation (reuses pooled buffer)
buf2 = manager.allocate(1024 * 1024)  # Gets same buffer
```

## Examples

### Matrix Multiplication (GEMM)

```python
import iron.runtime
import numpy as np

# Create runtime
runtime = iron.runtime.quick_start("/path/to/gemm_kernel.xclbin")

# Create test data
size = 64
a_data = np.random.rand(size, size).astype(np.float32).tobytes()
b_data = np.random.rand(size, size).astype(np.float32).tobytes()

# Allocate buffers
buffer_a = runtime.allocate_buffer(len(a_data))
buffer_b = runtime.allocate_buffer(len(b_data))
buffer_c = runtime.allocate_buffer(len(a_data))  # Output

# Write input data
buffer_a.write(a_data, len(a_data))
buffer_b.write(b_data, len(b_data))

# Get kernel and set arguments
kernel = runtime.get_kernel("gemm_kernel")
kernel.set_arg(0, buffer_a)
kernel.set_arg(1, buffer_b)
kernel.set_arg(2, buffer_c)
kernel.set_arg(3, size)

# Execute with profiling
options = iron.runtime.ExecutionOptions().with_profiling(True)
result = kernel.execute(options)

if result.success:
    # Read output
    output_data = buffer_c.read(size * size * 4)  # 4 bytes per float32
    output = np.frombuffer(output_data, dtype=np.float32).reshape(size, size)
    print(f"Execution time: {result.execution_time_us} us")
else:
    print(f"Execution failed: {result.error_message}")
```

### Batch Processing

```python
import iron.runtime

runtime = iron.runtime.NpuRuntime.create()
runtime.load_xclbin("/path/to/batch_kernel.xclbin")

# Pre-allocate all buffers
buffers = [runtime.allocate_buffer(buffer_size) for _ in range(num_items)]

# Get kernel handle once
kernel = runtime.get_kernel("batch_kernel")

# Process all items
for i, data in enumerate(input_data):
    # Write input
    buffers[i % len(buffers)].write(data, len(data))

    # Set argument and execute
    kernel.set_arg(0, buffers[i % len(buffers)])
    result = kernel.execute()

    if not result.success:
        print(f"Item {i} failed: {result.error_message}")
        break

    kernel.reset()

# Cleanup
runtime.unload()
```

## Troubleshooting

### ImportError: Could not import iron_runtime

Make sure the compiled module is in your Python path:

```bash
# Copy module to site-packages
cp build/iron_runtime*.so $(python -c "import site; print(site.getsitepackages()[0])")

# Or add build directory to PYTHONPATH
export PYTHONPATH=/path/to/build:$PYTHONPATH
```

### DeviceNotAvailableError

- Ensure NPU drivers are installed
- Check that the device is accessible: `lspci | grep -i npu` (Linux)
- Verify XRT installation: `xbutil examine` (Linux)

### XclbinError

- Verify the .xclbin file exists and is valid
- Ensure the .xclbin is compatible with your NPU device
- Check file permissions

## Development

### Running Tests

```bash
# Build with tests enabled
cmake .. -DIRON_BUILD_PYTHON_TESTS=ON

# Build
cmake --build .

# Run tests
cmake --build . --target test_python
```

### Building Wheel

```bash
cmake .. -DIRON_BUILD_WHEEL=ON
cmake --build . --target wheel

# Install wheel
pip install dist/iron_runtime-*.whl
```

## License

Apache 2.0 - See LICENSE file for details.

## Contributing

Contributions are welcome! Please submit issues and pull requests to the main repository.
