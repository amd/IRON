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


class AIEGEMV(AIEOperatorBase):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    def __init__(self, M, K, num_columns=1, tile_size=1, is_mv=True):

        self.M = M
        self.K = K
        self.num_columns = num_columns
        self.tile_size = tile_size
        self.is_mv = is_mv

        # For compatibility with my_matvec parameters
        self.m = self.tile_size

        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Compilation Artifacts
        # ---
        file_name_base = f"gemv_{self.num_columns}c_{self.M}x{self.K}_{self.tile_size}t"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=self.base_dir
            / "example"
            / "matrix_vector_mul"
            / "matrix_vector_mul.py",
            callback_fn="my_matvec",
            callback_args=[
                self.device_manager.device_type,
                self.num_columns,
                self.M,
                self.K,
                self.tile_size,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    f"mv.o", depends=[SourceArtifact.new("aie_kernels/generic/mv.cc")]
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

        # Runtime Setup
        # ---
        self.add_kernel(
            "gemv", xclbin_artifact, xclbin_artifact.kernel_name, insts_artifact
        )
        self.add_buffer("matrix", self.M * self.K)
        self.add_buffer("vector", self.K)
        self.add_buffer("output", self.M)
        self.add_to_runlist("gemv", "matrix", "vector", "output")

    def forward(self, matrix, vector):
        """Forward pass through GEMV operation

        Args:
            matrix: Input matrix of shape (..., M, K)
            vector: Input vector of shape (..., K) for MV or (..., M) for VM
            is_mv: True for matrix-vector multiplication, False for vector-matrix

        Returns:
            Output vector of shape (..., M) for MV or (..., K) for VM
        """
        # Handle 3D tensor shapes like (1, 1, emb_dim) by getting the last dimensions
        matrix_rows = matrix.shape[-2]
        matrix_cols = matrix.shape[-1]
        vector_size = vector.shape[-1]

        applicable = (
            vector_size == (matrix_cols if self.is_mv else matrix_rows)
            and matrix_rows == (self.M if self.is_mv else self.K)
            and matrix_cols == (self.K if self.is_mv else self.M)
            and matrix.dtype == torch.bfloat16
            and vector.dtype == torch.bfloat16
        )
        if not applicable:
            raise AIEOperatorConstraintError(
                "AIEElementwiseAdd: incompatible tensor shape(s)"
            )

        # For vector-matrix, we'll transpose the matrix internally
        if not self.is_mv:
            # Transpose the matrix for vector-matrix multiplication
            matrix = matrix.transpose(-2, -1)

        # Ensure vector is 1D for the last dimension
        if vector.dim() > 1 and vector.shape[-1] == 1:
            vector = vector.squeeze(-1)

        return self._execute_aie_operation(matrix, vector)

    def _execute_aie_operation(self, matrix, vector):
        """Execute matrix-vector multiplication on AIE hardware"""

        # Store original shapes
        original_matrix_shape = matrix.shape
        original_vector_shape = vector.shape

        # Flatten batch dimensions if needed
        if len(matrix.shape) > 2:
            matrix = matrix.view(-1, matrix.shape[-2], matrix.shape[-1])
        if len(vector.shape) > 1:
            vector = vector.view(-1, vector.shape[-1])

        batch_size = matrix.shape[0] if len(matrix.shape) > 2 else 1

        # Process each batch element
        results = []
        for i in range(batch_size):
            if batch_size > 1:
                matrix_batch = matrix[i]
                vector_batch = vector[i] if len(vector.shape) > 1 else vector
            else:
                matrix_batch = matrix
                vector_batch = vector

            result = self._process_single_gemv(matrix_batch, vector_batch)
            results.append(result)

        # Concatenate results
        if len(results) > 1:
            result = torch.stack(results, dim=0)
        else:
            result = results[0]

        # Restore original shape if needed
        if len(original_matrix_shape) > 2:
            if self.is_mv:
                result_shape = original_matrix_shape[:-2] + (self.M,)
            else:
                result_shape = original_matrix_shape[:-2] + (self.K,)
            result = result.view(result_shape)

        return result

    def _process_single_gemv(self, matrix_data, vector_data):
        """Process a single matrix-vector multiplication through the AIE kernel"""
        # Ensure inputs are 2D and 1D respectively
        if matrix_data.dim() == 3:
            matrix_data = matrix_data.squeeze(0)
        if vector_data.dim() == 2:
            vector_data = vector_data.squeeze(0)

        matrix_np = torch_to_numpy(matrix_data.contiguous())
        vector_np = torch_to_numpy(vector_data.contiguous())

        self.write_buffer("matrix", matrix_np)
        self.write_buffer("vector", vector_np)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", (self.M,))

        return result
