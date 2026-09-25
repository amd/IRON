# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils
from aie.utils.compile.utils import resolve_target_arch


def get_kernel_dir(dev=None) -> str:
    """Returns 'aie2p' for NPU2 (Strix, Krackan), 'aie2' for NPU1 (Phoenix)."""
    if dev is None:
        dev = aie_utils.get_current_device()
    return resolve_target_arch(dev)


def pin_current_device() -> None:
    """Bind the probed NPU as the explicitly selected device.

    The mlir-aie kernel factories choose their sources by architecture from the
    explicitly selected device only; with none selected they fall back to aie2,
    which on an NPU2 machine silently builds aie2 kernels.
    """
    if aie_utils.get_current_device(probe_runtime=False) is None:
        aie_utils.set_current_device(aie_utils.get_current_device())
