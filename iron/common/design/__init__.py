# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The library-owned build of a declared operator: Runtime, Program, and the sequence.

A declared :class:`~iron.common.declare.Operator` never constructs a
``Runtime`` or a ``Program``. :func:`build_design` does, from the
declaration: it tunes the overlay for the device, calls the overlay's
``design(target)`` to build the array and bind its streams, opens the runtime
sequence from the operator's buffers in declaration order, runs the
preamble (residents, barriers, parameter sync), then either derives the
fill/drain sequence from the buffer-to-stream bindings or hands a
:class:`Sequence` to the operator's ``design(rt)`` override.

``build_design`` is also the one design function every declared operator
compiles through, so the compile and fusion paths (``xclbin_design``,
``fuse_mlir``) see nothing new: they call it with the operator bound by name.

One module per participant: :mod:`.target` is what an overlay's ``design()``
receives, :mod:`.runtime` what an operator's ``design(rt)`` receives,
:mod:`.generator` the callable a compile runs, and :mod:`.build` the
function that puts the three together.
"""

from .build import (
    build_design,
    device_symbol,
    dispatch_parameters,
    generator_for,
)
from .generator import DesignGenerator
from .runtime import Sequence, Transfers
from .target import Target

__all__ = [
    "DesignGenerator",
    "Sequence",
    "Target",
    "Transfers",
    "build_design",
    "device_symbol",
    "dispatch_parameters",
    "generator_for",
]
