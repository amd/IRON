# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 in torch: the CPU reference the NPU is judged against.

Nothing on the NPU path imports this module: the graphs close over
:class:`.weights.LlamaWeights` and name their buffers from it. The tree here
carries the same names (:meth:`Llama.from_weights` fills it from those
arrays), and :meth:`Llama.from_hf` fills it from a Hugging Face
``state_dict``, which is what pins the names to the checkpoint's.

:meth:`Llama.forward` is the model as torch computes it: a stateless causal
pass over one token sequence. It is the second opinion the graphs are
checked against on the host (``iron/tests/common/llama_reference.py``) and
the oracle of the accuracy check (:mod:`.reference`): the
graph references define what the graphs compute, so only an independent
forward can catch a wiring mistake, a transposed layout or a softmax over
the wrong length. It needs no cache, because the logits at position ``t``
of a causal pass over ``t + 1`` tokens are what a cached decode produces at
step ``t``.
"""

import numpy as np
import torch
import torch.nn.functional as F
from ml_dtypes import bfloat16
from torch import nn

from .weights import LlamaWeights


class Attention(nn.Module):
    """Grouped-query attention: q is full width, k and v are grouped."""

    def __init__(self, emb_dim, n_heads, n_kv_groups, head_dim, dtype):
        super().__init__()
        self.q = _proj(emb_dim, n_heads * head_dim, dtype)
        self.k = _proj(emb_dim, n_kv_groups * head_dim, dtype)
        self.v = _proj(emb_dim, n_kv_groups * head_dim, dtype)
        self.o = _proj(n_heads * head_dim, emb_dim, dtype)


class FeedForward(nn.Module):
    """SwiGLU: two projections up, one back down."""

    def __init__(self, emb_dim, hidden_dim, dtype):
        super().__init__()
        self.gate = _proj(emb_dim, hidden_dim, dtype)
        self.up = _proj(emb_dim, hidden_dim, dtype)
        self.down = _proj(hidden_dim, emb_dim, dtype)


class Block(nn.Module):
    """One pre-norm transformer block."""

    def __init__(self, cfg, dtype):
        super().__init__()
        self.norm1 = _norm(cfg.emb_dim, dtype)
        self.attn = Attention(
            cfg.emb_dim, cfg.n_heads, cfg.n_kv_groups, cfg.head_dim, dtype
        )
        self.norm2 = _norm(cfg.emb_dim, dtype)
        self.ffn = FeedForward(cfg.emb_dim, cfg.hidden_dim, dtype)


class Llama(nn.Module):
    """Every weight llama 3.2 has, named as the checkpoint names it."""

    def __init__(self, cfg, dtype=torch.bfloat16):
        super().__init__()
        self.n_heads, self.n_kv_groups, self.head_dim = (
            cfg.n_heads,
            cfg.n_kv_groups,
            cfg.head_dim,
        )
        self.layers = nn.ModuleList([Block(cfg, dtype) for _ in range(cfg.n_layers)])
        self.norm = _norm(cfg.emb_dim, dtype)
        # Llama 3.2 ties the output head to the token embedding, so this one
        # parameter is read both to embed a token and to produce logits.
        self.out_head = _proj(cfg.emb_dim, cfg.vocab_size, dtype)

    def forward(self, tokens, angles):
        """Logits at every position of one token sequence, causally.

        ``tokens`` is ``(n,)``; ``angles`` the RoPE table, of which the first
        ``n`` rows apply. Returns ``(n, vocab_size)``.
        """
        (n,), H, G, D = tokens.shape, self.n_heads, self.n_kv_groups, self.head_dim
        x = F.embedding(tokens, self.out_head.weight)
        for blk in self.layers:
            assert isinstance(blk, Block)
            h = blk.norm1(x)
            q = _rope(blk.attn.q(h).view(n, H, D), angles[:n])
            k = _rope(blk.attn.k(h).view(n, G, D), angles[:n])
            v = blk.attn.v(h).view(n, G, D)
            o = F.scaled_dot_product_attention(
                q.transpose(0, 1),
                k.transpose(0, 1),
                v.transpose(0, 1),
                is_causal=True,
                enable_gqa=True,
            )
            x = x + blk.attn.o(o.transpose(0, 1).reshape(n, H * D))
            h = blk.norm2(x)
            x = x + blk.ffn.down(F.silu(blk.ffn.gate(h)) * blk.ffn.up(h))
        return self.out_head(self.norm(x))

    @classmethod
    def from_hf(cls, cfg, weights, dtype=torch.bfloat16):
        """Build the tree and fill it from a Hugging Face ``state_dict``.

        The tree is built on the ``meta`` device -- its parameters have shapes
        and dtypes but no storage -- and filled with ``assign=True`` so each
        parameter *becomes* the checkpoint tensor rather than being copied into.
        Without this the constructor would kaiming-initialise all 1.236 B
        parameters (~2.5 GB) purely to overwrite them, and the filled tree would
        then hold a second 2.5 GB that shares nothing with the checkpoint.
        ``assign=True`` makes the parameters share storage with ``weights``.
        """
        with torch.device("meta"):
            model = cls(cfg, dtype)
        model.load_state_dict(translate_hf(weights, cfg.n_layers), assign=True)
        # Nothing here trains, and a consumer feeds a weight straight into a
        # host ``F.linear``; grad tracking would only cost memory and surprise.
        model.requires_grad_(False)
        return model

    @classmethod
    def from_weights(cls, cfg, weights: LlamaWeights, dtype=torch.bfloat16):
        """Build the tree over a :class:`.weights.LlamaWeights`.

        Its names are already the tree's, so nothing is translated. A bf16
        tree over writable bf16 arrays shares their storage; anything else
        (a float32 reference, the read-only views of a mapped checkpoint)
        is a copy.
        """
        with torch.device("meta"):
            model = cls(cfg, dtype)
        state = {name: _tensor(a, dtype) for name, a in weights.named_parameters()}
        model.load_state_dict(state, assign=True)
        model.requires_grad_(False)
        return model


def _tensor(a: np.ndarray, dtype) -> torch.Tensor:
    """``a`` as a torch tensor of ``dtype``, sharing storage where it can."""
    if dtype is torch.bfloat16 and a.dtype == bfloat16:
        bits = a.view(np.uint16)
        if not bits.flags.writeable:
            bits = bits.copy()
        return torch.from_numpy(bits).view(torch.bfloat16)
    return torch.from_numpy(np.array(a, dtype=np.float32)).to(dtype)


def rope_angles(head_dim, context_length, rope_base=500000.0):
    """The RoPE table, ``(context_length, head_dim)``: cos and sin interleaved
    per frequency, as the device kernel and :func:`_rope` read it.
    """
    inv_freq = 1.0 / (rope_base ** (torch.arange(0, head_dim, 2).float() / head_dim))
    freqs = torch.outer(torch.arange(context_length).float(), inv_freq)
    angles = torch.empty(context_length, head_dim)
    angles[:, ::2] = torch.cos(freqs)
    angles[:, 1::2] = torch.sin(freqs)
    return angles


def _rope(x, angles):
    """Rotate the two halves of each ``(n, heads, head_dim)`` row by its position."""
    half = x.shape[-1] // 2
    x1, x2 = x[..., :half], x[..., half:]
    cos = angles[:, ::2].unsqueeze(1).to(x.dtype)
    sin = angles[:, 1::2].unsqueeze(1).to(x.dtype)
    return torch.cat((x1 * cos - x2 * sin, x1 * sin + x2 * cos), dim=-1)


# Hugging Face names, translated once
# ##########################################################################

#: Per-layer checkpoint suffix -> our per-layer parameter suffix.
FROM_HF = {
    "input_layernorm.weight": "norm1.weight",
    "self_attn.q_proj.weight": "attn.q.weight",
    "self_attn.k_proj.weight": "attn.k.weight",
    "self_attn.v_proj.weight": "attn.v.weight",
    "self_attn.o_proj.weight": "attn.o.weight",
    "post_attention_layernorm.weight": "norm2.weight",
    "mlp.gate_proj.weight": "ffn.gate.weight",
    "mlp.up_proj.weight": "ffn.up.weight",
    "mlp.down_proj.weight": "ffn.down.weight",
}

#: Whole-model checkpoint keys -> our parameter names.
FROM_HF_TOP = {
    "model.norm.weight": "norm.weight",
    "model.embed_tokens.weight": "out_head.weight",
}


def translate_hf(weights, n_layers):
    """Rename a Hugging Face ``state_dict`` onto this tree's parameter names.

    Raises if the checkpoint is missing anything the tree declares, so a
    renamed upstream key fails here rather than silently leaving a weight at
    its initial value.
    """
    out = {}
    for hf, ours in FROM_HF_TOP.items():
        out[ours] = weights[hf]
    for i in range(n_layers):
        for hf, ours in FROM_HF.items():
            out[f"layers.{i}.{ours}"] = weights[f"model.layers.{i}.{hf}"]
    return out


def _proj(in_features, out_features, dtype):
    """A bias-free projection, stored ``(out, in)`` exactly as HF ships it."""
    return nn.Linear(in_features, out_features, bias=False, dtype=dtype)


def _norm(dim, dtype):
    # eps must be spelled out: nn.RMSNorm(dim).eps is None, which makes torch
    # fall back to finfo(bfloat16).eps ~= 0.0078 instead of Llama's 1e-5 -- a
    # wrong number that would otherwise sit silently in the tree.
    return nn.RMSNorm(dim, eps=1e-5, dtype=dtype)
