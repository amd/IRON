# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
from pathlib import Path

from iron.common import (
    AIEOperatorBase,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEFusedQKVProj(AIEOperatorBase):
    """AIE-accelerated fused Q/K/V projection.

    Concatenates Wq, Wk, Wv row-wise into a single weight matrix and runs
    one GEMV with M = q_dim + k_dim + v_dim, K = embedding_dim.
    The host splits the output into Q, K, V segments.

    This operator reuses the standard GEMV design and mv.o kernel.
    No new AIE kernel is needed.

    For Llama 3.2 1B:
        embedding_dim = 2048
        q_dim = 2048 (32 heads x 64 dim)
        k_dim = 512  (8 KV heads x 64 dim)
        v_dim = 512  (8 KV heads x 64 dim)
        total_out = 3072
    """

    def __init__(
        self,
        embedding_dim,
        q_dim,
        k_dim,
        v_dim,
        num_aie_columns=4,
        tile_size_input=4,
        tile_size_output=None,
        context=None,
    ):
        self.embedding_dim = embedding_dim
        self.q_dim = q_dim
        self.k_dim = k_dim
        self.v_dim = v_dim
        self.total_out = q_dim + k_dim + v_dim
        self.num_aie_columns = num_aie_columns

        if tile_size_output is None:
            tile_size_output = self.total_out // num_aie_columns

        assert (
            tile_size_output % tile_size_input == 0
            and tile_size_output >= tile_size_input
        ), "tile_size_output must be a multiple of tile_size_input"

        self.tile_size_input = tile_size_input
        self.tile_size_output = tile_size_output

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def get_artifacts(self, prefix="fused_qkv_proj_"):
        """Build compilation artifacts reusing the standard GEMV design."""
        gemv_dir = Path(__file__).parent.parent / "gemv"
        file_name_base = (
            f"{prefix}{self.total_out}x{self.embedding_dim}_"
            f"{self.tile_size_input}tsi_{self.tile_size_output}tso_"
            f"{self.num_aie_columns}col"
        )

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=gemv_dir / "design.py",
            callback_fn="my_matvec",
            callback_args=[
                self.context.device_manager.device_type,
                self.num_aie_columns,
                self.total_out,
                self.embedding_dim,
                self.tile_size_input,
                self.tile_size_output,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    "mv.o",
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
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        self.add_buffer("weights", self.total_out * self.embedding_dim)
        self.add_buffer("input", self.embedding_dim)
        self.add_buffer("output", self.total_out)
        self.add_kernel(
            "fused_qkv",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("fused_qkv", "weights", "input", "output")

    @staticmethod
    def concatenate_weights(weight_q, weight_k, weight_v):
        """Concatenate Wq, Wk, Wv row-wise into a single matrix.

        Args:
            weight_q: (q_dim, embedding_dim) bf16 tensor
            weight_k: (k_dim, embedding_dim) bf16 tensor
            weight_v: (v_dim, embedding_dim) bf16 tensor

        Returns:
            (total_out, embedding_dim) bf16 tensor where
            total_out = q_dim + k_dim + v_dim
        """
        return torch.cat([weight_q, weight_k, weight_v], dim=0)

    def forward(self, x, weight_q=None, weight_k=None, weight_v=None):
        """Forward pass: compute [Q, K, V] = [Wq; Wk; Wv] @ x and split.

        Args:
            x: Input vector of shape (..., embedding_dim) in bf16
            weight_q: Optional (q_dim, embedding_dim) weight matrix
            weight_k: Optional (k_dim, embedding_dim) weight matrix
            weight_v: Optional (v_dim, embedding_dim) weight matrix

        Returns:
            Tuple of (Q, K, V) tensors with shapes:
                Q: (q_dim,)
                K: (k_dim,)
                V: (v_dim,)
        """
        x_flat = x.reshape(x.shape[-1])

        if weight_q is not None and weight_k is not None and weight_v is not None:
            w_combined = self.concatenate_weights(weight_q, weight_k, weight_v)
            self.write_buffer("weights", w_combined)

        self.write_buffer("input", x_flat)
        self.run_runlist()

        qkv = self.read_buffer_as_torch("output", (self.total_out,))
        q = qkv[: self.q_dim]
        k = qkv[self.q_dim : self.q_dim + self.k_dim]
        v = qkv[self.q_dim + self.k_dim :]
        return q, k, v
