# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The library-owned build of a declared operator: its Program and runtime.

A declared ``Operator`` never constructs a ``Runtime`` or a ``Program``.
``OperatorDesign.module`` does, from the declaration: it resolves the
operator for the device, calls its ``array()`` to build the array and bind
its operands' lanes, and builds aie.iron's ``Program`` around an
``OperatorRuntime``, the ``Runtime`` whose body runs the preamble (values,
parameter sync, barriers) and then either the fill/drain sequence derived
from the operands' tiles or the operator's ``sequence(rt)`` override, which
receives it. Against a shipped image the runtime is a ``ShippedRuntime``.
``OperatorDesign`` is that generator as mlir-aie's ``CompilableDesign``
compiles it, keyed on what the module is built from.
"""

from .bd import BdLimits
from .design import OperatorDesign
from .runtime import OperatorRuntime, ShimChannel
from .shipped import ShippedRuntime

__all__ = [
    "BdLimits",
    "OperatorDesign",
    "OperatorRuntime",
    "ShimChannel",
    "ShippedRuntime",
]
