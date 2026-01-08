# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import torch
import numpy as np
from ml_dtypes import bfloat16

from operators.common import (
    AIEOperatorBase,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from operators.gemv.op import AIEGEMV
from operators.silu.op import AIESiLU
from operators.elementwise_mul.op import AIEElementwiseMul
from operators.common.utils import torch_to_numpy


class AIESwiGLUDecode(AIEOperatorBase):

    def __init__(self, embedding_dim, hidden_dim, prio_accuracy=False, context=None):
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        self.prio_accuracy = prio_accuracy
        # weights to be set by user (e.g., assign_weights in FeedForward block)
        self.weights_1 = None
        self.weights_2 = None
        self.weights_3 = None

        # Artifacts created by set_up_artifacts()
        self.combined_xclbin = None
        self.gemv_1_xclbin = None
        self.gemv_1_insts = None
        self.silu_xclbin = None
        self.silu_insts = None
        self.eltwise_mul_xclbin = None
        self.eltwise_mul_insts = None
        self.gemv_2_xclbin = None
        self.gemv_2_insts = None

        super().__init__(context=context)

    def set_up_artifacts(self):
        artifacts = []
        device_str = self.context.device_manager.device_str()

        gemv_1 = AIEGEMV(
            M=self.hidden_dim,
            K=self.embedding_dim,
            num_aie_columns=8,
            tile_size_input=4,
            tile_size_output=self.hidden_dim // 8,
        )
        self.gemv_1 = gemv_1
        gemv_1_xclbin, gemv_1_insts = gemv_1.get_artifacts(
            prefix="swiglu_decode_gemv_1_"
        )
        gemv_1_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemv_1",
            "--xclbin-kernel-id=0x901",
        ]
        gemv_1_xclbin.kernel_name = "swiglu_gemv_1"
        artifacts.append(
            gemv_1_insts
        )  # xclbin artifact will be pulled in as a dependency of last xclbin

        silu = AIESiLU(
            size=self.hidden_dim,
            num_aie_columns=8,
            num_channels=2,
            tile_size=self.hidden_dim // 16,
        )
        self.silu = silu
        self.hidden_dim_padded = silu.size
        silu_xclbin, silu_insts = silu.get_artifacts(prefix="swiglu_decode_silu_")
        silu_xclbin.xclbin_input = gemv_1_xclbin
        silu_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_silu",
            "--xclbin-kernel-id=0x902",
        ]
        silu_xclbin.kernel_name = "swiglu_silu"
        silu_xclbin.depends += [gemv_1_xclbin]
        artifacts.append(silu_insts)

        eltwise_mul = AIEElementwiseMul(
            size=self.hidden_dim,
            num_aie_columns=8,
            num_channels=2,
            tile_size=self.hidden_dim // 8,
        )
        self.eltwise_mul = eltwise_mul
        assert self.hidden_dim <= eltwise_mul.size <= self.hidden_dim_padded
        eltwise_mul_xclbin, eltwise_mul_insts = eltwise_mul.get_artifacts(
            prefix="swiglu_decode_eltwise_mul_"
        )
        eltwise_mul_xclbin.xclbin_input = silu_xclbin
        eltwise_mul_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_eltwise_mul",
            "--xclbin-kernel-id=0x903",
        ]
        eltwise_mul_xclbin.kernel_name = "swiglu_eltwise_mul"
        eltwise_mul_xclbin.depends += [silu_xclbin]
        artifacts.append(eltwise_mul_insts)

        gemv_2 = AIEGEMV(
            M=self.embedding_dim,
            K=self.hidden_dim,
            num_aie_columns=8,
            tile_size_input=1,
            tile_size_output=self.embedding_dim // 8,
        )
        self.gemv_2 = gemv_2
        gemv_2_xclbin, gemv_2_insts = gemv_2.get_artifacts(
            prefix="swiglu_decode_gemv_2_"
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

        self.combined_xclbin = gemv_2_xclbin
        self.gemv_1_xclbin = gemv_1_xclbin
        self.gemv_1_insts = gemv_1_insts
        self.silu_xclbin = silu_xclbin
        self.silu_insts = silu_insts
        self.eltwise_mul_xclbin = eltwise_mul_xclbin
        self.eltwise_mul_insts = eltwise_mul_insts
        self.gemv_2_xclbin = gemv_2_xclbin
        self.gemv_2_insts = gemv_2_insts

        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        self.add_buffer("input", self.embedding_dim)
        self.add_buffer(
            "weights_1",
            self.embedding_dim * self.hidden_dim_padded,
            static_data=torch_to_numpy(self.weights_1),
        )
        self.add_buffer(
            "weights_2",
            self.embedding_dim * self.hidden_dim_padded,
            static_data=torch_to_numpy(self.weights_2),
        )
        self.add_buffer(
            "weights_3",
            self.hidden_dim_padded * self.embedding_dim,
            static_data=torch_to_numpy(self.weights_3),
        )
        self.add_buffer("left", self.hidden_dim_padded)
        self.add_buffer("left_swished", self.hidden_dim_padded)
        self.add_buffer("right", self.hidden_dim_padded)
        self.add_buffer("intermediate", self.hidden_dim_padded)
        self.add_buffer("output", self.embedding_dim)
        self.add_kernel(
            "swiglu_gemv_1",
            self.combined_xclbin,
            self.gemv_1_xclbin.kernel_name,
            self.gemv_1_insts,
        )
        self.add_kernel(
            "swiglu_silu",
            self.combined_xclbin,
            self.silu_xclbin.kernel_name,
            self.silu_insts,
        )
        self.add_kernel(
            "swiglu_eltwise_mul",
            self.combined_xclbin,
            self.eltwise_mul_xclbin.kernel_name,
            self.eltwise_mul_insts,
        )
        self.add_kernel(
            "swiglu_gemv_2",
            self.combined_xclbin,
            self.gemv_2_xclbin.kernel_name,
            self.gemv_2_insts,
        )
        self.add_to_runlist("swiglu_gemv_1", "weights_1", "input", "left")
        self.add_to_runlist("swiglu_gemv_1", "weights_2", "input", "right")
        self.add_to_runlist("swiglu_silu", "left", "left_swished")
        self.add_to_runlist(
            "swiglu_eltwise_mul", "left_swished", "right", "intermediate"
        )
        self.add_to_runlist("swiglu_gemv_2", "weights_3", "intermediate", "output")

    def forward(self, x):
        x_flat = x.reshape(x.shape[-1])
        assert x_flat.shape[0] == self.embedding_dim

        self.write_buffer("input", x_flat)
        self.run_runlist()
        result = self.read_buffer_as_torch(
            "output",
            (self.embedding_dim,),
        ).view_as(x)

        return result
