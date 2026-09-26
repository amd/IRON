# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graph functions: a graph is a Python function traced on handles.

Inputs are its positional parameters, outputs its return values, weights
what it closes over, state an :func:`state` object created outside, and
per-call scalars its keyword-only parameters annotated ``Scratchpad[T]`` or
``DispatchTime[T]`` (an operator may be bound to an integer expression of
one, ``pos * head_dim``, which is computed per call). A ``Carried[T]`` value
is one the graph computes for its own next call: it returns the next values
last, ``return logits, iron.carry(pos=pos + 1)``, and a call returns them as
numbers. An input defaulting to ``None`` may be left out; the version
without it sees ``None``. Operators are called on handles: ``GEMV(w, h)`` infers
its overlay and extent from its arguments (deduplicating overlays by
``design_key``), and an explicit instance ``q(w, h)`` is applied the same way.

    kv = [iron.state((n_kv, MAX, head_dim)) for _ in range(n_layers)]

    @iron.graph
    def decode(x, angles, *, pos: Scratchpad[np.int32]):
        h = RMSNorm(x, model.norm.weight)
        k = RoPE(GEMV(wk, h), angles)
        StridedCopy(k, kv[0], out_offset=pos)
        return GEMV(wo, h)

    net = decode.compile(dev, x=(1, emb), angles=(1, head_dim))
    logits = net(x_tok, ang_tok, pos=n * head_dim)

Tracing produces a :class:`TracedGraph`: the runlist, the buffer names and
sizes, the value bindings. It is pure bookkeeping and needs no toolchain.
:meth:`GraphFunction.compile` hands that to :class:`OperatorSequence` for
the image (a fused ELF on NPU2, per-step xclbins on NPU1) and returns a
:class:`CompiledGraph` to call. Calling an uncompiled graph with real
tensors compiles for their shapes, says so once, and dispatches.
"""

from .carried import CarriedLoop
from .compiled import CompiledGraph, GraphFunction, graph
from .handle import Affine, Carry, Handle, State, Value, carry, is_operand, state
from .trace import TracedGraph, TracedStep, Tracer, current, handle_of

__all__ = [
    "Affine",
    "Carry",
    "CarriedLoop",
    "CompiledGraph",
    "GraphFunction",
    "Handle",
    "State",
    "TracedStep",
    "TracedGraph",
    "Tracer",
    "Value",
    "carry",
    "current",
    "graph",
    "handle_of",
    "is_operand",
    "state",
]
