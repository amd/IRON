# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing: widths and packs chosen from measured costs.

The width candidates and the search are checked without a device; the
tuner end to end is checked on the NPU: its designs measured into a fresh
cost table, the graph compiled through ``GraphFunction.compile`` with the
tuner, and the tuned image run against the untuned one, bit for bit.
"""

import re

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.device import NPU2

import iron
from iron.common.graph.narrowing import (
    Calibration,
    CostTable,
    JointNarrowing,
    Runlist,
    StepCost,
    cost_key,
    model_us,
    variants,
)
from iron.common.graph.probe import Timing, calibrate, measure_steps
from iron.common.image import build_fused_mlir
from iron.operators import ElementwiseAdd, ElementwiseMul, GELU, SiLU

SIZE = 8192
TILE = 256


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(NPU2())
    yield
    aie_utils.set_current_device(previous)


def _chain_fn(a, b):
    x = SiLU(ElementwiseAdd(a, b, tile_size=TILE), tile_size=TILE)
    x = ElementwiseMul(x, b, tile_size=TILE)
    return SiLU(ElementwiseAdd(x, b, tile_size=TILE), tile_size=TILE)


def test_widths_are_the_settable_per_tunables():
    # SiLU fixes its channel count (init=False), so only its columns narrow.
    assert SiLU(size=SIZE, tile_size=TILE).ov.widths == ("num_aie_columns",)
    assert ElementwiseAdd(size=SIZE, tile_size=TILE).ov.widths == (
        "num_aie_columns",
        "num_channels",
    )


def test_variants_halve_down_to_one_column():
    found = variants(ElementwiseAdd(size=SIZE, tile_size=TILE), NPU2())
    assert [dict(v.widths)["num_aie_columns"] for v in found] == [8, 4, 2, 1]
    # Two inputs per column in, one out.
    assert [(v.mm2s, v.s2mm) for v in found] == [(16, 8), (8, 4), (4, 2), (2, 1)]
    assert len({v.key for v in found}) == 4


def test_entries_count_arrivals_into_a_device():
    runlist = Runlist(["a", "b", "a", "a", "c", "b", "c"])
    assert runlist.entries(frozenset("a")) == 2
    assert runlist.entries(frozenset("bc")) == 2
    assert runlist.entries(frozenset("abc")) == 1


def _table(path, steps, dispatch=50.0, reset=30.0, base=30.0):
    """A table holding the given (t_step, load) per key, alone figures
    composed as the probe measures them."""
    table = CostTable(path)
    for key, (t_step, load) in steps.items():
        table.record_step(
            key,
            StepCost(t_step, dispatch + base + load + reset, True, "turbo", 1, 1, "-"),
        )
    table.record_calibration(
        ("x", "y"),
        Calibration(dispatch, reset, base, base + 10, "turbo", 1, 1, "-"),
    )
    return table


def test_packs_designs_apart_in_first_use_order(tmp_path):
    # add, gelu, silu, then silu and add alternating. gelu is wide and has
    # no narrower width in the table, so it cannot pack; add and silu are
    # first used apart but adjacent five times, so they share a device.
    @iron.graph
    def fn(a, b):
        x = ElementwiseAdd(a, b, tile_size=TILE)
        x = GELU(x, tile_size=TILE)
        for _ in range(3):
            x = SiLU(x, tile_size=TILE)
            x = ElementwiseAdd(x, b, tile_size=TILE)
        return x

    traced = fn.trace(a=(SIZE,), b=(SIZE,))
    ops = {type(s.op).__name__: s.op for s in traced.steps}
    steps = {}
    for name in ("ElementwiseAdd", "SiLU"):
        for v in variants(ops[name], NPU2()):
            cols = dict(v.widths)["num_aie_columns"]
            steps[v.key] = (4.0 + cols, 8.0 * cols)
    table = _table(tmp_path / "costs.json", steps)
    tuning = JointNarrowing(table).tune(traced, NPU2())
    add, silu = cost_key(ops["ElementwiseAdd"]), cost_key(ops["SiLU"])
    assert tuning.groups == ((add, silu),) or tuning.groups == ((silu, add),)
    assert tuning.unmeasured == (cost_key(ops["GELU"]),)
    # Every step but gelu's is in the pack: enter it, gelu, back into it.
    assert tuning.configures == 4
    keys = [cost_key(s.op) for s in traced.steps]
    assert tuning.predicted_us == pytest.approx(
        model_us(
            table, keys, tuning.groups, {k: v.key for k, v in tuning.chosen.items()}
        )[0]
    )
    assert tuning.predicted_us < tuning.baseline_us


def test_tuned_graph_is_bit_identical_and_packed(tmp_path, npu_runtime):
    table = CostTable(tmp_path / "costs.json")
    traced = iron.graph(_chain_fn).trace(a=(SIZE,), b=(SIZE,))
    first = {}
    for s in traced.steps:
        first.setdefault(cost_key(s.op), s.op)
    timing = Timing(rounds=2, calls=10)
    for op in first.values():
        costs = measure_steps(table, variants(op, NPU2()), timing)
        assert all(c.exact for c in costs.values())
    add, silu = (variants(op, NPU2())[-1].op for op in list(first.values())[:2])
    calibrate(table, add, silu, timing)

    tuned = iron.graph(_chain_fn).compile(
        coresident=JointNarrowing(table), a=(SIZE,), b=(SIZE,)
    )
    plain = iron.graph(_chain_fn).compile(a=(SIZE,), b=(SIZE,))
    assert len(tuned.tuning.groups) == 1 and len(tuned.tuning.groups[0]) == 3
    text = build_fused_mlir(tuned.sequence)
    assert len(re.findall(r"aiex\.configure", text)) == tuned.tuning.configures == 2

    rng = np.random.default_rng(0)
    a = rng.standard_normal(SIZE).astype(bfloat16)
    b = rng.standard_normal(SIZE).astype(bfloat16)
    want = np.array(plain(a, b).numpy())
    got = np.array(tuned(a, b).numpy())
    assert want.tobytes() == got.tobytes()
