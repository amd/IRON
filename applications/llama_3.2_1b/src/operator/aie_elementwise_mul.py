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


class AIEElementwiseMul(AIEOperatorBase):
    """AIE-accelerated element-wise multiplication"""

    def __init__(self, size, num_columns=None, num_channels=None, tile_size=None):
        self.size = size

        # Enforce ShimDMA limits for elementwise_mul (uses 2 inputs per core)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        if num_columns is not None and num_channels is not None:
            total_shimdma_channels = num_columns * num_channels * 2  # 2 inputs per core
            if total_shimdma_channels > 16:  # Conservative ShimDMA limit
                # print(
                #     f"Warning: ElementwiseMul reducing {num_columns}c×{num_channels}ch to 8c×2ch (ShimDMA limit)"
                # )
                num_columns = min(num_columns, 8)
                num_channels = min(num_channels, 2)

        self.num_columns = num_columns
        self.num_channels = num_channels
        self.tile_size = tile_size

        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Compilation artifacts
        file_name_base = f"mul_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=self.base_dir
            / "example"
            / "elementwise_mul"
            / "eltwise_mul.py",
            callback_fn="my_eltwise_mul",
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
                    f"mul.o", depends=[SourceArtifact.new("aie_kernels/generic/mul.cc")]
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

        # Runtime setup
        self.add_buffer("input1", self.size)
        self.add_buffer("input2", self.size)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "eltwise_mul", xclbin_artifact, xclbin_artifact.kernel_name, insts_artifact
        )
        self.add_to_runlist("eltwise_mul", "input1", "input2", "output")

    def forward(self, x, y):
        """Forward pass for element-wise multiplication"""
        applicable = (
            len(x.shape) >= 1
            and len(y.shape) >= 1
            and x.shape[-1] == self.size
            and y.shape[-1] == self.size
        )
        if not applicable:
            raise AIEOperatorConstraintError(
                "AIEElementwiseMul: incompatible tensor shape(s)"
            )

        return self._execute_aie_operation(x, y)

    def _execute_aie_operation(self, x, y):
        """Execute element-wise multiplication operation on AIE hardware"""

        original_shape = x.shape
        x = x.view(-1, self.size)
        y = y.view(-1, self.size)
        batch_seq_len = x.shape[0]

        # Extract single size-d vectors and process each [size] vector pair separately
        results = []

        for i in range(batch_seq_len):
            x_single = x[i]
            y_single = y[i]

            x_np = torch_to_numpy(x_single)
            y_np = torch_to_numpy(y_single)

            # Verify size matches expected
            if len(x_np) != self.size or len(y_np) != self.size:
                raise RuntimeError(
                    f"Input size x={len(x_np)}, y={len(y_np)} doesn't match configured size {self.size}"
                )

            self.write_buffer("input1", x_np)
            self.write_buffer("input2", y_np)
            test_pattern = np.zeros(len(x_np), dtype=bfloat16)
            self.write_buffer("output", test_pattern)
            self.run_runlist()
            result = self.read_buffer_as_torch(
                "output", shape=x_np.shape, dtype=bfloat16
            )
            results.append(result)

        result = torch.stack(results, dim=0)
        result = result.view(original_shape)

        return result
