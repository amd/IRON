# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.common import (
    AIEOperatorBase,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from iron.common.utils import torch_to_numpy
from iron.operators.dual_gemv_silu_mul.op import interleave_weights


class AIESwiGLUFusedDecode(AIEOperatorBase):
    """AIE-accelerated fully fused SwiGLU decode operator.

    Computes: output = Wdown @ (silu(Wgate @ x) * (Wup @ x))

    Fuses the entire SwiGLU MLP into a single NPU design with a 2-stage
    tile pipeline per column. The intermediate vector between the dual-GEMV
    stage and the down-projection GEMV stage stays on-chip via inter-tile
    ObjectFIFOs, eliminating DDR round-trips.

    Architecture (per column):
      Stage 1 (row 2): Dual-GEMV + SiLU + Mul -> intermediate chunk
      Stage 2 (row 3): Down-projection GEMV consuming intermediate on-chip

    Each of 4 columns produces a PARTIAL output vector. The host reduces
    the 4 partials by element-wise addition to get the final output.
    """

    def __init__(
        self,
        embedding_dim,
        hidden_dim,
        num_aie_columns=4,
        m_input_stage1=4,
        m_output_stage1=None,
        m_input_stage2=1,
        m_output_stage2=None,
        context=None,
    ):
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.num_aie_columns = num_aie_columns
        self.inter_dim_per_col = hidden_dim // num_aie_columns
        self.m_input_stage1 = m_input_stage1
        self.m_input_stage2 = m_input_stage2

        if m_output_stage1 is None:
            m_output_stage1 = self.inter_dim_per_col
        if m_output_stage2 is None:
            m_output_stage2 = embedding_dim
        self.m_output_stage1 = m_output_stage1
        self.m_output_stage2 = m_output_stage2

        # Weights to be set by user before compilation
        self.weights_gate = None  # (hidden_dim, embedding_dim)
        self.weights_up = None  # (hidden_dim, embedding_dim)
        self.weights_down = None  # (embedding_dim, hidden_dim)

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def get_artifacts(self, prefix="swiglu_fused_decode_"):
        operator_dir = Path(__file__).parent
        file_name_base = (
            f"{prefix}{self.embedding_dim}x{self.hidden_dim}_"
            f"{self.m_input_stage1}tsi1_{self.m_output_stage1}tso1_"
            f"{self.m_input_stage2}tsi2_{self.m_output_stage2}tso2_"
            f"{self.num_aie_columns}col"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_swiglu_fused_decode",
            callback_args=[
                self.context.device_manager.device_type,
                self.num_aie_columns,
                self.embedding_dim,
                self.hidden_dim,
                self.m_input_stage1,
                self.m_output_stage1,
                self.m_input_stage2,
                self.m_output_stage2,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    "swiglu_fused.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / "aie2p"
                            / "swiglu_fused.cc"
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

    def _pack_weights(self):
        """Pack all weights into a single DDR buffer.

        Layout: [interleaved_gate_up | down_col0 | down_col1 | ...]

        Gate+Up are interleaved per-column using the same pattern as
        AIEDualGEMVSiLUMul: [Wgate_col0_rows, Wup_col0_rows, ...].

        Down weights are sliced column-wise: column c gets
        Wdown[:, c*inter:(c+1)*inter] which is (embedding_dim, inter_dim_per_col).
        """
        rows_per_col = self.hidden_dim // self.num_aie_columns

        # Interleave gate+up weights
        w_gate_up = interleave_weights(
            self.weights_gate,
            self.weights_up,
            rows_per_col,
            self.num_aie_columns,
        )

        # Slice down weights column-wise and concatenate
        down_slices = []
        for c in range(self.num_aie_columns):
            start = c * self.inter_dim_per_col
            end = start + self.inter_dim_per_col
            down_slices.append(self.weights_down[:, start:end].contiguous())

        # Flatten and concatenate all weights
        gate_up_flat = w_gate_up.flatten()
        down_flat = torch.cat([s.flatten() for s in down_slices], dim=0)
        combined = torch.cat([gate_up_flat, down_flat], dim=0)

        return combined

    def set_up_runtime(self):
        combined_weights = self._pack_weights()
        total_weight_count = len(combined_weights)

        self.add_buffer(
            "weights_all",
            total_weight_count,
            static_data=torch_to_numpy(combined_weights),
        )
        self.add_buffer("input", self.embedding_dim)
        self.add_buffer(
            "output_partials",
            self.embedding_dim * self.num_aie_columns,
        )

        self.add_kernel(
            "swiglu_fused_decode",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist(
            "swiglu_fused_decode", "weights_all", "input", "output_partials"
        )

    def forward(self, x):
        """Forward pass: computes Wdown @ (silu(Wgate @ x) * (Wup @ x))

        Args:
            x: Input vector of shape (..., embedding_dim)

        Returns:
            Output vector of shape (..., embedding_dim)
        """
        original_shape = x.shape
        x_flat = x.reshape(x.shape[-1])
        assert x_flat.shape[0] == self.embedding_dim

        self.write_buffer("input", x_flat)
        self.run_runlist()

        # Read partial outputs and reduce by summation
        partials = self.read_buffer_as_torch(
            "output_partials",
            (self.num_aie_columns, self.embedding_dim),
        )
        result = partials.sum(dim=0)

        return result.view(original_shape)
