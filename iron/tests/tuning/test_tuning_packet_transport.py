# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Packet transport: a window whose streams exceed the shim channels builds by sharing them."""

from __future__ import annotations

import pytest

from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.common.declare.profile import Profile
from iron.common.image.step import Edge, EdgeKind
from iron.tests.support import toys_schedule
from iron.tune.autotune import Timed
from iron.tune.search import check, fit


def _packet_window(device):
    """Return a norm feeding two equal GEMVs at half the array's columns, two channels each (npu2's 4x2 window).

    Their weights and the norm's input want one stream more than the shim
    has channels.
    """
    columns = device.cols // 2
    norm, gate, up = toys_schedule.two_gemv_window(columns=columns, channels=2)
    widths = {"num_aie_columns": columns, "num_channels": 2}
    members = (
        Member(type(norm), {"rows": norm.rows}),
        Member(type(gate), {"M": gate.M, "K": gate.K}, widths),
        Member(type(up), {"M": up.M, "K": up.K}, widths),
    )
    edges = (
        Edge(0, "y", 1, "B", kind=EdgeKind.STREAM),
        Edge(0, "y", 2, "B", kind=EdgeKind.STREAM),
    )
    region = Region(parts=members, edges=edges)
    recording = toys_schedule.two_gemv_window_recording("packet_window", norm, gate, up)
    return region, recording


@pytest.mark.supported_devices("npu2")
def test_the_window_past_the_shim_builds_with_packet_transport_and_is_bit_identical(
    device,
):
    """The window past the shim, built requesting packet transport on the placer's channel verdict, is bit-identical to its steps apart.

    This settles whether the shim channel limit is the compiler's or the
    array's: the budget met by sharing through packets rather than one stream
    each.
    """
    region, recording = _packet_window(device)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, Profile(), [Timed(recording)], device, Refinement.EXACT)
    assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
def test_the_window_past_the_shim_is_bit_identical_across_repeated_runs(device):
    """Repeated runs of the packet-transport window agree bit for bit with each other, not only with the reference."""
    region, recording = _packet_window(device)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    first = check(profile, profile, [Timed(recording)], device, Refinement.EXACT)
    second = check(profile, profile, [Timed(recording)], device, Refinement.EXACT)
    assert first.ok and second.ok, (first.why, second.why)


@pytest.mark.supported_devices("npu2")
def test_the_window_past_the_shim_does_not_hang(device):
    """The window fits the shim's channel budget by sharing, so static fit accepts it (no refusal, and no build to hang)."""
    region, recording = _packet_window(device)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, [Timed(recording)], device)
    assert result.ok, result.why
