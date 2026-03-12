# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Common utilities and base classes for IRON operators.

Exported groups:
  - Operator base classes: AIEOperatorBase, MLIROperator, CompositeOperator
  - Callable/argument types: CompositeCallable, AIERuntimeArgSpec
  - Context management: AIEContext
  - Compilation artifacts: XclbinArtifact, InstsBinArtifact, KernelObjectArtifact,
                            KernelArchiveArtifact, SourceArtifact, PythonGeneratedMLIRArtifact
  - Device management: AIEDeviceManager
"""

from .base import (
    AIEOperatorBase,
    MLIROperator,
    CompositeOperator,
    CompositeCallable,
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

__all__ = [
    "AIEOperatorBase",
    "MLIROperator",
    "CompositeOperator",
    "CompositeCallable",
    "AIERuntimeArgSpec",
    "AIEContext",
    "XclbinArtifact",
    "InstsBinArtifact",
    "KernelObjectArtifact",
    "KernelArchiveArtifact",
    "SourceArtifact",
    "PythonGeneratedMLIRArtifact",
    "AIEDeviceManager",
]
