#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-30B-A3B, a small mixture of experts, on the shared decoder
(``iron.lm``), its shape read from its checkpoint's ``config.json``.

Qwen3-MoE is Qwen3's layer with its feed-forward a mixture of experts
(``SparseMoE``): a router picks each token's ``num_experts_per_tok``
experts and weighs them by a softmax over their logits alone, which is
``TopKRouter``'s; the chosen experts' feed-forwards are ``Experts``, which
has no kernel yet. Its output head is untied.
"""

import dataclasses

import numpy as np

import iron
import iron.functional as F
from iron.applications.qwen3.model import Qwen3Layer
from iron.lm import CausalLM, DecoderConfig, Linear
from iron.lm.blocks import GatedMLP
from iron.operators.experts import Experts
from iron.operators.router import TopKRouter


@dataclasses.dataclass(frozen=True)
class Qwen3MoeConfig(DecoderConfig):
    """``DecoderConfig`` and its experts: every layer's feed-forward a
    mixture, its chosen experts' weights normalized, as Qwen3-MoE's
    checkpoints have them. ``Qwen3MoeConfig`` refuses any other.
    """

    num_experts: int = dataclasses.field(kw_only=True)
    num_experts_per_tok: int = dataclasses.field(kw_only=True)
    moe_intermediate_size: int = dataclasses.field(kw_only=True)
    norm_topk_prob: bool = dataclasses.field(default=False, kw_only=True)
    decoder_sparse_step: int = dataclasses.field(default=1, kw_only=True)
    mlp_only_layers: tuple[int, ...] = dataclasses.field(
        default=(), kw_only=True, metadata={"convert": tuple}
    )
    tie_word_embeddings: bool = False

    def __post_init__(self):
        super().__post_init__()
        if not self.norm_topk_prob:
            raise ValueError(
                "Qwen3MoeConfig: TopKRouter normalizes the chosen experts' "
                "weights; no operator weighs them unnormalized"
            )
        if self.decoder_sparse_step != 1 or self.mlp_only_layers:
            raise ValueError(
                f"Qwen3MoeConfig: decoder_sparse_step {self.decoder_sparse_step} "
                f"and mlp_only_layers {self.mlp_only_layers} make some layers "
                "dense; here every layer's feed-forward is a mixture"
            )


class SparseMoE(iron.Graph):
    """A mixture of experts on ``c``'s shape: ``gate``, the router, and
    ``experts``, each a gated feed-forward ``moe_intermediate_size`` wide,
    stacked once they load.
    """

    def __init__(self, c: Qwen3MoeConfig):
        self.gate = Linear(c.hidden_size, c.num_experts)
        expert = dataclasses.replace(c, intermediate_size=c.moe_intermediate_size)
        self.experts = [GatedMLP(expert) for _ in range(c.num_experts)]
        self.top_k = c.num_experts_per_tok

    def load_state_dict(self, tree, path: str = "") -> None:
        super().load_state_dict(tree, path)
        # As transformers stacks them: each expert's gate over its up.
        self.gate_up = np.stack(
            [
                np.concatenate([e.gate_proj.weight, e.up_proj.weight])
                for e in self.experts
            ]
        )
        self.down = np.stack([e.down_proj.weight for e in self.experts])

    def body(self, x):
        n, experts = x.shape[0], self.gate.weight.shape[0]
        logits = F.linear(x, self.gate.weight).reshape(n, experts)
        ids, weights = TopKRouter.step(logits, top_k=self.top_k)
        return Experts.step(x, ids, weights, self.gate_up, self.down)


class Qwen3MoeLayer(Qwen3Layer):
    """Qwen3's layer, its feed-forward ``SparseMoE``."""

    def __init__(self, c: Qwen3MoeConfig, i: int):
        super().__init__(c, i)
        self.mlp = SparseMoE(c)


class Qwen3Moe(CausalLM):
    """Qwen3-MoE on ``config``'s shape and a checkpoint's ``weights``, from
    its checkpoint and ``tokenizer.json``.
    """

    config = Qwen3MoeConfig
    layer_class = Qwen3MoeLayer
