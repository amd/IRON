# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn as nn
from src.block.gqa import GroupedQueryAttention
from src.block.feed_forward import FeedForward


class TransformerBlock(nn.Module):
    def __init__(
        self,
        cfg,
        prompt_length=42,
        num_tokens=1,
    ):
        super().__init__()
        self.cfg = cfg.copy()

        self.att = GroupedQueryAttention(
            d_in=cfg["emb_dim"],
            d_out=cfg["emb_dim"],
            num_heads=cfg["n_heads"],
            num_kv_groups=cfg["n_kv_groups"],
            dtype=cfg["dtype"],
            prompt_length=prompt_length,
            cfg=cfg,
        )
        self.ff = FeedForward(
            cfg,
            prompt_length=prompt_length,
            num_tokens=num_tokens,
        )

        self.norm1 = nn.RMSNorm(cfg["emb_dim"], eps=1e-5, dtype=cfg["dtype"])
        self.norm2 = nn.RMSNorm(cfg["emb_dim"], eps=1e-5, dtype=cfg["dtype"])

        if self.cfg["use_aie_norm1"]:
            from src.operator.aie_rms_norm import AIERMSNorm

            if self.cfg["use_kv_cache"]:
                max_prefill_size = prompt_length * self.cfg["emb_dim"]
            else:
                max_prefill_size = (prompt_length + num_tokens) * self.cfg["emb_dim"]
            self.aie_norm1_prefill = AIERMSNorm(
                size=max_prefill_size,
                eps=1e-5,
                num_columns=8,
                num_channels=2,
                tile_size=self.cfg["emb_dim"],
            )
            # For decode phase - single token (only when using KV cache)
            if self.cfg["use_kv_cache"]:
                decode_size = self.cfg["emb_dim"]  # 1 token * emb_dim
                self.aie_norm1_decode = AIERMSNorm(
                    size=decode_size,
                    eps=1e-5,
                    num_columns=1,
                    num_channels=2,
                    tile_size=self.cfg["emb_dim"],
                )
            else:
                # When not using KV cache, use same operator for both phases
                self.aie_norm1_decode = self.aie_norm1_prefill

        if self.cfg["use_aie_norm2"]:
            from src.operator.aie_rms_norm import AIERMSNorm

            if self.cfg["use_kv_cache"]:
                max_prefill_size = prompt_length * self.cfg["emb_dim"]
            else:
                max_prefill_size = (prompt_length + num_tokens) * self.cfg["emb_dim"]
            self.aie_norm2_prefill = AIERMSNorm(
                size=max_prefill_size,
                eps=1e-5,
                num_columns=8,
                num_channels=2,
                tile_size=self.cfg["emb_dim"],
            )
            # For decode phase - single token (only when using KV cache)
            if self.cfg["use_kv_cache"]:
                decode_size = self.cfg["emb_dim"]  # 1 token * emb_dim
                self.aie_norm2_decode = AIERMSNorm(
                    size=decode_size,
                    eps=1e-5,
                    num_columns=1,
                    num_channels=2,
                    tile_size=self.cfg["emb_dim"],
                )
            else:
                # When not using KV cache, use same operator for both phases
                self.aie_norm2_decode = self.aie_norm2_prefill

        if self.cfg["use_aie_residual"]:
            from src.operator.aie_elementwise_add import AIEElementwiseAdd

            if self.cfg["use_kv_cache"]:
                max_prefill_size = prompt_length * cfg["emb_dim"]
            else:
                max_prefill_size = (prompt_length + num_tokens) * cfg["emb_dim"]

            self.aie_residual_add_prefill = AIEElementwiseAdd(
                size=max_prefill_size,
                num_columns=8,
                num_channels=2,
                tile_size=cfg["emb_dim"],
            )

            # For decode phase - single token (only when using KV cache)
            if self.cfg["use_kv_cache"]:
                decode_size = cfg["emb_dim"]  # 1 token * emb_dim
                self.aie_residual_add_decode = AIEElementwiseAdd(
                    size=decode_size,
                    num_columns=1,
                    num_channels=2,
                    tile_size=cfg["emb_dim"],
                )
            else:
                # When not using KV cache, use same operator for both phases
                self.aie_residual_add_decode = self.aie_residual_add_prefill

    def forward(self, x, mask, angles, input_pos):
        original_shape = x.shape

        # (batch, sequence, embedding) where sequence=1 indicates decode
        if len(x.shape) == 3:
            is_decode_with_kv = (x.shape[1] == 1) and self.cfg["use_kv_cache"]
        elif len(x.shape) == 2:
            is_decode_with_kv = (x.shape[0] == 1) and self.cfg["use_kv_cache"]
        else:
            is_decode_with_kv = False

        shortcut = x
        if self.cfg["use_aie_norm1"]:
            if is_decode_with_kv:
                x = self.aie_norm1_decode(x, self.norm1.weight)
            else:
                x = self.aie_norm1_prefill(x, self.norm1.weight)
        else:
            x = self.norm1(x)

        x = self.att(x, mask, angles, input_pos)

        if self.cfg["use_aie_residual"]:
            if is_decode_with_kv:
                x = self.aie_residual_add_decode(x, shortcut)
            else:
                x = self.aie_residual_add_prefill(x, shortcut)
        else:
            x = x + shortcut

        # Shortcut connection for feed-forward block
        shortcut = x
        if self.cfg["use_aie_norm2"]:
            if is_decode_with_kv:
                x = self.aie_norm2_decode(x, self.norm2.weight)
            else:
                x = self.aie_norm2_prefill(x, self.norm2.weight)
        else:
            x = self.norm2(x)

        x = self.ff(x)

        if self.cfg["use_aie_residual"]:
            if is_decode_with_kv:
                x = self.aie_residual_add_decode(x, shortcut)
            else:
                x = self.aie_residual_add_prefill(x, shortcut)
        else:
            x = x + shortcut

        return x
