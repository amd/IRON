# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The declaration layer: operators and their members.

A host buffer's dimension is a ``Param()`` field or an integer literal, so
inference stays a lookup (``Declaration.infer``); a tile's may also be a
tunable, since inference never reads one.
"""

from .domain import Divisors, Width
from .field import Auto, Param, Unresolvable
from .shape import Select
from .operand import In, InOut, Operand, Out
from .operator import Built, Operator
from .precision import Precision
from .profile import Profile
from .rtp import Rtp
from .value import DispatchTime, Extent, Value
from .xclbin import Xclbin

__all__ = [
    "Built",
    "Divisors",
    "DispatchTime",
    "Extent",
    "In",
    "InOut",
    "Operand",
    "Operator",
    "Out",
    "Precision",
    "Profile",
    "Rtp",
    "Unresolvable",
    "Value",
    "Width",
    "Xclbin",
    "Auto",
    "Param",
    "Select",
]
