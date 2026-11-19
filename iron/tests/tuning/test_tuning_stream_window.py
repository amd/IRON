# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A stream window: a region of members linked on chip.

Every check calls the composition contract (``candidates``, ``fit``, ``check``,
``search``) before any compile, build or device use, so nothing here touches
the NPU; a test is ``@unbuilt`` while what it calls raises ``NotImplementedError`` (not built yet).
"""

from __future__ import annotations

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement, Region
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import (
    chain,
    fan_in_gate_up_mul,
    fan_out_norm_qkv,
    kv_write_then_read,
    scan_with_state_output,
    shared_input_two_reads,
    skip_edge,
    wide_mlp_window,
    window_with_outside_reader,
)
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, measure, search

DEVICE = DEVICES["npu2"]()
DEVICE_NPU1 = DEVICES["npu1"]()


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
def test_window_entry_round_trips_through_the_profile(window, tmp_path):
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
        for edit in candidates([Timed(recording)], start, DEVICE)
    )


@pytest.mark.parametrize("window", sorted(WINDOWS))
@pytest.mark.supported_devices("npu2")
def test_window_is_bit_identical_to_its_steps_run_apart(window):
    """A window's output is bit-identical to the same steps run apart, at its recorded size."""
    recording, region = WINDOWS[window]()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
def test_window_is_bit_identical_at_a_smaller_per_call_size():
    """The chain window, called at a size below the one it was recorded at, stays bit-identical to the steps apart."""
    recording, region = chain(size=128)
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu1")
def test_window_is_bit_identical_on_npu1_full_elf_and_per_step():
    """The chain window, built as a full ELF and as an xclbin per step, both bit-identical to the steps apart on npu1."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    base = Profile()
    result = check(profile, base, [Timed(recording)], DEVICE_NPU1, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.extensive
@pytest.mark.parametrize("window", sorted(WINDOWS))
@pytest.mark.supported_devices("npu2")
def test_tuner_proposes_and_keeps_a_window_on_its_own_toy(window):
    """The tuner, run on the window's toy alone, keeps what is at least as fast as the window, where the window pays."""
    recording, region = WINDOWS[window]()
    calls = [Timed(recording)]
    start = Profile()
    with_window = Profile()
    with_window.add_entry(Entry(region))
    window_ratio = measure(with_window, start, calls, DEVICE).ratio
    found = search(calls, start, DEVICE, budget_s=60.0)
    if window_ratio < 0.95:
        assert measure(found, start, calls, DEVICE).ratio < window_ratio * 1.05


def test_a_window_over_the_arrays_cores_is_refused_before_any_build():
    """A window demanding more cores than the array holds is refused by ``fit``, counts before the placer.

    At Llama decode's recorded widths this window demands 40 cores, 24
    shim-in and 8 shim-out channels, and fits only at 4 columns; this toy
    keeps the same shape of window (gate, up, SiLU, multiply) at those
    widths.
    """
    recording, region = wide_mlp_window(cols=(8, 8, 8, 8))
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "core" in (result.why or "")


@unbuilt
def test_a_window_over_the_shim_channels_is_refused_before_any_build():
    """A window whose members fit the array's cores but outrun its shim channels is refused before any build."""
    wide_recording, wide_region = fan_out_norm_qkv(columns=(8, 8, 8))
    profile = Profile()
    profile.add_entry(Entry(wide_region))
    result = fit(profile, [Timed(wide_recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "channel" in (result.why or "")


@unbuilt
def test_a_data_mover_with_no_compute_core_still_counts_shim_channels():
    """A data mover (``Copy``, no compute core) takes no core budget but is still priced on shim channels."""
    recording, members = kv_write_then_read(position=0)
    region = Region(members, ())
    profile = Profile()
    profile.add_entry(Entry(region))
    result = fit(profile, [Timed(recording)], DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "shim" in (result.why or "") or "channel" in (result.why or "")
