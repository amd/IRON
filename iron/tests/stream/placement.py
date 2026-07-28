#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Placements are written in array columns and resolved to stream's core ids.

:class:`~iron.common.stream.hardware.ComputeArray` reads the grid from the
mlir-aie device IRON is building for, and is the only place that knows what a
stream core id means, so operators never spell one out.
"""

import pytest

pytest.importorskip(
    "stream", reason="stream-dse not installed (see requirements_stream.txt)"
)

import aie.utils as aie_utils  # noqa: E402
from aie.iron.device import NPU2  # noqa: E402

aie_utils.set_current_device(NPU2())

from iron.common.stream.hardware import ComputeArray  # noqa: E402
from iron.operators.swiglu_prefill_stream import stream_design  # noqa: E402

ARRAY = stream_design.array()

DIMS = (256, 512, 2048)

# The core ids the fused placement resolves to on the whole-array Strix target.
MEASURED_ALLOCATION = {
    "Gemm_Left": [2, 3, 4, 5, 8, 9, 10, 11],
    "Gemm_Right": [14, 15, 16, 17, 20, 21, 22, 23],
    "Silu": [26, 27, 28, 29],
    "Elt_Mul": [32, 33, 34, 35],
    "Gemm_Down": [38, 39, 40, 41, 44, 45, 46, 47],
}


def test_array_matches_the_device():
    assert (ARRAY.num_columns, ARRAY.num_rows) == (8, 4)
    assert ARRAY.all_columns == tuple(range(8))


def test_columns_hold_only_compute_tiles():
    ids = [core for column in ARRAY.columns for core in column]
    assert len(ids) == ARRAY.num_columns * ARRAY.num_rows
    assert len(set(ids)) == len(ids)


def test_cores_follow_column_then_row_order():
    assert ARRAY.cores([0]) == ARRAY.columns[0]
    assert ARRAY.cores([0, 1]) == ARRAY.columns[0] + ARRAY.columns[1]


def test_rows_narrow_a_placement_to_one_worker_per_column():
    """The shape IRON's channeled operators give an elementwise layer."""
    assert ARRAY.cores(ARRAY.all_columns, rows=[0]) == tuple(
        column[0] for column in ARRAY.columns
    )


def test_allocate_gives_disjoint_consecutive_columns():
    ranges = ARRAY.allocate([2, 2, 1, 1, 2])
    assert ranges == ((0, 1), (2, 3), (4,), (5,), (6, 7))
    flat = [column for group in ranges for column in group]
    assert len(set(flat)) == len(flat)


def test_allocate_rejects_an_oversubscribed_array():
    with pytest.raises(ValueError):
        ARRAY.allocate([ARRAY.num_columns, 1])


def test_ids_agree_with_the_accelerator_stream_solves_against():
    """IRON derives core ids from the device; stream-dse reads them from its own
    accelerator description. A design is only correct while the two agree."""
    import os

    import stream
    import yaml

    path = os.path.join(
        os.path.dirname(stream.__file__),
        "inputs",
        "aie",
        "hardware",
        "whole_array_strix.yaml",
    )
    description = yaml.safe_load(open(path))
    by_column: dict[int, list[tuple[int, int]]] = {}
    for core_id, coordinate in description["core_coordinates"].items():
        if description["cores"][core_id].endswith("aie_tile.yaml"):
            column, row = coordinate
            by_column.setdefault(column, []).append((row, core_id))
    expected = tuple(
        tuple(core_id for _, core_id in sorted(rows))
        for _, rows in sorted(by_column.items())
    )
    assert ARRAY.columns == expected


def test_emitted_allocation_resolves_to_the_expected_cores(tmp_path):
    import yaml

    _, mapping_path = stream_design.build_inputs(*DIMS, tmp_path / "design")
    emitted = {
        layer["name"]: layer["core_allocation"][0]
        for layer in yaml.safe_load(open(mapping_path))["layers"]
    }
    assert emitted == MEASURED_ALLOCATION


def test_layer_by_layer_gives_every_layer_the_whole_array(tmp_path):
    import yaml

    _, mapping_path = stream_design.build_inputs(
        *DIMS, tmp_path / "design_k5", k=stream_design.LAYER_BY_LAYER
    )
    mapping = yaml.safe_load(open(mapping_path))
    columns = {
        layer["name"]: {
            core // (ARRAY.num_rows + 2) for core in layer["core_allocation"][0]
        }
        for layer in mapping["layers"]
    }
    assert all(used == set(ARRAY.all_columns) for used in columns.values())
    assert len(mapping["fused_groups"]) == stream_design.LAYER_BY_LAYER


def test_devices_other_than_the_default_resolve():
    from aie.iron.device import NPU1

    array = ComputeArray.from_device(NPU1())
    assert array.num_columns and array.num_rows
    assert array.cores(array.all_columns)
