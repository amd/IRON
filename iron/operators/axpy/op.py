# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from iron.common import (
    BinaryElementwiseOperator,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class AXPY(BinaryElementwiseOperator):
    """AIE-accelerated aX + Y operator"""

    scalar_factor: float = 3.0

    kernel_name: ClassVar[str] = "axpy"
    kernel_fn_name: ClassVar[str] = "saxpy"
    kernel_subdir: ClassVar[str] = "generic"
    callback_fn: ClassVar[str] = "my_axpy"

    def _mlir_callback_args(self):
        return super()._mlir_callback_args() + [self.scalar_factor]

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                self.callback_fn,
                tuple(self._mlir_callback_args()),
            ),
        )
