# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar, Dict

import aie.utils as aie_utils
from iron.common import (
    ChanneledUnaryOperator,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class LeakyReLU(ChanneledUnaryOperator):
    """AIE-accelerated Leaky ReLU operator"""

    alpha: float = 0.01

    kernel_name: ClassVar[str] = "leaky_relu"
    kernel_fn_name: ClassVar[str] = "leaky_relu_bf16"
    callback_fn: ClassVar[str] = "my_leaky_relu"
    _name_aliases: ClassVar[Dict[str, str]] = {
        **ChanneledUnaryOperator._name_aliases,
        "alpha": "a",
    }

    def _mlir_callback_args(self):
        return super()._mlir_callback_args() + [self.alpha]

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                self.callback_fn,
                tuple(self._mlir_callback_args()),
            ),
        )
