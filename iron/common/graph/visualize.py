# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pictures of a graph: its trace, and what compile and the tuner made of
it, drawn from the live objects as Graphviz text (``dot()``), SVG
(``svg()``) or one self-contained page (``html()``).
"""

from __future__ import annotations

import html
import json
import math
import re
import shutil
import subprocess
from collections import defaultdict
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from aie import ir
from aie.dialects import aie
from aie.helpers.util import mlir_type_to_np_dtype
from aie.utils import bfp
from aie.utils.config import aiecc_tool_path

from ..declare import Operator, Unresolvable
from ..design import OperatorDesign
from ..image.allocator import LiveRange
from .handle import Handle

if TYPE_CHECKING:
    from .compiled import CompiledGraph
    from .tuner import Prices
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

# A buffer of layer N: its weights, a tower's too (vision.layers.N.q), and a
# decoder's caches.
LAYERED = re.compile(r"(?:^|\.)(?:layers|keys|values|ple)\.(\d+)(?:\.|$)")


class Dataflow:
    """A traced graph, or a compiled version of one, as a picture.

    Args:
        traced: The graph's trace; a compiled version's is the graph it built,
            its folds applied and its designs narrowed.
        title: The caption.
        layers: The layers drawn, by index (``layers.3.q`` and
            ``vision.layers.3.q`` are layer 3), or None for every step. A step
            reading no layer's buffer is in the layer of what it reads; before
            the first layer, and after the last where it holds a weight or
            state of no layer (a head), it is in none.
        weights: Draw each weight as its own node; else name it in the box
            of the step reading it.
        version: The compiled version ``traced`` is of: each box names its
            design and the steps folded into it, a tuned version's moved
            tunables and packs too.
        prices: Each box shows the time these prices give its design.
    """

    def __init__(
        self,
        traced: TracedGraph,
        title: str = "",
        layers: set[int] | None = None,
        weights: bool = True,
        version: CompiledGraph | None = None,
        prices: Prices | None = None,
    ):
        self.traced = traced
        self.title = title or traced.name
        self.layers = layers
        self.weights = weights
        self.version = version
        self.prices = prices

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
            found = [LAYERED.search(self.root(h).name) for h in s.inputs + s.outputs]
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
        # An xclbin chain loads each design alone: it has no shared device.
        if tuning is None or not self.version.plan.full_elf:
            return {}
        return tuning.packs(self.traced, None)

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

    def moved(self) -> dict[int, dict]:
        """The tunables the tuner moved, by step index."""
        tuning = None if self.version is None else self.version.tuning
        return {} if tuning is None else tuning.moved(self.traced, None)

    def values(self) -> dict[int, list[str]]:
        """Each operator's per-call values as written, by the ``id`` of the
        operator, which the trace holds.
        """
        found = defaultdict(list)
        for b in self.traced.bindings:
            found[id(b.op)].append(f"{b.member.name} = {b.expression}")
        return found

    def box(
        self,
        i: int,
        values: Mapping[int, list[str]],
        designs: Mapping[int, tuple[str, int]],
        moved: Mapping[int, dict],
        prices: Mapping[int, float | None],
    ) -> list[str]:
        """The lines of step ``i``'s box, as Graphviz HTML-like label text.

        Args:
            i: The step's index.
            values: ``values()``.
            designs: ``designs()``.
            moved: ``moved()``.
            prices: Each step's time, None where it is not priced.
        """
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
        tuned = moved.get(i)
        if tuned:
            text = ", ".join(f"{k}={v}" for k, v in tuned.items())
            lines.append(
                f'<font point-size="9" color="{INK}"><b>tuned</b> {html.escape(text)}</font>'
            )
        if i in designs:
            label, count = designs[i]
            shared = f", shared by {count}" if count > 1 else ""
            lines.append(
                f'<font point-size="8" color="{MUTED}">design {label}{shared}</font>'
            )
        if i in prices:
            if prices[i] is not None:
                lines.append(
                    f'<font point-size="9" color="{INK_2}">{prices[i]:.1f} µs</font>'
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
            f"{n}={vars(resolved)[n]}" for n in type(op).declaration.autos
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
            image = "one full ELF" if plan.full_elf else "an xclbin per step"
            lines.append(
                f'<font point-size="11" color="{INK_2}">{image}: '
                f"{html.escape('; '.join(plan.reasons))}</font>"
            )
            tuning = self.version.tuning
            if tuning is not None:
                lines.append(
                    f'<font point-size="11" color="{INK_2}">'
                    f"{html.escape(tuning.summary())}</font>"
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
        values, designs, moved = self.values(), self.designs(), self.moved()
        prices = {} if self.prices is None else self.prices.step_us(self.traced, None)
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
            at = ("pack", packs[i]) if i in packs else ("layer", layer[i])
            label = "<br/>".join(self.box(i, values, designs, moved, prices))
            nodes[at].append(
                f'  "{prefix}s{i}" [shape=box, style="rounded,filled", '
                f'fillcolor="{color}33", color="{color}", penwidth=2, '
                f'tooltip="{tip}", label=<{label}>];'
            )
            for h in s.inputs:
                r = self.root(h)
                if r.role == "weight" and not self.weights:
                    continue
                bounded = " bounded" if h.bounds or h.index_by is not None else ""
                dashed = ", style=dashed" if r.role in ("weight", "state") else ""
                edges.append(
                    f'  "{source(h, at)}" -> "{prefix}s{i}" '
                    f'[label="{Dataflow.shape(h)}{bounded}"{dashed}];'
                )
            for h in s.outputs:
                if self.root(h).role == "state":
                    edges.append(
                        f'  "{prefix}s{i}" -> "{source(h, at)}" '
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
        values = self.values()
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


class ArenaPicture:
    """A compiled version's scratch buffers over its runlist: each a box
    from the first step touching it to the last, at its byte offset and
    size, so the bytes two buffers share are where their boxes stack in
    one column of steps and never overlap. Weights and states (residents),
    which hold their bytes for every step, are summed under the boxes.

    Args:
        version: The compiled version.
        title: The caption.
    """

    WIDTH, HEIGHT, LEFT, TOP, BOTTOM = 1100, 520, 80, 64, 70

    def __init__(self, version: CompiledGraph, title: str = ""):
        seq = version.sequence
        self.title = title or f"{version.traced.name}: scratch buffers over the runlist"
        layout = seq.layout
        names = [
            n
            for n, (kind, _, _) in layout.items()
            if kind == "scratch" and n not in seq.residents
        ]
        steps, first_writer = [], {}
        for step in seq.steps:
            reads, writes = [], []
            for ref, b in zip(step.buffers, step.op.buffers):
                if b.fills:
                    reads.append(ref.root)
                if b.drains:
                    writes.append(ref.root)
                    first_writer.setdefault(ref.root, step.op)
            steps.append((reads, writes))
        self.steps = len(steps)
        self.ranges = LiveRange.touching(steps, names)
        self.boxes = {n: layout[n][1:] for n in names}
        self.colors = {
            n: (
                FAMILIES[FAMILY.get(type(first_writer[n]).__name__, "other")]
                if n in first_writer
                else MUTED
            )
            for n in names
        }
        self.resident_bytes = sum(layout[n][2] for n in seq.residents if n in layout)

    def svg(self) -> str:
        """The boxes as SVG: steps across, byte offsets up."""
        if not self.boxes:
            raise ValueError(f"{self.title}: no scratch buffer is planned")
        base = min(offset for offset, _ in self.boxes.values())
        top = max(offset + size for offset, size in self.boxes.values()) - base
        width, height, left, upper = self.WIDTH, self.HEIGHT, self.LEFT, self.TOP
        plot_w = width - left - 20
        plot_h = height - upper - self.BOTTOM
        per_step = plot_w / self.steps
        per_byte = plot_h / top
        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" font-family="system-ui, sans-serif">',
            f'<rect width="{width}" height="{height}" fill="{SURFACE}"/>',
            f'<text x="{left}" y="28" font-size="17" fill="{INK}">{html.escape(self.title)}</text>',
            f'<text x="{left}" y="48" font-size="12" fill="{INK_2}">{len(self.boxes)} '
            f"buffers in {top / 1024:.1f} KiB; weights and states hold "
            f"{self.resident_bytes / 2**20:.1f} MiB more, for every step</text>",
        ]
        for k in range(5):
            y = upper + plot_h - k * plot_h / 4
            out.append(
                f'<line x1="{left}" x2="{left + plot_w}" y1="{y}" y2="{y}" '
                f'stroke="{HAIRLINE}" stroke-width="1"/>'
            )
            out.append(
                f'<text x="{left - 8}" y="{y + 4}" font-size="11" text-anchor="end" '
                f'fill="{MUTED}">{k * top / 4 / 1024:.0f} KiB</text>'
            )
        tick = max(1, self.steps // 10)
        for i in range(0, self.steps, tick):
            x = left + (i + 0.5) * per_step
            out.append(
                f'<text x="{x}" y="{upper + plot_h + 18}" font-size="11" '
                f'text-anchor="middle" fill="{MUTED}">{i}</text>'
            )
        out.append(
            f'<text x="{left + plot_w / 2}" y="{upper + plot_h + 40}" font-size="12" '
            f'text-anchor="middle" fill="{INK_2}">step</text>'
        )
        for name, (offset, size) in sorted(self.boxes.items(), key=lambda b: -b[1][1]):
            r = self.ranges[name]
            x = left + r.begin * per_step + 1
            w = max((r.end - r.begin + 1) * per_step - 2, 2)
            y = upper + plot_h - (offset - base + size) * per_byte + 1
            h = max(size * per_byte - 2, 2)
            out.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="3" '
                f'fill="{self.colors[name]}" fill-opacity="0.45" '
                f'stroke="{self.colors[name]}" stroke-width="1"><title>'
                f"{html.escape(name)}: {size} bytes at {offset}, steps "
                f"{r.begin} to {r.end}</title></rect>"
            )
            if w > 7 * len(name) and h > 13:
                out.append(
                    f'<text x="{x + 4:.1f}" y="{y + 12:.1f}" font-size="10" '
                    f'fill="{INK}">{html.escape(name)}</text>'
                )
        x = left + plot_w
        for family, color in reversed(FAMILIES.items()):
            if color not in self.colors.values():
                continue
            x -= 14 + 7 * len(family) + 18
            out.append(
                f'<rect x="{x}" y="38" width="12" height="12" rx="2" fill="{color}" '
                f'fill-opacity="0.45" stroke="{color}"/>'
            )
            out.append(
                f'<text x="{x + 16}" y="48" font-size="11" fill="{INK_2}">{family}</text>'
            )
        out.append("</svg>")
        return "\n".join(out)


class Floorplan:
    """Where a compiled version runs one step on the array: the tiles of
    the device that step configures, what each does, and the stream links
    between them, read from the image's lowered module (what aiecc placed
    and routed) and ``aie-translate --aie-flows-to-json``.

    Args:
        version: The compiled version.
        step: The step's index in its runlist.
        title: The caption; the step's operator if empty.
    """

    def __init__(self, version: CompiledGraph, step: int, title: str = ""):
        artifacts = version.artifacts
        record = artifacts.steps[step]
        op = version.traced.steps[step].op
        self.title = title or f"{type(op).__name__} (step {step})"
        self.color = FAMILIES[FAMILY.get(type(op).__name__, "other")]
        if artifacts.full_elf:
            path = artifacts.lowered_mlir
            name = OperatorDesign(op.resolved()).name
        else:
            [design] = [d for d in artifacts.designs if d.name == record.design]
            path = design.entry.lowered_mlir
            name = None
        if path is None or not path.exists():
            raise FileNotFoundError(
                f"{version.traced.name}: the build kept no lowered module for "
                f"step {step}"
            )
        with ir.Context(), ir.Location.unknown():
            module = ir.Module.parse(path.read_text())
            devices = [o for o in module.body.operations if isinstance(o, aie.DeviceOp)]
            device = self.device_of(devices, name)
            self.device = ir.StringAttr(device.attributes["sym_name"]).value
            self.read(list(device.regions[0].blocks[0].operations))
        routed = subprocess.run(
            [
                aiecc_tool_path("aie-translate"),
                "--aie-flows-to-json",
                f"--aie-device-name={self.device}",
                str(path),
            ],
            capture_output=True,
            check=True,
            text=True,
        ).stdout
        heading = dict(
            northbound=(0, 1), southbound=(0, -1), eastbound=(1, 0), westbound=(-1, 0)
        )
        self.links: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}
        for key, box in json.loads(routed).items():
            if not key.startswith("switchbox"):
                continue
            col, row = box["col"], box["row"]
            for way, (dx, dy) in heading.items():
                if box[way]:
                    self.links[(col, row), (col + dx, row + dy)] = box[way]

    @staticmethod
    def device_of(devices: list, name: str | None):
        """The device running design ``name``: its own, or the pack whose
        runtime sequence is named for it; on an xclbin's module, its one
        device.
        """
        if name is None:
            [device] = devices
            return device
        for device in devices:
            if ir.StringAttr(device.attributes["sym_name"]).value == name:
                return device
        for device in devices:
            for o in device.regions[0].blocks[0].operations:
                if (
                    isinstance(o, aie.RuntimeSequenceOp)
                    and ir.StringAttr(o.attributes["sym_name"]).value == name
                ):
                    return device
        raise KeyError(f"no device of the image runs {name}")

    def read(self, ops: list) -> None:
        """The tiles, cores, buffers and shim allocations of one device's ops."""
        tiles = {
            o.result.get_name(): (o.col.value, o.row.value)
            for o in ops
            if isinstance(o, aie.TileOp)
        }
        self.tiles = set(tiles.values())
        self.cores = {
            tiles[o.operands[0].get_name()] for o in ops if isinstance(o, aie.CoreOp)
        }
        self.held: dict[tuple[int, int], int] = defaultdict(int)
        self.owner: dict[tuple[int, int], str] = {}
        # A pack's runtime sequences are named for its members, which prefix
        # the symbols of each array merged into it.
        members = {
            ir.StringAttr(o.attributes["sym_name"]).value
            for o in ops
            if isinstance(o, aie.RuntimeSequenceOp)
        }
        for o in ops:
            if isinstance(o, aie.BufferOp):
                at = tiles[o.operands[0].get_name()]
                memref = ir.MemRefType(o.result.type)
                self.held[at] += math.prod(memref.shape) * bfp.itemsize(
                    mlir_type_to_np_dtype(memref.element_type)
                )
                member, _, _ = ir.StringAttr(o.attributes["sym_name"]).value.partition(
                    "__"
                )
                if member in members:
                    self.owner.setdefault(at, member)
        self.shims = defaultdict(int)
        for o in ops:
            if isinstance(o, aie.ShimDMAAllocationOp):
                self.shims[tiles[o.operands[0].get_name()]] += 1

    CELL, GAP, LEFT, TOP = 128, 34, 76, 70

    def corner(self, tile: tuple[int, int], rows: int) -> tuple[int, int]:
        """The top left of ``tile``'s square, row 0 at the bottom of ``rows``."""
        col, row = tile
        step = self.CELL + self.GAP
        return self.LEFT + col * step, self.TOP + (rows - 1 - row) * step

    def svg(self, columns: int | None = None, rows: int | None = None) -> str:
        """The array as SVG: ``columns`` and ``rows`` of tiles, by default
        to the last one the device uses.
        """
        columns = columns or 1 + max(c for c, _ in self.tiles)
        rows = rows or 1 + max(r for _, r in self.tiles)
        cell, gap, left, top = self.CELL, self.GAP, self.LEFT, self.TOP
        width = left + columns * (cell + gap) + 10
        height = top + rows * (cell + gap) + 54
        members = sorted(set(self.owner.values()))
        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" font-family="system-ui, sans-serif">',
            f'<rect width="{width}" height="{height}" fill="{SURFACE}"/>',
            f'<text x="{left}" y="30" font-size="18" fill="{INK}">{html.escape(self.title)}</text>',
            f'<text x="{left}" y="50" font-size="12" fill="{INK_2}">device '
            f"{html.escape(self.device)} of the built image"
            + (f": a pack of {len(members)} designs" if len(members) > 1 else "")
            + "</text>",
        ]
        for row in range(rows):
            _, y = self.corner((0, row), rows)
            kind = "shim" if row == 0 else "memtile" if row == 1 else "core"
            out.append(
                f'<text x="{left - 10}" y="{y + cell / 2 + 4}" font-size="11" '
                f'text-anchor="end" fill="{MUTED}">{kind} row {row}</text>'
            )
        for col in range(columns):
            x, _ = self.corner((col, 0), rows)
            out.append(
                f'<text x="{x + cell / 2}" y="{height - 30}" font-size="11" '
                f'text-anchor="middle" fill="{MUTED}">col {col}</text>'
            )
            for row in range(rows):
                tile = (col, row)
                x, y = self.corner(tile, rows)
                used = tile in self.cores or self.held.get(tile) or tile in self.shims
                opacity = 0.35 if tile in self.cores else 0.12 if used else 0
                stroke = self.color if used else HAIRLINE
                if tile in self.owner and len(members) > 1:
                    dash = (
                        ' stroke-dasharray="6 3"'
                        if members.index(self.owner[tile]) % 2
                        else ""
                    )
                else:
                    dash = ""
                lines = []
                if tile in self.cores:
                    lines.append("core")
                if self.held.get(tile):
                    lines.append(f"{self.held[tile] / 1024:.1f} KiB buffers")
                if tile in self.shims:
                    lines.append(f"{self.shims[tile]} host streams")
                if tile in self.owner and len(members) > 1:
                    lines.append(self.owner[tile])
                if tile in self.tiles and not used:
                    lines.append("routes through")
                out.append(
                    f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="6" '
                    f'fill="{self.color}" fill-opacity="{opacity}" stroke="{stroke}" '
                    f'stroke-width="{2 if used else 1}"{dash}><title>tile {tile}: '
                    f"{html.escape(', '.join(lines))}</title></rect>"
                )
                for n, line in enumerate(lines):
                    out.append(
                        f'<text x="{x + 8}" y="{y + 20 + 15 * n}" font-size="11" '
                        f'fill="{INK if n == 0 else INK_2}">{html.escape(line)}</text>'
                    )
        for (a, b), count in sorted(self.links.items()):
            (x0, y0), (x1, y1) = self.corner(a, rows), self.corner(b, rows)
            dx, dy = b[0] - a[0], -(b[1] - a[1])
            # Each direction of a link on its own side of the tiles' centre line.
            shift = 10 if (dx, dy) in ((1, 0), (0, -1)) else -10
            ax = x0 + cell / 2 + dx * cell / 2 + (shift if dy else 0)
            ay = y0 + cell / 2 + dy * cell / 2 + (shift if dx else 0)
            bx = x1 + cell / 2 - dx * cell / 2 + (shift if dy else 0)
            by = y1 + cell / 2 - dy * cell / 2 + (shift if dx else 0)
            out.append(
                f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{INK_2}" '
                f'stroke-width="{1 + min(count, 4)}" marker-end="url(#head)">'
                f"<title>{count} stream(s) {a} to {b}</title></line>"
            )
            out.append(
                f'<text x="{(ax + bx) / 2 + 4}" y="{(ay + by) / 2 - 3}" font-size="10" '
                f'fill="{INK_2}">{count}</text>'
            )
        out.insert(
            2,
            '<defs><marker id="head" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0 L10,5 '
            f'L0,10 z" fill="{INK_2}"/></marker></defs>',
        )
        out.append(
            f'<text x="{left}" y="{height - 10}" font-size="12" fill="{INK_2}">'
            f"{len(self.cores)} cores, "
            f"{sum(1 for t in self.tiles if t[1] == 1 and self.held.get(t))} memtiles "
            f"holding buffers, {len(self.shims)} shims, "
            f"{sum(self.links.values())} routed stream hops, to the host included</text>"
        )
        out.append("</svg>")
        return "\n".join(out)


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
