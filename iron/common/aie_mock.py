# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Mock module for AIE hardware abstraction layer.

This module provides stub implementations of AIE dependencies to enable
unit testing on systems without AMD NPU hardware.

Usage:
    For testing purposes, import this module to mock the 'aie' package:

    >>> import sys
    >>> from iron.common import aie_mock
    >>> sys.modules['aie'] = aie_mock
    >>> sys.modules['aie.utils'] = aie_mock
    >>> sys.modules['aie.utils.config'] = aie_mock

Note:
    This mock is for testing only. Production use requires actual
    AMD AIE hardware and the official aie package.
"""

import logging
from typing import Any, Optional
from unittest.mock import MagicMock


logger = logging.getLogger(__name__)


# Mock AIE utilities config module
class AIEConfig:
    """Mock AIE configuration."""

    DEBUG = False
    ENABLE_PROFILING = False
    DEVICE_INDEX = 0

    @staticmethod
    def get_device_count() -> int:
        """Return mock device count (0 - no hardware)."""
        return 0

    @staticmethod
    def get_device_info(index: int = 0) -> dict:
        """Return mock device info."""
        return {
            "device_id": 0,
            "device_name": "Mock AIE Device",
            "hardware_available": False,
            "driver_version": "mock-1.0.0",
        }


# Create mock module structure
class AIEUtils:
    """Mock AIE utilities module."""

    config = AIEConfig()


# Mock XRT (Xilinx Runtime) dependencies
class MockXRTBuffer:
    """Mock XRT buffer object."""

    def __init__(self, size: int = 0):
        self.size = size
        self.data = bytearray(size)

    def sync(self, direction: str = "to_device") -> None:
        """Mock sync operation."""
        pass

    def write(self, data: bytes, offset: int = 0) -> None:
        """Mock write operation."""
        pass

    def read(self, size: int = 0, offset: int = 0) -> bytes:
        """Mock read operation."""
        return bytes(self.data[offset : offset + size])


class MockXRTKernel:
    """Mock XRT kernel object."""

    def __init__(self, name: str = "mock_kernel"):
        self.name = name

    def __call__(self, *args, **kwargs):
        """Mock kernel call."""
        logger.debug(f"Mock kernel '{self.name}' called with args={args}")
        return None


class MockXRTDevice:
    """Mock XRT device object."""

    def __init__(self, index: int = 0):
        self.index = index
        self.name = f"Mock Device {index}"

    def get_xclbin_uuid(self) -> str:
        """Return mock XCLBIN UUID."""
        return "00000000-0000-0000-0000-000000000000"

    def alloc_bo(self, size: int, flags: int = 0) -> MockXRTBuffer:
        """Allocate mock buffer object."""
        return MockXRTBuffer(size)


class MockXRTContext:
    """Mock XRT context."""

    def __init__(self, device: Optional[MockXRTDevice] = None):
        self.device = device or MockXRTDevice()

    def open_kernel(self, name: str) -> MockXRTKernel:
        """Open mock kernel."""
        return MockXRTKernel(name)


# Mock pyxrt module
class pyxrt:
    """Mock pyxrt module for XRT runtime."""

    XCL_BO_FLAGS_NONE = 0
    XCL_BO_FLAGS_CACHEABLE = 1
    XCL_BO_FLAGS_P2P = 2

    @staticmethod
    def device(index: int = 0) -> MockXRTDevice:
        """Get mock device."""
        return MockXRTDevice(index)

    @staticmethod
    def hw_context(device: MockXRTDevice) -> MockXRTContext:
        """Get mock hardware context."""
        return MockXRTContext(device)

    @staticmethod
    def xclbuffer_sync(buffer: MockXRTBuffer, direction: str = "to_device") -> None:
        """Mock buffer sync."""
        buffer.sync(direction)


# Module exports for aie.utils.config
config = AIEConfig()

# Module exports for aie package
utils = AIEUtils()
pyxrt = pyxrt


# Mock functions for direct import
def get_device_count() -> int:
    """Get number of AIE devices (mock: 0)."""
    return 0


def get_device_info(index: int = 0) -> dict:
    """Get device info (mock data)."""
    return AIEConfig.get_device_info(index)


def initialize() -> bool:
    """Initialize AIE subsystem (mock: always succeeds)."""
    logger.info("AIE mock initialized - no hardware required")
    return True


def shutdown() -> None:
    """Shutdown AIE subsystem (mock: no-op)."""
    logger.info("AIE mock shutdown complete")


# Convenience function for test setup
def setup_mock() -> None:
    """Setup AIE mock in sys.modules for testing.

    This function registers mock modules in sys.modules to intercept
    imports of the real 'aie' package.

    Example:
        >>> from iron.common.aie_mock import setup_mock
        >>> setup_mock()
        >>> # Now imports like 'import aie' will use mocks
    """
    import sys

    # Create mock modules
    aie_mock_module = MagicMock()
    aie_mock_module.utils = AIEUtils()
    aie_mock_module.pyxrt = pyxrt
    aie_mock_module.get_device_count = get_device_count
    aie_mock_module.get_device_info = get_device_info
    aie_mock_module.initialize = initialize
    aie_mock_module.shutdown = shutdown

    aie_utils_mock = MagicMock()
    aie_utils_mock.config = AIEConfig()

    aie_utils_config_mock = MagicMock()
    aie_utils_config_mock.DEBUG = False
    aie_utils_config_mock.ENABLE_PROFILING = False
    aie_utils_config_mock.DEVICE_INDEX = 0
    aie_utils_config_mock.get_device_count = get_device_count
    aie_utils_config_mock.get_device_info = get_device_info

    # Register in sys.modules
    sys.modules["aie"] = aie_mock_module
    sys.modules["aie.utils"] = aie_utils_mock
    sys.modules["aie.utils.config"] = aie_utils_config_mock

    logger.info("AIE mock modules registered in sys.modules")


def teardown_mock() -> None:
    """Remove AIE mock from sys.modules.

    This function removes the mock modules from sys.modules,
    allowing the real 'aie' package to be imported.
    """
    import sys

    for key in list(sys.modules.keys()):
        if key.startswith("aie"):
            del sys.modules[key]

    logger.info("AIE mock modules removed from sys.modules")
