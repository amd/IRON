# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Common utilities and base classes for IRON operators."""

from .artifacts import Artifacts, Design, Step
from .build import DesignGenerator
from .declare import (
    DeclarationError,
    DispatchTime,
    In,
    Incompatible,
    InOut,
    Operator,
    Out,
    Overlay,
    Resident,
    Scratchpad,
    Shim,
    StreamIn,
    StreamOut,
    Untunable,
    Xclbin,
    dim,
    operator,
    optional,
    select,
    tunable,
)
from .elementwise import (
    BinaryElementwiseOperator,
    BinaryElementwiseOverlay,
    ChanneledUnaryOperator,
    ChanneledUnaryOverlay,
    ElementwiseOperator,
    ElementwiseOverlay,
)

__all__ = [
    "Artifacts",
    "BinaryElementwiseOperator",
    "BinaryElementwiseOverlay",
    "ChanneledUnaryOperator",
    "ChanneledUnaryOverlay",
    "DeclarationError",
    "Design",
    "DesignGenerator",
    "DispatchTime",
    "ElementwiseOperator",
    "ElementwiseOverlay",
    "In",
    "InOut",
    "Incompatible",
    "Operator",
    "Out",
    "Overlay",
    "Resident",
    "Scratchpad",
    "Shim",
    "Step",
    "StreamIn",
    "StreamOut",
    "Untunable",
    "Xclbin",
    "dim",
    "operator",
    "optional",
    "select",
    "tunable",
]
