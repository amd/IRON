# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator is written with.

The declaration vocabulary (``declare``): ``Operator`` and the
fields, operands and values a class body declares. The elementwise templates
(``elementwise``), which own the array and the sequence of an operator
that names only its kernel.
"""

from .declare import (
    Built,
    Divisors,
    DispatchTime,
    Extent,
    In,
    InOut,
    Operand,
    Operator,
    Out,
    Precision,
    Rtp,
    Unresolvable,
    Value,
    Width,
    Xclbin,
    Auto,
    Param,
    Select,
)
from .elementwise import (
    BinaryElementwise,
    Elementwise,
    KernelCall,
    RowBroadcast,
    Rowwise,
    UnaryElementwise,
)

__all__ = [
    "BinaryElementwise",
    "Built",
    "DispatchTime",
    "Divisors",
    "Elementwise",
    "Extent",
    "In",
    "InOut",
    "KernelCall",
    "Operand",
    "Operator",
    "Out",
    "Rtp",
    "RowBroadcast",
    "Rowwise",
    "Select",
    "UnaryElementwise",
    "Precision",
    "Unresolvable",
    "Value",
    "Width",
    "Xclbin",
    "Auto",
    "Param",
]
