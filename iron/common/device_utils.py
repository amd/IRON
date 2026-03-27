# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Device utility functions for handling NPU device types and configurations."""

from aie.iron.device import NPU1, NPU1Col1, NPU1Col2, NPU2


def get_device_name(dev):
    """Get device name string for looking up microkernel dimensions.

    Returns "npu1" for Phoenix/NPU1 devices, "npu2" for Strix/NPU2 devices.

    Args:
        dev: Either a string ("npu", "npu1", "npu2"), a device object with .resolve(),
             or a device type object.

    Returns:
        str: "npu1" or "npu2"
    """
    if isinstance(dev, str):
        if dev in ("npu", "npu1"):
            return "npu1"
        else:
            return "npu2"
    elif hasattr(dev, "resolve"):
        # Device object from device_manager.device_type
        return dev.resolve().name
    else:
        # Assume it's a device type object - check class name
        name = type(dev).__name__
        if "NPU1" in name:
            return "npu1"
        else:
            return "npu2"


def get_device_type(dev, n_aie_cols):
    """Resolve device type to appropriate NPU device instance.

    Handles both string inputs ("npu", "npu1", "npu2") and device objects.

    Args:
        dev: Either a string ("npu", "npu1", "npu2"), a device object with .resolve(),
             or a device type object.
        n_aie_cols: Number of AIE columns to use (1, 2, or 4).

    Returns:
        NPU device instance (NPU1, NPU1Col1, NPU1Col2, or NPU2)
    """
    dev_name = get_device_name(dev)
    if dev_name == "npu1":
        if n_aie_cols == 1:
            return NPU1Col1()
        elif n_aie_cols == 2:
            return NPU1Col2()
        else:
            return NPU1()
    else:
        return NPU2()
