# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Common utilities and base classes for IRON operators."""

from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
from .base import (
    AIEOperatorBase,
    MLIROperator,
    CompositeOperator,
    CompositeCallable,
    SingleXclbinCallable,
    AIERuntimeArgSpec,
)
from .context import AIEContext
from .compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from .device_manager import AIEDeviceManager
