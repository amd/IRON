# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEDequant(MLIROperator):

    def __init__(
        self,
        size,
        num_aie_columns,
        num_channels,
        tile_size,
        group_size=32,
        context=None,
    ):
        # Store num_aie_columns in self.num_columns for internal use (following the pattern)
        self.num_columns = num_aie_columns

        self.size = size
        self.tile_size = tile_size
        self.num_channels = num_channels
        self.group_size = group_size

        # Calculate buffer sizes (in bytes)
        # Input: int4 packed data + scale factors
        # For N int4 values, we need N/2 bytes + N/group_size scale factors (bfloat16, 2 bytes each)
        self.input_size = (size // 2) + (size // group_size) * 2
        self.output_size = size

        total_cores = self.num_columns * self.num_channels
        assert self.size % total_cores == 0, "Size must be divisible by total cores"
        assert total_cores <= 16, "Total cores (columns * channels) must be <= 16"

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"dequant_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_dequant_kernel",
            callback_args=[
                self.context.device_manager.device_str(),
                self.size,
                self.num_columns,
                self.num_channels,
                0,
                self.tile_size,
                self.group_size,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"expand_aie2_{self.tile_size}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "generic" / "expand.cc"
                    )
                ],
                extra_flags=[
                    f"-DTILE_SIZE={self.tile_size}",
                    f"-DGROUP_SIZE={self.group_size}",
                ],
            )
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.input_size,), dtype=np.uint8),  # input
            AIERuntimeArgSpec("out", (self.output_size,), dtype=bfloat16),  # output
        ]
