# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.0-H on the shared decoder (``iron.lm``), its shape read from
its checkpoint's ``config.json``.

Granite 4.0-H is Granite's layer (its four scalars, ``GraniteConfig``)
with most layers' attention replaced by a Mamba2 mixer (``Mamba``) and its
feed-forward a shared gated MLP (``SharedMLP``), plus a mixture of experts
where the config has experts (``GraniteMoE``). The attention layers rotate
nothing unless ``position_embedding_type`` is ``"rope"``.

A Mamba2 mixer projects its input to a gate, ``x``, ``B``, ``C`` and a
time step per head; ``x``, ``B`` and ``C`` pass a short causal depthwise
convolution, then a state space scan (``SelectiveScan``); the scan's
output, gated, is RMS-normed and projected back.
The convolution's last rows and the scan's state are the layer's
``Checkpoints`` states, as LFM2's convolution is.
"""

import dataclasses

import numpy as np

import iron
import iron.functional as F
from iron.applications.granite.model import Granite, GraniteConfig, GraniteLayer
from iron.lm import (
    CausalConv1d,
    Checkpoints,
    Linear,
    RMSNorm,
    Weights,
    residual_add,
)
from iron.operators.copy import Copy
from iron.operators.experts import Experts
from iron.operators.router import TopKRouter
from iron.operators.selective_scan import SelectiveScan


@dataclasses.dataclass(frozen=True)
class GraniteHybridConfig(GraniteConfig):
    """``GraniteConfig``, which layers are attention, the Mamba2 mixer's
    shape, the shared MLP's width and the experts, ``intermediate_size``
    wide.
    """

    # transformers' default; __post_init__ sets None but under "rope".
    rope_theta: float | None = dataclasses.field(default=10000.0, kw_only=True)
    layer_types: tuple[str, ...] = dataclasses.field(
        kw_only=True, metadata={"convert": tuple}
    )
    position_embedding_type: str | None = dataclasses.field(default=None, kw_only=True)
    shared_intermediate_size: int = dataclasses.field(kw_only=True)
    num_local_experts: int = dataclasses.field(default=0, kw_only=True)
    num_experts_per_tok: int = dataclasses.field(default=0, kw_only=True)
    mamba_n_heads: int = dataclasses.field(kw_only=True)
    mamba_d_head: int = dataclasses.field(kw_only=True)
    mamba_d_state: int = dataclasses.field(kw_only=True)
    mamba_n_groups: int = dataclasses.field(default=1, kw_only=True)
    mamba_d_conv: int = dataclasses.field(default=4, kw_only=True)

    def __post_init__(self):
        super().__post_init__()
        if len(self.layer_types) != self.num_hidden_layers:
            raise ValueError(
                f"GraniteHybridConfig: {len(self.layer_types)} layer_types for "
                f"{self.num_hidden_layers} layers"
            )
        if self.position_embedding_type != "rope":
            object.__setattr__(self, "rope_theta", None)

    @property
    def conv_channels(self) -> int:
        """A Mamba2 mixer's convolved channels: ``x``, then ``B`` and ``C``."""
        return self.mamba_n_heads * self.mamba_d_head + 2 * (
            self.mamba_n_groups * self.mamba_d_state
        )

    def attends(self, i: int) -> bool:
        """Whether layer ``i`` is attention (``"attention"``, or transformers'
        newer ``"full_attention"``), not Mamba2.
        """
        return self.layer_types[i] in ("attention", "full_attention")


class Mamba(iron.Graph):
    """A Mamba2 mixer on ``c``'s shape: ``in_proj`` to the gate, ``x``,
    ``B``, ``C`` and ``dt``; ``conv1d`` over ``x``, ``B`` and ``C``, then
    silu; the scan; ``norm`` of its output times silu of the gate; and
    ``out_proj``.
    """

    def __init__(self, c: GraniteHybridConfig):
        E, H, K = c.hidden_size, c.mamba_n_heads, c.mamba_d_conv
        self.inner = I = H * c.mamba_d_head
        self.channels = c.conv_channels
        self.groups = c.mamba_n_groups
        self.in_proj = Linear(E, I + self.channels + H, False, precision=c.precision)
        self.conv1d = CausalConv1d(c, self.channels, K, bias=True)
        self.dt_bias, self.A_log, self.D = (iron.param(H) for _ in range(3))
        self.norm = RMSNorm(I, c.eps)
        self.out_proj = Linear(I, E, False, precision=c.precision)
        state = (H, c.mamba_d_head, c.mamba_d_state)
        self.ssm_state = Checkpoints.of(
            state, c.max_seq_len, c.prefill_chunk, np.float32
        )

    def load_state_dict(self, tree, *, path: str = "") -> None:
        super().load_state_dict(tree, path=path)
        # Each head's (dt_bias, A, D) in float32.
        A = -np.exp(np.asarray(self.A_log, np.float32))
        self.head = iron.param(
            np.stack([self.dt_bias, A, self.D], 1).astype(np.float32)
        )

    def body(self, x, call):
        I, C = self.inner, self.channels
        w, p = self.in_proj.weight, self.in_proj.precision
        # Three projections, not one split three ways, as LFM2's conv.
        gate, xbc, dt = (
            F.linear(x, part, precision=p) for part in (w[:I], w[I : I + C], w[I + C :])
        )
        xbc = F.silu(self.conv1d(xbc, call))
        read, write = self.ssm_state.at(call)
        y, final = SelectiveScan.step(
            xbc,
            dt,
            self.head,
            Copy.step(read, dtype=np.float32),
            groups=self.groups,
        )
        Copy.step(final, write, dtype=np.float32)
        return self.out_proj(self.norm(y * F.silu(gate)))


class SharedMLP(iron.Graph):
    """The gated MLP every layer runs: ``input_linear``, the gate's rows
    over the up's, then ``output_linear``.
    """

    def __init__(self, c: GraniteHybridConfig):
        E, S = c.hidden_size, c.shared_intermediate_size
        self.width = S
        self.input_linear = Linear(E, 2 * S, False, precision=c.precision)
        self.output_linear = Linear(S, E, False, precision=c.precision)

    def body(self, x):
        w, S, p = self.input_linear.weight, self.width, self.input_linear.precision
        gate = F.linear(x, w[:S], precision=p)
        up = F.linear(x, w[S:], precision=p)
        return self.output_linear(F.silu(gate) * up)


class Router(iron.Graph):
    """The experts' router: ``layer``, a linear to a logit per expert."""

    def __init__(self, c: GraniteHybridConfig):
        self.layer = Linear(
            c.hidden_size, c.num_local_experts, False, precision=c.precision
        )


class GraniteMoE(iron.Graph):
    """A mixture of experts: ``router``, then ``Experts`` over the
    checkpoint's stacked ``input_linear`` (each expert's gate over its up)
    and ``output_linear``.
    """

    def __init__(self, c: GraniteHybridConfig):
        X, E, M = c.num_local_experts, c.hidden_size, c.intermediate_size
        self.router = Router(c)
        self.input_linear = Weights(weight=(X, 2 * M, E))
        self.output_linear = Weights(weight=(X, E, M))
        self.top_k = c.num_experts_per_tok

    def body(self, x):
        gate_up, down = self.input_linear.weight, self.output_linear.weight
        layer = self.router.layer
        logits = F.linear(x, layer.weight, precision=layer.precision)
        ids, weights = TopKRouter.step(logits, top_k=self.top_k)
        return Experts.step(x, ids, weights, gate_up, down)


class GraniteHybridLayer(GraniteLayer):
    """Granite's layer, ``mamba`` in attention's place where the layer is
    Mamba2, its feed-forward ``shared_mlp`` plus ``block_sparse_moe`` where
    the config has experts.
    """

    def __init__(self, c: GraniteHybridConfig, i: int):
        super().__init__(c, i)
        del self.mlp
        self.shared_mlp = SharedMLP(c)
        self.block_sparse_moe = GraniteMoE(c) if c.num_local_experts else None
        self.mamba = None
        if not c.attends(i):
            del self.self_attn, self.cache
            self.mamba = Mamba(c)

    def mix(self, h, call):
        return super().mix(h, call) if self.mamba is None else self.mamba(h, call)

    def body(self, x, call):
        x = residual_add(
            x, self.mix(self.input_layernorm(x), call), self.residual_multiplier
        )
        h = self.post_attention_layernorm(x)
        y = self.shared_mlp(h)
        if self.block_sparse_moe is not None:
            y = self.block_sparse_moe(h) + y
        return residual_add(x, y, self.residual_multiplier)


class GraniteHybrid(Granite):
    """Granite 4.0-H on ``config``'s shape and a checkpoint's ``weights``,
    from its sharded checkpoint and ``tokenizer.json``.
    """

    config = GraniteHybridConfig
    profile = None
    layer_class = GraniteHybridLayer
