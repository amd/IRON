# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pictures of a graph: its trace, and what compile and the tuner made of it.

A ``Dataflow`` reads the live objects (a ``TracedGraph``, and for a compiled
version its ``Plan``, ``Artifacts`` and ``Tuning``) and draws one box per
step, an edge per buffer between steps, weights as notes, states as
cylinders and the graph's inputs and outputs as ovals. ``dot()`` is the
Graphviz text, ``svg()`` runs Graphviz's ``dot`` on it, and ``html()`` is one
self-contained page of that SVG that pans, zooms and shows a clicked step's
operator, tunables and per-call values. ``TracedGraph.dot()`` and
``CompiledGraph.dot()`` (and their ``svg()`` and ``html()``) are these.

A compiled version's boxes name the design each step runs and the steps
folded into it; a tuned one's, the tunables the tuner moved, and its packs
are clusters. Given a ``CostTable``, each box shows the step time the table
prices it at. ``side_by_side`` draws two in one picture: a graph as traced
beside the same graph tuned.
"""

from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
from collections import defaultdict
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from ..declare import Operator, Unresolvable
from .handle import Handle
from .narrowing import cost_key

if TYPE_CHECKING:
    from .compiled import CompiledGraph
    from .narrowing import CostTable, Tuning
    from .trace import TracedGraph

INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"
HAIRLINE = "#e1e0d9"
AXIS = "#c3c2b7"
SURFACE = "#fcfcfb"

# One hue per family, in a fixed order that keeps adjacent hues apart for
# color-blind readers; an operator not listed in FAMILY is "other".
FAMILIES = {
    "matmul": "#2a78d6",
    "attention": "#eb6834",
    "norm": "#1baf7a",
    "elementwise": "#eda100",
    "data movement": "#e87ba4",
    "sampling": "#008300",
    "signal": "#6250d6",
    "other": "#e34948",
}
FAMILY = {
    "GEMV": "matmul",
    "GEMM": "matmul",
    "MHA": "attention",
    "GQAScores": "attention",
    "GQAContext": "attention",
    "Softmax": "attention",
    "RMSNorm": "norm",
    "LayerNorm": "norm",
    "ElementwiseAdd": "elementwise",
    "ElementwiseMul": "elementwise",
    "RowwiseMul": "elementwise",
    "SiLU": "elementwise",
    "GELU": "elementwise",
    "RoPE": "elementwise",
    "AXPY": "elementwise",
    "Clamp": "elementwise",
    "Tanh": "elementwise",
    "Sigmoid": "elementwise",
    "ReLU": "elementwise",
    "LeakyReLU": "elementwise",
    "Copy": "data movement",
    "Transpose": "data movement",
    "Repeat": "data movement",
    "Split3": "data movement",
    "Merge": "data movement",
    "Sample": "sampling",
    "Emit": "sampling",
    "DepthwiseConv1d": "signal",
    "Magnitude": "signal",
    "Log": "signal",
    "Resample": "signal",
    "Limbs": "signal",
    "Dequant": "signal",
}

# A buffer of layer N: its weights, and a decoder's caches.
LAYERED = re.compile(r"^(?:layers|keys|values|ple)\.(\d+)\b")


class Dataflow:
    """A traced graph, or a compiled version of one, as a picture.

    Args:
        traced: The graph's trace; a compiled version's is the graph it built,
            its folds applied and its designs narrowed.
        title: The caption.
        layers: The layers drawn, by index (``layers.3.q`` is layer 3), or
            None for every step. A step reading no layer's buffer is in the
            layer of what it reads, or in none before the first layer and
            after the last.
        weights: Draw each weight as its own node; else name it in the box
            of the step reading it.
        version: The compiled version ``traced`` is of: each box names its
            design and the steps folded into it, a tuned version's moved
            tunables and packs too.
        table: Each box shows the step time this table prices its design at.
    """

    def __init__(
        self,
        traced: TracedGraph,
        title: str = "",
        layers: set[int] | None = None,
        weights: bool = True,
        version: CompiledGraph | None = None,
        table: CostTable | None = None,
    ):
        self.traced = traced
        self.title = title or traced.name
        self.layers = layers
        self.weights = weights
        self.version = version
        self.table = table

    @staticmethod
    def root(h: Handle) -> Handle:
        while h.parent is not None:
            h = h.parent
        return h

    def layer_of(self) -> dict[int, int | None]:
        """Each step's layer, by step index."""
        steps = self.traced.steps
        own = {}
        for i, s in enumerate(steps):
            found = [LAYERED.match(self.root(h).name) for h in s.inputs + s.outputs]
            own[i] = next((int(m.group(1)) for m in found if m), None)
        placed = [i for i, n in own.items() if n is not None]
        layer, made = {}, {}
        for i, s in enumerate(steps):
            layer[i] = own[i]
            held = any(
                self.root(h).role in ("weight", "state") for h in s.inputs + s.outputs
            )
            if (
                own[i] is None
                and placed
                and placed[0] < i
                and (i < placed[-1] or not held)
            ):
                found = [made.get(self.root(h).name) for h in s.inputs]
                layer[i] = max((n for n in found if n is not None), default=None)
            for h in s.outputs:
                made[self.root(h).name] = layer[i]
        return layer

    def drawn(self) -> list[int]:
        """The indices of the steps drawn."""
        layer = self.layer_of()
        return [
            i
            for i in range(len(self.traced.steps))
            if self.layers is None or layer[i] in self.layers
        ]

    def packs(self) -> dict[int, int]:
        """The pack each step's design shares a device in, by step index:
        a tuned full ELF's devices holding more than one design.
        """
        tuning = None if self.version is None else self.version.tuning
        if tuning is None or not tuning.devices:
            return {}
        keys = self.keys()
        return {
            i: n
            for i, key in keys.items()
            for n, device in enumerate(tuning.devices)
            if key in device
        }

    def keys(self) -> dict[int, str]:
        """Each step's ``cost_key``, by step index, against the current device."""
        return {i: cost_key(s.op) for i, s in enumerate(self.traced.steps)}

    def designs(self) -> dict[int, tuple[str, int]]:
        """Each step's design in the compiled image, a short label, and how
        many operators run that design, by step index.
        """
        if self.version is None:
            return {}
        artifacts = self.version.artifacts
        labels = {
            d.name: (f"d{i}", len(d.operators)) for i, d in enumerate(artifacts.designs)
        }
        return {s.index: labels[s.design] for s in artifacts.steps}

    def moved(self) -> dict[str, dict]:
        """The tunables the tuner moved, by the setting key it chose."""
        tuning: Tuning | None = None if self.version is None else self.version.tuning
        if tuning is None:
            return {}
        return {
            v.key: dict(v.tunables) for key, v in tuning.chosen.items() if v.key != key
        }

    def box(self, i: int, values: Mapping[int, list[str]], context: dict) -> list[str]:
        """The lines of step ``i``'s box, as Graphviz HTML-like label text."""
        s = self.traced.steps[i]
        op = s.op
        name = type(op).__name__
        lines = [f"<b>{html.escape(name)}</b>"]
        for kind, links in (("prepares", op.prepare), ("finishes", op.finish)):
            if links:
                folded = ", ".join(type(link.op).__name__ for link in links)
                lines.append(
                    f'<font point-size="9" color="{INK}"><i>{kind} '
                    f"{html.escape(folded)}</i></font>"
                )
        for buffer, _, _ in op.placements:
            lines.append(
                f'<font point-size="9" color="{INK}"><i>writes {html.escape(buffer)} '
                f"in place</i></font>"
            )
        shapes = ", ".join(
            Dataflow.shape(h) for h in s.outputs if self.root(h).role != "state"
        )
        if shapes:
            lines.append(f'<font point-size="9">{shapes}</font>')
        if not self.weights:
            for h in s.inputs:
                r = self.root(h)
                if r.role == "weight":
                    lines.append(
                        f'<font point-size="9" color="{INK_2}">'
                        f"{html.escape(r.name)} {Dataflow.shape(r)}</font>"
                    )
        for v in values.get(id(op), []):
            lines.append(
                f'<font point-size="9" color="{INK_2}"><i>{html.escape(v)}</i></font>'
            )
        key = context["keys"].get(i)
        moved = context["moved"].get(key) if key is not None else None
        if moved:
            text = ", ".join(f"{k}={v}" for k, v in moved.items())
            lines.append(
                f'<font point-size="9" color="{INK}"><b>tuned</b> {html.escape(text)}</font>'
            )
        if i in context["designs"]:
            label, count = context["designs"][i]
            shared = f", shared by {count}" if count > 1 else ""
            lines.append(
                f'<font point-size="8" color="{MUTED}">design {label}{shared}</font>'
            )
        if self.table is not None and key is not None:
            if key in self.table.steps:
                lines.append(
                    f'<font point-size="9" color="{INK_2}">'
                    f"{self.table.t_step(key):.1f} µs</font>"
                )
            else:
                lines.append(f'<font point-size="8" color="{MUTED}">unmeasured</font>')
        return lines

    def tooltip(self, op: Operator) -> str:
        """The resolved operator's label and every tunable it runs with."""
        try:
            resolved = op.resolved()
        except (Unresolvable, ValueError) as e:
            return f"{type(op).__name__}: {e}"
        tunables = ", ".join(
            f"{n}={getattr(resolved, n)}" for n in type(op)._auto_fields
        )
        return f"{resolved.name}\n{tunables}"

    @staticmethod
    def shape(h: Handle) -> str:
        return "×".join(str(n) for n in h.shape) or "1"

    def caption(self) -> str:
        """The title, then what a compiled version's plan and tuning say."""
        lines = [html.escape(self.title)]
        if self.version is not None:
            plan = self.version.plan
            lines.append(
                f'<font point-size="11" color="{INK_2}">image {plan.image}, '
                f"dispatch {plan.dispatch}: {html.escape('; '.join(plan.reasons))}</font>"
            )
            tuning = self.version.tuning
            if tuning is not None:
                lines.append(
                    f'<font point-size="11" color="{INK_2}">modelled '
                    f"{tuning.baseline_us:.1f} µs ({tuning.baseline_configures} "
                    f"configures) as traced, {tuning.predicted_us:.1f} µs "
                    f"({tuning.configures}) tuned</font>"
                )
        return "<br/>".join(lines)

    def body(self, prefix: str = "") -> tuple[list[str], list[str]]:
        """This picture's nodes (in clusters) and edges, each node named
        with ``prefix`` so two pictures can share one graph.
        """
        steps = self.traced.steps
        drawn = self.drawn()
        kept = set(drawn)
        layer = self.layer_of()
        writer = {}
        for i, s in enumerate(steps):
            for h in s.outputs:
                if self.root(h).role in ("intermediate", "output"):
                    writer[self.root(h).name] = i
        values = defaultdict(list)
        for b in self.traced.bindings:
            values[id(b.op)].append(f"{b.member.name} = {b.expression}")
        context = dict(
            designs=self.designs(),
            keys={} if self.version is None and self.table is None else self.keys(),
            moved=self.moved(),
        )
        packs = self.packs()

        nodes: dict[object, list[str]] = defaultdict(list)
        edges: list[str] = []
        named: dict[str, str] = {}

        def source(h: Handle, at: object) -> str:
            r = self.root(h)
            if r.role in ("intermediate", "output"):
                if writer.get(r.name) in kept:
                    return f"{prefix}s{writer[r.name]}"
                node = f"{prefix}x_{r.name}"
                if node not in named:
                    who = steps[writer[r.name]].op if r.name in writer else None
                    named[node] = (
                        f'  "{node}" [shape=ellipse, style=dashed, '
                        f'label=<{html.escape(r.name)}<br/><font point-size="9" '
                        f'color="{MUTED}">{Dataflow.shape(r)} from '
                        f"{type(who).__name__ if who is not None else 'outside'}"
                        f"</font>>];"
                    )
                    nodes[None].append(named[node])
                return node
            node = f"{prefix}b_{r.name}"
            if node not in named:
                if r.role == "weight":
                    style = f'shape=note, color="{AXIS}", fontcolor="{INK_2}"'
                elif r.role == "state":
                    style = f'shape=cylinder, color="{INK_2}"'
                else:
                    style = f'shape=ellipse, penwidth=2, color="{INK_2}"'
                named[node] = (
                    f'  "{node}" [{style}, label=<{html.escape(r.name)}<br/>'
                    f'<font point-size="9" color="{MUTED}">{Dataflow.shape(r)} '
                    f"{r.role}</font>>];"
                )
                nodes[None if r.role == "input" else at].append(named[node])
            return node

        for i in drawn:
            s = steps[i]
            color = FAMILIES[FAMILY.get(type(s.op).__name__, "other")]
            tip = html.escape(self.tooltip(s.op), quote=True)
            nodes[(("pack", packs[i]) if packs else ("layer", layer[i]))].append(
                f'  "{prefix}s{i}" [shape=box, style="rounded,filled", '
                f'fillcolor="{color}33", color="{color}", penwidth=2, '
                f'tooltip="{tip}", label=<{"<br/>".join(self.box(i, values, context))}>];'
            )
            for h in s.inputs:
                r = self.root(h)
                if r.role == "weight" and not self.weights:
                    continue
                bounded = " bounded" if h.bounds or h.index_by is not None else ""
                dashed = ", style=dashed" if r.role in ("weight", "state") else ""
                edges.append(
                    f'  "{source(h, (("pack", packs[i]) if packs else ("layer", layer[i])))}" -> "{prefix}s{i}" '
                    f'[label="{Dataflow.shape(h)}{bounded}"{dashed}];'
                )
            for h in s.outputs:
                if self.root(h).role == "state":
                    edges.append(
                        f'  "{prefix}s{i}" -> "{source(h, (("pack", packs[i]) if packs else ("layer", layer[i])))}" '
                        f'[label="write {Dataflow.shape(h)}", penwidth=1.5];'
                    )
        returned = {self.root(h).name for h in self.traced.returned}
        for h in self.traced.outputs:
            r = self.root(h)
            if writer.get(r.name) in kept:
                kind = "returned" if r.name in returned else "carried"
                nodes[None].append(
                    f'  "{prefix}o_{r.name}" [shape=doubleoctagon, color="{INK_2}", '
                    f'label=<{html.escape(r.name)}<br/><font point-size="9" '
                    f'color="{MUTED}">{Dataflow.shape(r)} {kind}</font>>];'
                )
                edges.append(f'  "{prefix}s{writer[r.name]}" -> "{prefix}o_{r.name}";')
                for name, nxt in self.traced.carry.items():
                    if isinstance(nxt, Handle) and self.root(nxt).name == r.name:
                        nodes[None].append(
                            f'  "{prefix}v_{name}" [shape=plain, fontcolor="{INK_2}", '
                            f"label=<<i>{html.escape(name)}</i>, next call>];"
                        )
                        edges.append(
                            f'  "{prefix}o_{r.name}" -> "{prefix}v_{name}" [style=dotted];'
                        )

        out = list(nodes[None])
        for at, lines in nodes.items():
            if at is None:
                continue
            kind, n = at
            if n is None:
                out += lines
                continue
            label = f"layer {n}" if kind == "layer" else f"pack {n}: one device"
            out.append(f'  subgraph "cluster_{prefix}{kind}{n}" {{')
            out.append(
                f'    label=<{label}>; fontcolor="{INK_2}"; color="{HAIRLINE}"; '
                f'style="rounded"; penwidth=1;'
            )
            out += ["  " + line for line in lines]
            out.append("  }")
        return out, edges

    def legend(self, prefix: str = "") -> str:
        """The families drawn, each with its hue."""
        seen = {
            FAMILY.get(type(self.traced.steps[i].op).__name__, "other")
            for i in self.drawn()
        }
        rows = "".join(
            f'<tr><td bgcolor="{color}33" border="1" color="{color}" width="18"> '
            f'</td><td align="left">{html.escape(family)}</td></tr>'
            for family, color in FAMILIES.items()
            if family in seen
        )
        return (
            f'  "{prefix}legend" [shape=plain, label=<<table border="0" cellspacing="3" '
            f'cellpadding="2"><tr><td colspan="2" align="left"><b>operator family</b>'
            f"</td></tr>{rows}</table>>];"
        )

    def dot(self) -> str:
        """The picture as Graphviz text."""
        nodes, edges = self.body()
        return "\n".join([*header(self.caption()), *nodes, *edges, self.legend(), "}"])

    def svg(self) -> str:
        """The picture as SVG (``render``)."""
        return render(self.dot())

    def html(self) -> str:
        """The picture as one self-contained page (``page``)."""
        return page(self.dot(), self.panel(), self.title)

    def panel(self, prefix: str = "") -> dict[str, dict]:
        """What the page shows for a clicked step, by its node's name."""
        values = defaultdict(list)
        for b in self.traced.bindings:
            values[id(b.op)].append(f"{b.member.name} = {b.expression}")
        return {
            f"{prefix}s{i}": dict(
                op=type(self.traced.steps[i].op).__name__,
                detail=self.tooltip(self.traced.steps[i].op),
                values=values.get(id(self.traced.steps[i].op), []),
                inputs=[h.name for h in self.traced.steps[i].inputs],
                outputs=[h.name for h in self.traced.steps[i].outputs],
            )
            for i in self.drawn()
        }


def header(caption: str) -> list[str]:
    """The opening of a picture's Graphviz text, captioned."""
    return [
        "digraph G {",
        f'  graph [rankdir=TB, fontname="sans-serif", bgcolor="{SURFACE}", '
        f'label=<{caption}>, labelloc=t, fontsize=18, fontcolor="{INK}", '
        f"nodesep=0.25, ranksep=0.35, newrank=true];",
        f'  node [fontname="sans-serif", fontsize=11, fontcolor="{INK}", '
        f'color="{AXIS}", penwidth=1];',
        f'  edge [fontname="sans-serif", fontsize=9, fontcolor="{INK_2}", '
        f'color="{MUTED}", arrowsize=0.6];',
    ]


def side_by_side(pictures: Sequence[tuple[str, Dataflow]], title: str) -> str:
    """``pictures`` in one Graphviz graph, left to right, each in a cluster
    under its heading: a graph as traced beside the same graph tuned.
    """
    lines = header(html.escape(title))
    for n, (heading, picture) in enumerate(pictures):
        nodes, edges = picture.body(prefix=f"p{n}_")
        lines.append(f'  subgraph "cluster_p{n}" {{')
        lines.append(
            f"    label=<{heading}<br/>{picture.caption()}>; "
            f'color="{AXIS}"; style="rounded"; penwidth=1; fontsize=14;'
        )
        lines += ["  " + line for line in nodes]
        lines.append("  }")
        lines += edges
    lines.append(pictures[0][1].legend(prefix="p0_"))
    lines.append("}")
    return "\n".join(lines)


def render(dot: str, kind: str = "svg") -> str | bytes:
    """``dot`` laid out by Graphviz's ``dot``: SVG text, or the bytes of
    another of its formats (``"png"``).

    Graphviz names each SVG node ``node1``, ``node2``, ... and keeps the
    Graphviz name in its title; the SVG's node ids are the Graphviz names,
    so a page can find a step by the name ``Dataflow.panel`` keys it by.

    Raises:
        FileNotFoundError: Graphviz's ``dot`` is not on the path.
    """
    program = shutil.which("dot")
    if program is None:
        raise FileNotFoundError(
            "Graphviz's dot is not on the path; install graphviz to render a "
            "picture, or take its text from dot()"
        )
    done = subprocess.run(
        [program, f"-T{kind}"], input=dot.encode(), capture_output=True, check=True
    )
    if kind != "svg":
        return done.stdout
    return re.sub(
        r'<g id="[^"]+"(\s+class="node")>\s*<title>([^<]+)</title>',
        lambda m: f'<g id="{m.group(2)}"{m.group(1)}>\n<title>{m.group(2)}</title>',
        done.stdout.decode(),
    )


def page(dot: str, panel: Mapping[str, dict], title: str) -> str:
    """One self-contained HTML page of ``dot``'s SVG: drag to pan, the wheel
    or the buttons to zoom, and a click on a step shows ``panel``'s entry for
    it. It loads nothing.
    """
    return PAGE.format(
        title=html.escape(title),
        svg=render(dot),
        steps=json.dumps(panel).replace("</", "<\\/"),
        surface=SURFACE,
        ink=INK,
        muted=MUTED,
        hairline=HAIRLINE,
    )


PAGE = """<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>
  body {{ margin: 0; display: flex; height: 100vh; font-family: system-ui, sans-serif;
         background: {surface}; color: {ink}; }}
  #canvas {{ flex: 1; overflow: hidden; position: relative; cursor: grab; }}
  #canvas svg {{ transform-origin: 0 0; }}
  #panel {{ width: 340px; border-left: 1px solid {hairline}; padding: 12px;
           overflow-y: auto; font-size: 13px; }}
  #panel h2 {{ font-size: 14px; margin: 0 0 8px; }}
  #panel pre {{ white-space: pre-wrap; font-size: 12px; }}
  .muted {{ color: {muted}; }}
  .hit {{ cursor: pointer; }}
  .hit.selected path, .hit.selected polygon {{ stroke-width: 4; }}
  #zoom {{ position: absolute; top: 8px; right: 8px; z-index: 1; }}
  #zoom button {{ width: 28px; height: 28px; }}
</style></head>
<body>
<div id="canvas"><div id="zoom"><button id="in">+</button><button id="out">-</button></div>
{svg}</div>
<div id="panel"><h2>{title}</h2><div id="detail" class="muted">Click a step.
Drag to pan; the wheel or the buttons zoom.</div></div>
<script>
const steps = {steps};
const canvas = document.getElementById("canvas");
const svg = canvas.querySelector("svg");
let scale = 1, x = 0, y = 0, last = null;
const apply = () => {{ svg.style.transform = `translate(${{x}}px, ${{y}}px) scale(${{scale}})`; }};
canvas.addEventListener("mousedown", e => {{ last = [e.clientX, e.clientY]; }});
window.addEventListener("mouseup", () => {{ last = null; }});
window.addEventListener("mousemove", e => {{
  if (!last) return;
  x += e.clientX - last[0]; y += e.clientY - last[1]; last = [e.clientX, e.clientY]; apply();
}});
canvas.addEventListener("wheel", e => {{
  e.preventDefault(); scale = Math.min(8, Math.max(0.1, scale * (e.deltaY < 0 ? 1.1 : 0.9))); apply();
}});
document.getElementById("in").onclick = () => {{ scale = Math.min(8, scale * 1.2); apply(); }};
document.getElementById("out").onclick = () => {{ scale = Math.max(0.1, scale / 1.2); apply(); }};
const text = s => s.replace(/[&<>]/g, c => ({{"&": "&amp;", "<": "&lt;", ">": "&gt;"}})[c]);
for (const [id, s] of Object.entries(steps)) {{
  const node = document.getElementById(id);
  if (!node) continue;
  node.classList.add("hit");
  node.addEventListener("click", () => {{
    document.querySelectorAll(".selected").forEach(n => n.classList.remove("selected"));
    node.classList.add("selected");
    document.getElementById("detail").innerHTML =
      `<h2>${{text(s.op)}}</h2><pre>${{text(s.detail)}}</pre>` +
      s.values.map(v => `<div><i>${{text(v)}}</i></div>`).join("") +
      `<p class="muted">reads ${{text(s.inputs.join(", "))}}<br>writes ${{text(s.outputs.join(", "))}}</p>`;
  }});
}}
</script>
</body></html>
"""
