# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The one path from an exported workload and its candidate mappings to stream-dse's designs.

Every solve runs here, under the same options, and is cached under
``$NPU_CACHE_HOME/stream/``, keyed by what the operator names it by, the
candidates' text, the options (the kernel library among them) and the
installed stream-dse's sources: nothing is solved twice, and nothing is
written to the working directory. ``STREAM_BACKEND`` names the solver (OR-Tools GSCIP by default).
"""

# stream-dse, torch and onnxscript are requirements_stream.txt's.
# pyright: reportMissingImports=false

from __future__ import annotations

import dataclasses
import fcntl
import hashlib
import json
import logging
import os
from collections.abc import Sequence
from functools import cache
from importlib import metadata
from pathlib import Path
from typing import Any

from aie.utils.compile import NPU_CACHE_HOME
from aie.utils.compile.jit.operator import Unresolvable

from .hardware import ComputeArray
from .mapping import emit_mapping
from .workload import StreamWorkload

logger = logging.getLogger(__name__)

ROOT = NPU_CACHE_HOME / "stream"
# The stream-dse hardware description of each device, by its name.
ACCELERATORS = {"npu2": "whole_array_strix.yaml"}
SOLUTION = "solution.json"
# Per group, what the solve keeps resident in each memory (its memory_occupancy report).
OCCUPANCY = "occupancy.json"


def backend() -> str:
    return os.environ.get("STREAM_BACKEND", "ortools_gscip")


@cache
def stream_revision() -> str:
    """Return a token of the installed stream-dse's sources.

    Their modification times, not a commit, so an uncommitted edit counts.
    """
    import stream

    root = Path(stream.__file__).parent
    stamps = sorted(
        (str(path.relative_to(root)), path.stat().st_mtime_ns)
        for pattern in ("*.py", "*.yaml", "*.toml")
        for path in root.rglob(pattern)
    )
    version = metadata.version("stream-dse")
    return hashlib.sha256(f"{version}{stamps}".encode()).hexdigest()[:12]


def accelerator(dev) -> str:
    """Return the stream-dse hardware description of ``dev``.

    Raises:
        Unresolvable: stream-dse describes no such device.
    """
    import stream

    name = ACCELERATORS.get(dev.name)
    if name is None:
        raise Unresolvable(
            f"stream-dse has no hardware description of {dev.name}, only of "
            f"{sorted(ACCELERATORS)}"
        )
    return str(Path(stream.__file__).parent / "inputs" / "aie" / "hardware" / name)


def solve_options(dev, library):
    """Return how every solve runs.

    No link or off-chip contention, tile sizes searched around the
    mapping's seed, and each group's memory port activity reported.
    """
    from stream.api import SolveOptions, default_families

    overlap = {"overlap": {"transfer_contention": False, "offchip_contention": False}}
    ports = {"memory_ports": {"interval": False, "burst": False}}
    families = [
        ports if family == "memory_ports" else family
        for family in default_families(accelerator(dev), options=overlap)
    ]
    if ports not in families:
        families.append(ports)
    return SolveOptions(
        backend=backend(),
        nb_cols_to_use=ComputeArray.from_device(dev).num_columns,
        kernel_library=library,
        tile_search=True,
        artifacts=False,
        families=families,
        stage_options={"npu": dev.name},
    )


@dataclasses.dataclass(frozen=True)
class Solution:
    """stream-dse's design of a workload, on disk.

    Attributes:
        directory: Where it was solved, each group's design under
            ``group_<i>/codegen/``.
        candidate: Which of the candidate mappings was built.
        groups: Each fused group's layers, in the order they run.
        cycles: stream-dse's estimate of one call: its groups' and the
            dispatches between them.
        group_cycles: Each group's estimate.
        dispatch_cycles: The dispatches' estimate.
    """

    directory: Path
    candidate: int
    groups: tuple[tuple[str, ...], ...]
    cycles: float
    group_cycles: tuple[float, ...]
    dispatch_cycles: float

    def codegen(self, group: int) -> Path:
        """Return the directory of group ``group``'s ``final.mlir`` and ``kernels.json``."""
        return self.directory / f"group_{group}" / "codegen"

    @classmethod
    def load(cls, directory: Path) -> Solution:
        record = json.loads((directory / SOLUTION).read_text())
        return cls(
            directory,
            record["candidate"],
            tuple(tuple(g) for g in record["groups"]),
            record["cycles"],
            tuple(record["group_cycles"]),
            record["dispatch_cycles"],
        )

    def save(self) -> None:
        record = dataclasses.asdict(self)
        del record["directory"]
        (self.directory / SOLUTION).write_text(json.dumps(record, indent=1) + "\n")


def solve(
    name: str,
    key: Any,
    workload: StreamWorkload,
    candidates: Sequence[tuple[dict[str, dict], Sequence[Any]]],
    dev,
    library,
) -> Solution:
    """Return stream-dse's design of ``workload`` under the cheapest of ``candidates``.

    Several candidates are priced by ``select_mapping`` and the cheapest
    built; one is built as it is. A process solving the same key waits for
    the other's solution.

    Args:
        name: What the cache directory is named by.
        key: What, beside the candidates, the design is a function of; its
            ``repr`` is part of the cache key.
        workload: The exported workload.
        candidates: Each candidate mapping, as ``emit_mapping``'s kernel
            arguments and fused groups.
        dev: The device solved for.
        library: The ``KernelLibrary`` the solve prices and binds kernels by.

    Raises:
        RuntimeError: No candidate can be allocated.
    """
    from stream.api import generate_code, select_mapping

    from .mapping import build_mapping

    texts = [repr(build_mapping(workload, *c)) for c in candidates]
    options = solve_options(dev, library)
    token = repr((key, texts, repr(options), dev.name, stream_revision()))
    directory = ROOT / f"{name}-{hashlib.sha256(token.encode()).hexdigest()[:16]}"
    directory.mkdir(parents=True, exist_ok=True)
    with open(directory / ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if (directory / SOLUTION).exists():
            return Solution.load(directory)
        inputs = directory / "inputs"
        workload_path = workload.write(inputs / "workload.onnx")
        mappings = [
            emit_mapping(workload, *c, inputs / f"candidate_{i}.yaml")
            for i, c in enumerate(candidates)
        ]
        chosen = 0
        if len(mappings) > 1:
            best = select_mapping(
                accelerator(dev), workload_path, str(directory), mappings, options
            )
            chosen = mappings.index(best.mapping)
        logger.info("%s: building candidate %d of %d", name, chosen, len(mappings))
        estimate = generate_code(
            accelerator(dev), workload_path, str(directory), mappings[chosen], options
        )
        _, groups = candidates[chosen]
        solution = Solution(
            directory,
            chosen,
            tuple(tuple(g.layers) for g in groups),
            estimate.cycles,
            tuple(estimate.group_cycles),
            estimate.dispatch_cycles,
        )
        allocations = estimate.context.get("group_allocations") or {}
        occupancy = {
            group: ((allocation or {}).get("performance") or {}).get("memory_occupancy")
            for group, allocation in sorted(allocations.items())
        }
        (directory / OCCUPANCY).write_text(json.dumps(occupancy, indent=1) + "\n")
        solution.save()
        return solution
