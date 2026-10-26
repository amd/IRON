# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The library-owned build of a declared operator.

``OperatorDesign.module`` builds aie.iron's ``Program`` from the operator's
``build()`` and an ``OperatorRuntime``. For a full ELF, ``configuration`` puts
each ``BuiltArray`` and its sequences into one ``DeviceConfiguration``.
"""

from .design import BuiltArray, OperatorDesign, configuration, identities
from .runtime import OperatorRuntime

__all__ = [
    "BuiltArray",
    "OperatorDesign",
    "OperatorRuntime",
    "configuration",
    "identities",
]
