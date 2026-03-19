# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
import logging
from pathlib import Path

from iron.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEElementwiseAdd(AIEOperatorBase):
    """AIE-accelerated element-wise addition"""

    def __init__(
        self,
        size,
        num_aie_columns=None,
        num_channels=None,
        tile_size=None,
        context=None,
    ):
        max_multiple = num_aie_columns * tile_size
        padded_size = ((size + max_multiple - 1) // max_multiple) * max_multiple
        self.orig_size = size
        self.size = padded_size
        self.tile_size = tile_size

        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels

        # P2-6 CONFIGURATION VALIDATION: Warn about suboptimal 1-column large tile configs
        # Based on benchmark analysis (UPDATE-3.md):
        # - 1-column with tile >= 1024 shows +56% latency regression
        if num_aie_columns == 1 and tile_size and tile_size >= 1024:
            logger.warning(
                f"P2-6: 1-column configuration with large tile size ({tile_size}) "
                f"shows latency regression (+56%). "
                f"Recommend using 4-8 columns for large tile workloads."
            )

        # Enforce ShimDMA limits for elementwise_add (uses 2 inputs per core)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        total_shimdma_channels = self.num_aie_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        # Artifacts created by set_up_artifacts()
        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        # Compilation artifacts
        operator_dir = Path(__file__).parent
        file_name_base = f"add_{self.num_aie_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_eltwise_add",
            callback_args=[
                self.context.device_manager.device_type,
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
                    f"add.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir / "aie_kernels" / "generic" / "add.cc"
                        )
                    ],
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
        # Runtime setup
        self.add_buffer("input1", self.size)
        self.add_buffer("input2", self.size)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "eltwise_add",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("eltwise_add", "input1", "input2", "output")

    def forward(self, x, y):
        """Forward pass for element-wise addition"""
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
                "AIEElementwiseAdd: incompatible tensor shape(s)"
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
        """Execute element-wise addition operation on AIE hardware"""
        # x, y are [batch, size]
        batch = x.shape[0] if x.dim() > 1 else 1

        # Flatten inputs for AIE processing
        x_flat = x.view(-1)
        y_flat = y.view(-1)

        # Verify size matches expected
        if len(x_flat) != self.size or len(y_flat) != self.size:
            raise AIEOperatorConstraintError(
                f"Input size x={len(x_flat)}, y={len(y_flat)} doesn't match configured size {self.size}"
            )

        self.write_buffer("input1", x_flat)
        self.write_buffer("input2", y_flat)
        test_pattern = np.zeros(len(x_flat), dtype=bfloat16)
        self.write_buffer("output", test_pattern)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=x_flat.shape, dtype=bfloat16)

        return result
