# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pricing on-chip fusions: grouping the fusions a tuner's calls admit, and
choosing among them cheapest first. No device below the line.
"""

import math
import re
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.common.graph.fusion import candidates
from iron.common.graph.record import Recording
from iron.common.image.step import Edge, FusionKind
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tests.support.graphs import Chain as ChainGraph
from iron.tests.support.graphs import Rotate
from iron.tests.support.llama_model import small
from iron.tune.autotune import Point, Timed, Trial
from iron.tune.fusions import (
    FusionGroup,
    NARROWING_EXHAUSTIVE,
    _dominates,
    _resolve_narrowing,
    _widths,
    confirm_fusions,
    fusion_groups,
    group_fit_verdict,
    narrow_group,
    narrowings,
    price_fusions,
    select_rewrites,
    time_fusion_group,
)
from iron.tune.measure import (
    Cache,
    Standalone,
    Timing,
    platform,
    repeat_fusion,
    written_steps,
)

pytestmark = pytest.mark.usefixtures("npu2")

LLAMA_NPU2_PROFILE = Profile.load(
    Path(__file__).resolve().parents[2] / "applications/llama/profiles/npu2.json"
)

W = np.zeros(2048, bfloat16)


def _fused_graph():
    """A graph recording ``ElementwiseMul(SiLU(x), W)``, fusable at size=2048."""

    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=2048, num_aie_columns=1)
            return ElementwiseMul.step(gate, W, tile_size=2048, num_aie_columns=1)

    return Fused()


def _group(dev, first: int, rid: int = 0) -> FusionGroup:
    """A ``FusionGroup`` of SiLU -> ElementwiseMul, occurring once starting
    at ``first`` of recording ``rid``: enough for ``select_rewrites``.
    """
    silu = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    mul = ElementwiseMul(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    group = FusionGroup(FusionKind.STREAM, [silu, mul], [(0, "y", 1, "a")])
    group.occurrences = [(rid, first)]
    return group


# ---------------------------------------------------------------------------
# fusion_groups: grouping and weights
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def llama_recordings():
    model = small()
    decode_shapes, prompt_shapes = model.shapes()
    C = model.config.prefill_chunk
    decode = Timed(model.record(**decode_shapes), values=dict(position=0, token=0))
    prompt = Timed(
        model.record(**prompt_shapes),
        values=dict(position=C - 1, token=0, start=0, rows=C, rope_start=0),
    )
    return decode, prompt


def test_fusion_groups_merges_identical_shapes_across_llama_layers(llama_recordings):
    decode, prompt = llama_recordings
    dev = aie_utils.ensure_current_device()
    groups = fusion_groups([decode, prompt], dev)

    def silu_group(recording):
        rid = id(recording)
        return next(
            g
            for g in groups
            if g.kind is FusionKind.STREAM
            and len(g.steps) == 2
            and type(g.steps[0]) is SiLU
            and type(g.steps[1]) is ElementwiseMul
            and g.occurrences[0][0] == rid
        )

    def silu_pairs(recording):
        return [
            f
            for f in candidates(recording)
            if len(f.steps) == 2
            and type(recording.steps[f.steps[0]].op.resolved(dev)) is SiLU
            and type(recording.steps[f.steps[1]].op.resolved(dev)) is ElementwiseMul
        ]

    decode_group = silu_group(decode.recording)
    prompt_group = silu_group(prompt.recording)
    assert (
        len(decode_group.occurrences) == len(silu_pairs(decode.recording)) == 2
    )  # per layer
    assert len(prompt_group.occurrences) == len(silu_pairs(prompt.recording)) == 2
    # Every layer shares one identity: its points are not counted per layer.
    assert len(decode_group.points) == 1
    assert len(prompt_group.points) == 1


def test_fusion_groups_merges_repeated_shapes_and_tracks_every_occurrence():
    dev = aie_utils.ensure_current_device()
    recording = ChainGraph(size=2048, tile=2048, columns=1).record(a=(2048,), b=(2048,))
    groups = [
        g
        for g in fusion_groups([Timed(recording)], dev)
        if g.kind is FusionKind.STREAM and len(g.steps) == 2
    ]
    assert len(groups) == 3

    add_to_silu = next(g for g in groups if type(g.steps[0]) is ElementwiseAdd)
    assert sorted(p for _, p in add_to_silu.occurrences) == [0, 3]
    assert len(add_to_silu.points) == 1  # both occurrences share one identity

    silu_to_mul = next(g for g in groups if type(g.steps[1]) is ElementwiseMul)
    assert sorted(p for _, p in silu_to_mul.occurrences) == [1]

    mul_to_add = next(g for g in groups if type(g.steps[0]) is ElementwiseMul)
    assert sorted(p for _, p in mul_to_add.occurrences) == [2]


def test_fusion_groups_carries_each_points_weight():
    dev = aie_utils.ensure_current_device()
    recording = _fused_graph().record(x=(2048,))
    calls = [Timed(recording, points=[Point(0.3, {}), Point(0.7, {})])]
    [group] = [
        g
        for g in fusion_groups(calls, dev)
        if g.kind is FusionKind.STREAM and len(g.steps) == 2
    ]
    assert [weight for weight, _ in group.points] == [0.3, 0.7]


def test_op_values_falls_back_to_the_calls_own_value_a_point_does_not_give():
    """A point need not repeat every per-call value the call itself already
    gives: ``n``, which ``RoPE``'s one step binds its rows to, comes from
    ``Timed.values`` alone since neither point moves it, both points
    folding into the one identity it gives.
    """
    dev = aie_utils.ensure_current_device()
    recording = Rotate().record(x=(256, 64), angles=(256, 64))
    call = Timed(recording, values={"n": 128}, points=[Point(0.4, {}), Point(0.6, {})])
    [op] = {s.op for s in recording.steps}
    assert call.op_points(op) == [(1.0, {"valid": 128, "valid_angles": 128})]


# ---------------------------------------------------------------------------
# select_rewrites: cheapest first, never two sharing a step
# ---------------------------------------------------------------------------


def test_select_rewrites_takes_every_non_overlapping_gain():
    dev = aie_utils.ensure_current_device()
    a, b = _group(dev, 0), _group(dev, 4)
    priced = [(a, Trial({}, -10.0, 1.0)), (b, Trial({}, -5.0, 1.0))]
    assert set(select_rewrites(priced, log=lambda _: None)) == {a, b}


def test_select_rewrites_prefers_the_cheaper_of_two_overlapping_gains():
    dev = aie_utils.ensure_current_device()
    costlier, cheaper = _group(dev, 0), _group(dev, 0)
    # The cheaper is priced second: cost, not discovery order, decides.
    priced = [
        (costlier, Trial({}, -5.0, 1.0)),
        (cheaper, Trial({}, -20.0, 1.0)),
    ]
    assert select_rewrites(priced, log=lambda _: None) == [cheaper]


def test_select_rewrites_excludes_a_trial_that_does_not_gain():
    dev = aie_utils.ensure_current_device()
    gains, flat = _group(dev, 0), _group(dev, 4)
    priced = [(gains, Trial({}, -10.0, 1.0)), (flat, Trial({}, 2.0, 1.0))]
    assert select_rewrites(priced, log=lambda _: None) == [gains]


def test_select_rewrites_excludes_a_refused_trial():
    dev = aie_utils.ensure_current_device()
    group = _group(dev, 0)
    priced = [(group, Trial({}, -10.0, 1.0, refused="not bit-identical"))]
    assert select_rewrites(priced, log=lambda _: None) == []


# ---------------------------------------------------------------------------
# measure_fusion: wiring and output comparison kept kind-agnostic, for a
# fan-out's several edges and several host-visible outputs
# ---------------------------------------------------------------------------


def test_repeat_fusion_keeps_edges_for_a_kind_other_than_stream():
    """A staged fan-out's edges stay wired: ``Fusion`` itself refuses any
    only for ``PACK`` and ``MERGE``.
    """
    fusion = repeat_fusion(FusionKind.STAGED, 3, 2, [(0, "y", 1, "a")])
    assert fusion.steps == (3, 4)
    assert fusion.edges == (Edge(3, "y", 4, "a"),)


def test_repeat_fusion_takes_no_edges_for_pack_or_merge():
    fusion = repeat_fusion(FusionKind.PACK, 0, 2, [])
    assert fusion.edges == ()


def test_written_steps_keys_by_step_so_same_named_outputs_do_not_collide():
    dev = aie_utils.ensure_current_device()
    a = SiLU(size=2048, tile_size=2048, num_aie_columns=1).resolved(dev)
    b = SiLU(size=4096, tile_size=4096, num_aie_columns=1).resolved(dev)
    run = Standalone("two_silus", [a, b], full_elf=True)
    assert set(written_steps(run)) == {"0.y", "1.y"}


# ---------------------------------------------------------------------------
# Joint narrowing: searching the fused form's tunables, and sharing a
# member's shape safely with an occurrence a fusion does not narrow
# ---------------------------------------------------------------------------


def _merge_members(dev, add_cols=None):
    """RMSNorm -> GEMV -> ElementwiseAdd at Llama 1B decode's own shape
    (``rows=1``, ``M=K=2048``): the profile's own widths do not co-reside
    (GEMV and ElementwiseAdd both the whole chip wide); narrowing
    ElementwiseAdd alone lets them.
    """
    rms = LLAMA_NPU2_PROFILE.make(RMSNorm, rows=1, tile_size=2048, weighted=True)
    gemv = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048)
    add = LLAMA_NPU2_PROFILE.make(ElementwiseAdd, size=2048)
    if add_cols is not None:
        add = add._with_tunables(num_aie_columns=add_cols)
    return rms.resolved(dev), gemv.resolved(dev), add.resolved(dev)


def test_widths_orders_widest_first_and_keeps_its_own_setting():
    dev = aie_utils.ensure_current_device()
    gemv = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048)
    found = _widths(gemv, dev)
    cols = [w["num_aie_columns"] for w in found]
    assert cols == sorted(cols, reverse=True)
    own = vars(gemv.resolved(dev))["num_aie_columns"]
    assert any(w["num_aie_columns"] == own for w in found)


def test_dominates_requires_every_member_at_least_as_wide():
    wide = [{"num_aie_columns": 8}, {"num_aie_columns": 4}]
    narrower = [{"num_aie_columns": 4}, {"num_aie_columns": 4}]
    assert _dominates(wide, narrower)
    assert not _dominates(narrower, wide)
    assert not _dominates(wide, wide)


def test_group_fit_verdict_finds_the_merge_that_only_fits_narrowed(tmp_path):
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    assert group_fit_verdict([rms, gemv, add], fit_cache=tmp_path) is not None
    _, _, narrow_add = _merge_members(dev, add_cols=2)
    assert group_fit_verdict([rms, gemv, narrow_add], fit_cache=tmp_path) is None


def test_narrowings_narrows_only_the_member_that_needs_it(tmp_path):
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    group = FusionGroup(FusionKind.MERGE, [rms, gemv, add], [])
    combos = narrowings(group, dev, fit_cache=tmp_path)
    assert combos, "expected at least one combination that co-resides"
    cols = [s.get("num_aie_columns") for s in combos[0]]
    assert cols[1] == vars(gemv)["num_aie_columns"]  # GEMV never narrows
    assert cols[2] < vars(add)["num_aie_columns"]  # ElementwiseAdd does


def test_resolve_narrowing_locks_a_narrowed_members_shape():
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    group = FusionGroup(FusionKind.MERGE, [rms, gemv, add], [])
    group.occurrences = [(0, 0)]
    narrowed_add = {"num_aie_columns": 2}
    kept, entries = _resolve_narrowing(
        [group],
        {group: ({}, {}, narrowed_add)},
        {group: Trial({}, -50.0, 1.0)},
        [],
        dev,
        full_elf=True,
        timing=Timing(),
        repeats=9,
        cache=None,
        remeasure=False,
        log=lambda _: None,
    )
    assert kept == [group]
    [tunables] = [t for s, t in entries.values() if s.cls is ElementwiseAdd]
    assert tunables["num_aie_columns"] == 2


def test_resolve_narrowing_drops_a_group_whose_narrowing_conflicts():
    """Two groups sharing ElementwiseAdd(2048) each narrow it, to a
    different width: the cheaper, priced first, locks its own; the costlier
    cannot match it (no narrowing of its own it was priced at) and is
    dropped rather than silently narrowed to the cheaper's width.
    """
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    cheaper = FusionGroup(FusionKind.MERGE, [rms, gemv, add], [])
    cheaper.occurrences = [(0, 0)]
    costlier = FusionGroup(FusionKind.MERGE, [rms, gemv, add], [])
    costlier.occurrences = [(0, 4)]
    narrowed_2 = {"num_aie_columns": 2}
    narrowed_4 = {"num_aie_columns": 4}
    taken = select_rewrites(
        [(cheaper, Trial({}, -50.0, 1.0)), (costlier, Trial({}, -10.0, 1.0))],
        log=lambda _: None,
    )
    kept, entries = _resolve_narrowing(
        taken,
        {cheaper: ({}, {}, narrowed_2), costlier: ({}, {}, narrowed_4)},
        {cheaper: Trial({}, -50.0, 1.0), costlier: Trial({}, -10.0, 1.0)},
        [],
        dev,
        full_elf=True,
        timing=Timing(),
        repeats=9,
        cache=None,
        remeasure=False,
        log=lambda _: None,
    )
    assert kept == [cheaper]


# ---------------------------------------------------------------------------
# price_fusions: the profile it returns
# ---------------------------------------------------------------------------


def test_price_fusions_with_no_candidates_keeps_tunables_and_fusion_entries():
    dev = aie_utils.ensure_current_device()
    profile = Profile()
    profile.add(SiLU, num_aie_columns=1)
    profile.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=4096)), (ElementwiseMul, dict(size=4096))],
        [(0, "y", 1, "a")],
    )
    out = price_fusions([], dev, profile, full_elf=True, log=lambda _: None)
    assert out.tunables_for(SiLU, {}) == {"num_aie_columns": 1}
    gate = SiLU(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    up = ElementwiseMul(size=4096, tile_size=4096, num_aie_columns=1).resolved()
    assert out.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")])


# ---------------------------------------------------------------------------
# On the device: a gaining fusion is written and runs bit-identically.
# ---------------------------------------------------------------------------

FUSION_SIZE, FUSION_TILE, FUSION_COLS = 2**22, 4096, 8
W_BIG = np.zeros(FUSION_SIZE, bfloat16)


def _big_fused_graph():
    class Fused(iron.Graph):
        def body(self, x):
            gate = SiLU.step(x, tile_size=FUSION_TILE, num_aie_columns=FUSION_COLS)
            return ElementwiseMul.step(
                gate, W_BIG, tile_size=FUSION_TILE, num_aie_columns=FUSION_COLS
            )

    return Fused()


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_pricing_a_gaining_fusion_writes_an_entry_that_runs_bit_identically(tmp_path):
    recording = _big_fused_graph().record(x=(FUSION_SIZE,))
    dev = aie_utils.ensure_current_device()
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    profile = price_fusions(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        log=lambda _: None,
    )
    gate = SiLU(
        size=FUSION_SIZE, tile_size=FUSION_TILE, num_aie_columns=FUSION_COLS
    ).resolved()
    up = ElementwiseMul(
        size=FUSION_SIZE, tile_size=FUSION_TILE, num_aie_columns=FUSION_COLS
    ).resolved()
    assert profile.fused(FusionKind.STREAM, [gate, up], [(0, "y", 1, "a")])

    fused_graph = _big_fused_graph()
    fused_graph.profile = profile
    fused = fused_graph.compile(full_elf=True, x=(FUSION_SIZE,))
    plain = _big_fused_graph().compile(full_elf=True, x=(FUSION_SIZE,))

    rng = np.random.default_rng(0)
    x = (rng.random(FUSION_SIZE) * 4 - 2).astype(bfloat16)
    want = np.array(plain(x).numpy()[:FUSION_SIZE])
    got = np.array(fused(x).numpy()[:FUSION_SIZE])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()


# ---------------------------------------------------------------------------
# On the device: the fixed frame against an independent in-image measurement.
# ---------------------------------------------------------------------------

_END_TO_END = re.compile(r"([-+]\d+\.\d+) ± (\?|\d+\.\d+) us end to end")


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_fixed_frame_agrees_with_decode_groups_priced_in_the_whole_step(
    llama_recordings, tmp_path
):
    """Each of decode's own 2-step fusion groups (SiLU -> ElementwiseMul and
    both residual adds, GEMV -> ElementwiseAdd), ``measure_fusion``'s
    standalone price (``time_fusion_group``) against an independent figure
    for the same shape: timed compiled into the whole decode step against
    the same step unfused (``confirm_fusions``, whose own log line carries
    it) and divided by its occurrences (2 per group, one per layer, down
    Llama's small shape).

    The band is each side's own standard error, summed in quadrature (the
    two are independent interleaved timings of one shape) and multiplied by
    3, not the 2 standard errors ``Trial.gains`` takes elsewhere, floored at
    half the bug's own size (~165 us, one reconfigure): GEMV -> Add's
    standalone price and its in-image one agree only to 10-30 us (its own
    placement is not pinned, so a probe alone and one among decode's other
    designs need not place it alike), well inside a regression back to the
    old frame's bias but outside 3 standard errors most rounds. This runs
    beside other agents' own NPU runs too, whose jitter this test's own
    rounds do not sample.
    """
    decode, _ = llama_recordings
    dev = aie_utils.ensure_current_device()
    groups = [
        g
        for g in fusion_groups([decode], dev)
        if g.kind is FusionKind.STREAM and len(g.steps) == 2
    ]
    assert len(groups) >= 2, "expected at least SiLU -> Mul and a GEMV -> Add shape"

    timing = Timing(rounds=8, calls=10)
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    # decode's own Timed, for pricing alone, gives no per-call values; a
    # decode step CompiledGraph dispatches, so needs one.
    dispatched = Timed(decode.recording, values=dict(position=0, token=0))

    for group in groups:
        trial = time_fusion_group(
            group, full_elf=True, timing=timing, cache=cache, log=lambda _: None
        )
        assert trial.refused is None and trial.noise_us is not None

        logged = []
        confirm_fusions(
            [dispatched],
            dev,
            [group],
            {group: Trial({}, -1e6, 1.0)},  # the only candidate: its figure unread
            Profile(),
            full_elf=True,
            timing=timing,
            log=logged.append,
        )
        [line] = [m for m in logged if "end to end" in m]
        delta_s, noise_s = _END_TO_END.search(line).groups()
        occurrences = len(group.occurrences)
        in_image = float(delta_s) / occurrences
        in_image_noise = float(noise_s) / occurrences

        band = max(3 * math.hypot(trial.noise_us, in_image_noise), 80.0)
        assert abs(trial.delta_us - in_image) < band, (
            f"{group}: standalone {trial.delta_us:+.1f} us vs in-image "
            f"{in_image:+.1f} us, band {band:.1f} us"
        )


# ---------------------------------------------------------------------------
# On the device: a pack that already co-resides, and a merge that only
# fits its members narrowed.
# ---------------------------------------------------------------------------


def _qkv_recording(dev):
    """Llama decode's q/k/v GEMVs (M=2048/512/512, K=2048), independent:
    co-reside at the profile's own width, so packing them needs no
    narrowing.
    """
    q = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048).resolved(dev)
    k = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048).resolved(dev)
    v = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048).resolved(dev)
    steps = sequences.steps(
        (q, "Aq", "x", "oq"), (k, "Ak", "x", "ok"), (v, "Av", "x", "ov")
    )
    return Recording.of_steps("qkv", steps, ["Aq", "Ak", "Av", "x"], ["oq", "ok", "ov"])


def _short_decode_recording(dev):
    rms, gemv, add = _merge_members(dev)
    steps = sequences.steps(
        (rms, "x", "w", "n"), (gemv, "A", "n", "c"), (add, "r", "c", "out")
    )
    return Recording.of_steps("short_decode", steps, ["x", "w", "A", "r"], ["out"])


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_narrow_group_takes_the_qkv_pack_without_narrowing(tmp_path):
    dev = aie_utils.ensure_current_device()
    q = LLAMA_NPU2_PROFILE.make(GEMV, M=2048, K=2048).resolved(dev)
    k = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048).resolved(dev)
    v = LLAMA_NPU2_PROFILE.make(GEMV, M=512, K=2048).resolved(dev)
    group = FusionGroup(FusionKind.PACK, [q, k, v], [])
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    trial, combo = narrow_group(
        group,
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        fit_cache=tmp_path / "fits",
        log=lambda _: None,
    )
    assert combo is None, "q/k/v already co-reside at the profile's own width"
    assert trial.refused is None


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_price_fusions_takes_the_qkv_pack_without_confirming_end_to_end(tmp_path):
    """Three GEMVs alone, with no other step around them to amortize a
    configure the way Llama's own decode step's other designs do, do not
    gain from packing end to end (``confirm_fusions`` correctly drops this
    isolated recording's pack, as it should); ``confirm=False`` checks only
    that ``price_fusions`` finds and takes a pack on its own standalone
    price. ``candidates`` proposes every sub-window too (q&k, k&v), each a
    step cheaper than the full triple might overlap and take instead
    (``select_rewrites``); any of them, narrowed or not, is this test's own.
    """
    dev = aie_utils.ensure_current_device()
    recording = _qkv_recording(dev)
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    profile = price_fusions(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=4, calls=10),
        cache=cache,
        fit_cache=tmp_path / "fits",
        confirm=False,
        log=lambda _: None,
    )
    kinds = [kind for kind, _, _ in profile.fusions()]
    assert kinds == [FusionKind.PACK]


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_narrow_group_prices_the_merge_that_only_fits_narrowed(tmp_path):
    dev = aie_utils.ensure_current_device()
    rms, gemv, add = _merge_members(dev)
    group = FusionGroup(FusionKind.MERGE, [rms, gemv, add], [])
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    trial, combo = narrow_group(
        group,
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        fit_cache=tmp_path / "fits",
        log=lambda _: None,
    )
    assert combo is not None, "the profile's own width should not co-reside"
    assert combo[1]["num_aie_columns"] == vars(gemv)["num_aie_columns"]
    assert combo[2]["num_aie_columns"] < vars(add)["num_aie_columns"]
    assert trial.refused is None


@pytest.mark.supported_devices("npu2")
@pytest.mark.extensive
def test_price_fusions_takes_the_cheaper_of_two_overlapping_fusions(tmp_path):
    """RMSNorm -> GEMV -> ElementwiseAdd admits both a GEMV -> ElementwiseAdd
    stream and an RMSNorm -> GEMV merge, overlapping at GEMV: ``candidates``
    finds the merge only at 2 steps here (``iron.common.graph.fusion``'s own
    ``_merge_runs`` filters a window by fit at the profile's own width
    before proposing it, so the 3-step merge that only fits ElementwiseAdd
    narrowed is not among its candidates today). The stream already builds
    fused at its members' own width (``narrow_group`` tries that before any
    narrowing search), so no tunable moves; it prices cheaper than the
    merge, so ``select_rewrites`` takes it and skips the merge
    (``confirm_fusions`` would raise were the stream not bit-identical to
    the same steps unfused).
    """
    dev = aie_utils.ensure_current_device()
    recording = _short_decode_recording(dev)
    report = platform()
    cache = Cache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    profile = price_fusions(
        [Timed(recording)],
        dev,
        full_elf=True,
        timing=Timing(rounds=2, calls=5),
        cache=cache,
        fit_cache=tmp_path / "fits",
        log=lambda _: None,
    )
    rms, gemv, add = _merge_members(dev)
    assert profile.fused(FusionKind.STREAM, [gemv, add], [(0, "C", 1, "b")])
    assert not profile.fused(FusionKind.MERGE, [rms, gemv], ())
