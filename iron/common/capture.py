# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Ergonomic authoring front-end for :class:`~iron.common.sequence.OperatorSequence`.

``OperatorSequence.runlist`` is a hand-authored list of ``(operator, *buffer_name)``
tuples, with buffer names manually threaded (and sometimes aliased in place) between
steps -- see ``iron/applications/llama_3.2_1b/llama_npu.py``. :func:`capture` records
that same runlist from ordinary eager Python calls instead:

    with capture() as g:
        h1 = g(relu_op, g(gemm1_op, x, w1))
        logits = g(gemm2_op, h1, w2)
    seq = g.build("mnist_mlp").compile()

Nodes are linked by Python object identity, not by name, so the recorded runlist is a
plain topologically-ordered list -- fan-out (two calls reading the same value) and
fan-in (one call reading two earlier results) work without any extra bookkeeping,
since capture order is a valid topological order for free (Python cannot reference a
value before it is produced).

This module only builds the ``runlist``/``input_args``/``output_args`` triple
``OperatorSequence`` already consumes -- it adds no compilation or dispatch logic of
its own.
"""

from __future__ import annotations

import itertools
from contextlib import contextmanager


def _spec_bytes(spec):
    """Bytes one runtime argument occupies, from the shape the operator declares."""
    import numpy as np

    return int(np.prod(spec.shape)) * np.dtype(spec.dtype).itemsize


class Traced:
    """Placeholder for a tensor produced during graph capture.

    Carries no data -- it only stands in for a captured value so later calls can
    refer back to it. It does carry ``shape`` and ``dtype`` when they are known,
    which is what lets the next operator in the graph be built for the shapes it
    will actually see.
    """

    __slots__ = ("name", "shape", "dtype")

    def __init__(self, name, shape=None, dtype=None):
        self.name, self.shape, self.dtype = name, shape, dtype

    def __repr__(self):
        extent = f"{list(self.shape)}" if self.shape is not None else "?"
        return f"Traced({self.name!r}, {extent})"


class Graph:
    """A captured operator graph: an ordered runlist plus the buffer names
    :class:`~iron.common.sequence.OperatorSequence` needs.

    Do not construct directly; use :func:`capture`.
    """

    def __init__(self):
        self.runlist = []
        self._names = {}  # id(value) -> buffer name
        self._keepalive = {}  # id(value) -> value, so id() cannot be reused
        self._counter = itertools.count()
        self._produced = {}  # buffer name -> True, insertion-ordered
        self._consumed = {}  # buffer name -> True, insertion-ordered
        self._pinned = set()  # names the host addresses, never pooled

    def input(self, tensor, name=None):
        """Register an existing tensor as a named top-level input.

        Optional: any value used in a recorded call is auto-registered as a
        fresh input on first sight. Use this when a specific, stable buffer
        name (e.g. ``"x"``) is preferred over an auto-generated one.
        """
        name = name or self._fresh_name(None)
        self._track(tensor, name)
        return Traced(name)

    def named(self, name, shape=None, dtype=None):
        """A handle for a buffer the host addresses by an explicit name.

        Weights, caches, and the sequence's own inputs and outputs are filled
        and read host-side via ``get_buffer(name)``, so their names are part of
        the interface and must be pinned. Values produced by a recorded call
        are named automatically instead.
        """
        self._pinned.add(name)
        return Traced(name, shape, dtype)

    def slice(self, tensor, start, end):
        """Reference byte range ``[start:end)`` of an existing top-level buffer.

        Mirrors ``OperatorSequence``'s own ``"buffer_name[start:end]"`` slice
        notation (see ``calculate_buffer_layout``) -- e.g. per-head views into
        one parent attention buffer, as in ``llama_3.2_1b/llama_npu.py``'s
        decode runlist. ``tensor`` must resolve to a plain (unsliced) buffer
        name; slicing a slice is not supported (``OperatorSequence`` doesn't
        resolve nested slices either).
        """
        return Traced(f"{self._resolve(tensor)}[{start}:{end}]")

    def __call__(self, operator, *args):
        """Record one call to ``operator`` and return its output placeholder(s).

        ``args`` is either just the operator's inputs (a fresh output buffer is
        auto-allocated per declared "out"/"inout" arg spec, and returned) or the
        full positional argument list including pre-allocated output(s) (mirrors
        ``OperatorSequence``'s own raw calling convention, and is how in-place
        steps -- same buffer for input and output -- are expressed).
        """
        specs = operator.get_arg_spec()
        n_out = sum(1 for s in specs if s.writes)
        n_in = len(specs) - n_out

        if len(args) == n_in:
            in_names = [self._resolve(a) for a in args]
            # The operator already declares the shape of everything it writes,
            # so a recorded value knows its own shape without a second rule.
            out_specs = [s for s in specs if s.writes]
            outputs = [
                Traced(self._fresh_name(operator), spec.shape, spec.dtype)
                for spec in out_specs[:n_out]
            ]
            for out in outputs:
                self._track(out, out.name)
            out_names = [out.name for out in outputs]
        elif len(args) == len(specs):
            in_names = [self._resolve(a) for a in args[:n_in]]
            out_names = [self._resolve(a) for a in args[n_in:]]
            outputs = list(args[n_in:])
        else:
            raise TypeError(
                f"{type(operator).__name__} takes {n_in} input(s), optionally "
                f"followed by {n_out} pre-allocated output(s); got {len(args)} "
                "positional argument(s)"
            )

        self.runlist.append((operator, *in_names, *out_names))
        for name in in_names:
            self._consumed.setdefault(name, True)
        for name in out_names:
            self._produced.setdefault(name, True)

        return outputs[0] if len(outputs) == 1 else tuple(outputs)

    def infer_io(self):
        """Infer ``(input_args, output_args)`` from the recorded runlist.

        A buffer no recorded step ever produced is an input; a buffer no
        recorded step ever consumes (again) is an output. Split out from
        :meth:`build` so this pure bookkeeping is testable without
        constructing a real :class:`OperatorSequence` (which requires real
        ``MLIROperator`` instances, not test doubles).
        """
        input_args = [n for n in self._consumed if n not in self._produced]
        output_args = [n for n in self._produced if n not in self._consumed]
        return input_args, output_args

    def build(self, name, **kwargs):
        """Build the :class:`~iron.common.sequence.OperatorSequence` for this
        captured graph.

        ``input_args``/``output_args`` default to :meth:`infer_io` when not
        passed explicitly. Any other ``OperatorSequence`` keyword
        (``dispatch``, ``buffer_sizes``, ``context``, ...) is forwarded as-is.

        Imports :class:`~iron.common.sequence.OperatorSequence` lazily, so
        recording a graph (everything above this method) never requires the
        ``aie``/``pyxrt`` toolchain -- only building one for real does.
        """
        from .sequence import OperatorSequence

        inferred_inputs, inferred_outputs = self.infer_io()
        input_args = kwargs.pop("input_args", inferred_inputs)
        output_args = kwargs.pop("output_args", inferred_outputs)
        if kwargs.pop("pool_scratch", True):
            kwargs.setdefault("buffer_offsets", self.infer_buffer_offsets())
        return OperatorSequence(name, self.runlist, input_args, output_args, **kwargs)

    def infer_buffer_offsets(self):
        """Offsets that let intermediates whose lifetimes are disjoint overlap.

        Only values the recorder named itself are placed. Anything the caller
        named is addressed by the host -- weights, caches, the graph's own
        inputs and outputs -- so it keeps a private address.
        """
        from .allocator import live_ranges, plan

        sizes, steps = {}, []
        for op, *bufs in self.runlist:
            reads, writes = [], []
            for buf, spec in zip(bufs, op.get_arg_spec()):
                sizes.setdefault(buf, _spec_bytes(spec))
                (reads if spec.reads else writes).append(buf)
                if spec.reads and spec.writes:
                    writes.append(buf)
            steps.append((reads, writes))

        poolable = live_ranges(
            steps, pinned=self._pinned | {b for b in sizes if "[" in b}
        )
        allocations, _ = plan(poolable, sizes)
        return {name: a.offset for name, a in allocations.items()}

    def _fresh_name(self, operator):
        prefix = type(operator).__name__.lower() if operator is not None else "in"
        return f"{prefix}{next(self._counter)}"

    def _track(self, value, name):
        self._names[id(value)] = name
        self._keepalive[id(value)] = value

    def _resolve(self, value):
        # A Traced is its own name, regardless of which object returned it
        # (an auto-allocated output, or the wrapper g.input() hands back) --
        # resolving it by identity would require that exact wrapper object to
        # be reused, which callers have no reason to do.
        if isinstance(value, Traced):
            return value.name
        key = id(value)
        if key not in self._names:
            self._track(value, self._fresh_name(None))
        return self._names[key]


@contextmanager
def capture():
    """Context manager that records eager operator calls into a :class:`Graph`.

    Example::

        with capture() as g:
            h1 = g(relu_op, g(gemm1_op, x, w1))
            logits = g(gemm2_op, h1, w2)
        seq = g.build("mnist_mlp").compile()
    """
    yield Graph()
