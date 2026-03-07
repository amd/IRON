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
from iron.operators.dual_gemv_silu_mul.op import AIEDualGEMVSiLUMul, interleave_weights
from iron.operators.gemv.op import AIEGEMV
from iron.common.utils import torch_to_numpy


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
        self.fused_xclbin = None
        self.fused_insts = None
        self.gemv_2_xclbin = None
        self.gemv_2_insts = None

        super().__init__(context=context)

    def set_up_artifacts(self):
        artifacts = []
        device_str = self.context.device_manager.device_str()

        fused = AIEDualGEMVSiLUMul(
            M=self.hidden_dim,
            K=self.embedding_dim,
            num_aie_columns=4,
            tile_size_input=4,
            tile_size_output=self.hidden_dim // 4,
        )
        self.fused = fused
        self.hidden_dim_padded = self.hidden_dim
        fused_xclbin, fused_insts = fused.get_artifacts(prefix="swiglu_decode_fused_")
        fused_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_fused",
            "--xclbin-kernel-id=0x901",
        ]
        fused_xclbin.kernel_name = "swiglu_fused"
        artifacts.append(fused_insts)

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
        gemv_2_xclbin.xclbin_input = fused_xclbin
        gemv_2_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemv_2",
            "--xclbin-kernel-id=0x902",
        ]
        gemv_2_xclbin.kernel_name = "swiglu_gemv_2"
        gemv_2_xclbin.depends += [fused_xclbin]
        artifacts.append(gemv_2_xclbin)
        artifacts.append(gemv_2_insts)

        self.combined_xclbin = gemv_2_xclbin
        self.fused_xclbin = fused_xclbin
        self.fused_insts = fused_insts
        self.gemv_2_xclbin = gemv_2_xclbin
        self.gemv_2_insts = gemv_2_insts

        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        self.add_buffer("input", self.embedding_dim)
        # Pre-interleave W1 and W2 for the fused dual-GEMV design
        rows_per_col = self.hidden_dim // self.fused.num_aie_columns
        w_interleaved = interleave_weights(
            self.weights_1, self.weights_2, rows_per_col, self.fused.num_aie_columns
        )
        self.add_buffer(
            "weights_gate_up",
            2 * self.embedding_dim * self.hidden_dim_padded,
            static_data=torch_to_numpy(w_interleaved),
        )
        self.add_buffer(
            "weights_3",
            self.hidden_dim_padded * self.embedding_dim,
            static_data=torch_to_numpy(self.weights_3),
        )
        self.add_buffer("intermediate", self.hidden_dim_padded)
        self.add_buffer("output", self.embedding_dim)
        self.add_kernel(
            "swiglu_fused",
            self.combined_xclbin,
            self.fused_xclbin.kernel_name,
            self.fused_insts,
        )
        self.add_kernel(
            "swiglu_gemv_2",
            self.combined_xclbin,
            self.gemv_2_xclbin.kernel_name,
            self.gemv_2_insts,
        )
        self.add_to_runlist("swiglu_fused", "weights_gate_up", "input", "intermediate")
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
