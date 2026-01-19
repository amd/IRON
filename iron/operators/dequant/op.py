# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.operators.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEDequant(AIEOperatorBase):

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

        # Calculate buffer sizes
        # Input: int4 packed data + scale factors
        # For N int4 values, we need N/2 bytes + N/group_size scale factors (bfloat16, 2 bytes each)
        self.input_size = (size // 2) + (size // group_size) * 2
        self.output_size = size

        total_cores = self.num_columns * self.num_channels
        assert self.size % total_cores == 0, "Size must be divisible by total cores"
        assert total_cores <= 16, "Total cores (columns * channels) must be <= 16"

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = f"dequant_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_dequant_kernel",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_columns,
                self.num_channels,
                0,
                self.tile_size,
                self.group_size,
            ],
        )

        # Build the kernel object file with the appropriate tile size and group size
        kernel_artifact = KernelObjectArtifact.new(
            f"expand_aie2_{self.tile_size}.o",
            depends=[
                SourceArtifact.new(
                    self.context.base_dir / "aie_kernels" / "generic" / "expand.cc"
                )
            ],
            extra_flags=[
                f"-DTILE_SIZE={self.tile_size}",
                f"-DGROUP_SIZE={self.group_size}",
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[mlir_artifact, kernel_artifact],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        # Input buffer uses uint8 dtype, output uses bfloat16
        self.add_buffer("input", self.input_size, dtype=np.uint8)
        self.add_buffer("output", self.output_size, dtype=bfloat16)
        self.add_kernel(
            "dequant",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("dequant", "input", "output")

    def forward(self, x_packed):
        """
        Forward pass for dequantization.

        Args:
            x_packed: Packed uint8 numpy array containing int4 data + scale factors

        Returns:
            Dequantized bfloat16 torch tensor
        """
        if x_packed.size != self.input_size:
            raise AIEOperatorConstraintError(
                f"AIEDequant: input size {x_packed.size} does not match expected size {self.input_size}"
            )

        # Write input and execute
        self.write_buffer("input", x_packed.flatten())
        self.write_buffer("output", np.zeros(self.output_size, dtype=bfloat16))
        self.run_runlist()
        result = self.read_buffer_as_torch(
            "output", shape=(self.output_size,), dtype=bfloat16
        )

        return result
