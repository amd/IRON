#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LFM2-1.2B over the shared decoder and layer (``iron.lm``): its short
convolution on the NPU (``Lfm2``) and in float32 (``Lfm2Oracle``), and
LFM2-1.2B's shape, read from its checkpoint's
``config.json``. Run it with ``python -m iron.applications.lfm2.model``.

Sixteen layers, only six of them full attention (``full_attn_idxs``),
each ``Layer``'s on LFM2's own names (per-head q/k norms, Qwen3's shape);
the rest are a gated short causal depthwise convolution
(``conv_L_cache=3`` taps) in place of attention, then ``Layer``'s
feed-forward block. A conv layer holds no ``self_attn``, so ``layer()``
takes ``Layer``'s whole layer where the checkpoint holds one.

A conv layer's three per-channel taps, a row each (``iron.lm.Derived``,
once at load), read a window that spans the current call and the
``conv_kernel - 1`` gated rows before it. Those rows are the layer's
``Checkpoints`` state (``iron.lm``), a slot per chunk boundary, so a
prompt may resume from any chunk (a chat turn), after positions a decode
step wrote; slot 0, never written, is zero, "before the sequence".

The operators' tunables are the graph's profile, ``profiles/<device>.json``.
"""

import dataclasses
from pathlib import Path

import numpy as np

import iron
import iron.functional as F
from iron import lm
from iron.lm import (
    CausalLM,
    Checkpoints,
    DecoderConfig,
    Derived,
    Layer,
    Oracle,
    widen,
)
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul, RowwiseMul
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm


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
        F = self.block_ff_dim
        if self.auto_adjust_ff_dim:
            F = int(2 * F / 3)
            if self.ffn_dim_multiplier is not None:
                F = int(self.ffn_dim_multiplier * F)
            F = self.multiple_of * -(-F // self.multiple_of)
        object.__setattr__(self, "intermediate_size", F)


class Lfm2Oracle(Oracle):
    """LFM2-1.2B's forward pass in float32, on the host."""

    def layer(self, i, angles, w, x):
        if "self_attn" in vars(w):
            return super().layer(i, angles, w, x)
        x = x + self._conv(self.normed(x, w.operator_norm), w.conv)
        return self.config.layer(i).feed_forward_oracle(self, w, x)

    def _conv(self, h, w):
        c = self.config
        n, E, K = h.shape[0], h.shape[1], c.conv_kernel
        bcx = h @ w.in_proj.weight.T
        b, cc, x = bcx[:, :E], bcx[:, E : 2 * E], bcx[:, 2 * E :]
        gated = b * x
        taps = w.conv.weight.reshape(E, K)
        padded = np.concatenate([np.zeros((K - 1, E), dtype=np.float32), gated], axis=0)
        total = np.zeros((n, E), dtype=np.float32)
        for k in range(K):
            total += taps[:, k] * padded[k : k + n]
        return (cc * total) @ w.out_proj.weight.T

    def head(self, x):
        norm = widen(self.weights.model.embedding_norm.weight)
        return self.rms_norm(x, norm) @ self.embedding.T


class Lfm2(CausalLM):
    """LFM2-1.2B on ``config``'s shape and a checkpoint's ``weights``, by
    its names: each layer either an attention layer's weights or a conv
    layer's, distinguished by which the checkpoint gives it. Every matrix
    is read ``(out, in)``, as the checkpoint ships it.
    """

    profile = Path(__file__).with_name("profiles")
    oracle = Lfm2Oracle

    def __init__(self, config: Lfm2Config, weights):
        super().__init__(config, weights)
        E, K, C = config.hidden_size, config.conv_kernel, config.prefill_chunk
        derived = Derived(weights)
        for i, w in enumerate(self.layers):
            if "conv" in vars(w):
                tail = Checkpoints.of((K - 1, E), config.max_seq_len, C)
                self.recurrent[i] = {"conv": tail}
                # A row per tap, each the row RowwiseMul takes.
                conv = w.conv.conv
                taps = conv.weight.reshape(E, K).T
                derived.put(conv, taps=np.ascontiguousarray(taps))
        self.derived = derived.tree()
        # The rows before a call end block 0; a chunk's rows are block 1.
        self.conv_window = iron.state((2, C, E))
        self.conv_tail = iron.state((K - 1, E))

    def layer(self, step, i, w, x):
        """Layer ``i``: an attention layer is ``Layer``'s; a conv layer its
        short conv in attention's place, then ``Layer``'s feed-forward.
        """
        if "self_attn" in vars(w):
            return super().layer(step, i, w, x)
        layer = self.config.layer(i)
        x = layer.add(x, self.conv(step, i, w.conv, layer.norm(x, w.operator_norm)))
        return layer.feed_forward(w, x)

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
            F.linear(h, *part).reshape(n, E)
            for part in Layer.cut(w.in_proj, (0, E, 2 * E, 3 * E))
        )
        gated = ElementwiseMul.step(b, x)
        tap = self.derived.model.layers[i].conv.conv.taps
        read, write = self.recurrent[i]["conv"].at(step)
        flat = self.conv_window.reshape(2 * C, E)
        first = C - (K - 1)
        Copy.step(read, flat[first:C])
        if step.prompt:
            Copy.step(gated, self.conv_window[1, : step.rows])
            total = RowwiseMul.step(flat[first : first + C], tap[0])
            for k in range(1, K):
                total = ElementwiseAdd.step(
                    total, RowwiseMul.step(flat[first + k : first + k + C], tap[k])
                )
            total = total[: step.rows]
            for j in range(K - 1):
                Copy.step(flat[first + step.rows + j], self.conv_tail[j])
            Copy.step(self.conv_tail, write)
        else:
            Copy.step(gated.reshape(E), flat[C])
            total = RowwiseMul.step(gated, tap[K - 1])
            for k in range(K - 1):
                prior = RowwiseMul.step(flat[first + k : first + k + 1], tap[k])
                total = ElementwiseAdd.step(total, prior)
            Copy.step(flat[first + 1 : C + 1], write)
        y = ElementwiseMul.step(cc, total)
        return F.linear(y, w.out_proj.weight)

    def head(self, x):
        return GEMV.step(
            self.weights.model.embed_tokens.weight,
            RMSNorm.step(
                x,
                weight=self.weights.model.embedding_norm.weight,
                epsilon=self.config.eps,
            ),
        )


class Runner(lm.Runner):
    """LFM2-1.2B, from its checkpoint and ``tokenizer.json``."""

    config = Lfm2Config
    model = Lfm2
    bos = 1


if __name__ == "__main__":
    lm.main(Runner, "LFM2-1.2B on the NPU")
