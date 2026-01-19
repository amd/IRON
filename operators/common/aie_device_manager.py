# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Global AIE Device Manager for resource sharing and cleanup
"""

import logging
import os
import sys
from pathlib import Path
from typing import Dict, Optional, Any
import pyxrt
from aie.utils import DefaultNPURuntime
from aie.utils.npukernel import NPUKernel
from aie.iron.device import NPU1, NPU2


class AIEDeviceManager:
    """Singleton manager for AIE XRT resources"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.runtime = DefaultNPURuntime
        # Expose device for AIEContext buffer allocation
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

    def cleanup(self):
        """Clean up all XRT resources"""
        # HostRuntime handles cleanup
        pass

    def reset(self):
        """Reset the device manager (for debugging)"""
        pass
