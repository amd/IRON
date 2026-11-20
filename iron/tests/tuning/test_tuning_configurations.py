# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Configurations: what is loaded together, and how a call switches between them."""

from __future__ import annotations

import pytest
from aie.dialects.aie import get_target_model

from iron.common.declare.composition import (
    Configuration,
    Entry,
    Member,
    Refinement,
    Region,
    Schedule,
    Switch,
)
from iron.common.declare.composition import (
    Edge as CompositionEdge,
)
from iron.common.declare.profile import Profile
from iron.common.graph.record import Recording
from iron.common.image.step import EdgeKind, HandOff
from iron.operators.relu import ReLU
from iron.operators.sigmoid import Sigmoid
from iron.operators.tanh import Tanh
from iron.tests.support import sequences, toys_schedule
from iron.tests.support.fusable import gemv_silu_mul, gemv_silu_mul_recording
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_composition import independent_regions_recording
from iron.tests.support.toys_edges import combination_toy, member
from iron.tests.support.tuning import reached_by_candidates, unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import AddEntry, candidates, check, fit, search


def _alternating_configuration(device) -> tuple[Configuration, object]:
    size = 2048
    members = tuple(
        Member(cls, {"size": size}, {"num_aie_columns": device.cols})
        for cls in (ReLU, Tanh, ReLU, Tanh, ReLU, Tanh, ReLU, Tanh)
    )
    configuration = Configuration(parts=members)
    recording = toys_schedule.Alternating(device.cols).record(x=(size,))
    return configuration, recording


def _independent_pair_recording(name: str, gemv, mul) -> Recording:
    """Return ``gemv`` then ``mul`` on other inputs: neither reads the other."""
    return Recording.of_steps(
        name,
        sequences.steps((gemv, "A", "B", "y"), (mul, "a", "b", "z")),
        ["A", "B", "a", "b"],
        ["y", "z"],
    )


def _wide_configuration(device) -> tuple[Configuration, object]:
    size = 8192
    members = tuple(
        Member(cls, {"size": size}, {"num_aie_columns": device.cols, "num_channels": 2})
        for cls in (ReLU, Tanh, Sigmoid, ReLU, Tanh, Sigmoid)
    )
    configuration = Configuration(parts=members)
    recording = toys_schedule.Wide(device.cols).record(x=(size,))
    return configuration, recording


def test_membership_as_one_design_round_trips_and_is_proposed(tmp_path, device):
    """A single design's membership round-trips through a profile and is a candidate."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
    entry = Entry(root=Configuration(parts=(member(gemv),)))
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "membership_single.json")
    loaded = Profile.load(tmp_path / "membership_single.json")
    assert loaded.entries() == [entry]
    recording = gemv_silu_mul_recording("config_single", gemv, silu, mul)
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, device)
    )


def test_region_as_one_packing_piece_round_trips_and_is_proposed(tmp_path, device):
    """A region nested as one piece of a configuration's packing round-trips and is a candidate."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
    region = Region(
        parts=(member(gemv), member(silu)),
        edges=(CompositionEdge(0, "C", 1, "x", kind=EdgeKind.STREAM),),
    )
    configuration = Configuration(parts=(region, member(mul)))
    entry = Entry(root=configuration)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "region_in_configuration.json")
    loaded = Profile.load(tmp_path / "region_in_configuration.json")
    assert loaded.entries() == [entry]
    recording = gemv_silu_mul_recording("config_region_piece", gemv, silu, mul)
    calls = [Timed(recording)]
    reached = reached_by_candidates(region, calls, device)
    assert any(
        isinstance(edit, AddEntry) and edit.entry == entry
        for edit in candidates(calls, reached, device)
    )


def test_several_regions_in_one_packing_round_trip_and_are_proposed(tmp_path, device):
    """Several regions sharing one configuration (two independent windows) round-trip and are a candidate.

    Regions the search holds: the first window's, reached by candidates, and
    the last step's own at its recorded tunables.
    """
    gemv1, silu1, mul1 = gemv_silu_mul(M=256, cols=4, tile=64)
    region1 = Region(
        parts=(member(gemv1), member(silu1)),
        edges=(CompositionEdge(0, "C", 1, "x", kind=EdgeKind.STREAM),),
    )
    recording = gemv_silu_mul_recording("config_several_regions", gemv1, silu1, mul1)
    calls = [Timed(recording)]
    start = reached_by_candidates(region1, calls, device)
    own = next(
        edit
        for edit in candidates(calls, start, device)
        if isinstance(edit, AddEntry)
        and isinstance(edit.entry.root, Region)
        and len(edit.entry.root.parts) == 1
        and edit.entry.root.parts[0].cls is type(mul1)
    )
    start = own.apply(start)
    configuration = Configuration(parts=(region1, own.entry.root))
    entry = Entry(root=configuration)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "several_regions.json")
    loaded = Profile.load(tmp_path / "several_regions.json")
    assert loaded.entries() == [entry]
    assert any(
        isinstance(edit, AddEntry) and edit.entry == entry
        for edit in candidates(calls, start, device)
    )


@pytest.mark.supported_devices("npu2")
def test_several_regions_in_one_configuration_are_bit_identical(device):
    """Two regions, each a GEMV streamed into its SiLU, loaded together in one configuration and run in turn.

    Bit-identical to every step in a configuration of its own.
    """
    recording = independent_regions_recording("config_two_regions")
    ops = [step.op for step in recording.steps]
    regions = tuple(
        Region(
            parts=(member(gemv), member(silu)),
            edges=(CompositionEdge(0, "C", 1, "x", kind=EdgeKind.STREAM),),
        )
        for gemv, silu in (ops[:2], ops[2:])
    )
    profile = Profile()
    profile.add_entry(Entry(root=Configuration(parts=regions)))
    base = Profile()
    for op in ops:
        base.add_entry(Entry(root=Configuration(parts=(member(op),))))
    assert fit(profile, [Timed(recording)], device).ok
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
def test_nesting_a_region_inside_a_region_round_trips_and_is_proposed(tmp_path, device):
    """A region nested inside a region (the Alternating toy's two halves grouped, then wrapped) round-trips and is a candidate."""
    size = 2048
    first = ReLU(size=size, num_aie_columns=device.cols)
    middle = Tanh(size=size, num_aie_columns=device.cols)
    last = ReLU(size=size, num_aie_columns=device.cols)
    recording = Recording.of_steps(
        "config_nested",
        sequences.steps((first, "x", "a"), (middle, "a", "b"), (last, "b", "y")),
        ["x"],
        ["y"],
    )
    inner = Region(
        parts=(
            Member(ReLU, {"size": size}, {"num_aie_columns": device.cols}),
            Member(Tanh, {"size": size}, {"num_aie_columns": device.cols}),
        )
    )
    outer = Region(
        parts=(inner, Member(ReLU, {"size": size}, {"num_aie_columns": device.cols}))
    )
    entry = Entry(root=outer)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "nested_region.json")
    loaded = Profile.load(tmp_path / "nested_region.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, device)
    )


@pytest.mark.supported_devices("npu1", "npu2")
def test_concurrency_one_after_another_is_bit_identical(device):
    """The Alternating toy's eight steps, loaded one after another, are bit-identical to every step in a configuration of its own."""
    configuration, recording = _alternating_configuration(device)
    profile = Profile()
    profile.add_entry(Entry(root=configuration))
    base = Profile()
    for part in configuration.parts:
        base.add_entry(Entry(root=Configuration(parts=(part,))))
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_concurrency_at_once_with_no_shared_data_is_bit_identical(device):
    """Independent steps sharing a configuration concurrently (``Configuration.concurrent``) are bit-identical to each loaded alone.

    The two chains' projections share no data: neither reaches the other.
    """
    recording = independent_regions_recording("config_concurrent")
    members = tuple(member(recording.steps[s].op) for s in (0, 2))
    configuration = Configuration(parts=members, concurrent=1)
    profile = Profile()
    profile.add_entry(Entry(root=configuration))
    base = Profile()
    for part in members:
        base.add_entry(Entry(root=Configuration(parts=(part,))))
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_concurrency_at_once_of_consecutive_steps_is_bit_identical(device):
    """Two configurations concurrent under one id run at once as one pack, bit-identical to each loaded alone.

    A step each, the two consecutive and independent.
    """
    gemv, _, mul = gemv_silu_mul(M=256, cols=2, tile=64)
    recording = _independent_pair_recording("config_at_once_consecutive", gemv, mul)
    profile = Profile()
    base = Profile()
    for op in (gemv, mul):
        profile.add_entry(Entry(root=Configuration(parts=(member(op),), concurrent=1)))
        base.add_entry(Entry(root=Configuration(parts=(member(op),))))
    assert fit(profile, [Timed(recording)], device).ok
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_disjoint_columns_concurrency_is_bit_identical(device):
    """Two designs on disjoint columns at once (``Configuration.concurrent`` with a ``columns`` width each) are bit-identical to each alone."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=2, tile=64)
    left = Configuration(
        parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}),), columns=2, concurrent=1
    )
    right = Configuration(
        parts=(Member(type(mul), {"size": mul.size}),), columns=2, concurrent=1
    )
    profile = Profile()
    profile.add_entry(Entry(root=left))
    profile.add_entry(Entry(root=right))
    base = Profile()
    base.add_entry(
        Entry(
            root=Configuration(parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}),))
        )
    )
    base.add_entry(
        Entry(root=Configuration(parts=(Member(type(mul), {"size": mul.size}),)))
    )
    recording = _independent_pair_recording("config_disjoint_columns", gemv, mul)
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_width_partial_columns_is_bit_identical(device):
    """``Configuration.columns`` (a partial width) is bit-identical to the full-width configuration."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
    full = Configuration(parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}),))
    narrow = Configuration(
        parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}),), columns=2
    )
    base = Profile()
    base.add_entry(Entry(root=full))
    profile = Profile()
    profile.add_entry(Entry(root=narrow))
    recording = gemv_silu_mul_recording("config_width", gemv, silu, mul)
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@unbuilt
@pytest.mark.supported_devices("npu1", "npu2")
def test_switch_kinds_are_bit_identical_and_priced_per_core(device):
    """Every ``Switch`` kind (RELOAD, CHANGED_CORES, OVERLAPPED) is bit-identical; (c) the tuner prices the switch per core and keeps what pays."""
    configuration, recording = _alternating_configuration(device)
    base = Profile()
    base.add_entry(
        Entry(root=Configuration(parts=configuration.parts, switch=Switch.RELOAD))
    )
    for switch in (Switch.CHANGED_CORES, Switch.OVERLAPPED):
        profile = Profile()
        profile.add_entry(
            Entry(root=Configuration(parts=configuration.parts, switch=switch))
        )
        result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
        assert result.ok, result.why
    found = search([Timed(recording)], base, device, budget_s=60.0)
    assert any(
        isinstance(e.root, Configuration) and e.root.switch is not None
        for e in found.entries()
    )


@pytest.mark.supported_devices("npu1", "npu2")
def test_teardown_true_and_false_are_bit_identical(device):
    """``Configuration.teardown`` (True or False) is bit-identical to the build's own default."""
    configuration, recording = _alternating_configuration(device)
    base = Profile()
    base.add_entry(Entry(root=configuration))
    for teardown in (True, False):
        profile = Profile()
        profile.add_entry(
            Entry(root=Configuration(parts=configuration.parts, teardown=teardown))
        )
        result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
        assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu1", "npu2")
def test_residency_keeps_a_buffer_on_chip_and_is_bit_identical(device):
    """``Configuration.resident`` (weights kept on chip into the next configuration) is bit-identical to reloading them."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
    base = Profile()
    base.add_entry(
        Entry(
            root=Configuration(parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}),))
        )
    )
    base.add_entry(
        Entry(root=Configuration(parts=(Member(type(mul), {"size": mul.size}),)))
    )
    profile = Profile()
    profile.add_entry(
        Entry(
            root=Configuration(
                parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}),), resident=("A",)
            )
        )
    )
    profile.add_entry(
        Entry(root=Configuration(parts=(Member(type(mul), {"size": mul.size}),)))
    )
    recording = gemv_silu_mul_recording("config_resident", gemv, silu, mul)
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_packaging_full_elf_and_xclbin_per_step_are_bit_identical(device):
    """A configuration built as a full ELF and as an xclbin per step are bit-identical."""
    configuration, recording = _alternating_configuration(device)
    full_elf = Profile()
    full_elf.add_entry(Entry(root=configuration))
    full_elf.add_schedule(Schedule(version=recording.version, packaging="full_elf"))
    xclbin = Profile()
    xclbin.add_entry(Entry(root=configuration))
    xclbin.add_schedule(Schedule(version=recording.version, packaging="xclbin"))
    result = check(xclbin, full_elf, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


# npu1 builds GEMM on an array narrower than the device, which a
# configuration beside another operator's does not take.
_CONFIGURATION_PAYS = [
    pytest.param(
        name,
        id=f"device_{name}",
        marks=(
            ()
            if name == "npu2"
            else pytest.mark.xfail(
                strict=True,
                raises=AssertionError,
                reason="candidates does not propose configurations yet",
            )
        ),
    )
    for name in sorted(DEVICES)
]

# The seconds the search takes on npu2 to price the configuration that pays
# (326 s: a configuration before it hangs the placer to its 300 s limit),
# with margin.
_CONFIGURATION_BUDGET_S = 600.0


@pytest.mark.extensive
@pytest.mark.parametrize("device", _CONFIGURATION_PAYS, indirect=True)
@pytest.mark.supported_devices("npu1", "npu2")
def test_tuner_keeps_the_configuration_that_pays(device):
    """The tuner, on the pre-norm MLP toy alone, keeps the configuration (narrowed to co-reside) that pays.

    Its two projections share one GEMM array, so its four arrays loaded
    together serve all five steps, where a region holds the GEMM's cores
    once a projection. On the Wide toy a one-column stream region beats
    every configuration, so the search rightly keeps none there.
    """
    recording = toys_schedule.PreNormMLP(512, 1024, device.cols).record(
        x=(256, 512), up=(512, 1024), down=(1024, 512)
    )
    found = search(
        [Timed(recording)], Profile(), device, budget_s=_CONFIGURATION_BUDGET_S
    )
    assert any(isinstance(e.root, Configuration) for e in found.entries())


def test_the_designs_saving_most_switches_are_proposed_first_narrowed_to_co_reside(
    device,
):
    """On the Wide toy, its three designs loaded together save the most switches: the first configuration proposed.

    Narrowed until their cores fit the array, which ``fit`` accepts.
    """
    _, recording = _wide_configuration(device)
    calls = [Timed(recording)]
    first = next(
        edit
        for edit in candidates(calls, Profile(), device)
        if isinstance(edit, AddEntry) and isinstance(edit.entry.root, Configuration)
    )
    parts = first.entry.root.parts
    assert [m.cls for m in parts] == [ReLU, Tanh, Sigmoid]
    assert all(m.tunables["num_aie_columns"] < device.cols for m in parts)
    assert fit(first.apply(Profile()), calls, device).ok


def test_each_array_of_one_shape_is_proposed_by_its_shape(device):
    """The through-memory toy's copies share one shape on arrays of other widths: each configuration proposed names that shape, and fits or is refused."""
    _, recording, _, _ = combination_toy(
        device, HandOff.SPLIT, "through_memory", "memtile", "min", "same", "recorded"
    )
    calls = [Timed(recording)]
    proposed = []
    try:
        for edit in candidates(calls, Profile(), device):
            if isinstance(edit, AddEntry) and isinstance(
                edit.entry.root, Configuration
            ):
                proposed.append(edit)
    except NotImplementedError:
        pass
    assert proposed
    for edit in proposed:
        assert edit.entry.root.parts == (member(recording.steps[0].op),)
        fit(edit.apply(Profile()), calls, device)


def test_a_configuration_over_the_arrays_cores_is_refused(device):
    """The Wide toy's six cores a column, over the array's, are refused by counts before any build."""
    configuration, recording = _wide_configuration(device)
    # Three distinct arrays (ReLU, Tanh, Sigmoid), each two cores a column
    # (two channels) at every column: more than the array's cores.
    model = get_target_model(device.resolve())
    cores = model.columns() * sum(
        model.is_core_tile(0, row) for row in range(model.rows())
    )
    assert 3 * device.cols * 2 > cores
    profile = Profile()
    profile.add_entry(Entry(root=configuration))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "cores" in (result.why or "")


def test_members_running_at_once_sharing_written_data_is_refused(device):
    """Two members of one configuration sharing written data while run at once (``Configuration.concurrent``) is refused before any build."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=2, tile=64)
    members = (
        Member(type(gemv), {"M": gemv.M, "K": gemv.K}),
        Member(type(silu), {"size": silu.size}),
    )
    # An edge between concurrent members: they are not independent, so
    # running them "at once" with no edge (PACK's rule) is a hazard.
    configuration = Configuration(parts=members, concurrent=1)
    recording = gemv_silu_mul_recording("config_shared_concurrent", gemv, silu, mul)
    profile = Profile()
    profile.add_entry(Entry(root=configuration))
    profile.add_entry(
        Entry(
            root=Region(
                parts=members,
                edges=(CompositionEdge(0, "C", 1, "x", kind=EdgeKind.STAGED),),
            )
        )
    )
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "independent" in (result.why or "") or "shared" in (result.why or "")


def test_a_member_given_more_columns_than_its_configuration_is_refused(device):
    """A configuration at a partial width narrows its members to fit; one given a wider width itself is refused by counts, before any build."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
    profile = Profile()
    profile.add_entry(
        Entry(
            root=Configuration(
                parts=(
                    Member(
                        type(gemv), {"M": gemv.M, "K": gemv.K}, {"num_aie_columns": 4}
                    ),
                ),
                columns=2,
            )
        )
    )
    recording = gemv_silu_mul_recording("config_member_too_wide", gemv, silu, mul)
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "columns" in (result.why or "")


def test_residency_across_a_teardown_is_refused(device):
    """A buffer named resident into a configuration torn down before it is refused before any build."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
    profile = Profile()
    profile.add_entry(
        Entry(
            root=Configuration(
                parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}),),
                teardown=True,
                resident=("A",),
            )
        )
    )
    profile.add_entry(
        Entry(root=Configuration(parts=(Member(type(mul), {"size": mul.size}),)))
    )
    recording = gemv_silu_mul_recording("config_resident_teardown", gemv, silu, mul)
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "teardown" in (result.why or "")


def test_overlapping_columns_at_once_is_refused(device):
    """Two configurations claiming overlapping columns while concurrent is refused before any build.

    Each claims three quarters of the array's columns, so the two cannot be
    disjoint, while each member fits its own claim.
    """
    gemv, silu, mul = gemv_silu_mul(M=256, cols=device.cols // 2, tile=64)
    claimed = device.cols * 3 // 4
    left = Configuration(
        parts=(Member(type(gemv), {"M": gemv.M, "K": gemv.K}),),
        columns=claimed,
        concurrent=1,
    )
    right = Configuration(
        parts=(Member(type(mul), {"size": mul.size}),), columns=claimed, concurrent=1
    )
    recording = _independent_pair_recording("config_overlapping_columns", gemv, mul)
    profile = Profile()
    profile.add_entry(Entry(root=left))
    profile.add_entry(Entry(root=right))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "placer"
    assert "column" in (result.why or "") or "disjoint" in (result.why or "")


def test_phased_or_teardown_on_an_xclbin_is_refused(device):
    """A phased region, or a configuration's teardown, named on an xclbin-per-step packaging is refused before any build."""
    gemv, silu, mul = gemv_silu_mul(M=256, cols=4, tile=64)
    region = Region(
        parts=(
            Member(type(gemv), {"M": gemv.M, "K": gemv.K}),
            Member(type(silu), {"size": silu.size}),
        ),
        edges=(CompositionEdge(0, "C", 1, "x", kind=EdgeKind.STAGED),),
        phases=(1,),
    )
    recording = gemv_silu_mul_recording("config_phased_xclbin", gemv, silu, mul)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    profile.add_schedule(Schedule(version=recording.version, packaging="xclbin"))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "analysis"
    assert "xclbin" in (result.why or "")
