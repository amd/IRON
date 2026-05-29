# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Global AIE Device Manager for resource sharing and cleanup

Note: This module requires the AMD XRT toolchain (Linux only).
On Windows or systems without XRT, import will fail gracefully
and tests using AIE hardware will be skipped.
"""

import logging
import os
import sys
from pathlib import Path
from typing import Dict, Optional, Any

# Lazy imports - only available on Linux with XRT toolchain
pyxrt = None
DefaultNPURuntime = None
NPUKernel = None
NPU1 = None
NPU2 = None

try:
    import pyxrt
    from aie.utils import DefaultNPURuntime
    from aie.utils.npukernel import NPUKernel
    from aie.iron.device import NPU1, NPU2

    AIE_TOOLCHAIN_AVAILABLE = True
except ImportError:
    AIE_TOOLCHAIN_AVAILABLE = False


class AIEDeviceManager:
    """Singleton manager for AIE XRT resources"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not AIE_TOOLCHAIN_AVAILABLE:
            raise ImportError(
                "AIE toolchain not available. This module requires:\n"
                "  - Linux OS\n"
                "  - AMD XRT drivers\n"
                "  - pyxrt Python bindings\n"
                "  - aie.iron MLIR toolchain\n"
                "Tests using AIE hardware will be skipped on this platform."
            )
        # DefaultNPURuntime in current aie wheels is already the live singleton instance
        # (a CachedXRTRuntime), not a constructor. Do not call it.
        self.runtime = DefaultNPURuntime
        # Accessing protected member _device as AIEContext needs pyxrt.device
        self.device = self.runtime._device
        self.device_type = self.runtime.device()

    def get_kernel_handle(self, xclbin_path: str, kernel_name: str, insts_path: str):
        """Get kernel handle using HostRuntime"""
        npu_kernel = NPUKernel(
            xclbin_path=xclbin_path, insts_path=insts_path, kernel_name=kernel_name
        )
        return self.runtime.load(npu_kernel)

    def device_str(self) -> str:
        return self.device_type.resolve().name

    @property
    def aie_device(self):
        """Return the aie.iron.device object (NPU1/NPU2) suitable for Program(dev, rt)."""
        return self.device_type

    def cleanup(self):
        """Clean up all XRT resources"""
        # HostRuntime handles cleanup
        pass

    def reset(self):
        """Reset the device manager (for debugging)"""
        pass
