# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The one path from an exported workload and its candidate mappings to stream-dse's designs.

Every solve runs here, under the same options, and is cached under
``$NPU_CACHE_HOME/stream/``, keyed by what the operator names it by, the
candidate mappings, the options (the kernel library among them) and the
installed stream-dse's version: nothing is solved twice, and nothing is
written to the working directory. ``STREAM_BACKEND`` names the solver
(OR-Tools GSCIP by default). stream-dse bounds each allocation solve in
time (``SolveOptions.time_limit_s``) and takes the best design found by
then, so a solve that reaches the bound can differ between hosts.
"""

from __future__ import annotations

import dataclasses
import fcntl
import hashlib
import json
import logging
import os
from collections.abc import Sequence
from importlib import metadata
from pathlib import Path
from typing import Any

from aie.utils.compile import NPU_CACHE_HOME

from .hardware import ComputeArray, accelerator
from .mapping import StreamMapping
from .workload import StreamWorkload

logger = logging.getLogger(__name__)

ROOT = NPU_CACHE_HOME / "stream"
SOLUTION = "solution.json"
# The constraint families every solve builds with options other than
# stream-dse's defaults: contention between transfers and the memory-port
# bounds are left out of the model, and stream-dse bounds each step by each
# core's own input stream instead. The kernel library's cycles and the
# operators' device runs are of designs solved this way; a change here needs
# both measured again.
FAMILY_OPTIONS = {
    "overlap": {"transfer_contention": False, "offchip_contention": False},
    "memory_ports": {"interval": False, "burst": False},
}


def backend() -> str:
    return os.environ.get("STREAM_BACKEND", "ortools_gscip")


def stream_version() -> str:
    return metadata.version("stream-dse")


def solve_options(dev, library):
    """Return how every solve runs.

    The whole array, the tile sizes searched around each mapping's seed,
    and stream-dse's default constraint families under ``FAMILY_OPTIONS``.
    """
    from stream.api import (
        SolveOptions,
        default_families,
    )  # pyright: ignore[reportMissingImports]

    return SolveOptions(
        backend=backend(),
        nb_cols_to_use=ComputeArray.from_device(dev).num_columns,
        kernel_library=library,
        tile_search=True,
        artifacts=False,
        families=default_families(accelerator(dev), options=FAMILY_OPTIONS),
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


def solve_digest(
    key: Any,
    workload: StreamWorkload,
    candidates: Sequence[StreamMapping],
    dev,
    library,
) -> str:
    """Return the digest of everything a design is a function of."""
    mappings = [candidate.to_dict(workload) for candidate in candidates]
    token = repr((key, mappings, solve_options(dev, library), stream_version()))
    return hashlib.sha256(token.encode()).hexdigest()[:16]


def solve(
    name: str,
    key: Any,
    workload: StreamWorkload,
    candidates: Sequence[StreamMapping],
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
            ``repr`` is part of ``solve_digest``.
        workload: The exported workload.
        candidates: The mappings stream-dse chooses between.
        dev: The device solved for.
        library: The ``KernelLibrary`` the solve prices and binds kernels by.

    Raises:
        RuntimeError: No candidate can be allocated.
    """
    from stream.api import (
        generate_code,
        select_mapping,
    )  # pyright: ignore[reportMissingImports]

    hardware = accelerator(dev)
    options = solve_options(dev, library)
    digest = solve_digest(key, workload, candidates, dev, library)
    directory = ROOT / f"{name}-{digest}"
    directory.mkdir(parents=True, exist_ok=True)
    with open(directory / ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if (directory / SOLUTION).exists():
            return Solution.load(directory)
        inputs = directory / "inputs"
        workload_path = workload.write(inputs / "workload.onnx")
        paths = [
            candidate.write(workload, inputs / f"candidate_{i}.yaml")
            for i, candidate in enumerate(candidates)
        ]
        chosen, priced = 0, None
        if len(paths) > 1:
            priced = select_mapping(
                hardware, workload_path, str(directory), paths, options
            )
            chosen = next(i for i, path in enumerate(paths) if path == priced.mapping)
        logger.info("%s: building candidate %d of %d", name, chosen, len(paths))
        estimate = generate_code(
            hardware,
            workload_path,
            str(directory),
            paths[chosen],
            options,
            estimate=priced,
        )
        solution = Solution(
            directory,
            chosen,
            tuple(tuple(group.layers) for group in candidates[chosen].groups),
            estimate.cycles,
            tuple(estimate.group_cycles),
            estimate.dispatch_cycles,
        )
        solution.save()
        return solution
