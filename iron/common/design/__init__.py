# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The library-owned build of a declared operator: Runtime, Program, and the sequence.

A declared :class:`~iron.common.declare.Operator` never constructs a
``Runtime`` or a ``Program``. :func:`build_design` does, from the
declaration: it resolves the operator for the device, calls its
``array(target)`` to build the array and bind its operands' lanes, opens
the runtime sequence from the operator's buffers in declaration order, runs
the preamble (values, barriers, parameter sync), then either derives the
fill/drain sequence from the operands' tiles or hands a :class:`Sequence`
to the operator's ``sequence(rt)`` override.

Every declared operator compiles through ``build_design``, so the compile
and fusion paths (``xclbin_design``, ``fuse_mlir``) call it with the
operator bound by name.

One module per participant: :mod:`.target` is what an operator's ``array()``
receives, :mod:`.runtime` what an operator's ``sequence(rt)`` receives,
:mod:`.generator` the callable a compile runs, and :mod:`.build` the
function that puts the three together.
"""

from .build import device_symbol, generator_for
from .generator import DesignGenerator
from .runtime import Sequence, Transfers, transfers
from .target import Target

__all__ = [
    "DesignGenerator",
    "Sequence",
    "Target",
    "Transfers",
    "device_symbol",
    "generator_for",
    "transfers",
]
