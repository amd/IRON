# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import aie.utils.config

import aie.utils as aie_utils
from aie.utils.compile.utils import resolve_target_arch


def get_kernel_dir(dev=None) -> str:
    """Returns 'aie2p' for NPU2 (Strix, Krackan), 'aie2' for NPU1 (Phoenix)."""
    if dev is None:
        dev = aie_utils.get_current_device()
    return resolve_target_arch(dev)


def lut_sources(dev=None):
    """``lut_based_ops.cpp`` when this arch's kernels need it, else nothing.

    aie2's exp/log kernels reference its tables; aie2p's do not. Returned as a
    bundle for declare_kernel rather than as an object to archive: the tables
    have no MLIR call site, so an object carrying them can never be discovered
    by tracing calls, and compiling them into the kernel's own translation unit
    is what removes the problem rather than working around it.
    """
    kernel_dir = get_kernel_dir(dev) if dev is not None else get_kernel_dir()
    if kernel_dir != "aie2":
        return ()
    return (
        Path(aie.utils.config.root_path())
        / "aie_runtime_lib"
        / kernel_dir.upper()
        / "lut_based_ops.cpp",
    )
