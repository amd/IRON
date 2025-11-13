# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn as nn
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


class AIERMSNorm(AIEOperatorBase):
    """AIE-accelerated RMS Normalization layer"""

    def __init__(
        self, emb_dim, eps=1e-6, num_columns=None, num_channels=None, tile_size=None
    ):
        self.emb_dim = emb_dim
        self.eps = eps

        if num_channels is None:
            num_channels = 2
        if num_columns is None:
            num_columns = 4

        # Initializes weights to 1
        self.weight = nn.Parameter(torch.ones(emb_dim, dtype=torch.bfloat16))

        self.num_columns = num_columns
        self.num_channels = num_channels
        self.tile_size = tile_size

        # Initialize AIE base class
        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Compilation artifacts
        total_elements = self.emb_dim * self.num_columns * self.num_channels
        file_name_base = f"weighted_rms_{total_elements}_{self.num_columns}c_{self.num_channels}ch_{self.emb_dim}emb"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=self.base_dir
            / "operators"
            / "rms_norm"
            / "weighted_rms_norm.py",
            callback_fn="my_weighted_rms_norm",
            callback_args=[
                self.device_manager.device_type,
                total_elements,
                self.num_columns,
                self.num_channels,
                self.emb_dim,
                0,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    f"rms_norm.o",
                    depends=[SourceArtifact.new("aie_kernels/aie2p/rms_norm.cc")],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

        # Runtime setup
        total_elements = self.emb_dim * self.num_columns * self.num_channels
        self.add_buffer("input1", total_elements)
        self.add_buffer("input2", total_elements)
        self.add_buffer("output", total_elements)
        self.add_kernel(
            "eltwise_mul", xclbin_artifact, xclbin_artifact.kernel_name, insts_artifact
        )
        self.add_to_runlist("eltwise_mul", "input1", "input2", "output")

    def forward(self, x, y):
        """Forward pass through RMS normalization"""
        applicable = (
            len(x.shape) >= 2
            and x.shape[-1] == self.emb_dim
            and x.dtype == torch.bfloat16
        )
        if not applicable:
            raise AIEOPeratorConstraintError("AIERMSNorm: incompatible tensor shape(s)")

        return self._execute_aie_operation(x, y)

    def _execute_aie_operation(self, x, y):
        """Execute RMS normalization on AIE hardware"""

        original_shape = x.shape
        if len(x.shape) > 2:
            x = x.view(-1, x.shape[-1])
        if y is not None and len(y.shape) > 1:
            y = y.view(-1, y.shape[-1])

        batch_size, seq_len = x.shape
        rows_per_batch = self.num_columns * self.num_channels

        # Process in batches
        results = []
        for i in range(0, batch_size, rows_per_batch):
            end_idx = min(i + rows_per_batch, batch_size)
            batch_data = x[i:end_idx, :]

            # Pad if necessary to match expected rows_per_batch
            if batch_data.shape[0] < rows_per_batch:
                padding = torch.zeros(
                    rows_per_batch - batch_data.shape[0],
                    seq_len,
                    dtype=batch_data.dtype,
                    device=batch_data.device,
                )
                batch_data_padded = torch.cat([batch_data, padding], dim=0)
                result = self._process_batch(batch_data_padded, y)
                result = result[: batch_data.shape[0], :]
            else:
                result = self._process_batch(batch_data, y)

            results.append(result)

        # Concatenate all batch results
        result = torch.cat(results, dim=0)

        # Restore original shape if needed
        if len(original_shape) > 2:
            result = result.view(original_shape)

        return result

    def _process_batch(self, batch_data, weight_data):
        """Process a batch of sequences through the AIE kernel"""
        batch_flat = batch_data.view(-1)
        input_data = torch_to_numpy(batch_flat)
        weights_data = torch_to_numpy(weight_data)

        # Calculate buffer sizes for the batch
        input_size = input_data.nbytes

        # Write data to buffers
        self.write_buffer("input1", input_data)
        self.write_buffer("input2", weights_data)
        # Initialize output buffer
        test_pattern = np.zeros(len(input_data), dtype=bfloat16)
        self.write_buffer("output", test_pattern)

        # Execute kernel
        self.run_runlist()

        # Read output
        batch_result = self.read_buffer_as_torch(
            "output", shape=batch_data.shape, dtype=bfloat16
        )

        return batch_result
