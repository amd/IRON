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
gated rows before it. Those rows are its ``CausalConv1d``'s ``Checkpoints``
state (``iron.lm``), a slot per chunk boundary, so a
prompt may resume from any chunk (a chat turn), after positions a decode
step wrote; slot 0, never written, is zero, "before the sequence".

The operators' tunables are the graph's profile, ``profiles/<device>.json``.
"""

import dataclasses
from pathlib import Path

import iron
from iron import Precision, lm
from iron.lm import (
    Attention,
    CausalConv1d,
    CausalLM,
    DecoderConfig,
    DecoderLayer,
    GatedMLP,
    Linear,
    RMSNorm,
    not_json,
)


@dataclasses.dataclass(frozen=True)
class Lfm2Config(DecoderConfig):
    """``DecoderConfig``, LFM2's own feed-forward width and norm epsilon
    keys, which layers are full attention, and every projection's
    ``precision``.
    """

    precision: Precision = lm.not_json(Precision.MEDIUM, kw_only=True)
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
    weights (``CausalConv1d``), gated on both sides by rows of
    ``in_proj``, then ``out_proj``.
    """

    def __init__(self, c: Lfm2Config):
        E, K = c.hidden_size, c.conv_kernel
        self.in_proj = Linear(E, 3 * E, bias=False, precision=c.precision)
        self.conv = CausalConv1d(c, E, K)
        self.out_proj = Linear(E, E, bias=False, precision=c.precision)

    def body(self, h, call):
        n, E = h.shape[0], self.out_proj.weight.shape[0]
        b, c, x = (y.reshape(n, E) for y in self.in_proj.split(h, E, E, E))
        return self.out_proj(c * self.conv(b * x, call))


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

    def mix(self, h, call):
        return super().mix(h, call) if self.conv is None else self.conv(h, call)


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


if __name__ == "__main__":
    lm.main(Lfm2)
