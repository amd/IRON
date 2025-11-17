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
from pathlib import Path


def get_elementwise_mul_artifacts(
    base_dir,
    device_type,
    size,
    tile_size=2048,
    num_columns=8,
    num_channels=2,
    prefix="eltwise_mul_",
):
    file_name_base = f"{prefix}{num_columns}c_{num_channels}ch_{size}_{tile_size}t"

    mlir_artifact = PythonGeneratedMLIRArtifact.new(
        f"{file_name_base}.mlir",
        import_path=base_dir / "example" / "elementwise_mul" / "eltwise_mul.py",
        callback_fn="my_eltwise_mul",
        callback_args=[
            device_type,
            size,
            num_columns,
            num_channels,
            tile_size,
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

    return xclbin_artifact, insts_artifact


class AIEElementwiseMul(AIEOperatorBase):
    """AIE-accelerated element-wise multiplication"""

    def __init__(self, size, num_columns=None, num_channels=None, tile_size=None):
        max_multiple = num_columns * tile_size
        padded_size = ((size + max_multiple - 1) // max_multiple) * max_multiple
        self.orig_size = size
        self.size = padded_size
        self.tile_size = tile_size

        self.num_columns = num_columns
        self.num_channels = num_channels
        # Enforce ShimDMA limits for elementwise_mul (uses 2 inputs per core)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        total_shimdma_channels = self.num_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Compilation artifacts
        xclbin_artifact, insts_artifact = get_elementwise_mul_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.size,
            self.tile_size,
            self.num_columns,
            self.num_channels,
            prefix="",
        )

        # Override device_type in the mlir_artifact's callback_args if needed
        mlir_artifact = xclbin_artifact.depends[0]
        mlir_artifact.callback_args[0] = self.device_manager.device_type

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
            and x.shape[-1] <= self.size
            and y.shape[-1] <= self.size
            and x.numel() <= self.size
            and y.numel() <= self.size
            and x.numel() == y.numel()
            and x.shape == y.shape
        )
        if not applicable:
            raise AIEOperatorConstraintError(
                "AIEElementwiseMul: incompatible tensor shape(s)"
            )

        # Always flatten to [batch, orig_size]
        original_shape = x.shape
        batch = x.shape[0] if x.dim() > 1 else 1
        x_flat = x.reshape(batch, -1)
        y_flat = y.reshape(batch, -1)

        pad_len = self.size - x_flat.shape[1]
        if pad_len > 0:
            x_flat = torch.nn.functional.pad(x_flat, (0, pad_len))
            y_flat = torch.nn.functional.pad(y_flat, (0, pad_len))

        out = self._execute_aie_operation(x_flat, y_flat)

        # Remove padding if added
        numel = np.prod(original_shape)
        if pad_len > 0:
            out = out.reshape(-1)[..., :numel]
        # Restore original shape
        out = out.reshape(*original_shape)

        return out

    def _execute_aie_operation(self, x, y):
        """Execute element-wise multiplication operation on AIE hardware"""
        # x, y are [batch, size]
        batch = x.shape[0] if x.dim() > 1 else 1

        # Flatten inputs for AIE processing
        x_flat = x.view(-1)
        y_flat = y.view(-1)
        x_np = torch_to_numpy(x_flat)
        y_np = torch_to_numpy(y_flat)

        # Verify size matches expected
        if len(x_np) != self.size or len(y_np) != self.size:
            raise AIEOperatorConstraintError(
                f"Input size x={len(x_np)}, y={len(y_np)} doesn't match configured size {self.size}"
            )

        self.write_buffer("input1", x_np)
        self.write_buffer("input2", y_np)
        test_pattern = np.zeros(len(x_np), dtype=bfloat16)
        self.write_buffer("output", test_pattern)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=x_np.shape, dtype=bfloat16)

        return result
