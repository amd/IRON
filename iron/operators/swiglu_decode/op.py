# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import torch
import numpy as np
from ml_dtypes import bfloat16

from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor
from iron.common import (
    CompositeOperator,
    AIERuntimeArgSpec,
    SingleXclbinCallable,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from iron.operators.gemv.op import AIEGEMV
from iron.operators.silu.op import AIESiLU
from iron.operators.elementwise_mul.op import AIEElementwiseMul
from iron.common.utils import torch_to_numpy


class SwiGLUDecodeCallable:
    def __init__(self, op):
        self.op = op
        # Create callables for sub-operators
        # We need to manually construct SingleXclbinCallable because sub-operators weren't "compiled" in the standard way

        # Helper to create callable from operator and artifacts
        def create_callable(sub_op, xclbin_path, kernel_name, insts_artifact):
            return SingleXclbinCallable(
                xclbin_path=xclbin_path,
                kernel_name=kernel_name,
                insts_bin_path=insts_artifact.filename,
                args_spec=sub_op.get_arg_spec(),
            )

        self.gemv_1_callable = create_callable(
            op.gemv_1,
            op.combined_xclbin.filename,
            op.gemv_1_xclbin.kernel_name,
            op.gemv_1_insts,
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
        self.gemv_2_callable = create_callable(
            op.gemv_2,
            op.combined_xclbin.filename,
            op.gemv_2_xclbin.kernel_name,
            op.gemv_2_insts,
        )

        # Allocate and upload weights
        w1 = torch_to_numpy(op.weights_1)
        self.weights_1 = XRTTensor(w1, dtype=w1.dtype)
        w2 = torch_to_numpy(op.weights_2)
        self.weights_2 = XRTTensor(w2, dtype=w2.dtype)
        w3 = torch_to_numpy(op.weights_3)
        self.weights_3 = XRTTensor(w3, dtype=w3.dtype)

        # Allocate intermediate buffers
        # left: output of gemv_1 (hidden_dim_padded)
        self.left = XRTTensor((op.hidden_dim_padded,), dtype=bfloat16)
        # right: output of gemv_1 (hidden_dim_padded)
        self.right = XRTTensor((op.hidden_dim_padded,), dtype=bfloat16)
        # left_swished: output of silu (hidden_dim_padded)
        self.left_swished = XRTTensor((op.hidden_dim_padded,), dtype=bfloat16)
        # intermediate: output of eltwise_mul (hidden_dim_padded)
        self.intermediate = XRTTensor((op.hidden_dim_padded,), dtype=bfloat16)

    def __call__(self, input_buf, output_buf):
        # Ensure inputs are on device
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
        # 1. GEMV(weights_1, input, left)
        self.gemv_1_callable(self.weights_1, input_buf, self.left)

        # 2. GEMV(weights_2, input, right)
        self.gemv_1_callable(self.weights_2, input_buf, self.right)

        # 3. SiLU(left, left_swished)
        self.silu_callable(self.left, self.left_swished)

        # 4. EltwiseMul(left_swished, right, intermediate)
        self.eltwise_mul_callable(self.left_swished, self.right, self.intermediate)

        # 5. GEMV(weights_3, intermediate, output)
        self.gemv_2_callable(self.weights_3, self.intermediate, output_buf)


class AIESwiGLUDecode(CompositeOperator):

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
        gemv_1_xclbin, gemv_1_insts = gemv_1.get_artifacts(prefix="swiglu_gemv_1_")
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
            tile_size=self.hidden_dim // 16,
        )
        self.silu = silu
        self.hidden_dim_padded = silu.size
        silu_xclbin, silu_insts = silu.get_artifacts(prefix="swiglu_silu_")
        silu_xclbin.xclbin_input = gemv_1_xclbin
        silu_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_silu",
            "--xclbin-kernel-id=0x902",
        ]
        silu_xclbin.kernel_name = "swiglu_silu"
        silu_xclbin.dependencies.add(gemv_1_xclbin)
        artifacts.append(silu_insts)

        eltwise_mul = AIEElementwiseMul(
            size=self.hidden_dim,
            num_aie_columns=8,
            tile_size=self.hidden_dim // 8,
        )
        self.eltwise_mul = eltwise_mul
        assert self.hidden_dim <= eltwise_mul.size <= self.hidden_dim_padded
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

        gemv_2 = AIEGEMV(
            M=self.embedding_dim,
            K=self.hidden_dim,
            num_aie_columns=8,
            tile_size_input=1,
            tile_size_output=self.embedding_dim // 8,
        )
        self.gemv_2 = gemv_2
        gemv_2_xclbin, gemv_2_insts = gemv_2.get_artifacts(prefix="swiglu_gemv_2_")
        gemv_2_xclbin.xclbin_input = eltwise_mul_xclbin
        gemv_2_xclbin.extra_flags += [
            "--xclbin-instance-name=swiglu_gemv_2",
            "--xclbin-kernel-id=0x904",
        ]
        gemv_2_xclbin.kernel_name = "swiglu_gemv_2"
        gemv_2_xclbin.dependencies.add(eltwise_mul_xclbin)
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

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.embedding_dim,)),
            AIERuntimeArgSpec("out", (self.embedding_dim,)),
        ]

    def get_callable(self):
        return SwiGLUDecodeCallable(self)
