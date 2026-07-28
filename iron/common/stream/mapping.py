# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Emit the stream-dse mapping for an exported workload.

An operator declares *where* each node runs (:class:`Placement`) and how nodes
are fused (:class:`FusedGroup`); this module turns that into the mapping YAML
stream-dse consumes. Node names are taken from the
:class:`~iron.common.stream.workload.StreamWorkload` the ONNX was generated from,
and every placement is checked against it, so a mapping can never refer to a node
the workload does not contain.

The placement is deliberately explicit -- which compute tiles a layer occupies is
a hardware decision worth reading in one place -- while the repetitive YAML
plumbing is generated. Placements carry no absolute tensor dimensions, only tile
sizes and core sets, so they hold across problem sizes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from iron.common.stream.hardware import ComputeArray
from iron.common.stream.workload import StreamWorkload


@dataclass(frozen=True)
class Placement:
    """Where one workload node runs.

    ``columns`` are the array columns it occupies, resolved to core ids against
    the :class:`~iron.common.stream.hardware.ComputeArray`; ``rows`` narrows that
    to some rows of each column (all of them by default); ``splits`` is the
    inter-core tiling as ``(dim, split)`` pairs; ``kernel_kwargs`` are the
    arguments of the node's stream-dse kernel (e.g. a GEMM's tile shape).
    """

    columns: Sequence[int]
    splits: Sequence[tuple[str, int]] = ()
    kernel_kwargs: dict = field(default_factory=dict)
    rows: Sequence[int] | None = None


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


def _layer_entry(
    name: str, placement: Placement, kernel_key: str, array: ComputeArray
) -> dict:
    return {
        "name": name,
        "core_allocation": [list(array.cores(placement.columns, placement.rows))],
        "inter_core_tiling": [
            [{"dim": dim, "split": split} for dim, split in placement.splits]
        ],
        "kernel": {"name": kernel_key, "kwargs": dict(placement.kernel_kwargs)},
    }


def build_mapping(
    workload: StreamWorkload,
    placements: dict[str, Placement],
    groups: Sequence[FusedGroup],
    array: ComputeArray,
) -> dict:
    """The mapping for ``workload`` as a plain dict (validated against it)."""
    kernel_of = dict(workload.nodes)
    unknown = set(placements) - set(kernel_of)
    if unknown:
        raise ValueError(
            f"placements refer to nodes absent from the workload: {sorted(unknown)}"
        )

    grouped = [name for group in groups for name in group.layers]
    missing = [name for name in grouped if name not in placements]
    if missing:
        raise ValueError(f"fused groups refer to nodes without a placement: {missing}")

    layers = [
        _layer_entry(name, placements[name], kernel, array)
        for name, kernel in workload.nodes
        if name in placements
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
    placements: dict[str, Placement],
    groups: Sequence[FusedGroup],
    array: ComputeArray,
    path,
) -> str:
    """Write the mapping YAML to ``path`` and return it."""
    import yaml

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(
            build_mapping(workload, placements, groups, array),
            f,
            default_flow_style=False,
            sort_keys=False,
        )
    return str(path)
