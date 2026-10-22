# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-30B-A3B, a small mixture of experts, on the shared decoder
(``iron.lm``), its shape read from its checkpoint's ``config.json``.

Qwen3-MoE is Qwen3's layer with its feed-forward a mixture of experts
(``SparseMoE``): a router picks each token's ``num_experts_per_tok``
experts and weighs them by a softmax over their logits alone, which is
``TopKRouter``'s. Its output head is untied.

The experts stay in the mapped checkpoint, 58 GB of them at 30B. Between
the router and the experts the host copies the ones a call chose into
states every layer shares (``SparseMoE.stage``), so the device holds only
those and the page cache whichever the host read lately. The staged
experts run as one gated feed-forward, each row's routing weights
scaling its experts' activations and zero at the others'.
"""

import dataclasses
from pathlib import Path

import numpy as np

import iron
import iron.functional as F
from iron import Precision
from iron.applications.qwen3.model import Qwen3Layer
from iron.common.graph.handle import State
from iron.lm import CausalLM, DecoderConfig, GatedMLP, Linear, activation
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


@dataclasses.dataclass(frozen=True)
class Staged:
    """The experts a call of ``rows`` rows is staged in, each ``width`` wide
    in a slot of its own: ``gate`` and ``up`` stacked as one projection's
    rows, ``down`` as one's columns, and ``routed``, each row's routing
    weight for each slot over that slot's columns.
    """

    gate: State
    up: State
    down: State
    routed: State

    @classmethod
    def of(cls, rows: int, slots: int, width: int, hidden: int) -> "Staged":
        n = slots * width
        return cls(
            iron.state((n, hidden)),
            iron.state((n, hidden)),
            iron.state((hidden, n)),
            iron.state((rows, n)),
        )


class SparseMoE(iron.Graph):
    """A mixture of experts on ``c``'s shape: ``gate``, the router, and
    ``experts``, each a gated feed-forward ``moe_intermediate_size`` wide,
    left in the checkpoint. ``Qwen3Moe`` gives every layer's ``staged``,
    the experts a call stages, by its rows.
    """

    staged: dict[int, Staged]

    def __init__(self, c: Qwen3MoeConfig):
        self.gate = Linear(c.hidden_size, c.num_experts, bias=False)
        expert = dataclasses.replace(c, intermediate_size=c.moe_intermediate_size)
        self.experts = [GatedMLP(expert) for _ in range(c.num_experts)]
        self.top_k = c.num_experts_per_tok
        self.width = c.moe_intermediate_size
        self.act = activation(c.hidden_act)

    def body(self, x):
        n, experts = x.shape[0], self.gate.weight.shape[0]
        logits = F.linear(x, self.gate.weight).reshape(n, experts)
        ids, weights = TopKRouter.step(logits, top_k=self.top_k)
        s = self.staged[n]
        iron.on_host(self.stage, ids, weights, writes=(s.gate, s.up, s.down, s.routed))
        # A prompt chunk's staged experts are 98304 wide at 30B, past what
        # flm.ProjectionGEMM's per-call transfers fit in one descriptor.
        p = Precision.HIGHEST
        h = self.act(F.linear(x, s.gate, precision=p)) * F.linear(x, s.up, precision=p)
        routed = s.routed[: x.valid[0]] if x.valid else s.routed
        return F.linear(h * routed.reshape(h.shape), s.down, precision=p)

    def stage(self, ids, weights, gate, up, down, routed) -> None:
        """Copy the experts ``ids`` chose into ``gate``, ``up`` and ``down``, a
        slot each, and each of ``ids``' rows' ``weights`` into ``routed`` at
        its experts' slots, zero at the others. A slot none chose keeps the
        expert it held, which no row weighs.
        """
        chosen, slots = np.unique(ids, return_inverse=True)
        I, n = self.width, len(ids)
        for slot, e in enumerate(chosen):
            expert, at = self.experts[e], slice(slot * I, (slot + 1) * I)
            gate[at] = expert.gate_proj.weight
            up[at] = expert.up_proj.weight
            down[:, at] = expert.down_proj.weight
        routed[:n] = 0
        rows = np.arange(n)[:, None]
        routed[:n].reshape(n, -1, I)[rows, slots.reshape(ids.shape)] = weights[
            :, ::2, None
        ]


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
    profile = Path(__file__).with_name("profiles")

    def __init__(self, config: Qwen3MoeConfig, weights):
        super().__init__(config, weights)
        c = config
        H, I, K = c.hidden_size, c.moe_intermediate_size, c.num_experts_per_tok
        staged = {
            rows: Staged.of(rows, min(c.num_experts, rows * K), I, H)
            for rows in (1, c.prefill_chunk)
        }
        for layer in self.layers:
            layer.mlp.staged = staged
