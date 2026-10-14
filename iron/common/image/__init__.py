# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a design becomes once it is built, and how it is called.

A design (``iron.common.design``) is MLIR; an image is the xclbin or ELF
that MLIR compiles to, together with everything needed to dispatch it. The
modules read in build order: ``packaging`` decides which kind of image a
plan wants, ``allocator`` places the buffers it needs, ``fusion``
composes several designs into one module, mlir-aie's ``Program.compose``
(``coresidence`` packs several into one device configuration), ``fused``
puts that module (or each design, chained into xclbins) through mlir-aie's
``CompilableDesign``, and ``artifacts`` records what came out.
``sequence`` drives all of that for one run, and ``callable`` is what
a caller finally invokes. ``standalone`` is the one-operator case: an
operator called on its own, outside a graph (``Operator.compile``).
"""

from .allocator import ArenaPlan
from .coresidence import AdjacentPacking, Packing
from .fusion import Fusion

__all__ = [
    "AdjacentPacking",
    "ArenaPlan",
    "Fusion",
    "Packing",
]
