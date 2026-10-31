# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator is written with: IRON's ``Operator`` (``declare``).

Whose class body declares with ``aie.utils.compile.jit``'s ``param``,
``tunable`` and ``per_call`` and aie.iron's ``In``/``Out``/``InOut``; and
the elementwise templates (``elementwise``), owning the array and sequence
of an operator naming its kernel.
"""

from .declare import (
    Block,
    Built,
    Operand,
    Operator,
    Precision,
    Rtp,
    Unresolvable,
    Value,
    Xclbin,
)
from .elementwise import (
    BinaryElementwise,
    Elementwise,
    KernelCall,
    RowBroadcast,
    Rowwise,
    UnaryElementwise,
    WeightedRowwise,
)

__all__ = [
    "BinaryElementwise",
    "Block",
    "Built",
    "Elementwise",
    "KernelCall",
    "Operand",
    "Operator",
    "Precision",
    "RowBroadcast",
    "Rowwise",
    "Rtp",
    "UnaryElementwise",
    "Unresolvable",
    "Value",
    "WeightedRowwise",
    "Xclbin",
]
