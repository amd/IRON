# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing without a device: width candidates, the cost model, the
pack search, and the placer verdicts it keeps.

The costs are made up, composed as the probe measures them; the placer runs
mlir-aie's passes in process. Hardware checks a tuned graph against the
untuned one (``iron/tests/infrastructure/narrowing.py``).
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.declare import Profile
from iron.common.graph.costcache import Accuracy, CostCache, Measurement
from iron.common.graph.fold import folded
from iron.common.graph.narrowing import (
    Calibration,
    CostTable,
    JointNarrowing,
    Runlist,
    StepCost,
    cost_key,
    fitting,
    model_us,
    variants,
)
from iron.common.graph.probe import judge
from iron.common.harness import vectors
from iron.lm.layers import SwiGLU
from iron.operators import GELU, GEMM, MHA, ElementwiseAdd, ReLU, RoPE, SiLU
from iron.operators.flm import DequantBFP

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


class TwoExtents(iron.Graph):
    """An add at two extents, one array, with a silu between."""

    def body(self, a, b, c, d):
        t = ElementwiseAdd(a, b, tile_size=TILE)
        u = SiLU(ElementwiseAdd(c, d, tile_size=TILE), tile_size=TILE)
        return ElementwiseAdd(t, b, tile_size=TILE), u


class Rotate(iron.Graph):
    """RoPE over the first `n` positions, `n` given per call."""

    def body(self, x, angles, *, n: Scratchpad[np.int32]):
        return RoPE(x[:n], angles[:n])


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
        for w in map(dict, (v.tunables for v in found))
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
    profile = Profile()
    profile.add(ElementwiseAdd, num_aie_columns=2)
    with profile:
        found = variants(ElementwiseAdd(size=SIZE, tile_size=TILE), npu2)
    assert dict(found[0].tunables)["num_aie_columns"] == 2
    assert {dict(v.tunables)["num_aie_columns"] for v in found[1:]} == {8, 4, 2, 1}


def test_a_tunable_the_call_gives_is_not_searched(npu2):
    add = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=2)
    assert add.pinned == {"tile_size", "num_aie_columns"}
    found = variants(add, npu2)
    # Eight channels would take past the 16 MM2S channels of the shim row.
    assert [v.tunables for v in found] == [(("num_channels", c),) for c in (1, 4, 2)]
    assert {v.resolved.num_aie_columns for v in found} == {2}
    pinned = ElementwiseAdd(
        size=SIZE, tile_size=TILE, num_aie_columns=2, num_channels=1
    )
    assert [v.tunables for v in variants(pinned, npu2)] == [()]


class PinnedTwin(iron.Graph):
    """Two adds of one design, the second's columns given by its call."""

    def body(self, a, b):
        t = ElementwiseAdd(a, b, tile_size=TILE)
        return ElementwiseAdd(t, b, tile_size=TILE, num_aie_columns=8)


def test_a_design_keeps_a_tunable_any_of_its_calls_pins(tmp_path, npu2):
    traced = PinnedTwin().trace(a=(SIZE,), b=(SIZE,))
    free, pinned = (s.op for s in traced.steps)
    assert cost_key(free) == cost_key(pinned)
    steps = {}
    for v in variants(free, npu2):
        cols = dict(v.tunables)["num_aie_columns"]
        steps[v.key] = (4.0 + cols, 8.0 * cols)
    table = _table(tmp_path / "costs.json", steps)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(traced, npu2)
    assert tuning.chosen[cost_key(free)].resolved.num_aie_columns == 8
    narrowed, _ = tuning.apply(traced, npu2)
    assert {cost_key(s.op, npu2) for s in narrowed.steps} == {cost_key(free)}


def test_variants_leave_out_a_width_whose_bounded_transfers_do_not_fit(npu2):
    # Two lanes round-robin 1024 one-row tiles each: past a descriptor's 1023.
    op = Rotate().trace(x=(2048, 64), angles=(2048, 64)).steps[0].op
    found = variants(op, npu2)
    assert [dict(v.tunables)["num_aie_columns"] for v in found] == [8, 4, 1]


def test_derived_fields_are_not_widths(npu2):
    # resolve() sets GEMM's A shims and MHA's lanes from the other fields
    # whatever it is given, so a width there would be measured once per
    # value and built alike.
    gemm = GEMM(M=512, K=512, N=512)
    assert gemm.resolved(npu2).widths == {"num_aie_columns": 8}
    found = variants(gemm, npu2)
    assert len({v.key for v in found}) == len(found)
    assert MHA(num_heads=8, seq_pad=256).resolved(npu2).widths == {}
    with pytest.raises(TypeError, match="no tunable"):
        gemm.with_tunables(n_shim_mem_a=1)


def test_a_baked_replication_is_not_searched(npu2):
    # The join bakes DequantBFP's two n-halves, though a per= names them.
    assert DequantBFP(K=2048, N=2048).resolved(npu2).domains(npu2) == {
        "cols": (8, 4, 2, 1)
    }


def test_a_profile_refuses_a_derived_field():
    with pytest.raises(TypeError, match="derived or fixed"):
        Profile().add(GEMM, M=512, n_shim_mem_a=1)


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


def test_designs_of_one_array_load_it_once(tmp_path):
    table = _table(tmp_path / "costs.json", {"a": (1.0, 100.0), "b": (2.0, 100.0)})
    alone = model_us(table, ["a", "b", "a"])
    shared = model_us(table, ["a", "b", "a"], arrays={"a": 0, "b": 0})
    assert (alone[1], shared[1]) == (4, 2)
    # Three entries against one, each a base and one load; a reset in both.
    assert alone[0] - shared[0] == pytest.approx(2 * (30.0 + 100.0))


def _table(path, steps, dispatch=50.0, reset=30.0, base=30.0):
    """A table holding the given (t_step, load) per key, alone figures
    composed as the probe measures them.
    """
    table = CostTable(path)
    for key, (t_step, load) in steps.items():
        table.record_step(
            key,
            StepCost(
                t_step, dispatch + base + load + reset, True, True, "turbo", 1, 1, "-"
            ),
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
            cols = dict(v.tunables)["num_aie_columns"]
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
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(traced, npu2)
    add, silu = cost_key(ops["ElementwiseAdd"]), cost_key(ops["SiLU"])
    assert tuning.groups in (((add, silu),), ((silu, add),))
    assert tuning.unmeasured == (cost_key(ops["GELU"]),)
    assert f"unmeasured, left as traced: {cost_key(ops['GELU'])}" in tuning.report()
    # Every step but gelu's is in the pack: enter it, gelu, back into it.
    assert tuning.configures == 4
    keys = [cost_key(s.op) for s in traced.steps]
    chosen = {k: v.key for k, v in tuning.chosen.items()}
    assert tuning.predicted_us == pytest.approx(
        model_us(table, keys, tuning.groups, chosen)[0]
    )
    assert tuning.predicted_us < tuning.baseline_us


@pytest.mark.parametrize("accurate", [True, False])
def test_an_inexact_width_is_taken_only_if_accurate(accurate, tmp_path, npu2):
    traced, ops, table = _add_silu(tmp_path, npu2)
    key = cost_key(ops["ElementwiseAdd"])
    default, *others = variants(ops["ElementwiseAdd"], npu2)
    tuner = JointNarrowing(table, fit_cache=tmp_path / "fits")
    tuning = tuner.tune(traced, npu2)
    exact = tuning.chosen[key]
    assert exact.key != default.key and tuning.inexact == ()
    for v in others:
        table.record_step(
            v.key,
            dataclasses.replace(table.steps[v.key], exact=False, accurate=accurate),
        )
    tuning = tuner.tune(traced, npu2)
    assert tuning.chosen[key].key == (exact.key if accurate else default.key)
    assert tuning.inexact == ((key,) if accurate else ())
    assert ("not exact" in tuning.report()) == accurate


def test_apply_rebuilds_the_narrowed_steps(tmp_path, npu2):
    traced, ops, table = _add_silu(tmp_path, npu2)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(traced, npu2)
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


def test_designs_of_one_array_take_one_width(tmp_path, npu2):
    traced = TwoExtents().trace(a=(SIZE,), b=(SIZE,), c=(2 * SIZE,), d=(2 * SIZE,))
    small, large, silu, _ = (s.op for s in traced.steps)
    steps = {}
    for op in (small, large, silu):
        for v in variants(op, npu2):
            cols = dict(v.tunables)["num_aie_columns"]
            steps[v.key] = (4.0 + cols, 8.0 * cols)
    table = _table(tmp_path / "costs.json", steps)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(traced, npu2)
    # As traced, the adds' one array is entered twice around silu's.
    assert tuning.baseline_configures == 4
    adds = [tuning.chosen[cost_key(op)] for op in (small, large)]
    assert adds[0].tunables == adds[1].tunables and adds[0].array == adds[1].array
    # The pack names the array by its first design, which brings the other.
    assert tuning.groups == ((cost_key(small), cost_key(silu)),)
    assert tuning.configures == 2
    keys = [cost_key(s.op) for s in traced.steps]
    assert tuning.predicted_us == pytest.approx(
        model_us(
            table,
            keys,
            tuning.groups,
            {k: v.key for k, v in tuning.chosen.items()},
            {k: v.array for k, v in tuning.chosen.items()},
        )[0]
    )


def test_placer_verdicts_are_kept_across_tunings(tmp_path, npu2):
    traced, _, table = _add_silu(tmp_path, npu2)
    fit_cache = tmp_path / "fits"
    first = JointNarrowing(table, fit_cache=fit_cache).tune(traced, npu2)
    records = sorted(fit_cache.iterdir())
    assert records and all(r.read_text() == "fits" for r in records)
    widths = {k: v.tunables for k, v in first.chosen.items()}

    # A second tuning reads the verdicts rather than asking the placer: one
    # recorded as refused is taken as refused, and the pack moves to its
    # next-cheapest widths, which the placer is then asked about.
    for r in records:
        r.write_text("refused: recorded by the test")
    second = JointNarrowing(table, fit_cache=fit_cache).tune(traced, npu2)
    assert len(list(fit_cache.iterdir())) > len(records)
    assert second.groups == first.groups
    assert {k: v.tunables for k, v in second.chosen.items()} != widths


def test_a_setting_the_placer_refuses_alone_is_not_measured(tmp_path, npu2):
    # 128x128 B tiles double-buffered beside A and C are past a core's
    # memory at any column count; the default is kept for its build to say so.
    gemm = GEMM(M=2048, K=2048, N=2048, tile_m=64, tile_k=128, tile_n=128)
    found = variants(gemm, npu2)
    kept, refused = fitting(found, tmp_path / "fits")
    assert kept == found[:1]
    assert refused.keys() == {v.key for v in found[1:]} and refused
    assert all("could not be placed" in why for why in refused.values())
    assert fitting(found, tmp_path / "fits") == (kept, refused)


def _swiglu(tmp_path, dev, gate_us):
    """SwiGLU at one row as traced, and a table holding every design it runs
    as traced and folded at its default width, the folded gate taking
    ``gate_us`` a step and every other design 10.
    """
    E, H = 2048, 8192
    w = np.zeros((H, E), bfloat16)
    traced = SwiGLU(w, w, np.zeros((E, H), bfloat16)).trace(x=(1, E))
    folds, _ = folded(traced, dev)
    steps = {
        cost_key(s.op, dev): (10.0, 20.0) for g in (traced, folds) for s in g.steps
    }
    steps[cost_key(folds.steps[0].op, dev)] = (gate_us, 20.0)
    return traced, _table(tmp_path / "costs.json", steps)


def test_a_fold_is_taken_where_the_model_says_it_gains(tmp_path, npu2):
    traced, table = _swiglu(tmp_path, npu2, gate_us=11.0)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(traced, npu2)
    assert [str(f) for f in tuning.folds] == ["SiLU into GEMV"]
    assert "fold: SiLU into GEMV" in tuning.report()
    # The baseline is the graph as traced: gate and up, then silu, mul, down.
    assert tuning.baseline_configures == 4
    assert tuning.predicted_us < tuning.baseline_us
    applied, _ = tuning.apply(traced, npu2)
    assert [type(s.op).__name__ for s in applied.steps] == [
        "GEMV",
        "GEMV",
        "ElementwiseMul",
        "GEMV",
    ]
    assert [type(link.op) for link in applied.steps[0].op.finish] == [SiLU]


@pytest.mark.parametrize("gate_us", [400.0, None], ids=["dearer", "unmeasured"])
def test_a_fold_is_left_where_it_costs_or_is_unmeasured(gate_us, tmp_path, npu2):
    traced, table = _swiglu(tmp_path, npu2, gate_us=gate_us or 11.0)
    if gate_us is None:
        folds, _ = folded(traced, npu2)
        del table.steps[cost_key(folds.steps[0].op, npu2)]
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(traced, npu2)
    assert tuning.folds == ()
    assert [str(f) for f in tuning.unpriced] == ([] if gate_us else ["SiLU into GEMV"])
    assert ("unpriced, not taken: fold SiLU into GEMV" in tuning.report()) == (
        gate_us is None
    )
    applied, _ = tuning.apply(traced, npu2)
    assert [type(s.op).__name__ for s in applied.steps] == [
        type(s.op).__name__ for s in traced.steps
    ]


def test_cache_keys_follow_the_build_the_values_and_the_inputs(npu2):
    add = ElementwiseAdd(size=SIZE, tile_size=TILE)
    narrow = add.with_tunables(num_aie_columns=2)
    x = np.arange(SIZE, dtype=np.float32)
    key = CostCache.key(add)
    assert CostCache.key(ElementwiseAdd(size=SIZE, tile_size=TILE)) == key
    assert CostCache.key(add, {}, {}) == key
    others = [
        CostCache.key(narrow),
        CostCache.key(add, {"n": 1}),
        CostCache.key(add, {"n": 2}),
        CostCache.key(add, inputs={"a": x}),
        CostCache.key(add, inputs={"a": x + 1}),
    ]
    assert len({key, *others}) == 1 + len(others)


def test_cache_entries_round_trip_per_platform_and_mode(tmp_path):
    m = Measurement(4.0, 90.0, "ab" * 32, "turbo", 8, 50, "2026-10-06")
    cal = Calibration(50.0, 30.0, 30.0, 40.0, "turbo", 8, 50, "2026-10-06")
    cache = CostCache("NPU Strix Halo", "turbo", root=tmp_path)
    cache.put("k", m)
    cache.put("pair", cal)
    assert cache.directory == tmp_path / "npu-strix-halo" / "turbo"
    again = CostCache("NPU Strix Halo", "turbo", root=tmp_path)
    assert again.get("k", Measurement) == m
    assert again.get("pair", Calibration) == cal
    assert (
        CostCache("NPU Strix Halo", "default", root=tmp_path).get("k", Measurement)
        is None
    )
    assert CostCache("NPU Strix", "turbo", root=tmp_path).get("k", Measurement) is None
    # Exactness is against whichever width the table takes as default.
    assert m.cost("ab" * 32, False).exact and not m.cost("cd" * 32, False).exact
    # An inexact width is accurate only as judged; an exact one always is.
    assert m.cost("ab" * 32, False).accurate
    assert m.cost("cd" * 32, True).accurate and not m.cost("cd" * 32, False).accurate
    verdict = Accuracy(False, "C under the default's gate: 1 mismatch", "2026-10-07")
    judged = CostCache.judged_key("k", "w")
    assert judged not in {CostCache.beside_key("k", "w"), CostCache.pair_key("k", "w")}
    cache.put(judged, verdict)
    assert again.get(judged, Accuracy) == verdict


def _gemm_judged(npu2):
    """GEMM at its default tile_k and at 16, random inputs, its reference's
    output, and each width's bound on C.
    """
    default = GEMM(M=256, K=256, N=256)
    narrow = default.with_tunables(tile_k=16)
    v = vectors(default)
    bounds = [op.gate().bound(*v.inputs.values()) for op in (default, narrow)]
    return default, narrow, v, bounds


def test_a_width_within_its_default_s_gate_is_accurate(npu2):
    default, narrow, v, _ = _gemm_judged(npu2)
    verdict = judge(default, narrow, v.inputs, v.outputs)
    assert verdict.within and verdict.detail == ""


def test_a_width_past_its_default_s_bound_is_refused(npu2):
    default, narrow, v, (bound, _) = _gemm_judged(npu2)
    c = v["C"].astype(np.float32)
    c[0, 0] += 2 * bound[0, 0]
    verdict = judge(default, narrow, v.inputs, {"C": c.astype(bfloat16)})
    assert not verdict.within and verdict.detail.startswith("C under the default's")


def test_a_width_is_never_judged_by_its_looser_bound_alone(npu2):
    # tile_k=16 rounds the accumulator four times as often as 64 does.
    default, narrow, v, (tight, loose) = _gemm_judged(npu2)
    c = v["C"].astype(np.float32)
    c[0, 0] += 1.5 * tight[0, 0]
    c = c.astype(bfloat16)
    err = abs(float(c[0, 0]) - float(v["C"][0, 0]))
    assert tight[0, 0] < err < loose[0, 0]
    assert judge(narrow, narrow, v.inputs, {"C": c}).within
    assert not judge(default, narrow, v.inputs, {"C": c}).within


def test_a_declared_gate_judges_before_the_contract(npu2):
    rope = RoPE(rows=8, cols=64)
    v = vectors(rope, **RoPE.test.draw(rope))
    off = (v["y"].astype(np.float32) * 1.03).astype(bfloat16)
    assert judge(rope, rope, v.inputs, {"y": off}).within
    assert not judge(rope, rope, v.inputs, {"y": -v["y"]}).within


def test_an_exact_gate_or_a_short_bound_is_not_judged(npu2):
    relu = ReLU(size=64, num_aie_columns=1, tile_size=64)
    v = vectors(relu)
    assert judge(relu, relu, v.inputs, v.outputs) is None
    rope = Rotate().trace(x=(64, 64), angles=(64, 64)).steps[0].op
    v = vectors(rope)
    full = dict(valid=64, valid_angles=64)
    assert judge(rope, rope, v.inputs, v.outputs, full).within
    short = dict(valid=32, valid_angles=32)
    assert judge(rope, rope, v.inputs, v.outputs, short) is None
