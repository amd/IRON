# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The library-owned build of a declared operator.

``OperatorDesign.module`` resolves the operator, runs its ``array()`` and
builds aie.iron's ``Program`` around an ``OperatorRuntime``: the preamble,
then the sequence derived from the operands or the operator's own
``sequence(rt)``. For a fused image, ``configuration`` puts ``BuiltArray`` s
and their sequences into one ``DeviceConfiguration`` for ``Program.compose``.
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
