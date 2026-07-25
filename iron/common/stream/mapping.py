# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
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

from iron.common.stream.workload import StreamWorkload


@dataclass(frozen=True)
class Placement:
    """Where one workload node runs.

    ``cores`` lists the compute tiles per allocation, ``splits`` the matching
    inter-core tiling as ``(dim, split)`` pairs, and ``kernel_kwargs`` the
    arguments of the node's stream-dse kernel (e.g. a GEMM's tile shape).
    """

    cores: Sequence[Sequence[int]]
    splits: Sequence[Sequence[tuple[str, int]]] = ()
    kernel_kwargs: dict = field(default_factory=dict)


@dataclass(frozen=True)
class FusedGroup:
    """A set of nodes fused into one design, with its layer-fusion tiling.

    ``intra_core_tiling`` entries are ``(node_name, dim, tile)``. Splitting a
    workload into several groups makes stream-dse emit one design per group.
    """

    name: str
    layers: Sequence[str]
    intra_core_tiling: Sequence[tuple[str, str, int]] = ()


def _layer_entry(name: str, placement: Placement, kernel_key: str) -> dict:
    entry = {
        "name": name,
        "core_allocation": [list(cores) for cores in placement.cores],
        "inter_core_tiling": [
            [{"dim": dim, "split": split} for dim, split in group]
            for group in placement.splits
        ],
        "kernel": {"name": kernel_key, "kwargs": dict(placement.kernel_kwargs)},
    }
    return entry


def build_mapping(
    workload: StreamWorkload,
    placements: dict[str, Placement],
    groups: Sequence[FusedGroup],
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
        _layer_entry(name, placements[name], kernel)
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
    path,
) -> str:
    """Write the mapping YAML to ``path`` and return it."""
    import yaml

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(
            build_mapping(workload, placements, groups),
            f,
            default_flow_style=False,
            sort_keys=False,
        )
    return str(path)
