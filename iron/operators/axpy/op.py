# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from aie.iron.kernels import datamovement

from iron.common import (
    BinaryElementwiseOperator,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class AXPY(BinaryElementwiseOperator):
    """AIE-accelerated aX + Y operator"""

    scalar_factor: float = 3.0

    callback_fn: ClassVar[str] = "my_axpy"

    def _kernel(self):
        return datamovement.axpy(self._tile_elements)

    def _mlir_callback_args(self):
        return super()._mlir_callback_args() + [self.scalar_factor, self._kernel()]

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                self.callback_fn,
                tuple(self._mlir_callback_args()),
            ),
        )
