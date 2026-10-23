# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3.5's text decoder on the shared decoder (``iron.lm``), its shape
read from its checkpoint's ``config.json``. Run it with ``python -m
iron.applications.qwen3_5.model``.

Qwen3.5 is Llama's layer with most layers' attention replaced by a Gated
DeltaNet (``GatedDeltaNet``), every norm scaling by ``1 + weight``
(``RMSNorm.plus_one``). The attention layers norm q and k per head, turn
only the first ``partial_rotary_factor`` of each head, and gate their
output by a sigmoid of a second projection of the input, q's rows each
head's [q | gate] in the checkpoint (``GatedAttention``).

A Gated DeltaNet projects its input to q, k and v, which pass a short
causal depthwise convolution and SiLU, and to a gate ``z`` and each value
head's ``a`` and ``b``; the gated delta rule (``GatedDeltaRule``) reads
them; its output is RMS-normed per head, times silu of ``z``, and
projected back. The convolution's last rows and the rule's state are the
layer's ``Checkpoints`` states, as Granite 4.0-H's Mamba2 mixer's are.
"""

import dataclasses

import numpy as np

import iron
import iron.functional as F
from iron import lm
from iron.lm import Attention, CausalConv1d, CausalLM, Checkpoints, DecoderConfig
from iron.lm import DecoderLayer, Linear, RMSNorm, Weights, subtree
from iron.operators.copy import Copy
from iron.operators.gated_delta_rule import GatedDeltaRule
from iron.operators.sigmoid import Sigmoid


@dataclasses.dataclass(frozen=True)
class Qwen35Config(DecoderConfig):
    """``DecoderConfig`` under ``text_config``, which layers are attention,
    the Gated DeltaNet's shape and the rotated fraction of a head.
    """

    json_prefix = "text_config."

    rope_theta: float = dataclasses.field(
        metadata={"json": "rope_parameters.rope_theta"}
    )
    layer_types: tuple[str, ...] = dataclasses.field(
        kw_only=True, metadata={"convert": tuple}
    )
    partial_rotary_factor: float = dataclasses.field(
        default=0.25,
        kw_only=True,
        metadata={"json": "rope_parameters.partial_rotary_factor"},
    )
    linear_conv_kernel_dim: int = dataclasses.field(kw_only=True)
    linear_key_head_dim: int = dataclasses.field(kw_only=True)
    linear_value_head_dim: int = dataclasses.field(kw_only=True)
    linear_num_key_heads: int = dataclasses.field(kw_only=True)
    linear_num_value_heads: int = dataclasses.field(kw_only=True)

    def __post_init__(self):
        super().__post_init__()
        kinds = set(self.layer_types) - {"full_attention", "linear_attention"}
        if len(self.layer_types) != self.num_hidden_layers or kinds:
            raise ValueError(
                f"Qwen35Config: layer_types {self.layer_types} are not "
                f"{self.num_hidden_layers} of full_attention and linear_attention"
            )
        rotary = int(self.head_dim * self.partial_rotary_factor)
        object.__setattr__(self, "rotary_dim", rotary)

    @classmethod
    def from_json(cls, data: dict, source="config.json") -> "Qwen35Config":
        """``DecoderConfig.from_json``.

        Raises:
            ValueError: ``data`` asks for what is not built: biased
                attention or a scaled RoPE.
        """
        text = dict(data.get("text_config", {}))
        # Its own, else the file's root, where a released checkpoint has it.
        if "tie_word_embeddings" in data:
            text.setdefault("tie_word_embeddings", data["tie_word_embeddings"])
        if text.get("attention_bias"):
            raise ValueError(f"{source}: attention_bias is not built here")
        kind = text.get("rope_parameters", {}).get("rope_type", "default")
        if kind != "default":
            raise ValueError(f"{source}: RoPE {kind!r} is not built here")
        return super().from_json({**data, "text_config": text}, source)

    @property
    def conv_channels(self) -> int:
        """A Gated DeltaNet's convolved channels: q, k, then v."""
        K, V = self.linear_key_head_dim, self.linear_value_head_dim
        return 2 * self.linear_num_key_heads * K + self.linear_num_value_heads * V


class GatedAttention(Attention):
    """``Attention`` normed per head on q and k, its output times a sigmoid
    of the gate, ``q_proj``'s second half once loaded.
    """

    def projections(self, c) -> None:
        super().projections(c)
        self.q_proj = Linear(c.hidden_size, 2 * self.heads * self.head_dim, False)

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        H, D = self.heads, self.head_dim
        # Each head's [q | gate] rows, as every q's then every gate's.
        w = self.q_proj.weight.reshape(H, 2, D, -1).transpose(1, 0, 2, 3)
        self.q_proj.weight, self.gate = w.reshape(2, H * D, -1)
        self.q_proj.out_features = H * D

    def output(self, o, x):
        return self.o_proj(o * Sigmoid.step(F.linear(x, self.gate)))


class GatedDeltaNet(iron.Graph):
    """A Gated DeltaNet on ``c``'s shape: ``in_proj_qkv``, ``conv1d`` over
    it and SiLU, the gated delta rule over it, ``in_proj_a`` and
    ``in_proj_b``; ``norm`` per value head times silu of ``in_proj_z``;
    and ``out_proj``.
    """

    def __init__(self, c: Qwen35Config):
        E, K = c.hidden_size, c.linear_conv_kernel_dim
        Hv, Dv = c.linear_num_value_heads, c.linear_value_head_dim
        self.channels, self.k_heads = c.conv_channels, c.linear_num_key_heads
        self.eps = c.eps
        self.in_proj_qkv = Linear(E, self.channels, False)
        self.in_proj_z = Linear(E, Hv * Dv, False)
        self.in_proj_b, self.in_proj_a = Linear(E, Hv, False), Linear(E, Hv, False)
        self.conv1d = CausalConv1d(c, self.channels, K)
        self.dt_bias, self.A_log = iron.param(Hv), iron.param(Hv)
        # Plain: not one of the norms that scale by 1 + weight.
        self.norm = Weights(weight=(Dv,))
        self.out_proj = Linear(Hv * Dv, E, False)
        state = (Hv, c.linear_key_head_dim, Dv)
        self.ssm_state = Checkpoints.of(
            state, c.max_seq_len, c.prefill_chunk, np.float32
        )

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        # Each value head's (dt_bias, A) in float32.
        A = -np.exp(np.asarray(self.A_log, np.float32))
        self.head = iron.param(np.stack([self.dt_bias, A], 1).astype(np.float32))

    def body(self, x, call):
        n, Hv, Dv = x.shape[0], self.head.shape[0], self.norm.weight.size
        qkv = F.silu(self.conv1d(self.in_proj_qkv(x), call))
        read, write = self.ssm_state.at(call)
        y, final = GatedDeltaRule.step(
            qkv,
            self.in_proj_a(x),
            self.in_proj_b(x),
            self.head,
            Copy.step(read, dtype=np.float32),
            k_heads=self.k_heads,
        )
        Copy.step(final, write, dtype=np.float32)
        y = F.rms_norm(y.reshape(n * Hv, Dv), (Dv,), self.norm.weight, self.eps)
        return self.out_proj(y.reshape(n, Hv * Dv) * F.silu(self.in_proj_z(x)))


class Qwen35Layer(DecoderLayer):
    """Llama's layer, ``linear_attn`` in attention's place where the layer
    is linear attention, else ``GatedAttention``.
    """

    def __init__(self, c: Qwen35Config, i: int):
        self.linear_attn = None
        if c.layer_types[i] == "full_attention":
            super().__init__(c, i, GatedAttention(c, i, norms="qk"))
            return
        super().__init__(c, i)
        del self.self_attn, self.cache
        self.linear_attn = GatedDeltaNet(c)

    def mix(self, h, call):
        if self.linear_attn is None:
            return super().mix(h, call)
        return self.linear_attn(h, call)


class Qwen35(CausalLM):
    """Qwen3.5's text decoder on ``config``'s shape and a checkpoint's
    ``weights``, the decoder's under ``model.language_model`` (the vision
    tower and the multi-token prediction head unread), from its checkpoint
    and ``tokenizer.json``.

    The checkpoint has no ``generation_config.json``: generation stops at
    ``<|endoftext|>`` or ``<|im_end|>``.
    """

    config = Qwen35Config
    profile = None
    layer_class = Qwen35Layer
    eos = {248044, 248046}

    def __init__(self, config: Qwen35Config, weights):
        head = {} if config.tie_word_embeddings else {"lm_head": weights.lm_head}
        text = subtree(weights, model=weights.model.language_model, **head)
        super().__init__(config, text)

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        RMSNorm.plus_one(self)


if __name__ == "__main__":
    lm.main(Qwen35)
