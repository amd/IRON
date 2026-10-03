# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reference attention core: ``softmax(q @ k_t) @ v`` for every head at once.

Running it gives the golden output; exporting it gives stream-dse's workload. The caller
transposes ``k_t`` and folds ``1/sqrt(d_head)`` into ``q``. The names below name the ONNX
tensors, the mapping's layers and runtime arguments, and the runtime buffers."""

import math

import torch
from torch import nn

QUERY = "q"
KEY_TRANSPOSED = "k_t"
VALUE = "v"
SCORES = "scores"
PROBABILITIES = "probs"
CONTEXT = "context"

TENSOR_NAMES = (QUERY, KEY_TRANSPOSED, VALUE, SCORES, PROBABILITIES, CONTEXT)

# Node names in the exported graph, in topological order.
SCORES_NODE, SOFTMAX_NODE, CONTEXT_NODE = "Attn_Scores", "Attn_Softmax", "Attn_Context"
NODE_NAMES = [SCORES_NODE, SOFTMAX_NODE, CONTEXT_NODE]

RESULT_NAMES = {SCORES_NODE: SCORES, SOFTMAX_NODE: PROBABILITIES, CONTEXT_NODE: CONTEXT}


class AttentionCore(nn.Module):
    """Each head's scores, softmax and context over a pre-scaled ``q``, heads leading.
    ``causal`` masks on the CPU only; the design's softmax kernel applies the mask itself.
    ``flash`` exports one unnormalised online-softmax step per key block."""

    def __init__(self, causal: bool = False, flash: bool = False):
        super().__init__()
        self.causal = causal
        self.flash = flash

    def forward(self, q, k_t, v):
        if self.flash:
            import iron.common.stream.ops  # noqa: F401  (registers the operator)

            return torch.ops.iron_stream.partial_softmax(q @ k_t) @ v
        scores = q @ k_t
        if self.causal:
            scores = scores + causal_mask(
                scores.shape[-2], scores.shape[-1], scores.dtype
            )
        return torch.softmax(scores, dim=-1) @ v


def causal_mask(seq_q: int, seq_k: int, dtype) -> torch.Tensor:
    """Additive mask: 0 where a query may attend, -inf where it may not."""
    keep = torch.ones(seq_q, seq_k, dtype=torch.bool).tril()
    return torch.where(keep, 0.0, float("-inf")).to(dtype)


def attention_core_module(causal: bool = False, flash: bool = False) -> AttentionCore:
    """The module the design is exported from. It holds no parameters: every operand
    is an activation the sequence hands in."""
    return AttentionCore(causal, flash).eval()


def query_scale(d_head: int) -> float:
    """The factor folded into ``q`` in place of scaling the scores."""
    return 1.0 / math.sqrt(d_head)


def generate_golden_reference(
    seq_len, d_head, heads=1, seed=42, dtype=torch.bfloat16, causal=False
):
    """Golden operands and output, the heads leading and the query already scaled."""
    generator = torch.Generator().manual_seed(seed)
    shape = (heads, seq_len, d_head)
    q = torch.randn(shape, generator=generator).to(dtype) * query_scale(d_head)
    k = torch.randn(shape, generator=generator).to(dtype)
    v = torch.randn(shape, generator=generator).to(dtype)
    k_t = k.transpose(-2, -1).contiguous()
    context = attention_core_module(causal)(q, k_t, v)
    return {QUERY: q, KEY_TRANSPOSED: k_t, VALUE: v, CONTEXT: context}
