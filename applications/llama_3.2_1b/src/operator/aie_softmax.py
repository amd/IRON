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


class AIESoftmax(AIEOperatorBase):

    def __init__(self, size: int, last_dim: int, num_columns=1, num_channels=1):
        self.size = size
        self.tile_size = last_dim

        self.num_channels = num_channels
        self.num_columns = num_columns

        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Compilation artifacts
        file_name_base = f"softmax_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=self.base_dir / "example" / "softmax" / "softmax.py",
            callback_fn="softmax",
            callback_args=[
                self.device_manager.device_type,
                self.size,
                self.num_columns,
                self.num_channels,
                0,
                self.tile_size,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    f"softmax.o",
                    depends=[SourceArtifact.new("aie_kernels/aie2p/softmax.cc")],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"gemm_{file_name_base}.bin", depends=[mlir_artifact]
        )

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

        # Runlist setup
        self.add_buffer("in", self.size)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "softmax", xclbin_artifact, xclbin_artifact.kernel_name, insts_artifact
        )
        self.add_to_runlist("softmax", "in", "output")

    def forward(self, x):
        applicable = (
            x.shape[-1] * x.shape[-2] == self.size
            and x.shape[-1] == self.tile_size
            and x.shape[-1] % 16 == 0
            and x.shape[-2] % 16 == 0
        )
        if not applicable:
            raise AIEOperatorConstraintError("AIESoftmax: incompatible tensor shape(s)")

        return self._execute_aie_operation(x)

    def _execute_aie_operation(self, x):
        original_shape = x.shape

        # Reshape for processing
        # Split x into a list of H tensors of size [S_q, S_kv]
        heads = x.shape[1]
        x_list = [x[0, h, :, :] for h in range(heads)]
        results = []
        for i in range(heads):
            x_np = torch_to_numpy(x_list[i])
            input_size = x_np.nbytes
            self.write_buffer("in", x_np)
            test_pattern = np.zeros(len(x_np), dtype=bfloat16)
            self.write_buffer("output", test_pattern)
            self.run_runlist()
            result = self.read_buffer_as_torch(
                "output", shape=x_list[i].shape, dtype=bfloat16
            )
            results.append(result)

        result = torch.stack(results, dim=0).unsqueeze(
            0
        )  # Shape: (1, heads, S_q, S_kv)

        return result
