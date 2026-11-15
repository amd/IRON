# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What stream-dse solves for flash attention over every head, causal or not.

The torch module the workload is exported from, which gives stream-dse the
graph and its shapes, and its mapping: each layer's kernel arguments, the three
layers fused into one group. Placement and the query and key blocks are
stream-dse's; the mapping seeds the search at blocks the kernels compile.
"""

from functools import cache

from iron.common.stream.mapping import FusedGroup, StreamMapping

from .op import CONTEXT, LAYERS, SCORES, SOFTMAX


def flash_attention_module():
    """Return the graph of flash attention as a ``torch.nn.Module``.

    ``partial_softmax(q @ k_t) @ v`` per head, heads leading, over a
    pre-scaled ``q`` and a pre-transposed ``k_t``. The module gives stream-dse
    the three layers and their shapes, not the arithmetic: the mask, the
    running max and sum and the division are the kernels', so the softmax is
    an elementwise node whose key axis stream-dse is free to block. torch is
    imported here, when a workload is exported, and not with the operator.
    """
    from torch import nn  # pyright: ignore[reportMissingImports]

    from iron.common.stream import ops

    class FlashAttention(nn.Module):
        def forward(self, q, k_t, v):
            return ops.partial_softmax(q @ k_t) @ v

    return FlashAttention().eval()


@cache
def workload(heads: int, seq_len: int, d_head: int):
    """Return the workload exported at one problem size, its nodes named ``op.LAYERS``."""
    import torch  # pyright: ignore[reportMissingImports]

    from iron.common.stream.workload import export_workload

    def zeros(*shape):
        return torch.zeros((heads, *shape), dtype=torch.bfloat16)

    return export_workload(
        flash_attention_module(),
        (zeros(seq_len, d_head), zeros(d_head, seq_len), zeros(seq_len, d_head)),
        node_names=LAYERS,
    )


def mapping(
    query_block: int, key_block: int, d_head: int, causal: bool
) -> StreamMapping:
    """Return the mapping of the three layers as one fused group, the tile search seeded at ``query_block``.

    ``causal`` is each layer's: the score GEMM skips the blocks past the
    diagonal, and the flash kernels are built with the mask. The score GEMM
    multiplies in bf16 (``Precision.HIGH``), as mha.cc's QK^T in IRON's MHA.
    """

    def gemm(m, k, n, **flags):
        return dict(m=m, k=k, n=n, layout="default", **flags)

    kernels = {
        SCORES: gemm(query_block, d_head, key_block, causal=causal, precision="high"),
        SOFTMAX: dict(m=query_block, n=key_block, layout="contiguous", causal=causal),
        CONTEXT: gemm(query_block, key_block, d_head, flash=True, causal=causal),
    }
    return StreamMapping(kernels, [FusedGroup(LAYERS)])
