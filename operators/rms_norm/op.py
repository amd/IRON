# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn as nn
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from operators.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from operators.common.utils import torch_to_numpy


class AIERMSNorm(AIEOperatorBase):
    """AIE-accelerated RMS Normalization layer"""

    def __init__(
        self,
        size,
        eps=1e-6,
        num_aie_columns=None,
        num_channels=None,
        tile_size=None,
        weighted=False,
        context=None,
    ):
        max_multiple = num_aie_columns * tile_size
        padded_size = ((size + max_multiple - 1) // max_multiple) * max_multiple
        self.orig_size = size
        self.size = padded_size
        self.tile_size = tile_size

        self.num_columns = num_aie_columns
        self.num_channels = num_channels
        self.eps = eps
        self.weighted = weighted

        # Initializes weights to 1. Weights have size embedding dim, which is assumed to be tile size
        self.weight = nn.Parameter(torch.ones(tile_size, dtype=torch.bfloat16))

        # Enforce ShimDMA limits for weighted RMS Norm (uses 2 inputs per core)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        total_shimdma_channels = self.num_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        # Artifacts created by set_up_artifacts()
        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        # Compilation artifacts
        operator_dir = Path(__file__).parent
        file_name_base = f"weighted_rms_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design_weighted.py",
            callback_fn="my_weighted_rms_norm",
            callback_args=[
                self.context.device_manager.device_type,
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
                KernelArchiveArtifact.new(
                    f"rms_norm_archive.a",
                    depends=[
                        KernelObjectArtifact.new(
                            f"rms_norm.o",
                            depends=[
                                SourceArtifact.new(
                                    self.context.base_dir
                                    / "aie_kernels"
                                    / "aie2p"
                                    / "rms_norm.cc"
                                )
                            ],
                        ),
                        KernelObjectArtifact.new(
                            "mul.o",
                            depends=[
                                SourceArtifact.new(
                                    self.context.base_dir / "aie_kernels" / "generic" / "mul.cc"
                                )
                            ],
                        ),
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
        static_weights = None
        if self.weight is not None:
            static_weights = torch_to_numpy(self.weight)

        self.add_buffer("input1", self.size)
        self.add_buffer("input2", self.tile_size, static_data=static_weights)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "eltwise_mul",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("eltwise_mul", "input1", "input2", "output")

    def forward(self, x, y=None):
        """Forward pass through RMS normalization"""
        applicable = (
            len(x.shape) >= 1 and x.shape[-1] <= self.size and x.numel() <= self.size
        )
        if not applicable:
            raise AIEOperatorConstraintError("AIERMSNorm: incompatible tensor shape(s)")

        # Always flatten to [batch, orig_size]
        original_shape = x.shape
        batch = x.shape[0] if x.dim() > 1 else 1
        x_flat = x.reshape(batch, -1)
        if y is not None:
            y_flat = y.reshape(batch, -1)
        else:
            y_flat = None

        pad_len = self.size - x_flat.shape[1]
        if pad_len > 0:
            x_flat = torch.nn.functional.pad(x_flat, (0, pad_len))

        out = self._execute_aie_operation(x_flat, y_flat)

        # Remove padding if added
        numel = np.prod(original_shape)
        if pad_len > 0:
            out = out.reshape(-1)[..., :numel]
        # Restore original shape
        out = out.reshape(*original_shape)

        return out

    def _execute_aie_operation(self, x, y=None):
        """Execute RMS normalization on AIE hardware"""
        # x, y are [batch, size]
        batch = x.shape[0] if x.dim() > 1 else 1

        # Flatten inputs for AIE processing
        x_flat = x.view(-1)
        if y is not None:
            y_flat = y.view(-1)

        # Verify size matches expected
        if len(x_flat) != self.size:
            raise AIEOperatorConstraintError(
                f"Input size x={len(x_flat)} doesn't match configured size {self.size}"
            )

        self.write_buffer("input1", x_flat)
        if y is not None:
            self.write_buffer("input2", y_flat)
        else:
            assert (
                self.weight is not None
            ), "Weights must be provided either as input or during initialization."
        test_pattern = np.zeros(len(x_flat), dtype=bfloat16)
        self.write_buffer("output", test_pattern)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=x_flat.shape, dtype=bfloat16)

        return result
