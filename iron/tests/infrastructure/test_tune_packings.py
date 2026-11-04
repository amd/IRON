# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pricing packings.

A version's arrays grouped into shared device configurations (``iron.tune.packings``).
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron import In, Out
from aie.utils.compile.jit.params import param
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common import Operator
from iron.common.declare.profile import PackingEntry
from iron.common.graph.compiled import apply_profile
from iron.common.graph.packing import apply as apply_packings
from iron.common.graph.record import Recording
from iron.common.image.compose import Packing
from iron.common.image.step import FusionKind
from iron.lm.generation import Sampler
from iron.lm.tune import calls
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gelu import GELU
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.silu import SiLU
from iron.operators.tanh import Tanh
from iron.tests.support import sequences
from iron.tests.support.graphs import Chain
from iron.tests.support.llama_model import small
from iron.tune.autotune import Point, Shape, Timed, settings, time_shape
from iron.tune.costmodel import CostModel
from iron.tune.failures import Kind, Ledger
from iron.tune.fold import fold_profile
from iron.tune.fusions import design_cores
from iron.tune.measure import Budget, Cache, CpuWaitRefused, Timing, platform
from iron.tune.packings import (
    Packer,
    _decide_fold,
    _end_to_end,
    _foreign,
    _narrow_for_rejected,
    _refusal,
    _rejoin,
    _with_fusions,
    adjacent,
    price_packings,
    widen_packings,
    width_tunables,
)
from iron.tune.verify import verify

pytestmark = pytest.mark.usefixtures("npu2")

SIZE = 2048


class Alternating(iron.Graph):
    """ReLU and Tanh in turn, eight steps: every step a switch apart."""

    def body(self, x):
        for _ in range(4):
            x = Tanh.step(ReLU.step(x, num_aie_columns=8), num_aie_columns=8)
        return x


WIDE = 8192


class Wide(iron.Graph):
    """ReLU, Tanh and Sigmoid in turn at eight columns and two channels, twice: 16 cores each, 48 together, so packed only narrowed."""

    def body(self, x):
        for _ in range(2):
            for op in (ReLU, Tanh, Sigmoid):
                x = op.step(x, num_aie_columns=8, num_channels=2)
        return x


LONG = 2**24


class Runs(iron.Graph):
    """Four ReLUs then four Tanhs over a long vector: one switch among eight long steps."""

    def body(self, x):
        for op in (ReLU, Tanh):
            for _ in range(4):
                x = op.step(x, num_aie_columns=8)
        return x


class BoundedReLUs(iron.Graph):
    """Two ReLUs over a call's first ``n`` elements."""

    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(ReLU.step(x[:n]))


ROUND = 2**22


class Rounds(iron.Graph):
    """ReLU, Tanh and Sigmoid in turn over a call's first ``n`` elements, twice, at eight columns; given ``other``, a second version over the same arrays."""

    def body(self, x, other=None, *, n: Scratchpad[np.int32]):
        x = x[:n]
        for _ in range(2):
            for op in (ReLU, Tanh, Sigmoid):
                x = op.step(x, num_aie_columns=8)
        if other is None:
            return x
        return x, Copy.step(other)


class Projections(iron.Graph):
    """One shape's GEMV twice, at two output tiles: two arrays, as q and o were with only q given half a head's tiles."""

    def body(self, w, x):
        y = GEMV.step(w, x, tile_size_output=32)
        return GEMV.step(w, y, tile_size_output=256)


def _packer(recording, dev, tmp_path, full_elf=True):
    return Packer(
        Timed(recording),
        dev,
        full_elf=full_elf,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=None,
        fit_cache=tmp_path / "fit",
        log=lambda _: None,
        lock=False,
        model=CostModel(),
    )


def test_a_grouping_a_run_refused_is_refused_this_tune_alone(tmp_path, npu2):
    """A timing refusal rules a grouping out of this tune's search, not every tune's fit cache."""
    packer = _packer(Alternating().record(x=(SIZE,)), npu2, tmp_path)
    group = {k: {} for k in packer.shapes}
    assert packer.fits(group)
    reason = f"{Kind.TIMING.value}: a callable's median call waited 900 us for a CPU"
    packer.refused[frozenset(packer._distinct(group))] = reason
    assert not packer.fits(group)
    assert not any("refused" in f.read_text() for f in (tmp_path / "fit").iterdir())
    fresh = _packer(Alternating().record(x=(SIZE,)), npu2, tmp_path)
    assert fresh.fits({k: {} for k in fresh.shapes})


def test_a_timing_refusal_is_its_own_kind_in_the_ledger(tmp_path, npu2):
    logged = []
    ledger = Ledger(tmp_path / "ledger")
    kind = _refusal(
        CpuWaitRefused("a callable's median call waited 900 us for a CPU"),
        npu2,
        iron.Profile(),
        "Alternating packed",
        "Alternating-0",
        ledger,
        logged.append,
    )
    assert kind is Kind.TIMING
    [entry] = ledger.entries()
    assert entry.kind == "timing refused" and "refused, timing refused" in logged[0]


def test_width_tunables_are_the_ones_counting_columns_channels_or_cores():
    assert width_tunables(GEMV(M=512, K=2048)) == ["num_aie_columns", "num_channels"]
    assert width_tunables(MHA(num_heads=32, num_KV_heads=8, d=64, seq_pad=1)) == [
        "num_pipelines"
    ]


def test_adjacent_counts_the_switches_a_merge_removes():
    order = ["a", "b", "a", "b", None, "c", "c", "a"]
    assert adjacent(order, {"a": 0, "b": 1, "c": 2}) == {(0, 1): 3, (0, 2): 1}
    assert adjacent(order, {"a": 0, "b": 0, "c": 2}) == {(0, 2): 1}


def test_a_budget_ends_a_search_once_its_time_left_is_under_the_reserve():
    logged = []
    assert not Budget(None, logged.append).ends("a search")
    assert not Budget(3600, logged.append).ends("a search")
    spent = Budget(0, logged.append)
    assert spent.ends("a search") and spent.ends("a search")
    assert spent.stopped == ["a search"] and len(logged) == 1


def test_a_packer_finds_each_array_and_its_narrower_widths(npu2, tmp_path):
    packer = _packer(Alternating().record(x=(SIZE,)), npu2, tmp_path)
    assert len(packer.shapes) == 2
    assert [k is not None for k in packer.order] == [True] * 8
    relu, tanh = packer.order[:2]
    assert packer.cores({relu: {}}) == 8
    narrow = {"num_aie_columns": 1, "num_channels": 1}
    assert narrow in packer.options(relu)
    assert packer.cores({relu: narrow, tanh: {}}) == 9


def test_one_shapes_two_arrays_are_one_unit_a_change_aligns(npu2, tmp_path):
    """A profile names shapes, so the two GEMVs of one shape are one unit, set as one; aligning it to one of its arrays' settings puts both on it."""
    packer = _packer(Projections().record(w=(2048, 2048), x=(2048,)), npu2, tmp_path)
    (unit,) = set(packer.order)
    assert len(packer.arrays(unit, {})) == 2
    aligned = [
        packer.cores({unit: s})
        for k, s in packer.changes({unit: {}})
        if len(packer.arrays(k, s)) == 1
    ]
    assert min(aligned) * 2 == packer.cores({unit: {}})


class TwoWidths(iron.Graph):
    """GELU over the first ``n`` rows of a 2048- and a 512-wide input: one array key."""

    def body(self, x, y, *, n: Scratchpad[np.int32]):
        return GELU.step(x[:n]), GELU.step(y[:n])


def test_a_packer_counts_each_array_a_full_elf_builds(npu2, tmp_path):
    """Two designs of one array key reading other scratchpad words take an array each, their row bounds scaling apart (``n`` against ``n / 4``)."""
    packer = _packer(TwoWidths().record(x=(64, 2048), y=(64, 512)), npu2, tmp_path)
    group = {k: {} for k in packer.shapes}
    one = design_cores(packer.recorded(next(iter(packer.shapes))).resolved(npu2))
    assert packer.cores(group) == 2 * one


def test_a_retile_holds_a_weight_s_coding(npu2, tmp_path):
    """A GEMV's coded_a is bound when its recording is coded, before the search, so a re-tile stays coded rather than building over a plain weight."""
    model = small()
    packer = _packer(model.record(**model.shapes()[0]), npu2, tmp_path)
    key = next(k for k in packer.shapes if isinstance(packer.recorded(k), GEMV))
    shape = packer.tiling(key, {"num_aie_columns": 1})
    assert "coded_a" in shape.pinned
    op = shape.members[0][0]
    assert {s.get("coded_a", op.coded_a) for s in settings(op, npu2, shape.pinned)} == {
        op.coded_a
    }


def test_a_width_resolved_afresh_keeps_its_coding(npu2, tmp_path):
    """A width its recorded tiles do not divide resolves them afresh, its coding held rather than reset plain."""
    gemv = GEMV(M=512, K=1536, coded_a=True, tile_size_output=64, num_aie_columns=4)
    steps = sequences.steps((gemv, "a", "x", "y"))
    recording = Recording.of_steps("one_gemv", steps, ["a", "x"], ["y"])
    packer = _packer(recording, npu2, tmp_path)
    (key,) = packer.shapes
    afresh = [o for o in packer.options(key) if o.get("tile_size_output", 64) is None]
    assert afresh
    for option in afresh:
        assert all(op.coded_a for op in packer.arrays(key, option).values())


def test_aligning_a_unit_to_another_array_keeps_its_coding(npu2, tmp_path):
    """A unit aligned to another array's setting keeps its own coded_a, even aligned whole to a plain GEMV."""
    steps = sequences.steps(
        (GEMV(M=2048, K=1536, coded_a=True), "a", "x", "y"),
        (GEMV(M=512, K=1536), "b", "x", "z"),
    )
    recording = Recording.of_steps("two_gemvs", steps, ["a", "b", "x"], ["y", "z"])
    packer = _packer(recording, npu2, tmp_path)
    group = {k: {} for k in packer.shapes}
    for key, setting in packer.changes(group):
        assert setting.get("coded_a", packer.recorded(key).coded_a) == (
            packer.recorded(key).coded_a
        )


def test_a_shape_whose_operators_share_no_setting_is_left_as_recorded(npu2):
    """Nothing to search where no setting suits every operator: none timed, none taken, rather than indexing the empty intersection."""
    gemv = GEMV(M=2048, K=2048)
    shape = Shape(gemv)
    shape.members = [(gemv, [(1.0, {})], {}), (Tanh(size=2048), [(1.0, {})], {})]
    logged = []
    assert time_shape(shape, npu2, full_elf=True, log=logged.append) == []
    assert logged[-1].endswith("left as recorded")


def test_a_packing_names_no_dimension_a_hosts_context_sizes(npu2, tmp_path):
    """A packing found at one context names none of the dimensions a host's own context sizes (MHA's KV cache and the cache copies)."""
    model, sibling = small(), small(max_seq_len=512)
    decode, _ = calls(model, 0, 0, 256, 1, Sampler(0.7, 50), sibling)
    assert any("kv_len" in v for v in decode.varying.values())
    packer = Packer(
        decode,
        npu2,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=None,
        fit_cache=tmp_path / "fit",
        log=lambda _: None,
        lock=False,
        model=CostModel(),
    )
    members = packer.members({k: {} for k in packer.shapes})
    assert not any("kv_len" in dims for cls, dims, _ in members if cls is MHA)
    profile = iron.Profile()
    # The context-sized designs alone: every decode design together does not place.
    profile.add_packing([m for m in members if m[0] in (MHA, Copy)])
    sizes = []
    for m in (model, sibling):
        _, packing = apply_packings(m.record(**m.shapes()[0]), profile, [], npu2)
        sizes.append([len(g) for g in packing.groups])
    assert sizes[0] == sizes[1] and sizes[0], sizes


def test_a_pack_no_placer_places_runs_unpacked(npu2, caplog):
    """Every decode design of the small model in one group places under neither placer: it is not packed, and a warning says why."""
    model = small()
    decode, _ = calls(model, 0, 0, 256, 1, Sampler(0.7, 50), small(max_seq_len=512))
    packer = Packer(
        decode,
        npu2,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=None,
        fit_cache=None,
        log=lambda _: None,
        lock=False,
        model=CostModel(),
    )
    profile = iron.Profile()
    profile.add_packing(packer.members({k: {} for k in packer.shapes}))
    _, packing = apply_packings(model.record(**model.shapes()[0]), profile, [], npu2)
    assert packing == Packing()
    assert "does not place, so it is not packed" in caplog.text


def test_writes_a_fixed_offset_apart_at_a_per_call_row_are_one_shape(npu2):
    """K's and V's write into a paired cache differ only per call, so a packing or fusion entry naming one names both."""
    kv = iron.state((16, 2, 2, 64))

    class Write(iron.Graph):
        def body(self, k, v, *, pos: Scratchpad[np.int32]):
            kv[pos, :, 0] = k
            kv[pos, :, 1] = v

    t = Write().record(k=(2, 64), v=(2, 64))
    first, second = (Shape(s.op.resolved(npu2)) for s in t.steps)
    assert first.key == second.key
    offsets = [b.expression.evaluate({"pos": 3}) for b in t.bindings]
    assert offsets == [3 * 256, 3 * 256 + 64]


class Single(iron.Graph):
    """One step: ``fold_candidates`` needs a pair, so this recording never admits one."""

    def body(self, x):
        return ReLU.step(x)


def _version(name: str) -> tuple:
    return ((name, (1,), "bf16"),)


@pytest.mark.parametrize(
    "delta,se,kept,message",
    [
        (-50.0, 5.0, True, "keeps its folds"),
        (-1.0, 10.0, False, "keeps the profile as it stood"),  # too small next to noise
        (5.0, 10.0, False, "keeps the profile as it stood"),  # a regression
        (-50.0, None, False, "do not gain beyond the noise"),  # unmeasurable noise
    ],
)
def test_decide_fold_keeps_the_fusions_only_where_the_call_gains_beyond_noise(
    delta, se, kept, message
):
    """A regression, or a gain too small next to ``CONFIDENCE`` standard errors of noise, both narrow the version's entry away entirely."""
    decode = Timed(Alternating().record(x=(SIZE,)))
    v = _version("decode")
    fusions = [(FusionKind.FOLD, (), (), frozenset({v}))]
    logged = []
    got = _decide_fold(fusions, decode, v, delta, se, logged.append)
    assert got == (fusions if kept else [])
    assert message in logged[0]
    if kept:
        assert decode.recording.name in logged[0]


def test_fold_profile_leaves_a_profile_with_nothing_to_fold_unchanged():
    """A recording with no pair to fold (``Single``) adds nothing ``fold_profile`` did not already carry."""
    base = iron.Profile()
    with_folds = fold_profile(base, [Timed(Single().record(x=(SIZE,)))])
    assert with_folds.fusions() == base.fusions() == []


_DECODE_V, _PROMPT_V = _version("decode"), _version("prompt")


@pytest.mark.parametrize(
    "fusions,expected",
    [
        pytest.param(
            [(FusionKind.FOLD, (), (), frozenset({_DECODE_V}))],
            [],
            id="drops an entry naming only the rejected version",
        ),
        pytest.param(
            [(FusionKind.FOLD, (), (), frozenset({_DECODE_V, _PROMPT_V}))],
            [(FusionKind.FOLD, (), (), frozenset({_PROMPT_V}))],
            id="shrinks an entry naming several versions",
        ),
        pytest.param(
            [
                (FusionKind.FOLD, (), (), None),
                (FusionKind.FOLD, (), (), frozenset({_PROMPT_V})),
                (FusionKind.STREAM, (), (), frozenset({_DECODE_V})),
            ],
            None,
            id="leaves other kinds and other versions alone",
        ),
    ],
)
def test_narrow_for_rejected(fusions, expected):
    assert _narrow_for_rejected(fusions, _DECODE_V) == (
        fusions if expected is None else expected
    )


def test_a_version_that_rejects_its_folds_takes_the_packings_searched_without_them():
    decode_v, prompt_v = _version("decode"), _version("prompt")
    folded_group = ((GEMV, {"M": 2048, "K": 2048}), (ElementwiseAdd, {"size": 2048}))
    plain_group = ((GEMV, {"M": 2048, "K": 2048}), (ElementwiseMul, {"size": 2048}))
    unscoped = ((ReLU, {"size": SIZE}), (Tanh, {"size": SIZE}))
    folded = Profile()
    folded.add_packing(folded_group, [decode_v, prompt_v])
    folded.add_packing(unscoped)
    unfolded = Profile()
    unfolded.add_packing(plain_group, [decode_v])
    unfolded.add_packing(folded_group, [prompt_v])
    joined = _rejoin(folded, unfolded, {decode_v})
    got = {
        (tuple(c.__name__ for c, *_ in e.members), e.versions)
        for e in joined.packings()
    }
    assert got == {
        (("GEMV", "ElementwiseAdd"), frozenset({prompt_v})),
        (("ReLU", "Tanh"), None),
        (("GEMV", "ElementwiseMul"), frozenset({decode_v})),
    }


def test_a_packing_naming_a_shape_these_graphs_never_run_is_another_graph_s():
    calls = [Timed(Alternating().record(x=(SIZE,)))]
    ours = PackingEntry(((ReLU, {"size": SIZE}, None), (Tanh, {"size": SIZE}, None)))
    theirs = PackingEntry(
        ((ReLU, {"size": SIZE}, None), (GEMV, {"M": 3072, "K": 8192}, None))
    )
    dev = aie_utils.ensure_current_device()
    assert not _foreign(ours, calls, dev)
    assert _foreign(theirs, calls, dev)


def test_with_fusions_replaces_only_the_fusions():
    base = Profile()
    base.add(GEMV, M=2048, K=2048, num_aie_columns=8)
    base.add_packing([(GEMV, {"M": 2048, "K": 2048}), (ElementwiseAdd, {"size": 2048})])
    base.add_fusion(
        FusionKind.STREAM,
        [(GEMV, {"M": 2048, "K": 2048}), (ElementwiseAdd, {"size": 2048})],
        [(0, "C", 1, "b")],
    )
    replaced = _with_fusions(base, [])
    assert replaced.fusions() == []
    assert list(replaced) == list(base)
    assert replaced.packings() == base.packings()


def test_fold_profile_scopes_each_entry_to_the_version_it_was_found_in():
    """Decode and the prompt chunk run SwiGLU at different widths, so ``fold_profile`` scopes each its own entry: only decode's own projections are ``GEMV``."""
    model = small()
    decode_shapes, prompt_shapes = model.shapes()
    decode, prompt = model.record(**decode_shapes), model.record(**prompt_shapes)
    assert decode.version != prompt.version

    with_folds = fold_profile(Profile(), [Timed(decode), Timed(prompt)])
    fusions = with_folds.fusions()
    by_class = {steps[0][0].__name__: versions for _, steps, _, versions in fusions}
    assert by_class["GEMV"] == frozenset({decode.version})
    silu_versions = {
        versions for _, steps, _, versions in fusions if steps[0][0].__name__ == "SiLU"
    }
    assert silu_versions == {frozenset({decode.version}), frozenset({prompt.version})}

    # Rejecting the prompt's own folds (the per-version decision) drops
    # only its own singleton-scoped entry, decode's own untouched.
    narrowed = _narrow_for_rejected(fusions, prompt.version)
    assert len(narrowed) == len(fusions) - 1
    assert frozenset({decode.version}) in {v for _, _, _, v in narrowed}
    assert frozenset({prompt.version}) not in {v for _, _, _, v in narrowed}


@pytest.mark.supported_devices("npu1")
def test_calls_time_only_the_versions_asked_for():
    model = small()
    [decode] = calls(model, 0, 0, 256, 1, Sampler(0.7, 50), versions=["decode"])
    assert decode.recording.version == model.record(**model.shapes()[0]).version


def test_on_an_xclbin_a_packing_joins_its_steps_dispatches(npu2, tmp_path):
    """An xclbin per step dispatches each step but a packed group's steps in a row once; a full ELF's dispatches do not follow the grouping."""
    recording = Alternating().record(x=(SIZE,))
    full, xclbin = (_packer(recording, npu2, tmp_path, f) for f in (True, False))
    alone = [{k: {}} for k in full.shapes]
    together = [{k: {} for k in full.shapes}]
    assert full.features(alone)["dispatches"] == 0
    assert full.features(together)["dispatches"] == 0
    assert xclbin.features(alone)["dispatches"] == len(xclbin.order) - 1
    assert xclbin.features(together)["dispatches"] == 0


class Doubled(Operator):
    """Doubles its input on the host: a step no packing search times."""

    reference_only = True
    rows: int = param()
    x = In(rows, 8)
    y = Out(rows, 8)

    def reference(self, x):
        return x * 2


class Doubles(iron.Graph):
    """Two independent ``Doubled`` steps."""

    def body(self, x, y):
        return Doubled.step(x), Doubled.step(y)


def test_a_search_that_finds_nothing_keeps_the_packings_a_version_has(npu2, tmp_path):
    """A version searched keeps its own packings where no grouping beats them, including an entry naming a version these calls do not run."""
    recording = Doubles().record(x=(4, 8), y=(8, 8))
    profile = Profile()
    profile.add_packing(
        [(Doubled, {"rows": 4}), (Doubled, {"rows": 8})],
        [recording.version, _version("prompt")],
    )
    logged = []
    out = price_packings(
        [Timed(recording)],
        npu2,
        profile,
        full_elf=True,
        fit_cache=tmp_path / "fit",
        log=logged.append,
    )
    assert f"{recording.name}: no packing gains" in logged
    assert out.packings() == profile.packings()


def test_a_version_its_profile_does_not_build_is_refused(npu2, tmp_path):
    """A fusion entry giving SiLU three columns, which 2048 elements do not split into: the version is not searched, and the tune goes on."""
    recording = Chain(size=SIZE, tile=SIZE, columns=1).record(a=(SIZE,), b=(SIZE,))
    profile = Profile()
    profile.add_fusion(
        FusionKind.STREAM,
        [
            (SiLU, {"size": SIZE}, {"num_aie_columns": 3}),
            (ElementwiseMul, {"size": SIZE}),
        ],
        [(0, "y", 1, "a")],
    )
    logged = []
    out = price_packings(
        [Timed(recording)],
        npu2,
        profile,
        full_elf=True,
        fit_cache=tmp_path / "fit",
        log=logged.append,
    )
    assert any(
        line.startswith(f"{recording.name} as profiled: refused, build failure")
        for line in logged
    ), logged
    assert out.fusions() == profile.fusions() and not out.packings()


def test_widen_keeps_an_entry_to_its_versions_where_it_does_not_build(npu2):
    """Another version's entry gives ReLU three columns, which 2048 elements do not split into: this version fails, so the entry keeps to its own."""
    recording = Single().record(x=(SIZE,))
    prompt = _version("prompt")
    profile = Profile()
    profile.add_packing(
        [(ReLU, {"size": SIZE}, {"num_aie_columns": 3}), (Tanh, {"size": SIZE})],
        [prompt],
    )
    logged = []
    widened = widen_packings([Timed(recording)], npu2, profile, log=logged.append)
    assert any("refused, build failure" in line for line in logged), logged
    (entry,) = widened.packings()
    assert entry.versions == {prompt}


# ---------------------------------------------------------------------------
# On the device
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_price_packings_packs_alternating_arrays_bit_identically(tmp_path):
    """Eight steps of two 8-column arrays, each step a switch, narrowed to share one configuration the packed graph keeps end to end."""
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    recording = Alternating().record(x=(SIZE,))
    kept = []
    profile = price_packings(
        [Timed(recording)],
        dev,
        iron.Profile(),
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=cache,
        fit_cache=tmp_path / "fit",
        progress=lambda found, model: kept.append(found),
        log=print,
    )
    assert len(profile.packings()) == 1
    assert [len(p.packings()) for p in kept] == [1], "the version's find, kept"
    _, _, packing = apply_profile(recording, profile, dev)
    assert len(packing.groups) == 1 and len(packing.groups[0]) == 2

    packed_graph = Alternating()
    packed_graph.profile = profile
    packed = packed_graph.compile(x=(SIZE,))
    plain = Alternating().compile(x=(SIZE,))
    x = (np.random.default_rng(0).random(SIZE) * 4 - 2).astype(bfloat16)
    want = np.asarray(plain(x))
    got = np.asarray(packed(x))
    assert np.array_equal(want.view(np.uint16), got.view(np.uint16))
    reference = np.tanh(np.maximum(x.astype(np.float32), 0))
    for _ in range(3):
        reference = np.tanh(np.maximum(reference, 0))
    np.testing.assert_allclose(got.astype(np.float32), reference, atol=2e-2)


@pytest.mark.supported_devices("npu2")
def test_a_spent_budget_keeps_what_the_first_round_found(tmp_path):
    """A tune out of time still checks and keeps its first merge, bit-identical, where a cap would have kept nothing."""
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    recording = Alternating().record(x=(SIZE,))
    logged = []
    budget = Budget(0, logged.append)
    profile = price_packings(
        [Timed(recording)],
        dev,
        iron.Profile(),
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=cache,
        fit_cache=tmp_path / "fit",
        log=logged.append,
        budget=budget,
    )
    print("\n".join(logged))
    assert budget.stopped == [f"{recording.name}'s packing search"]
    assert len(profile.packings()) == 1
    packed_graph = Alternating()
    packed_graph.profile = profile
    x = (np.random.default_rng(0).random(SIZE) * 4 - 2).astype(bfloat16)
    want = np.asarray(Alternating().compile(x=(SIZE,))(x))
    got = np.asarray(packed_graph.compile(x=(SIZE,))(x))
    assert np.array_equal(want.view(np.uint16), got.view(np.uint16))


@pytest.mark.supported_devices("npu2")
def test_price_packings_skips_a_version_its_switches_cannot_pay(tmp_path):
    """One switch beside eight long steps: no grouping could gain the share packing is worth searching for, so the version is not searched."""
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    logged = []
    profile = price_packings(
        [Timed(Runs().record(x=(LONG,)))],
        dev,
        iron.Profile(),
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=cache,
        fit_cache=tmp_path / "fit",
        log=logged.append,
    )
    print("\n".join(logged))
    assert not profile.packings()
    assert any(line.endswith("not searched") for line in logged)
    assert not any("grouped" in line for line in logged)


@pytest.mark.supported_devices("npu2")
def test_end_to_end_decides_at_the_shortest_point_and_verify_runs_every_point():
    """A search's end-to-end check runs the call at its shortest point alone; the final verify runs every point, including one past the input."""
    dev = aie_utils.ensure_current_device()
    narrowed = iron.Profile()
    narrowed.add(ReLU, num_aie_columns=1)
    timing = Timing(rounds=1, calls=2)

    def past(profile: Profile) -> list[Timed]:
        graph = BoundedReLUs()
        graph.profile = profile
        points = [Point(0.5, dict(n=SIZE)), Point(0.5, dict(n=2 * SIZE))]
        return [Timed(graph.record(x=(SIZE,)), values=dict(n=SIZE), points=points)]

    [call] = past(narrowed)
    delta, _ = _end_to_end(call, dev, Profile(), narrowed, timing, print, False)
    assert np.isfinite(delta)
    with pytest.raises(IndexError):
        verify(past, dev, Profile(), narrowed, timing=timing)


def test_the_shortest_point_weighs_the_whole_call():
    recording = BoundedReLUs().record(x=(SIZE,))
    call = Timed(recording, points=[Point(0.25, dict(n=64)), Point(0.75, dict(n=SIZE))])
    assert call.shortest().points == [Point(1.0, dict(n=64))]
    assert Timed(recording).shortest().points == []


@pytest.mark.supported_devices("npu1")
def test_end_to_end_builds_an_xclbin_per_step_on_npu1(npu1):
    """npu1 has no full ELF, so the end-to-end check a fold is judged by builds each version as an xclbin per step instead."""
    recording = BoundedReLUs().record(x=(SIZE,))
    profile = iron.Profile()
    own = Timed(recording, values=dict(n=SIZE))
    delta, _ = _end_to_end(
        own, npu1, profile, profile, Timing(rounds=1, calls=2), print, False
    )
    assert np.isfinite(delta)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("rows, applies", [(2048, True), (ROUND, False)])
def test_widen_packings_applies_an_entry_only_where_it_pays(rows, applies):
    """An entry found in one version narrows its arrays to one column, applying in another only at short calls where that still gains."""
    dev = aie_utils.ensure_current_device()
    first = Rounds().record(x=(ROUND,))
    second = Rounds().record(x=(ROUND,), other=(64,))
    narrow = {"num_aie_columns": 1, "num_channels": 1}
    profile = iron.Profile()
    profile.add_packing(
        [(op, {"size": ROUND}, narrow) for op in (ReLU, Tanh, Sigmoid)],
        versions=[first.version],
    )
    logged = []
    widened = widen_packings(
        [Timed(first, values=dict(n=2048)), Timed(second, values=dict(n=rows))],
        dev,
        profile,
        timing=Timing(rounds=2, calls=5),
        log=logged.append,
    )
    print("\n".join(logged))
    (entry,) = widened.packings()
    want = {first.version, second.version} if applies else {first.version}
    assert entry.versions == want, logged
    _, _, packing = apply_profile(second, widened, dev)
    assert bool(packing.groups) == applies


@pytest.mark.supported_devices("npu2")
def test_price_packings_narrows_what_does_not_co_reside(tmp_path):
    """Three arrays of 16 cores each take 48 of 32 at their own widths: the packer narrows the cheapest until they share one configuration."""
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    recording = Wide().record(x=(WIDE,))
    logged = []
    profile = price_packings(
        [Timed(recording)],
        dev,
        iron.Profile(),
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=cache,
        fit_cache=tmp_path / "fit",
        log=logged.append,
    )
    print("\n".join(logged))
    (entry,) = profile.packings()
    assert entry.versions == {recording.version}
    assert any(tunables for _, _, tunables in entry.members), "nothing was narrowed"
    packed_graph = Wide()
    packed_graph.profile = profile
    packed = packed_graph.compile(x=(WIDE,))
    plain = Wide().compile(x=(WIDE,))
    x = (np.random.default_rng(0).random(WIDE) * 4 - 2).astype(bfloat16)
    assert np.array_equal(
        np.asarray(plain(x)).view(np.uint16), np.asarray(packed(x)).view(np.uint16)
    )
    reference = x.astype(np.float32)
    for _ in range(2):
        reference = 1 / (1 + np.exp(-np.tanh(np.maximum(reference, 0))))
    np.testing.assert_allclose(
        np.asarray(packed(x)).astype(np.float32), reference, atol=2e-2
    )


class Beside(iron.Graph):
    """Two independent ReLUs, each on every column at two channels: packed, twice a shim's channels."""

    def body(self, x, y):
        return (
            ReLU.step(x, num_aie_columns=8, num_channels=2),
            ReLU.step(y, num_aie_columns=8, num_channels=2),
        )


@pytest.mark.supported_devices("npu2")
def test_a_spent_budget_searches_no_further_past_a_refusal(tmp_path):
    """Out of time, a version whose grouping a check refused is not grouped and checked again."""
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    logged = []
    budget = Budget(0, logged.append)
    recording = Beside().record(x=(2**16,), y=(2**16,))
    profile = price_packings(
        [Timed(recording)],
        dev,
        iron.Profile(),
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=cache,
        fit_cache=tmp_path / "fit",
        log=logged.append,
        budget=budget,
    )
    print("\n".join(logged))
    assert sum(": refused, " in line for line in logged) == 1, logged
    assert f"{recording.name}: not searched again after 1 refusal(s)" in logged
    assert not profile.packings()
