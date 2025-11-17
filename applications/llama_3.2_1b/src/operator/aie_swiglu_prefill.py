# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import torch
import numpy as np
from ml_dtypes import bfloat16
import logging

from .aie_base import AIEOperatorBase
from ..compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from ..utils import torch_to_numpy, numpy_to_torch
from .aie_gemm import get_gemm_artifacts
from .aie_silu import get_silu_artifacts
from .aie_elementwise_mul import get_elementwise_mul_artifacts


class AIESwiGLUPrefill(AIEOperatorBase):

    def __init__(self, seq_len, embedding_dim, hidden_dim):
        self.seq_len = seq_len
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        # weights to be set by user (e.g., assign_weights in FeedForward block)
        self.weights_1 = None
        self.weights_2 = None
        self.weights_3 = None
        super().__init__()

    def set_up(self):
        # Artifact setup
        # ---
        artifacts = []
        device_str = self.device_manager.device_str()
        gemm_config = {}

        gemm_1_xclbin, gemm_1_insts = get_gemm_artifacts(
            self.base_dir,
            device_str,
            self.seq_len,
            self.embedding_dim,
            self.hidden_dim,
            prefix="swiglu_gemm_1_",
            **gemm_config
        )
        gemm_1_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemm_1",
            "--xclbin-kernel-id=0x901",
        ]
        gemm_1_xclbin.kernel_name = "swiglu_gemm_1"
        artifacts.append(
            gemm_1_insts
        )  # xclbin artifact will be pulled in as a dependency of last xclbin

        silu_xclbin, silu_insts = get_silu_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.seq_len * self.hidden_dim,
            tile_size=self.hidden_dim,
            num_columns=8,
            prefix="swiglu_silu_",
        )
        silu_xclbin.xclbin_input = gemm_1_xclbin
        silu_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_silu",
            "--xclbin-kernel-id=0x902",
        ]
        silu_xclbin.kernel_name = "swiglu_silu"
        silu_xclbin.depends += [gemm_1_xclbin]
        artifacts.append(silu_insts)

        eltwise_mul_xclbin, eltwise_mul_insts = get_elementwise_mul_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.seq_len * self.hidden_dim,
            tile_size=self.hidden_dim,
            num_columns=8,
            prefix="swiglu_eltwise_mul_",
        )
        eltwise_mul_xclbin.xclbin_input = silu_xclbin
        eltwise_mul_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_eltwise_mul",
            "--xclbin-kernel-id=0x903",
        ]
        eltwise_mul_xclbin.kernel_name = "swiglu_eltwise_mul"
        eltwise_mul_xclbin.depends += [silu_xclbin]
        artifacts.append(eltwise_mul_insts)

        gemm_2_xclbin, gemm_2_insts = get_gemm_artifacts(
            self.base_dir,
            device_str,
            self.seq_len,
            self.hidden_dim,
            self.embedding_dim,
            prefix="swiglu_gemm_2_",
            **gemm_config
        )
        gemm_2_xclbin.xclbin_input = eltwise_mul_xclbin
        gemm_2_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemm_2",
            "--xclbin-kernel-id=0x904",
        ]
        gemm_2_xclbin.kernel_name = "swiglu_gemm_2"
        gemm_2_xclbin.depends += [eltwise_mul_xclbin]
        artifacts.append(gemm_2_xclbin)
        artifacts.append(gemm_2_insts)

        self.add_artifacts(artifacts)

        # Runtime setup
        # ---
        combined_xclbin = gemm_2_xclbin
        self.add_buffer("input", self.seq_len * self.embedding_dim)
        self.add_buffer(
            "weights_1",
            self.embedding_dim * self.hidden_dim,
            static_data=torch_to_numpy(self.weights_1.T),
        )
        self.add_buffer(
            "weights_2",
            self.embedding_dim * self.hidden_dim,
            static_data=torch_to_numpy(self.weights_2.T),
        )
        self.add_buffer(
            "weights_3",
            self.hidden_dim * self.embedding_dim,
            static_data=torch_to_numpy(self.weights_3.T),
        )
        self.add_buffer("left", self.seq_len * self.hidden_dim)
        self.add_buffer("left_swished", self.seq_len * self.hidden_dim)
        self.add_buffer("right", self.seq_len * self.hidden_dim)
        self.add_buffer("intermediate", self.seq_len * self.hidden_dim)
        self.add_buffer("output", self.seq_len * self.embedding_dim)
        self.add_kernel(
            "swiglu_gemm_1", combined_xclbin, gemm_1_xclbin.kernel_name, gemm_1_insts
        )
        self.add_kernel(
            "swiglu_silu", combined_xclbin, silu_xclbin.kernel_name, silu_insts
        )
        self.add_kernel(
            "swiglu_eltwise_mul",
            combined_xclbin,
            eltwise_mul_xclbin.kernel_name,
            eltwise_mul_insts,
        )
        self.add_kernel(
            "swiglu_gemm_2", combined_xclbin, gemm_2_xclbin.kernel_name, gemm_2_insts
        )
        self.add_to_runlist("swiglu_gemm_1", "input", "weights_1", "left")
        self.add_to_runlist("swiglu_gemm_1", "input", "weights_2", "right")
        self.add_to_runlist("swiglu_silu", "left", "left_swished")
        self.add_to_runlist(
            "swiglu_eltwise_mul", "left_swished", "right", "intermediate"
        )
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
        x_np = torch_to_numpy(x_flat)

        self.write_buffer("input", x_np)
        test_pattern = np.zeros(len(x_np), dtype=bfloat16)
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=x_np.shape, dtype=bfloat16)

        return result
