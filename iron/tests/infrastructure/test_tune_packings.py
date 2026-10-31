# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pricing packings: a version's arrays grouped into shared device
configurations (``iron.tune.packings``). No NPU above ``# On the device``.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common.declare.profile import PackingEntry
from iron.common.graph.compiled import apply_profile
from iron.common.graph.packing import apply as apply_packings
from iron.common.image.step import FusionKind
from iron.lm.generation import Sampler
from iron.lm.tune import calls
from iron.tests.support.llama_model import small
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.tanh import Tanh
from iron.tune import cli as tune_cli
from iron.tune.autotune import Point, Timed
from iron.tune.costmodel import CostModel
from iron.tune.fold import fold_profile
from iron.tune.measure import Cache, Timing, platform
from iron.tune.packings import (
    Packer,
    _decide_fold,
    _end_to_end,
    _foreign,
    _narrow_for_rejected,
    _rejoin,
    _with_fusions,
    adjacent,
    price_packings,
    widen_packings,
    width_tunables,
)

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
    """ReLU, Tanh and Sigmoid in turn at eight columns and two channels,
    twice: 16 cores each, 48 together, so packed only narrowed."""

    def body(self, x):
        for _ in range(2):
            for op in (ReLU, Tanh, Sigmoid):
                x = op.step(x, num_aie_columns=8, num_channels=2)
        return x


LONG = 2**24


class Runs(iron.Graph):
    """Four ReLUs then four Tanhs over a long vector: one switch among eight
    long steps."""

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
    """ReLU, Tanh and Sigmoid in turn over a call's first ``n`` elements,
    twice, at eight columns; given ``other``, a second version over the same
    arrays (it copies ``other`` too). A short call is switch-bound and a long
    one bound by the arrays' own time, as a decode step and a prompt chunk
    are."""

    def body(self, x, other=None, *, n: Scratchpad[np.int32]):
        x = x[:n]
        for _ in range(2):
            for op in (ReLU, Tanh, Sigmoid):
                x = op.step(x, num_aie_columns=8)
        if other is None:
            return x
        return x, Copy.step(other)


class Projections(iron.Graph):
    """One shape's GEMV twice, at two output tiles: two arrays, as q and o
    were with only q given half a head's tiles."""

    def body(self, w, x):
        y = GEMV.step(w, x, tile_size_output=32)
        return GEMV.step(w, y, tile_size_output=256)


def _packer(recording, dev, tmp_path):
    return Packer(
        Timed(recording),
        dev,
        timing=Timing(rounds=2, calls=5),
        repeats=5,
        cache=None,
        fit_cache=tmp_path / "fit",
        log=lambda _: None,
        lock=False,
        model=CostModel(),
    )


def test_width_tunables_are_the_ones_counting_columns_channels_or_cores():
    assert width_tunables(GEMV(M=512, K=2048)) == ["num_aie_columns", "num_channels"]
    assert width_tunables(MHA(num_heads=32, num_KV_heads=8, d=64, seq_pad=1)) == [
        "num_pipelines"
    ]


def test_adjacent_counts_the_switches_a_merge_removes():
    order = ["a", "b", "a", "b", None, "c", "c", "a"]
    assert adjacent(order, {"a": 0, "b": 1, "c": 2}) == {(0, 1): 3, (0, 2): 1}
    assert adjacent(order, {"a": 0, "b": 0, "c": 2}) == {(0, 2): 1}


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
    """A profile names shapes, so the two GEMVs of one shape are one unit,
    set as one; aligning it to one of its arrays' settings puts both on it.
    """
    packer = _packer(Projections().record(w=(2048, 2048), x=(2048,)), npu2, tmp_path)
    (unit,) = set(packer.order)
    assert len(packer.arrays(unit, {})) == 2
    aligned = [
        packer.cores({unit: s})
        for k, s in packer.changes({unit: {}})
        if len(packer.arrays(k, s)) == 1
    ]
    assert min(aligned) * 2 == packer.cores({unit: {}})


def test_a_packing_names_no_dimension_a_hosts_context_sizes(npu2, tmp_path):
    """A host fits its own context, which sizes the decode step's KV cache
    and so MHA and the cache copies: a packing found at one context names
    none of those dimensions, so the model fitted to another packs the same
    designs together."""
    model, sibling = small(), small(max_seq_len=512)
    decode, _ = calls(model, 0, 0, 256, 1, Sampler(0.7, 50), sibling)
    assert any("kv_len" in v for v in decode.varying.values())
    packer = Packer(
        decode,
        npu2,
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
    profile.add_packing(members)
    sizes = []
    for m in (model, sibling):
        _, packing = apply_packings(m.record(**m.shapes()[0]), profile, [], npu2)
        sizes.append([len(g) for g in packing.groups])
    assert sizes[0] == sizes[1] and sizes[0], sizes


class Single(iron.Graph):
    """One step: ``fold_candidates`` needs a pair, so this recording,
    unlike ``Alternating``'s own chain of unary ones, never admits one.
    """

    def body(self, x):
        return ReLU.step(x)


def _version(name: str) -> tuple:
    return ((name, (1,), "bf16"),)


def test_decide_fold_keeps_the_fusions_where_the_call_gains_beyond_noise():
    decode = Timed(Alternating().record(x=(SIZE,)))
    v = _version("decode")
    fusions = [(FusionKind.FOLD, (), (), frozenset({v}))]
    logged = []
    kept = _decide_fold(fusions, decode, v, -50.0, 5.0, logged.append)
    assert kept == fusions
    assert "keeps its folds" in logged[0] and decode.recording.name in logged[0]


def test_decide_fold_narrows_the_version_out_where_it_does_not_gain_beyond_noise():
    """A regression, or a gain too small next to ``CONFIDENCE`` standard
    errors of noise, both refuse to keep it: the version's own entry (the
    only one naming it) is narrowed away entirely, not just logged against.
    """
    decode = Timed(Alternating().record(x=(SIZE,)))
    v = _version("decode")
    fusions = [(FusionKind.FOLD, (), (), frozenset({v}))]
    logged = []
    kept = _decide_fold(fusions, decode, v, -1.0, 10.0, logged.append)
    assert kept == []
    assert "keeps the profile as it stood" in logged[0]

    logged.clear()
    kept = _decide_fold(fusions, decode, v, 5.0, 10.0, logged.append)  # a regression
    assert kept == []
    assert "keeps the profile as it stood" in logged[0]


def test_decide_fold_treats_an_unmeasurable_noise_as_no_gain():
    decode = Timed(Alternating().record(x=(SIZE,)))
    v = _version("decode")
    fusions = [(FusionKind.FOLD, (), (), frozenset({v}))]
    logged = []
    kept = _decide_fold(fusions, decode, v, -50.0, None, logged.append)
    assert kept == []
    assert "do not gain beyond the noise" in logged[0]


def test_fold_profile_leaves_a_profile_with_nothing_to_fold_unchanged():
    """``price_folds_before_packing``'s own early branch (no fold the
    scoping admits) follows from this alone, device-free: a recording with
    no pair to fold (``Single``) adds nothing ``fold_profile`` did not
    already carry.
    """
    base = iron.Profile()
    with_folds = fold_profile(base, [Timed(Single().record(x=(SIZE,)))])
    assert with_folds.fusions() == base.fusions() == []


def test_narrow_for_rejected_drops_a_fold_entry_naming_only_that_version():
    v = _version("decode")
    fusions = [(FusionKind.FOLD, (), (), frozenset({v}))]
    assert _narrow_for_rejected(fusions, v) == []


def test_narrow_for_rejected_shrinks_a_fold_entry_naming_several_versions():
    decode_v, prompt_v = _version("decode"), _version("prompt")
    fusions = [(FusionKind.FOLD, (), (), frozenset({decode_v, prompt_v}))]
    assert _narrow_for_rejected(fusions, decode_v) == [
        (FusionKind.FOLD, (), (), frozenset({prompt_v}))
    ]


def test_narrow_for_rejected_leaves_other_kinds_and_other_versions_alone():
    decode_v, prompt_v = _version("decode"), _version("prompt")
    unscoped_fold = (FusionKind.FOLD, (), (), None)
    prompt_only_fold = (FusionKind.FOLD, (), (), frozenset({prompt_v}))
    stream = (FusionKind.STREAM, (), (), frozenset({decode_v}))
    fusions = [unscoped_fold, prompt_only_fold, stream]
    assert _narrow_for_rejected(fusions, decode_v) == fusions


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
    """``small()``'s decode step and its prompt chunk run SwiGLU at
    different widths (a prompt chunk's rows fold into the one shape), so
    ``fold_profile`` scopes each its own ``SiLU -> ElementwiseMul`` entry to
    its own version alone, not both: the per-version decision ``price_
    folds_before_packing`` makes needs exactly this to tell one version's
    folds from the other's. Only decode's own projections are ``GEMV``
    (the prompt chunk's are ``ProjectionGEMM``, which declares no
    ``fold()``), so its residual-add entries name decode's version only.
    """
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


def test_a_tune_on_an_xclbin_per_step_times_no_switch(npu1, tmp_path):
    """npu1 packs nothing, so its tune neither times the switches a cost
    model is calibrated on (a dispatch) nor writes one; its folds are
    still priced, and its profile written."""
    args = tune_cli.parser("npu1").parse_args([])
    path = tmp_path / "npu1.json"
    found = tune_cli._save_packings(args, [], npu1, iron.Profile(), path, False)
    assert found == path and path.exists()
    assert CostModel.load(npu1.name) is None


# ---------------------------------------------------------------------------
# On the device
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_price_packings_packs_alternating_arrays_bit_identically(tmp_path):
    """Eight steps of two 8-column arrays, each step a switch: the packer
    narrows them to share one configuration and keeps it end to end; the
    packed graph computes what the unpacked one does."""
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
def test_price_packings_skips_a_version_its_switches_cannot_pay(tmp_path):
    """One switch beside eight long steps: no grouping could gain the
    share packing is worth searching for, so the version is not searched."""
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
def test_end_to_end_runs_a_call_at_each_of_its_points():
    """A point bounding past the graph's input is a call it refuses: the
    end-to-end check runs the call at each of its points, not only at its
    own values."""
    dev = aie_utils.ensure_current_device()
    recording = BoundedReLUs().record(x=(SIZE,))
    profile = iron.Profile()
    timing = Timing(rounds=1, calls=2)
    own = Timed(recording, values=dict(n=SIZE))
    delta, _ = _end_to_end(own, dev, profile, profile, timing, print, False)
    assert np.isfinite(delta)
    past = Timed(
        recording,
        values=dict(n=SIZE),
        points=[Point(0.5, dict(n=SIZE)), Point(0.5, dict(n=2 * SIZE))],
    )
    with pytest.raises(IndexError):
        _end_to_end(past, dev, profile, profile, timing, print, False)


@pytest.mark.supported_devices("npu1")
def test_end_to_end_builds_an_xclbin_per_step_on_npu1(npu1):
    """npu1 has no full ELF: the end-to-end check a fold is judged by builds
    each version as an xclbin per step (it asked for a full ELF, and raised)."""
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
    """An entry found in one version narrows its arrays to one column. In
    the other version, at short calls it removes switches and applies
    there too; at long calls the narrowed arrays cost more than the switches
    it removes, so it keeps to the version it names rather than being
    dropped."""
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
    """Three arrays of 16 cores each take 48 of 32 at their own widths: the
    packer narrows the cheapest until they share one configuration, and the
    packed graph computes what the unpacked one does."""
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
