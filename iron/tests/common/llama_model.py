# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A Llama 3.2 model at a size a host test runs in seconds, with random weights."""

import sys
from pathlib import Path

import torch

sys.path.insert(
    0, str(Path(__file__).resolve().parents[2] / "applications" / "llama_3.2_1b")
)
from llama_inference_harness import compute_rope_angles  # noqa: E402


class _Param:
    def __init__(self, tensor):
        self.weight = tensor


class _Attn:
    pass


class _Block:
    def __init__(self, gen, E, H, G, D, F):
        w = lambda *shape, scale: _Param(  # noqa: E731
            (torch.randn(*shape, generator=gen) * scale).to(torch.bfloat16)
        )
        self.norm1, self.norm2 = w(E, scale=0.1), w(E, scale=0.1)
        self.norm1.weight += 1
        self.norm2.weight += 1
        self.attn = _Attn()
        self.attn.q, self.attn.k = w(H * D, E, scale=E**-0.5), w(
            G * D, E, scale=E**-0.5
        )
        self.attn.v, self.attn.o = w(G * D, E, scale=E**-0.5), w(
            E, H * D, scale=(H * D) ** -0.5
        )
        self.ffn = _Attn()
        self.ffn.gate, self.ffn.up = w(F, E, scale=E**-0.5), w(F, E, scale=E**-0.5)
        self.ffn.down = w(E, F, scale=F**-0.5)


class _Model:
    def __init__(self, cfg, seed=0):
        gen = torch.Generator().manual_seed(seed)
        self.layers = [
            _Block(
                gen,
                cfg.emb_dim,
                cfg.n_heads,
                cfg.n_kv_groups,
                cfg.head_dim,
                cfg.hidden_dim,
            )
            for _ in range(cfg.n_layers)
        ]
        self.norm = _Param(
            (1 + 0.1 * torch.randn(cfg.emb_dim, generator=gen)).to(torch.bfloat16)
        )
        self.out_head = _Param(
            (
                torch.randn(cfg.vocab_size, cfg.emb_dim, generator=gen)
                * cfg.emb_dim**-0.5
            ).to(torch.bfloat16)
        )

    def named_parameters(self):
        for i, blk in enumerate(self.layers):
            for path in (
                "norm1",
                "norm2",
                "attn.q",
                "attn.k",
                "attn.v",
                "attn.o",
                "ffn.gate",
                "ffn.up",
                "ffn.down",
            ):
                obj = blk
                for part in path.split("."):
                    obj = getattr(obj, part)
                yield f"layers.{i}.{path}.weight", obj.weight
        yield "norm.weight", self.norm.weight
        yield "out_head.weight", self.out_head.weight


class Config:
    """Llama's shape at a size the reference runs in seconds; a real layout, small.

    The model is what ``DecodeGraph`` and ``llama_cpu`` both read: layers of
    ``norm1/norm2``, ``attn.q/k/v/o`` and ``ffn.gate/up/down`` weights, the
    final norm and the output head, drawn at a seed so both sides see the
    same numbers; ``angles`` is the RoPE table for ``context_length``.
    """

    n_layers, n_heads, n_kv_groups, head_dim = 2, 16, 4, 64
    emb_dim, hidden_dim, vocab_size = 256, 512, 1024
    context_length = 64

    def __init__(self):
        self.model = _Model(self)
        self.angles = compute_rope_angles(self.head_dim, self.context_length).to(
            torch.bfloat16
        )
