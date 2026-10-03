#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON reads the compute grid from the mlir-aie device and leaves placement to stream:
only :class:`~iron.common.stream.hardware.ComputeArray` knows what a stream core id means,
and the emitted mapping declares no cores."""

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


def test_array_matches_the_device():
    assert (ARRAY.num_columns, ARRAY.num_rows) == (8, 4)


def test_columns_hold_only_compute_tiles():
    ids = [core for column in ARRAY.columns for core in column]
    assert len(ids) == ARRAY.num_columns * ARRAY.num_rows
    assert len(set(ids)) == len(ids)


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


def test_the_mapping_declares_no_placement(tmp_path):
    """Placement is stream's: every emitted layer carries a kernel and no cores."""
    import yaml

    _, mapping_path = stream_design.build_inputs(*DIMS, tmp_path / "design")
    for layer in yaml.safe_load(open(mapping_path))["layers"]:
        assert layer["core_allocation"] == []
        assert layer["inter_core_tiling"] == []
        assert layer["kernel"]["name"]


def test_layer_by_layer_emits_one_group_per_layer(tmp_path):
    import yaml

    _, mapping_path = stream_design.build_inputs(
        *DIMS, tmp_path / "design_k5", k=stream_design.LAYER_BY_LAYER
    )
    mapping = yaml.safe_load(open(mapping_path))
    assert len(mapping["fused_groups"]) == stream_design.LAYER_BY_LAYER
    assert all(len(group["layers"]) == 1 for group in mapping["fused_groups"])


def test_devices_other_than_the_default_resolve():
    from aie.iron.device import NPU1

    array = ComputeArray.from_device(NPU1())
    assert array.num_columns and array.num_rows
