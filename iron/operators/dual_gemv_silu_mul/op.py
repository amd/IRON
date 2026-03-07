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
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from iron.common.utils import torch_to_numpy


def interleave_weights(W1, W2, rows_per_col, cols):
    """Interleave W1 and W2 rows per-column for the fused DMA pattern.

    Output layout: [W1_col0_rows, W2_col0_rows, W1_col1_rows, W2_col1_rows, ...]

    This ensures that when the DMA streams data to each column's A FIFO,
    the W1 rows arrive first followed by W2 rows, matching the core body's
    consumption order.
    """
    M = W1.shape[0]
    K = W1.shape[1]
    result = torch.empty(2 * M, K, dtype=W1.dtype)
    for col in range(cols):
        start = col * rows_per_col
        end = start + rows_per_col
        out_start = col * 2 * rows_per_col
        result[out_start : out_start + rows_per_col] = W1[start:end]
        result[out_start + rows_per_col : out_start + 2 * rows_per_col] = W2[start:end]
    return result


class AIEDualGEMVSiLUMul(AIEOperatorBase):
    """AIE-accelerated fused dual-GEMV + SiLU + elementwise multiply.

    Computes: output = silu(W1 @ x) * (W2 @ x)

    Fuses three operations into a single NPU design:
    - Two matrix-vector multiplications sharing the same input vector
    - SiLU activation on the first GEMV result
    - Elementwise multiplication of SiLU output with second GEMV result

    The intermediate vectors (left, right) never touch DRAM.
    W1 and W2 are pre-interleaved in DDR for DMA-compatible streaming.
    """

    def __init__(
        self,
        M,
        K,
        num_aie_columns=4,
        tile_size_input=4,
        tile_size_output=None,
        context=None,
    ):
        if tile_size_output is None:
            tile_size_output = M // num_aie_columns
        assert tile_size_output % tile_size_input == 0
        assert tile_size_output >= tile_size_input
        self.M = M
        self.K = K
        self.num_aie_columns = num_aie_columns
        self.tile_size_input = tile_size_input
        self.tile_size_output = tile_size_output

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def get_artifacts(self, prefix="dual_gemv_silu_mul_"):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"{prefix}{self.M}x{self.K}_{self.tile_size_input}tsi_"
            f"{self.tile_size_output}tso_{self.num_aie_columns}col"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_dual_gemv_silu_mul",
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
                    "dual_gemv_silu_mul.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / "aie2p"
                            / "dual_gemv_silu_mul.cc"
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
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        # The design expects a single interleaved weight buffer (2*M*K)
        self.add_buffer("weights_interleaved", 2 * self.M * self.K)
        self.add_buffer("vector", self.K)
        self.add_buffer("output", self.M)
        self.add_kernel(
            "dual_gemv_silu_mul",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist(
            "dual_gemv_silu_mul", "weights_interleaved", "vector", "output"
        )

    def forward(self, vector, matrix1=None, matrix2=None):
        """Forward pass: computes silu(matrix1 @ vector) * (matrix2 @ vector)"""
        vector = vector.reshape(*vector.shape[-1:])

        if matrix1 is not None and matrix2 is not None:
            rows_per_col = self.M // self.num_aie_columns
            w_interleaved = interleave_weights(
                matrix1, matrix2, rows_per_col, self.num_aie_columns
            )
            self.write_buffer("weights_interleaved", w_interleaved)
        self.write_buffer("vector", vector)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", (self.M,))
        return result
