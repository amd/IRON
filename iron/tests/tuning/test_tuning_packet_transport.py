# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Packet transport: a window whose streams exceed the shim channels builds by sharing them."""

from __future__ import annotations

from iron.common.declare.composition import Entry, Member, Refinement, Region
from iron.common.declare.profile import Profile
from iron.common.image.step import Edge, EdgeKind
from iron.tests.support import toys_schedule
from iron.tests.support.tools import DEVICES
from iron.tests.support.tuning import unbuilt
from iron.tune.search import check, fit

DEVICE = DEVICES["npu2"]()


def _packet_window():
    """Return a 4x2 window: a norm feeding two equal GEMVs streaming their weights at once over the shim channels."""
    norm, gate, up = toys_schedule.two_gemv_window(columns=4, channels=2)
    members = (
        Member(type(norm), {"rows": norm.rows}),
        Member(
            type(gate),
            {"M": gate.M, "K": gate.K},
            {"num_aie_columns": 4, "num_channels": 2},
        ),
        Member(
            type(up), {"M": up.M, "K": up.K}, {"num_aie_columns": 4, "num_channels": 2}
        ),
    )
    edges = (
        Edge(0, "y", 1, "B", kind=EdgeKind.STREAM),
        Edge(0, "y", 2, "B", kind=EdgeKind.STREAM),
    )
    region = Region(parts=members, edges=edges)
    recording = toys_schedule.two_gemv_window_recording("packet_window", norm, gate, up)
    return region, recording


@unbuilt
def test_the_4x2_window_builds_with_packet_transport_and_is_bit_identical():
    """The 4x2 window, built requesting packet transport on the placer's channel verdict, is bit-identical to its steps apart.

    This settles whether the shim channel limit is the compiler's or the
    array's: the budget met by sharing through packets rather than one stream
    each.
    """
    region, recording = _packet_window()
    base = Profile()
    base.add_entry(
        Entry(root=Region(parts=region.parts))
    )  # the steps apart: no shared-channel edges
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = check(profile, base, recording, DEVICE, Refinement.EXACT)
    assert result.ok, result.why


@unbuilt
def test_the_4x2_window_is_bit_identical_across_repeated_runs():
    """Repeated runs of the packet-transport window agree bit for bit with each other, not only with the reference."""
    region, recording = _packet_window()
    profile = Profile()
    profile.add_entry(Entry(root=region))
    first = check(profile, profile, recording, DEVICE, Refinement.EXACT)
    second = check(profile, profile, recording, DEVICE, Refinement.EXACT)
    assert first.ok and second.ok, (first.why, second.why)


@unbuilt
def test_the_4x2_window_does_not_hang():
    """The window fits the shim's channel budget by sharing, so static fit accepts it (no refusal, and no build to hang)."""
    region, recording = _packet_window()
    profile = Profile()
    profile.add_entry(Entry(root=region))
    result = fit(profile, recording, DEVICE)
    assert result.ok, result.why
