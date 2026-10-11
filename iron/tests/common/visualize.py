# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pictures of a graph, drawn device-free from its trace: every step is a
node, every buffer a step reads an edge into it from its producer, and a
folded step names what it folded.
"""

import re
import shutil

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.graph.fold import folded
from iron.common.graph.visualize import Dataflow, render, side_by_side
from iron.lm import unread_weights
from iron.lm.embeddinggemma2.vision import model as vision
from iron.lm.layers import SwiGLU
from iron.tests.common.llama_model import small

E, H = 2048, 8192

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored

# Laying a picture out needs Graphviz's dot, which is not a Python package.
needs_dot = pytest.mark.skipif(shutil.which("dot") is None, reason="no Graphviz dot")


def z(*shape):
    return np.zeros(shape, dtype=bfloat16)


def edges(dot: str) -> set[tuple[str, str]]:
    return set(re.findall(r'^\s*"([^"]+)" -> "([^"]+)"', dot, re.M))


def nodes(dot: str) -> set[str]:
    return set(re.findall(r'^\s*"([^"]+)" \[', dot, re.M))


def test_a_traced_graph_names_every_step_and_every_edge():
    t = small().trace()
    dot = t.dot()
    writer, expected = {}, set()
    for i, s in enumerate(t.steps):
        for h in s.inputs:
            root = Dataflow.root(h)
            source = (
                f"s{writer[root.name]}" if root.name in writer else f"b_{root.name}"
            )
            expected.add((source, f"s{i}"))
        for h in s.outputs:
            root = Dataflow.root(h)
            if root.role == "state":
                expected.add((f"s{i}", f"b_{root.name}"))
            else:
                writer[root.name] = i
    for h in t.outputs:
        expected.add((f"s{writer[h.name]}", f"o_{h.name}"))
    expected.add(("o_carry_token", "v_token"))
    assert {f"s{i}" for i in range(len(t.steps))} <= nodes(dot)
    assert edges(dot) == expected


def test_a_layer_drawn_alone_keeps_its_steps_and_marks_what_flows_in():
    t = small().trace()
    picture = Dataflow(t, layers={1})
    layer = picture.layer_of()
    assert {
        type(t.steps[i].op).__name__ for i in range(len(t.steps)) if layer[i] is None
    } == {
        "Copy",
        "RMSNorm",
        "GEMV",
        "Sample",
    }
    dot = picture.dot()
    assert {f"s{i}" for i in picture.drawn()} <= nodes(dot)
    assert not any(f"s{i}" in nodes(dot) for i in layer if layer[i] != 1)
    # The residual and the angles come in from steps not drawn.
    assert any(n.startswith("x_") for n in nodes(dot))


def test_a_towers_layers_are_found_under_its_prefix():
    c = vision.VISION
    graph = vision.Vision(c, unread_weights(vision.layout(c), c.n_layers))
    (shapes,) = graph.shapes()
    t = graph.trace(**shapes)
    drawn = set(Dataflow(t, layers={1}).drawn())
    for i, s in enumerate(t.steps):
        names = [Dataflow.root(h).name for h in s.inputs]
        if any(n.startswith("vision.layers.1.") for n in names):
            assert i in drawn
        if any(n.startswith(("vision.layers.0.", "vision.layers.2.")) for n in names):
            assert i not in drawn


def test_a_folded_step_names_what_it_folded(npu2):
    t = SwiGLU(z(H, E), z(H, E), z(E, H)).trace(x=(1, E))
    f, _ = folded(t, npu2)
    dot = f.dot()
    assert "finishes SiLU, ElementwiseMul" in dot
    up, gate, down = (f"s{i}" for i in range(3))
    assert {(up, gate), (gate, down)} <= edges(dot)


@needs_dot
def test_a_page_finds_each_step_it_describes():
    t = small().trace()
    page = t.html()
    for i in range(len(t.steps)):
        assert f'<g id="s{i}" class="node">' in page
        assert f'"s{i}": {{"op": ' in page
    assert "<script" in page and "src=" not in page


@needs_dot
def test_two_pictures_side_by_side_keep_their_nodes_apart(npu2):
    t = SwiGLU(z(H, E), z(H, E), z(E, H)).trace(x=(1, E))
    f, _ = folded(t, npu2)
    dot = side_by_side([("traced", t.picture()), ("folded", f.picture())], "SwiGLU")
    assert {"p0_s3", "p1_s2"} <= nodes(dot) and "p1_s3" not in nodes(dot)
    assert render(dot, "png").startswith(b"\x89PNG")
