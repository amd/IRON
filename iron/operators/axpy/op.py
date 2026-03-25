# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEAXPY(MLIROperator):
    """AIE-accelerated aX + Y operator"""

    def __init__(
        self,
        size,
        num_aie_columns,
        num_channels,
        tile_size,
        scalar_factor=0.01,
        context=None,
    ):
        max_multiple = num_aie_columns * tile_size
        if size % max_multiple != 0:
            raise ValueError(
                f"size ({size}) must be a multiple of num_aie_columns * tile_size ({max_multiple})"
            )

        self.size = size
        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels
        self.scalar_factor = scalar_factor

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        scalar_str = (
            f"{self.scalar_factor:.8f}".rstrip("0")
            .rstrip(".")
            .replace(".", "_")
            .replace("-", "neg")
        )
        return f"axpy_{self.num_aie_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t_{scalar_str}s"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=self.operator_dir / "design.py",
            callback_fn="my_axpy",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.num_channels,
                self.tile_size,
                0,
                self.scalar_factor,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                "axpy.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "generic" / "axpy.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),  # x
            AIERuntimeArgSpec("in", (self.size,)),  # y
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
