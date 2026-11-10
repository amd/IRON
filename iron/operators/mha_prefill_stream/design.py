# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What stream-dse solves for flash attention over every head, causal or not.

The torch module the workload is exported from, one online-softmax step
per key block, and its mapping: each layer's kernel arguments, the three
layers fused into one group. Placement and the query and key blocks are
stream-dse's; the mapping seeds the search at blocks the kernels compile.
"""

# stream-dse, torch and onnxscript are requirements_stream.txt's.
# pyright: reportMissingImports=false

from functools import cache

import torch
from torch import nn

from iron.common.stream import ops
from iron.common.stream.mapping import FusedGroup
from iron.common.stream.workload import export_workload

from .op import CONTEXT, LAYERS, RESULTS, SCORES, SOFTMAX


class FlashAttention(nn.Module):
    """``softmax(q @ k_t) @ v`` per head, heads leading, one key block at a time.

    Over a pre-scaled ``q`` and a pre-transposed ``k_t``. The mask, the
    running max and sum and the division are the kernels', so the
    graph sees an elementwise step whose key axis is free to be blocked.
    """

    def forward(self, q, k_t, v):
        return ops.partial_softmax(q @ k_t) @ v


@cache
def workload(heads: int, seq_len: int, d_head: int):
    """Return the workload exported at one problem size, named as ``op`` names it."""

    def zeros(*shape):
        return torch.zeros((heads, *shape), dtype=torch.bfloat16)

    return export_workload(
        FlashAttention().eval(),
        (zeros(seq_len, d_head), zeros(d_head, seq_len), zeros(seq_len, d_head)),
        node_names=list(LAYERS),
        result_names=RESULTS,
    )


def mapping(query_block: int, key_block: int, d_head: int, causal: bool):
    """Return the kernel arguments and the one fused group, the search seeded at ``query_block``.

    ``causal`` is each layer's: the score GEMM skips the blocks past the
    diagonal, and the flash kernels are built with the mask.
    """

    def gemm(m, k, n, **flags):
        return dict(m=m, k=k, n=n, layout="default", **flags)

    kernels = {
        SCORES: gemm(query_block, d_head, key_block, causal=causal),
        SOFTMAX: dict(m=query_block, n=key_block, layout="contiguous", causal=causal),
        CONTEXT: gemm(query_block, key_block, d_head, flash=True, causal=causal),
    }
    return kernels, [FusedGroup("Fused_Group_1", LAYERS)]
