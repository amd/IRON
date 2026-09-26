# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator is written with.

The declaration vocabulary (:mod:`.declare`): :class:`Operator` and the
fields, operands and values a class body declares. The elementwise templates
(:mod:`.elementwise`), which own the array and the sequence of an operator
that names only its kernel. :class:`DesignGenerator` and :func:`from_spec`,
for an operator whose design is written by hand.
"""

from .declare import (
    DeclarationError,
    DispatchTime,
    Extent,
    In,
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
    from_spec,
    optional,
    param,
    select,
)
from .design import DesignGenerator
from .elementwise import BinaryElementwise, Elementwise, UnaryElementwise

__all__ = [
    "BinaryElementwise",
    "DeclarationError",
    "DesignGenerator",
    "DispatchTime",
    "Elementwise",
    "Extent",
    "In",
    "Incompatible",
    "Operator",
    "Out",
    "Profile",
    "Scratchpad",
    "Shim",
    "UnaryElementwise",
    "Unresolvable",
    "Value",
    "Xclbin",
    "auto",
    "from_spec",
    "optional",
    "param",
    "select",
]
