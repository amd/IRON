# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A stream window: a region of members linked on chip.

Every check calls the composition contract (``candidates``, ``fit``, ``check``,
``search``) before any compile, build or device use, so nothing here touches
the NPU; a test is ``@unbuilt`` while what it calls raises ``NotImplementedError`` (not built yet).
"""

from __future__ import annotations

import dataclasses

import pytest
from aie.dialects.aie import WireBundle, get_target_model

from iron.common.declare import Profile
from iron.common.declare.composition import Configuration, Entry, Refinement, Region
from iron.common.design import OperatorDesign
from iron.common.graph.record import Recording
from iron.common.graph.sdf import Derivation
from iron.common.image.compose import SHIM_SHORT, fits, transported
from iron.common.image.step import Edge, Fusion, FusionKind
from iron.operators.copy import Copy
from iron.tests.support import sequences
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import (
    chain,
    fan_in_gate_up_mul,
    fan_out_norm_projections,
    fan_out_norm_qkv,
    member,
    scan_with_state_output,
    shared_input_two_reads,
    skip_edge,
    wide_mlp_window,
    window_with_outside_reader,
)
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import BUILT_PLACERS, candidates, check, fit, measure, search


def _outside_reader_window():
    recording, members, forward = window_with_outside_reader()
    edges = sorted(
        forward + (skip_edge(),),
        key=lambda e: (e.producer, e.consumer, e.output, e.input),
    )
    return recording, Region(members, tuple(edges))


WINDOWS = {
    "chain": chain,
    "fan_in": fan_in_gate_up_mul,
    "fan_out": fan_out_norm_qkv,
    "shared_input_two_reads": shared_input_two_reads,
    "several_outputs": scan_with_state_output,
    "outside_reader_and_final_output": _outside_reader_window,
}


@pytest.mark.parametrize("window", sorted(WINDOWS))
def test_window_entry_round_trips_through_the_profile(window, tmp_path, device):
    """A region of stream edges round-trips through the profile, and ``candidates`` proposes a window over its chain."""
    recording, region = WINDOWS[window]()
    entry = Entry(region)
    profile = Profile()
    profile.add_entry(entry)
    profile.save(tmp_path / "profile.json")
    loaded = Profile.load(tmp_path / "profile.json")
    assert loaded.entries() == [entry]
    start = Profile()
    assert any(
        entry in edit.apply(start).entries()
        for edit in candidates([Timed(recording)], start, device)
    )


# SelectiveScan's lanes write ``y`` by head, the multiply reads it by row: a
# round read off a memtile in the multiply's order, built on npu2; npu1's
# waits on host 203.
BUILT_WINDOWS = [
    pytest.param(
        name,
        w,
        id=f"device_{name}-window_{w}",
        marks=unbuilt if w == "several_outputs" and name == "npu1" else (),
    )
    for name in sorted(DEVICES)
    for w in sorted(WINDOWS)
]


@pytest.mark.parametrize(("device", "window"), BUILT_WINDOWS, indirect=["device"])
@pytest.mark.supported_devices("npu1", "npu2")
def test_window_is_bit_identical_to_its_steps_run_apart(window, device):
    """A window's output is bit-identical to the same steps run apart, at its recorded size."""
    recording, region = WINDOWS[window]()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu1", "npu2")
def test_window_is_bit_identical_at_a_smaller_per_call_size(device):
    """The chain window, called at a size below the one it was recorded at, stays bit-identical to the steps apart."""
    recording, region = chain(size=128)
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
# npu1's full ELF is the open packaging; npu2 runs both in test_fusion_staged.py.
@pytest.mark.supported_devices("npu1")
def test_window_is_bit_identical_on_npu1_full_elf_and_per_step(device):
    """The chain window, built as a full ELF and as an xclbin per step, both bit-identical to the steps apart on npu1."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.parametrize(("device", "window"), BUILT_WINDOWS, indirect=["device"])
@pytest.mark.supported_devices("npu1", "npu2")
def test_tuner_proposes_and_keeps_a_window_on_its_own_toy(window, device):
    """The tuner, run on the window's toy alone, keeps what is at least as fast as the window, where the window pays."""
    recording, region = WINDOWS[window]()
    calls = [Timed(recording)]
    start = Profile()
    with_window = Profile()
    with_window.add_entry(Entry(region))
    window_ratio = measure(with_window, start, calls, device).ratio
    found = search(calls, start, device, budget_s=60.0)
    if window_ratio < 0.95:
        assert measure(found, with_window, calls, device).ratio < 1.05


def test_a_window_over_the_arrays_cores_is_refused_before_any_build(device):
    """A window demanding more cores than the array holds is refused by ``fit``, counts before the placer.

    At Llama decode's recorded widths this window demands 40 cores, 24
    shim-in and 8 shim-out channels, and fits npu2 only at 4 columns; this
    toy keeps the same shape of window (gate, up, SiLU, multiply), each
    member at every column of the device.
    """
    recording, region = wide_mlp_window(device)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], device)
    assert not result.ok
    assert result.stage == "counts"
    assert "core" in (result.why or "")


def test_a_window_whose_drains_outrun_the_shim_joins_them_in_memtiles(device):
    """The norm fanned into Q, K and V at the array's full width drains more lanes than the shim receives, its fills shared by packets or not.

    Its build joins each run of a projection's lanes in a memtile into one
    host lane (``Fusion.drains``), and so it fits.
    """
    recording, region = fan_out_norm_qkv(columns=(device.cols,) * 3)
    designs = [OperatorDesign(step.op.resolved()) for step in recording.steps]
    fusion = Fusion(
        FusionKind.STREAM, (0, 1, 2, 3), tuple(Edge(0, "y", c, "B") for c in (1, 2, 3))
    )
    members = {str(j): d for j, d in enumerate(designs)}
    for packets in (False, True):
        unjoined = dataclasses.replace(fusion, packets=packets, drains=1)
        assert SHIM_SHORT in (fits(members, fusion=unjoined) or "")
    assert transported(fusion, designs).drains > 1
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], device)
    assert result.ok, result.why


def test_a_window_draining_more_outputs_than_the_shim_receives_is_refused(device):
    """A norm fanned into one more one-column projection than the shim has receiving channels is refused by the placer, before any build.

    Each projection drains an output of its own, and a drain join joins only
    one output's lanes, so no transport fits it under any placer the build
    takes.
    """
    model = get_target_model(device.resolve())
    row = next(r for r in range(model.rows()) if model.is_shim_noc_tile(0, r))
    receives = sum(
        model.get_num_dest_shim_mux_connections(c, row, WireBundle.DMA)
        for c in range(model.columns())
        if model.is_shim_noc_tile(c, row)
    )
    recording, region = fan_out_norm_projections(receives + 1)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], device, placements=tuple(BUILT_PLACERS))
    assert not result.ok
    assert result.stage == "placer"
    assert "ShimNOCTile" in (result.why or "")


@pytest.mark.supported_devices("npu2")
def test_a_window_whose_drains_outrun_the_shim_is_bit_identical(device):
    """The full-width norm -> Q, K, V window, its drains joined in memtiles, is bit-identical to its steps run apart."""
    recording, region = fan_out_norm_qkv(columns=(device.cols,) * 3)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


def test_a_data_mover_with_no_compute_core_still_counts_shim_channels(device):
    """A data mover (``Copy``, no compute core) takes no core budget but is still priced on shim channels.

    One more one-channel copy than the shim has receiving channels, all run
    at once: the copies record no core, so the counts pass them, but each
    drains an output of its own, which neither packets (only a sending
    channel is shared) nor a drain join (one output's lanes) shares, so the
    placer a pack's build takes refuses them before any build. Run one after
    another, they share the channels over time and fit.
    """
    model = get_target_model(device.resolve())
    row = next(r for r in range(model.rows()) if model.is_shim_noc_tile(0, r))
    receives = sum(
        model.get_num_dest_shim_mux_connections(c, row, WireBundle.DMA)
        for c in range(model.columns())
        if model.is_shim_noc_tile(c, row)
    )
    copies = [Copy(input_buffer_size=1024, num_channels=1) for _ in range(receives + 1)]
    recording = Recording.of_steps(
        "copies_past_the_shim",
        sequences.steps(*((c, f"x{i}", f"y{i}") for i, c in enumerate(copies))),
        [f"x{i}" for i in range(len(copies))],
        [f"y{i}" for i in range(len(copies))],
    )
    parts = tuple(member(c) for c in copies)
    derivation = Derivation(Region(parts), recording, device)
    assert not any(recorded.cores for _, recorded in derivation.recorded)
    calls = [Timed(recording)]
    one_after_another = Profile()
    one_after_another.add_entry(Entry(Configuration(parts=parts)))
    assert fit(one_after_another, calls, device).ok
    at_once = Profile()
    at_once.add_entry(Entry(Configuration(parts=parts, concurrent=1)))
    result = fit(at_once, calls, device, placements=("sequential",))
    assert not result.ok
    assert result.stage == "placer"
    assert "ShimNOCTile" in (result.why or "")
