# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pictures of a graph, drawn device-free from its recording: every step is a
node, and every buffer a step reads an edge into it from its producer.
"""

import re

import pytest

from iron.common.graph.visualize import layers
from iron.applications.embedding_gemma2.model import Config, Multimodal
from iron.lm import Checkpoint
from iron.lm.testing import require, weights_dir
from iron.tests.support.llama_model import small

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def edges(dot: str) -> set[tuple[str, str]]:
    return set(re.findall(r'^\s*"([^"]+)" -> "([^"]+)"', dot, re.M))


def nodes(dot: str) -> set[str]:
    return set(re.findall(r'^\s*"([^"]+)" \[', dot, re.M))


def test_a_recorded_graph_names_every_step_and_every_edge():
    t = small().record()
    dot = t.dot()
    writer, expected = {}, set()
    for i, s in enumerate(t.steps):
        for h in s.inputs:
            root = h.buffer
            source = (
                f"s{writer[root.name]}" if root.name in writer else f"b_{root.name}"
            )
            expected.add((source, f"s{i}"))
        for h in s.outputs:
            root = h.buffer
            if root.role == "state":
                expected.add((f"s{i}", f"b_{root.name}"))
            else:
                writer[root.name] = i
    for h in t.outputs:
        expected.add((f"s{writer[h.name]}", f"o_{h.name}"))
    expected.add(("o_carry_token", "v_token"))
    assert {f"s{i}" for i in range(len(t.steps))} <= nodes(dot)
    assert edges(dot) == expected


def in_layer(t, n: int) -> set[int]:
    return {i for i, at in layers(t).items() if at == n}


def test_each_layer_s_steps_are_drawn_in_its_cluster():
    t = small().record()
    layer = layers(t)
    assert {
        type(t.steps[i].op).__name__ for i in range(len(t.steps)) if layer[i] is None
    } == {
        "Copy",
        "RMSNorm",
        "GEMV",
        "Sample",
    }
    cluster = t.dot().split('subgraph "cluster_layer1" {')[1].split("  }")[0]
    steps = {n for n in nodes(cluster) if n.startswith("s")}
    assert steps == {f"s{i}" for i in in_layer(t, 1)}


def test_a_towers_layers_are_found_under_its_prefix():
    path = weights_dir("embeddinggemma-2") / "model.safetensors"
    require(path)
    graph = Multimodal(Config(), Checkpoint(path).tree("unread"))
    _, _, shapes, _ = graph.shapes()
    t = graph.record(**shapes)
    drawn = in_layer(t, 1)
    found = set()
    for i, s in enumerate(t.steps):
        names = [h.buffer.name for h in s.inputs]
        if any(".encoder.layers.1." in n for n in names):
            found.add(i)
        if any(".encoder.layers.0." in n or ".encoder.layers.2." in n for n in names):
            assert i not in drawn
    assert found and found <= drawn


def test_a_per_layer_slice_is_drawn_in_its_layer():
    """Each layer's own slice of the per-layer projection, sliced once at
    load into its own param rather than from the shared tensor at body
    time, is read only by its own layer's steps.
    """
    path = weights_dir("embeddinggemma-2") / "model.safetensors"
    require(path)
    graph = Multimodal(Config(), Checkpoint(path).tree("unread"))
    text, *_ = graph.shapes()
    t = graph.record(**text)
    drawn = in_layer(t, 1)

    def reads(name: str) -> set[int]:
        return {
            i
            for i, s in enumerate(t.steps)
            if any(h.buffer.name == name for h in s.inputs)
        }

    assert reads("text.language_model.ple.layers.1") <= drawn
    assert not reads("text.language_model.ple.layers.0") & drawn
    assert not reads("text.language_model.ple.layers.2") & drawn
