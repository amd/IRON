# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    PythonGeneratedMLIRArtifact,
)


class AIERepeat(MLIROperator):
    """AIE-accelerated repeat-interleave operator"""

    def __init__(
        self,
        rows,
        cols,
        repeat,
        transfer_size=None,
        dtype=bfloat16,
        context=None,
    ):
        self.rows = rows
        self.cols = cols
        self.repeat = repeat
        self.transfer_size = transfer_size
        self.dtype = dtype
        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        name = f"repeat_{self.rows}x{self.cols}_by_{self.repeat}"
        if self.transfer_size is not None:
            name += f"_{self.transfer_size}ts"
        return name

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="repeat",
            callback_args=[
                self.context.device_manager.device_type,
                self.dtype,
                self.rows,
                self.cols,
                self.repeat,
                self.transfer_size,
            ],
        )

    def get_kernel_artifacts(self):
        return []

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.rows, self.cols)),
            AIERuntimeArgSpec("out", (self.rows * self.repeat, self.cols)),
        ]
