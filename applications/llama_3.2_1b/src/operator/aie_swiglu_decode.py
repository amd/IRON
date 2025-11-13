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
from .aie_gemv import get_gemv_artifacts
from .aie_silu import get_silu_artifacts
from .aie_elementwise_mul import get_elementwise_mul_artifacts


class AIESwiGLUDecode(AIEOperatorBase):

    def __init__(self, embedding_dim, hidden_dim):
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
        gemv_config = {
            "num_columns": 1,
            "tile_size": 1
        }

        gemv_1_xclbin, gemv_1_insts = get_gemv_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.hidden_dim,
            self.embedding_dim,
            prefix="swiglu_decode_gemv_1_",
            **gemv_config
        )
        gemv_1_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemv_1",
            "--xclbin-kernel-id=0x901",
        ]
        gemv_1_xclbin.kernel_name = "swiglu_gemv_1"
        artifacts.append(
            gemv_1_insts
        )  # xclbin artifact will be pulled in as a dependency of last xclbin

        silu_xclbin, silu_insts = get_silu_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.hidden_dim,
            num_columns=4,
            prefix="swiglu_decode_silu_",
        )
        silu_xclbin.xclbin_input = gemv_1_xclbin
        silu_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_silu",
            "--xclbin-kernel-id=0x902",
        ]
        silu_xclbin.kernel_name = "swiglu_silu"
        silu_xclbin.depends += [gemv_1_xclbin]
        artifacts.append(silu_insts)

        eltwise_mul_xclbin, eltwise_mul_insts = get_elementwise_mul_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.hidden_dim,
            prefix="swiglu_decode_eltwise_mul_",
        )
        eltwise_mul_xclbin.xclbin_input = silu_xclbin
        eltwise_mul_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_eltwise_mul",
            "--xclbin-kernel-id=0x903",
        ]
        eltwise_mul_xclbin.kernel_name = "swiglu_eltwise_mul"
        eltwise_mul_xclbin.depends += [silu_xclbin]
        artifacts.append(eltwise_mul_insts)

        gemv_2_xclbin, gemv_2_insts = get_gemv_artifacts(
            self.base_dir,
            self.device_manager.device_type,
            self.embedding_dim,
            self.hidden_dim,
            prefix="swiglu_decode_gemv_2_",
            **gemv_config
        )
        gemv_2_xclbin.xclbin_input = eltwise_mul_xclbin
        gemv_2_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemv_2",
            "--xclbin-kernel-id=0x904",
        ]
        gemv_2_xclbin.kernel_name = "swiglu_gemv_2"
        gemv_2_xclbin.depends += [eltwise_mul_xclbin]
        artifacts.append(gemv_2_xclbin)
        artifacts.append(gemv_2_insts)

        self.add_artifacts(artifacts)

        # Runtime setup
        # ---
        combined_xclbin = gemv_2_xclbin
        self.add_buffer("input", self.embedding_dim)
        self.add_buffer(
            "weights_1",
            self.embedding_dim * self.hidden_dim,
            static_data=torch_to_numpy(self.weights_1),
        )
        self.add_buffer(
            "weights_2",
            self.embedding_dim * self.hidden_dim,
            static_data=torch_to_numpy(self.weights_2),
        )
        self.add_buffer(
            "weights_3",
            self.hidden_dim * self.embedding_dim,
            static_data=torch_to_numpy(self.weights_3),
        )
        self.add_buffer("left", self.hidden_dim)
        self.add_buffer("left_swished", self.hidden_dim)
        self.add_buffer("right", self.hidden_dim)
        self.add_buffer("intermediate", self.hidden_dim)
        self.add_buffer("output", self.embedding_dim)
        self.add_kernel(
            "swiglu_gemv_1", combined_xclbin, gemv_1_xclbin.kernel_name, gemv_1_insts
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
            "swiglu_gemv_2", combined_xclbin, gemv_2_xclbin.kernel_name, gemv_2_insts
        )
        self.add_to_runlist("swiglu_gemv_1", "weights_1", "input", "left")
        self.add_to_runlist("swiglu_gemv_1", "weights_2", "input", "right")
        self.add_to_runlist("swiglu_silu", "left", "left_swished")
        self.add_to_runlist(
            "swiglu_eltwise_mul", "left_swished", "right", "intermediate"
        )
        self.add_to_runlist("swiglu_gemv_2", "weights_3", "intermediate", "output")

    def forward(self, x):
        # Turn into a numpy vector and drop the batch and other higher dimensions, if any; will error if batch or other higher dimensions > 1
        x_np = torch_to_numpy(x.reshape(x.shape[-1]))

        assert x_np.shape[0] == self.embedding_dim

        self.write_buffer("input", x_np)
        self.run_runlist()
        result = self.read_buffer_as_torch(
            "output",
            (self.embedding_dim, ),
        ).view_as(x)

        return result
