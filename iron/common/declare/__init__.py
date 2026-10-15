# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The declaration layer: operators and their members.

A host buffer's dimension is a ``Param()`` field or an integer literal, so
inference stays a lookup (``Operator.infer``); a tile's may also be a
tunable, since inference never reads one.
"""

from .domain import Divisors, Width
from .field import Auto, AutoSpec, Param, ParamSpec, Unresolvable
from .shape import Select
from .operand import In, InOut, Operand, Out
from .chain import Chain, Link
from .operator import Operator
from .profile import Profile
from .value import DispatchTime, Extent, Value
from .xclbin import Xclbin

__all__ = [
    "Chain",
    "Divisors",
    "DispatchTime",
    "Extent",
    "In",
    "InOut",
    "Link",
    "Operand",
    "Operator",
    "Out",
    "Profile",
    "Unresolvable",
    "Value",
    "Width",
    "Xclbin",
    "Auto",
    "AutoSpec",
    "Param",
    "ParamSpec",
    "Select",
]
