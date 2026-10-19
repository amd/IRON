# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A recorded graph drawn as Graphviz text (``Recording.dot()``)."""

from __future__ import annotations

import html
import re
from collections import defaultdict
from typing import TYPE_CHECKING

from .handle import Handle

if TYPE_CHECKING:
    from .record import Recording

# A buffer of layer N: its weights, a tower's too (vision.layers.N.q), and a
# decoder's caches.
LAYERED = re.compile(r"(?:^|\.)(?:layers|keys|values)\.(\d+)(?:\.|$)")


def layers(recording: Recording) -> dict[int, int | None]:
    """Each step's layer, by step index (``layers.3.q`` and
    ``vision.layers.3.q`` are layer 3). A step reading no layer's buffer is
    in the layer of what it reads, else of what reads it; before the first
    layer, and after the last where it holds a weight or state of no layer
    (a head), it is in none.
    """
    steps = recording.steps
    own = {}
    for i, s in enumerate(steps):
        found = [LAYERED.search(h.root.name) for h in s.inputs + s.outputs]
        own[i] = next((int(m.group(1)) for m in found if m), None)
    placed = [i for i, n in own.items() if n is not None]
    layer, made = {}, {}
    for i, s in enumerate(steps):
        layer[i] = own[i]
        held = any(h.root.role in ("weight", "state") for h in s.inputs + s.outputs)
        if own[i] is None and placed and placed[0] < i and (i < placed[-1] or not held):
            found = [made.get(h.root.name) for h in s.inputs]
            layer[i] = max((n for n in found if n is not None), default=None)
        for h in s.outputs:
            made[h.root.name] = layer[i]
    # One reading only a slice of a shared tensor and what came before
    # the layers (a per-layer projection) is in the layer of its readers.
    read: dict[str, int] = {}
    for i in reversed(range(len(steps))):
        s = steps[i]
        if layer[i] is None and placed and placed[0] < i < placed[-1]:
            found = [read.get(h.root.name) for h in s.outputs]
            layer[i] = min((n for n in found if n is not None), default=None)
        if layer[i] is not None:
            for h in s.inputs:
                read[h.root.name] = layer[i]
    return layer


def _shape(h: Handle) -> str:
    return "×".join(str(n) for n in h.shape) or "1"


def _box(recording: Recording, i: int, values: dict[int, list[str]]) -> str:
    """Step ``i``'s label: its operator, its outputs' shapes and its
    per-call values.
    """
    s = recording.steps[i]
    op = s.op
    lines = [f"<b>{html.escape(type(op).__name__)}</b>"]
    shapes = ", ".join(_shape(h) for h in s.outputs if h.root.role != "state")
    if shapes:
        lines.append(shapes)
    lines += [f"<i>{html.escape(v)}</i>" for v in values.get(id(op), [])]
    return "<br/>".join(lines)


def dot(recording: Recording) -> str:
    """``recording`` as Graphviz text: a box per step, clustered by layer, an
    edge per operand labelled with its shape (and ``bounded`` where a
    per-call value bounds or indexes it), and a node per input, weight,
    state and output.
    """
    steps = recording.steps
    layer = layers(recording)
    writer = {}
    for i, s in enumerate(steps):
        for h in s.outputs:
            if h.root.role in ("intermediate", "output"):
                writer[h.root.name] = i
    values = defaultdict(list)
    for b in recording.bindings:
        values[id(b.op)].append(f"{b.member.name} = {b.expression}")

    nodes: dict[int | None, list[str]] = defaultdict(list)
    edges: list[str] = []
    named: set[str] = set()

    def source(h: Handle, at: int | None) -> str:
        r = h.root
        if r.name in writer:
            return f"s{writer[r.name]}"
        node = f"b_{r.name}"
        if node not in named:
            named.add(node)
            shape = {"weight": "note", "state": "cylinder"}.get(r.role, "ellipse")
            nodes[None if r.role == "input" else at].append(
                f'  "{node}" [shape={shape}, label=<{html.escape(r.name)}<br/>'
                f"{_shape(r)} {r.role}>];"
            )
        return node

    for i, s in enumerate(steps):
        nodes[layer[i]].append(
            f'  "s{i}" [shape=box, style=rounded, '
            f"label=<{_box(recording, i, values)}>];"
        )
        for h in s.inputs:
            bounded = " bounded" if h.bounds or h.index_by is not None else ""
            edges.append(
                f'  "{source(h, layer[i])}" -> "s{i}" [label="{_shape(h)}{bounded}"];'
            )
        for h in s.outputs:
            if h.root.role == "state":
                edges.append(
                    f'  "s{i}" -> "{source(h, layer[i])}" [label="write {_shape(h)}"];'
                )
    returned = {h.root.name for h in recording.returned}
    for h in recording.outputs:
        r = h.root
        if r.name not in writer:
            continue
        kind = "returned" if r.name in returned else "carried"
        nodes[None].append(
            f'  "o_{r.name}" [shape=doubleoctagon, '
            f"label=<{html.escape(r.name)}<br/>{_shape(r)} {kind}>];"
        )
        edges.append(f'  "s{writer[r.name]}" -> "o_{r.name}";')
        for name, nxt in recording.carry.items():
            if isinstance(nxt, Handle) and nxt.root.name == r.name:
                nodes[None].append(
                    f'  "v_{name}" [shape=plain, '
                    f"label=<<i>{html.escape(name)}</i>, next call>];"
                )
                edges.append(f'  "o_{r.name}" -> "v_{name}" [style=dotted];')

    out = [
        "digraph G {",
        f"  graph [label=<{html.escape(recording.name)}>, labelloc=t];",
        *nodes.pop(None, []),
    ]
    for n, lines in nodes.items():
        out.append(f'  subgraph "cluster_layer{n}" {{')
        out.append(f'    label="layer {n}";')
        out += ["  " + line for line in lines]
        out.append("  }")
    return "\n".join([*out, *edges, "}"])
