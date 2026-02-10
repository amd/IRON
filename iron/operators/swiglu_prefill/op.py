# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import torch
import numpy as np
from ml_dtypes import bfloat16

from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
from aie.utils.npukernel import NPUKernel
from iron.common import (
    CompositeOperator,
    AIERuntimeArgSpec,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from iron.operators.gemm.op import AIEGEMM
from iron.operators.silu.op import AIESiLU
from iron.operators.elementwise_mul.op import AIEElementwiseMul


class SwiGLUPrefillCallable:
    def __init__(self, op):
        self.op = op

        def create_callable(sub_op, xclbin_path, kernel_name, insts_artifact):
            return NPUKernel(
                xclbin_path=xclbin_path,
                kernel_name=kernel_name,
                insts_path=insts_artifact.filename,
            )

        self.gemm_1_callable = create_callable(
            op.gemm_1,
            op.combined_xclbin.filename,
            op.gemm_1_xclbin.kernel_name,
            op.gemm_1_insts,
        )
        self.silu_callable = create_callable(
            op.silu,
            op.combined_xclbin.filename,
            op.silu_xclbin.kernel_name,
            op.silu_insts,
        )
        self.eltwise_mul_callable = create_callable(
            op.eltwise_mul,
            op.combined_xclbin.filename,
            op.eltwise_mul_xclbin.kernel_name,
            op.eltwise_mul_insts,
        )
        self.gemm_2_callable = create_callable(
            op.gemm_2,
            op.combined_xclbin.filename,
            op.gemm_2_xclbin.kernel_name,
            op.gemm_2_insts,
        )

        # Allocate and upload weights
        self.weights_1 = XRTTensor.from_torch(op.weights_1.T)
        self.weights_2 = XRTTensor.from_torch(op.weights_2.T)
        self.weights_3 = XRTTensor.from_torch(op.weights_3.T)

        # Allocate intermediate buffers
        # Sizes are padded
        size_hidden = op.seq_len_padded * op.hidden_dim_padded
        self.left = XRTTensor((size_hidden,), dtype=bfloat16)
        self.right = XRTTensor((size_hidden,), dtype=bfloat16)
        self.left_swished = XRTTensor((size_hidden,), dtype=bfloat16)
        self.intermediate = XRTTensor((size_hidden,), dtype=bfloat16)
        self.last_output_buf = None

    def __call__(self, input_buf, output_buf):
        self.last_output_buf = output_buf
        input_buf.to("npu")
        output_buf.to("npu")
        self.weights_1.to("npu")
        self.weights_2.to("npu")
        self.weights_3.to("npu")
        self.left.to("npu")
        self.right.to("npu")
        self.left_swished.to("npu")
        self.intermediate.to("npu")

        # Sequence:
        # 1. GEMM(input, weights_1, left)
        self.gemm_1_callable(input_buf, self.weights_1, self.left)

        # 2. GEMM(input, weights_2, right)
        self.gemm_1_callable(input_buf, self.weights_2, self.right)

        # 3. SiLU(left, left_swished)
        self.silu_callable(self.left, self.left_swished)

        # 4. EltwiseMul(left_swished, right, intermediate)
        self.eltwise_mul_callable(self.left_swished, self.right, self.intermediate)

        # 5. GEMM(intermediate, weights_3, output)
        self.gemm_2_callable(self.intermediate, self.weights_3, output_buf)


class AIESwiGLUPrefill(CompositeOperator):

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
        self.silu_xclbin = None
        self.silu_insts = None
        self.eltwise_mul_xclbin = None
        self.eltwise_mul_insts = None
        self.gemm_2_xclbin = None
        self.gemm_2_insts = None

        super().__init__(context=context)

    def set_up_artifacts(self):
        # Artifact setup
        # ---
        # Note: All operators (GEMM, SiLU, ElementwiseMul) apply their own padding
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

        silu = AIESiLU(
            size=self.seq_len_padded * self.hidden_dim_padded,
            num_aie_columns=8,
            tile_size=self.hidden_dim_padded // 8,
        )
        self.silu = silu
        assert silu.size == self.seq_len_padded * self.hidden_dim_padded

        silu_xclbin, silu_insts = silu.get_artifacts(prefix="swiglu_silu_")
        silu_xclbin.xclbin_input = gemm_1_xclbin
        silu_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_silu",
            "--xclbin-kernel-id=0x902",
        ]
        silu_xclbin.kernel_name = "swiglu_silu"
        silu_xclbin.dependencies.add(gemm_1_xclbin)
        artifacts.append(silu_insts)

        eltwise_mul = AIEElementwiseMul(
            size=self.seq_len_padded * self.hidden_dim_padded,
            num_aie_columns=8,
            tile_size=self.hidden_dim_padded // 8,
        )
        self.eltwise_mul = eltwise_mul
        assert eltwise_mul.size == self.seq_len_padded * self.hidden_dim_padded

        eltwise_mul_xclbin, eltwise_mul_insts = eltwise_mul.get_artifacts(
            prefix="swiglu_eltwise_mul_"
        )
        eltwise_mul_xclbin.xclbin_input = silu_xclbin
        eltwise_mul_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_eltwise_mul",
            "--xclbin-kernel-id=0x903",
        ]
        eltwise_mul_xclbin.kernel_name = "swiglu_eltwise_mul"
        eltwise_mul_xclbin.dependencies.add(silu_xclbin)
        artifacts.append(eltwise_mul_insts)

        gemm_2 = AIEGEMM(
            M=self.seq_len, K=self.hidden_dim, N=self.embedding_dim, **accuracy_flags
        )
        self.gemm_2 = gemm_2
        assert gemm_2.M == self.seq_len_padded
        assert gemm_2.K == self.hidden_dim_padded
        assert gemm_2.N == self.embedding_dim_padded

        gemm_2_xclbin, gemm_2_insts = gemm_2.get_artifacts(prefix="swiglu_gemm_2_")
        gemm_2_xclbin.xclbin_input = eltwise_mul_xclbin
        gemm_2_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemm_2",
            "--xclbin-kernel-id=0x904",
        ]
        gemm_2_xclbin.kernel_name = "swiglu_gemm_2"
        gemm_2_xclbin.dependencies.add(eltwise_mul_xclbin)
        artifacts.append(gemm_2_xclbin)
        artifacts.append(gemm_2_insts)

        self.combined_xclbin = gemm_2_xclbin
        self.gemm_1_xclbin = gemm_1_xclbin
        self.gemm_1_insts = gemm_1_insts
        self.silu_xclbin = silu_xclbin
        self.silu_insts = silu_insts
        self.eltwise_mul_xclbin = eltwise_mul_xclbin
        self.eltwise_mul_insts = eltwise_mul_insts
        self.gemm_2_xclbin = gemm_2_xclbin
        self.gemm_2_insts = gemm_2_insts

        self.add_artifacts(artifacts)

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.seq_len_padded * self.embedding_dim_padded,)),
            AIERuntimeArgSpec(
                "out", (self.seq_len_padded * self.embedding_dim_padded,)
            ),
        ]

    def get_callable(self):
        return SwiGLUPrefillCallable(self)
