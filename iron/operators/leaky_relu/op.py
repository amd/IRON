# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIELeakyReLU(MLIROperator):
    """AIE-accelerated LEAKY RELU operator"""

    def __init__(
        self, size, num_aie_columns, num_channels, tile_size, alpha=0.01, context=None
    ):
        max_multiple = num_aie_columns * tile_size
        assert (
            size % max_multiple == 0
        ), "size must be multiple of num_aie_columns * tile_size"
        assert size % tile_size == 0, "size must be multiple of tile_size"

        self.size = size
        self.tile_size = tile_size

        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels
        self.alpha = alpha

        total_shimdma_channels = self.num_aie_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        super().__init__(context=context)

    def get_operator_name(self):
        # Use fixed-precision formatting to avoid scientific notation (e.g. 1e-05)
        # which would produce invalid filenames with '-' characters.
        alpha_str = f"{self.alpha:.6f}".replace(".", "_")
        return f"leaky_relu_{self.num_aie_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t_a{alpha_str}"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_leaky_relu",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.num_channels,
                self.tile_size,
                0,
                self.alpha,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                "leaky_relu.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / "aie2p"
                        / "leaky_relu.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),  # input
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
