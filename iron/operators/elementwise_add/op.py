# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEElementwiseAdd(MLIROperator):
    """AIE-accelerated element-wise addition"""

    def __init__(
        self,
        size,
        tile_size,
        num_aie_columns=8,
        context=None,
    ):
        assert (
            size % (num_aie_columns * tile_size) == 0
        ), "size must be multiple of num_aie_columns * tile_size"
        self.size = size
        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns
        # Enforce ShimDMA limits for elementwise_add (uses 2 inputs per core)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        total_shimdma_channels = self.num_aie_columns * 2
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"
        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"add_{self.num_aie_columns}col_{self.size}_{self.tile_size}t"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=self.operator_dir / "design.py",
            callback_fn="my_eltwise_add",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.tile_size,
                0,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                "add.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "generic" / "add.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),  # input1
            AIERuntimeArgSpec("in", (self.size,)),  # input2
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
