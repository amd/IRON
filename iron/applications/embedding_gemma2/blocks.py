# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The Gemma-shaped layer EmbeddingGemma 2's text encoder and vision tower
share: ``geglu``, the GELU-gated feed-forward; ``sandwich``, a block
between two RMS norms with its residual; ``attention``, an encoder's
bidirectional attention over one sequence, its queries and keys RMS-normed
and rotated; and ``sandwich_layer``, attention then the feed-forward, each
between sandwich norms.
"""

from collections.abc import Callable
from functools import partial

from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gelu import GELU
from iron.operators.gemm import GEMM
from iron.operators.mha import MHA
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE


def geglu(x, w_gate, w_up, w_down, **gemm):
    """The GELU-gated feed-forward of ``x``, ``(rows, embedding_dim)``,
    ``W_down @ (GELU(W_gate @ x) * (W_up @ x))``, each projection a GEMM
    with ``gemm``'s keywords reading the weight as stored.
    """
    gate = GELU(GEMM(x, w_gate, b_col_maj=True, **gemm))
    f = ElementwiseMul(gate, GEMM(x, w_up, b_col_maj=True, **gemm))
    return GEMM(f, w_down, b_col_maj=True, **gemm)


def sandwich(x, block: Callable, pre, post, epsilon: float):
    """``x`` plus ``block`` of it between two RMS norms, weighted ``pre``
    before the block and ``post`` after it.
    """
    h = RMSNorm(x, weight=pre, epsilon=epsilon)
    return ElementwiseAdd(x, RMSNorm(block(h), weight=post, epsilon=epsilon))


def attention(
    h,
    angles,
    *,
    q_proj,
    k_proj,
    v_proj,
    o_proj,
    q_norm,
    k_norm,
    heads: int,
    groups: int,
    head_dim: int,
    epsilon: float,
    window: int | None = None,
    **gemm,
):
    """Bidirectional attention over the rows of ``h``, unscaled: ``q_proj``,
    ``k_proj`` and ``v_proj`` project them (GEMMs with ``gemm``'s keywords),
    the queries and keys are RMS-normed by ``q_norm`` and ``k_norm`` and
    rotated by ``angles``, a row each, and the values RMS-normed; ``MHA``
    attends within ``window`` positions if given, over the pipelines the
    profile gives it, and ``o_proj`` projects the heads back. Each weight
    is a checkpoint's ``(out, in)``.
    """
    T, H, G, D = h.shape[0], heads, groups, head_dim
    q = GEMM(h, q_proj, b_col_maj=True, **gemm).reshape(T * H, D)
    k = GEMM(h, k_proj, b_col_maj=True, **gemm).reshape(T * G, D)
    v = GEMM(h, v_proj, b_col_maj=True, **gemm).reshape(T * G, D)
    q = RoPE(RMSNorm(q, weight=q_norm, epsilon=epsilon), angles)
    k = RoPE(RMSNorm(k, weight=k_norm, epsilon=epsilon), angles)
    v = RMSNorm(v, epsilon=epsilon)
    o = MHA(
        q.reshape(T, H, D),
        k.reshape(T, G, D),
        v.reshape(T, G, D),
        heads_interleaved=True,
        kv_interleaved=True,
        causal=False,
        emulate_bf16_mmul_with_bfp16=False,
        window=window,
        scale=1.0,
    )
    return GEMM(o.reshape(T, H * D), o_proj, b_col_maj=True, **gemm)


def sandwich_layer(
    x,
    attend: Callable,
    norms: tuple,
    gate,
    up,
    down,
    epsilon: float,
    **gemm,
):
    """A layer on ``x``: ``attend`` between ``norms``' first two RMS norm
    weights, then the GELU-gated feed-forward (``gate``, ``up``, ``down``,
    GEMMs with ``gemm``'s keywords) between its last two, each with its
    residual.
    """
    x = sandwich(x, attend, norms[0], norms[1], epsilon)
    feed_forward = partial(geglu, w_gate=gate, w_up=up, w_down=down, **gemm)
    return sandwich(x, feed_forward, norms[2], norms[3], epsilon)
