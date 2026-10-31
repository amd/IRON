# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Applying a profile's packings (``Profile.add_packing``) to a recording.

The steps of each packing's shapes, where it applies in the recording's version, rebuilt
at the tunables it gives them, and their designs grouped into one device configuration,
which a full ELF then configures once for every step of them in a row.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from ..declare import Profile
from ..design import OperatorDesign
from ..image.compose import Packing
from ..image.step import Fusion
from .fusion_tunables import rebuild
from .record import Recording


def apply(
    recording: Recording, profile: Profile, fused: Sequence[Fusion], dev
) -> tuple[Recording, Packing]:
    """Return ``recording`` with each step a packing entry applying in its version names (``Profile.packings_of``).

    Outside ``fused``, rebuilt at its member's tunables, and the packing grouping their
    designs, one group per entry that names two or more of them. Where several entries
    name a step's shape, the one naming most of the recording's shapes takes it, the
    earlier on a tie: the grouping found for this graph, not another model's that shares
    one of its shapes.
    """
    inside = {i for f in fused for i in f.steps}
    version = recording.version
    found = {
        i: matches
        for i, step in enumerate(recording.steps)
        if i not in inside
        and (matches := profile.packings_of(step.op.resolved(dev), version))
    }
    covered: dict[int, set[int]] = {}
    for matches in found.values():
        for index, member, _ in matches:
            covered.setdefault(index, set()).add(member)
    members: dict[int, int] = {}
    tunables: dict[int, Mapping[str, Any]] = {}
    for i, matches in found.items():
        index, _, given = max(matches, key=lambda m: (len(covered[m[0]]), -m[0]))
        members[i] = index
        if given:
            tunables[i] = given
    recording = rebuild(recording, tunables, dev)
    groups: dict[int, dict[str, None]] = {}
    for i, entry in members.items():
        name = OperatorDesign(recording.steps[i].op.resolved(dev)).name
        groups.setdefault(entry, {})[name] = None
    return recording, Packing(tuple(tuple(g) for g in groups.values() if len(g) > 1))
