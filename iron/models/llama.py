# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2's parameters, as a module tree.

A checkpoint is a ``state_dict``, so the thing that reads one should be an
``nn.Module``. Declaring the tree once buys the whole surface for free:
``load_state_dict`` to fill it, ``named_parameters()`` to walk it, ``__repr__``
to print it -- and, most usefully here, a *name* for every weight that is the
same string on the checkpoint, in the module tree, and on the device buffer.

That last point is what this file is really for. Both llama backends used to
spell out where each weight came from, one hand-typed key per weight per
layer::

    self.decode.fused.get_buffer(f"W_attn_query_{i}").torch_view()[:] = (
        config.weights[f"model.layers.{i}.self_attn.q_proj.weight"].flatten())

with a matching list on the prefill side. Nine of those per layer, in two
places, with a ``.T`` on some and not others. Here the same fact is one row of
:data:`FROM_HF`, and uploading is a loop over ``named_parameters()``.

This tree holds parameters and nothing else -- no ``forward``. What llama
*computes* lives in ``iron/applications/llama_3.2_1b/``: the NPU runlists in
``llama_npu.py`` and the torch reference in ``llama_cpu.py``. Giving this class
a third opinion on the same arithmetic would be the duplication the tree is
meant to remove.
"""

import torch
from torch import nn

# Layout differs by phase and belongs to neither the checkpoint nor the model:
# prefill's GEMM wants each projection K-major (hence ``.T``), decode's GEMV
# wants it M-major. Both read the same parameter and transform on upload.


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
        self.layers = nn.ModuleList([Block(cfg, dtype) for _ in range(cfg.n_layers)])
        self.norm = _norm(cfg.emb_dim, dtype)
        # Llama 3.2 ties the output head to the token embedding, so this one
        # parameter is read both to embed a token and to produce logits.
        self.out_head = _proj(cfg.emb_dim, cfg.vocab_size, dtype)

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
