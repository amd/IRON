# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils
from aie.iron.device import NPU2


def get_kernel_dir(dev=None) -> str:
    """Returns 'aie2p' for NPU2 (Strix, Krackan), 'aie2' for NPU1 (Phoenix)."""
    if dev is None:
        dev = aie_utils.get_current_device()
    return "aie2p" if isinstance(dev, NPU2) else "aie2"
