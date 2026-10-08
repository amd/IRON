# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing without a device: width candidates, the cost model, the
pack search, and the placer verdicts and tunings it keeps.

The costs are made up, composed as the probe measures them; the placer runs
mlir-aie's passes in process. Hardware checks a tuned graph against the
untuned one (``iron/tests/infrastructure/narrowing.py``).
"""

import dataclasses
import json

import pytest

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
from iron.operators import GELU, GEMM, ElementwiseAdd, SiLU

SIZE = 8192
TILE = 256

pytestmark = pytest.mark.usefixtures("npu2")


class AddSilu(iron.Graph):
    """add, gelu, then silu and add alternating: add and silu are first used
    apart but adjacent five times.
    """

    def __init__(self):
        super().__init__()
        wide = dict(size=SIZE, tile_size=TILE)
        self.add = ElementwiseAdd(**wide)
        self.gelu = GELU(**wide)
        self.silu = SiLU(**wide)

    def body(self, a, b):
        x = self.gelu(self.add(a, b))
        for _ in range(3):
            x = self.add(self.silu(x), b)
        return x


def test_widths_are_the_settable_per_tunables(npu2):
    # SiLU fixes its channel count (init=False), so only its columns narrow.
    assert SiLU(size=SIZE, tile_size=TILE).widths == {"num_aie_columns": None}
    assert ElementwiseAdd(size=SIZE, tile_size=TILE).resolved(npu2).widths == {
        "num_aie_columns": 8,
        "num_channels": 1,
    }


def test_variants_range_over_every_width_the_shims_allow(npu2):
    found = variants(ElementwiseAdd(size=SIZE, tile_size=TILE), npu2)
    widths = [
        (w["num_aie_columns"], w["num_channels"])
        for w in map(dict, (v.widths for v in found))
    ]
    # The default first; none past the 16 MM2S channels of the shim row.
    assert widths == [
        (8, 1),
        (4, 2),
        (4, 1),
        (2, 4),
        (2, 2),
        (2, 1),
        (1, 8),
        (1, 4),
        (1, 2),
        (1, 1),
    ]
    # Two inputs per stream in, one out.
    assert all(
        (v.mm2s, v.s2mm) == (2 * c * k, c * k) for v, (c, k) in zip(found, widths)
    )
    assert len({v.key for v in found}) == len(found)


def test_variants_widen_a_default_its_resolution_keeps_narrow(npu2):
    found = variants(ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=2), npu2)
    assert dict(found[0].widths)["num_aie_columns"] == 2
    assert {dict(v.widths)["num_aie_columns"] for v in found[1:]} == {8, 4, 2, 1}


def test_variants_give_each_design_once(npu2):
    # GEMM resolves n_shim_mem_a to at most its columns: many settings, one design.
    found = variants(GEMM(M=2560, K=768, N=3072, b_col_maj=True), npu2)
    assert len({v.key for v in found}) == len(found)
    assert [dict(v.widths)["num_aie_columns"] for v in found] == [8, 4, 2, 1]


def test_a_narrowed_operator_keeps_its_fixed_fields():
    add = ElementwiseAdd(size=SIZE, tile_size=TILE)
    narrow = add.with_tunables(num_aie_columns=2)
    assert (narrow.size, narrow.tile_size, narrow.num_aie_columns) == (SIZE, TILE, 2)
    with pytest.raises(TypeError, match="no tunable"):
        add.with_tunables(size=SIZE // 2)


def test_entries_count_arrivals_into_a_device():
    runlist = Runlist(["a", "b", "a", "a", "c", "b", "c"])
    assert runlist.entries(frozenset("a")) == 2
    assert runlist.entries(frozenset("bc")) == 2
    assert runlist.entries(frozenset("abc")) == 1


def _table(path, steps, dispatch=50.0, reset=30.0, base=30.0):
    """A table holding the given (t_step, load) per key, alone figures
    composed as the probe measures them.
    """
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


def _add_silu(tmp_path, dev):
    """The traced graph, its operators by class, and a table holding every
    width of add and silu, and none of gelu.
    """
    traced = AddSilu().trace(a=(SIZE,), b=(SIZE,))
    ops = {type(s.op).__name__: s.op for s in traced.steps}
    steps = {}
    for name in ("ElementwiseAdd", "SiLU"):
        for v in variants(ops[name], dev):
            cols = dict(v.widths)["num_aie_columns"]
            steps[v.key] = (4.0 + cols, 8.0 * cols)
    return traced, ops, _table(tmp_path / "costs.json", steps)


def test_table_round_trips(tmp_path, npu2):
    _, _, table = _add_silu(tmp_path, npu2)
    table.save()
    again = CostTable(table.path)
    assert again.steps == table.steps and again.calibrations == table.calibrations
    assert again.base_us == table.base_us


def test_packs_designs_apart_in_first_use_order(tmp_path, npu2):
    # gelu is wide and has no narrower width in the table, so it cannot
    # pack; add and silu are first used apart but adjacent five times, so
    # they share a device.
    traced, ops, table = _add_silu(tmp_path, npu2)
    tuning = JointNarrowing(table, cache=tmp_path).tune(traced, npu2)
    add, silu = cost_key(ops["ElementwiseAdd"]), cost_key(ops["SiLU"])
    assert tuning.groups in (((add, silu),), ((silu, add),))
    assert tuning.unmeasured == (cost_key(ops["GELU"]),)
    # Every step but gelu's is in the pack: enter it, gelu, back into it.
    assert tuning.configures == 4
    keys = [cost_key(s.op) for s in traced.steps]
    chosen = {k: v.key for k, v in tuning.chosen.items()}
    assert tuning.predicted_us == pytest.approx(
        model_us(table, keys, tuning.groups, chosen)[0]
    )
    assert tuning.predicted_us < tuning.baseline_us


def test_apply_rebuilds_the_narrowed_steps(tmp_path, npu2):
    traced, ops, table = _add_silu(tmp_path, npu2)
    tuning = JointNarrowing(table, cache=tmp_path).tune(traced, npu2)
    narrowed, groups = tuning.apply(traced)
    # One operator per design still: every add step runs the one new add.
    by_class = {}
    for step in narrowed.steps:
        by_class.setdefault(type(step.op).__name__, set()).add(id(step.op))
    assert all(len(ids) == 1 for ids in by_class.values())
    assert [len(g) for g in groups] == [2]
    for op in groups[0]:
        want = tuning.chosen[cost_key(ops[type(op).__name__])]
        assert cost_key(op) == want.key
    # gelu is untouched: the same operator, not a copy.
    [gelu] = [s.op for s in narrowed.steps if isinstance(s.op, GELU)]
    assert gelu is ops["GELU"]


def test_placer_verdicts_are_kept_across_tunings(tmp_path, npu2):
    traced, _, table = _add_silu(tmp_path, npu2)
    fits = tmp_path / "fits"
    first = JointNarrowing(table, cache=tmp_path).tune(traced, npu2)
    records = sorted(fits.iterdir())
    assert records and all(r.read_text() == "fits" for r in records)
    widths = {k: v.widths for k, v in first.chosen.items()}

    # A second tuning reads the verdicts rather than asking the placer: one
    # recorded as refused is taken as refused, and the pack moves to its
    # next-cheapest widths, which the placer is then asked about. The
    # recorded tuning's pack is refused too, so it is searched again.
    for r in records:
        r.write_text("refused: recorded by the test")
    second = JointNarrowing(table, cache=tmp_path).tune(traced, npu2)
    assert len(list(fits.iterdir())) > len(records)
    assert second.groups == first.groups
    assert {k: v.widths for k, v in second.chosen.items()} != widths


def test_a_tuning_is_kept_for_its_runlist_and_table(tmp_path, npu2):
    traced, ops, table = _add_silu(tmp_path, npu2)
    first = JointNarrowing(table, cache=tmp_path).tune(traced, npu2)
    [record] = (tmp_path / "tunings").iterdir()
    assert first.groups

    # A second tuning takes the record, rebuilt, without searching: one
    # rewritten to leave every design at its default width, alone, is what
    # it returns.
    again = JointNarrowing(table, cache=tmp_path).tune(traced, npu2)
    assert again.groups == first.groups
    assert {k: v.key for k, v in again.chosen.items()} == {
        k: v.key for k, v in first.chosen.items()
    }
    record.write_text(json.dumps({"chosen": {}, "groups": []}))
    taken = JointNarrowing(table, cache=tmp_path).tune(traced, npu2)
    assert taken.groups == ()
    assert all(v.key == k for k, v in taken.chosen.items())
    assert taken.predicted_us == pytest.approx(taken.baseline_us)

    # Another table is another record, searched for.
    add = cost_key(ops["ElementwiseAdd"])
    table.record_step(add, dataclasses.replace(table.steps[add], t_step_us=1.0))
    searched = JointNarrowing(table, cache=tmp_path).tune(traced, npu2)
    assert len(list((tmp_path / "tunings").iterdir())) == 2
    assert searched.groups == first.groups
