# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The declaration layer: operators and their members.

A host buffer's dimension is a ``param()`` field or an integer literal, so
inference stays a lookup (``Operator.infer``); a tile's may also be a
tunable, since inference never reads one.
"""

from .domain import Choices, Divisors, Width
from .field import (
    Unresolvable,
    auto,
    OptionalDim,
    param,
    Select,
)
from .operand import In, InOut, Operand, Out
from .operator import CopyRun, Link, Operator
from .placement import Level, Pins, Placement
from .profile import Profile
from .value import Carried, DispatchTime, Extent, Scratchpad, Value
from .xclbin import Xclbin

__all__ = [
    "Carried",
    "Choices",
    "CopyRun",
    "Divisors",
    "DispatchTime",
    "Extent",
    "In",
    "InOut",
    "Level",
    "Link",
    "Operand",
    "Operator",
    "Out",
    "Pins",
    "Placement",
    "Profile",
    "Scratchpad",
    "Unresolvable",
    "Value",
    "Width",
    "Xclbin",
    "auto",
    "OptionalDim",
    "param",
    "Select",
]
