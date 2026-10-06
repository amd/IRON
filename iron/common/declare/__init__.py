# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The declaration layer: operators and their members.

A host buffer's dimension is a ``param()`` field or an integer literal, so
inference stays a lookup (``Operator.infer``); a tile's may also be a
tunable, since inference never reads one.
"""

from .field import (
    Unresolvable,
    auto,
    OptionalDim,
    param,
    Select,
)
from .member import (
    Carried,
    Direction,
    DispatchTime,
    Extent,
    In,
    InOut,
    Out,
    Scratchpad,
    Shim,
    Value,
)
from .operator import Operator
from .profile import Profile
from .xclbin import Xclbin

__all__ = [
    "Carried",
    "Direction",
    "DispatchTime",
    "Extent",
    "In",
    "InOut",
    "Operator",
    "Out",
    "Profile",
    "Scratchpad",
    "Shim",
    "Unresolvable",
    "Value",
    "Xclbin",
    "auto",
    "OptionalDim",
    "param",
    "Select",
]
