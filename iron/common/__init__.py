# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Common utilities and base classes for IRON operators."""

from .base import (
    AIEOperatorBase,
    MLIROperator,
    CompositeOperator,
    AIERuntimeArgSpec,
    same_shape_unary,
    same_shape_binary,
)
from .operator_bases import ChanneledUnaryOperator, BinaryElementwiseOperator
from .declare import (
    Overlay,
    Operator,
    operator,
    dim,
    tunable,
    optional,
    In,
    Out,
    InOut,
    StreamIn,
    StreamOut,
    Scratchpad,
    DispatchTime,
    Resident,
    Shim,
    Untunable,
    Incompatible,
    DeclarationError,
)
from .context import AIEContext
from .compilation import (
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    RemoteFileArtifact,
    DesignGenerator,
)
from .layout import Stride, TiledStride, TiledStridedLayout, tiled_2d
