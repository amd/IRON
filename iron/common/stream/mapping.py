# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A candidate mapping of an exported workload: each layer's kernel and the fused groups.

Placement and tile sizes are left to stream-dse; the kernel arguments seed
its tile search.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

from .workload import StreamWorkload


@dataclass(frozen=True)
class FusedGroup:
    """Layers stream-dse generates one design for.

    Attributes:
        layers: Its layers, by name.
        post_ops: Those of its elementwise layers that run on the cores of
            the GEMM producing their input, on its output tile.
    """

    layers: Sequence[str]
    post_ops: Sequence[str] = ()


@dataclass(frozen=True)
class StreamMapping:
    """One mapping stream-dse may solve a workload under.

    Attributes:
        kernels: Each layer's stream-dse kernel arguments (a GEMM's call
            shape, say), by layer name.
        groups: The fused groups, in the order they run.
    """

    kernels: dict[str, dict[str, Any]]
    groups: Sequence[FusedGroup]

    def to_dict(self, workload: StreamWorkload) -> dict:
        """Return the mapping as stream-dse's YAML holds it, checked against ``workload``.

        Raises:
            ValueError: A layer named is not the workload's, or a grouped
                layer has no kernel arguments.
        """
        kernel_of = dict(workload.nodes)
        unknown = set(self.kernels) - set(kernel_of)
        if unknown:
            raise ValueError(
                f"kernel arguments name layers the workload has not: {sorted(unknown)}"
            )
        grouped = [name for group in self.groups for name in group.layers]
        missing = [name for name in grouped if name not in self.kernels]
        if missing:
            raise ValueError(f"grouped layers without kernel arguments: {missing}")
        return {
            "layers": [
                {
                    "name": name,
                    "core_allocation": [],
                    "kernel": {"name": kernel, "kwargs": dict(self.kernels[name])},
                }
                for name, kernel in workload.nodes
                if name in self.kernels
            ],
            "fused_groups": [
                {
                    "name": f"group_{index}",
                    "layers": list(group.layers),
                    **({"post_ops": list(group.post_ops)} if group.post_ops else {}),
                }
                for index, group in enumerate(self.groups)
            ],
            "runtime_args": {buffer: {} for buffer in workload.buffers},
        }

    def write(self, workload: StreamWorkload, path) -> str:
        """Write the mapping's YAML to ``path`` and return the path."""
        import yaml

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            yaml.dump(
                self.to_dict(workload), f, default_flow_style=False, sort_keys=False
            )
        return str(path)
