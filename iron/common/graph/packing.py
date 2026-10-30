# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Applying a profile's packings (``Profile.add_packing``) to a recording:
the steps of each packing's shapes, where it applies in the recording's
version, rebuilt at the tunables it gives them, and their designs grouped
into one device configuration, which a full ELF then configures once for
every step of them in a row.
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
    """``recording`` with each step a packing entry applying in its version
    names (``Profile.packing_of``), outside ``fused``, rebuilt at its
    member's tunables, and the packing grouping their designs, one group per
    entry that names two or more of them.
    """
    inside = {i for f in fused for i in f.steps}
    members: dict[int, int] = {}
    tunables: dict[int, Mapping[str, Any]] = {}
    version = recording.version
    for i, step in enumerate(recording.steps):
        if i in inside:
            continue
        found = profile.packing_of(step.op.resolved(dev), version)
        if found is None:
            continue
        members[i], given = found
        if given:
            tunables[i] = given
    recording = rebuild(recording, tunables, dev)
    groups: dict[int, dict[str, None]] = {}
    for i, entry in members.items():
        name = OperatorDesign(recording.steps[i].op.resolved(dev)).name
        groups.setdefault(entry, {})[name] = None
    return recording, Packing(tuple(tuple(g) for g in groups.values() if len(g) > 1))
