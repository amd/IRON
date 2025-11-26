# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from operators.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    torch_to_numpy,
    numpy_to_torch,
)


class AIEGELU(AIEOperatorBase):
    """AIE-accelerated GELU activation function"""

    def __init__(self, size, num_aie_columns, num_channels, tile_size):
        max_multiple = num_aie_columns * tile_size
        padded_size = ((size + max_multiple - 1) // max_multiple) * max_multiple
        self.orig_size = size
        self.size = padded_size
        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels
        
        total_shimdma_channels = self.num_aie_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = f"gelu_{self.num_aie_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_gelu",
            callback_args=[
                self.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.num_channels,
                self.tile_size,
                0,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    f"gelu.o", 
                    depends=[SourceArtifact.new(self.base_dir / "aie_kernels" / "aie2p" / "gelu.cc")]
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        self.add_buffer("input", self.size)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "gelu", self.xclbin_artifact, self.xclbin_artifact.kernel_name, self.insts_artifact
        )
        self.add_to_runlist("gelu", "input", "output")

    def forward(self, x):
        """Forward pass for GELU activation"""
        if x.numel() > self.size:
            raise AIEOperatorConstraintError("AIEGELU: input too large for configured size")

        original_shape = x.shape
        x_flat = x.reshape(-1)
        
        # Pad if necessary
        pad_len = self.size - x_flat.numel()
        if pad_len > 0:
            x_flat = torch.nn.functional.pad(x_flat, (0, pad_len))

        # Execute on AIE
        x_np = torch_to_numpy(x_flat)
        self.write_buffer("input", x_np)
        self.write_buffer("output", np.zeros(self.size, dtype=bfloat16))
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=(self.size,), dtype=bfloat16)

        # Remove padding and restore shape
        if pad_len > 0:
            result = result[:x_flat.numel() - pad_len]
        
        return result.reshape(*original_shape)
