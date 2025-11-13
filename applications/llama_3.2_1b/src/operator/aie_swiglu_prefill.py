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

        seq_len_chunk_size = self.get_seq_len_chunk_size()

        gemm_1_xclbin, gemm_1_insts = get_gemm_artifacts(
            self.base_dir,
            device_str,
            seq_len_chunk_size,
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
            seq_len_chunk_size * self.hidden_dim,
            num_columns=4,
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
            seq_len_chunk_size * self.hidden_dim,
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
            seq_len_chunk_size,
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
        self.add_buffer("input", seq_len_chunk_size * self.embedding_dim)
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
        self.add_buffer("left", seq_len_chunk_size * self.hidden_dim)
        self.add_buffer("left_swished", seq_len_chunk_size * self.hidden_dim)
        self.add_buffer("right", seq_len_chunk_size * self.hidden_dim)
        self.add_buffer("intermediate", seq_len_chunk_size * self.hidden_dim)
        self.add_buffer("output", seq_len_chunk_size * self.embedding_dim)
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

    def get_seq_len_chunk_size(self):
        min_multiple = 256
        return (self.seq_len + min_multiple - 1) // min_multiple * min_multiple

    def forward(self, x):
        # Turn into a 2D numpy array and drop the batch and other higher dimensions, if any; will error if batch or other higher dimensions > 1
        x_np = torch_to_numpy(x.reshape(*x.shape[-2:]))

        seq_len = x_np.shape[0]
        seq_len_chunk_size = self.get_seq_len_chunk_size()

        output_parts = []
        for i in range(0, seq_len, seq_len_chunk_size):
            chunk_end = min(i + seq_len_chunk_size, x_np.shape[0])
            x_chunk = x_np[i:chunk_end]

            # Since the sequence is a concatenation of rows, we don't need to pad the input;
            # if this chunk is smaller than the chunksize, it is fine to just leave the last rows uninitialized, saving some writes
            self.write_buffer("input", x_chunk)
            self.run_runlist()
            output_chunk = self.read_buffer(
                "output",
                (
                    seq_len_chunk_size,
                    self.embedding_dim,
                ),
            )

            # Drop padding, if any (match output to input dimensions)
            output_parts.append(output_chunk[: x_chunk.shape[0]])

        output_np = np.concatenate(output_parts, axis=0)
        output_torch = numpy_to_torch(output_np).view_as(x)
        return output_torch
