# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIELayerNorm(MLIROperator):
    """AIE-accelerated Layer Normalization operator"""

    def __init__(
        self, size, num_aie_columns, num_channels, tile_size, trace_size=0, context=None
    ):
        max_multiple = num_aie_columns * tile_size
        if size % max_multiple != 0:
            raise ValueError(
                f"size ({size}) must be a multiple of num_aie_columns * tile_size ({max_multiple})"
            )

        self.size = size
        self.tile_size = tile_size
        self.trace_size = trace_size
        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels

        total_shimdma_channels = self.num_aie_columns * self.num_channels
        if total_shimdma_channels > 16:
            raise ValueError(
                f"num_aie_columns * num_channels ({total_shimdma_channels}) exceeds conservative ShimDMA limit of 16"
            )

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"layer_norm_{self.num_aie_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=self.operator_dir / "design.py",
            callback_fn="my_layer_norm",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.num_channels,
                self.trace_size,
                self.tile_size,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"layer_norm.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / "aie2p"
                        / "layer_norm.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),  # input
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
