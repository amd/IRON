# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator is written with.

The declaration vocabulary (``declare``): ``Operator`` and the
fields, operands and values a class body declares. The elementwise templates
(``elementwise``), which own the array and the sequence of an operator
that names only its kernel.
"""

from .declare import (
    Carried,
    DeclarationError,
    DispatchTime,
    Extent,
    In,
    Incompatible,
    InOut,
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
    "Carried",
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
