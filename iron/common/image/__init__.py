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

from .allocator import LiveRange, live_ranges, peak_live_bytes, plan as plan_buffers
from .artifacts import Artifacts, Design, Step
from .callable import (
    SequenceCallable,
    SequenceCompareCallable,
    SequenceFullELFCallable,
    SequenceReferenceCallable,
    SequenceXclbinCallable,
)
from .fused import FusedImage, XclbinChain, build_fused_mlir
from .fusion import fuse_mlir, trace_buffer_size
from .jit_compile import DispatchStream, dispatch_stream, insts_design, xclbin_design
from .packaging import ELF, XCLBIN, each_step, plan
from .sequence import OperatorSequence

__all__ = [
    "Artifacts",
    "Design",
    "DispatchStream",
    "ELF",
    "FusedImage",
    "LiveRange",
    "OperatorSequence",
    "SequenceCallable",
    "SequenceCompareCallable",
    "SequenceFullELFCallable",
    "SequenceReferenceCallable",
    "SequenceXclbinCallable",
    "Step",
    "XCLBIN",
    "XclbinChain",
    "build_fused_mlir",
    "dispatch_stream",
    "each_step",
    "fuse_mlir",
    "insts_design",
    "live_ranges",
    "peak_live_bytes",
    "plan",
    "plan_buffers",
    "trace_buffer_size",
    "xclbin_design",
]
