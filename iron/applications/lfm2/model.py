#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LFM2-1.2B over the shared decoder and layer (``iron.lm``): its short
convolution on the NPU (``Lfm2``) and LFM2-1.2B's shape, read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.lfm2.model``.

Sixteen layers, only six of them full attention (``full_attn_idxs``),
each a ``DecoderLayer`` with per-head q/k norms (Qwen3's shape); the rest
are a gated short causal depthwise convolution (``conv_L_cache=3`` taps)
in place of attention, then the same feed-forward block. ``renames``
moves LFM2's modules to the names the parts read once at load; a conv
layer holds no ``self_attn``, so ``layer()`` takes the whole
``DecoderLayer`` where the checkpoint holds one.

A conv layer's three per-channel taps, a row each (``sanitize``, once at
load), read a window that spans the current call and the
``conv_kernel - 1`` gated rows before it. Those rows are the layer's
``Checkpoints`` state (``iron.lm``), a slot per chunk boundary, so a
prompt may resume from any chunk (a chat turn), after positions a decode
step wrote; slot 0, never written, is zero, "before the sequence".

The operators' tunables are the graph's profile, ``profiles/<device>.json``.
"""

import dataclasses
from functools import partial
from pathlib import Path

import numpy as np

import iron
import iron.functional as F
from iron import lm
from iron.lm import Attention, CausalLM, Checkpoints, DecoderConfig
from iron.operators.copy import Copy
from iron.operators.elementwise_mul import RowwiseMul


@dataclasses.dataclass(frozen=True)
class Lfm2Config(DecoderConfig):
    """``DecoderConfig``, LFM2's own feed-forward width and norm epsilon
    keys, and which layers are full attention.
    """

    intermediate_size: int = dataclasses.field(default=0, init=False)
    eps: float = dataclasses.field(
        default=1e-5, kw_only=True, metadata={"json": "norm_eps"}
    )
    # Hugging Face's Lfm2MLP narrows block_ff_dim by the three after it.
    block_ff_dim: int = dataclasses.field(
        kw_only=True, metadata={"json": "block_ff_dim"}
    )
    auto_adjust_ff_dim: bool = dataclasses.field(
        default=False, kw_only=True, metadata={"json": "block_auto_adjust_ff_dim"}
    )
    ffn_dim_multiplier: float | None = dataclasses.field(
        default=None, kw_only=True, metadata={"json": "block_ffn_dim_multiplier"}
    )
    multiple_of: int = dataclasses.field(
        default=1, kw_only=True, metadata={"json": "block_multiple_of"}
    )
    #: Layer indices that are full attention; every other layer is a
    #: gated short conv.
    full_attn_idxs: tuple[int, ...] = dataclasses.field(
        default=(), metadata={"json": "full_attn_idxs", "convert": tuple}
    )
    #: The short conv's kernel width.
    conv_kernel: int = dataclasses.field(default=3, metadata={"json": "conv_L_cache"})

    def __post_init__(self):
        super().__post_init__()
        ff = self.block_ff_dim
        if self.auto_adjust_ff_dim:
            ff = int(2 * ff / 3)
            if self.ffn_dim_multiplier is not None:
                ff = int(self.ffn_dim_multiplier * ff)
            ff = self.multiple_of * -(-ff // self.multiple_of)
        object.__setattr__(self, "intermediate_size", ff)

    def attention(self, i: int) -> Attention:
        return dataclasses.replace(super().attention(i), qk_norm=True)


class Lfm2(CausalLM):
    """LFM2-1.2B on ``config``'s shape and a checkpoint's ``weights``, by
    its names: each layer either an attention layer's weights or a conv
    layer's, distinguished by which the checkpoint gives it. Every matrix
    is read ``(out, in)``, as the checkpoint ships it.
    """

    profile = Path(__file__).with_name("profiles")

    def __init__(self, config: Lfm2Config, weights):
        super().__init__(config, weights)
        self.final_norm = self.decoder.embedding_norm
        E, K, C = config.hidden_size, config.conv_kernel, config.prefill_chunk
        for i, w in enumerate(self.layers):
            if "conv" in vars(w):
                tail = Checkpoints.of((K - 1, E), config.max_seq_len, C)
                self.recurrent[i] = {"conv": tail}
        # The rows before a call end block 0; a chunk's rows are block 1.
        self.conv_window = iron.state((2, C, E))
        self.conv_tail = iron.state((K - 1, E))

    renames = {
        "operator_norm": "input_layernorm",
        "ffn_norm": "post_attention_layernorm",
        "feed_forward.w1": "mlp.gate_proj",
        "feed_forward.w3": "mlp.up_proj",
        "feed_forward.w2": "mlp.down_proj",
        "self_attn.out_proj": "self_attn.o_proj",
        "self_attn.q_layernorm": "self_attn.q_norm",
        "self_attn.k_layernorm": "self_attn.k_norm",
    }

    def sanitize(self, w):
        if "conv" in vars(w):
            # A row per tap, each the row RowwiseMul takes.
            c = self.config
            taps = w.conv.conv.weight.reshape(c.hidden_size, c.conv_kernel).T
            w.conv.taps = np.ascontiguousarray(taps)
        return w

    def layer(self, step, i, w, x):
        """Layer ``i``: an attention layer is ``DecoderLayer``'s; a conv
        layer its short conv in attention's place, then the feed-forward.
        """
        if "self_attn" in vars(w):
            return super().layer(step, i, w, x)
        layer = self.config.layer(i)
        x = layer.block(x, w.input_layernorm, partial(self.conv, step, i, w.conv))
        return layer.block(x, w.post_attention_layernorm, partial(layer.mlp, w.mlp))

    def conv(self, step, i, w, h):
        """The gated short conv in place of attention: a depth-wise causal
        FIR of ``conv_kernel`` taps over ``h``'s rows, each channel its own
        tap weights, gated on both sides by a projection of ``h``.
        """
        c, n = self.config, h.shape[0]
        E, K, C = c.hidden_size, c.conv_kernel, c.prefill_chunk
        # Three projections, not one split three ways: a bounded row count's
        # column range of a combined projection is a strided view no single
        # descriptor fits, where three plain projections need none.
        b, cc, x = (
            F.linear(h, w.in_proj.weight[k * E : (k + 1) * E]).reshape(n, E)
            for k in range(3)
        )
        gated = b * x
        tap = w.taps
        read, write = self.recurrent[i]["conv"].at(step)
        flat = self.conv_window.reshape(2 * C, E)
        first = C - (K - 1)
        Copy.step(read, flat[first:C])
        if step.prompt:
            Copy.step(gated, self.conv_window[1, : step.rows])
            total = RowwiseMul.step(flat[first : first + C], tap[0])
            for k in range(1, K):
                total = total + RowwiseMul.step(flat[first + k : first + k + C], tap[k])
            total = total[: step.rows]
            for j in range(K - 1):
                Copy.step(flat[first + step.rows + j], self.conv_tail[j])
            Copy.step(self.conv_tail, write)
        else:
            Copy.step(gated.reshape(E), flat[C])
            total = RowwiseMul.step(gated, tap[K - 1])
            for k in range(K - 1):
                total = total + RowwiseMul.step(flat[first + k : first + k + 1], tap[k])
            Copy.step(flat[first + 1 : C + 1], write)
        return F.linear(cc * total, w.out_proj.weight)


class Runner(lm.Runner):
    """LFM2-1.2B, from its checkpoint and ``tokenizer.json``."""

    config = Lfm2Config
    model = Lfm2
    bos = 1


if __name__ == "__main__":
    lm.main(Runner, "LFM2-1.2B on the NPU")
