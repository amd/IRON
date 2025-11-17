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


def get_silu_artifacts(
    base_dir,
    device_type,
    size,
    tile_size=1024,
    num_columns=8,
    num_channels=2,
    prefix="silu_",
):
    file_name_base = f"{prefix}{num_columns}c_{num_channels}ch_{size}_{tile_size}t"

    mlir_artifact = PythonGeneratedMLIRArtifact.new(
        f"{file_name_base}.mlir",
        import_path=base_dir / "example" / "silu" / "silu.py",
        callback_fn="my_silu",
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
                f"silu.o", depends=[SourceArtifact.new("aie_kernels/aie2p/silu.cc")]
            ),
        ],
    )

    insts_artifact = InstsBinArtifact.new(
        f"{file_name_base}.bin", depends=[mlir_artifact]
    )

    return xclbin_artifact, insts_artifact


class AIESiLU(AIEOperatorBase):
    """AIE-accelerated SiLU activation function"""

    def __init__(self, size, num_columns=None, num_channels=None, tile_size=None):
        max_multiple = num_columns * tile_size
        padded_size = ((size + max_multiple - 1) // max_multiple) * max_multiple
        self.orig_size = size
        self.size = padded_size
        self.tile_size = tile_size

        self.num_columns = num_columns
        self.num_channels = num_channels
        # Enforce ShimDMA limits for SiLU (uses 1 input per core)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        total_shimdma_channels = self.num_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Compilation artifacts
        xclbin_artifact, insts_artifact = get_silu_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.size,
            self.tile_size,
            self.num_columns,
            self.num_channels,
            prefix="silu_",
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
        applicable = (
            len(x.shape) >= 1 and x.shape[-1] <= self.size and x.numel() <= self.size
        )
        if not applicable:
            raise AIEOperatorConstraintError("AIESiLU: incompatible tensor shape(s)")

        # Always flatten to [batch, orig_size]
        original_shape = x.shape
        batch = x.shape[0] if x.dim() > 1 else 1
        x_flat = x.reshape(batch, -1)

        pad_len = self.size - x_flat.shape[1]
        if pad_len > 0:
            x_flat = torch.nn.functional.pad(x_flat, (0, pad_len))

        out = self._execute_aie_operation(x_flat)

        # Remove padding if added
        numel = np.prod(original_shape)
        if pad_len > 0:
            out = out.reshape(-1)[..., :numel]
        # Restore original shape
        out = out.reshape(*original_shape)

        return out

    def _execute_aie_operation(self, x, y=None):
        """Execute SiLU operation on AIE hardware"""
        # x is [batch, size]
        batch = x.shape[0] if x.dim() > 1 else 1

        # Flatten inputs for AIE processing
        x_flat = x.view(-1)
        x_np = torch_to_numpy(x_flat)

        # Verify size matches expected
        if len(x_np) != self.size:
            raise AIEOperatorConstraintError(
                f"Input size x={len(x_np)} doesn't match configured size {self.size}"
            )

        self.write_buffer("input", x_np)
        test_pattern = np.zeros(len(x_np), dtype=bfloat16)
        self.write_buffer("output", test_pattern)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=x_np.shape, dtype=bfloat16)

        return result
