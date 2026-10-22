# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Autotuning without a device: the settings an operator is searched over,
the placer's verdicts, the cost cache, the accuracy gate, and the profile a
tuning writes, its times made up. Hardware times a tuned graph
(``iron/tests/infrastructure/test_autotune.py``).
"""

import dataclasses
import json

import aie.utils as aie_utils
import aie.utils.benchmark as benchmark
import numpy as np
import pytest
from aie.iron.device import from_name
from ml_dtypes import bfloat16

import iron
from iron.common.declare import Precision, Profile
from iron.common.testing import vectors
from iron.operators import GEMM, GEMV, MHA, ElementwiseAdd, ReLU, RoPE, Sample, SiLU
from iron.operators import Softmax
from iron.operators.flm import DequantBFP
from iron.operators.flm import ProjectionGEMM
from iron.operators.gemm import GEMMPlacement
from iron.tests.support.graphs import Rotate
from iron.tests.support.llama_model import llama_1b
from iron.tune import autotune as tuning
from iron.tune.autotune import Point, Shape, Timed, autotune, line, settings
from iron.tune.measure import Cache, Measurement, Timing, judge, time_interleaved

SIZE = 8192
TILE = 256

pytestmark = pytest.mark.usefixtures("npu2")


def designs(op, dev, pinned=frozenset()):
    """``op``'s settings, each with the design it resolves to."""
    return [
        (s, op._with_tunables(**s).resolved(dev)) for s in settings(op, dev, pinned)
    ]


def identities(found, dev):
    return {tuning._identity(d, dev) for _, d in found}


def test_settings_range_over_every_width_the_shims_allow(npu2):
    found = designs(ElementwiseAdd(size=SIZE, tile_size=TILE), npu2)
    widths = [(s["num_aie_columns"], s["num_channels"]) for s, _ in found]
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
    assert len(identities(found, npu2)) == len(found)


def test_settings_give_each_design_once():
    # Settings of Llama's decode MHA that resolve alike on NPU1's four
    # columns are one design, which would otherwise be built and timed once
    # a setting.
    dev = from_name("npu1", n_cols=4)
    with aie_utils.set_current_device(dev):
        model = llama_1b(num_hidden_layers=1)
        recording = model.record(**model.shapes()[0])
        [mha] = {s.op for s in recording.steps if isinstance(s.op, MHA)}
        found = designs(mha, dev)
        assert len(identities(found, dev)) == len(found)
        assert all(d.num_pipelines <= dev.cols for _, d in found)


def test_settings_widen_a_default_its_resolution_keeps_narrow(npu2):
    profile = Profile()
    profile.add(ElementwiseAdd, num_aie_columns=2)
    found = settings(profile.make(ElementwiseAdd, size=SIZE, tile_size=TILE), npu2)
    assert found[0]["num_aie_columns"] == 2
    assert {s["num_aie_columns"] for s in found[1:]} == {8, 4, 2, 1}


def test_a_tunable_the_call_gives_is_not_searched(npu2):
    add = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=2)
    assert add.pinned == {"tile_size", "num_aie_columns"}
    # Eight channels would take past the 16 MM2S channels of the shim row.
    assert settings(add, npu2) == [{"num_channels": c} for c in (1, 4, 2)]
    pinned = ElementwiseAdd(
        size=SIZE, tile_size=TILE, num_aie_columns=2, num_channels=1
    )
    assert settings(pinned, npu2) == [{}]


class PinnedTwin(iron.Graph):
    """Two adds of one shape, the second's columns given by its call."""

    def body(self, a, b):
        t = ElementwiseAdd.step(a, b, tile_size=TILE)
        return ElementwiseAdd.step(t, b, tile_size=TILE, num_aie_columns=8)


def test_a_shape_keeps_a_tunable_any_of_its_calls_pins(npu2):
    recording = PinnedTwin().record(a=(SIZE,), b=(SIZE,))
    [shape] = tuning.shapes([Timed(recording)], npu2)
    assert "num_aie_columns" in shape.pinned and len(shape.members) == 1
    free = shape.members[0][0]
    found = settings(free, npu2, shape.pinned)
    assert found == [{"num_channels": 1}]


def test_settings_keep_a_width_whose_bounded_tile_count_moves_to_d2(npu2):
    # Two lanes round-robin 1024 one-row tiles each, past D1's 1023 wrap; a
    # tile split over D1 and D0 keeps the count on D2, which has none.
    op = Rotate().record(x=(2048, 64), angles=(2048, 64)).steps[0].op
    assert [s["num_aie_columns"] for s in settings(op, npu2)] == [8, 4, 2, 1]


def test_derived_fields_are_not_widths(npu2):
    # resolve() sets GEMM's A shims and MHA's lanes from the other fields
    # whatever it is given, so a width there would be timed once per value
    # and built alike.
    gemm = GEMM(M=512, K=512, N=512)
    assert "n_shim_mem_a" not in gemm.resolved(npu2)._domains(npu2)
    # n_shim_mem_a resolves to at most the columns: many settings, one design.
    found = designs(GEMM(M=2560, K=768, N=3072, b_col_maj=True), npu2)
    assert len(identities(found, npu2)) == len(found)
    widths = [s["num_aie_columns"] for s, _ in found]
    assert list(dict.fromkeys(widths)) == [8, 4, 2, 1]
    mha = MHA(num_heads=8, seq_pad=256).resolved(npu2)
    assert mha._domains(npu2) == {
        "num_pipelines": (8, 4, 2, 1),
        "B_q": (64, 32, 16),
        "pv_cores": (1, 2),
    }


def test_gemm_searches_tile_k_only_where_c_accumulates_in_f32(npu2):
    plain = GEMM(M=2048, K=2048, N=2048).resolved(npu2)
    assert set(plain._domains(npu2)) == {
        "num_aie_columns",
        "tile_m",
        "tile_n",
        "placement",
    }
    exact = GEMM(M=2048, K=2048, N=2048, precision=Precision.HIGHEST).resolved(npu2)
    assert set(exact._domains(npu2)) == {
        "num_aie_columns",
        "tile_m",
        "tile_k",
        "tile_n",
        "placement",
    }


@pytest.mark.parametrize("name", ["npu1", "npu2"])
def test_gemm_tiles_are_whole_kernel_blocks(name):
    dev = from_name(name, n_cols=4 if name == "npu1" else 8)
    gemm = GEMM(M=2048, K=2048, N=2048, precision=Precision.HIGHEST).resolved(dev)
    # aie2's kernel blocks m by four of its r = 4, aie2p's by two.
    assert gemm.mac_block(dev)[0] == (16 if name == "npu1" else 8)
    domains = gemm._domains(dev)
    for field, block in zip(("tile_m", "tile_k", "tile_n"), gemm.mac_block(dev)):
        assert all(tile % block == 0 for tile in domains[field]), (field, block)


def test_a_baked_replication_is_not_searched(npu2):
    # The join bakes DequantBFP's two n-halves, though a per= names them.
    assert DequantBFP(K=2048, N=2048).resolved(npu2)._domains(npu2) == {
        "cols": (8, 4, 2, 1)
    }


def test_a_tile_the_call_gives_never_moves(npu2):
    found = designs(GEMV(M=2048, K=2048, tile_size_output=32), npu2)
    assert len(found) > 1
    assert {d.tile_size_output for _, d in found} == {32}


def test_a_tile_a_profile_gives_is_searched(npu2):
    profile = Profile()
    profile.add(GEMV, tile_size_output=32)
    found = designs(profile.make(GEMV, M=2048, K=2048), npu2)
    assert found[0][1].tile_size_output == 32
    assert {d.tile_size_output for _, d in found} > {32}


def test_a_ladder_runs_through_the_resolved_value(npu2):
    # The default chunk, 8016, is the slice's largest even divisor to 8192,
    # which no power of two from the step reaches.
    sample = Sample(vocab=128256).resolved(npu2)
    assert sample._domains(npu2)["chunk"] == (8016, 4008, 2004, 1002)
    # Three octaves either side of 256, kept to multiples of 64.
    add = ElementwiseAdd(size=1 << 16, num_aie_columns=8).resolved(npu2)
    assert add._domains(npu2)["tile_size"] == (2048, 1024, 512, 256, 128, 64)


def test_a_block_is_no_larger_than_a_core_holds(npu2):
    # Uncapped, a 32768-row prefill's ladder runs to kv_len, and generating
    # MHA at a 32768 x 32768 score tile to ask the placer takes 8 GiB.
    mha = MHA(num_heads=8, seq_pad=32768).resolved(npu2)
    assert mha._domains(npu2)["B_q"] == (64, 32, 16)
    wide = MHA(num_heads=4, seq_pad=2048, d=256, causal=False).resolved(npu2)
    assert wide._domains(npu2)["B_q"] == (16,)
    softmax = Softmax(rows=32, cols=32768).resolved(npu2)
    assert max(softmax._domains(npu2)["block"]) == 4096


def test_descent_reaches_every_mha_setting_one_tunable_a_move(npu2):
    found = settings(MHA(num_heads=2, seq_len=100), npu2)
    default = found[0]
    moves = {tuple(default.items()): 0}
    frontier = [default]
    depth = 0
    while frontier:
        depth += 1
        reached = {
            tuple(w.items()): w
            for s in frontier
            for name in s
            for w in line(found, s, name)
            if tuple(w.items()) not in moves
        }
        moves |= dict.fromkeys(reached, depth)
        frontier = list(reached.values())
    assert len(moves) == len(found)
    for s in found:
        apart = sum(s[n] != default[n] for n in s)
        assert moves[tuple(s.items())] <= apart, s


def test_a_row_a_core_holds_whole_is_one_block(npu2):
    found = designs(Softmax(rows=32, cols=2048), npu2)
    assert {d.streamed for _, d in found} == {False, True}
    assert all(d.streamed or d.block == 2048 for _, d in found)


def test_flm_gemm_searches_its_a_tile_and_row_blocks(npu2):
    gemm = ProjectionGEMM(M=2048, K=2048, N=2048).resolved(npu2)
    assert gemm._domains(npu2) == {
        "tile_ma": (64, 32, 16),
        "m_chunk": (8, 4, 2, 1),
        "k_tile": (512, 256, 128),
        "ct_k": (256, 128, 64),
    }


def test_a_placement_is_searched_by_name(tmp_path, npu2):
    gemm = GEMM(M=2048, K=2048, N=2048, num_aie_columns=2, b_col_maj=True)
    found = settings(gemm, npu2, frozenset({"tile_m", "tile_n"}))
    assert {s["placement"] for s in found} == {
        GEMMPlacement.SHIMS,
        GEMMPlacement.TILES,
    }
    # A profile's placement starts the search, the declared ones after it.
    profile = Profile()
    profile.add(GEMM, placement=GEMMPlacement.TILES)
    held = profile.make(GEMM, M=512, K=512, N=512)
    assert held.resolved(npu2)._domains(npu2)["placement"] == (
        GEMMPlacement.TILES,
        GEMMPlacement.SHIMS,
    )


def test_a_placement_takes_its_own_enum_alone():
    with pytest.raises(
        TypeError, match=r"GEMM: placement \('diagonal'\) must be a GEMMPlacement"
    ):
        GEMM(M=512, K=512, N=512, placement="diagonal")


def test_a_profile_refuses_a_derived_field():
    with pytest.raises(TypeError, match="derived or fixed"):
        Profile().add(GEMM, M=512, n_shim_mem_a=1)


def test_a_narrowed_operator_keeps_its_fixed_fields():
    add = ElementwiseAdd(size=SIZE, tile_size=TILE)
    narrow = add._with_tunables(num_aie_columns=2)
    assert (narrow.size, narrow.tile_size, narrow.num_aie_columns) == (SIZE, TILE, 2)
    with pytest.raises(TypeError, match="no tunable"):
        add._with_tunables(size=SIZE // 2)


def test_cache_keys_follow_the_build_the_values_and_the_inputs(npu2):
    add = ElementwiseAdd(size=SIZE, tile_size=TILE)
    x = np.arange(SIZE, dtype=np.float32)
    key = Cache.key(add)
    assert Cache.key(ElementwiseAdd(size=SIZE, tile_size=TILE)) == key
    assert Cache.key(add, {}, {}) == key
    others = [
        Cache.key(add._with_tunables(num_aie_columns=2)),
        Cache.key(add, {"n": 1}),
        Cache.key(add, {"n": 2}),
        Cache.key(add, inputs={"a": x}),
        Cache.key(add, inputs={"a": x + 1}),
        Cache.key(add, full_elf=False),
    ]
    assert len({key, *others}) == 1 + len(others)


def test_cache_entries_round_trip_per_platform_and_mode(tmp_path):
    m = Measurement(
        4.0, (4.1, 3.9), "ab" * 32, "run", "turbo", 50, (4.0, 4.2), "2026-10-06"
    )
    cache = Cache("NPU Strix Halo", "turbo", root=tmp_path)
    cache.put("k", m)
    assert cache.directory == tmp_path / "npu-strix-halo" / "turbo"
    assert Cache("NPU Strix Halo", "turbo", root=tmp_path).get("k") == m
    assert Cache("NPU Strix Halo", "default", root=tmp_path).get("k") is None
    assert Cache("NPU Strix", "turbo", root=tmp_path).get("k") is None
    # An entry written with other fields is timed again.
    path = cache.directory / "k.json"
    fields = json.loads(path.read_text())
    del fields["run"]
    path.write_text(json.dumps(fields))
    assert cache.get("k") is None


def test_settings_all_cached_are_not_timed(monkeypatch, tmp_path):
    from iron.tune import measure as measuring

    monkeypatch.setattr(measuring, "pmode", lambda: "turbo")
    ops = [ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=c) for c in (8, 4)]
    cache = Cache("NPU Strix Halo", "turbo", root=tmp_path)
    m = Measurement(4.0, (4.1, 3.9), "ab" * 32, "run", "turbo", 50)
    for op in ops:
        cache.put(Cache.key(op, full_elf=True), m)
    assert measuring.measure(ops, full_elf=True, cache=cache) == {0: m, 1: m}


def test_a_difference_pairs_rounds_only_within_one_run():
    a = Measurement(4.0, (4.0, 5.0, 3.0), "", "r", "turbo", 50)
    b = Measurement(3.0, (3.0, 4.0, 2.0), "", "r", "turbo", 50)
    assert a.difference(b) == (1.0, 0.0)
    delta, noise = a.difference(dataclasses.replace(b, run="other"))
    assert delta == 1.0 and noise > 0.5


def test_each_setting_pairs_with_the_default_timed_in_its_own_batch(monkeypatch):
    """Past one batch the default is timed again beside each batch, and a
    setting is compared with that one, round for round.
    """
    from iron.tune import measure as measuring

    class Run:
        def __init__(self, name, ops, **_):
            self.callable = (name, ops[0])

        def load(self):
            pass

        def digest(self):
            return "same"

    batches = []

    def time_interleaved(runs, timing, groups, fastest, log):
        batches.append(len(batches))
        # A batch's long runs are slower the later the batch, its short ones free.
        n = len(runs) // 2
        return [
            benchmark.Stats.from_samples(
                [0.0 if i < n else 10.0 * len(batches) + i] * timing.rounds
            )
            for i in range(len(runs))
        ]

    monkeypatch.setattr(measuring, "Standalone", Run)
    monkeypatch.setattr(measuring, "time_interleaved", time_interleaved)
    monkeypatch.setattr(measuring, "pmode", lambda: "turbo")
    monkeypatch.setattr(measuring, "CONTEXTS", 4)  # one setting a batch
    ops = [
        ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=c) for c in (8, 4, 2)
    ]
    ran = measuring.measure(ops, full_elf=True, log=lambda _: None)
    assert len(batches) == 2
    for i in (1, 2):
        assert ran[i].default_round_us != ran[3 - i].default_round_us
        assert ran[i].against_default()[1] == 0.0


def _gemm_judged():
    """GEMM at its default tile_k and at 16, random inputs, its reference's
    output, and each setting's bound on C.
    """
    default = GEMM(M=256, K=256, N=256)
    narrow = default._with_tunables(tile_k=16)
    v = vectors(default)
    bounds = [
        op.resolved().tolerance().bound(*v.inputs.values()) for op in (default, narrow)
    ]
    return default, narrow, v, bounds


def test_a_setting_is_never_judged_by_its_looser_bound_alone(npu2):
    # tile_k=16 rounds the accumulator four times as often as 64 does.
    default, narrow, v, (tight, loose) = _gemm_judged()
    c = v["C"].astype(np.float32)
    c[0, 0] += 1.5 * tight[0, 0]
    c = c.astype(bfloat16)
    err = abs(float(c[0, 0]) - float(v["C"][0, 0]))
    assert tight[0, 0] < err < loose[0, 0]
    assert judge(narrow, narrow, v.inputs, {"C": c}) is None
    assert judge(default, narrow, v.inputs, {"C": c}) is not None


def test_a_gate_admits_an_output_within_it_and_refuses_one_past(npu2):
    rope = RoPE(rows=8, cols=64)
    v = vectors(rope, **RoPE.test.draw(rope))
    off = (v["y"].astype(np.float32) * 1.03).astype(bfloat16)
    assert judge(rope, rope, v.inputs, {"y": off}) is None
    assert judge(rope, rope, v.inputs, {"y": -v["y"]}) is not None


def test_an_exact_gate_or_a_short_bound_admits_only_bit_identical(npu2):
    relu = ReLU(size=64, num_aie_columns=1, tile_size=64)
    v = vectors(relu)
    assert "bit-identical" in judge(relu, relu, v.inputs, v.outputs)
    rope = Rotate().record(x=(64, 64), angles=(64, 64)).steps[0].op
    v = vectors(rope)
    full = dict(valid=64, valid_angles=64)
    assert judge(rope, rope, v.inputs, v.outputs, full) is None
    short = dict(valid=32, valid_angles=32)
    assert "under a bound" in judge(rope, rope, v.inputs, v.outputs, short)


class Chain(iron.Graph):
    def body(self, a, b):
        return SiLU.step(ElementwiseAdd.step(a, b, tile_size=TILE), tile_size=TILE)


def _fake(monkeypatch, step_us, output=lambda op: "same"):
    """Time each operator at ``step_us(op)``, rounds paired, without a
    device; every setting fits.
    """

    def measure(ops, *, values=None, **_):
        return {
            i: Measurement(
                step_us(op),
                (step_us(op),) * 3,
                output(op),
                "run",
                "turbo",
                50,
                () if i == 0 else (step_us(ops[0]),) * 3,
            )
            for i, op in enumerate(ops)
        }

    monkeypatch.setattr(tuning, "measure", measure)
    monkeypatch.setattr(tuning, "refusal", lambda op: None)


def _tune(recording, dev, profile=None):
    return autotune([Timed(recording)], dev, profile, full_elf=True, log=lambda _: None)


def test_autotune_writes_the_fastest_setting_per_shape(monkeypatch, npu2):
    # Fewer columns are faster here, SiLU's by more.
    _fake(monkeypatch, lambda op: op.num_aie_columns * (2 if type(op) is SiLU else 1))
    recording = Chain().record(a=(SIZE,), b=(SIZE,))
    profile = _tune(recording, npu2)
    add = profile.make(ElementwiseAdd, size=SIZE, tile_size=TILE).resolved(npu2)
    silu = profile.make(SiLU, size=SIZE, tile_size=TILE).resolved(npu2)
    assert add.num_aie_columns == 1 and silu.num_aie_columns == 1


def test_a_setting_that_gains_nothing_keeps_the_recorded_one(monkeypatch, npu2):
    _fake(monkeypatch, lambda op: 1.0)
    recording = Chain().record(a=(SIZE,), b=(SIZE,))
    profile = _tune(recording, npu2)
    for cls in (ElementwiseAdd, SiLU):
        op = profile.make(cls, size=SIZE, tile_size=TILE).resolved(npu2)
        assert op.num_aie_columns == 8


def test_a_faster_setting_whose_output_differs_is_judged(monkeypatch, npu2):
    _fake(monkeypatch, lambda op: op.num_aie_columns, output=lambda op: repr(op))
    judged = []

    def refuse(default, op, *_):
        judged.append(op.num_aie_columns)
        return "refused by the test"

    monkeypatch.setattr(tuning, "_judged", refuse)
    recording = Chain().record(a=(SIZE,), b=(SIZE,))
    profile = _tune(recording, npu2)
    assert judged
    op = profile.make(ElementwiseAdd, size=SIZE, tile_size=TILE).resolved(npu2)
    assert op.num_aie_columns == 8


def test_a_tuned_profile_replaces_the_entries_it_covers(monkeypatch, npu2):
    _fake(monkeypatch, lambda op: op.num_aie_columns)
    old = Profile()
    old.add(ElementwiseAdd, num_aie_columns=4)
    old.add(GEMV, tile_size_output=32)
    recording = Chain().record(a=(SIZE,), b=(SIZE,))
    profile = _tune(recording, npu2, old)
    entries = {(cls, tuple(matched)) for cls, matched, _ in profile}
    assert (ElementwiseAdd, ()) not in entries and (GEMV, ()) in entries
    # The add's new entry gives it the one column the made-up times favour.
    assert profile.make(ElementwiseAdd, size=SIZE, tile_size=TILE).num_aie_columns == 1


def test_an_operator_is_timed_at_each_point_its_extents_move(monkeypatch, npu2):
    timed = []

    def measure(ops, *, values=None, **_):
        timed.append(dict(values))
        return {
            i: Measurement(1.0, (1.0,) * 3, "same", "run", "turbo", 50, (1.0,) * 3)
            for i in range(len(ops))
        }

    monkeypatch.setattr(tuning, "measure", measure)
    monkeypatch.setattr(tuning, "refusal", lambda op: None)
    call = Timed(
        Rotate().record(x=(64, 64), angles=(64, 64)),
        points=[Point(0.5, {"n": 16}), Point(0.5, {"n": 64})],
    )
    [shape] = tuning.shapes([call], npu2)
    assert isinstance(shape, Shape)
    tuning.time_shape(shape, npu2, full_elf=True, log=lambda _: None)
    assert len({tuple(sorted(v.items())) for v in timed}) == 2


def test_a_gemm_s_busiest_core_makes_a_call_per_k_tile_of_each_of_its_tiles(npu2):
    op = GEMM(M=512, K=256, N=256, tile_m=32, tile_k=64, tile_n=64).resolved(npu2)
    tiles = 512 // 32 * 256 // 64
    cores = op.n_aie_rows * op.num_aie_columns
    assert op.matmul_calls({}) == -(-tiles * 256 // 64 // cores)
    # Under a bound only the rows and K it covers are computed.
    assert op.matmul_calls({"valid": 32, "valid_k": 64}) == -(-256 // 64 // cores)


@pytest.mark.parametrize("margin, timed", [(1.01, False), (0.99, True)])
def test_a_gemm_setting_slower_by_its_kernel_alone_is_never_timed(
    monkeypatch, npu2, margin, timed
):
    def key(array):
        return f"{array.tile_m}x{array.tile_k}x{array.tile_n}"

    monkeypatch.setattr(
        GEMM, "matmul", lambda self: type("K", (), {"recipe_key": key(self)})
    )
    ran = []

    def measure(ops, **_):
        ran.extend(key(op.layout()) for op in ops)
        return {
            i: Measurement(
                100.0, (100.0,) * 3, "same", "run", "turbo", 50, (100.0,) * 3
            )
            for i in range(len(ops))
        }

    monkeypatch.setattr(tuning, "measure", measure)
    monkeypatch.setattr(tuning, "refusal", lambda op: None)
    op = GEMM(M=256, K=256, N=256, precision=Precision.HIGH)
    shape = Shape(op)
    shape.members.append((op, [(1.0, {})], {}))
    found = [op._with_tunables(**s).resolved(npu2) for s in settings(op, npu2)]
    # Every tile but 16 rows by 16 columns runs at 1 cycle a call, that one
    # at what puts its bound just over or just under the 100 us step.
    cycles = {key(o.layout()): 1 for o in found}
    small = next(o for o in found if key(o.layout()) == "16x64x16")
    calls = small.matmul_calls({})
    mhz = 1800.0
    cycles["16x64x16"] = margin * 100.0 * mhz * tuning.CLOCK_HEADROOM / calls
    tuning.time_shape(
        shape,
        npu2,
        full_elf=True,
        exhaustive=len(found),
        cycles=cycles,
        core_mhz=mhz,
        log=lambda _: None,
    )
    assert ("16x64x16" in ran) == timed
    assert len(set(ran)) == len(set(cycles)) - (not timed)


def test_kernel_cycles_are_the_nightly_s_rows_by_their_build(
    monkeypatch, tmp_path, npu2
):
    latest = {
        "schema": 1,
        "rows": {"mm/a": {"cycles": {"value": 900, "unit": "cycles"}}, "mm/b": {}},
        "builds": {"mm/a": "matmul-1", "mm/b": "matmul-2"},
    }
    (tmp_path / "npu2.json").write_text(json.dumps(latest))
    monkeypatch.setattr(tuning.ExternalFunction, "recipe_key", None, raising=False)
    monkeypatch.setattr(tuning, "KERNEL_CHECKS", f"file://{tmp_path}/{{npu}}.json")
    assert tuning.kernel_cycles(npu2) == {"matmul-1": 900}
    monkeypatch.setattr(tuning, "KERNEL_CHECKS", f"file://{tmp_path}/none.json")
    assert tuning.kernel_cycles(npu2, log=lambda _: None) == {}


def test_an_mlir_aie_that_names_no_builds_gives_no_kernel_cycles(monkeypatch, npu2):
    monkeypatch.delattr(tuning.ExternalFunction, "recipe_key", raising=False)
    monkeypatch.setattr(tuning, "KERNEL_CHECKS", "file:///never/read/{npu}.json")
    assert tuning.kernel_cycles(npu2) == {}


@pytest.mark.parametrize("name", ["npu1", "npu2"])
def test_every_gemm_tile_searched_is_one_the_nightly_times(name, request):
    """mlir-aie's nightly times the tiles ``_iron_gemm_tiles`` in its
    ``test/python/npu/kernel_cases.py`` names: powers of two, m and n at
    least 16 (m 8 on npu2 without bfp16 macs), k 64 below HIGHEST, whose
    double-buffered A and B, C and stack fit 64 KiB. A tile the search
    reaches outside them has no cycles to skip it by.
    """
    dev = request.getfixturevalue(name)
    for precision in Precision:
        op = GEMM(M=4096, K=4096, N=4096, precision=precision)
        least_m = 8 if name == "npu2" and precision != Precision.MEDIUM else 16
        c_bytes = 6 if precision == Precision.HIGHEST else 4
        for s in settings(op, dev):
            r = op._with_tunables(**s).resolved(dev)
            m, k, n = r.tile_m, r.tile_k, r.tile_n
            assert all(v & (v - 1) == 0 for v in (m, k, n)), (m, k, n)
            assert m >= least_m and n >= 16, (precision, m, n)
            assert k == 64 or precision == Precision.HIGHEST, (precision, k)
            assert 4 * (m * k + k * n) + c_bytes * m * n + 0xD00 <= 64 * 1024


class Projection(iron.Graph):
    def body(self, x, w):
        return GEMM.step(x, w)


def test_retuning_keeps_what_the_profile_set_that_the_search_does_not_move(
    monkeypatch, npu2
):
    _fake(monkeypatch, lambda op: op.tile_n)  # the narrowest tile_n is fastest
    old = Profile()
    old.add(GEMM, tile_k=32)
    graph = Projection()
    graph.profile = old
    recording = graph.record(x=(256, 256), w=(256, 256))
    profile = _tune(recording, npu2, old)
    op = profile.make(GEMM, M=256, K=256, N=256)
    assert op.tile_k == 32 and op.resolved(npu2).tile_n == 16


@pytest.mark.supported_devices("npu2")
def test_a_run_is_timed_by_the_time_its_image_took():
    """An image's call returns the handle an empty dispatch is timed on
    (aiecc's empty sequence) and a result whose npu_time is the time the
    image took, which run_interleaved reads as the call's figure.
    """

    class Double(iron.Graph):
        def body(self, x):
            return ElementwiseAdd.step(x, x)

    version = Double().compile(x=(16, 256))
    version(np.ones((16, 256), bfloat16))
    call = version.callable
    handle, result = call()
    assert result.npu_time == round(call.last_elapsed * 1e9)
    assert handle is not None and handle.empty_dispatch_ns() is not None
    (timed,) = time_interleaved([call], Timing(rounds=2, calls=3))
    assert len(timed.samples_us) == 2 and min(timed.samples_us) > 0
