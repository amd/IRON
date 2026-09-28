# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator is written with.

The declaration vocabulary (:mod:`.declare`): :class:`Operator` and the
fields, operands and values a class body declares. The elementwise templates
(:mod:`.elementwise`), which own the array and the sequence of an operator
that names only its kernel.
"""

from .declare import (
    DeclarationError,
    DispatchTime,
    Extent,
    In,
    InOut,
    Incompatible,
    Operator,
    Out,
    Profile,
    Scratchpad,
    Shim,
    Unresolvable,
    Value,
    Xclbin,
    auto,
    optional,
    param,
    select,
)
from .elementwise import BinaryElementwise, Elementwise, Rowwise, UnaryElementwise

__all__ = [
    "BinaryElementwise",
    "DeclarationError",
    "DispatchTime",
    "Elementwise",
    "Extent",
    "In",
    "InOut",
    "Incompatible",
    "Operator",
    "Out",
    "Profile",
    "Rowwise",
    "Scratchpad",
    "Shim",
    "UnaryElementwise",
    "Unresolvable",
    "Value",
    "Xclbin",
    "auto",
    "optional",
    "param",
    "select",
]
