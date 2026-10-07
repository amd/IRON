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
    DispatchTime,
    Extent,
    In,
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
    OptionalDim,
    param,
    Select,
)
from .elementwise import (
    BinaryElementwise,
    Elementwise,
    Finish,
    Rowwise,
    UnaryElementwise,
)

__all__ = [
    "BinaryElementwise",
    "Carried",
    "DispatchTime",
    "Elementwise",
    "Extent",
    "Finish",
    "In",
    "InOut",
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
    "OptionalDim",
    "param",
    "Select",
]
