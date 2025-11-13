# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn as nn
from ..utils import torch_to_numpy, assign
from src.operator.aie_elementwise_mul import AIEElementwiseMul
from src.operator.aie_gemm import AIEGEMM
from src.operator.aie_gemv import AIEGEMV
from src.operator.aie_silu import AIESiLU


class FeedForward(nn.Module):
    def __init__(
        self,
        cfg,
        prompt_length=0,
        num_tokens=1,
    ):
        super().__init__()
        self.cfg = cfg.copy()

        assert cfg["use_aie_ffn_swiglu"] != (
            cfg["use_aie_ffn_silu"] or cfg["use_aie_ffn_gemm"] or cfg["use_aie_ffn_mul"]
        ), "Cannot mix fused SwiGLU with individual AIE operators."

        self.emb_dim = cfg["emb_dim"]
        self.hidden_dim = cfg["hidden_dim"]

        # Initialize SiLU activation
        if self.cfg["use_aie_ffn_silu"]:
            self.silu = AIESiLU(
                size=cfg["hidden_dim"], num_columns=4, num_channels=2, tile_size=1024
            )
        else:
            self.silu = nn.SiLU()

        self.emb_dim = cfg["emb_dim"]
        self.hidden_dim = cfg["hidden_dim"]

        # Initialize FFN up and down projections
        if self.cfg["use_aie_ffn_gemm"]:
            if self.cfg["use_kv_cache"]:
                M_prefill = prompt_length
            else:
                M_prefill = prompt_length + num_tokens

            aie_config_prefill = {
                "num_columns": 8,
                "tile_m": 64,
                "tile_k": 64,
                "tile_n": 64,
                "use_static_weight": True,
            }

            self.fc1 = AIEGEMM(
                M=M_prefill, K=self.emb_dim, N=self.hidden_dim, **aie_config_prefill
            )
            self.fc2 = AIEGEMM(
                M=M_prefill, K=self.emb_dim, N=self.hidden_dim, **aie_config_prefill
            )
            self.fc3 = AIEGEMM(
                M=M_prefill, K=self.hidden_dim, N=self.emb_dim, **aie_config_prefill
            )

        if self.cfg["use_kv_cache"] and self.cfg["use_aie_gemv"]:
            aie_gemv_config = {"num_columns": 1, "is_mv": False}
            # FC1 and FC2: emb_dim -> hidden_dim
            self.aie_fc1_gemv = AIEGEMV(
                M=self.hidden_dim, K=self.emb_dim, **aie_gemv_config
            )
            self.aie_fc2_gemv = AIEGEMV(
                M=self.hidden_dim, K=self.emb_dim, **aie_gemv_config
            )
            # FC3: hidden_dim -> emb_dim
            self.aie_fc3_gemv = AIEGEMV(
                M=self.emb_dim, K=self.hidden_dim, **aie_gemv_config
            )

        # Initialize AIE elementwise multiply
        if self.cfg["use_aie_ffn_mul"]:
            self.aie_mul = AIEElementwiseMul(
                size=self.hidden_dim,
                num_columns=4,
                num_channels=2,
                tile_size=1024,
            )

    def forward(self, x):
        original_shape = x.shape

        # Check if input is a vector (decode phase) or matrix (prefill phase)
        # Handle 1D: (emb_dim,), 2D: (1, emb_dim), or 3D: (1, 1, emb_dim)
        is_vector = (
            len(x.shape) == 1
            or (len(x.shape) == 2 and x.shape[0] == 1)
            or (len(x.shape) == 3 and x.shape[0] == 1 and x.shape[1] == 1)
        )

        is_decode_with_kv = is_vector and self.cfg["use_kv_cache"]
        is_prefill = not is_vector or not self.cfg["use_kv_cache"]

        if is_vector and self.cfg["use_kv_cache"] and self.cfg["use_aie_gemv"]:
            x_fc1 = self.aie_fc1_gemv(None, x)
            x_fc2 = self.aie_fc2_gemv(None, x)
        else:
            x_fc1 = self.fc1(x)
            x_fc2 = self.fc2(x)

        x_fc1_silu = self.silu(x_fc1)

        if self.cfg["use_aie_ffn_mul"]:
            x = self.aie_mul(x_fc1_silu, x_fc2)
        else:
            x = x_fc1_silu * x_fc2

        if is_vector and self.cfg["use_kv_cache"] and self.cfg["use_aie_gemv"]:
            result = self.aie_fc3_gemv(None, x)
            return result.view(original_shape)
        else:
            return self.fc3(x).view(original_shape)

    def assign_weights(self, l, fc1, fc2, fc3):
        self.fc1.weight = assign(
            self.fc1.weight,
            fc1,
            f"model.layers.{l}.mlp.gate_proj.weight",
        )
        self.fc2.weight = assign(
            self.fc2.weight,
            fc2,
            f"model.layers.{l}.mlp.up_proj.weight",
        )
        self.fc3.weight = assign(
            self.fc3.weight,
            fc3,
            f"model.layers.{l}.mlp.down_proj.weight",
        )

        if self.cfg["use_kv_cache"] and self.cfg["use_aie_gemv"]:
            self.aie_fc1_gemv.weight = fc1
            self.aie_fc2_gemv.weight = fc2
            self.aie_fc3_gemv.weight = fc3
