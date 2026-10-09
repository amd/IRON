# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A checked-in cost table holds every design its model's tuner prices, and
nothing else: what ``measure_graph`` would run for it, found without a device.
"""

from pathlib import Path

import numpy as np
import pytest
from aie.iron.device import from_name

from iron.common.graph import tune as graph_tune
from iron.common.graph.narrowing import CostTable
from iron.common.graph.probe import Designs
from iron.lm import SEED, Sampler
from iron.lm.llama3 import tune as llama_tune
from iron.lm.tune import CALIBRATION_PAIRS, calls, contexts
from iron.tests.common.llama_model import llama_1b


@pytest.mark.parametrize(
    "dispatch, name",
    [("fused", "costs_npu2.json"), ("separate", "costs_npu2_separate.json")],
)
def test_llamas_table_holds_every_design_it_tunes(npu2, dispatch, name):
    sample = Sampler(0.7, 50, np.random.default_rng(SEED))
    designs = Designs.of(calls(llama_1b(), sample, 256, 0, 8192, 6), npu2)
    table = CostTable(Path(llama_tune.__file__).with_name(name))
    stale = designs.stale(table)
    missing = designs.missing(table, CALIBRATION_PAIRS)
    settings = {v.key: (vs[0], v) for vs in designs.settings.values() for v in vs}
    unmeasured = []
    for key in missing:
        if ">" in key:
            unmeasured.append(f"  entry {key}")
            continue
        if "@" in key:
            unmeasured.append(f"  operating point {key}")
            continue
        if key not in settings:
            unmeasured.append(f"  calibration or pack {key}")
            continue
        default, setting = settings[key]
        start = dict(default.tunables)
        moved = {n: x for n, x in setting.tunables if start[n] != x}
        unmeasured.append(
            f"  {key}: {type(setting.op).__name__} at {start}"
            + (f", moved to {moved}" if moved else ", its default")
        )
    assert not stale and not missing, (
        f"{table.path} is out of date; run `python -m iron.lm.llama3.tune "
        f"--dispatch {dispatch}` on an idle NPU2. {len(missing)} to measure:\n"
        + "\n".join(unmeasured)
        + f"\n{len(stale)} the graph no longer has: {stale}"
    )


def test_a_ladder_of_contexts_halves_down_and_weighs_each_by_its_share():
    found = contexts(8192, 6, 1)
    assert [c for _, c in found] == [256, 512, 1024, 2048, 4096, 8192]
    assert sum(w for w, _ in found) == pytest.approx(1.0)
    # The contexts past halfway to the one below: (8192 - 6144) / 8192.
    assert found[-1][0] == pytest.approx(0.25)
    assert [c for _, c in contexts(8192, 6, 2048)] == [2048, 4096, 8192]
    assert contexts(6144, 6, 2048) == [(1.0, 6144)]
    with pytest.raises(ValueError, match="not a multiple of 2048"):
        contexts(1000, 6, 2048)


def test_llama_prices_only_attention_at_its_contexts(npu2):
    sample = Sampler(0.7, 50, np.random.default_rng(SEED))
    designs = Designs.of(calls(llama_1b(1), sample, 256, 0, 8192, 6), npu2)
    priced = {k: designs.first[k][0] for k in designs.points}
    assert {type(op).__name__ for op in priced.values()} == {"MHA"}
    assert sorted(len(designs.points[k]) for k in priced) == [3, 6]
    for points in designs.points.values():
        assert sum(w for w, _ in points.values()) == pytest.approx(1.0)


@pytest.mark.parametrize(
    "device, argv, name",
    [
        ({"name": "npu2", "n_cols": 8}, [], "costs_npu2.json"),
        ({"name": "npu2", "n_cols": 8}, ["--dispatch", "fused"], "costs_npu2.json"),
        (
            {"name": "npu2", "n_cols": 8},
            ["--dispatch", "separate"],
            "costs_npu2_separate.json",
        ),
        ({"name": "npu1", "n_cols": 4}, [], "costs_npu1.json"),
        ({"name": "npu1", "n_cols": 4}, ["--dispatch", "separate"], "costs_npu1.json"),
        (
            {"name": "npu1", "n_cols": 4},
            ["--dispatch", "fused"],
            "costs_npu1_fused.json",
        ),
        (
            {"name": "npu2", "n_cols": 8},
            ["--table", "elsewhere.json"],
            "elsewhere.json",
        ),
    ],
)
def test_a_table_is_named_for_its_device_and_a_packaging_not_its_own(
    tmp_path, device, argv, name
):
    args = graph_tune.parser("", tmp_path).parse_args(argv)
    found = graph_tune.table(args, from_name(**device), tmp_path)
    assert found == (Path(name) if "--table" in argv else tmp_path / name)
