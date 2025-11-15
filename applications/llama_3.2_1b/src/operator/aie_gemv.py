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


def get_gemv_artifacts(
    base_dir, device_type, M, K, tile_size=1, num_columns=1, prefix="gemv_"
):
    file_name_base = f"{prefix}{num_columns}c_{M}x{K}_{tile_size}t"

    mlir_artifact = PythonGeneratedMLIRArtifact.new(
        f"{file_name_base}.mlir",
        import_path=base_dir / "example" / "matrix_vector_mul" / "matrix_vector_mul.py",
        callback_fn="my_matvec",
        callback_args=[
            device_type,
            num_columns,
            M,
            K,
            tile_size,
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

    return xclbin_artifact, insts_artifact


class AIEGEMV(AIEOperatorBase):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    def __init__(
        self,
        M,
        K,
        num_columns=1,
        tile_size=1,
        is_mv=True,
        use_static_weight=False,
    ):

        self.M = M  # matrix rows  (if is_mv=False, matrix columns)
        self.K = K  # matrix columns, vector rows  (if is_mv=False, matrix rows, vector columns)
        self.num_columns = num_columns
        self.tile_size = tile_size
        self.is_mv = is_mv
        if use_static_weight:
            self.weight = torch.zeros(
                (M, K) if is_mv else (K, M), dtype=torch.bfloat16
            ).T  # weights are stored col-major/transposed
        else:
            self.weight = None

        # For compatibility with my_matvec parameters
        self.m = self.tile_size

        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Compilation Artifacts
        # ---
        xclbin_artifact, insts_artifact = get_gemv_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.M,
            self.K,
            self.tile_size,
            self.num_columns,
        )
        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

        # Runtime Setup
        # ---
        static_weights = None
        if self.weight is not None:
            # Kernel expects row-major weights, so might need to transpose;
            # also might need to transpose if is_mv
            if self.is_mv:
                static_weights = self.weight.T
            else:
                # Double transpose cancels out
                static_weights = self.weight
            if isinstance(static_weights, torch.Tensor):
                static_weights = torch_to_numpy(static_weights)
        self.add_kernel(
            "gemv", xclbin_artifact, xclbin_artifact.kernel_name, insts_artifact
        )
        self.add_buffer("matrix", self.M * self.K, static_data=static_weights)
        self.add_buffer("vector", self.K)
        self.add_buffer("output", self.M)
        self.add_to_runlist("gemv", "matrix", "vector", "output")

    def forward(self, vector, matrix=None):
        """Forward pass through GEMV operation

        Args:
            matrix: Input matrix of shape (..., M, K)
            vector: Input vector of shape (..., K) for MV or (..., M) for VM
            is_mv: True for matrix-vector multiplication, False for vector-matrix

        Returns:
            Output vector of shape (..., M) for MV or (..., K) for VM
        """

        # Flatten batch dimensions if needed
        if matrix is not None:
            matrix = matrix.reshape(*matrix.shape[-2:])
        vector = vector.reshape(*vector.shape[-1:])

        # For vector-matrix, we'll transpose the matrix internally
        if matrix is not None and not self.is_mv:
            # Transpose the matrix for vector-matrix multiplication
            # (if using static weights, the matrix is already transposed once at setup if needed)
            matrix = matrix.transpose(-2, -1)

        if matrix is not None:
            matrix_rows = matrix.shape[-2]
            matrix_cols = matrix.shape[-1]
        else:
            matrix_rows = self.M
            matrix_cols = self.K

        vector_size = vector.shape[-1]

        applicable = (
            matrix_cols == vector_size
            and matrix_rows == self.M
            and matrix_cols == self.K
            and (matrix is None or matrix.dtype == torch.bfloat16)
            and vector.dtype == torch.bfloat16
        )
        if not applicable:
            raise AIEOperatorConstraintError(
                "AIEElementwiseAdd: incompatible tensor shape(s)"
            )

        vector_np = torch_to_numpy(vector)
        if matrix is not None:
            matrix_np = torch_to_numpy(matrix)
            # If matrix is none, we are using static weights that have already been written to the buffer
            self.write_buffer("matrix", matrix_np)
        self.write_buffer("vector", vector_np)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", (self.M,))

        return result
