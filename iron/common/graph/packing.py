# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Applying a profile's packings (``Profile.add_packing``) to a recording.

The steps of each packing's shapes, where it applies in the recording's version, rebuilt
at the tunables it gives them, and their designs grouped into one device configuration,
which a full ELF then configures once for every step of them in a row, and an xclbin
dispatches once (``merges``).
"""

from __future__ import annotations

import logging
from collections.abc import Mapping, Sequence
from typing import Any

from ..declare import Profile
from ..design import OperatorDesign
from ..image.compose import ANNEALED, Packing, fits
from ..image.step import Fusion, FusionKind
from .fusion_tunables import rebuild
from .record import Recording

logger = logging.getLogger(__name__)

# Each packed group's placer and the diagnostic where none routes it, by its
# designs' identities.
_placed: dict[tuple[str, ...], tuple[str | None, str | None]] = {}

#: Host buffers one xclbin kernel takes at most (aiecc's ``kMaxHostBOs``).
HOST_BUFFERS = 16


def apply(
    recording: Recording, profile: Profile, fused: Sequence[Fusion], dev
) -> tuple[Recording, Packing]:
    """Return ``recording`` with each step a packing entry applying in its version names (``Profile.packings_of``).

    Outside ``fused``, rebuilt at its member's tunables, and the packing grouping their
    designs, one group per entry that names two or more of them. Where several entries
    name a step's shape, the one naming most of the recording's shapes takes it, the
    earlier on a tie: the grouping found for this graph, not another model's that shares
    one of its shapes. A group the default placer cannot route is placed by the
    annealing one where that routes it (``Packing.annealed``); one neither routes (an
    operator's mapping changed since the profile was tuned) is not packed, with a
    warning naming why.
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
    groups: dict[int, dict[str, OperatorDesign]] = {}
    for i, entry in members.items():
        design = OperatorDesign(recording.steps[i].op.resolved(dev))
        groups.setdefault(entry, {})[design.name] = design
    packed, annealed = [], set()
    for entry, group in groups.items():
        if len(group) < 2:
            continue
        key = tuple(d.identity for d in group.values())
        if key not in _placed:
            refused = fits(group)
            if refused is None:
                _placed[key] = (None, None)
            elif fits(group, placer=ANNEALED) is None:
                _placed[key] = (ANNEALED, None)
            else:
                _placed[key] = (None, refused)
        placer, refused = _placed[key]
        if refused is not None:
            logger.warning(
                "%s: packing %d (%s) does not place, so it is not packed: %s",
                recording.name,
                entry,
                ", ".join(group),
                refused,
            )
            continue
        packed.append(tuple(group))
        if placer == ANNEALED:
            annealed.update(group)
    return recording, Packing(tuple(packed), tuple(sorted(annealed)))


def merges(
    recording: Recording, fused: Sequence[Fusion], packing: Packing, dev
) -> tuple[Fusion, ...]:
    """Return each run of two or more consecutive steps outside ``fused`` whose designs ``packing`` groups together, as one ``MERGE``.

    An xclbin's form of a packing: the group configured once and its steps in a row
    dispatched once, back to back. A host step between two ends a run, and so does a
    step that would take the run past what one xclbin kernel carries: more host
    buffers than ``HOST_BUFFERS`` (a merged sequence passes each step's own), or a
    design that leaves its configuration unplaced, since one sequence keeps each shim
    end sending into the array in flight to its end (mlir-aie's ``ShimTransferSpans``),
    so its designs cannot take turns on a shim channel as a full ELF's separate
    sequences do.
    """
    if not packing.groups:
        return ()
    inside = {i for f in fused for i in f.steps}
    groups: list[tuple[str, ...] | None] = []
    designs: list[OperatorDesign] = []
    for i, step in enumerate(recording.steps):
        op = step.op.resolved(dev)
        designs.append(OperatorDesign(op))
        group = (
            None
            if i in inside or op.reference_only
            else packing.group_of(designs[i].name)
        )
        groups.append(group if group is not None and len(group) > 1 else None)
    hosted = [sum(not b.on_chip for b in s.op.buffers) for s in recording.steps]
    found: list[Fusion] = []
    # By the run's designs: each layer repeats the last one's.
    placed: dict[tuple[str, ...], bool] = {}
    lo = 0
    # Each design's first step in the run: a design's steps all run on its one array.
    firsts: dict[str, int] = {designs[0].name: 0} if designs else {}
    for hi in range(1, len(groups) + 1):
        if (
            hi < len(groups)
            and groups[hi] is not None
            and groups[hi] == groups[lo]
            and not recording.crosses_host(hi - 1, hi)
            and sum(hosted[lo : hi + 1]) <= HOST_BUFFERS
        ):
            if designs[hi].name in firsts:
                continue
            steps = (*firsts.values(), hi)
            key = tuple(designs[j].name for j in steps)
            if key not in placed:
                # Placed as a full ELF builds it: the same arrays and shim ends,
                # without the dispatch scalars an xclbin binds only at its build.
                placed[key] = (
                    fits(
                        {str(j): designs[j] for j in steps},
                        fusion=Fusion(FusionKind.MERGE, steps),
                    )
                    is None
                )
            if placed[key]:
                firsts[designs[hi].name] = hi
                continue
        if groups[lo] is not None and hi - lo > 1:
            found.append(Fusion(FusionKind.MERGE, tuple(range(lo, hi))))
        lo = hi
        firsts = {designs[hi].name: hi} if hi < len(designs) else {}
    return tuple(found)
