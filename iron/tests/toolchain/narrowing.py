# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing without a device: width candidates, the cost model, the
pack search, and the placer verdicts it keeps.

The costs are made up, composed as the probe measures them; the placer runs
mlir-aie's passes in process. Hardware checks a tuned graph against the
untuned one (``iron/tests/infrastructure/narrowing.py``).
"""

import dataclasses
from collections import Counter
from pathlib import Path

import numpy as np
import pytest
from aie.iron.device import from_name
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
    PackCost,
    Runlist,
    StepCost,
    cost_key,
    fitting,
    model_us,
    variants,
)
from iron.common.graph.probe import Call, Designs, judge
from iron.common.harness import vectors
from iron.lm.layers import SwiGLU
from iron.operators import (
    GELU,
    GEMM,
    GEMV,
    MHA,
    Clamp,
    ElementwiseAdd,
    GQAContext,
    ReLU,
    RoPE,
    Sample,
    SiLU,
    Softmax,
)
from iron.operators.flm import GEMM as FlmGEMM
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


class TwoClamps(iron.Graph):
    """Two clamps of one shape, apart only in their bounds."""

    def body(self, x):
        y = Clamp(x, low=-0.75, high=1.25, tile_size=TILE)
        return Clamp(y, low=-3e4, high=3e4, tile_size=TILE)


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
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "fused"
    )
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
    mha = MHA(num_heads=8, seq_pad=256).resolved(npu2)
    assert mha.widths == {"num_pipelines": 1}
    assert mha.domains(npu2) == {
        "num_pipelines": (8, 4, 2, 1),
        "B_q": (256, 128, 64),
        "B_kv": (256, 128, 64),
    }
    with pytest.raises(TypeError, match="no tunable"):
        gemm.with_tunables(n_shim_mem_a=1)


def test_gemm_searches_tile_k_only_where_c_accumulates_in_f32(npu2):
    plain = GEMM(M=2048, K=2048, N=2048).resolved(npu2)
    assert set(plain.domains(npu2)) == {"num_aie_columns", "tile_m", "tile_n"}
    exact = GEMM(M=2048, K=2048, N=2048, prio_accuracy=True).resolved(npu2)
    assert set(exact.domains(npu2)) == {"num_aie_columns", "tile_m", "tile_k", "tile_n"}


@pytest.mark.parametrize("name", ["npu1", "npu2"])
def test_gemm_tiles_are_whole_kernel_blocks(name):
    dev = from_name(name, n_cols=4 if name == "npu1" else 8)
    gemm = GEMM(
        M=2048, K=2048, N=2048, prio_accuracy=True, emulate_bf16_mmul_with_bfp16=False
    ).resolved(dev)
    # aie2's kernel blocks m by four of its r = 4, aie2p's by two.
    assert gemm.mac_block(dev)[0] == (16 if name == "npu1" else 8)
    domains = gemm.domains(dev)
    for field, block in zip(("tile_m", "tile_k", "tile_n"), gemm.mac_block(dev)):
        assert all(tile % block == 0 for tile in domains[field]), (field, block)


def test_a_baked_replication_is_not_searched(npu2):
    # The join bakes DequantBFP's two n-halves, though a per= names them.
    assert DequantBFP(K=2048, N=2048).resolved(npu2).domains(npu2) == {
        "cols": (8, 4, 2, 1)
    }


def test_a_tile_the_call_gives_never_moves(npu2):
    found = variants(GEMV(M=2048, K=2048, tile_size_output=32), npu2)
    assert len(found) > 1
    assert {v.resolved.tile_size_output for v in found} == {32}


def test_a_tile_a_profile_gives_is_searched(npu2):
    profile = Profile()
    profile.add(GEMV, tile_size_output=32)
    with profile:
        gemv = GEMV(M=2048, K=2048)
    found = variants(gemv, npu2)
    assert found[0].resolved.tile_size_output == 32
    assert {v.resolved.tile_size_output for v in found} > {32}


def test_a_ladder_runs_through_the_resolved_value(npu2):
    # The default chunk, 8016, is the slice's largest even divisor to 8192,
    # which no power of two from the step reaches.
    sample = Sample(vocab=128256).resolved(npu2)
    assert sample.domains(npu2)["chunk"] == (8016, 4008, 2004, 1002)
    # Three octaves either side of 256, kept to multiples of 64.
    add = ElementwiseAdd(size=1 << 16, num_aie_columns=8).resolved(npu2)
    assert add.domains(npu2)["tile_size"] == (2048, 1024, 512, 256, 128, 64)


def test_a_block_is_no_larger_than_a_core_holds(npu2):
    # Uncapped, a 32768-row prefill's ladder runs to kv_len, and generating
    # MHA at a 32768 x 32768 score tile to ask the placer takes 8 GiB.
    mha = MHA(num_heads=8, seq_pad=32768).resolved(npu2)
    assert mha.domains(npu2)["B_kv"] == (512, 256, 128, 64)
    context = GQAContext(heads=32, groups=8, seq_len=32768).resolved(npu2)
    assert context.domains(npu2)["chunk"] == (512, 256, 128, 64)
    softmax = Softmax(rows=32, cols=32768).resolved(npu2)
    assert max(softmax.domains(npu2)["block"]) == 4096


def test_a_row_a_core_holds_whole_is_one_block(npu2):
    found = variants(Softmax(rows=32, cols=2048), npu2)
    assert {v.resolved.streamed for v in found} == {False, True}
    assert all(v.resolved.streamed or v.resolved.block == 2048 for v in found)


def test_flm_gemm_searches_its_a_tile_and_row_blocks(npu2):
    gemm = FlmGEMM(M=2048, K=2048, N=2048).resolved(npu2)
    assert gemm.domains(npu2) == {"tile_ma": (64, 32, 16), "m_chunk": (8, 4, 2, 1)}


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


def test_a_full_elf_load_is_an_entry_less_its_base(tmp_path):
    table = _table(tmp_path / "costs.json", {"a": (1.0, 100.0)})
    assert table.load("x") == pytest.approx(80.0)
    assert table.load("a") == pytest.approx(100.0)
    # What one run leaves over its step is not a load: D0 and R drift with it.
    table.record_step("t", StepCost(1.0, 500.0, True, True, "turbo", 1, 1, "-"))
    with pytest.raises(ValueError, match="neither beside another design"):
        table.load("t")


def test_a_measured_pack_costs_its_entry_and_its_steps_on_it(tmp_path):
    table = _table(tmp_path / "costs.json", {"a": (1.0, 100.0), "b": (2.0, 100.0)})
    apart = model_us(table, ["a", "b", "a"])
    # One entry, odd: a reset.
    assert model_us(table, ["a", "b", "a"], [("a", "b")]) == pytest.approx(
        (50.0 + 4.0 + 30.0 + 200.0 + 30.0, 2)
    )
    # Run beside x, alternating: its entry and the pack's, 150.
    x = table.load("x") + table.base_us
    table.record_pack(
        ["b", "a"], PackCost("x", x + 150.0, {"a": 3.0, "b": 4.0}, "turbo", 1, 1, "-")
    )
    assert table.pack_entry(table.pack_name(["a", "b"])) == pytest.approx(150.0)
    assert table.pack_name(["b", "a", "b"]) in table.packs
    assert model_us(table, ["a", "b", "a"], [("a", "b")]) == pytest.approx(
        (50.0 + 10.0 + 150.0 + 30.0, 2)
    )
    # Apart, each is still priced as measured alone.
    assert model_us(table, ["a", "b", "a"]) == apart
    table.save()
    again = CostTable(table.path)
    assert again.packs == table.packs


def _table(path, steps, dispatch=50.0, reset=30.0, base=30.0):
    """A table holding the given (t_step, load) per key, composed as the
    probe measures them: each beside x, and the pairs of ``TRIANGLE``.
    """
    table = CostTable(path, "npu2", "fused")
    for key, (t_step, load) in steps.items():
        cost = StepCost(
            t_step, dispatch + base + load + reset, True, True, "turbo", 1, 1, "-"
        )
        table.record_step(
            key,
            dataclasses.replace(
                cost, beside="x", pair_us=2 * base + TRIANGLE["x"] + load
            ),
        )
    for a, b in (("x", "y"), ("y", "z"), ("x", "z")):
        mean = base + (TRIANGLE[a] + TRIANGLE[b]) / 2
        table.record_calibration(
            (a, b), Calibration(dispatch, reset, base, mean, "turbo", 1, 1, "-")
        )
    return table


# The loads of the designs an xclbin-chain table is calibrated on, each
# setting measured beside x.
TRIANGLE = {"x": 80.0, "y": 90.0, "z": 100.0}


def _separate(path, steps, fixed=7.0):
    """An xclbin-chain table holding the given (c, L) per key, composed as
    the probe measures them: each beside x, and the pairs of ``TRIANGLE``.
    """
    table = CostTable(path, "npu2", "separate")
    for key, (c, load) in steps.items():
        cost = StepCost(c, fixed, True, True, "turbo", 1, 1, "-")
        table.record_step(
            key, dataclasses.replace(cost, beside="x", pair_us=TRIANGLE["x"] + load)
        )
    for a, b in (("x", "y"), ("y", "z"), ("x", "z")):
        mean = (TRIANGLE[a] + TRIANGLE[b]) / 2
        table.record_calibration(
            (a, b), Calibration(fixed, 0.0, 0.0, mean, "turbo", 1, 1, "-")
        )
    return table


def test_a_switch_is_counted_wrapping_to_the_first_step():
    assert Runlist(["a", "b", "a", "a", "c"]).switches() == Counter(a=2, b=1, c=1)
    assert Runlist(["a", "a", "a"]).switches() == Counter()
    assert Runlist(["a", "b"]).switches() == Counter(a=1, b=1)


def test_an_xclbin_chain_pays_a_step_each_and_a_load_per_switch(tmp_path):
    table = _separate(tmp_path / "costs.json", {"a": (10.0, 100.0), "b": (20.0, 50.0)})
    # a a b a: into b, then back into a; the last a runs into the first.
    assert model_us(table, ["a", "a", "b", "a"]) == pytest.approx(
        (7.0 + 3 * 10.0 + 20.0 + 50.0 + 100.0, 2)
    )
    assert model_us(table, ["a", "b"]) == pytest.approx((7.0 + 30.0 + 150.0, 2))
    assert model_us(table, ["a", "a"]) == pytest.approx((7.0 + 20.0, 0))
    # Each design is its own kernel and load, one array or not.
    assert model_us(table, ["a", "b"], arrays={"a": 0, "b": 0}) == model_us(
        table, ["a", "b"]
    )
    assert model_us(table, ["a", "b"], chosen={"b": "a"}) == pytest.approx(
        (7.0 + 20.0 + 200.0, 2)
    )
    with pytest.raises(ValueError, match="packs none"):
        model_us(table, ["a", "b"], [("a", "b")])


def test_a_load_is_solved_from_the_pairs_or_its_own_pair(tmp_path):
    table = _separate(tmp_path / "costs.json", {"a": (10.0, 100.0)})
    for key, load in TRIANGLE.items():
        assert table.load(key) == pytest.approx(load)
    assert table.load("a") == pytest.approx(100.0)
    assert table.load("unmeasured") == 0.0
    assert (table.dispatch_us, table.reset_us, table.base_us) == (7.0, 0.0, 0.0)
    # The reference's own row is measured beside nothing; the pairs price it.
    table.record_step("x", StepCost(5.0, 7.0, True, True, "turbo", 1, 1, "-"))
    assert table.load("x") == pytest.approx(80.0)
    # A design paired with one of a triangle is determined by least squares.
    table.record_calibration(
        ("x", "w"), Calibration(7.0, 0.0, 0.0, (80.0 + 60.0) / 2, "turbo", 1, 1, "-")
    )
    assert table.load("w") == pytest.approx(60.0)
    assert table.load("y") == pytest.approx(90.0)


def test_a_load_the_measurements_do_not_determine_is_refused(tmp_path):
    table = CostTable(tmp_path / "costs.json", "npu2", "separate")
    # A cycle of four is as undetermined as one pair: (L + d, L' - d) fits too.
    for a, b in (("p", "q"), ("q", "r"), ("r", "s"), ("s", "p")):
        table.record_calibration(
            (a, b), Calibration(7.0, 0.0, 0.0, 90.0, "turbo", 1, 1, "-")
        )
    with pytest.raises(ValueError, match="do not determine the load of p"):
        table.load("p")
    alone = StepCost(5.0, 7.0, True, True, "turbo", 1, 1, "-")
    table.record_step("t", alone)
    with pytest.raises(ValueError, match="neither beside another design"):
        table.load("t")
    table.record_step("u", dataclasses.replace(alone, beside="v", pair_us=170.0))
    with pytest.raises(ValueError, match="beside v, whose own load is not"):
        table.load("u")


def test_an_xclbin_table_round_trips_and_a_full_elf_one_keeps_its_bytes(tmp_path):
    table = _separate(tmp_path / "costs.json", {"a": (10.0, 100.0)})
    table.record_step("x", StepCost(5.0, 7.0, True, True, "turbo", 1, 1, "-"))
    table.save()
    again = CostTable(table.path, "npu2", "separate")
    assert again.steps == table.steps and again.calibrations == table.calibrations
    assert again.load("a") == pytest.approx(100.0)
    rows = table.path.read_text().splitlines()
    assert '"beside": "x"' in next(r for r in rows if r.startswith('  "a"'))
    assert "beside" not in next(r for r in rows if r.startswith('  "x"'))
    measured = Path(iron.__file__).parent / "lm" / "llama3" / "costs_npu2.json"
    copy = tmp_path / "costs_npu2.json"
    copy.write_bytes(measured.read_bytes())
    CostTable(copy, "npu2", "fused").save()
    assert copy.read_bytes() == measured.read_bytes()


class Apart(iron.Graph):
    """An add at two extents, one array: the smaller alternating with silu,
    the larger sixteen times in a row.
    """

    def body(self, a, b, c, d):
        x = a
        for _ in range(3):
            x = SiLU(ElementwiseAdd(x, b, tile_size=TILE), tile_size=TILE)
        y = c
        for _ in range(16):
            y = ElementwiseAdd(y, d, tile_size=TILE)
        return x, y


def test_an_xclbin_chain_narrows_a_design_it_switches_into_often(tmp_path, npu2):
    traced = Apart().trace(a=(SIZE,), b=(SIZE,), c=(2 * SIZE,), d=(2 * SIZE,))
    small, silu, *_, large = (s.op for s in traced.steps)
    steps = {}
    for op in (small, large):
        for v in variants(op, npu2):
            cols = v.resolved.num_aie_columns
            steps[v.key] = (4.0 + v.resolved.size / (64 * cols), 80.0 * cols)
    table = _separate(tmp_path / "costs.json", steps)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "separate"
    )
    # Three arrivals each: the small add's step cannot repay a wide load.
    # One arrival into sixteen steps: the large add's wide step does.
    narrow, wide = (tuning.chosen[cost_key(op)] for op in (small, large))
    assert narrow.resolved.num_aie_columns == 1
    assert wide.key == cost_key(large) and wide.resolved.num_aie_columns == 8
    assert narrow.array != wide.array
    assert tuning.groups == () and tuning.unmeasured == (cost_key(silu),)
    assert tuning.chosen[cost_key(silu)].key == cost_key(silu)
    assert (tuning.configures, tuning.baseline_configures) == (7, 7)
    keys = [cost_key(s.op) for s in traced.steps]
    chosen = {k: v.key for k, v in tuning.chosen.items()}
    assert tuning.predicted_us == pytest.approx(model_us(table, keys, (), chosen)[0])
    small_at = [steps[cost_key(small)], steps[narrow.key]]
    saved = [3 * c + 3 * load for c, load in small_at]
    assert tuning.baseline_us - tuning.predicted_us == pytest.approx(
        saved[0] - saved[1]
    )
    narrowed, groups = tuning.apply(traced, npu2)
    assert groups == []
    assert {cost_key(s.op, npu2) for s in narrowed.steps} == {
        narrow.key,
        wide.key,
        cost_key(silu),
    }


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
    assert (again.device, again.dispatch) == ("npu2", "fused")


def test_a_table_prices_only_its_device_and_packaging(tmp_path, npu2):
    traced, _, table = _add_silu(tmp_path, npu2)
    table.save()
    with pytest.raises(ValueError, match="measured for dispatch 'fused'"):
        CostTable(table.path, "npu2", "separate")
    tuner = JointNarrowing(table, fit_cache=tmp_path / "fits")
    with pytest.raises(ValueError, match="this version is packaged 'separate'"):
        tuner.tune(traced, npu2, "separate")
    with pytest.raises(ValueError, match="measured on npu2, not npu1"):
        tuner.tune(traced, from_name("npu1", n_cols=4), "fused")
    with pytest.raises(ValueError, match="give the table its device"):
        CostTable(tmp_path / "new.json").save()


def test_a_tuned_compile_takes_the_packaging_first(tmp_path, npu2):
    # each_step makes the version an xclbin, which a full-ELF table cannot price.
    _, _, table = _add_silu(tmp_path, npu2)
    tuner = JointNarrowing(table, fit_cache=tmp_path / "fits")
    with pytest.raises(ValueError, match="this version is packaged 'separate'"):
        AddSilu().compile(
            npu2, boundaries=iron.each_step, coresident=tuner, a=(SIZE,), b=(SIZE,)
        )


def test_packs_designs_apart_in_first_use_order(tmp_path, npu2):
    # gelu is wide and has no narrower width in the table, so it cannot
    # pack; add and silu are first used apart but adjacent five times, so
    # they share a device.
    traced, ops, table = _add_silu(tmp_path, npu2)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "fused"
    )
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
    assert tuning.devices == (tuple(tuning.chosen[k].key for k in tuning.groups[0]),)


def test_the_search_prices_a_pack_as_measured(tmp_path, npu2):
    traced, _, table = _add_silu(tmp_path, npu2)
    tuner = JointNarrowing(table, fit_cache=tmp_path / "fits")
    keys = [cost_key(s.op) for s in traced.steps]

    def modelled(tuning):
        return model_us(
            table,
            keys,
            tuning.groups,
            {k: v.key for k, v in tuning.chosen.items()},
            {k: v.array for k, v in tuning.chosen.items()},
        )[0]

    first = tuner.tune(traced, npu2, "fused")
    [device] = first.devices
    x = table.load("x") + table.base_us
    # The pack, measured as one device, costs far more than the sum of its
    # members' own measurements predicts: the search drops it.
    table.record_pack(
        device, PackCost("x", x + 1e6, {k: 1.0 for k in device}, "turbo", 1, 1, "-")
    )
    dearer = tuner.tune(traced, npu2, "fused")
    assert device not in dearer.devices
    assert dearer.predicted_us == pytest.approx(modelled(dearer))
    # Measured cheaper than that sum: the search keeps it, at the measured cost.
    table.record_pack(
        device, PackCost("x", x + 1.0, {k: 0.0 for k in device}, "turbo", 1, 1, "-")
    )
    cheaper = tuner.tune(traced, npu2, "fused")
    assert cheaper.devices == first.devices
    assert cheaper.predicted_us == pytest.approx(modelled(cheaper))
    assert cheaper.predicted_us < first.predicted_us


def test_the_packs_a_tuning_takes_are_measured_until_none_is_missing(tmp_path, npu2):
    traced, _, table = _add_silu(tmp_path, npu2)
    designs = Designs.of([Call(traced)], npu2)
    [device] = JointNarrowing(table).tune(traced, npu2, "fused").devices
    assert designs.unpacked(table) == [device]
    x = table.load("x") + table.base_us
    table.record_pack(
        device, PackCost("x", x + 1.0, {k: 0.0 for k in device}, "turbo", 1, 1, "-")
    )
    assert designs.unpacked(table) == []
    separate = CostTable(tmp_path / "separate.json", "npu2", "separate")
    assert designs.unpacked(separate) == []


@pytest.mark.parametrize("accurate", [True, False])
def test_an_inexact_width_is_taken_only_if_accurate(accurate, tmp_path, npu2):
    traced, ops, table = _add_silu(tmp_path, npu2)
    key = cost_key(ops["ElementwiseAdd"])
    default, *others = variants(ops["ElementwiseAdd"], npu2)
    tuner = JointNarrowing(table, fit_cache=tmp_path / "fits")
    tuning = tuner.tune(traced, npu2, "fused")
    exact = tuning.chosen[key]
    assert exact.key != default.key and tuning.inexact == ()
    for v in others:
        table.record_step(
            v.key,
            dataclasses.replace(table.steps[v.key], exact=False, accurate=accurate),
        )
    tuning = tuner.tune(traced, npu2, "fused")
    assert tuning.chosen[key].key == (exact.key if accurate else default.key)
    assert tuning.inexact == ((key,) if accurate else ())
    assert ("not exact" in tuning.report()) == accurate


def test_apply_rebuilds_the_narrowed_steps(tmp_path, npu2):
    traced, ops, table = _add_silu(tmp_path, npu2)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "fused"
    )
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
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "fused"
    )
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


class PinnedSibling(iron.Graph):
    """An add at two extents, one array, the larger's columns given by its call."""

    def body(self, a, b, c, d):
        t = ElementwiseAdd(a, b, tile_size=TILE)
        return t, ElementwiseAdd(c, d, tile_size=TILE, num_aie_columns=8)


def test_designs_of_one_array_may_search_different_tunables(tmp_path, npu2):
    traced = PinnedSibling().trace(a=(SIZE,), b=(SIZE,), c=(2 * SIZE,), d=(2 * SIZE,))
    free, pinned = (s.op for s in traced.steps)
    assert {n for n, _ in variants(free, npu2)[0].tunables} == {
        "num_aie_columns",
        "num_channels",
    }
    assert {n for n, _ in variants(pinned, npu2)[0].tunables} == {"num_channels"}
    steps = {}
    for op in (free, pinned):
        for v in variants(op, npu2):
            cols = v.resolved.num_aie_columns
            steps[v.key] = (4.0 + cols, 8.0 * cols)
    table = _table(tmp_path / "costs.json", steps)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "fused"
    )
    # Alone the free add would take one column; its sibling holds it at eight.
    chosen = [tuning.chosen[cost_key(op)] for op in (free, pinned)]
    assert chosen[0].resolved.num_aie_columns == 8
    assert chosen[0].array == chosen[1].array


def test_designs_apart_only_in_their_probes_share_one_cost(tmp_path, npu2):
    traced = TwoClamps().trace(x=(SIZE,))
    first, second = (s.op for s in traced.steps)
    assert first.design_key() != second.design_key()
    key = cost_key(first)
    assert cost_key(second) == key
    # Measured once, at the probe, whichever clamp was traced first.
    designs = Designs.of([Call(traced)], npu2)
    assert list(designs.settings) == [key]
    found = designs.settings[key]
    assert all((v.op.low, v.op.high) == (-np.inf, np.inf) for v in found)
    assert [v.key for v in variants(second, npu2)] == [v.key for v in found]
    steps = {}
    for v in found:
        cols = dict(v.tunables)["num_aie_columns"]
        steps[v.key] = (4.0 + cols, 8.0 * cols)
    table = _table(tmp_path / "costs.json", steps)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "fused"
    )
    assert list(tuning.chosen) == [key]
    chosen = tuning.chosen[key]
    assert chosen.key != found[0].key
    narrowed, _ = tuning.apply(traced, npu2)
    a, b = (s.op for s in narrowed.steps)
    assert (a.low, a.high, b.low, b.high) == (-0.75, 1.25, -3e4, 3e4)
    for op in (a, b):
        assert dict(chosen.tunables).items() <= vars(op).items()
        assert cost_key(op) == chosen.key


def test_a_clamp_folded_into_flm_gemm_costs_what_the_gemm_does(npu2):
    # The epilogue clamps whether or not one is asked for, at (-inf, inf).
    plain = FlmGEMM(M=256, K=512, N=1024)
    clamped = plain.fold(Clamp(size=256 * 1024, low=-0.25, high=1.5))
    assert clamped.clamp == (-0.25, 1.5)
    assert clamped.design_key() != plain.design_key()
    assert cost_key(clamped, npu2) == cost_key(plain, npu2)


def test_placer_verdicts_are_kept_across_tunings(tmp_path, npu2):
    traced, _, table = _add_silu(tmp_path, npu2)
    fit_cache = tmp_path / "fits"
    first = JointNarrowing(table, fit_cache=fit_cache).tune(traced, npu2, "fused")
    records = sorted(fit_cache.iterdir())
    assert records and all(r.read_text() == "fits" for r in records)
    widths = {k: v.tunables for k, v in first.chosen.items()}

    # A second tuning reads the verdicts rather than asking the placer: one
    # recorded as refused is taken as refused, and the pack moves to its
    # next-cheapest widths, which the placer is then asked about.
    for r in records:
        r.write_text("refused: recorded by the test")
    second = JointNarrowing(table, fit_cache=fit_cache).tune(traced, npu2, "fused")
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


def _swiglu(tmp_path, dev, gate_us, step_us=10.0, table=_table):
    """SwiGLU at one row as traced, and a table (``_table`` or ``_separate``)
    holding every design it runs as traced and folded at its default width,
    the folded gate taking ``gate_us`` a step, every other design
    ``step_us``, and each a load of 20.
    """
    E, H = 2048, 8192
    w = np.zeros((H, E), bfloat16)
    traced = SwiGLU(w, w, np.zeros((E, H), bfloat16)).trace(x=(1, E))
    folds, _ = folded(traced, dev)
    steps = {
        cost_key(s.op, dev): (step_us, 20.0) for g in (traced, folds) for s in g.steps
    }
    steps[cost_key(folds.steps[0].op, dev)] = (gate_us, 20.0)
    return traced, table(tmp_path / "costs.json", steps)


def test_a_fold_is_taken_where_the_model_says_it_gains(tmp_path, npu2):
    traced, table = _swiglu(tmp_path, npu2, gate_us=11.0)
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "fused"
    )
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
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "fused"
    )
    assert tuning.folds == ()
    assert [str(f) for f in tuning.unpriced] == ([] if gate_us else ["SiLU into GEMV"])
    assert ("unpriced, not taken: fold SiLU into GEMV" in tuning.report()) == (
        gate_us is None
    )
    applied, _ = tuning.apply(traced, npu2)
    assert [type(s.op).__name__ for s in applied.steps] == [
        type(s.op).__name__ for s in traced.steps
    ]


@pytest.mark.parametrize("gate_us", [135.0, 300.0], ids=["saves", "dearer"])
def test_an_xclbin_chain_folds_where_it_saves_a_dispatch(gate_us, tmp_path, npu2):
    # Each step is mostly its dispatch: folding silu into the gate saves one
    # unless the folded gate costs more than the two.
    traced, table = _swiglu(
        tmp_path, npu2, gate_us=gate_us, step_us=130.0, table=_separate
    )
    tuning = JointNarrowing(table, fit_cache=tmp_path / "fits").tune(
        traced, npu2, "separate"
    )
    # gate and up, silu, mul, down: four switches, as the folded runlist has.
    assert tuning.baseline_configures == 4
    assert tuning.baseline_us == pytest.approx(7.0 + 5 * 130.0 + 4 * 20.0)
    if gate_us < 2 * 130.0:
        assert [str(f) for f in tuning.folds] == ["SiLU into GEMV"]
        assert (tuning.configures, tuning.groups) == (4, ())
        assert tuning.predicted_us == pytest.approx(
            7.0 + gate_us + 3 * 130.0 + 4 * 20.0
        )
    else:
        assert tuning.folds == ()
        assert tuning.predicted_us == tuning.baseline_us


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
