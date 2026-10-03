# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The one path from an operator's exported workload and mapping to a generated design.
An operator gives its family name, shape string and design knobs; the accelerator, solver,
output root and design-cache key are chosen here."""

import json
import os

import stream

from iron.common.stream.design import (
    stream_revision,
    trace_size,
    trace_tiles,
    traced_tiles,
)
from iron.common.stream.hardware import array
from iron.common.stream.kernel_library import library
from iron.common.stream.kernel_library import revision as library_revision

ACCELERATOR = os.path.join(
    os.path.dirname(stream.__file__),
    "inputs",
    "aie",
    "hardware",
    "whole_array_strix.yaml",
)
BACKEND = os.environ.get("STREAM_BACKEND", "ortools_gscip")
OUTPUT_ROOT = "outputs"
ESTIMATE = "estimate.json"
# Reports what every tile DMA, the shim's measured bandwidth and each link carry per iteration;
# with neither bound set it adds no constraint, so the design stream returns is unchanged.
PORT_REPORT = {"memory_ports": {"interval": False, "burst": False}}


def experiment_id(family: str, shape: str, suffix: str = "") -> str:
    """The design-cache key: every knob that changes the generated design must appear."""
    hardware = os.path.splitext(os.path.basename(ACCELERATOR))[0]
    grid = array()
    if trace_size():
        tiles = "_".join(f"{col}.{row}" for col, row in traced_tiles())
        suffix += (
            f"_traced{trace_size()}_n{trace_tiles()}{'_' + tiles if tiles else ''}"
        )
    return (
        f"{hardware}-{family}{suffix}_{shape}"
        f"-{grid.num_rows}_row_{grid.num_columns}_col-{BACKEND}"
        f"-{stream_revision()}{library_revision()}"
    )


def design_dir(experiment_id: str) -> str:
    return os.path.join(OUTPUT_ROOT, experiment_id)


def solve_options(npu: str, kernel_library=None):
    """How every solve runs: no link or off-chip contention (traced core idle time here is
    lock stall, not route queueing), tile sizes searched around the mapping's seed, and port
    activity reported."""
    from stream.api import SolveOptions
    from stream.opt.solver.solver import ConstraintSelection

    return SolveOptions(
        backend=BACKEND,
        nb_cols_to_use=array().num_columns,
        constraint_selection=ConstraintSelection(
            transfer_contention=False, offchip_contention=False
        ),
        kernel_library=kernel_library or library(),
        tile_search=True,
        families=[PORT_REPORT],
        stage_options={
            "npu": npu,
            "trace_size": trace_size(),
            "trace_max_tiles": trace_tiles(),
            "trace_tiles": traced_tiles(),
        },
    )


def run_partition_codegen(
    experiment_id: str, workload_path, candidate_mappings, npu: str
) -> int:
    """Price each candidate mapping with its own solve, build the cheapest, and return its index."""
    from stream.api import select_mapping

    candidates = [str(path) for path in candidate_mappings]
    best = select_mapping(
        ACCELERATOR,
        str(workload_path),
        design_dir(experiment_id),
        candidates,
        solve_options(npu),
    )
    run_codegen(experiment_id, workload_path, best.mapping, npu)
    return candidates.index(best.mapping)


def run_codegen(
    experiment_id: str, workload_path, mapping_path, npu: str, kernel_library=None
) -> None:
    """Solve the allocation, write each fused group's MLIR under the design directory, and
    record stream's estimate of it beside them."""
    from stream.api import generate_code

    estimate = generate_code(
        ACCELERATOR,
        str(workload_path),
        design_dir(experiment_id),
        str(mapping_path),
        solve_options(npu, kernel_library),
    )
    write_estimate(design_dir(experiment_id), estimate)


def write_estimate(directory: str, estimate) -> None:
    """stream's cycles for one run of the design, per fused group and for the dispatch, and per
    group its steady-state latency and port-activity rows (busiest first): bits per iteration
    against each resource's bandwidth and the initiation interval."""
    performance = {
        index: (allocation or {}).get("performance") or {}
        for index, allocation in sorted(
            estimate.context.get("group_allocations").items()
        )
    }
    record = {
        "cycles": estimate.cycles,
        "group_cycles": list(estimate.group_cycles),
        "dispatch_cycles": estimate.dispatch_cycles,
        "groups": {
            f"group_{index}": {
                "latency": view.get("latency"),
                "port_activity": view.get("memory_ports", []),
            }
            for index, view in performance.items()
        },
    }
    with open(os.path.join(directory, ESTIMATE), "w") as f:
        json.dump(record, f, indent=1)
