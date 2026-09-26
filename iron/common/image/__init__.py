# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a design becomes once it is built, and how it is called.

A design (:mod:`iron.common.design`) is MLIR; an image is the xclbin or ELF
that MLIR compiles to, together with everything needed to dispatch it. The
modules read in build order: :mod:`.packaging` decides which kind of image a
plan wants, :mod:`.fusion` merges several designs into one module,
:mod:`.jit_compile` puts a module through mlir-aie's JIT, :mod:`.allocator`
places the buffers it needs, and :mod:`.artifacts` records what came out.
:mod:`.sequence` drives all of that for one run, and :mod:`.callable` is what
a caller finally invokes.
"""

from .allocator import ArenaPlan
from .fused import build_fused_mlir
from .packaging import ELF, XCLBIN, each_step
from .sequence import OperatorSequence

__all__ = [
    "ArenaPlan",
    "ELF",
    "OperatorSequence",
    "XCLBIN",
    "build_fused_mlir",
    "each_step",
]
