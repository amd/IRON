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
to the operator's ``sequence(rt)`` override. :class:`OperatorDesign` is
that generator as mlir-aie's ``CompilableDesign`` compiles it, keyed on
what the module is built from.

One module per participant: :mod:`.target` is what an operator's ``array()``
receives, :mod:`.runtime` what an operator's ``sequence(rt)`` receives,
:mod:`.external` what it receives against a shipped image, and
:mod:`.build` puts them together.
"""

from .build import OperatorDesign, build_design, device_symbol
from .external import ExternalSequence
from .runtime import Sequence, Transfers
from .target import Target

__all__ = [
    "ExternalSequence",
    "OperatorDesign",
    "Sequence",
    "Target",
    "Transfers",
    "build_design",
    "device_symbol",
]
