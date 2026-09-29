# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graphs: a ``Graph`` subclass's ``body`` traced on handles.

Inputs are ``body``'s positional parameters, outputs its return values,
weights and state (an ``state``) what the instance holds, named by
attribute path (a weight the body indexes or reshapes is a
``weight``), and per-call scalars its keyword-only parameters
annotated ``Scratchpad[T]`` or ``DispatchTime[T]``. An input defaulting to
``None`` may be left out; the version traced without it sees ``None``. A
``Carried[T]`` value is one the graph computes for its own next call: the
body returns the next values last, ``return logits, iron.carry(pos=pos +
1)``, and a call returns them as numbers; on a full ELF the device can
compute them itself and loop (``CarriedLoop``). Operators are called on handles:
``GEMV(w, h)`` infers its extents from its arguments (operators with one
``array_key`` share an array), and an explicit instance ``q(w, h)`` is
applied the same way.

    class Decode(iron.Graph):
        def __init__(self, w):
            self.w = w
            self.kv = iron.state((n_kv, MAX, head_dim))

        def body(self, x, angles, *, pos: Scratchpad[np.int32]):
            h = RMSNorm(x, weight=self.w.norm)
            k = RoPE(GEMV(self.w.k, h), angles)
            Copy(k, self.kv[:, pos])
            return GEMV(self.w.o, h)

    net = Decode(w).compile(dev, x=(1, emb), angles=(1, head_dim))
    logits = net(x_tok, ang_tok, pos=n)

Tracing produces a ``TracedGraph``: the runlist, the buffer names and
sizes, the value bindings. It is pure bookkeeping and needs no toolchain.
``Graph.compile`` hands that to ``OperatorSequence`` for
the image (a fused ELF on NPU2, per-step xclbins on NPU1) and returns a
``CompiledGraph`` to call. Calling an uncompiled graph with real
tensors compiles for their shapes, prints a note, and dispatches.
"""

from .carried import CarriedLoop
from .compiled import CompiledGraph, Graph
from .handle import Carry, Handle, Value, carry, is_operand, state, weight
from .trace import TracedGraph, Tracer

__all__ = [
    "CarriedLoop",
    "Carry",
    "CompiledGraph",
    "Graph",
    "Handle",
    "TracedGraph",
    "Tracer",
    "Value",
    "carry",
    "is_operand",
    "state",
    "weight",
]
