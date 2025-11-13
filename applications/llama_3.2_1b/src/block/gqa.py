# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import torch
import torch.nn as nn

from src.operator.rope import apply_rope
from src.operator.aie_rope import AIERope
from src.operator.aie_softmax import AIESoftmax
from src.operator.aie_mha import AIEMHA
from src.operator.aie_gemm import AIEGEMM
from src.operator.aie_gemv import AIEGEMV

from torchtune.modules import KVCache

from ..utils import assign


class GroupedQueryAttention(nn.Module):
    def __init__(
        self,
        d_in,
        d_out,
        num_heads,
        num_kv_groups,
        prompt_length=0,
        num_tokens=1,
        dtype=None,
        max_batch_size=1,
        max_seq_len=8192,
        cfg=None,
    ):
        super().__init__()
        assert d_out % num_heads == 0, "d_out must be divisible by num_heads"
        assert (
            num_heads % num_kv_groups == 0
        ), "num_heads must be divisible by num_kv_groups"

        self.cfg = cfg.copy() if cfg is not None else {}

        self.d_out = d_out
        self.num_heads = num_heads
        self.head_dim = d_out // num_heads

        self.num_tokens = num_tokens

        # Weights for Attention layer
        self.W_key = nn.Linear(
            d_in, num_kv_groups * self.head_dim, bias=False, dtype=dtype
        )
        self.W_value = nn.Linear(
            d_in, num_kv_groups * self.head_dim, bias=False, dtype=dtype
        )
        self.W_query = nn.Linear(d_in, d_out, bias=False, dtype=dtype)
        self.out_proj = nn.Linear(d_out, d_out, bias=False, dtype=dtype)

        self.num_kv_groups = num_kv_groups
        self.group_size = num_heads // num_kv_groups

        self.prompt_length = prompt_length

        aie_gemm_config = {
            "num_columns": 8,
            "tile_m": 64,
            "tile_k": 64,
            "tile_n": 64,
        }

        # Initialize KV Cache
        if self.cfg["use_kv_cache"]:
            self.kv_cache = KVCache(
                batch_size=max_batch_size,
                max_seq_len=max_seq_len,
                num_kv_heads=self.num_kv_groups,
                head_dim=self.head_dim,
                dtype=torch.bfloat16,
            )

        # Initialize AIE Regular MHA operator
        if self.cfg["use_aie_regular_mha"]:
            self.aie_softmax = AIESoftmax(
                num_columns=1,
                num_channels=1,
                size=prompt_length * prompt_length,
                last_dim=prompt_length,
            )
            M_for_gemm = prompt_length + num_tokens
            self.aie_mha_gemm_qk = AIEGEMM(
                M=M_for_gemm, K=self.head_dim, N=M_for_gemm, **aie_gemm_config
            )
            self.aie_mha_gemm_pv = AIEGEMM(
                M=M_for_gemm, K=M_for_gemm, N=self.head_dim, **aie_gemm_config
            )

        # Initialize AIE RoPE operator
        if self.cfg["use_aie_rope"]:
            self.aie_rope = AIERope(
                num_columns=1,
                num_channels=1,
                size=self.prompt_length * self.head_dim,
                last_dim=self.head_dim,
            )

        # Initialize fused AIE MHA operator
        if self.cfg["use_aie_fused_mha"]:
            self.aie_mha = AIEMHA(
                num_heads=num_heads,
                seq_len=prompt_length,
                d=self.head_dim,
                num_KV_heads=0,  # Regular MHA since we feed repeated K/V
                num_of_pipelines=8,
            )

        # Initialize AIE GEMV operators for decode phase (when using KV cache)
        if self.cfg["use_kv_cache"] and self.cfg["use_aie_gemv"]:

            aie_gemv_config = {
                "num_columns": 1,
                "is_mv": False,
                "use_static_weight": True,
            }
            self.aie_query_gemv = AIEGEMV(M=d_out, K=d_in, **aie_gemv_config)
            kv_out_dim = num_kv_groups * self.head_dim
            self.aie_key_gemv = AIEGEMV(M=kv_out_dim, K=d_in, **aie_gemv_config)
            self.aie_value_gemv = AIEGEMV(M=kv_out_dim, K=d_in, **aie_gemv_config)
            self.aie_out_proj_gemv = AIEGEMV(M=d_out, K=d_out, **aie_gemv_config)

        # Initialize AIE GEMM operators
        if self.cfg["use_aie_attn_projection_gemm"]:
            if self.cfg["use_kv_cache"]:
                M_for_gemm = self.prompt_length
            else:
                M_for_gemm = self.prompt_length + self.num_tokens

            # Query: (batch_size, d_in) @ (d_in, d_out) -> (batch_size, d_out)
            self.aie_query = AIEGEMM(M=M_for_gemm, K=d_in, N=d_out, **aie_gemm_config)
            # Key: (batch_size, d_in) @ (d_in, num_kv_groups * head_dim) -> (batch_size, num_kv_groups * head_dim)
            kv_out_dim = num_kv_groups * self.head_dim
            self.aie_key = AIEGEMM(
                M=M_for_gemm, K=d_in, N=kv_out_dim, **aie_gemm_config
            )
            # Value: same dimensions as key
            self.aie_value = AIEGEMM(
                M=M_for_gemm, K=d_in, N=kv_out_dim, **aie_gemm_config
            )
            # Output projection: (batch_size, d_out) @ (d_out, d_out) -> (batch_size, d_out)
            self.aie_out_proj = AIEGEMM(
                M=M_for_gemm, K=d_out, N=d_out, **aie_gemm_config
            )

    def forward(self, x, mask, angles, input_pos=None):
        b, num_tokens, d_in = x.shape
        is_prefill = input_pos is None
        is_decode = input_pos is not None

        # Choose between GEMM (prefill) and GEMV (decode) based on KV cache usage
        if self.cfg["use_kv_cache"] and is_decode and self.cfg["use_aie_gemv"]:
            # Decode phase with KV cache - use GEMV for single token
            # weight.T @ input, which is vector-matrix multiplication (So, is_mv=False)
            x_flat = x.reshape(1, -1)  # Shape: (1, d_in)
            input_dtype = x.dtype

            queries_flat = self.aie_query_gemv(x_flat)
            queries = queries_flat.reshape(b, num_tokens, self.d_out).to(input_dtype)

            keys_flat = self.aie_key_gemv(x_flat)
            keys = keys_flat.reshape(
                b, num_tokens, self.num_kv_groups * self.head_dim
            ).to(input_dtype)

            values_flat = self.aie_value_gemv(x_flat)
            values = values_flat.reshape(
                b, num_tokens, self.num_kv_groups * self.head_dim
            ).to(input_dtype)

        elif self.cfg["use_aie_attn_projection_gemm"]:
            # Prefill phase - use GEMM for multiple tokens
            x_flat = x.reshape(-1, d_in)
            input_dtype = x.dtype

            queries_flat = self.aie_query(x_flat, self.W_query.weight.T)
            queries = queries_flat.reshape(b, num_tokens, self.d_out).to(input_dtype)

            keys_flat = self.aie_key(x_flat, self.W_key.weight.T)
            keys = keys_flat.reshape(
                b, num_tokens, self.num_kv_groups * self.head_dim
            ).to(input_dtype)

            values_flat = self.aie_value(x_flat, self.W_value.weight.T)
            values = values_flat.reshape(
                b, num_tokens, self.num_kv_groups * self.head_dim
            ).to(input_dtype)
        else:
            queries = self.W_query(x)
            keys = self.W_key(x)
            values = self.W_value(x)

        keys = keys.view(b, num_tokens, self.num_kv_groups, self.head_dim)
        values = values.view(b, num_tokens, self.num_kv_groups, self.head_dim)
        queries = queries.view(b, num_tokens, self.num_heads, self.head_dim)

        # Determine angle slice based on KV cache usage and phase
        if self.cfg["use_kv_cache"] and is_decode:
            # Decode phase with KV cache: use single position
            current_pos = input_pos.item()
            angle_slice = angles[current_pos : current_pos + 1, :]
        else:
            # Prefill phase or no KV cache: use all tokens
            angle_slice = angles[:num_tokens, :]

        # Apply RoPE with AIE or CPU fallback
        def apply_rope_and_transpose(tensor, num_heads_dim, angle_slice):
            expected_seq_len = (
                1 if (self.cfg["use_kv_cache"] and is_decode) else self.prompt_length
            )
            can_use_aie = (
                self.cfg["use_aie_rope"]
                and tensor.shape[-1] == self.head_dim
                and tensor.shape[-2] == expected_seq_len
            )

            if can_use_aie:
                # AIE RoPE path: flatten -> apply -> reshape -> transpose
                tensor = self.aie_rope(tensor.view(b, num_tokens, -1), angle_slice)
                return tensor.view(
                    b, num_tokens, num_heads_dim, self.head_dim
                ).transpose(1, 2)
            else:
                # CPU RoPE path: transpose -> apply
                tensor = tensor.transpose(1, 2)
                return apply_rope(tensor, angle_slice)

        keys = apply_rope_and_transpose(keys, self.num_kv_groups, angle_slice)
        queries = apply_rope_and_transpose(queries, self.num_heads, angle_slice)
        values = values.transpose(1, 2)

        if self.cfg["use_kv_cache"]:
            if is_prefill:
                self.kv_cache.reset()
                self.kv_cache.update(keys, values)
                cached_keys, cached_values = keys, values
            else:
                self.kv_cache.update(keys, values)
                current_seq_len = input_pos.item() + 1
                cached_keys = self.kv_cache.k_cache[:, :, :current_seq_len, :]
                cached_values = self.kv_cache.v_cache[:, :, :current_seq_len, :]

            keys = cached_keys
            values = cached_values

        # Expand keys and values to match query heads for all cases (grouped query attention)
        keys = keys.repeat_interleave(self.group_size, dim=1)
        values = values.repeat_interleave(self.group_size, dim=1)

        # Use fused AIE MHA if enabled and conditions are met
        if is_prefill or not self.cfg["use_kv_cache"]:
            if (
                self.cfg["use_aie_fused_mha"]
                and b == 1
                and num_tokens == self.prompt_length
                and self.head_dim == 64
            ):
                # TODO: Doesn't give good output ven with num_kv_groups set to 8 with kv_cache
                # TODO: Doesn't match the output of CPU only when used without kv_cache
                context_vec = self.aie_mha(
                    queries, keys, values
                )  # Shape: (num_heads, num_tokens, head_dim)

                # Reshape context_vec to prepare for output projection
                context_vec = context_vec.transpose(1, 2)
                context_vec = context_vec.reshape(b, num_tokens, self.d_out)

            elif self.cfg["use_aie_regular_mha"]:
                # attn_scores = queries @ keys.transpose(2, 3)
                # Compute attention scores for each head separately since AIE GEMM doesn't support batched operations
                attn_scores_list = []
                for head in range(self.num_heads):
                    q_head = queries[:, head, :, :]  # Shape: (b, num_tokens, head_dim)
                    k_head = keys[:, head, :, :]  # Shape: (b, num_tokens, head_dim)

                    # Use 2D tensors directly (remove batch dimension if b=1)
                    q_2d = q_head.squeeze(0)  # Shape: (num_tokens, head_dim)
                    k_2d = k_head.squeeze(0)  # Shape: (num_tokens, head_dim)

                    # Compute Q @ K^T for this head
                    attn_head = self.aie_mha_gemm_qk(
                        q_2d, k_2d.T
                    )  # Shape: (num_tokens, num_tokens)
                    attn_head = attn_head.unsqueeze(0).unsqueeze(
                        0
                    )  # Add batch and head dimensions
                    attn_scores_list.append(
                        attn_head
                    )  # Shape: (1, 1, num_tokens, num_tokens)

                attn_scores = torch.cat(
                    attn_scores_list, dim=1
                )  # Shape: (b, num_heads, num_tokens, num_tokens)
                attn_scores = attn_scores.masked_fill(mask, -torch.inf)
                scaled_scores = attn_scores / (self.head_dim**0.5)

                # TODO: Make softmax more configurable to run in any scenario
                if (
                    scaled_scores.shape[-1] == self.prompt_length
                    and scaled_scores.shape[-1] % 16 == 0
                ):
                    attn_weights = self.aie_softmax(scaled_scores)
                else:
                    attn_weights = torch.nn.functional.softmax(scaled_scores, dim=-1)

                # Compute context vector for each head separately using AIE GEMM
                context_vec_list = []
                for head in range(self.num_heads):
                    attn_head = attn_weights[
                        :, head, :, :
                    ]  # Shape: (b, num_tokens, num_tokens)
                    v_head = values[:, head, :, :]  # Shape: (b, num_tokens, head_dim)

                    # Use 2D tensors directly (remove batch dimension if b=1)
                    attn_2d = attn_head.squeeze(0)  # Shape: (num_tokens, num_tokens)
                    v_2d = v_head.squeeze(0)  # Shape: (num_tokens, head_dim)

                    # Compute attn @ V for this head
                    context_head = self.aie_mha_gemm_pv(
                        attn_2d, v_2d
                    )  # Shape: (num_tokens, head_dim)
                    context_head = context_head.unsqueeze(0).unsqueeze(
                        1
                    )  # Add batch and head dimensions
                    context_vec_list.append(
                        context_head
                    )  # Shape: (1, 1, num_tokens, head_dim)

                context_vec = torch.cat(
                    context_vec_list, dim=1
                )  # Shape: (b, num_heads, num_tokens, head_dim)
                context_vec = context_vec.transpose(
                    1, 2
                )  # Shape: (b, num_tokens, num_heads, head_dim)
                context_vec = context_vec.reshape(b, num_tokens, self.d_out)
            else:

                def my_mha(queries, keys, values):
                    inv_scale = 1 / np.sqrt(values.shape[-1])
                    context_vec = torch.nn.functional.scaled_dot_product_attention(
                        queries.to(torch.bfloat16).to("cpu"),
                        keys.to(torch.bfloat16).to("cpu"),
                        values.to(torch.bfloat16).to("cpu"),
                        dropout_p=0.0,
                        is_causal=True,
                        scale=inv_scale,
                    )
                    return context_vec

                context_vec = my_mha(queries, keys, values)
                context_vec = context_vec.transpose(1, 2)
                context_vec = context_vec.reshape(b, num_tokens, self.d_out)
        else:
            attn_scores = queries @ keys.transpose(2, 3)

            if mask is not None:
                attn_scores = attn_scores.masked_fill(mask, -torch.inf)

            scaled_scores = attn_scores / (self.head_dim**0.5)

            if (
                scaled_scores.shape[-1] == self.prompt_length
                and self.cfg["use_aie_softmax"]
                and scaled_scores.shape[-1] % 16 == 0
            ):
                attn_weights = self.aie_softmax(scaled_scores)
            else:
                attn_weights = torch.nn.functional.softmax(scaled_scores, dim=-1)

            context_vec = (attn_weights @ values).transpose(1, 2)
            context_vec = context_vec.reshape(b, num_tokens, self.d_out)

        # Choose output projection based on phase
        if self.cfg["use_kv_cache"] and is_decode and self.cfg["use_aie_gemv"]:
            context_vec_flat = context_vec.reshape(1, -1)
            output_flat = self.aie_out_proj_gemv(context_vec_flat)
            context_vec = output_flat.reshape(b, num_tokens, self.d_out).to(input_dtype)
        elif self.cfg["use_aie_attn_projection_gemm"]:
            context_vec_flat = context_vec.reshape(-1, self.d_out)
            output_flat = self.aie_out_proj(context_vec_flat, self.out_proj.weight.T)
            context_vec = output_flat.reshape(b, num_tokens, self.d_out).to(input_dtype)
        else:
            context_vec = self.out_proj(context_vec)

        return context_vec

    def assign_weights(self, l, w_query, w_key, w_value, w_out_proj):
        if self.cfg["use_kv_cache"] and self.cfg["use_aie_gemv"]:
            self.aie_query_gemv.weight = w_query
            self.aie_key_gemv.weight = w_key
            self.aie_value_gemv.weight = w_value
            self.aie_out_proj_gemv.weight = w_out_proj

        self.W_query.weight = assign(
            self.W_query.weight,
            w_query,
            f"model.layers.{l}.self_attn.q_proj.weight",
        )
        self.W_key.weight = assign(
            self.W_key.weight,
            w_key,
            f"model.layers.{l}.self_attn.k_proj.weight",
        )
        self.W_value.weight = assign(
            self.W_value.weight,
            w_value,
            f"model.layers.{l}.self_attn.v_proj.weight",
        )
        self.out_proj.weight = assign(
            self.out_proj.weight,
            w_out_proj,
            f"model.layers.{l}.self_attn.o_proj.weight",
        )
