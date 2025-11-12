# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16

from .aie_base import AIEOperatorBase, AIEOperatorConstraintError
from ..compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from ..utils import torch_to_numpy, numpy_to_torch


class AIESiLU(AIEOperatorBase):
    """AIE-accelerated SiLU activation function"""

    def __init__(self, size, num_columns=None, num_channels=None, tile_size=None):
        self.size = size

        # SiLU uses only 1 input per core (less ShimDMA pressure than elementwise ops)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        if num_columns is not None and num_channels is not None:
            total_shimdma_channels = num_columns * num_channels  # 1 input per core
            if total_shimdma_channels > 16:  # Conservative ShimDMA limit
                print(
                    f"Warning: SiLU reducing {num_columns}c×{num_channels}ch to 8c×2ch (ShimDMA limit)"
                )
                num_columns = min(num_columns, 8)
                num_channels = min(num_channels, 2)

        self.num_columns = num_columns
        self.num_channels = num_channels
        self.tile_size = tile_size

        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Compilation artifacts
        file_name_base = f"silu_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=self.base_dir / "operators" / "silu" / "silu.py",
            callback_fn="my_silu",
            callback_args=[
                self.device_manager.device_type,
                self.size,
                self.num_columns,
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
                    f"silu.o", depends=[SourceArtifact.new("aie_kernels/aie2p/silu.cc")]
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

        # Runtime setup
        self.add_buffer("input", self.size)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "silu", xclbin_artifact, xclbin_artifact.kernel_name, insts_artifact
        )
        self.add_to_runlist("silu", "input", "output")

    def forward(self, x):
        """Forward pass for SiLU activation"""
        applicable = len(x.shape) >= 1 and x.shape[-1] == self.size
        if not applicable:
            raise AIEOperatorConstraintError("AIESiLU: incompatible tensor shape(s)")

        return self._execute_aie_operation(x)

    def _execute_aie_operation(self, x, y=None):
        """Execute SiLU activation operation on AIE hardware"""

        original_shape = x.shape
        x = x.view(-1, self.size)
        batch_seq_len = x.shape[0]

        # Extract single size-d vectors and process each [size] vector separately
        results = []

        for i in range(batch_seq_len):
            x_single = x[i]
            x_np = torch_to_numpy(x_single)

            # Verify size matches expected
            if len(x_np) != self.size:
                raise RuntimeError(
                    f"Input size {len(x_np)} doesn't match configured size {self.size}"
                )

            input_size = x_np.nbytes

            # Write data to buffers
            self.write_buffer("input", x_np)
            test_pattern = np.zeros(len(x_np), dtype=bfloat16)
            self.write_buffer("output", test_pattern)

            # Execute kernel
            self.run_runlist()

            # Read output
            result = self.read_buffer_as_torch(
                "output", shape=x_single.shape, dtype=bfloat16
            )
            results.append(result)

        result = torch.stack(results, dim=0)

        # Restore original shape
        result = result.view(original_shape)

        return result
