# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The declaration layer: operators and their members.

A host buffer's dimension is a ``field()`` or an integer literal, so
inference stays a lookup (``Declaration.infer``); a tile's may also be a
tunable, since inference never reads one.
"""

from .domain import Divisors, Width
from .field import Auto, Unresolvable, field
from .shape import Select
from .operand import Operand
from .operator import Built, Operator
from .precision import Precision
from .profile import Profile
from .rtp import Rtp
from .value import Extent, Value
from .xclbin import Xclbin

__all__ = [
    "Built",
    "Divisors",
    "Extent",
    "Operand",
    "Operator",
    "Precision",
    "Profile",
    "Rtp",
    "Unresolvable",
    "Value",
    "Width",
    "Xclbin",
    "Auto",
    "field",
    "Select",
]
