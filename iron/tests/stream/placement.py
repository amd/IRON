#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Placements are written in array columns and resolved to stream's core ids.

An accelerator description gives every compute tile a ``[column, row]``
coordinate; :class:`~iron.common.stream.hardware.ComputeArray` is the only place
that reads it, so operators never spell out a core id.
"""

import pytest

pytest.importorskip(
    "stream", reason="stream-dse not installed (see requirements_stream.txt)"
)

from iron.common.stream.hardware import ComputeArray  # noqa: E402
from iron.operators.swiglu_prefill_stream import stream_design  # noqa: E402

ARRAY = stream_design.ARRAY

# The core ids this operator was measured with, on the whole-array Strix target.
MEASURED_ALLOCATION = {
    "Gemm_Left": [2, 3, 4, 5, 8, 9, 10, 11],
    "Gemm_Right": [14, 15, 16, 17, 20, 21, 22, 23],
    "Silu": [26, 27, 28, 29],
    "Elt_Mul": [32, 33, 34, 35],
    "Gemm_Down": [38, 39, 40, 41, 44, 45, 46, 47],
}


def test_array_matches_the_accelerator():
    assert (ARRAY.num_columns, ARRAY.num_rows) == (8, 4)
    assert ARRAY.all_columns == tuple(range(8))


def test_columns_hold_only_compute_tiles():
    ids = [core for column in ARRAY.columns for core in column]
    assert len(ids) == ARRAY.num_columns * ARRAY.num_rows
    assert len(set(ids)) == len(ids)


def test_cores_follow_column_then_row_order():
    assert ARRAY.cores([0]) == ARRAY.columns[0]
    assert ARRAY.cores([0, 1]) == ARRAY.columns[0] + ARRAY.columns[1]


def test_allocate_gives_disjoint_consecutive_columns():
    ranges = ARRAY.allocate([2, 2, 1, 1, 2])
    assert ranges == ((0, 1), (2, 3), (4,), (5,), (6, 7))
    flat = [column for group in ranges for column in group]
    assert len(set(flat)) == len(flat)


def test_allocate_rejects_an_oversubscribed_array():
    with pytest.raises(ValueError):
        ARRAY.allocate([ARRAY.num_columns, 1])


def test_emitted_allocation_is_the_measured_one(tmp_path):
    import yaml

    _, mapping_path = stream_design.build_inputs(
        256, 512, 2048, 32, 32, 64, tmp_path / "design"
    )
    emitted = {
        layer["name"]: layer["core_allocation"][0]
        for layer in yaml.safe_load(open(mapping_path))["layers"]
    }
    assert emitted == MEASURED_ALLOCATION


@pytest.mark.parametrize("accelerator", ["whole_array.yaml", "single_col.yaml"])
def test_other_accelerators_resolve(accelerator):
    import os

    import stream

    path = os.path.join(
        os.path.dirname(stream.__file__), "inputs", "aie", "hardware", accelerator
    )
    array = ComputeArray.from_accelerator(path)
    assert array.num_rows == 4
    assert array.cores(array.all_columns)
