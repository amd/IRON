# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.0-H on the shared decoder (``iron.lm``), its shape read from its checkpoint's ``config.json``.

This package ships the dense sizes only; a checkpoint with experts is
refused (``num_local_experts``).

Granite 4.0-H is Granite's layer (its four scalars, ``GraniteConfig``)
with most layers' attention replaced by a Mamba2 mixer (``Mamba``) and
its feed-forward a shared gated MLP (``SharedMLP``). The attention
layers rotate nothing unless ``position_embedding_type`` is ``"rope"``.
A Mamba2 mixer's convolution and state-space scan (``SelectiveScan``)
carry state between calls as ``Checkpoints``.
"""

import dataclasses
from pathlib import Path

import numpy as np

import iron
import iron.functional as F
from iron.applications.granite.model import Granite, GraniteConfig, GraniteLayer
from iron.lm import (
    CausalConv1d,
    Checkpoints,
    Linear,
    RMSNorm,
    main,
    residual_add,
)
from iron.operators.copy import Copy
from iron.operators.selective_scan import SelectiveScan


@dataclasses.dataclass(frozen=True)
class GraniteHybridConfig(GraniteConfig):
    """``GraniteConfig``, which layers are attention, the Mamba2 mixer's shape and the shared MLP's width.

    A checkpoint with experts (``num_local_experts``) is refused; this
    package ships the dense sizes only.
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
        if self.num_local_experts:
            raise ValueError(
                f"GraniteHybridConfig: num_local_experts {self.num_local_experts}, "
                "this package ships the dense sizes only"
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
        """Whether layer ``i`` is attention (``"attention"``, or transformers' newer ``"full_attention"``), not Mamba2."""
        return self.layer_types[i] in ("attention", "full_attention")


class Mamba(iron.Graph):
    """A Mamba2 mixer on ``c``'s shape.

    ``in_proj`` to the gate, ``x``, ``B``, ``C`` and ``dt``; ``conv1d``
    over ``x``, ``B`` and ``C``, then silu; the scan; ``norm`` of its
    output times silu of the gate; and ``out_proj``.
    """

    def __init__(self, c: GraniteHybridConfig):
        E, H, K = c.hidden_size, c.mamba_n_heads, c.mamba_d_conv
        self.inner = d_inner = H * c.mamba_d_head
        self.channels = c.conv_channels
        self.groups = c.mamba_n_groups
        self.in_proj = Linear(
            E, d_inner + self.channels + H, False, precision=c.precision
        )
        self.conv1d = CausalConv1d(c, self.channels, K, bias=True)
        self.dt_bias, self.A_log, self.D = (iron.param(H) for _ in range(3))
        self.norm = RMSNorm(d_inner, c.eps)
        self.out_proj = Linear(d_inner, E, False, precision=c.precision)
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
        d_inner, C = self.inner, self.channels
        w, p = self.in_proj.weight, self.in_proj.precision
        gate, xbc, dt = (
            F.linear(x, part, precision=p)
            for part in (w[:d_inner], w[d_inner : d_inner + C], w[d_inner + C :])
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
    """The gated MLP every layer runs.

    ``input_linear``, the gate's rows over the up's, then ``output_linear``.
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


class GraniteHybridLayer(GraniteLayer):
    """Granite's layer, ``mamba`` in attention's place where the layer is Mamba2, its feed-forward ``shared_mlp``."""

    def __init__(self, c: GraniteHybridConfig, i: int):
        super().__init__(c, i)
        del self.mlp
        self.shared_mlp = SharedMLP(c)
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
        return residual_add(x, y, self.residual_multiplier)


class GraniteHybrid(Granite):
    """Granite 4.0-H on ``config``'s shape and a checkpoint's ``weights``, from its checkpoint and ``tokenizer.json``."""

    config = GraniteHybridConfig
    profile = Path(__file__).with_name("profiles")
    layer_class = GraniteHybridLayer


if __name__ == "__main__":
    main(GraniteHybrid)
