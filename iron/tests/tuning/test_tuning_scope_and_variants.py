# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Transformation tests for scope and variants, which design applies where and when."""

import numpy as np
import pytest

import iron
from iron import Carried, Precision, Scratchpad
from iron.common.declare import Profile
from iron.common.declare.composition import (
    Binding,
    Entry,
    Hold,
    Member,
    Refinement,
    Region,
    Schedule,
    Scope,
    Variants,
)
from iron.common.graph.fusion import composed
from iron.common.graph.record import Recording
from iron.common.image.packaging import SCRATCHPAD_WORDS
from iron.common.image.step import BufferRef, Edge, EdgeKind, SequenceStep
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.operators.layer_norm import LayerNorm
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import toys_schedule
from iron.tests.support.toys_edges import member
from iron.tests.support.toys_settings import (
    RangedPair,
    coded_consumer_recording_with_weight,
    small_integer_weight,
)
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Point, Timed
from iron.tune.fusions import Applied
from iron.tune.search import (
    AddVariants,
    Switches,
    candidates,
    check,
    fit,
    measure,
    search,
)

pytestmark = pytest.mark.usefixtures("device")


def _split_at_256() -> Variants:
    """Return RangedPair's ``rows`` split at 256: GEMM at 256 rows below, at the full 2048 above."""
    small = Entry(root=Member(cls=GEMM, dims={"M": 256, "K": 256, "N": 256}))
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    return Variants(
        values=("rows",), ranges=((((0, 256),), small), (((257, 2048),), large))
    )


def _gemv_decode(device):
    """Return a decode-sized GEMV's recording."""
    return Recording.of_step(GEMV(M=2048, K=2048).resolved(device))


class _Projection(iron.Graph):
    """One held weight's GEMV over a decode step's vector, or each row of a prompt chunk."""

    def __init__(self, M: int, K: int):
        self.w = iron.param(small_integer_weight((M, K), 0))

    def body(self, x):
        rows = x.shape[0] if len(x.shape) == 2 else None
        return GEMV.step(self.w, x, num_batches=rows, repeat=rows or 1)


@unbuilt
def test_scope_entries_round_trip_by_version_occurrence_and_device_part(
    tmp_path, device
):
    """A ``Scope`` (versions, occurrences, device part) round-trips through the profile, and ``candidates`` proposes each."""
    decode_rec = _gemv_decode(device)
    member = Member(cls=GEMV, dims={"M": 2048, "K": 2048})
    by_version = Entry(
        root=member, scope=Scope(versions=frozenset({decode_rec.version}))
    )
    profile = Profile()
    profile.add_entry(by_version)
    profile.add_entry(Entry(root=member, scope=Scope(occurrences=(0,))))
    profile.add_entry(Entry(root=member, scope=Scope(device_part="strix-halo")))
    path = tmp_path / "profile.json"
    profile.save(path)
    loaded = Profile.load(path)
    assert loaded.entries() == profile.entries()
    found = list(candidates([Timed(decode_rec)], loaded, device))
    assert any(e.apply(Profile()).entries() == [by_version] for e in found)


@pytest.mark.supported_devices("npu1", "npu2")
def test_an_entry_scoped_to_one_run_composes_that_run_alone(device):
    """A region scoped to the last of its four runs (``Scope.occurrences``) fuses that run alone, the others as recorded, bit-identical to the untuned build."""
    recording = toys_schedule.Alternating(2).record(x=(2048,))
    relu, tanh = (member(recording.steps[s].op) for s in (0, 1))
    region = Region(
        parts=(relu, tanh), edges=(Edge(0, "y", 1, "x", kind=EdgeKind.STREAM),)
    )
    profile = Profile()
    profile.add_entry(Entry(root=region, scope=Scope(occurrences=(3,))))
    assert [f.steps for f in composed(recording, profile)[1]] == [(6, 7)]
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
def test_a_design_per_range_round_trips_as_variants(tmp_path, device):
    """A design per range of a per-call value (``Variants``), boundaries from a grid, round-trips and is proposed."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    small = Entry(root=Member(cls=GEMM, dims={"M": 256, "K": 256, "N": 256}))
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    variants = Variants(
        values=("rows",),
        ranges=(
            (((0, 256),), small),
            (((257, 2048),), large),
        ),
    )
    profile = Profile()
    profile.add_variants(variants)
    path = tmp_path / "profile.json"
    profile.save(path)
    loaded = Profile.load(path)
    assert loaded.variants() == [variants]
    # Proposed from a profile varying nothing yet, each range's entry the GEMM
    # at its capacity, as candidates names a step (all of its dims).
    found = list(candidates([Timed(recording)], Profile(), device))
    assert any(
        isinstance(e, AddVariants)
        and e.variants.values == variants.values
        and [box for box, _ in e.variants.ranges] == [box for box, _ in variants.ranges]
        and [(r.root.cls, r.root.dims["M"]) for _, r in e.variants.ranges]
        == [(r.root.cls, r.root.dims["M"]) for _, r in variants.ranges]
        for e in found
    )


@unbuilt
def test_a_binding_names_how_a_per_call_value_reaches_the_design(tmp_path, device):
    """A per-call value's binding (compile, runtime, per_range) round-trips, and ``candidates`` proposes each."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    compile_bound = Binding(value="rows", how="compile")
    runtime_bound = Binding(value="valid", how="runtime")
    profile = Profile()
    profile.add_binding(compile_bound)
    profile.add_binding(runtime_bound)
    path = tmp_path / "profile.json"
    profile.save(path)
    loaded = Profile.load(path)
    assert loaded.bindings() == [compile_bound, runtime_bound]
    found = list(candidates([Timed(recording)], loaded, device))
    assert any(
        Binding(value="rows", how="per_range") in e.apply(Profile()).bindings()
        for e in found
    )


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_variant_is_bit_identical_to_the_untuned_build_on_both_sides_of_its_boundary(
    device,
):
    """A variant is bit-identical to the single bounded baseline at each side of its boundary.

    A call's ``values`` carries ``rows`` at one specific number: one call at 256 (the
    small variant's own range, the graph re-recorded at 256 rows of ``x``) and one at
    257 (the large variant's), both held to the one baseline design bounded at the full
    2048. ``valid``, which no variant is over, is at its full 256 in both.
    """
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    baseline = Profile()
    baseline.add(GEMM, M=2048, K=256, N=256, tile_m=64)
    small = Entry(root=Member(cls=GEMM, dims={"M": 256, "K": 256, "N": 256}))
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    variants = Variants(
        values=("rows",), ranges=((((0, 256),), small), (((257, 2048),), large))
    )
    tuned = Profile()
    tuned.add_variants(variants)
    at_small = Timed(recording, values={"rows": 256, "valid": 256})
    at_large = Timed(recording, values={"rows": 257, "valid": 256})
    for call in (at_small, at_large):
        result = check(tuned, baseline, [call], device, refinement=Refinement.EXACT)
        assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_derived_chunk_size_is_checked_against_its_base(device, request):
    """``Schedule.size`` naming a smaller derived chunk is bit-identical against the chunk's own base, run at the full length.

    Running fewer rows of a prompt chunk is a shorter call, not a reordered reduction, so
    this is held to bit identity. The half chunk is the graph re-recorded at four of the
    chunk's eight rows, run twice over them.
    """
    if not device.can_dispatch_full_elf:
        # fit waits on a derived version on an xclbin per step.
        request.applymarker(unbuilt)
    chunk = _Projection(2048, 2048).record(x=(8, 2048))
    base = Profile()
    derived = Profile()
    derived.add_schedule(Schedule(version=chunk.version, size="half_chunk"))
    result = check(derived, base, [Timed(chunk)], device, refinement=Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_boundary_is_kept_only_where_its_saving_beats_a_switch_and_one_more_design(
    device,
):
    """The tuner keeps a boundary only where the calls it serves gain over the single bounded design plus a switch and a compile.

    The split is sized so that its small side is clearly faster than the single design
    bounded at the full 2048 (``measure``'s ratio under 0.95), so ``search`` must keep it.
    The call runs most of its points at 256 rows and some at 1024. ``search`` keeps
    the split over ``rows`` that pays most, at a power of two from 256 up so the
    256-row point runs on a design smaller than the bounded one: on npu2, at 1024,
    both points on its 1024-row design with no switch between calls.
    """
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    points = (Point(0.9, {"rows": 256}), Point(0.1, {"rows": 1024}))
    calls = [Timed(recording, values={"rows": 256, "valid": 256}, points=points)]
    start = Profile()
    with_entry = Profile()
    with_entry.add_variants(_split_at_256())
    ratio = measure(with_entry, start, calls, device).ratio
    assert ratio < 0.95
    # On a warm build cache search reaches and prices its splits in about 190 s.
    tuned = search(calls, start, device, budget_s=300.0)
    (kept,) = tuned.variants()
    assert kept.values == ("rows",)
    (((_, boundary),), _), _ = kept.ranges
    assert boundary in (256, 512, 1024)


@pytest.mark.parametrize(
    "order",
    [
        "read_before_last_write",
        "read_unwritten_part",
        "read_after_writes",
        "read_written_part_first",
        "unwritten_part_unread",
    ],
)
def test_an_output_read_where_a_call_has_not_written_it_breaks_a_merge(device, order):
    """A returned output written in parts outlasts the call where a step reads part of it this call has not yet written.

    Read before the write of its second half, or a half no step writes, each call reads
    what the call before left there, so merging calls is refused before any build.
    Read only where this call already wrote it, or with a half no step writes and none
    reads, it is the host's after each call, and the merge waits on what is not built
    rather than being refused.
    """
    add = ElementwiseAdd(size=256, tile_size=128, num_aie_columns=1)
    first, second = BufferRef("out", 0, 512), BufferRef("out", 512, 512)
    writes = [
        SequenceStep(add, (BufferRef("x"), BufferRef("x"), first)),
        SequenceStep(add, (BufferRef("x"), BufferRef("x"), second)),
    ]
    reads = SequenceStep(add, (BufferRef("x"), second, BufferRef("t")))
    reads_first = SequenceStep(add, (BufferRef("x"), first, BufferRef("t")))
    steps = {
        "read_before_last_write": [writes[0], reads, writes[1]],
        "read_unwritten_part": [writes[0], reads],
        "read_after_writes": [*writes, reads],
        "read_written_part_first": [writes[0], reads_first, writes[1]],
        "unwritten_part_unread": [writes[0], reads_first],
    }[order]
    recording = Recording.of_steps(
        "halves", steps, ["x"], ["out", "t"], pinned={"out": 1024}
    )
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, size="merged_2x"))
    if order in (
        "read_after_writes",
        "read_written_part_first",
        "unwritten_part_unread",
    ):
        with pytest.raises(NotImplementedError, match="part of out"):
            fit(profile, [Timed(recording)], device)
        return
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "breaks a dependence" in (result.why or "")


def test_a_call_whose_points_span_more_than_one_range_is_refused_before_any_build(
    device,
):
    """A call at ``rows=256`` timed at 64 and at 1024 would run the 256-row design past its capacity: refused, not built."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    small = Entry(root=Member(cls=GEMM, dims={"M": 256, "K": 256, "N": 256}))
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    tuned = Profile()
    tuned.add_variants(
        Variants(
            values=("rows",), ranges=((((0, 256),), small), (((257, 2048),), large))
        )
    )
    points = (Point(0.5, {"rows": 64}), Point(0.5, {"rows": 1024}))
    call = Timed(recording, values={"rows": 256, "valid": 256}, points=points)
    with pytest.raises(NotImplementedError, match="span more than one range"):
        Applied.of(call, tuned, device)
    within = Timed(recording, values={"rows": 256, "valid": 256}, points=points[:1])
    assert Applied.of(within, tuned, device).recording.steps[0].op.M == 256


def test_a_range_whose_capacity_the_graph_cannot_record_is_refused(device):
    """A range up to 100 rows records a GEMM of 100 rows, which GEMM refuses: a design not legal at that capacity, refused before any build."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    small = Entry(root=Member(cls=GEMM, dims={"M": 100, "K": 256, "N": 256}))
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    profile = Profile()
    profile.add_variants(
        Variants(
            values=("rows",), ranges=((((0, 100),), small), (((101, 2048),), large))
        )
    )
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "not legal" in (result.why or "")


def test_a_call_whose_points_span_more_than_one_range_fits(device):
    """A call timed at 64 and at 1024 runs each point on its own range's design, each fitted at its capacity, so ``fit`` admits it."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    tuned = Profile()
    tuned.add_variants(_split_at_256())
    points = (Point(0.5, {"rows": 64}), Point(0.5, {"rows": 1024}))
    call = Timed(recording, values={"rows": 256, "valid": 256}, points=points)
    assert fit(tuned, [call], device).ok
    bare = Timed(recording)
    with pytest.raises(NotImplementedError, match="does not give rows"):
        fit(tuned, [bare], device)


def test_a_split_both_versions_take_is_fitted_beside_what_only_one_takes(device):
    """Two versions split at 256 rows, the narrower one scheduled and its copy packed: each range's design takes what its own version does.

    The narrower version's schedule and pack name none of the wider one's
    steps, so the wider one's designs are fitted without them; the calls as a
    whole are still held to matching every entry.
    """
    g = RangedPair(K=256, N=256)
    wide = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    narrow = g.record(x=(2048, 256), w=(256, 256), y=(1024,))
    calls = [
        Timed(wide, values={"rows": 256, "valid": 256}),
        Timed(narrow, values={"rows": 256, "valid": 128}),
    ]
    profile = Profile()
    profile.add_variants(_split_at_256())
    profile.add_schedule(Schedule(version=narrow.version))
    profile.add_entry(Entry(Region(parts=(member(narrow.steps[1].op),))))
    result = fit(profile, calls, device)
    assert result.ok, result.why
    with pytest.raises(ValueError, match="matches none of the calls' steps"):
        fit(profile, calls[:1], device)


class _NormThenNorm(iron.Graph):
    """A norm over the first ``n`` rows of ``x`` on one lane, then a norm of those rows on the lanes its profile gives."""

    def body(self, x, *, n: Scratchpad[np.int32]):
        return LayerNorm.step(RMSNorm.step(x[:n], num_aie_columns=1))


def test_a_ranges_design_balances_only_at_its_own_values(device):
    """Split at 8 rows, held in L1: the top design's second norm on two lanes balances only at an even ``n``, and runs at 8 alone.

    Below 8 the one-lane design runs, so nothing refuses the split at 1. What
    still waits is the analysis of a call bounded at 0.
    """
    recording = _NormThenNorm().record(x=(8, 256))
    region = Region(
        tuple(member(s.op) for s in recording.steps), (Edge(0, "y", 1, "x"),)
    )
    below, full = (
        Profile.dims(LayerNorm, vars(r.steps[1].op))
        for r in (recording.at_capacity({"n": 7}), recording)
    )
    profile = Profile()
    profile.add(LayerNorm, num_aie_columns=1)
    profile.add_entry(Entry(region.held(0, Hold.L1).deepened(0, 2)))
    profile.add_variants(
        Variants(
            values=("n",),
            ranges=(
                (
                    ((0, 7),),
                    Entry(Member(LayerNorm, below, {"num_aie_columns": 1})),
                ),
                (((8, 8),), Entry(Member(LayerNorm, full, {"num_aie_columns": 2}))),
            ),
        )
    )
    with pytest.raises(NotImplementedError, match="at n = 0"):
        fit(profile, [Timed(recording, {"n": 8})], device)


def _packed(recording) -> Entry:
    """Return RangedPair's GEMM and copy as one pack (a region of no edges), named at the recording's shapes."""
    return Entry(Region(parts=tuple(member(s.op) for s in recording.steps)))


def test_a_design_per_range_keeps_what_the_profile_composes_at_its_capacity(device):
    """A pack naming the 2048-row GEMM is named again at 256 rows in the design below the boundary, so the range keeps it."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    profile = Profile()
    profile.add_entry(_packed(recording))
    profile.add_variants(_split_at_256())
    variant, chosen = recording.selected(profile, {"rows": 128, "valid": 256})
    (entry,) = chosen.entries()
    assert [m.dims["M"] for m in entry.root.steps() if m.cls is GEMM] == [256]
    assert variant.occurrences(entry) == ((0, 1),)
    full, kept = recording.selected(profile, {"rows": 1024, "valid": 256})
    assert full is recording and kept.entries() == profile.entries()


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_pack_and_a_split_are_bit_identical_on_each_design(device):
    """The pack beside the split at 256, a call at 128 and at 1024: each point on its design, the pack named at that design's capacity."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    baseline = Profile()
    baseline.add(GEMM, M=2048, K=256, N=256, tile_m=64)
    tuned = Profile()
    tuned.add_entry(_packed(recording))
    tuned.add_variants(_split_at_256())
    points = (Point(0.5, {"rows": 128}), Point(0.5, {"rows": 1024}))
    call = Timed(recording, values={"rows": 128, "valid": 256}, points=points)
    result = check(tuned, baseline, [call], device, refinement=Refinement.EXACT)
    assert result.ok, result.why


class _Growing(iron.Graph):
    """A projection of ``x``'s first ``rows``, ``rows`` one more each call, as a decode position steps."""

    def body(self, x, w, *, rows: Carried[np.int32]):
        projected = GEMM.step(x[:rows], w, b_col_maj=True, precision=Precision.MEDIUM)
        return projected, iron.carry(rows=rows + 1)


def test_switches_follow_the_calls_order_where_the_varied_value_is_carried(device):
    """Carried one up a call from 200, the calls cross 256 once in their 1849 calls up to 2048, into the 2048-row design.

    With no order (RangedPair's ``rows`` is not carried), consecutive calls are taken as
    independent draws of the points: 90% at 256 and 10% at 1024 switch into each design
    0.9 x 0.1 of the time.
    """
    split = _split_at_256()
    profile = Profile()
    profile.add_variants(split)
    growing = _Growing().record(x=(2048, 256), w=(256, 256))
    ordered = Switches.of(Timed(growing, values={"rows": 200}), profile)
    small, large = ((box,) for box, _ in split.ranges)
    assert ordered.ordered
    assert ordered.rates[small] == 0
    assert ordered.rates[large] == pytest.approx(1 / 1849)
    assert ordered.at[large] == {"rows": 257}
    pair = RangedPair(K=256, N=256).record(x=(2048, 256), w=(256, 256), y=(2048,))
    points = (Point(0.9, {"rows": 256}), Point(0.1, {"rows": 1024}))
    drawn = Switches.of(
        Timed(pair, values={"rows": 256, "valid": 256}, points=points), profile
    )
    assert not drawn.ordered
    assert drawn.rates == {small: pytest.approx(0.09), large: pytest.approx(0.09)}


def test_one_value_varied_by_two_sets_of_variants_is_refused(device):
    """Two sets of variants over ``rows`` would each select a design for one call: refused before any build."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    profile = Profile()
    profile.add_variants(_split_at_256())
    profile.add_variants(_split_at_256())
    result = fit(
        profile, [Timed(recording, values={"rows": 256, "valid": 256})], device
    )
    assert not result.ok
    assert result.stage == "counts"
    assert "two sets of variants" in (result.why or "")


def test_candidates_split_a_bounding_value_at_powers_of_two_its_capacity_records(
    device,
):
    """``candidates`` splits ``rows`` at powers of two GEMM records, each range's entry the GEMM at its capacity.

    ``valid`` bounds no input's rows, so it is not split; nor is a value the profile
    already varies.
    """
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    found = []
    with pytest.raises(NotImplementedError, match="candidates does not generate"):
        for edit in candidates([Timed(recording)], Profile(), device):
            if isinstance(edit, AddVariants):
                found.append(edit.variants)
    assert {v.values for v in found} == {("rows",)}
    boundaries = [v.ranges[0][0][0][1] for v in found]
    assert 256 in boundaries
    assert all(b & (b - 1) == 0 and 0 < b < 2048 for b in boundaries)
    at_256 = found[boundaries.index(256)]
    assert [(r.root.cls, r.root.dims["M"]) for _, r in at_256.ranges] == [
        (GEMM, 256),
        (GEMM, 2048),
    ]
    assert at_256.ranges[1][0] == ((257, 2048),)
    varied = Profile()
    varied.add_variants(at_256)
    with pytest.raises(NotImplementedError, match="candidates does not generate"):
        assert not any(
            isinstance(e, AddVariants)
            for e in candidates([Timed(recording)], varied, device)
        )


@pytest.mark.supported_devices("npu1", "npu2")
def test_a_call_whose_points_span_two_ranges_is_bit_identical_on_each_design(device):
    """A call at 128 and at 1024 runs 128 on the 256-row design and 1024 on the 2048-row one, each bit-identical to the single bounded baseline."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    baseline = Profile()
    baseline.add(GEMM, M=2048, K=256, N=256, tile_m=64)
    tuned = Profile()
    tuned.add_variants(_split_at_256())
    points = (Point(0.5, {"rows": 128}), Point(0.5, {"rows": 1024}))
    call = Timed(recording, values={"rows": 128, "valid": 256}, points=points)
    result = check(tuned, baseline, [call], device, refinement=Refinement.EXACT)
    assert result.ok, result.why


def test_a_half_chunk_of_a_graph_reading_a_coded_weight_waits(device):
    """A graph reading a coded weight, coded as a build codes it, splits into a half chunk not yet: it waits, and is not refused."""
    recording = coded_consumer_recording_with_weight(
        rows=1,
        num_aie_columns=1,
        weight=small_integer_weight((128, 128), 0),
        num_batches=2,
    )
    recording.code_weights()
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, size="half_chunk"))
    with pytest.raises(NotImplementedError, match="a coded weight"):
        fit(profile, [Timed(recording)], device)


def test_a_malformed_range_entry_is_raised_not_refused_as_illegal(device):
    """An entry that names a step's tunable among its dims is an error in the profile, not a design illegal at its capacity."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    malformed = Entry(
        root=Member(cls=GEMM, dims={"M": 256, "K": 256, "N": 256, "tile_m": 64})
    )
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    profile = Profile()
    profile.add_variants(
        Variants(
            values=("rows",), ranges=((((0, 256),), malformed), (((257, 2048),), large))
        )
    )
    with pytest.raises(ValueError, match="dims name its tunables"):
        fit(profile, [Timed(recording)], device)


def test_ranges_that_do_not_tile_the_value_space_are_refused(device):
    """Ranges that leave a gap in the per-call value's space are refused before any build."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    small = Entry(root=Member(cls=GEMM, dims={"M": 256, "K": 256, "N": 256}))
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    gapped = Variants(
        values=("rows",),
        ranges=(
            (((0, 200),), small),
            (((400, 2048),), large),
        ),
    )
    profile = Profile()
    profile.add_variants(gapped)
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "do not tile" in (result.why or "")


def test_a_design_not_legal_at_its_ranges_capacity_is_refused(device):
    """A range's entry naming a step its capacity does not record (512 rows where at most 256 run) is refused before any build."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    wrong = Entry(root=Member(cls=GEMM, dims={"M": 512, "K": 256, "N": 256}))
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    profile = Profile()
    profile.add_variants(
        Variants(
            values=("rows",), ranges=((((0, 256),), wrong), (((257, 2048),), large))
        )
    )
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "not legal" in (result.why or "")


def test_more_variants_than_the_hosts_image_budget_is_refused(device):
    """More variant designs than ``fit``'s ``max_images`` (one more resident image apiece) is refused before any build."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    ranges = tuple(
        (
            ((lo, 2048 if lo == 1984 else lo + 63),),
            Entry(root=Member(cls=GEMM, dims={"M": 64, "K": 256, "N": 256})),
        )
        for lo in range(0, 2048, 64)
    )
    profile = Profile()
    profile.add_variants(Variants(values=("rows",), ranges=ranges))
    result = fit(profile, [Timed(recording)], device, max_images=4)
    assert not result.ok
    assert result.stage == "counts"
    assert "images at once" in (result.why or "")


def test_more_runtime_parameters_than_a_calls_scratchpad_is_refused(device):
    """More run-time parameters than a call's scratchpad holds is refused before any build."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    profile = Profile()
    for i in range(SCRATCHPAD_WORDS + 1):
        profile.add_binding(Binding(value=f"v{i}", how="runtime"))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "scratchpad holds" in (result.why or "")


def test_a_compile_time_value_that_varies_within_its_range_without_variants_is_refused(
    device,
):
    """A value bound ``compile`` that still varies within a range it is not given ``Variants`` over is refused before any build."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    profile = Profile()
    profile.add_binding(Binding(value="rows", how="compile"))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "compile time" in (result.why or "")


def test_a_runtime_parameter_in_a_pack_on_an_xclbin_is_refused(device):
    """A run-time-bound per-call parameter inside a pack (independent steps, no edges) is refused on an xclbin-per-step packaging before any build."""
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    pack = Region(
        parts=(
            Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}),
            Member(
                cls=Copy, dims={"input_buffer_size": 2048, "output_buffer_size": 2048}
            ),
        )
    )
    profile = Profile()
    profile.add_entry(Entry(root=pack))
    profile.add_binding(Binding(value="rows", how="runtime"))
    profile.add_schedule(Schedule(version=recording.version, packaging="xclbin"))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "xclbin" in (result.why or "")
