# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Transformation tests for scope and variants, which design applies where and when."""

import pytest

import iron
from iron.common.declare import Profile
from iron.common.declare.composition import (
    Binding,
    Entry,
    Member,
    Refinement,
    Region,
    Schedule,
    Scope,
    Variants,
)
from iron.common.graph.record import Recording
from iron.common.image.packaging import SCRATCHPAD_WORDS
from iron.common.image.step import BufferRef, SequenceStep
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemm import GEMM
from iron.operators.gemv import GEMV
from iron.tests.support.toys_settings import RangedPair, small_integer_weight
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, measure, search

pytestmark = pytest.mark.usefixtures("device")


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
    found = list(candidates([Timed(recording)], loaded, device))
    assert any(e.apply(Profile()).variants() == [variants] for e in found)


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
@unbuilt
@pytest.mark.supported_devices("npu1", "npu2")
def test_a_boundary_is_kept_only_where_its_saving_beats_a_switch_and_one_more_design(
    device,
):
    """The tuner keeps a boundary only where the calls it serves gain over the single bounded design plus a switch and a compile.

    The split is sized so that its small side is clearly faster than the single design
    bounded at the full 2048 (``measure``'s ratio under 0.95), so ``search`` must keep it.
    """
    g = RangedPair(K=256, N=256)
    recording = g.record(x=(2048, 256), w=(256, 256), y=(2048,))
    calls = [Timed(recording)]
    start = Profile()
    small = Entry(root=Member(cls=GEMM, dims={"M": 256, "K": 256, "N": 256}))
    large = Entry(root=Member(cls=GEMM, dims={"M": 2048, "K": 256, "N": 256}))
    variants = Variants(
        values=("rows",), ranges=((((0, 256),), small), (((257, 2048),), large))
    )
    with_entry = Profile()
    with_entry.add_variants(variants)
    ratio = measure(with_entry, start, calls, device).ratio
    assert ratio < 0.95
    tuned = search(calls, start, device, budget_s=5.0)
    assert variants in tuned.variants()


@pytest.mark.parametrize("read_first", [True, False])
def test_an_output_written_in_parts_and_read_before_its_last_write_breaks_a_merge(
    device, read_first
):
    """A returned output written in halves outlasts the call where a step reads the second half before writing it.

    Each call then reads what the call before left there, so merging calls is refused
    before any build. Read only after both halves are written, it is the host's after
    each call, and the merge waits on what is not built rather than being refused.
    """
    add = ElementwiseAdd(size=256, tile_size=128, num_aie_columns=1)
    first, second = BufferRef("out", 0, 512), BufferRef("out", 512, 512)
    writes = [
        SequenceStep(add, (BufferRef("x"), BufferRef("x"), first)),
        SequenceStep(add, (BufferRef("x"), BufferRef("x"), second)),
    ]
    reads = SequenceStep(add, (BufferRef("x"), second, BufferRef("t")))
    steps = [writes[0], reads, writes[1]] if read_first else [*writes, reads]
    recording = Recording.of_steps(
        "halves", steps, ["x"], ["out", "t"], pinned={"out": 1024}
    )
    profile = Profile()
    profile.add_schedule(Schedule(version=recording.version, size="merged_2x"))
    if not read_first:
        with pytest.raises(NotImplementedError, match="part of out"):
            fit(profile, [Timed(recording)], device)
        return
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "breaks a dependence" in (result.why or "")


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
