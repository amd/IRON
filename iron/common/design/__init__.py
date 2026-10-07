# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The library-owned build of a declared operator: Runtime, Program, and the sequence.

A declared ``Operator`` never constructs a
``Runtime`` or a ``Program``. ``build_design`` does, from the
declaration: it resolves the operator for the device, calls its
``array(target)`` to build the array and bind its operands' lanes, opens
the runtime sequence from the operator's buffers in declaration order, runs
the preamble (values, barriers, parameter sync), then either derives the
fill/drain sequence from the operands' tiles or hands a ``Sequence``
to the operator's ``sequence(rt)`` override. ``OperatorDesign`` is
that generator as mlir-aie's ``CompilableDesign`` compiles it, keyed on
what the module is built from.

One module per participant: ``target`` is what an operator's ``array()``
receives, ``runtime`` what an operator's ``sequence(rt)`` receives,
``external`` what it receives against a shipped image, and
``build`` puts them together.
"""

from .bd import BdLimits
from .build import OperatorDesign, build_design, device_symbol
from .external import ExternalSequence, ShimChannel
from .runtime import Sequence
from .target import Target

__all__ = [
    "BdLimits",
    "ExternalSequence",
    "OperatorDesign",
    "Sequence",
    "ShimChannel",
    "Target",
    "build_design",
    "device_symbol",
]
