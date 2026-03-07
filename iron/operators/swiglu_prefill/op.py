# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import torch
import numpy as np
from ml_dtypes import bfloat16

from iron.common import (
    AIEOperatorBase,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from iron.operators.gemm.op import AIEGEMM
from iron.operators.silu_mul.op import AIESiLUMul
from iron.common.utils import torch_to_numpy


class AIESwiGLUPrefill(AIEOperatorBase):

    def __init__(
        self, seq_len, embedding_dim, hidden_dim, prio_accuracy=False, context=None
    ):
        self.seq_len = seq_len
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        # weights to be set by user (e.g., assign_weights in FeedForward block)
        self.weights_1 = None
        self.weights_2 = None
        self.weights_3 = None

        self.prio_accuracy = prio_accuracy
        # Artifacts created by set_up_artifacts()
        self.combined_xclbin = None
        self.gemm_1_xclbin = None
        self.gemm_1_insts = None
        self.silu_mul_xclbin = None
        self.silu_mul_insts = None
        self.gemm_2_xclbin = None
        self.gemm_2_insts = None

        super().__init__(context=context)

    def set_up_artifacts(self):
        # Artifact setup
        # ---
        # Note: All operators (GEMM, SiLUMul) apply their own padding
        # to meet hardware alignment requirements. We store the padded dimensions
        # from GEMM and verify that all operators use consistent padded sizes.
        artifacts = []
        device_str = self.context.device_manager.device_str()

        accuracy_flags = {}
        if self.prio_accuracy:
            accuracy_flags = {
                "emulate_bf16_mmul_with_bfp16": False,
                "prio_accuracy": True,
                "round_conv_even": True,
            }

        gemm_1 = AIEGEMM(
            M=self.seq_len, K=self.embedding_dim, N=self.hidden_dim, **accuracy_flags
        )
        self.gemm_1 = gemm_1
        self.seq_len_padded = gemm_1.M
        self.embedding_dim_padded = gemm_1.K
        self.hidden_dim_padded = gemm_1.N
        gemm_1_xclbin, gemm_1_insts = gemm_1.get_artifacts(prefix="swiglu_gemm_1_")
        gemm_1_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemm_1",
            "--xclbin-kernel-id=0x901",
        ]
        gemm_1_xclbin.kernel_name = "swiglu_gemm_1"
        artifacts.append(
            gemm_1_insts
        )  # xclbin artifact will be pulled in as a dependency of last xclbin

        silu_mul = AIESiLUMul(
            size=self.seq_len_padded * self.hidden_dim_padded,
            num_aie_columns=8,
            num_channels=2,
            tile_size=self.hidden_dim_padded // 8,
        )
        self.silu_mul = silu_mul
        assert silu_mul.size == self.seq_len_padded * self.hidden_dim_padded

        silu_mul_xclbin, silu_mul_insts = silu_mul.get_artifacts(
            prefix="swiglu_silu_mul_"
        )
        silu_mul_xclbin.xclbin_input = gemm_1_xclbin
        silu_mul_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_silu_mul",
            "--xclbin-kernel-id=0x902",
        ]
        silu_mul_xclbin.kernel_name = "swiglu_silu_mul"
        silu_mul_xclbin.depends += [gemm_1_xclbin]
        artifacts.append(silu_mul_insts)

        gemm_2 = AIEGEMM(
            M=self.seq_len, K=self.hidden_dim, N=self.embedding_dim, **accuracy_flags
        )
        self.gemm_2 = gemm_2
        assert gemm_2.M == self.seq_len_padded
        assert gemm_2.K == self.hidden_dim_padded
        assert gemm_2.N == self.embedding_dim_padded

        gemm_2_xclbin, gemm_2_insts = gemm_2.get_artifacts(prefix="swiglu_gemm_2_")
        gemm_2_xclbin.xclbin_input = silu_mul_xclbin
        gemm_2_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemm_2",
            "--xclbin-kernel-id=0x903",
        ]
        gemm_2_xclbin.kernel_name = "swiglu_gemm_2"
        gemm_2_xclbin.depends += [silu_mul_xclbin]
        artifacts.append(gemm_2_xclbin)
        artifacts.append(gemm_2_insts)

        self.combined_xclbin = gemm_2_xclbin
        self.gemm_1_xclbin = gemm_1_xclbin
        self.gemm_1_insts = gemm_1_insts
        self.silu_mul_xclbin = silu_mul_xclbin
        self.silu_mul_insts = silu_mul_insts
        self.gemm_2_xclbin = gemm_2_xclbin
        self.gemm_2_insts = gemm_2_insts

        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        # Runtime setup
        # ---
        self.add_buffer("input", self.seq_len_padded * self.embedding_dim_padded)
        self.add_buffer(
            "weights_1",
            self.embedding_dim_padded * self.hidden_dim_padded,
            static_data=torch_to_numpy(self.weights_1.T),
        )
        self.add_buffer(
            "weights_2",
            self.embedding_dim_padded * self.hidden_dim_padded,
            static_data=torch_to_numpy(self.weights_2.T),
        )
        self.add_buffer(
            "weights_3",
            self.hidden_dim_padded * self.embedding_dim_padded,
            static_data=torch_to_numpy(self.weights_3.T),
        )
        self.add_buffer("left", self.seq_len_padded * self.hidden_dim_padded)
        self.add_buffer("right", self.seq_len_padded * self.hidden_dim_padded)
        self.add_buffer("intermediate", self.seq_len_padded * self.hidden_dim_padded)
        self.add_buffer("output", self.seq_len_padded * self.embedding_dim_padded)
        self.add_kernel(
            "swiglu_gemm_1",
            self.combined_xclbin,
            self.gemm_1_xclbin.kernel_name,
            self.gemm_1_insts,
        )
        self.add_kernel(
            "swiglu_silu_mul",
            self.combined_xclbin,
            self.silu_mul_xclbin.kernel_name,
            self.silu_mul_insts,
        )
        self.add_kernel(
            "swiglu_gemm_2",
            self.combined_xclbin,
            self.gemm_2_xclbin.kernel_name,
            self.gemm_2_insts,
        )
        self.add_to_runlist("swiglu_gemm_1", "input", "weights_1", "left")
        self.add_to_runlist("swiglu_gemm_1", "input", "weights_2", "right")
        self.add_to_runlist("swiglu_silu_mul", "left", "right", "intermediate")
        self.add_to_runlist("swiglu_gemm_2", "intermediate", "weights_3", "output")

    def forward(self, x):
        """Forward pass for SwiGLU operation"""

        # Always flatten to [batch, orig_size]
        original_shape = x.shape
        batch = x.shape[0] if x.dim() > 1 else 1
        x_flat = x.reshape(batch, -1)

        out = self._execute_aie_operation(x_flat)

        # Restore original shape
        out = out.reshape(*original_shape)

        return out

    def _execute_aie_operation(self, x):
        # x is [batch, size]
        batch = x.shape[0] if x.dim() > 1 else 1

        # Flatten inputs for AIE processing
        x_flat = x.view(-1)

        # Verify input size matches expected dimensions
        expected_size = batch * self.seq_len * self.embedding_dim
        assert x_flat.shape[0] == expected_size

        # Pad input if necessary to match GEMM requirements
        if self.seq_len_padded * self.embedding_dim_padded > x_flat.shape[0]:
            x_padded = torch.zeros(
                self.seq_len_padded * self.embedding_dim_padded,
                dtype=x_flat.dtype,
                device=x_flat.device,
            )
            x_padded[: x_flat.shape[0]] = x_flat
            x_flat = x_padded

        self.write_buffer("input", x_flat)
        self.run_runlist()

        # Read padded output buffer
        result_padded = self.read_buffer_as_torch(
            "output",
            shape=(self.seq_len_padded * self.embedding_dim_padded,),
            dtype=bfloat16,
        )

        # Extract only the unpadded portion
        result = result_padded[:expected_size].view(batch, -1)

        return result
