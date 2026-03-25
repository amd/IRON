# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIERope(MLIROperator):

    def __init__(
        self,
        rows: int,
        cols: int,
        angle_rows=None,
        num_aie_columns=1,
        method_type=0,
        context=None,
    ):
        if angle_rows is None:
            angle_rows = rows

        if not (cols % (16 * 2) == 0 and cols >= (16 * 2)):
            raise ValueError("cols must be multiple of 32 and >= 32")
        if rows % num_aie_columns != 0:
            raise ValueError("rows must be divisible by num_aie_columns")
        if not (angle_rows <= rows and rows % angle_rows == 0):
            raise ValueError("angle_rows must divide rows")
        if not (angle_rows >= num_aie_columns and angle_rows % num_aie_columns == 0):
            raise ValueError("angle_rows must be divisible by num_aie_columns")

        self.rows = rows
        self.cols = cols
        self.angle_rows = angle_rows
        self.num_aie_columns = num_aie_columns
        self.method_type = method_type
        if method_type not in {0, 1}:
            raise ValueError(f"method_type must be 0 or 1, got {method_type}")

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"rope_{self.num_aie_columns}col_{self.rows}rows_{self.cols}cols_{self.angle_rows}arows_{self.method_type}m"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=self.operator_dir / "design.py",
            callback_fn="rope",
            callback_args=[
                self.context.device_manager.device_type,
                self.rows,
                self.cols,
                self.angle_rows,
                self.num_aie_columns,
                0,
                self.method_type,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"rope_{self.method_type}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "generic" / "rope.cc"
                    )
                ],
                extra_flags=[
                    "-DTWO_HALVES" if 0 == self.method_type else "-DINTERLEAVED"
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec(
                "in",
                (
                    self.rows,
                    self.cols,
                ),
            ),  # input tensor
            AIERuntimeArgSpec(
                "in",
                (
                    self.angle_rows,
                    self.cols,
                ),
            ),  # angles
            AIERuntimeArgSpec(
                "out",
                (
                    self.rows,
                    self.cols,
                ),
            ),  # output
        ]
