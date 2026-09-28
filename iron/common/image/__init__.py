# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a design becomes once it is built, and how it is called.

A design (:mod:`iron.common.design`) is MLIR; an image is the xclbin or ELF
that MLIR compiles to, together with everything needed to dispatch it. The
modules read in build order: :mod:`.packaging` decides which kind of image a
plan wants, :mod:`.allocator` places the buffers it needs, :mod:`.fusion`
merges several designs into one module (:mod:`.coresidence` packs several
into one device configuration), :mod:`.fused` puts that module (or
each design, chained into xclbins) through mlir-aie's ``CompilableDesign``,
and :mod:`.artifacts` records what came out.
:mod:`.sequence` drives all of that for one run, and :mod:`.callable` is what
a caller finally invokes. :mod:`.standalone` is the one-operator case: an
operator built and called on its own, outside a graph.
"""

from .allocator import ArenaPlan
from .coresidence import AdjacentPacking, Packing
from .fusion import Fusion
from .packaging import ELF, XCLBIN, each_step
from .sequence import OperatorSequence
from .standalone import OperatorImage

__all__ = [
    "AdjacentPacking",
    "ArenaPlan",
    "ELF",
    "Fusion",
    "OperatorImage",
    "OperatorSequence",
    "Packing",
    "XCLBIN",
    "each_step",
]
