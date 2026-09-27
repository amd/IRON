# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3 on the CPU: the forward pass the NPU is judged by.

:class:`Reference` is the model as a plain float32 causal pass over one
token sequence, with no cache: the logits at position ``t`` of a causal pass
over ``t + 1`` tokens are what a cached decode produces at step ``t``. It
is written here rather than composed from the operators' references on
purpose: the graph's reference defines what the graph computes, so only an
independent forward can catch a wiring mistake, a transposed layout or a
softmax over the wrong length. It is the oracle of the graph on the host
(``iron/tests/common/llama_reference.py``) and of the accuracy check
(:func:`iron.applications.common.accuracy`).
"""

from types import SimpleNamespace

import numpy as np

# Llama's RMSNorm epsilon.
EPS = np.float32(1e-5)


class Reference:
    """Llama 3's forward pass in float32, on ``config``'s shape and RoPE
    table and ``weights``, as :class:`.npu.Llama` takes them.

    The NPU's bf16 table is rounded from the same float32 one. The weights
    are widened to float32 once, here (exactly: every bf16 is a float32),
    which for the 1B model is 5 GB.
    """

    def __init__(self, config, weights):
        self.config = config
        self.embedding = weights.embedding.astype(np.float32)
        self.norm = weights.norm.astype(np.float32)
        self.layers = [
            SimpleNamespace(**{f: a.astype(np.float32) for f, a in vars(lw).items()})
            for lw in weights.layers
        ]
        self.angles = config.angles()

    def logits(self, tokens) -> np.ndarray:
        """The logits after the last of ``tokens`` (``(n,)``), ``(vocab_size,)``,
        each token attending to itself and those before it.
        """
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        c = self.config
        (n,), H, G, D = tokens.shape, c.n_heads, c.n_kv_groups, c.head_dim
        cos = self.angles[:n, None, ::2]
        sin = self.angles[:n, None, 1::2]

        def rope(x):
            """Rotate the two halves of each ``(n, heads, D)`` row by its position."""
            x1, x2 = x[..., : D // 2], x[..., D // 2 :]
            return np.concatenate([x1 * cos - x2 * sin, x1 * sin + x2 * cos], axis=-1)

        def rms_norm(x, w):
            return x / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + EPS) * w

        causal = np.triu(np.full((n, n), -np.inf, dtype=np.float32), k=1)
        scale = np.float32(1 / np.sqrt(D))
        x = self.embedding[tokens]
        for lw in self.layers:
            h = rms_norm(x, lw.norm1)
            q = rope((h @ lw.q.T).reshape(n, H, D))
            # Each key and value head serves H // G consecutive query heads.
            k = np.repeat(rope((h @ lw.k.T).reshape(n, G, D)), H // G, axis=1)
            v = np.repeat((h @ lw.v.T).reshape(n, G, D), H // G, axis=1)
            scores = np.einsum("qhd,khd->hqk", q, k) * scale + causal
            p = np.exp(scores - scores.max(axis=-1, keepdims=True))
            p /= p.sum(axis=-1, keepdims=True)
            x = x + np.einsum("hqk,khd->qhd", p, v).reshape(n, H * D) @ lw.o.T
            h = rms_norm(x, lw.norm2)
            gate = h @ lw.gate.T
            # SiLU, with the sigmoid as a tanh, which does not overflow.
            silu = gate * np.float32(0.5) * (1 + np.tanh(gate * np.float32(0.5)))
            x = x + (silu * (h @ lw.up.T)) @ lw.down.T
        return rms_norm(x[-1], self.norm) @ self.embedding.T
