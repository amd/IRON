# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator is written with.

IRON's operator (``declare``), on mlir-aie's declaration: a class body
declares with ``aie.utils.compile.jit``'s ``param``, ``tunable`` and
``per_call`` and aie.iron's ``In``/``Out``/``InOut``. The elementwise templates
(``elementwise``), which own the array and the sequence of an operator
that names only its kernel.
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
