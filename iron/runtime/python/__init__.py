# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""
IRON NPU Runtime Python Package.

This package provides Python access to the IRON NPU runtime,
enabling kernel loading and execution on AMD/Xilinx NPUs.

Platform Support:
    - Linux: XRT (Xilinx Runtime) backend
    - Windows: xDNA runtime backend

Example:
    >>> import iron.runtime
    >>> # Create runtime instance
    >>> runtime = iron.runtime.NpuRuntime.create()
    >>> # Load kernel package
    >>> runtime.load_xclbin("/path/to/kernel.xclbin")
    >>> # Get kernel handle
    >>> kernel = runtime.get_kernel("my_kernel")
    >>> # Allocate buffers
    >>> input_buffer = runtime.allocate_buffer(1024 * 1024)
    >>> output_buffer = runtime.allocate_buffer(1024 * 1024)
    >>> # Set arguments and execute
    >>> kernel.set_arg(0, input_buffer)
    >>> kernel.set_arg(1, output_buffer)
    >>> result = kernel.execute()
    >>> if result.success:
    ...     data = output_buffer.read(1024)

Exceptions:
    RuntimeError: Base exception for runtime errors
    KernelNotFoundError: Raised when kernel is not found
    ArgumentError: Raised for invalid kernel arguments
    BufferError: Raised for buffer operation failures
    XclbinError: Raised for xclbin loading errors
    DeviceNotAvailableError: Raised when NPU device is unavailable

Classes:
    NpuRuntime: Main runtime interface
    Buffer: Device memory buffer
    KernelHandle: Kernel execution handle
    BufferManager: Buffer pool manager
    ExecutionOptions: Kernel execution options
    ExecutionResult: Kernel execution result
"""

from __future__ import annotations

import os
import sys
from typing import Optional, List, Dict, Any, Union

# Import compiled extension module
try:
    from .iron_runtime import (
        # Main classes
        NpuRuntime,
        Buffer,
        KernelHandle,
        BufferManager,
        # Data structures
        ExecutionOptions,
        ExecutionResult,
        # Version info
        get_version,
        get_version_tuple,
        # Platform info
        PLATFORM,
        HAS_XRT,
        HAS_XDNA,
        # Exceptions
        RuntimeError,
        KernelNotFoundError,
        ArgumentError,
        BufferError,
        XclbinError,
        DeviceNotAvailableError,
    )
except ImportError as e:
    # Provide helpful error message
    raise ImportError(
        f"Could not import iron_runtime extension module: {e}\n"
        f"Platform: {sys.platform}\n"
        f"Python path: {sys.path}\n"
        f"\n"
        f"Make sure the iron_runtime extension module is compiled and installed.\n"
        f"See README.md for build instructions."
    ) from e

# Module metadata
__version__ = "1.0.0"
__author__ = "Jordan Lee"
__all__ = [
    # Main classes
    "NpuRuntime",
    "Buffer",
    "KernelHandle",
    "BufferManager",
    # Data structures
    "ExecutionOptions",
    "ExecutionResult",
    # Version functions
    "get_version",
    "get_version_tuple",
    # Platform info
    "PLATFORM",
    "HAS_XRT",
    "HAS_XDNA",
    # Exceptions
    "RuntimeError",
    "KernelNotFoundError",
    "ArgumentError",
    "BufferError",
    "XclbinError",
    "DeviceNotAvailableError",
]


# Convenience functions
def create_runtime(device_id: int = 0) -> NpuRuntime:
    """
    Create NPU runtime instance.

    Convenience wrapper around NpuRuntime.create().

    Args:
        device_id: Device ID (default: 0)

    Returns:
        NpuRuntime: Runtime instance

    Example:
        >>> runtime = create_runtime()
        >>> runtime = create_runtime(device_id=0)
    """
    return NpuRuntime.create(device_id)


def is_device_available() -> bool:
    """
    Check if NPU device is available.

    Returns:
        bool: True if NPU is present and accessible
    """
    return NpuRuntime.is_device_available()


def get_platform() -> str:
    """
    Get current platform string.

    Returns:
        str: 'linux', 'windows', or 'unknown'
    """
    return NpuRuntime.current_platform


# Version compatibility
def version() -> tuple:
    """
    Get IRON runtime version as tuple.

    Returns:
        tuple: (major, minor, patch) version numbers
    """
    return get_version_tuple()


def version_string() -> str:
    """
    Get IRON runtime version as string.

    Returns:
        str: Version string (e.g., "1.0.0")
    """
    return get_version()


# Context manager for runtime
class RuntimeContext:
    """
    Context manager for NPU runtime.

    Automatically loads and unloads xclbin files.

    Example:
        >>> with RuntimeContext("/path/to/kernel.xclbin") as runtime:
        ...     kernel = runtime.get_kernel("my_kernel")
        ...     result = kernel.execute()
    """

    def __init__(self, xclbin_path: Optional[str] = None, device_id: int = 0):
        """
        Initialize runtime context.

        Args:
            xclbin_path: Path to .xclbin file (optional)
            device_id: Device ID (default: 0)
        """
        self.runtime: Optional[NpuRuntime] = None
        self.xclbin_path = xclbin_path
        self.device_id = device_id

    def __enter__(self) -> NpuRuntime:
        """Create runtime and load xclbin."""
        self.runtime = NpuRuntime.create(self.device_id)
        if self.xclbin_path:
            self.runtime.load_xclbin(self.xclbin_path)
        return self.runtime

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Unload runtime resources."""
        if self.runtime:
            self.runtime.unload()


# High-level execution helper
def execute_kernel(
    runtime: NpuRuntime,
    kernel_name: str,
    arguments: List[Any],
    timeout_ms: int = 0,
    profile: bool = False,
) -> ExecutionResult:
    """
    Execute kernel with simplified interface.

    Convenience wrapper around runtime.execute().

    Args:
        runtime: NPU runtime instance
        kernel_name: Name of kernel to execute
        arguments: List of arguments (Buffers, ints, or floats)
        timeout_ms: Timeout in milliseconds
        profile: Enable profiling

    Returns:
        ExecutionResult: Execution status and outputs

    Example:
        >>> runtime = NpuRuntime.create()
        >>> runtime.load_xclbin("/path/to/kernel.xclbin")
        >>> result = execute_kernel(
        ...     runtime,
        ...     "gemm_kernel",
        ...     [buffer_a, buffer_b, buffer_c, 64]
        ... )
    """
    options = ExecutionOptions()
    options.timeout_ms = timeout_ms
    options.profile = profile
    options.synchronous = True

    return runtime.execute(kernel_name, arguments, options)


# Quick start helper
def quick_start(xclbin_path: str, device_id: int = 0) -> NpuRuntime:
    """
    Quick start helper for common use case.

    Creates runtime and loads xclbin in one call.

    Args:
        xclbin_path: Path to .xclbin file
        device_id: Device ID (default: 0)

    Returns:
        NpuRuntime: Ready-to-use runtime instance

    Example:
        >>> runtime = quick_start("/path/to/kernel.xclbin")
        >>> kernel = runtime.get_kernel("my_kernel")
    """
    runtime = NpuRuntime.create(device_id)
    runtime.load_xclbin(xclbin_path)
    return runtime
