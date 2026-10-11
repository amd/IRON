# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2's text encoder in float32 on the host, the oracle the
NPU encoder is judged by, and its tokenizer and task prompts.
"""

from collections.abc import Mapping
from types import SimpleNamespace

import numpy as np
from tokenizers import Tokenizer

from iron.lm import Oracle, rope_angles

from .model import Config

PROMPTS = {
    "BitextMining": "task: search result | query: ",
    "Classification": "task: classification | query: ",
    "Clustering": "task: clustering | query: ",
    "CodeRetrieval": "task: code retrieval | query: ",
    "Document": "title: none | text: ",
    "FactChecking": "task: fact checking | query: ",
    "InstructionRetrieval": "task: code retrieval | query: ",
    "MultilabelClassification": "task: classification | query: ",
    "PairClassification": "task: sentence similarity | query: ",
    "QuestionAnswering": "task: question answering | query: ",
    "Reranking": "task: search result | query: ",
    "Retrieval": "task: search result | query: ",
    "Retrieval-document": "title: none | text: ",
    "Retrieval-query": "task: search result | query: ",
    "STS": "task: sentence similarity | query: ",
    "SearchQuery": "task: search result | query: ",
    "SentenceSimilarity": "task: sentence similarity | query: ",
    "Summarization": "task: sentence similarity | query: ",
    "document": "title: none | text: ",
    "query": "task: search result | query: ",
}


def tokenizer(path) -> Tokenizer:
    """The tokenizer of `path`, a `tokenizer.json`; its `encode` adds BOS and EOS."""
    return Tokenizer.from_file(str(path))


def tokens(
    tokenizer: Tokenizer,
    config: Config,
    text: str,
    task: str,
    audio_tokens: int = 0,
    image_tokens: int = 0,
) -> list[int]:
    """`text` behind `task`'s prompt (`PROMPTS`), with BOS and EOS, each
    `<|audio|>` and `<|image|>` in it a run of that many placeholders
    between its markers, as the processor expands them.
    """
    c, out = config, []
    runs = {
        c.audio_token: [c.boa, *[c.audio_token] * audio_tokens, c.eoa],
        c.image_token: [c.boi, *[c.image_token] * image_tokens, c.eoi],
    }
    for t in tokenizer.encode(PROMPTS[task] + text).ids:
        out += runs.get(t, [t])
    return out


def rms_norm(x, w, eps):
    return (
        x * np.power(np.mean(x * x, axis=-1, keepdims=True) + eps, np.float32(-0.5)) * w
    )


def gelu_tanh(x):
    c = np.float32(np.sqrt(2 / np.pi))
    return np.float32(0.5) * x * (1 + np.tanh(c * (x + np.float32(0.044715) * x**3)))


class EmbeddingGemmaOracle:
    """EmbeddingGemma 2's text encoder in float32, on the host.

    Args:
        config: The encoder's shape.
        weights: The tree `load_weights` gives over `layout(config)`.
    """

    def __init__(self, config: Config, weights: SimpleNamespace):
        self.config = config
        # Widened by the rows a call looks up: the whole table in float32 is 512 MB.
        self.embedding = weights.embedding
        self.norm, self.projection, self.ple, self.ple_norm = (
            vars(weights)[k].astype(np.float32)
            for k in ("norm", "projection", "ple", "ple_norm")
        )
        self.layers = [
            SimpleNamespace(**{k: v.astype(np.float32) for k, v in vars(w).items()})
            for w in weights.layers
        ]

    def layer(self, i: int, angles: np.ndarray, w: SimpleNamespace, x, ple):
        """Layer `i` on `x` `(n, emb_dim)`, with its per-layer input `ple`
        `(n, ple_dim)` and the RoPE table `angles` of its head size.
        """
        c, n = self.config, x.shape[0]
        H, (G, D) = c.n_heads, c.heads(i)
        h = rms_norm(x, w.norm1, c.eps)
        q = rms_norm((h @ w.q.T).reshape(n, H, D), w.q_norm, c.eps)
        k = rms_norm((h @ w.k.T).reshape(n, G, D), w.k_norm, c.eps)
        v = rms_norm((h @ w.v.T).reshape(n, G, D), np.float32(1), c.eps)
        q, k = Oracle.rotate(q, angles), Oracle.rotate(k, angles)
        window = None if i in c.global_layers else c.sliding_window
        a = self.attend(q, k, v, window) @ w.o.T
        x = x + rms_norm(a, w.norm2, c.eps)
        h = rms_norm(x, w.norm3, c.eps)
        f = (gelu_tanh(h @ w.gate.T) * (h @ w.up.T)) @ w.down.T
        x = x + rms_norm(f, w.norm4, c.eps)
        p = (gelu_tanh(x @ w.ple_gate.T) * ple) @ w.ple_proj.T
        return (x + rms_norm(p, w.ple_norm, c.eps)) * w.scalar

    @staticmethod
    def attend(q, k, v, window: int | None):
        """Bidirectional attention of `q` `(n, H, D)` over `k`, `v` `(n, G, D)`,
        unscaled; with a `window`, a key at most `window` positions away.
        """
        n, H, D = q.shape
        k, v = (np.repeat(a, H // a.shape[1], axis=1) for a in (k, v))
        p = q.transpose(1, 0, 2) @ k.transpose(1, 2, 0)
        if window is not None:
            pos = np.arange(n)
            p[:, np.abs(pos[:, None] - pos[None, :]) > window] = -np.inf
        p -= p.max(axis=-1, keepdims=True)
        np.exp(p, out=p)
        p /= p.sum(axis=-1, keepdims=True)
        return (p @ v.transpose(1, 0, 2)).transpose(1, 0, 2).reshape(n, H * D)

    def token_states(self, tokens, soft: Mapping[int, np.ndarray] = {}) -> np.ndarray:
        """Each token's `(n, out_dim)` output, before pooling.

        Args:
            tokens: The token ids.
            soft: Each placeholder id's soft tokens `(k, emb_dim)`, the
                `k` placeholders' embeddings in order.

        Raises:
            ValueError: A placeholder's count is not its soft tokens'.
        """
        c = self.config
        tokens = np.asarray(tokens, dtype=np.int64).reshape(-1)
        n = tokens.size
        # Hugging Face rounds the scale to the weights' dtype: 22.625 in bfloat16 only.
        x = self.embedding[tokens].astype(np.float32) * np.float32(np.sqrt(c.emb_dim))
        for token, rows in soft.items():
            at = tokens == token
            if at.sum() != len(rows):
                raise ValueError(
                    f"{at.sum()} placeholders {token} for {len(rows)} soft tokens"
                )
            x[at] = rows
        ple = (x @ self.ple.T) * np.float32(c.emb_dim**-0.5)
        ple = rms_norm(ple.reshape(n, c.n_layers, c.ple_dim), self.ple_norm, c.eps)
        angles = {
            False: rope_angles(c.sliding_head_dim, n, c.sliding_rope_base),
            True: rope_angles(c.global_head_dim, n, c.global_rope_base),
        }
        for i, w in enumerate(self.layers):
            x = self.layer(i, angles[i in c.global_layers], w, x, ple[:, i])
        return rms_norm(x, self.norm, c.eps) @ self.projection.T

    def __call__(
        self, tokens, dims: int | None = None, soft: Mapping[int, np.ndarray] = {}
    ) -> np.ndarray:
        """The embedding of `tokens`, with `soft` as `token_states` takes it:
        the mean of their states, its first `dims` L2-normalized.
        """
        e = self.token_states(tokens, soft).mean(axis=0)[:dims]
        return e / np.linalg.norm(e)
