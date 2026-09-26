# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graph functions: a graph is a Python function traced on handles.

Inputs are its positional parameters, outputs its return values, weights
what it closes over, state an :func:`state` object created outside, and
per-call scalars its keyword-only parameters annotated ``Scratchpad[T]`` or
``DispatchTime[T]``. Operators are called on handles: ``GEMV(w, h)`` infers
its extents from its arguments (operators with one ``array_key`` share an
array), and an explicit instance ``q(w, h)`` is applied the same way.

    kv = [iron.state((n_kv, MAX, head_dim)) for _ in range(n_layers)]

    @iron.graph
    def decode(x, angles, *, pos: Scratchpad[np.int32]):
        h = RMSNorm(x, model.norm.weight)
        k = RoPE(GEMV(wk, h), angles)
        Copy(k, kv[0][:, pos])
        return GEMV(wo, h)

    net = decode.compile(dev, x=(1, emb), angles=(1, head_dim))
    logits = net(x_tok, ang_tok, pos=n)

Tracing produces a :class:`TracedGraph`: the runlist, the buffer names and
sizes, the value bindings. It is pure bookkeeping and needs no toolchain.
:meth:`GraphFunction.compile` hands that to :class:`OperatorSequence` for
the image (a fused ELF on NPU2, per-step xclbins on NPU1) and returns a
:class:`CompiledGraph` to call. Calling an uncompiled graph with real
tensors compiles for their shapes, prints a note, and dispatches.
"""

from .compiled import CompiledGraph, GraphFunction, graph
from .handle import Handle, Value, is_operand, state
from .trace import TracedGraph, Tracer, current

__all__ = [
    "CompiledGraph",
    "GraphFunction",
    "Handle",
    "TracedGraph",
    "Tracer",
    "Value",
    "current",
    "graph",
    "is_operand",
    "state",
]
