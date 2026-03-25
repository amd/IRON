# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Global AIE Device Manager for resource sharing and cleanup
"""

import logging
import os
from pathlib import Path
import pyxrt
from aie.utils.hostruntime.xrtruntime.hostruntime import XRTHostRuntime


class AIEDeviceManager:
    """Singleton manager for AIE XRT resources"""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Only initialize once
        if AIEDeviceManager._initialized:
            return
        AIEDeviceManager._initialized = True

        self.device = pyxrt.device(0)
        self.device_type = XRTHostRuntime().device()
        self.contexts: dict[str, tuple] = {}  # xclbin_path -> (context, xclbin)
        self.kernels: dict[tuple, object] = {}  # (xclbin_path, kernel_name) -> kernel
        self._default_kernel_names: dict[str, str] = {}  # xclbin_path -> kernel_name

    def get_context_and_kernel(
        self, xclbin_path: str, kernel_name: str | None = None
    ) -> tuple:
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

        # Get kernel name if not provided; cache it alongside the context so
        # we don't call get_kernels() on every lookup for the same xclbin.
        if kernel_name is None:
            if xclbin_path not in self._default_kernel_names:
                kernels = xclbin.get_kernels()
                if not kernels:
                    raise RuntimeError("No kernels found in xclbin")
                self._default_kernel_names[xclbin_path] = kernels[0].get_name()
            kernel_name = self._default_kernel_names[xclbin_path]

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
        """Return the resolved device name string (e.g. 'npu1' or 'npu2')."""
        return self.device_type.resolve().name

    def cleanup(self):
        """Clean up all XRT resources"""
        # Clear kernels before contexts: kernels hold references to contexts.
        self.kernels.clear()
        self._default_kernel_names.clear()
        self.contexts.clear()
        self.device = None

        logging.debug("Cleaned up AIE device manager")

    def reset(self):
        """Reset the device manager (for debugging)"""
        self.cleanup()
        AIEDeviceManager._instance = None
        AIEDeviceManager._initialized = False
