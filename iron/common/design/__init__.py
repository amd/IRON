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
receives it. Against a shipped image, ``array()`` builds no cores: it pins
the operands' lanes to the image's shim channels and places what the
sequence writes.
``OperatorDesign`` is that generator as mlir-aie's ``CompilableDesign``
compiles it, keyed on what the module is built from. For a fused image,
``BuiltArray`` is one design's array and ``configuration`` puts arrays and
their sequences into one aie.iron ``DeviceConfiguration``, which
``Program.compose`` composes.
"""

from .bd import BdLimits
from .design import BuiltArray, OperatorDesign, configuration, identities
from .runtime import OperatorRuntime

__all__ = [
    "BdLimits",
    "BuiltArray",
    "OperatorDesign",
    "OperatorRuntime",
    "configuration",
    "identities",
]
