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


class AIESiLU(MLIROperator):
    """AIE-accelerated SiLU activation function"""

    def __init__(self, size, tile_size, num_aie_columns=8, context=None):
        if size % (num_aie_columns * tile_size) != 0:
            raise ValueError(
                f"size ({size}) must be a multiple of num_aie_columns * tile_size ({num_aie_columns * tile_size})"
            )
        self.size = size
        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns
        # Enforce ShimDMA limits for SiLU (uses 1 input per core)
        # Maximum safe configuration: 8 columns × 1 channel = 8 ShimDMA channels
        if self.num_aie_columns > 8:
            raise ValueError(
                f"num_aie_columns ({self.num_aie_columns}) exceeds ShimDMA limit: a unary operator uses 2 DMA channels per column, max 8 columns (16 channels total)"
            )
        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"silu_{self.num_aie_columns}col_{self.size}_{self.tile_size}t"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_silu",
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
                "silu.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "aie2p" / "silu.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),  # input
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
