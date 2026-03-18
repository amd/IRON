#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Jordan Lee
# SPDX-License-Identifier: Apache-2.0

"""Standalone test runner for forward layer tests.

This script sets up AIE mocks before any iron imports to avoid
circular dependency issues with the aie package.
"""

import sys
import logging

# ============================================================
# STEP 1: Setup AIE mock BEFORE any iron imports
# ============================================================

print("Setting up AIE mock...")

from unittest.mock import MagicMock


# Create mock module structure
class AIEConfig:
    DEBUG = False
    ENABLE_PROFILING = False
    DEVICE_INDEX = 0

    @staticmethod
    def get_device_count() -> int:
        return 0

    @staticmethod
    def get_device_info(index: int = 0) -> dict:
        return {
            "device_id": 0,
            "device_name": "Mock AIE Device",
            "hardware_available": False,
            "driver_version": "mock-1.0.0",
        }


class AIEExtras:
    """Mock aie.extras module."""

    pass


class AIEExtrasContext:
    """Mock aie.extras.context module."""

    @staticmethod
    def mlir_mod_ctx():
        """Mock MLIR module context - returns null context."""
        from contextlib import nullcontext

        return nullcontext()


# Mock classes for aie.iron.device
class NPU1:
    """Mock NPU1 device class."""

    pass


class NPU2:
    """Mock NPU2 device class."""

    pass


class DefaultNPURuntime:
    """Mock DefaultNPURuntime."""

    pass


class NPUKernel:
    """Mock NPUKernel class."""

    def __init__(self, *args, **kwargs):
        pass


class AIEUtils:
    config = AIEConfig()
    DefaultNPURuntime = DefaultNPURuntime


class AIEUtilsNPUKernel:
    NPUKernel = NPUKernel


class AIEIronDevice:
    NPU1 = NPU1
    NPU2 = NPU2


# Create mock modules
aie_mock = MagicMock()
aie_mock.utils = AIEUtils()
aie_mock.pyxrt = MagicMock()
aie_mock.get_device_count = AIEConfig.get_device_count
aie_mock.get_device_info = AIEConfig.get_device_info
aie_mock.initialize = lambda: True
aie_mock.shutdown = lambda: None
aie_mock.iron = MagicMock()
aie_mock.iron.device = AIEIronDevice

aie_extras_mock = MagicMock()
aie_extras_mock.context = AIEExtrasContext()

aie_extras_context_mock = MagicMock()
aie_extras_context_mock.mlir_mod_ctx = AIEExtrasContext.mlir_mod_ctx

# Mock pyxrt module (imported directly in aie_device_manager)
pyxrt_mock = MagicMock()
pyxrt_mock.device = MagicMock()
pyxrt_mock.hw_context = MagicMock()
pyxrt_mock.xclbuffer_sync = MagicMock()
pyxrt_mock.XCL_BO_FLAGS_NONE = 0
pyxrt_mock.XCL_BO_FLAGS_CACHEABLE = 1
pyxrt_mock.XCL_BO_FLAGS_P2P = 2

# Register mock modules in sys.modules
sys.modules["aie"] = aie_mock
sys.modules["aie.utils"] = AIEUtils
sys.modules["aie.utils.config"] = AIEConfig
sys.modules["aie.utils.npukernel"] = AIEUtilsNPUKernel
sys.modules["aie.extras"] = aie_extras_mock
sys.modules["aie.extras.context"] = aie_extras_context_mock
sys.modules["aie.iron"] = MagicMock()
sys.modules["aie.iron.device"] = AIEIronDevice
sys.modules["pyxrt"] = pyxrt_mock

print("  AIE mock modules registered")

# ============================================================
# STEP 2: Now import iron modules
# ============================================================

print("Importing iron modules...")
logging.basicConfig(level=logging.WARNING)

from iron.generation.test_forward_layer import run_all_tests

# ============================================================
# STEP 3: Run tests
# ============================================================

print("\n" + "=" * 60)
print("Running Forward Layer Test Suite")
print("=" * 60 + "\n")

success = run_all_tests()

sys.exit(0 if success else 1)
