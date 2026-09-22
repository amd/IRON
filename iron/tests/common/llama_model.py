# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2's shape at a size a host test runs in seconds, on the real tree."""

import torch

from iron.applications.llama_3_2_1b.model import Llama, rope_angles


class Config:
    """Llama's shape, small, with the parameter tree drawn at a seed.

    ``model`` is :class:`iron.applications.llama_3_2_1b.model.Llama` at these dimensions, so the
    graphs, the forward and the checkpoint loader all read one tree;
    ``angles`` is the RoPE table for ``context_length``.
    """

    n_layers, n_heads, n_kv_groups, head_dim = 2, 16, 4, 64
    emb_dim, hidden_dim, vocab_size = 256, 512, 1024
    context_length = 64

    def __init__(self, seed=0):
        torch.manual_seed(seed)
        self.model = Llama(self).requires_grad_(False)
        self.angles = rope_angles(self.head_dim, self.context_length).to(torch.bfloat16)


class Llama1B(Config):
    """Llama 3.2 1B's real shape with unset weights: for builds, not numbers.

    The tree is made on the meta device and given storage without writing
    it, so the 2.5 GB is mapped and never touched."""

    n_layers, n_heads, n_kv_groups, head_dim = 16, 32, 8, 64
    emb_dim, hidden_dim, vocab_size = 2048, 8192, 128256
    context_length = 2048

    def __init__(self):
        with torch.device("meta"):
            model = Llama(self)
        self.model = model.to_empty(device="cpu").requires_grad_(False)
        self.angles = rope_angles(self.head_dim, self.context_length).to(torch.bfloat16)
