#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LFM2-1.2B over the shared decoder and layer (``iron.lm``): its short
convolution on the NPU (``Lfm2``) and LFM2-1.2B's shape, read from its
checkpoint's ``config.json``. Run it with ``python -m
iron.applications.lfm2.model``.

Sixteen layers, only six of them full attention (``full_attn_idxs``),
each with per-head q/k norms (Qwen3's shape); the rest are a gated short
causal depthwise convolution (``conv_L_cache=3`` taps) in place of
attention, then the same feed-forward block (``Lfm2Layer``). ``renames``
moves LFM2's modules to the names the layers give them before they load.

A conv layer's three per-channel taps, a row each (derived once it loads),
read a window that spans the current call and the ``conv_kernel - 1``
gated rows before it. Those rows are its ``ShortConv``'s ``Checkpoints``
state (``iron.lm``), a slot per chunk boundary, so a
prompt may resume from any chunk (a chat turn), after positions a decode
step wrote; slot 0, never written, is zero, "before the sequence".

The operators' tunables are the graph's profile, ``profiles/<device>.json``.
"""

import dataclasses
from pathlib import Path
from types import SimpleNamespace

import numpy as np

import iron
import iron.functional as F
from iron import lm
from iron.lm import (
    Attention,
    CausalLM,
    Checkpoints,
    DecoderConfig,
    DecoderLayer,
    GatedMLP,
    Linear,
    RMSNorm,
    not_json,
)
from iron.lm.blocks import _add


@dataclasses.dataclass(frozen=True)
class Lfm2Config(DecoderConfig):
    """``DecoderConfig``, LFM2's own feed-forward width and norm epsilon
    keys, and which layers are full attention.
    """

    intermediate_size: int = not_json(0, init=False)
    eps: float = dataclasses.field(
        default=1e-5, kw_only=True, metadata={"json": "norm_eps"}
    )
    # Hugging Face's Lfm2MLP narrows block_ff_dim by the three after it.
    block_ff_dim: int = dataclasses.field(kw_only=True)
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
        default=(), metadata={"convert": tuple}
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


class ShortConv(iron.Graph):
    """The gated short conv in place of attention: a depth-wise causal FIR
    of ``conv_kernel`` taps over a call's rows, each channel its own tap
    weights, gated on both sides by rows of ``in_proj``, then ``out_proj``.
    The ``conv_kernel - 1`` gated rows before a call are its ``state``, a
    slot per prompt-chunk boundary; ``window`` and ``tail`` are the scratch
    the model's conv layers share.
    """

    def __init__(self, c: Lfm2Config):
        E, K = c.hidden_size, c.conv_kernel
        self.in_proj = Linear(E, 3 * E, bias=False)
        self.conv = SimpleNamespace(weight=iron.param(E, 1, K))
        self.out_proj = Linear(E, E, bias=False)
        self.state = Checkpoints.of((K - 1, E), c.max_seq_len, c.prefill_chunk)
        self.window = self.tail = None

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        # A row per tap, each the row RowwiseMul takes.
        E, _, K = self.conv.weight.shape
        self.taps = np.ascontiguousarray(self.conv.weight.reshape(E, K).T)

    def body(self, h, call):
        n, E = h.shape[0], self.out_proj.weight.shape[0]
        b, c, x = (y.reshape(n, E) for y in self.in_proj.split(h, E, E, E))
        read, write = self.state.at(call)
        state = F.ConvState(read, write, self.window, self.tail)
        return self.out_proj(c * F.causal_conv1d(b * x, self.taps, state))


class Lfm2Layer(DecoderLayer):
    """Layer ``i``: where ``full_attn_idxs`` names it, Llama's, its q and k
    normed per head; else a ``ShortConv`` in attention's place.
    """

    def __init__(self, c: Lfm2Config, i: int):
        if i in c.full_attn_idxs:
            attention = Attention(c, i, norms="qk", o_bias=c.attention_bias)
            super().__init__(c, i, attention)
            self.conv = None
            return
        self.input_layernorm = RMSNorm(c.hidden_size, c.eps)
        self.post_attention_layernorm = RMSNorm(c.hidden_size, c.eps)
        self.mlp = GatedMLP(c)
        self.residual_multiplier = 1.0
        self.conv = ShortConv(c)

    def body(self, x, call):
        if self.conv is None:
            return super().body(x, call)
        x = _add(x, self.conv(self.input_layernorm(x), call), self.residual_multiplier)
        h = self.mlp(self.post_attention_layernorm(x))
        return _add(x, h, self.residual_multiplier)


class Lfm2(CausalLM):
    """LFM2-1.2B on ``config``'s shape and a checkpoint's ``weights``,
    renamed as ``Lfm2Layer`` names them. Every matrix is read ``(out,
    in)``, as the checkpoint ships it. From its checkpoint and
    ``tokenizer.json``.
    """

    config = Lfm2Config
    profile = Path(__file__).with_name("profiles")
    layer_class = Lfm2Layer
    renames = {
        "model.embedding_norm": "model.norm",
        "operator_norm": "input_layernorm",
        "ffn_norm": "post_attention_layernorm",
        "feed_forward.w1": "mlp.gate_proj",
        "feed_forward.w3": "mlp.up_proj",
        "feed_forward.w2": "mlp.down_proj",
        "self_attn.out_proj": "self_attn.o_proj",
        "self_attn.q_layernorm": "self_attn.q_norm",
        "self_attn.k_layernorm": "self_attn.k_norm",
    }

    def __init__(self, config: Lfm2Config, weights):
        super().__init__(config, weights)
        E, K, C = config.hidden_size, config.conv_kernel, config.prefill_chunk
        window, tail = iron.state((2, C, E)), iron.state((K - 1, E))
        for layer in self.layers:
            if layer.conv is not None:
                layer.conv.window, layer.conv.tail = window, tail


if __name__ == "__main__":
    lm.main(Lfm2)
