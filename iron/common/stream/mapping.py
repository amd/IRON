# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Emit the stream-dse mapping YAML for an exported workload from each node's kernel
arguments and its :class:`FusedGroup`, leaving placement to stream. Every node is checked
against the :class:`~iron.common.stream.workload.StreamWorkload` the ONNX came from."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from iron.common.stream.workload import StreamWorkload


@dataclass(frozen=True)
class FusedGroup:
    """A set of nodes fused into one design, with its layer-fusion tiling.

    ``intra_core_tiling`` entries are ``(node_name, dim, tile)``. Splitting a
    workload into several groups makes stream-dse emit one design per group.
    """

    name: str
    layers: Sequence[str]
    intra_core_tiling: Sequence[tuple[str, str, int]] = ()


def group_boundaries(
    workload: StreamWorkload, group_layers: Sequence[Sequence[str]]
) -> list[tuple[tuple[str, ...], tuple[str, ...]]]:
    """Per group, the tensors it consumes from outside and produces for outside.

    These are the group's runtime arguments: what an operator built from several
    fused groups has to hand from one to the next. Both sequences follow the order
    the group's nodes use them, which is the order stream-dse gives the generated
    design its arguments in.
    """
    graph = workload.model.graph
    produced_by = {out: node.name for node in graph.node for out in node.output}
    consumers: dict[str, list[str]] = {}
    for node in graph.node:
        for tensor in node.input:
            consumers.setdefault(tensor, []).append(node.name)
    graph_outputs = {out.name for out in graph.output}

    boundaries = []
    for layers in group_layers:
        members = set(layers)
        inputs: list[str] = []
        outputs: list[str] = []
        for node in graph.node:
            if node.name not in members:
                continue
            for tensor in node.input:
                if produced_by.get(tensor) not in members and tensor not in inputs:
                    inputs.append(tensor)
            for tensor in node.output:
                escapes = tensor in graph_outputs or any(
                    consumer not in members for consumer in consumers.get(tensor, [])
                )
                if escapes and tensor not in outputs:
                    outputs.append(tensor)
        boundaries.append((tuple(inputs), tuple(outputs)))
    return boundaries


def build_mapping(
    workload: StreamWorkload,
    kernel_kwargs: dict[str, dict],
    groups: Sequence[FusedGroup],
) -> dict:
    """The mapping for ``workload`` as a plain dict, validated against it.
    ``kernel_kwargs`` are each node's stream-dse kernel arguments, e.g. a GEMM's tile.
    """
    kernel_of = dict(workload.nodes)
    unknown = set(kernel_kwargs) - set(kernel_of)
    if unknown:
        raise ValueError(
            f"kernel arguments refer to nodes absent from the workload: {sorted(unknown)}"
        )

    grouped = [name for group in groups for name in group.layers]
    missing = [name for name in grouped if name not in kernel_kwargs]
    if missing:
        raise ValueError(
            f"fused groups refer to nodes without kernel arguments: {missing}"
        )

    layers = [
        {
            "name": name,
            "core_allocation": [],
            "inter_core_tiling": [],
            "kernel": {"name": kernel, "kwargs": dict(kernel_kwargs[name])},
        }
        for name, kernel in workload.nodes
        if name in kernel_kwargs
    ]
    return {
        "layers": layers,
        "fused_groups": [
            {
                "name": group.name,
                "layers": list(group.layers),
                "intra_core_tiling": [
                    {"dim": f"{node}.{dim}", "tile": tile}
                    for node, dim, tile in group.intra_core_tiling
                ],
            }
            for group in groups
        ],
        "runtime_args": {buffer: {} for buffer in workload.buffers},
    }


def emit_mapping(
    workload: StreamWorkload,
    kernel_kwargs: dict[str, dict],
    groups: Sequence[FusedGroup],
    path,
) -> str:
    """Write the mapping YAML to ``path`` and return it."""
    import yaml

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(
            build_mapping(workload, kernel_kwargs, groups),
            f,
            default_flow_style=False,
            sort_keys=False,
        )
    return str(path)
