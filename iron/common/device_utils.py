# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import aie.utils as aie_utils
from aie.utils.compile.utils import resolve_target_arch


def get_kernel_dir(dev=None) -> str:
    """Returns 'aie2p' for NPU2 (Strix, Krackan), 'aie2' for NPU1 (Phoenix)."""
    if dev is None:
        dev = aie_utils.get_current_device()
    return resolve_target_arch(dev)
