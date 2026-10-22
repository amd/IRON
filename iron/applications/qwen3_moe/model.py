# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-30B-A3B, a small mixture of experts, on the shared decoder
(``iron.lm``), its shape read from its checkpoint's ``config.json``.

Qwen3-MoE is Qwen3's layer with its feed-forward a mixture of experts
(``SparseMoE``): a router picks each token's ``num_experts_per_tok``
experts and weighs them by a softmax over their logits alone, which is
``TopKRouter``'s; the chosen experts' feed-forwards are ``Experts``. Its
output head is untied.

The experts stay in the mapped checkpoint, 58 GB of them at 30B: between
the router and ``Experts`` the host copies the ones a call chose into a
state every layer shares (``SparseMoE.stage``), so the device holds only
those and the page cache whichever the host read lately.
"""

import dataclasses

import numpy as np

import iron
import iron.functional as F
from iron.applications.qwen3.model import Qwen3Layer
from iron.common.graph.handle import State
from iron.lm import CausalLM, DecoderConfig, GatedMLP, Linear
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
    left in the checkpoint. ``Qwen3Moe`` gives every layer's the states a
    call's chosen experts are staged in: ``gate_up`` and ``down``, a slot
    per expert as transformers stacks them, and ``ids``, each row's choices
    by slot.
    """

    gate_up: State
    down: State
    ids: State

    def __init__(self, c: Qwen3MoeConfig):
        self.gate = Linear(c.hidden_size, c.num_experts, bias=False)
        expert = dataclasses.replace(c, intermediate_size=c.moe_intermediate_size)
        self.experts = [GatedMLP(expert) for _ in range(c.num_experts)]
        self.top_k = c.num_experts_per_tok

    def body(self, x):
        n, experts = x.shape[0], self.gate.weight.shape[0]
        logits = F.linear(x, self.gate.weight).reshape(n, experts)
        ids, weights = TopKRouter.step(logits, top_k=self.top_k)
        slots = min(experts, n * self.top_k)
        staged = (self.gate_up[:slots], self.down[:slots], self.ids[:n])
        iron.on_host(self.stage, ids, writes=staged)
        return Experts.step(x, staged[2], weights, *staged[:2])

    def stage(self, ids, gate_up, down, staged) -> None:
        """Copy the experts ``ids`` chose into ``gate_up`` and ``down``, a slot
        each, and each row's choices by slot into ``staged``; a row past
        ``ids``' takes slot 0.
        """
        chosen, slots = np.unique(ids, return_inverse=True)
        width = down.shape[2]
        for slot, e in enumerate(chosen):
            expert = self.experts[e]
            gate_up[slot, :width] = expert.gate_proj.weight
            gate_up[slot, width:] = expert.up_proj.weight
            down[slot] = expert.down_proj.weight
        staged[: len(ids)] = slots.reshape(ids.shape)
        staged[len(ids) :] = 0


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

    def __init__(self, config: Qwen3MoeConfig, weights):
        super().__init__(config, weights)
        c = config
        H, I, K = c.hidden_size, c.moe_intermediate_size, c.num_experts_per_tok
        slots = min(c.num_experts, c.prefill_chunk * K)
        gate_up, down = iron.state((slots, 2 * I, H)), iron.state((slots, H, I))
        ids = iron.state((c.prefill_chunk, K), np.int32)
        for layer in self.layers:
            layer.mlp.gate_up, layer.mlp.down, layer.mlp.ids = gate_up, down, ids
