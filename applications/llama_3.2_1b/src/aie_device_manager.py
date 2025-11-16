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
from aie.iron.hostruntime.config import detect_npu_device
from aie.iron.device import NPU1, NPU2


class AIEDeviceManager:
    """Singleton manager for AIE XRT resources"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.device = pyxrt.device(0)
        self.device_type = detect_npu_device()
        self.contexts = {}  # xclbin_path -> (context, xclbin)
        self.kernels = {}  # (xclbin_path, kernel_name) -> kernel

    def get_context_and_kernel(
        self, xclbin_path: str, kernel_name: str | None = None
    ) -> (pyxrt.hw_context, pyxrt.kernel):
        """Get or create hardware context and kernel for xclbin"""
        # Check if we already have a context for this xclbin

        if xclbin_path not in self.contexts:
            xclbin = pyxrt.xclbin(xclbin_path)
            self.device.register_xclbin(xclbin)
            xclbin_uuid = xclbin.get_uuid()
            context = pyxrt.hw_context(self.device, xclbin_uuid)
            self.contexts[xclbin_path] = (context, xclbin)
            logging.debug(f"Created new context for {Path(xclbin_path).name}")
        else:
            context, xclbin = self.contexts[xclbin_path]
            logging.debug(f"Reusing context for {Path(xclbin_path).name}")

        # Get kernel name if not provided
        if kernel_name is None:
            kernels = xclbin.get_kernels()
            if not kernels:
                raise RuntimeError("No kernels found in xclbin")
            kernel_name = kernels[0].get_name()

        # Check if we already have the kernel
        kernel_key = (xclbin_path, kernel_name)
        if kernel_key not in self.kernels:
            self.kernels[kernel_key] = pyxrt.kernel(context, kernel_name)
            logging.debug(
                f"Created new kernel {kernel_name} from xclbin {Path(xclbin_path).name}"
            )
        else:
            logging.debug(
                f"Reusing kernel: {kernel_name} from xclbin {Path(xclbin_path).name}"
            )

        return context, self.kernels[kernel_key]

    def device_str(self) -> str:
        return self.device_type.resolve().name

    def cleanup(self):
        """Clean up all XRT resources"""
        self.kernels.clear()

        # Clear contexts
        for xclbin_path, (context, xclbin) in self.contexts.items():
            try:
                del context
            except:
                pass
        self.contexts.clear()

        # Clear device
        if self.device is not None:
            try:
                del self.device
            except:
                pass
            self.device = None

        logging.debug("Cleaned up AIE device manager")

    def reset(self):
        """Reset the device manager (for debugging)"""
        self.cleanup()
        AIEDeviceManager._instance = None
