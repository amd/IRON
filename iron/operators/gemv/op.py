# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
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
from iron.common.utils import torch_to_numpy


class AIEGEMV(AIEOperatorBase):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    def __init__(
        self,
        M,
        K,
        num_aie_columns=1,
        tile_size_input=2,
        tile_size_output=None,
        is_mv=True,
        use_static_weight=False,
        context=None,
    ):
        if tile_size_output is None:
            tile_size_output = tile_size_input

        assert (
            tile_size_output % tile_size_input == 0
            and tile_size_output >= tile_size_input
        ), "tile_size_output must be a multiple of tile_size_input"
        self.M = M  # matrix rows  (if is_mv=False, matrix columns)
        self.K = K  # matrix columns, vector rows  (if is_mv=False, matrix rows, vector columns)
        self.num_aie_columns = num_aie_columns
        self.tile_size_input = tile_size_input
        self.tile_size_output = tile_size_output
        self.is_mv = is_mv
        if use_static_weight:
            self.weight = torch.zeros(
                (M, K) if is_mv else (K, M), dtype=torch.bfloat16
            ).T  # weights are stored col-major/transposed
        else:
            self.weight = None

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def get_artifacts(self, prefix="gemv_"):
        # The underlying MLIR design is a matrix-vector multiplication. We support vector-matrix multiplication by transposing the matrix beforehand (AB = C <=> B^T A^T = C^T).
        operator_dir = Path(__file__).parent
        file_name_base = f"{prefix}{self.M}x{self.K}_{self.tile_size_input}tsi_{self.tile_size_output}tso_{self.num_aie_columns}col"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_matvec",
            callback_args=[
                self.context.device_manager.device_type,
                self.num_aie_columns,
                self.M,
                self.K,
                self.tile_size_input,
                self.tile_size_output,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    f"mv.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir / "aie_kernels" / "generic" / "mv.cc"
                        )
                    ],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        return xclbin_artifact, insts_artifact

    def set_up_artifacts(self):
        xclbin_artifact, insts_artifact = self.get_artifacts()

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        # If this operator is only used as a sub-operator in another operator that sets it up, we should skip the setup here as those artifacts and buffers may not be needed.
        # Runtime Setup
        # ---
        static_weights = None
        if self.weight is not None:
            # Kernel expects row-major weights, so might need to transpose (torch weights are stored in col-major);
            # also might need to transpose if is_mv
            if self.is_mv:
                static_weights = self.weight.T
            else:
                # Double transpose cancels out
                static_weights = self.weight
            if isinstance(static_weights, torch.Tensor):
                static_weights = torch_to_numpy(static_weights)
        self.add_kernel(
            "gemv",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
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
        original_vector_dims = vector.ndim
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

        if matrix is not None:
            # If matrix is none, we are using static weights that have already been written to the buffer
            self.write_buffer("matrix", matrix)
        self.write_buffer("vector", vector)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", (self.M,))

        # Add back batch dimensions if we removed them earlier.
        if result.ndim < original_vector_dims:
            result = result.reshape(*((1,) * (original_vector_dims - 1)), -1)

        return result
