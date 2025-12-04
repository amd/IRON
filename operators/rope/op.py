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
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIERope(AIEOperatorBase):

    def __init__(
        self,
        size: int,
        last_dim: int,
        num_aie_columns=None,
        num_channels=None,
        method_type=0,
        context=None,
    ):
        self.size = size
        self.tile_size = last_dim

        if num_channels is None:
            num_channels = 1
        if num_aie_columns is None:
            num_aie_columns = 1

        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels
        self.method_type = method_type
        assert method_type in {0, 1}

        # Artifacts created by set_up_artifacts()
        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        # Compilation artifacts
        operator_dir = Path(__file__).parent
        file_name_base = f"rope_{self.num_aie_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t_{self.method_type}m"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="rope",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.num_channels,
                0,
                self.tile_size,
                self.method_type,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    f"rope_{self.method_type}.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir / "aie_kernels" / "generic" / "rope.cc"
                        )
                    ],
                    extra_flags=[
                        "-DTWO_HALVES" if 0 == self.method_type else "-DINTERLEAVED"
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
        self.add_buffer("in", self.size)
        self.add_buffer("angles", self.size)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "rope",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("rope", "in", "angles", "output")

    def forward(self, x, y):
        applicable = (
            x.shape[-1] * x.shape[-2] == self.size
            and x.shape[-1] == self.tile_size
            and x.shape[-1] % 16 == 0
            and x.shape[-2:] == y.shape
        )
        if not applicable:
            raise AIEOPeratorConstraintError("AIERope: incompatible tensor shape(s)")

        original_shape = x.shape
        if len(x.shape) > 2:
            x = x.view(-1, x.shape[-1])
        if len(y.shape) > 2:
            y = y.view(-1, y.shape[-1])

        batch_size, head_dim = x.shape
        rows_per_batch = self.num_aie_columns

        # Process in batches
        results = []
        for i in range(0, batch_size, rows_per_batch):
            end_idx = min(i + rows_per_batch, batch_size)
            batch_data = x[i:end_idx, :]

            # Pad if necessary to match expected rows_per_batch
            if batch_data.shape[0] < rows_per_batch:
                padding = torch.zeros(
                    rows_per_batch - batch_data.shape[0],
                    head_dim,
                    dtype=batch_data.dtype,
                    device=batch_data.device,
                )
                batch_data_padded = torch.cat([batch_data, padding], dim=0)
                result = self._process_batch(
                    batch_data_padded, y[i % y.shape[0] : batch_size]
                )
                result = result[: batch_data.shape[0], :]
            else:
                result = self._process_batch(batch_data, y[i % y.shape[0] : batch_size])

            results.append(result)

        # Concatenate all batch results
        result = torch.cat(results, dim=0)

        # Restore original shape if needed
        if len(original_shape) > 2:
            result = result.view(original_shape)

        return result

    def _process_batch(self, batch_data, angle_data):
        """Process a batch of sequences through the AIE kernel"""
        batch_flat = batch_data.view(-1)

        # Calculate buffer sizes for the batch
        input_size = batch_data.nbytes

        # Write data to buffers
        self.write_buffer("input", batch_data)
        self.write_buffer("angles", angle_data)
        test_pattern = np.zeros(len(batch_data), dtype=bfloat16)
        self.write_buffer("output", test_pattern)

        # Execute kernel
        self.run_runlist()

        # Read output
        batch_result = self.read_buffer_as_torch(
            "output", shape=batch_data.shape, dtype=bfloat16
        )

        return batch_result
