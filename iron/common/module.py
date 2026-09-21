# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A module: several graph functions over one buffer plan (OPERATOR_MODEL_PLAN.md §8).

Two graphs that close over the same tensors and the same state objects
compile together: one allocation for weights, state and intermediates
across both, weights uploaded once, state shared because it is the same
bytes, one image with one entry point per graph::

    llama = iron.compile(dev, prefill=(prefill, dict(tokens=(MAX, E), angles=(MAX, D))),
                              decode=(decode, dict(x=(1, E), angles=(1, D))))
    llama.prefill(tok, ang, n=len(prompt))
    logits = llama.decode(x, ang, pos=p)

Each graph is traced on its own; what the module adds is names. A graph's
private buffers (inputs, outputs, intermediates) are prefixed with its
name so two graphs' locals never collide, a weight keeps one name across
graphs (the first graph's, by tensor identity), and a state already has
one (its own). The runlists concatenate into one sequence over one layout:
intermediates pool by live range as before, and pooling across graphs is
safe because a call runs one graph and only pinned buffers outlive it.

Under a full ELF the fused module carries one runtime sequence per graph,
named for it, over the same three arenas (spike S4's construction), and
the loader addresses each as ``main:<name>``. Under an xclbin the chained
per-step image runs each graph's own range of steps.
"""

from __future__ import annotations

from .graph import CompiledGraph, GraphFunction, TracedGraph, _EntryCallable


class CompiledModule:
    """The compiled graphs, as attributes named for them."""

    def __init__(self, graphs: dict[str, CompiledGraph], sequence, plan, image):
        self._graphs = dict(graphs)
        self.sequence = sequence
        self.plan = plan
        self.image = image

    def __getattr__(self, name):
        graphs = self.__dict__.get("_graphs", {})
        if name in graphs:
            return graphs[name]
        raise AttributeError(f"module has no graph {name!r}; it has {sorted(graphs)}")

    @property
    def graphs(self) -> dict[str, CompiledGraph]:
        return dict(self._graphs)


def trace_module(name: str, **graphs) -> tuple[TracedGraph, dict[str, tuple[int, int]]]:
    """Trace each graph and join them: one traced graph, and each one's step range.

    ``graphs`` maps a name to ``(GraphFunction, shapes)``. The joined trace's
    inputs, outputs and values are every graph's, in order, its steps the
    concatenation, its pinned buffers the union; ``ranges`` says which steps
    are which graph's.
    """
    traced: dict[str, TracedGraph] = {}
    for gname, (fn, shapes) in graphs.items():
        if not isinstance(fn, GraphFunction):
            raise TypeError(f"{gname}: expected a graph function, got {fn!r}")
        traced[gname] = fn.trace(**dict(shapes))
    _share_names(traced)
    steps, inputs, outputs, values, bindings = [], [], [], [], []
    pinned, weights, states, ranges = {}, {}, {}, {}
    for gname, t in traced.items():
        ranges[gname] = (len(steps), len(steps) + len(t.steps))
        steps += t.steps
        inputs += t.inputs
        outputs += t.outputs
        values += t.values
        bindings += t.bindings
        pinned.update(t.pinned)
        for key, entry in t.weights.items():
            weights.setdefault(key, entry)
        states.update(t.states)
    for gname, t in traced.items():
        if len({v.name for v in values}) != len(values):
            raise ValueError(
                f"{name}: two graphs declare a per-call value of the same name; "
                f"a module's values are one namespace"
            )
    joined = TracedGraph(name, steps, inputs, outputs, values, pinned, weights, states, bindings)
    joined.parts = traced
    joined.ranges = ranges
    return joined, ranges


def _share_names(traced: dict[str, TracedGraph]) -> None:
    """Prefix each graph's private handles; give a shared weight one name."""
    weight_names: dict[int, str] = {}
    for gname, t in traced.items():
        for key, (tensor, h) in t.weights.items():
            if key in weight_names:
                h.name = weight_names[key]
            else:
                weight_names[key] = h.name
        private = set()
        for h in t.inputs + t.outputs:
            private.add(id(h))
        for step in t.steps:
            for h in step.slots:
                base = h.parent if h.parent is not None else h
                if base.role in ("input", "output", "intermediate"):
                    private.add(id(base))
        seen = set()
        for step in t.steps:
            for h in step.slots:
                base = h.parent if h.parent is not None else h
                if id(base) in private and id(base) not in seen:
                    seen.add(id(base))
                    base.name = f"{gname}.{base.name}"
        for h in t.inputs + t.outputs:
            if id(h) not in seen:
                seen.add(id(h))
                h.name = f"{gname}.{h.name}"
        # pinned is keyed by name: rebuild it after the renaming
        t.pinned = _pinned(t)


def _pinned(t: TracedGraph) -> dict:
    pinned = {}
    for _, h in t.weights.values():
        pinned[h.name] = h.nbytes
    for h in t.states.values():
        pinned[h.name] = h.nbytes
    for step in t.steps:
        for h in step.inputs + step.outputs:
            if h.parent is not None and h.parent.role == "intermediate":
                pinned.setdefault(h.parent.name, h.parent.nbytes)
    return pinned


def compile(dev=None, *, image=None, boundaries=None, context=None, verbose=False, **graphs):
    """Compile several graph functions as one module; see the module docstring.

    ``graphs`` maps each entry point's name to ``(graph_function, shapes)``.
    The image is chosen per module by the §8 rules over every graph's values
    (``iron.common.packaging``): the full ELF on NPU2 with one sequence per
    graph, else the per-step xclbin chain running each graph's steps.
    """
    import aie.utils as aie_utils

    from .packaging import each_step, plan

    if not graphs:
        raise TypeError("compile() needs at least one graph: name=(graph_function, shapes)")
    if dev is not None:
        aie_utils.set_current_device(dev)
    if boundaries not in (None, each_step):
        raise NotImplementedError(
            "a module packages as one full ELF or as the per-step xclbin chain; "
            "chunks(n) applies to a single graph"
        )
    joined, ranges = trace_module("+".join(graphs), **graphs)
    chosen = plan(aie_utils.get_current_device().resolve().name, joined, boundaries, image)
    if chosen.image != "elf" and chosen.dispatch != "separate":
        # xclbin with no boundaries: the module runs per step, not as chunks.
        chosen = plan(aie_utils.get_current_device().resolve().name, joined, each_step, image)
    if verbose:
        print(chosen.report(joined.name))
    sequence = joined.sequence(dispatch=chosen.dispatch, context=context)
    sequence.entries = {name: joined.parts[name].runlist for name in ranges}
    sequence.ranges = ranges
    sequence.compile()
    compiled = {}
    for gname, t in joined.parts.items():
        compiled[gname] = CompiledGraph(
            t, sequence=sequence, callable=_EntryCallable(sequence, gname, ranges[gname])
        )
        compiled[gname].plan = chosen
    return CompiledModule(compiled, sequence, chosen, sequence.image)
